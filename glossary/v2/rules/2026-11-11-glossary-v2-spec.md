# Spec: Từ điển thuật ngữ liên cấp – liên môn (Ver 2) và Dữ liệu xuất JSON

> **Mã:** `SPEC-GLOSSARY-V2`, phiên bản 1.0, ngày 2026-11-19, trạng thái **đã duyệt**
> **Phạm vi:** Quy tắc biên soạn, hợp nhất, chống trùng, đối chiếu kiểm chứng và xuất JSON cho hệ thống Từ điển thuật ngữ Ver 2 (tách file theo môn ở tầng Markdown, liên thông đa môn ở tầng JSON).
> **Quan hệ với hệ thống hiện hành:** Kế thừa nguồn chứng cứ từ bài học gốc (`lessons/`) và từ điển `v1` ([SPEC-TEXTBOOK-01](../../v1/rules/2026-10-27-textbook-framework-spec.md)). **Không sửa đổi, không xóa** dữ liệu bài học gốc và `glossary/v1/` hiện có.
> **Tài liệu tham chiếu đối chứng:** [Huong-dan-tu-dien.md](../reference/Huong-dan-tu-dien.md) và [Tu-dien.md](../reference/Tu-dien.md) của người dùng.

---

## 1. Mục tiêu và nguyên tắc bất biến về nguồn

### 1.1. Mục tiêu

- Xây dựng bộ từ điển thuật ngữ chuẩn hóa **Ver 2** song ngữ (Anh – Việt), lấy thuật ngữ tiếng Anh làm khóa định danh (`### [English term]`), cô đọng bản chất khoa học trong 1–2 câu thay vì chép nguyên văn lời dẫn dài dòng của SGK.
- Giải quyết bài toán **quá tải ngữ cảnh (context overflow) và bảo trì** bằng kiến trúc tách file Markdown theo từng môn học (`Chuyên ngành gốc`), sau đó biên dịch tự động sang JSON để kiểm tra chống trùng xuyên môn và phục vụ truy vấn nhẹ.
- Bảo toàn khả năng mở rộng đa nguồn trong tương lai (SGK Kết nối tri thức lớp 10–11–12 và giáo trình quốc tế) mà không ghi đè dữ liệu cũ.

### 1.2. Nguyên tắc chống chép mẫu (Vai trò của `report/research/Tu-dien.md`)

- **Nguồn biên soạn duy nhất** của các mục từ SGK trong dự án là dữ liệu **Tầng 1 (bài học nguyên văn đã đối chiếu ảnh PDF)** và **Tầng 2 (`dataset/<unit>.json`)** đã nghiệm thu của từng bộ sách.
- File [report/research/Tu-dien.md](../report/research/Tu-dien.md) **chỉ dùng để kiểm chứng và đối chiếu sau khi tạo xong**, tuyệt đối:
  - **Không** dùng làm file hạt giống (seed) để điền tiếp hay sửa trực tiếp lên đó.
  - **Không** sao chép câu giải nghĩa tiếng Anh, tiếng Việt hoặc danh sách mục từ từ `report/research/Tu-dien.md` sang từ điển mới.
- Khi xây dựng từ điển Ver 2 cho môn Sinh học (`Tu-dien-Sinh-hoc.md`), phải **tạo mới hoàn toàn từ đầu** dựa trên dữ liệu chuẩn `sinh_10`, `sinh_11`, `sinh_12`, sau đó đem ra **so sánh đối chiếu hai chiều** với `report/research/Tu-dien.md` theo quy trình tại Mục 6.

---

## 2. Kiến trúc lưu trữ và luồng dữ liệu

