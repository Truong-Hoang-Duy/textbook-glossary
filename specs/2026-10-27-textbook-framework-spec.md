# Spec: Bài học nguyên văn (Tầng 1), Từ điển thuật ngữ (Tầng 2), Dữ liệu xuất (JSON)

> **Mã:** `SPEC-TEXTBOOK-01`, phiên bản 0.4, ngày 2026-10-27, trạng thái **nháp, chờ duyệt**
> **Phạm vi:** Quy tắc chung cho mọi môn và mọi lớp, **hiện chỉ áp dụng cho SGK**. Spec này là **lõi**; điểm riêng của từng môn (cấp mục, ngôn ngữ OCR, cột từ điển, công thức, phạm vi chép…) nằm trong **hồ sơ môn** `specs/profiles/<mon>.json` (mục 10).
> **Plan thí điểm:** [Sinh 12](../plans/2026-10-26-bio12-extraction-plan.md)
> **Quan hệ với tài liệu khác:** README tóm tắt quy tắc. Spec này, hồ sơ môn và các file trong `textbook/schema/` là chuẩn duy nhất về **định dạng**. Plan của từng bộ chỉ ghi việc cần làm và tiến độ.

---

## 1. Mục tiêu và giới hạn

**Mục tiêu**

- Giữ được mạch sư phạm và hình minh họa của từng bài (Tầng 1).
- Có từ điển Markdown **đúng định dạng mẫu `_Huong-dan/Từ điển Sinh học 12.md`** để giáo viên và agent tạo học liệu đọc trực tiếp (Tầng 2).
- JSON được **sinh hoàn toàn bằng script** từ `progress.json`, Tầng 1 và Tầng 2, theo `textbook/schema/unit.schema.json`. Không có bước nhập tay.

**Không thuộc phạm vi**

- Các sách khác ngoài SGK (SCD, SGV, SBT, tài liệu bồi dưỡng GV). Sẽ mở rộng sau, khi đó mới bổ sung quy tắc vào spec.
- Dùng nguồn ngoài bộ KNTT.
- Tích hợp với review-station hay hệ thống khác. Định dạng JSON được thiết kế độc lập; hệ thống nào dùng thì tự đọc theo schema.
- Đổi schema khi chưa hỏi người dùng.

## 2. Kiến trúc

```
sgk/khoi_<lop>/<unit>/SGK*.pdf           (sách quét, không có text layer)
        │  ocr_pages.py  → cache/ocr/<unit>/<pdf>/pNNNN.txt   (dữ liệu trung gian, chỉ để kiểm tra tự động)
        │  Claude đọc ẢNH trang, viết Markdown
        ▼
specs/profiles/<mon>.json               hồ sơ môn (profile.schema.json), mọi script đọc
progress.json                            cây mục lục (progress.schema.json)
TẦNG 1  <Kind>-NN-…/[<Kind>-NN-…/]<Mã>-….md  + img/ + figures.json
        │  thuật ngữ in đậm tại câu định nghĩa, mốc trang <!-- pdf:N -->
        ▼
TẦNG 2  Tu-dien-<Mon>-<lop>-<Kind>-N.md   (định dạng mẫu _Huong-dan)
        │  export_unit.py
        ▼
textbook/dataset/<unit>.json             (unit.schema.json)
```

Mỗi tầng chỉ được sinh từ tầng ngay trên nó. Phát hiện sai ở tầng dưới thì sửa ở tầng trên, rồi sinh lại.

## 3. `progress.json`: cây mục lục, số trang, tiến độ

Kiểm tra bằng `textbook/schema/progress.schema.json`.

### 3.1. Vì sao dùng cây đệ quy

Mỗi SGK KNTT chia mục lục theo một kiểu riêng (khảo sát 28 bộ lớp 10–12):

| Kiểu mục lục | Ví dụ |
|---|---|
| Chương → Bài | Toán, Vật lí, Hoá học, Công nghệ, Sinh 11 |
| Phần → Chương → Bài | Sinh 12, Địa lí 10, Sinh 10 |
| Phần → Bài | Địa lí 11, 12 |
| Chủ đề → Bài | Lịch sử, Tin học |
| Tập → Bài (+ "Ôn tập học kì" không số) | Ngữ văn |
| Unit → Lesson (đánh lại từ 1 mỗi Unit), xen Review | Tiếng Anh |
| Chủ đề / Phương án lựa chọn → mạch nội dung không số | Âm nhạc |

Ngoài ra còn các mục không đánh số ở đầu và cuối sách: Lời nói đầu, Hướng dẫn sử dụng sách, Mở đầu, Bảng tra cứu khái niệm/thuật ngữ, Bảng phiên âm, Glossary.

Vì vậy mục lục **không cố định tên cấp**. `toc` là một cây đệ quy sâu 1–3 cấp. Mỗi nút giữ đúng tiền tố và tên in trên sách, kèm `role` cho biết nút là nhóm, bài hay trang đầu/cuối.

### 3.2. Nút trong cây

| Khoá | Ý nghĩa |
|---|---|
| `id` | Mã nút, duy nhất trong bộ: mã loại + số 2 chữ số (`c01`, `cd01`, `b01`, `u01`), hoặc slug nếu không đánh số (`mo-dau`, `on-tap-hk1`). Nếu trùng trong bộ (ví dụ Lesson đánh lại từ 1 mỗi Unit) thì nối mã nút cha phía trước: `u01-l1` |
| `role` | `group` (nhóm chứa nút con), `lesson` (bài có nội dung, có file Tầng 1), `front_matter` / `back_matter` (trang đầu/cuối sách) |
| `kind` | Loại nút chuẩn hoá từ chữ in trên sách, xem bảng dưới |
| `label` | Tiền tố in trên sách, giữ nguyên cách viết: `Phần bốn`, `Chương 1`, `Chủ đề 3`, `Bài 12`, `Unit 2`, `Review 1`. `null` nếu không có |
| `number` | Số thứ tự dạng số nguyên (`bốn` → 4, `II` → 2). `null` nếu không đánh số |
| `title` | Tên in trên sách, **không gồm tiền tố**: `Di truyền học` |
| `dir`, `children` | Chỉ nút `group` có: thư mục Tầng 1 và danh sách nút con |
| `lesson_type`, `file`, `source_file`, `pdf_pages`, `printed_offset`, `status` | Chỉ nút không phải `group` có. `lesson_type` bắt buộc với `lesson`. `file` là `null` nếu trang đầu/cuối không chép (khi đó `status: skip`) |

