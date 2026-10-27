# Spec: Bài học nguyên văn (Tầng 1), Từ điển thuật ngữ (Tầng 2), Dữ liệu xuất (JSON)

> **Mã:** `SPEC-TEXTBOOK-01`, phiên bản 0.3, ngày 2026-10-27, trạng thái **nháp, chờ duyệt**
> **Phạm vi:** Quy tắc chung cho mọi môn và mọi lớp, **hiện chỉ áp dụng cho SGK**. Spec này không ghi số liệu của riêng môn nào.
> **Plan thí điểm:** [Sinh 12](../plans/2026-10-26-bio12-extraction-plan.md)
> **Quan hệ với tài liệu khác:** README tóm tắt quy tắc. Spec này và các file trong `textbook/schema/` là chuẩn duy nhất về **định dạng**. Plan của từng bộ chỉ ghi việc cần làm và tiến độ.

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
        │  ocr_pages.py  → .ocr/<pdf>/pNNNN.txt   (chỉ để tham khảo và kiểm tra tự động)
        │  Claude đọc ẢNH trang, viết Markdown
        ▼
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

### 3.3. Quy tắc

- Tên **chép đúng như in ở trang mở đầu** của nút, đọc từ ảnh. Nếu mục lục của sách ghi khác (ví dụ Sinh 12: mục lục ghi "Chương I", "Bài 5. Công nghệ di truyền" nhưng trang đầu ghi "Chương 1", "Công nghệ gene") thì theo trang đầu, và ghi chỗ khác biệt vào `notes` của `progress.json`.
- Số bài giữ đúng như sách. Sách đánh liên tục (Sinh 12: Chương 2 bắt đầu từ Bài 7) thì giữ liên tục.
- Bài "Ôn tập chương" có số (Hoá 11: Bài 3) là `kind: bai`, `lesson_type: on_tap`. Không có số thì là `kind: on_tap`.
- Tên hiển thị đầy đủ = `label + ". " + title` (hoặc chỉ `title` nếu `label` là `null`), ví dụ `Chủ đề 1. Cách mạng tư sản và sự phát triển của chủ nghĩa tư bản`.
- `printed_offset`: `trang in = trang PDF − printed_offset`. Nút nào lệch khác với giá trị của file thì ghi riêng ở nút đó.
- `status`: `pending → layer1 → layer2 → verified`, hoặc `skip` cho trang đầu/cuối không chép.
- **Thư mục Tầng 1** đi theo cây: mỗi nút `group` một thư mục `<Kind>-<NN>-<slug>` (`Phan-04-Di-truyen-hoc`, `Chu-de-01-Cach-mang-tu-san`, `Unit-01-Life-stories`, `Tap-1`). Nút lá là một file `<Mã>-<slug>.md` (`B01-DNA-va-co-che-tai-ban-DNA.md`, `U01-L1-Getting-started.md`). Trang đầu/cuối nằm ở thư mục gốc của bộ.

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
| `## I. …` / `### 1. …` / `**a) …**` | Có | `term.location.section` (`I`, `II.1`, `III.2.a`) |
| `## ❓ <tên hộp đúng như sách>` | | |
| `## 💡 <tên hộp đúng như sách>` | | |
| `## 📌 Kiến thức cốt lõi` | | |
| `## ✏️ Luyện tập và vận dụng` | | |
| `## 📷 Danh sách hình trong bài` | Có, nếu bài có hình | `lesson.figures` |

SGK không có khung yêu cầu cần đạt (ví dụ Vật lí, Địa lí, Âm nhạc, Tiếng Anh) thì bỏ khối 🎯; khi đó `objectives` là `null`. Môn có cấu trúc riêng ghi cách ánh xạ heading vào `notes` của `progress.json` và không sửa spec.

### 4.3. Quy ước bắt buộc