```
TẦNG 1 + TẦNG 2 (đã verified theo SPEC-TEXTBOOK-01)
  ├── textbook/khoi_<lop>/<unit>/*.md          (nguyên văn bài học + mốc trang in)
  └── textbook/dataset/<unit>.json             (thuật ngữ theo từng bộ sách)
          │
          │  Biên soạn mới theo môn (gộp liên cấp 10–11–12, cô đọng song ngữ EN/VI)
          ▼
TẦNG TỪ ĐIỂN VER 2 — MARKDOWN THEO MÔN (nguồn bảo trì chính)
  ├── Tu-dien-Toan-hoc.md
  ├── Tu-dien-Vat-li.md
  ├── Tu-dien-Hoa-hoc.md
  ├── Tu-dien-Sinh-hoc.md      ◄── Đối chiếu kiểm chứng với report/research/Tu-dien.md
  ├── Danh-sach-xung-dot.md    (các ca trùng chéo EN/VI hoặc đồng âm liên môn chờ duyệt)
  └── Danh-sach-xem-xet.md     (các thuật ngữ Ngoài nguồn chưa có định nghĩa trong sách)
          │
          │  Script biên dịch & kiểm tra chống trùng xuyên môn (giai đoạn sau)
          ▼
TẦNG DỮ LIỆU XUẤT JSON VER 2 (phục vụ truy vấn, agent tạo học liệu, web)
  ├── glossary_master.json     (kho tổng hợp liên môn đã kiểm định không trùng)
  └── by_subject/<mon>.json    (gồm mục gốc của môn + mục môn khác có Bối cảnh tại môn này)
```

**Lý do tách file Markdown theo môn thay vì gộp 1 file `Tu-dien.md` duy nhất:**

- Giữ dung lượng mỗi file Markdown ở ngưỡng **400–900 mục** (thay vì 2.500–5.000+ mục gây tràn cửa sổ ngữ cảnh của AI và xung đột Git khi bảo trì song song nhiều môn).
- Tính liên môn vẫn được giữ trọn vẹn nhờ trường `Chuyên ngành gốc`, các gạch con liên ngành trong `Bối cảnh`, và bước hợp nhất tự động lên JSON. Khi cần 1 file Markdown tổng hợp toàn cục để xem/tra cứu, script có thể kết xuất tự động từ `glossary_master.json` (chỉ đọc, không sửa tay).

---

## 3. Định dạng mục từ Markdown (Ver 2)

Mỗi file `Tu-dien-<Mon>.md` sắp xếp các mục theo **thứ tự bảng chữ cái A–Z không phân biệt hoa thường** của thuật ngữ tiếng Anh (ký hiệu đặc biệt/tên Latin in nghiêng → chữ số → `A–Z` → chữ cái Hy Lạp).

### 3.1. Cấu trúc chuẩn của một mục

```markdown
### [English term]
- **Tiếng Việt:** ...
- **Chuyên ngành gốc:** ... (Toán học / Vật lí / Hóa học / Sinh học)
- **Giải thích (EN):** ...
- **Giải thích (VI):** ...
- **Bối cảnh:** ...
- **Nguồn:** ...
```

Khi một mục được gộp từ nhiều lớp/sách có định nghĩa khác nhau hoặc dùng ở nhiều ngữ cảnh, mở rộng thành:

```markdown
### [English term]
- **Tiếng Việt:** ...
- **Chuyên ngành gốc:** ...
- **Giải thích (EN):** ...
- **Giải thích (VI):** ...
- **Giải thích khác (SGK <Môn> <lớp>):** EN: ... / VI: ...
- **Bối cảnh:**
  - <Ngữ cảnh 1>.
  - <Ngữ cảnh 2>.
- **Nguồn:** <Nguồn 1>; <Nguồn 2>
```

### 3.2. Quy tắc chi tiết từng trường