Bảng `kind` và mã dùng cho `id`. Gặp loại mới thì thêm dòng vào bảng này; schema không cần sửa.

| Chữ in trên sách | `kind` | Mã `id` | Chữ in trên sách | `kind` | Mã `id` |
|---|---|---|---|---|---|
| Phần | `phan` | `p` | Bài | `bai` | `b` |
| Chương | `chuong` | `c` | Lesson | `lesson` | `l` |
| Chủ đề | `chu_de` | `cd` | Review | `review` | `r` |
| Tập | `tap` | `t` | Ôn tập (không số) | `on_tap` | slug |
| Unit | `unit` | `u` | Mạch nội dung (Âm nhạc) | `mach_noi_dung` | slug |
| Phương án lựa chọn | `phuong_an` | `pa` | Mở đầu, Lời nói đầu, Hướng dẫn, Bảng tra cứu… | `mo_dau`, `loi_noi_dau`, `huong_dan`, `bang_tra_cuu` | slug |
| Sơ đồ tóm tắt kiến thức chương (cuối chương, không có trong mục lục) | `so_do_tom_tat` | slug (`so-do-tom-tat-c01`) | Mục lục | `muc_luc` | slug |

### 3.3. Quy tắc

- Tên **chép đúng như in ở trang mở đầu** của nút, đọc từ ảnh. Trang mở đầu thường in hoa: viết lại chữ thường theo cách viết hoa của mục lục, tên riêng và kí hiệu giữ nguyên (Mendel, DNA).
- Trang có nội dung nhưng mục lục không ghi (ví dụ sơ đồ tóm tắt cuối chương) vẫn phải có nút riêng, để mọi trang nội dung đều thuộc một nút lá. Nếu mục lục của sách ghi khác (ví dụ Sinh 12: mục lục ghi "Chương I", "Bài 5. Công nghệ di truyền" nhưng trang đầu ghi "Chương 1", "Công nghệ gene") thì theo trang đầu, và ghi chỗ khác biệt vào `notes` của `progress.json`.
- Số bài giữ đúng như sách. Sách đánh liên tục (Sinh 12: Chương 2 bắt đầu từ Bài 7) thì giữ liên tục.
- Bài "Ôn tập chương" có số (Hoá 11: Bài 3) là `kind: bai`, `lesson_type: on_tap`. Không có số thì là `kind: on_tap`.
- Tên hiển thị đầy đủ = `label + ". " + title` (hoặc chỉ `title` nếu `label` là `null`), ví dụ `Chủ đề 1. Cách mạng tư sản và sự phát triển của chủ nghĩa tư bản`.
- `printed_offset`: `trang in = trang PDF − printed_offset`. Nút nào lệch khác với giá trị của file thì ghi riêng ở nút đó.
- `status`: `pending → layer1 → layer2 → verified`, hoặc `skip` cho trang đầu/cuối không chép.
- **Thư mục Tầng 1** đi theo cây: mỗi nút `group` một thư mục `<Kind>-<NN>-<slug>` (`Phan-04-Di-truyen-hoc`, `Chu-de-01-Cach-mang-tu-san`, `Unit-01-Life-stories`, `Tap-1`). Nút lá là một file `<Mã>-<slug>.md` (`B01-DNA-va-co-che-tai-ban-DNA.md`, `U01-L1-Getting-started.md`). Trang đầu/cuối nằm ở thư mục gốc của bộ. Slug bỏ dấu, giữ hoa/thường, nối bằng `-`, dài tối đa 50 ký tự và cắt ở ranh giới từ (`slugify()` trong `_common.py`), để đường dẫn không vượt giới hạn 260 ký tự của Windows.

### 3.4. Ví dụ

Sinh 12 (Phần → Chương → Bài):

```json
{
  "unit": "sinh_12", "subject": "sinh", "subject_name": "Sinh học", "grade": 12,
  "files": [{ "file": "SGK SINH HOC 12 - KNTT.pdf", "volume": null, "page_count": 199, "printed_offset": 2 }],
  "toc": [
    { "id": "p04", "role": "group", "kind": "phan", "label": "Phần bốn", "number": 4, "title": "Di truyền học",
      "dir": "Phan-04-Di-truyen-hoc", "children": [
        { "id": "c01", "role": "group", "kind": "chuong", "label": "Chương 1", "number": 1, "title": "Di truyền phân tử",
          "dir": "Chuong-01-Di-truyen-phan-tu", "children": [
            { "id": "b01", "role": "lesson", "kind": "bai", "label": "Bài 1", "number": 1,
              "title": "DNA và cơ chế tái bản DNA", "lesson_type": "ly_thuyet",
              "file": "B01-DNA-va-co-che-tai-ban-DNA.md", "source_file": "SGK SINH HOC 12 - KNTT.pdf",
              "pdf_pages": [7, 10], "status": "pending" } ] } ] }
  ],
  "notes": ["Mục lục ghi \"Chương I\", \"Bài 5. Công nghệ di truyền\"; trang đầu ghi \"Chương 1\", \"Công nghệ gene\" — theo trang đầu."],
  "audits": [],
  "last_session_note": ""
}
```

Lịch sử 11 (Chủ đề → Bài, có trang đầu/cuối), chỉ ghi phần `toc`:

```json
[
  { "id": "loi-noi-dau", "role": "front_matter", "kind": "loi_noi_dau", "label": null, "number": null,
    "title": "Lời nói đầu", "file": null, "source_file": "…", "pdf_pages": [4, 4], "status": "skip" },
  { "id": "cd01", "role": "group", "kind": "chu_de", "label": "Chủ đề 1", "number": 1,
    "title": "Cách mạng tư sản và sự phát triển của chủ nghĩa tư bản", "dir": "Chu-de-01-Cach-mang-tu-san",
    "children": [ { "id": "b01", "role": "lesson", "kind": "bai", "label": "Bài 1", "number": 1, "…": "…" } ] },
  { "id": "bang-tra-cuu", "role": "back_matter", "kind": "bang_tra_cuu", "label": null, "number": null,
    "title": "Bảng tra cứu khái niệm, thuật ngữ", "file": "Bang-tra-cuu.md", "…": "…" }
]
```

Tiếng Anh: `Unit 1` (`u01`) chứa `Lesson 1` (`u01-l1`); `Review 1` (`r1`) là nút lá ở cấp cao nhất.

### 3.5. Ghi chú và kết quả kiểm tra

Mỗi bộ chỉ có `progress.json` làm hồ sơ, không có file mô tả riêng.

- `notes`: các điểm đặc thù của sách, mỗi ý một chuỗi. Ví dụ: chỗ mục lục khác trang mở đầu, cách ánh xạ heading riêng, phần cấu trúc lạ.
- `audits`: mỗi đợt kiểm tra mẫu (cổng 4) thêm một phần tử `{date, scope, terms, sample, errors, fixed, note}`. `scope` là danh sách `id` nút trong `toc` đã kiểm tra.
- `last_session_note`: việc đang dở ở cuối phiên gần nhất.

## 4. Tầng 1: Bài học nguyên văn

### 4.1. Frontmatter

```yaml
---
unit: sinh_12
lesson_id: b01                                   # id nút trong progress.json
toc_path:                                        # tên hiển thị đầy đủ từ gốc tới bài, đúng progress.json
  - "Phần bốn. Di truyền học"
  - "Chương 1. Di truyền phân tử"
  - "Bài 1. DNA và cơ chế tái bản DNA"
source_file: "SGK SINH HOC 12 - KNTT.pdf"
pdf_pages: [7, 10]
lesson_type: ly_thuyet       # ly_thuyet | thuc_hanh | du_an | on_tap
status: draft                # draft | verified (do check_lesson.py xác nhận)
---
```

### 4.2. Khung heading

Heading cố định để script nhận ra từng khối. Khối nào sách không có thì bỏ.

| Heading | Bắt buộc | Xuất ra JSON |
|---|---|---|
| `# <TÊN HIỂN THỊ IN HOA>` (ví dụ `# BÀI 1: DNA VÀ CƠ CHẾ TÁI BẢN DNA`) | Có | |
| `## 🎯 <nhãn khung đúng như sách>` | Có, nếu sách có khung | `lesson.objectives` |
| `## 🔤 Thuật ngữ` | Chỉ môn Toán | `lesson.key_terms` |
| `## 🔴 Mở đầu` | | |
| Các cấp mục đánh số **theo hồ sơ môn** (mặc định `## I. …` / `### 1. …` / `**a) …**`) | Có | `term.location.section` (`I`, `II.1`, `III.2.a`; Toán: `1`, `1.a`) |
| Heading thêm của hồ sơ (`extra_headings`, ví dụ Ngữ văn `## Đọc`, Tiếng Anh `## GETTING STARTED`) | | Coi như hộp: `section` là `null` |
| `## ❓ <tên hộp đúng như sách>` | | |
| `## 💡 <tên hộp đúng như sách>` | | |
| `## 📌 Kiến thức cốt lõi` | | |
| `## ✏️ Luyện tập và vận dụng` | | |
| `## 📷 Danh sách hình trong bài` | Có, nếu bài có hình | `lesson.figures` |

SGK không có khung yêu cầu cần đạt (ví dụ Vật lí, Địa lí, Âm nhạc, Tiếng Anh) thì bỏ khối 🎯; khi đó `objectives` là `null`. `check_lesson.py` chỉ chấp nhận heading là hộp emoji, một cấp mục, hoặc một `extra_headings` của hồ sơ môn. Môn có heading khác thì **sửa hồ sơ môn**, không sửa spec và không ghi vào `notes`.

Bài thực hành có thể in yêu cầu cần đạt thành mục La Mã (`## I. YÊU CẦU CẦN ĐẠT`) thay cho khung đầu bài: chép đúng như sách, khi xuất JSON thì lấy mục này làm `objectives`.

Trang in xoay ngang (sơ đồ tóm tắt cuối chương): khai báo `"rotate": 90` trong `figures.json`, chạy lại OCR trang đó với `ocr_pages.py --force --psm 1`, và chép các nhánh sơ đồ thành danh sách lồng nhau dưới ảnh.

### 4.3. Quy ước bắt buộc