- **Nguyên văn:** chép đúng câu chữ, chính tả và cách viết của sách. Không chuẩn hóa ở Tầng 1.
- **Mốc trang:** đặt `<!-- pdf:N -->` ngay trước nội dung bắt đầu trang PDF N. Mốc đầu tiên phải trùng `pdf_pages[0]`.
- **In đậm:** chỉ in đậm `**…**` thuật ngữ **tại câu sách định nghĩa nó**, mỗi thuật ngữ in đậm một lần trong cả bộ. Không in đậm những chỗ chỉ nhắc lại.
- **Công thức và kí hiệu:** dùng LaTeX `$…$` hoặc `$$…$$`.
- **Môn Sinh:** tên gene in nghiêng (`*lacZ*`), protein viết đứng. Viết giống như sách in.

### 4.4. Hình minh họa

- Sách là ảnh quét, không có hình nhúng riêng, nên phải **cắt theo khung (bbox)** từ ảnh trang render ở 300 DPI.
- `figures.json` đặt trong thư mục nhóm chứa bài: `{ "<mã hình>": {"pdf_page": N, "bbox": [x0, y0, x1, y1]} }`, đơn vị là point của PDF. `crop_figures.py` đọc file này, nên cắt lại lúc nào cũng ra cùng kết quả.
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
5. **Bảng 4 cột**, giữ nguyên tiêu đề cột: `| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |`
6. **`## Ghi chú nguồn cần kiểm tra`**

### 5.2. Quy tắc từng cột

- **Thuật ngữ:** tên chính phải trùng với một cụm in đậm ở Tầng 1. Phần trong ngoặc là tên viết tắt hoặc tên khác, ví dụ `Điểm khởi đầu sao chép (Ori)`.
- **Tiếng Anh:** có thể để trống. Không đưa vào học liệu cho học sinh nếu sách không ghi.
- **Giải nghĩa:** bám sát câu in đậm ở Tầng 1. Được rút gọn nhưng không diễn giải lại, không thêm ý.
- **Bối cảnh sử dụng:** khi nào dùng thuật ngữ này và phân biệt với nghĩa khác. Nên ghi bài và mục.
- **Ngoài nguồn:** thuật ngữ được dùng trong phạm vi từ điển nhưng không có câu định nghĩa nào trong phạm vi đó. Ô Giải nghĩa ghi **đúng mẫu sau** và không viết thêm gì:
  `Ngoài nguồn — chưa định nghĩa trong <phạm vi>. Xem: <bài KNTT có định nghĩa, kèm trang PDF | chưa xác định>`
- Số mục Ngoài nguồn và số ghi chú tùy theo nội dung từng chương, không có chỉ tiêu cố định.

### 5.3. Ghi chú nguồn cần kiểm tra

Giữ dạng danh sách đánh số như mẫu. Thêm trạng thái và vị trí ở đầu dòng:

```
1. [mở] Bài 2 (mục III.4.a, pdf:17) — Thuật ngữ: Codon — <vấn đề>
2. [đóng] Bài 3 (mục I.1, pdf:21) — Thuật ngữ: — — <vấn đề> → <kết luận> (2026-10-28)
```

Chỉ đóng ghi chú sau khi đã đối chiếu với ảnh trang. Không đề nghị đối chiếu với nguồn ngoài SGK (văn bản luật, chương trình, sách bộ khác). Từ điển chỉ được đổi sang `trang_thai: verified` khi không còn ghi chú nào `mở`.

## 6. Xuất JSON (`export_unit.py`)

Định dạng đích: `textbook/schema/unit.schema.json` (phiên bản `2.1`). Gồm 6 khối:

| Khối | Lấy từ | Nội dung |
|---|---|---|
| `meta` | `progress.json` và script đếm | `schema_version`, `unit`, `subject`, `subject_name`, `grade`, `generated_at`, `counts` (bài, thuật ngữ, Ngoài nguồn, ghi chú đang mở) |
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
| `english` | Cột Tiếng Anh | Để trống thì là `null` |
| `meaning` | Cột Giải nghĩa | `null` nếu là dòng Ngoài nguồn |
| `usage_context` | Cột Bối cảnh sử dụng | |
| `scope` | Vị trí dòng trong từ điển | `shared` (mục Thuật ngữ dùng chung) hoặc `lesson` |
| `source_status` | Cột Giải nghĩa | `out_of_source` nếu bắt đầu bằng "Ngoài nguồn", còn lại `in_source` |
| `reference` | Phần "Xem: …" của dòng Ngoài nguồn | Các dòng khác là `null` |
| `location` | Chỗ in đậm ở Tầng 1 | `lesson_id`, `section` (tính từ heading), `pdf_page` (mốc gần nhất phía trước), `printed_page`. Dòng Ngoài nguồn là `null` |
| `dictionary` | Tên file từ điển | |
| `note_ids` | Ghi chú `mở` nhắc tên thuật ngữ | |