| Trường | Bắt buộc | Quy tắc biên soạn |
|---|---|---|
| Tiêu đề `### ` | Có | Thuật ngữ tiếng Anh chuẩn quốc tế tương ứng với khái niệm; một khóa duy nhất (không nối nhiều từ bằng dấu `/`). Tên khoa học Latin viết in nghiêng (`### *Drosophila melanogaster*`). |
| `Tiếng Việt` | Có | Thuật ngữ tiếng Việt chuẩn theo đúng danh pháp GDPT 2018 trong SGK (ví dụ `DNA`, `gene`, `acid`, `amino acid`). Nếu có tên gọi phụ/viết tắt phổ biến trong sách thì đặt trong ngoặc đơn. |
| `Chuyên ngành gốc` | Có | Ngành khoa học khai sinh ra khái niệm (`Toán học` / `Vật lí` / `Hóa học` / `Sinh học`). Mục từ đặt tại file `Tu-dien-<Mon>.md` tương ứng với `Chuyên ngành gốc` của nó. |
| `Giải thích (EN)` | Có | **1–2 câu cô đọng** nêu đúng bản chất và điều kiện khoa học cốt lõi rút ra từ toàn bộ tiểu mục chứa thuật ngữ ở Tầng 1; khớp nghĩa 1–1 với `Giải thích (VI)`. Tuyệt đối không đưa kiến thức ngoài nguồn Tầng 1. |
| `Giải thích (VI)` | Có | **1–2 câu cô đọng** chuẩn văn phong từ điển: lược bỏ lời dẫn dắt sư phạm dài dòng của SGK, nhưng **phải tổng hợp đủ điều kiện/bản chất nằm ở các câu kế cận trong cùng tiểu mục** (ví dụ `biuret test`: phải đủ mục đích *nhận biết protein*, cơ chế *liên kết peptide tạo phức chất màu tím với Cu²⁺* và điều kiện *trong môi trường kiềm*). |
| `Giải thích khác (...)` | Khi cần | Chỉ thêm khi cùng một thuật ngữ xuất hiện ở lớp/sách khác với định nghĩa có phạm vi hoặc góc tiếp cận khác biệt rõ rệt cần bảo toàn cho từng khối lớp. |
| `Bối cảnh` | Có | Lĩnh vực, khối lớp, chủ đề sử dụng và lưu ý phân biệt nghĩa (nếu dễ nhầm). Nhiều bối cảnh thì tách thành danh sách mục con thụt lề 2 dấu cách (`  - `). Không lặp thừa số bài kiểu `Bài 15: Bài 15 mục I.3`. |
| `Nguồn` | Có | Ghi đầy đủ tên sách, chương/chủ đề, bài, mục và **số trang in thực tế (`tr. <printed_page>`)** truy xuất từ mốc `<!-- pdf:N -->` trừ `printed_offset` ở Tầng 1. Không để `tr. chưa rõ` đối với các bộ SGK đã có PDF trong dự án. Nhiều nguồn nối bằng dấu `; `. |

### 3.3. Quy tắc gom đa đoạn toàn bài và Công thức viết câu giải nghĩa (Khắc phục hạn chế của V1)

Ở hệ thống Tầng 2 cũ (`SPEC-TEXTBOOK-01`), quy tắc "chỉ in đậm 1 lần đầu tiên" kết hợp cổng kiểm tra máy móc `bigram ≥ 0.65` gây ra 4 hạn chế thực tế: (1) neo nhầm vào lần nhắc thoáng qua đầu tiên thay vì mục định nghĩa chính ở phía sau; (2) cắt dán nguyên câu văn kể chuyện của SGK (kèm từ nối *"Nhờ đó..."*, *"được gọi là..."*); (3) dừng cứng trước chữ *"Ví dụ:"* làm mất phương pháp/cơ chế đặc trưng ngay câu sau; (4) đẩy đặc trưng nhận diện khái niệm xuống ô `Bối cảnh`. Khi biên soạn Ver 2 bắt buộc áp dụng 4 quy tắc khắc phục sau:

1. **Quét ngữ cảnh đa đoạn trên toàn bài/toàn bộ sách (Multi-section Scan):**
   - Không chỉ đọc duy nhất đoạn `location` có chữ in đậm ở Tầng 2. Phải gom **tất cả các đoạn văn trong bài học (và các bài liên quan được dẫn ở cột `Bối cảnh` Tầng 2)** có nhắc tới thuật ngữ để chọn đúng mục giải thích trực diện và đầy đủ nhất làm trục chính.
   - *Ví dụ chuẩn (`targeted drug` — Sinh 10 Bài 1):* Không khóa hẹp ở câu ngoặc đơn phụ tại Mục I.5 (*"...thuốc đặc hiệu ức chế các protein gây bệnh (được gọi là thuốc hướng đích)"*), mà phải tổng hợp với đoạn chuyên sâu Y – dược tại Mục II.1 (*"tác động tới những loại protein riêng biệt để chữa các bệnh hiểm nghèo như ung thư"*).