- **Nguyên văn:** chép đúng câu chữ, chính tả và cách viết của sách. Không chuẩn hóa ở Tầng 1. Phạm vi chép theo hồ sơ `verbatim_scope`: `toan_bai` chép cả bài; `ly_thuyet` chép phần lí thuyết/tri thức, văn bản đọc chỉ ghi tên, tác giả, trang; `cho_quyet_dinh` thì **chưa được làm Tầng 1** (`check_lesson.py` dừng).
- **Mốc trang:** đặt `<!-- pdf:N -->` ngay trước nội dung bắt đầu trang PDF N. Mốc đầu tiên phải trùng `pdf_pages[0]`.
- **In đậm:** giữ nguyên chỗ sách in đậm (nhãn đoạn như `**Khởi đầu:**`, thuật ngữ như `**tiền mRNA**`). Ngoài ra in đậm thuật ngữ **tại câu sách định nghĩa nó**, mỗi thuật ngữ một lần trong cả bộ; không in đậm những chỗ chỉ nhắc lại. Từ điển (Tầng 2) chỉ lấy thuật ngữ từ chỗ in đậm.
- **Công thức và kí hiệu:** dùng LaTeX `$…$` hoặc `$$…$$`.
- **Nhãn mô tả:** thuật ngữ sách **không có câu định nghĩa nhưng có câu mô tả** được gắn nhãn `<!-- term: <tên thuật ngữ> -->` ở dòng ngay trước mỗi đoạn mô tả nó (có thể nhiều đoạn, ở các bài khác nhau trong cùng nhóm). Tên trong nhãn viết đúng chính tả (kể cả khi sách in sai).
  - **Gắn nhãn khi** trong đoạn có ít nhất một câu mà thuật ngữ là chủ thể và câu nêu một trong các ý: chức năng, vai trò ("có chức năng", "dùng để", "làm khuôn…"); thành phần, cấu tạo ("gồm", "cấu tạo từ"); nguồn gốc, cách tạo ra ("do … quy định", "do … đề xuất", "được gọi là"); đặc điểm phân biệt ("có tính…"); cơ chế hoạt động.
  - **Không gắn nhãn khi** thuật ngữ chỉ có trong tiêu đề, câu hỏi, bài tập, nhãn hình, hoặc chỉ được nêu tên trong một ví dụ hay danh sách liệt kê.
  - Không gắn nhãn cho thuật ngữ đã có chỗ in đậm.
- **Lỗi in của sách** (thiếu chữ, sai chính tả, đánh số mục trùng) giữ nguyên, không sửa.
- **Chú thích chân trang** (ví dụ nguồn hình `(*)`) chép thành dòng `> (\*) …` ở cuối phần nội dung của trang đó, trước mốc trang kế tiếp.
- **Bảng** trong sách chép thành bảng Markdown. Bảng phức tạp (ví dụ Bảng mã di truyền) vừa cắt thành hình vừa chép thành bảng.
- **Đoạn bị `check_lesson.py` gắn cờ** (khớp OCR dưới ngưỡng) phải đối chiếu lại ảnh trang. Nếu đúng (OCR đọc sai), thêm ngay sau đoạn một dòng `<!-- ocr-ok: <lý do> -->`. Nhãn hộp có emoji (spec 4.2) không đem so OCR.
- **Khung kiến thức** (hồ sơ `definition_boxes`, ví dụ Toán "Định nghĩa", "Định lí"): chép thành trích dẫn `> **<nhãn>.** …`, in đậm thuật ngữ được định nghĩa bên trong khung. Định lí, tính chất, công thức không có tên riêng thì đặt tên dòng từ điển theo tên sách gọi (ví dụ "Định lí côsin"); sách không đặt tên thì không tạo dòng.
- **Công thức** theo hồ sơ `formula`: `latex` dùng `$…$`; `latex_mhchem` dùng thêm `\ce{…}` cho công thức và phương trình hoá học. Công thức chép **từng kí tự** theo ảnh (phép so OCR bỏ qua LaTeX nên không bắt được sai sót trong công thức; cổng 4 kiểm tra riêng).
- **Mã lệnh** (hồ sơ `code_blocks: true`): chép trong khối ```` ``` ```` kèm tên ngôn ngữ; khối mã không đem so OCR.
- **Quy ước riêng của môn** (ví dụ Sinh: tên gene in nghiêng) nằm trong `conventions` của hồ sơ môn; ở Tầng 1 vẫn viết giống như sách in.

### 4.4. Hình minh họa

- Sách là ảnh quét, không có hình nhúng riêng, nên phải **cắt theo khung (bbox)** từ ảnh trang render ở 300 DPI.
- `figures.json` đặt trong thư mục nhóm chứa bài: `{ "<mã hình>": {"pdf_page": N, "bbox": [x0, y0, x1, y1]} }`, đơn vị là point của PDF. `crop_figures.py` đọc file này, nên cắt lại lúc nào cũng ra cùng kết quả.
- **Ảnh cắt gồm cả chú thích của hình**, để ảnh đứng riêng vẫn đọc được:
  - Hình: mọi nét vẽ, nhãn, mũi tên, kí hiệu đầu mạch (3′, 5′), chú giải (a)/(b) **và dòng chú thích "Hình x.y. …" ngay dưới** (đủ mọi dòng nếu chú thích dài).
  - Bảng: **tiêu đề "Bảng x.y. …" phía trên**, thân bảng và khối "Chú thích: …" ngay dưới bảng.
  - **Không gồm** chữ của đoạn văn bên cạnh hay phía trên/dưới, và chú thích chân trang "(\*) Nguồn hình: …" ở cuối trang (chép thành dòng chữ theo mục 4.3).
- Trong bài vẫn chép chú thích thành chữ ngay dưới ảnh (để tìm kiếm và kiểm tra OCR), dù ảnh đã có chú thích.
- **Cách đo và kiểm tra** (bắt buộc theo thứ tự):
  1. `crop_figures.py <unit> --grid <trang>` vẽ lưới 10 pt ở 100 dpi vào `cache/figures/<unit>/grid_pNNN.png`. Đọc bbox trên lưới này, không ước lượng trên ảnh độ phân giải thấp.
  2. `crop_figures.py <unit> <thư mục nhóm>` cắt với khung = bbox + lề 4 pt và kiểm tra **cả bốn cạnh khung phải nằm trên nền trắng**. Cạnh nào đi qua nét vẽ (hình bị cắt mất, hoặc khung chạm chú thích/chữ bên cạnh) thì script báo lỗi; sửa bbox rồi chạy lại đến khi hết lỗi.
  3. Xem ảnh kiểm tra `cache/figures/<unit>/<mã>.png` (toàn trang, khung đỏ) **ở độ phân giải đủ đọc nhãn**, không chỉ xem ảnh đã cắt thu nhỏ. Kiểm tra hai điều: không mất nét hay nhãn nào ở mép, và **chú thích (hoặc tiêu đề bảng) nằm trọn trong khung**.
- Không lấy hình từ nguồn khác (kể cả `_SGK-Nguyen-ban`): hình phải cắt từ đúng file PDF trong `sgk/`, vì bản khác có thể khác nhãn và chú thích.
- Tên file hình: `H<lop>-<mon>-<id bài>-<stt>.png`, ví dụ `H12-sinh-b01-01.png`, `H12-tieng_anh-u01-l1-01.png`.
- Chèn hình vào bài: `![Hình 1.1](img/H12-sinh-b01-01.png)`, dòng ngay sau là chú thích **nguyên văn** của sách.
- Bảng `📷` có các cột: mã hình, trang PDF, vị trí trong bài, chú thích gốc.

## 5. Tầng 2: Từ điển thuật ngữ

Mỗi **nhóm chứa bài trực tiếp** (Chương, Chủ đề, Unit, Tập…, tuỳ sách) một file `Tu-dien-<Mon>-<lop>-<Kind>-<N>.md`, ví dụ `Tu-dien-Sinh-hoc-12-Chuong-1.md`, `Tu-dien-Lich-su-11-Chu-de-1.md`, `Tu-dien-Tieng-Anh-12-Unit-1.md`. Nút lá ở cấp cao nhất (Review, Mở đầu…) gộp vào từ điển của nhóm đứng ngay trước; nếu đứng đầu sách thì gộp vào nhóm ngay sau. Định dạng **giống mẫu `_Huong-dan/Từ điển Sinh học 12.md`**, chỉ thêm những ràng buộc cần thiết để script đọc được và để chống bịa.

### 5.1. Cấu trúc

1. **Frontmatter**: dùng đúng các khoá của mẫu.

   ```yaml
   ---
   name: tu-dien-sinh-hoc-12-chuong-1
   description: Từ điển thuật ngữ Sinh học 12, Phần bốn Di truyền học, Chương 1 Di truyền phân tử (Bài 1–6). Tham chiếu chuẩn hoá thuật ngữ và bối cảnh cho mọi học liệu. Đọc trước khi tạo hoặc sửa bất kỳ học liệu nào.
   loai_hoc_lieu: tu-dien-thuat-ngu
   mon: Sinh học
   lop: 12
   phan: "Phần bốn. Di truyền học"                # tên nút cấp trên của nhóm; bỏ khoá nếu không có
   chuong: "Chương 1. Di truyền phân tử"          # tên nhóm chứa bài, dù sách gọi là Chương, Chủ đề, Unit hay Tập
   bai_so: "1-6"
   nguon: "SGK SINH HOC 12 - KNTT.pdf, Bài 1–6 (Tầng 1 trong textbook/khoi_12/sinh_12/)"
   ngay_tao: 2026-10-27
   ngay_cap_nhat: 2026-10-27
   trang_thai: draft                              # draft | verified
   ---
   ```

2. **Tiêu đề** `# Từ điển thuật ngữ <Môn> <lớp> — <Phần> (<Chương>, Bài x–y)`, sau đó một đoạn mô tả ngắn.
3. **`## Quy ước sử dụng`**: các gạch đầu dòng về viết tắt và cách viết thống nhất của môn. Đây là nơi duy nhất được chuẩn hóa cách viết.
4. **`## Thuật ngữ dùng chung`** (tùy chọn), sau đó mỗi bài một mục **`## <label>: <title>`** lấy từ `progress.json` (ví dụ `## Bài 1: DNA và cơ chế tái bản DNA`, `## Lesson 1: Getting started`; bài không có `label` thì `## <title>`). Script khớp mục với bài theo `label` và `title`.
5. **Bảng 4 cột**, tiêu đề cột theo hồ sơ `dictionary_columns` (mặc định `| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |`; Tiếng Anh: `| Từ vựng | Loại từ, phiên âm | Nghĩa tiếng Việt | Bối cảnh sử dụng |`)
6. **`## Đã xét, không tạo mục`** (mục 5.4)
7. **`## Ghi chú nguồn cần kiểm tra`**