Schema tự kiểm tra các ràng buộc chống bịa: dòng `in_source` bắt buộc có `meaning` và `location`; dòng `out_of_source` bắt buộc có `meaning` và `location` là `null`; ghi chú `closed` bắt buộc có `resolution` và `resolved_on`.

**Báo lỗi và dừng, không đoán,** khi gặp một trong các trường hợp: không tìm thấy chỗ in đậm của thuật ngữ `in_source`, có hai `id` giống nhau, tên mục bài không khớp `progress.json`, hoặc JSON không hợp lệ theo schema.

## 7. Cổng chất lượng

| # | Cổng | Đạt khi |
|---|---|---|
| 0 | `progress.json` | Hợp lệ theo `progress.schema.json`; `id` không trùng; tên đã đối chiếu ảnh |
| 1 | `check_lesson.py` | Frontmatter đủ và khớp `progress.json`; mốc trang tăng dần và nằm trong `pdf_pages`; bigram có dấu giữa **từng đoạn** và OCR trang tương ứng ≥ 0.65 (đoạn bị gắn cờ thì đối chiếu ảnh); mọi hình trong `figures.json` có file và có dòng trong bảng 📷 |
| 2 | `check_dict.py` | Đúng cấu trúc mục 5.1; mọi thuật ngữ `in_source` có chỗ in đậm ở Tầng 1; bigram giữa Giải nghĩa và đoạn chứa chỗ in đậm ≥ 0.65; ô Ngoài nguồn đúng mẫu; mọi ghi chú đúng định dạng mục 5.3 |
| 3 | `export_unit.py` | 0 lỗi theo `unit.schema.json`, 0 `id` trùng |
| 4 | Kiểm tra mẫu | 20–30 mục, đối chiếu ảnh trang, sai ≤ 5% (mục tiêu 0%), ghi một phần tử vào `audits` của `progress.json` |

## 8. Các quyết định đã chốt

| # | Câu hỏi | Quyết định (2026-10-27) |
|---|---|---|
| Q1 | Repo có được đẩy lên remote công khai không? | **Được.** Tầng 1 và `img/` được đưa vào git như các file khác |
| Q2 | Đặt tên "Phần" theo sách hay theo hệ riêng? | **Theo sách** (`Phần bốn` → `Phan-04`), xem mục 3.3 |
| Q4 | Mỗi sách chia mục lục một kiểu (Phần/Chương/Chủ đề/Unit…) | **Cây đệ quy**, giữ đúng tiền tố và tên in trên sách, không cố định tên cấp (mục 3) |
| Q3 | Từ điển có thêm cột `Loại` không? | **Không.** Từ điển giữ đúng định dạng mẫu `_Huong-dan` (4 cột). JSON bỏ các khoá `type`, `notation`, `related_terms` |

## 9. Công cụ (`textbook/scripts/`)

| Script | Việc |
|---|---|
| `_common.py` | Đường dẫn, đọc `progress.json`, tách token có dấu, bigram, đọc cache OCR, kiểm tra schema |
| `ocr_pages.py` | Render trang và OCR bằng tesseract (`textbook/tessdata/`, ngôn ngữ `vie`), ghi `.ocr/<pdf>/pNNNN.txt` |
| `crop_figures.py` | Đọc `figures.json`, render 300 DPI, cắt hình |
| `check_lesson.py` | Cổng 0 và cổng 1 |
| `check_dict.py` | Cổng 2 |
| `export_unit.py` | Cổng 3, ghi `textbook/dataset/<unit>.json` (kiểm tra bằng `jsonschema`) |

Nội dung Tầng 1 và Tầng 2 do **Claude đọc ảnh trang rồi viết**. Script chỉ cắt hình, kiểm tra và chuyển đổi.