2. **Viết câu định nghĩa tự thân theo khung 2 vế "Loại khái niệm + Đặc trưng phân biệt" (Genus – Differentia):**
   - **Loại bỏ hoàn toàn vỏ câu dẫn chuyện của SGK:** Cấm mở đầu bằng từ nối phụ thuộc mạch văn trước (*"Nhờ đó..."*, *"Vì vậy..."*, *"Sự kết hợp... đang hình thành nên một ngành mới được gọi là..."*) và cấm lặp cấu trúc *"X là ... được gọi là X"*. Mở đầu trực tiếp bằng danh từ chỉ loại: *Ngành... / Thuốc... / Quá trình... / Hợp chất... / Bào quan...*
   - **Bổ sung đặc trưng phân biệt từ câu giải thích/ví dụ liền kề:** Khi câu chứa tên thuật ngữ trong SGK mới chỉ giới thiệu nguồn gốc hoặc thành phần chung chung chưa đủ phân biệt với khái niệm lân cận, **bắt buộc rút thêm cơ chế, công cụ hoặc ứng dụng tiêu biểu ở các câu giải thích/ví dụ ngay kế sau trong cùng tiểu mục** (nối bằng `;` hoặc `, ví dụ...`).
   - *Ví dụ chuẩn (`systems biology` — Sinh 10 Bài 1 Mục I.5):* Không dừng ở câu 1 (*"Sự kết hợp của ngành sinh học với hoá học, tin học, toán học và vật lí..."*), mà rút thêm phương pháp cốt lõi ở câu kế tiếp để thành: *"Ngành kết hợp sinh học với hoá học, tin học, toán, vật lí; dùng mô hình máy tính để dự đoán tương tác giữa các protein."*
   - *Ví dụ chuẩn (`biuret test` — Sinh 10 Bài 6 Mục III.3):* Gom cả đoạn 1 (cơ chế liên kết peptide với Cu²⁺) và đoạn 2 (điều kiện môi trường kiềm) thành: *"Nhận biết protein: liên kết peptide tạo phức chất màu tím với Cu²⁺ trong môi trường kiềm."*
3. **Phân định rạch ròi vai trò giữa `Giải thích` và `Bối cảnh`:**
   - `Giải thích (EN/VI)` phải tự đứng độc lập và chứa trọn bản chất + điều kiện/phương pháp nhận diện khái niệm.
   - `Bối cảnh` chỉ định vị phạm vi sử dụng (môn, lớp, bài, mục, lĩnh vực ứng dụng) và cảnh báo phân biệt với nghĩa/thuật ngữ dễ nhầm.
4. **Kiểm soát chống bịa bằng "Bám nguồn theo mệnh đề ý (Fact-grounding)" thay cho `bigram ≥ 0.65`:**
   - Bỏ kiểm tra trùng chuỗi cặp từ liên tiếp (`bigram ≥ 0.65`) ở tầng Ver 2 để giải phóng câu chữ khỏi văn phong kể chuyện của SGK.
   - Thay bằng nguyên tắc kiểm chứng ngữ nghĩa: **mọi mệnh đề thông tin trong `Giải thích (EN/VI)` đều phải chỉ ra được nằm ở dòng/mục cụ thể nào của Tầng 1** (được phép gộp ý từ nhiều mục trong bài và cô đọng lại ngữ pháp, tuyệt đối không thêm kiến thức ngoài Tầng 1). Khi rà soát, có thể đối chiếu thêm lịch sử các mục giáo viên đã sửa tay trên `review-station` (nếu có) để nhận diện nhanh những chỗ Tầng 2 cũ bị rườm rà hoặc hẹp nghĩa.

### 3.4. Quy ước công thức và ký hiệu

- Công thức toán học, vật lí, biểu thức thống kê phức tạp: dùng LaTeX `$...$` (ví dụ `$f'(x) = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h}$`, `$df = n - 1$`).
- Chỉ số hóa học, điện tích ion hoặc ký hiệu đơn giản đi trong câu văn giải nghĩa: ưu tiên ký tự Unicode trực tiếp gọn sạch (`Cu²⁺`, `H₂O`, `CO₂`, `NH₄⁺`, `NO₃⁻`, `5'→3'`) để không bị lỗi lặp chuỗi khi hiển thị/sao chép dạng text thuần; phương trình phản ứng phức tạp dùng LaTeX chuẩn.

---

## 4. Quy tắc hợp nhất, chống trùng và xử lý liên môn

### 4.1. Bốn quy tắc chống trùng (kiểm tra trên toàn bộ các môn)

Khi đưa một ứng viên thuật ngữ mới vào hệ thống, kiểm tra lần lượt:

1. **Trùng khóa Tiếng Anh** (không phân biệt hoa/thường) với mục `X` đã có:
   - Nếu cùng một khái niệm khoa học → **Cập nhật vào `X`** (không tạo mục mới).
   - Nếu là hai khái niệm khác hẳn bản chất giữa hai ngành → Áp dụng quy tắc **Đồng âm khác bản chất** (Mục 4.3).
2. **Khác Tiếng Anh nhưng trùng tên Tiếng Việt** với mục `X` đã có:
   - Nếu cùng một khái niệm (chỉ khác cách chọn từ đồng nghĩa tiếng Anh, ví dụ `targeted drug` vs `targeted therapy` cho *Thuốc hướng đích*, hoặc `genetically modified organism` vs `genetically modified organism (GMO)` cho *Sinh vật biến đổi gene*) → **Gộp chung vào 1 mục `X` duy nhất**, chọn thuật ngữ tiếng Anh chuẩn nhất làm tiêu đề `### `.
3. **Không trùng cả Tiếng Anh lẫn Tiếng Việt**:
   - Tạo mục mới vào đúng file `Tu-dien-<Mon>.md` theo thứ tự A–Z.
4. **Xung đột chéo** (Tiếng Anh trùng mục `X`, nhưng Tiếng Việt lại trùng mục `Y` khác `X`):
   - Tạm cập nhật vào `X` theo khóa tiếng Anh, giữ nguyên `Y`, đồng thời **ghi bắt buộc vào `Danh-sach-xung-dot.md`** để người phụ trách chuyên môn chốt.

### 4.2. Nguyên tắc cập nhật "Không ghi đè" (Non-destructive Merge)

Khi gộp thông tin từ lớp/bài/môn mới vào mục `X` đã tồn tại:
- Không xóa bối cảnh cũ, không xóa nguồn cũ.
- Nối nguồn mới vào cuối trường `Nguồn` bằng dấu `; `.
- Nếu xuất hiện ở lĩnh vực/cấp học mới: chuyển `Bối cảnh` sang dạng danh sách gạch con và thêm dòng mới.
- Nếu định nghĩa ở sách mới có chi tiết/góc nhìn khác cần lưu ý riêng khi ra đề cho lớp đó: thêm trường `- **Giải thích khác (<Tên sách>):** EN: ... / VI: ...`.

### 4.3. Giao thoa liên môn: "Cùng khái niệm khác ứng dụng" vs "Đồng âm khác bản chất"

- **Trường hợp A — Cùng một khái niệm gốc, ứng dụng ở nhiều môn** (ví dụ `Derivative`, `Integral`, `Variance` gốc Toán học dùng trong Vật lí/Sinh học; `Activation energy`, `Peptide bond`, `Biuret reaction` giữa Hóa học và Sinh học):
  - Chỉ giữ **1 mục duy nhất** đặt tại file của **`Chuyên ngành gốc`**.
  - Thêm gạch con của các môn ứng dụng vào trường `Bối cảnh` và nối đầy đủ `Nguồn` của các SGK liên quan.
  - Khi xuất JSON riêng cho từng môn (`by_subject/<mon>.json`), trình biên dịch tự động kéo mục này vào tất cả các môn xuất hiện trong `Bối cảnh`.
- **Trường hợp B — Đồng âm nhưng khác hẳn bản chất khái niệm** (ví dụ `Vector` đại lượng có hướng Toán/Lí vs `Vector` thể truyền gene Sinh học; `Nucleus` hạt nhân nguyên tử Lí/Hóa vs nhân tế bào Sinh học; `Cell` pin điện hóa vs tế bào; `Base` bazơ Hóa học vs base nitơ Sinh học vs cơ số Toán học):
  - **Tách thành các mục riêng biệt**, gắn hậu tố chuyên ngành trong ngoặc đơn ở tiêu đề tiếng Anh: ví dụ `### Vector (mathematics)` (trong `Tu-dien-Toan-hoc.md`) và `### Vector (molecular biology)` (trong `Tu-dien-Sinh-hoc.md`).
  - Tại mục `Bối cảnh` của mỗi bên, thêm một gạch con `- *Lưu ý:* không nhầm với ... trong <Môn kia> (...)` để cảnh báo chéo.

### 4.4. Xử lý thuật ngữ "Ngoài nguồn" và thuật ngữ không đưa vào từ điển