### 5.2. Quy tắc từng cột

- **Thuật ngữ:** tên chính (hoặc tên trong ngoặc) phải trùng với một cụm in đậm ở Tầng 1. Tiêu đề in đậm dạng `**a) mRNA**` cũng tính; khi đó Giải nghĩa được so với các đoạn ngay sau tiêu đề.
- **Thuật ngữ mô tả:** sách không định nghĩa nhưng có mô tả (nhãn `<!-- term: … -->` ở Tầng 1, mục 4.3). Cột Bối cảnh **bắt đầu bằng `[mô tả] `**; Giải nghĩa **ghép nguyên văn** các câu trong các đoạn gắn nhãn, chỉ được lược bớt, không thêm ý, và phải khớp phần ghép các đoạn đó (bigram ≥ 0.65). Khi ra câu hỏi không hỏi "định nghĩa" của các thuật ngữ này.
- **Ba loại dòng:** có định nghĩa (chỗ in đậm) → `in_source`; mô tả (`[mô tả]`) → `described`; Ngoài nguồn → `out_of_source`. Thuật ngữ không có trong SGK (ví dụ helicase, primase) không được vào từ điển dưới bất kì loại nào.
- **Bài không có thuật ngữ mới** (ví dụ bài thực hành) vẫn có mục `## Bài n: …`, ghi một câu thay cho bảng. Phần trong ngoặc là tên viết tắt hoặc tên khác, ví dụ `Điểm khởi đầu sao chép (Ori)`.
- **Tiếng Anh:** có thể để trống. Không đưa vào học liệu cho học sinh nếu sách không ghi.
- **Giải nghĩa:** bám sát câu in đậm ở Tầng 1. Được rút gọn nhưng không diễn giải lại, không thêm ý.
- **Bối cảnh sử dụng:** khi nào dùng thuật ngữ này và phân biệt với nghĩa khác. Nên ghi bài và mục.
- **Ngoài nguồn:** thuật ngữ được dùng trong phạm vi từ điển nhưng không có câu định nghĩa nào trong phạm vi đó. Ô Giải nghĩa ghi **đúng mẫu sau** và không viết thêm gì:
  `Ngoài nguồn — chưa định nghĩa trong <phạm vi>. Xem: <bài KNTT có định nghĩa, kèm trang PDF | chưa xác định>`
- Số mục Ngoài nguồn và số ghi chú tùy theo nội dung từng chương, không có chỉ tiêu cố định.

### 5.3. Đặt tên, tách gộp, lỗi in

- **Tên chính** theo cách sách gọi (ví dụ "Enzyme nối", không phải "Enzyme ligase"). Tên khác mà sách cũng dùng, tên viết tắt, tên trong từ điển mẫu (nếu sách có dùng) đưa vào ngoặc, cách nhau bằng `;`: `Protein ức chế (lacI; protein ức chế lacI)`.
- **Mỗi khái niệm một dòng.** Sách in đậm riêng từng cụm (vị trí A, P, E) thì tách dòng. Hai thuật ngữ sách mô tả chung một câu (miRNA, siRNA) thì hai dòng, giải nghĩa giống nhau và cột Bối cảnh nói rõ là dùng chung.
- **Lỗi in trong tên thuật ngữ** (ví dụ sách in "β–galatosidase"): Tầng 1 giữ nguyên; tên dòng, nhãn mô tả và Giải nghĩa viết đúng; thêm một ghi chú nguồn đã đóng nêu cách in của sách.

### 5.4. Mục "Đã xét, không tạo mục"

Đặt ngay trước mục Ghi chú nguồn. Mỗi dòng có dạng `- <thuật ngữ> — <lý do>[: <giải thích ngắn>]`, với lý do là một trong các giá trị:

| Lý do | Dùng khi |
|---|---|
| `không có trong SGK` | Thuật ngữ không xuất hiện trong sách (ví dụ có trong từ điển mẫu do giáo viên bổ sung) |
| `chỉ nhắc tên` | Có trong sách nhưng không có câu nào định nghĩa hay mô tả (tiêu chí ở 4.3) |
| `chỉ có trong ví dụ, bài tập` | Chỉ xuất hiện trong ví dụ, câu hỏi, bài tập |
| `tên khác của <dòng>` | Cùng khái niệm với một dòng đã có nhưng sách không dùng tên này |
| `gộp vào <dòng>` | Là một ý đã nằm trong giải nghĩa của dòng khác |
| `tiêu đề, không phải thuật ngữ` | Tên bài, tên mục |

Mục này cho biết thuật ngữ nào **loại có chủ ý**, phân biệt với thuật ngữ **bị bỏ sót**.

### 5.5. Độ phủ (`check_coverage.py`)

Script gom ứng viên của nhóm: cụm in đậm trong câu và nhãn mô tả ở Tầng 1; cụm ngay sau "được gọi là / gọi là / còn được gọi là" (trừ trong câu hỏi, bài tập); tên thuật ngữ trong từ điển mẫu `_Huong-dan/Từ điển <Môn> <lớp>.md` (nếu có) ở các bài của nhóm. **Mỗi ứng viên phải trùng tên chính hoặc tên trong ngoặc của một dòng bảng, hoặc có dòng trong mục "Đã xét".** Ứng viên do script gom nhầm (cụm không phải thuật ngữ) cũng ghi vào "Đã xét" với lý do phù hợp.

### 5.6. Ghi chú nguồn cần kiểm tra

Giữ dạng danh sách đánh số như mẫu. Thêm trạng thái và vị trí ở đầu dòng:

```
1. [mở] Bài 2 (mục III.4.a, pdf:17) — Thuật ngữ: Codon — <vấn đề>
2. [đóng] Bài 3 (mục I.1, pdf:21) — Thuật ngữ: — — <vấn đề> → <kết luận> (2026-10-28)
```

Chỉ đóng ghi chú sau khi đã đối chiếu với ảnh trang. Không đề nghị đối chiếu với nguồn ngoài SGK (văn bản luật, chương trình, sách bộ khác). Từ điển chỉ được đổi sang `trang_thai: verified` khi không còn ghi chú nào `mở`.

### 5.7. Bảng thuật ngữ cuối sách

Nhiều SGK có trang giải thích thuật ngữ ở cuối sách ("Giải thích một số thuật ngữ trong sách", "Bảng tra cứu khái niệm, thuật ngữ", "Glossary"). Đây là nút `back_matter`, `kind: bang_tra_cuu`, **có file Tầng 1** (không `skip`).

- Tầng 1 chép nguyên văn, mỗi mục in đậm tên thuật ngữ: `**Allele**: …`.
- Định nghĩa trong bài học vẫn là nguồn chính. Thuật ngữ **chỉ** được định nghĩa ở bảng cuối sách thì vẫn là `in_source`: `check_dict.py` và `export_unit.py` tìm chỗ in đậm cả trong file bảng này, và `location.lesson_id` là `id` của nút bảng.
- Dòng từ điển đặt ở mục bài **dùng** thuật ngữ đó; nếu nhiều bài cùng dùng thì đặt ở "Thuật ngữ dùng chung".
- Cổng 2b: mỗi mục của bảng phải có trong một từ điển nào đó của bộ (bảng hoặc "Đã xét"). Khi bộ còn nhóm chưa có từ điển, script chỉ cảnh báo.
- Mục Ngoài nguồn của một chương ghi `Xem:` trỏ tới mục tương ứng trong bảng cuối sách nếu có.

## 6. Xuất JSON (`export_unit.py`)

Định dạng đích: `textbook/schema/unit.schema.json` (phiên bản `2.3`). Gồm 6 khối:

| Khối | Lấy từ | Nội dung |
|---|---|---|
| `meta` | `progress.json`, hồ sơ môn và script đếm | `schema_version`, `unit`, `profile`, `subject`, `subject_name`, `grade`, `generated_at`, `counts` (bài, thuật ngữ, Ngoài nguồn, ghi chú đang mở) |
| `source` | `progress.json` → `files` | Loại sách (`sgk`), bộ sách, NXB, danh sách file PDF kèm tập, số trang, độ lệch trang |
| `toc` | `progress.json` + Tầng 1 | Cây mục lục như mục 3 (bỏ `dir`). Nút lá có thêm `printed_pages`; nút `lesson` có thêm `objectives` (khối 🎯: `label`, `items`, `pdf_page`), `key_terms` (khối 🔤), `figures` (bảng 📷) |
| `dictionaries` | Frontmatter và mục Quy ước của từng từ điển | `file`, `name`, `title`, `group_id` (nút nhóm mà từ điển phủ), `lesson_ids`, `conventions`, `status`, `created`, `updated` |
| `terms` | Mỗi dòng bảng 4 cột | Xem bảng dưới |
| `source_notes` | Mục Ghi chú nguồn | `id` (`<name>#<số>`), `status` (`open`/`closed`), `lesson_id`, `section`, `pdf_page`, `term_ids`, `issue`, `resolution`, `resolved_on` |

Các khoá của `terms`:

| Khoá | Lấy từ | Ghi chú |
|---|---|---|
| `id` | Tên chính | `<unit, _ đổi thành ->-<slug không dấu>`; trùng thì thêm `-<lesson_id>` |
| `term`, `aliases` | Cột Thuật ngữ | `term` là phần ngoài ngoặc, `aliases` là phần trong ngoặc |
| `english`, `notation` | Cột 2 | Hồ sơ `dictionary_columns.keys[1]` chọn khoá nhận cột 2 (mặc định `english`; Tiếng Anh: `notation` = loại từ, phiên âm). Khoá còn lại là `null` |
| `meaning` | Cột Giải nghĩa | `null` nếu là dòng Ngoài nguồn |
| `usage_context` | Cột Bối cảnh sử dụng | |
| `scope` | Vị trí dòng trong từ điển | `shared` (mục Thuật ngữ dùng chung) hoặc `lesson` |
| `source_status` | Cột Giải nghĩa, Bối cảnh | `out_of_source` nếu Giải nghĩa bắt đầu bằng "Ngoài nguồn"; `described` nếu Bối cảnh bắt đầu bằng `[mô tả] ` (tiền tố được bỏ khỏi `usage_context`); còn lại `in_source` |
| `reference` | Phần "Xem: …" của dòng Ngoài nguồn | Các dòng khác là `null` |
| `location` | Chỗ in đậm (hoặc đoạn gắn nhãn đầu tiên, nếu `described`) ở Tầng 1 | `lesson_id`, `section` (tính từ heading), `pdf_page` (mốc gần nhất phía trước), `printed_page`. Dòng Ngoài nguồn là `null` |
| `dictionary` | Tên file từ điển | |
| `note_ids` | Ghi chú `mở` nhắc tên thuật ngữ | |

Schema tự kiểm tra các ràng buộc chống bịa: dòng `in_source` và `described` bắt buộc có `meaning` và `location`; dòng `out_of_source` bắt buộc có `meaning` và `location` là `null`; ghi chú `closed` bắt buộc có `resolution` và `resolved_on`.

**Báo lỗi và dừng, không đoán,** khi gặp một trong các trường hợp: không tìm thấy chỗ in đậm của thuật ngữ `in_source`, có hai `id` giống nhau, tên mục bài không khớp `progress.json`, hoặc JSON không hợp lệ theo schema.

## 7. Cổng chất lượng

| # | Cổng | Đạt khi |
|---|---|---|
| 0 | `progress.json` | Hợp lệ theo `progress.schema.json`; `id` không trùng; tên đã đối chiếu ảnh |
| 1 | `check_lesson.py` | Heading đúng hồ sơ môn; frontmatter đủ và khớp `progress.json`; mốc trang tăng dần và nằm trong `pdf_pages`; bigram có dấu giữa **từng đoạn** và OCR trang tương ứng ≥ 0.65 (đoạn bị gắn cờ thì đối chiếu ảnh); mọi hình trong `figures.json` có file và có dòng trong bảng 📷 |
| 2 | `check_dict.py` | Đúng cấu trúc mục 5.1; mọi thuật ngữ `in_source` có chỗ in đậm ở Tầng 1; bigram giữa Giải nghĩa và đoạn chứa chỗ in đậm ≥ 0.65; ô Ngoài nguồn đúng mẫu; mọi ghi chú đúng định dạng mục 5.6 |
| 2b | `check_coverage.py` | Mọi ứng viên thuật ngữ của nhóm đều có dòng trong bảng hoặc trong mục "Đã xét, không tạo mục" (mục 5.5) |
| 3 | `export_unit.py` | 0 lỗi theo `unit.schema.json`, 0 `id` trùng |
| 4 | Kiểm tra mẫu | 20–30 mục, đối chiếu ảnh trang, sai ≤ 5% (mục tiêu 0%), ghi một phần tử vào `audits` của `progress.json`. Mẫu phải có các nhóm trong hồ sơ `audit_focus`: `cong_thuc` (ít nhất 1/3 mẫu là mục có công thức, đối chiếu **từng kí tự** với ảnh), `mo_ta` (có mục `described`), `hinh` (có mục đặt cạnh hình) |

## 8. Các quyết định đã chốt