- Các thuật ngữ ở Tầng 2 thuộc diện `out_of_source` (sách có nhắc tên trong bài nhưng không định nghĩa hay mô tả trên toàn bộ cả 3 khối 10–11–12 của dự án): **không tạo mục rỗng** trong `Tu-dien-<Mon>.md`, mà chuyển vào `Danh-sach-xem-xet.md` kèm vị trí xuất hiện.
- Lưu ý: Nhiều thuật ngữ bị đánh dấu `Ngoài nguồn` cục bộ ở một chương (ví dụ *Sinh vật nhân sơ* ở Chương 1 Sinh 10, hoặc *Enzyme* ở Chương 1 Sinh 11) thực chất **đã có định nghĩa đầy đủ ở chương/lớp khác** (Bài 7 Sinh 10, Bài 13 Sinh 10). Khi gộp liên cấp ở Ver 2, các mục này sẽ lấy định nghĩa chuẩn từ bài có định nghĩa và gắn thêm bối cảnh/nguồn của các bài sử dụng.
- Các thuật ngữ do giáo viên bổ sung ngoài phạm vi SGK (không có mặt trong văn bản Tầng 1 của bất kỳ cuốn SGK nào, ví dụ `helicase`, `primase`) **không tự ý đưa vào** khi tạo từ nguồn SGK; chỉ bổ sung khi có nguồn tài liệu mở rộng chính thức được khai báo ở trường `Nguồn`.

---

## 5. Khung cấu trúc JSON đích (cho giai đoạn triển khai code)

Mỗi mục từ khi biên dịch từ `Tu-dien-<Mon>.md` sang JSON sẽ tuân theo cấu trúc chuẩn (chờ chốt trước khi tạo file trong `textbook/schema/`):

```json
{
  "id": "sinh-biuret-test",
  "term_en": "biuret test",
  "term_vi": "Phép thử Biuret",
  "aliases_vi": [],
  "origin_discipline": "Hóa học",
  "explanation_en": "Detects proteins: peptide bonds form a purple complex with Cu²⁺ in alkaline medium.",
  "explanation_vi": "Nhận biết protein: liên kết peptide tạo phức chất màu tím với Cu²⁺ trong môi trường kiềm.",
  "alt_explanations": [],
  "contexts": [
    {
      "discipline": "Sinh học",
      "grade": 10,
      "lesson_ref": "Bài 6",
      "detail": "Nhận biết protein trong thực hành (Mục III.3)."
    },
    {
      "discipline": "Hóa học",
      "grade": 12,
      "lesson_ref": "Bài 9, Bài 10",
      "detail": "Phản ứng màu nhận biết peptide (trừ dipeptide) và protein."
    }
  ],
  "sources": [
    {
      "raw": "SGK Sinh học 10 KNTT, Chương 01, B6, Mục III.3, tr. 41",
      "unit": "sinh_10",
      "book": "SGK Sinh học 10 KNTT",
      "chapter": "01",
      "lesson": "B6",
      "section": "III.3",
      "printed_pages": [41]
    }
  ],
  "disambiguation_notes": []
}
```

---

## 6. Quy trình Kiểm chứng & Đối chiếu riêng khi tạo mới môn Sinh học

Vì [report/research/Tu-dien.md](../report/research/Tu-dien.md) (603 mục: 583 mục Sinh học phủ Sinh 10 Bài 1–13, Sinh 11 Bài 1–8, Sinh 12 Bài 1–18 + 20 mục Toán) là mẫu thực tế của người dùng, quy trình làm môn Sinh học bắt buộc trải qua **2 pha độc lập**:

### Pha 1: Tạo mới độc lập (`Tu-dien-Sinh-hoc.md`)
- Chỉ đọc dữ liệu chuẩn của dự án (`sinh_10`, `sinh_11`, `sinh_12` — tổng cộng 1.103 dòng định nghĩa/mô tả ở Tầng 2 và văn bản gốc Tầng 1).
- Không đọc hay tra cứu `report/research/Tu-dien.md` trong lúc viết để đảm bảo tính khách quan và bám 100% trang sách thật (đầy đủ cả Sinh 10 Bài 14–26, Sinh 11 Bài 9–29, Sinh 12 Bài 19–35 mà bản mẫu chưa có).