| # | Câu hỏi | Quyết định (2026-10-27) |
|---|---|---|
| Q1 | Repo có được đẩy lên remote công khai không? | **Được.** Tầng 1 và `img/` được đưa vào git như các file khác |
| Q2 | Đặt tên "Phần" theo sách hay theo hệ riêng? | **Theo sách** (`Phần bốn` → `Phan-04`), xem mục 3.3 |
| Q5 | Thuật ngữ sách có mô tả nhưng không định nghĩa (DNA polymerase, tái bản DNA…) có vào từ điển không? | **Có**, loại `described` (phương án A, 2026-10-27), xem mục 4.3, 5.2 |
| Q6 | Làm sao để không bỏ sót thuật ngữ và tiêu chí chọn nhất quán giữa người làm? | Tiêu chí mô tả cụ thể (4.3), quy tắc tên (5.3), mục "Đã xét" (5.4), cổng độ phủ 2b (5.5) — phương án A, 2026-10-27 |
| Q7 | Spec có đủ cho mọi môn không? | Spec lõi + **hồ sơ môn** (`specs/profiles/`, mục 10) — phương án A, 2026-10-27 |
| Q8 | Ngữ văn có chép nguyên văn toàn bộ văn bản đọc không? | **Chờ người dùng chốt.** Hồ sơ `ngu_van` để `verbatim_scope: cho_quyet_dinh`, chưa được làm Tầng 1 |
| Q4 | Mỗi sách chia mục lục một kiểu (Phần/Chương/Chủ đề/Unit…) | **Cây đệ quy**, giữ đúng tiền tố và tên in trên sách, không cố định tên cấp (mục 3) |
| Q3 | Từ điển có thêm cột `Loại` không? | **Không.** Từ điển giữ đúng định dạng mẫu `_Huong-dan` (4 cột). JSON bỏ các khoá `type`, `notation`, `related_terms` |

## 9. Công cụ (`textbook/scripts/`)

| Script | Việc |
|---|---|
| `_common.py` | Đường dẫn, đọc `progress.json`, **nạp hồ sơ môn** (`load_profile`), tách token có dấu, bigram, đọc cache OCR, kiểm tra schema |
| `ocr_pages.py` | Render trang và OCR bằng tesseract (`textbook/tessdata/`, ngôn ngữ theo hồ sơ `ocr_lang`), ghi `cache/ocr/<unit>/<pdf>/pNNNN.txt` ở gốc dự án. Cache là dữ liệu trung gian, không thuộc kết quả, không chép vào Tầng 1; xóa được và tạo lại bằng script |
| `crop_figures.py` | `--grid` (kèm `--file` khi SGK nhiều tập): vẽ lưới đo bbox. Mặc định: đọc `figures.json`, cắt 300 DPI, báo lỗi cạnh khung đi qua nét vẽ, ghi ảnh kiểm tra vào `cache/figures/` |
| `check_lesson.py` | Cổng 0 và cổng 1 |
| `check_dict.py` | Cổng 2 |
| `check_coverage.py` | Cổng 2b |
| `export_unit.py` | Cổng 3, ghi `textbook/dataset/<unit>.json` (kiểm tra bằng `jsonschema`) |

Nội dung Tầng 1 và Tầng 2 do **Claude đọc ảnh trang rồi viết**. Script chỉ cắt hình, kiểm tra và chuyển đổi.

## 10. Hồ sơ môn (`specs/profiles/`)

Mỗi môn một file `specs/profiles/<mon>.json`, kiểm tra bằng `textbook/schema/profile.schema.json`. `_default.json` chứa giá trị mặc định (lấy từ Sinh 12); hồ sơ môn chỉ ghi các khoá khác mặc định. Script tìm hồ sơ có `subjects` chứa mã môn của bộ (phần trước số lớp: `toan_10` → `toan`); không có thì dùng `_default`.

| Khoá | Ý nghĩa | Dùng ở |
|---|---|---|
| `status`, `verified_on` | `da_kiem_chung` (đã chạy trọn quy trình trên PDF thật) hoặc `chua_khao_sat` | Cổng 1 cảnh báo khi chưa kiểm chứng |
| `ocr_lang` | Ngôn ngữ tesseract (`vie`, `eng+vie`) | `ocr_pages.py` |
| `section_levels` | Các cấp mục đánh số: tiền tố Markdown + regex bắt số mục | Cổng 1, `section` khi xuất |
| `extra_headings` | Heading khác được phép (Ngữ văn, Tiếng Anh) | Cổng 1 |
| `definition_boxes` | Nhãn khung kiến thức (Toán, Lí) | Tầng 1 (mục 4.3) |
| `dictionary_columns` | Tiêu đề 4 cột và khoá JSON của từng cột | Cổng 2, 2b, 3 |
| `formula`, `code_blocks` | Quy ước công thức, mã lệnh | Tầng 1, cổng 1 |
| `verbatim_scope` | Phạm vi chép nguyên văn | Cổng 1 dừng nếu `cho_quyet_dinh` |
| `template` | Từ điển mẫu cho cổng 2b (có `{grade}`), hoặc `null` | Cổng 2b |
| `audit_focus` | Nhóm bắt buộc trong mẫu cổng 4 | Cổng 4 |
| `conventions` | Quy ước viết riêng của môn, chép vào "Quy ước sử dụng" của từ điển | Tầng 2 |
| `open_questions` | Điểm cần khảo sát hoặc cần người dùng chốt | Giai đoạn 1 |

**Quy trình cho môn mới** (Giai đoạn 1 trong CLAUDE.md):

1. Mở hồ sơ môn. Nếu `status: chua_khao_sat`: khảo sát 1–2 bài đầu trên ảnh PDF, trả lời từng `open_questions`, sửa hồ sơ (cấp mục, heading thêm, khung kiến thức…), chạy thử cổng 1 trên bài đó.
2. Đổi `status: da_kiem_chung`, ghi `verified_on`, xoá các `open_questions` đã trả lời. Câu nào cần người dùng chốt thì hỏi trước khi làm tiếp.
3. Chỉ sau bước 2 mới làm Tầng 1 hàng loạt.

Hồ sơ hiện có (2026-10-29): `sinh` (sinh_12) và `hoa` (hoa_12) đã kiểm chứng; `toan`, `vat_ly`, `lich_su`, `dia`, `tin_hoc`, `ngu_van`, `tieng_anh`, `am_nhac`, `cong_nghe` là khung **chưa khảo sát** (dựng theo mục lục 28 bộ cũ và cấu trúc chung của sách KNTT, chưa có PDF để kiểm chứng). Môn khác (GD KT&PL, GDQP&AN, HĐTN-HN…) dùng `_default` cho đến khi có hồ sơ riêng.