### Pha 2: Đối chiếu kiểm chứng với `report/research/Tu-dien.md`
Sau khi có bản nháp `Tu-dien-Sinh-hoc.md`, thực hiện đối sánh toàn diện với 583 mục Sinh học trong file mẫu trên 4 tiêu chí và lập **Báo cáo đối chiếu**:

1. **Độ phủ thuật ngữ (trong phạm vi các bài giao nhau: Sinh 10 B1–13, Sinh 11 B1–8, Sinh 12 B1–18):**
   - Mục nào có ở bản mẫu của thầy mà bản tạo mới **chưa có**: phải phân loại rõ lý do — *(a) Bỏ sót thật trong SGK* → bổ sung ngay từ Tầng 1; *(b) Thuật ngữ ngoài SGK do giáo viên thêm (như `helicase`, `primase`)* → ghi nhận vào báo cáo/danh sách xem xét, không tự bịa nguồn SGK; *(c) Ví dụ tên loài/hóa chất thực hành cụ thể (`*Pisum sativum*`, `acetone 80%`...)* → chốt tiêu chí giữ hay loại đồng bộ trên toàn bộ 3 khối.
2. **Khớp khóa Tiếng Anh (`### [English term]`):**
   - Liệt kê các cặp cùng khái niệm tiếng Việt nhưng bản tạo mới và bản mẫu chọn từ tiếng Anh khác nhau, đồng thời chỉ ra các cặp đang bị tách đôi trong bản mẫu (`GMO`, `targeted drug/therapy`, `macroelement/macronutrient`, `DNA`) để chuẩn hóa về 1 khóa duy nhất.
3. **Chất lượng cô đọng `Giải thích (EN)` & `Giải thích (VI)`:**
   - Lấy mẫu đối chiếu trực tiếp (như trường hợp `biuret test`, `ribosome`, `thylakoid`, `allele`) để kiểm tra bản tạo mới đã đủ ngắn gọn (1–2 câu) và gom đủ điều kiện khoa học từ tiểu mục Tầng 1 hay chưa, có bị sót số trang (`tr.`) nào không.
4. **Kiểm chứng gộp liên cấp:**
   - Đối chiếu các mục xuất hiện ở nhiều khối lớp (Sinh 10 + 11 + 12) xem việc tách `Bối cảnh` mục con và `Giải thích khác` có nhất quán và dễ đọc hơn hoặc ngang bằng bản mẫu không.

---

## 7. Các quyết định đã chốt (2026-11-19)

| # | Vấn đề | Quyết định chính thức | Trạng thái |
|---|---|---|---|
| 1 | Thư mục lưu trữ từ điển Ver 2 | Đặt trọn gói trong `glossary/v2/` (`markdown/`, `data/`, `rules/`, `reference/`, `reports/`), ngang hàng với `glossary/v1/` để sẵn sàng mở rộng `v3/`, `v4/`... về sau; bài học gốc nằm riêng tại `lessons/` | Đã chốt |
| 2 | Định dạng chuỗi `Nguồn` cho SGK KNTT | `SGK <Môn> <lớp> KNTT, <Phần/Chương nếu có>, B<n> (Mục <x>), tr. <trang_in>` (hoặc `Bảng giải thích thuật ngữ, tr. <trang_in>`), bắt buộc có số trang in thực tế | Đã chốt |
| 3 | Tiêu chí chọn mục từ đối với loài sinh vật và hóa chất thực hành | Lấy toàn bộ các mục `in_source` và `described` ở Tầng 2, cộng thêm các đối tượng thí nghiệm kinh điển có vai trò khái niệm rõ trong bài học (như *Pisum sativum*, *Drosophila melanogaster*, *Mirabilis jalapa*, *Hibiscus mutabilis*...) | Đã chốt |
| 4 | Phân định `Chuyên ngành gốc` cho khái niệm giao thoa Hóa – Sinh | Các phân tử sinh học và phép thử sinh học (`amino acid`, `lipid`, `carbohydrate`, `biuret test`...) giữ ở `Sinh học` (`Tu-dien-Sinh-hoc.md`); các khái niệm thuần hóa lí / vật lí / toán học (`activation energy`, `covalent bond`, `hydrogen bond`, `T-test`...) đặt ở `Hóa học` / `Vật lí` / `Toán học` kèm `Bối cảnh` Sinh học (tự động kéo vào `by_subject/sinh_hoc.json` khi xuất JSON) | Đã chốt |
