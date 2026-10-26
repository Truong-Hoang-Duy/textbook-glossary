# KHUNG KIẾN TRÚC & KẾ HOẠCH TỔNG THỂ HỆ THỐNG TRÍCH XUẤT SGK MỚI
## THAY THẾ TOÀN DIỆN `glossary/` — TẠO NỘI DUNG CHUẨN HÓA CHO `review-station`
### Khung tổng quát đa môn học (Multi-Subject Framework) — Thí điểm: Sinh học 12 (KNTT)

> **Mã tài liệu:** `PLAN-TEXTBOOK-REVIEWSTATION-FRAMEWORK-01`  
> **Tên file kế hoạch:** `2026-10-26-bio12-extraction-plan.md`  
> **Phạm vi áp dụng:** Bộ khung chuẩn (Framework/SOP) cho **Claude Code** và **Nhà phát triển (User)** để tự động hóa tạo môn mới (Sinh học, Toán học, Vật lí, Hóa học, Lịch sử, Địa lí...)  
> **Tài liệu tham chiếu chuẩn (Benchmark):** `_SGK-Nguyen-ban/` (đặc biệt là Sinh-12 Bài 1–18)  
> **Tài liệu mẫu từ điển Tầng 2:** `_Huong-dan/Từ điển Sinh học 12.md`  
> **Thư mục cũ bị thay thế:** `glossary/` (hủy bỏ hoàn toàn mô hình JSON vi mô cũ)  
> **Thư mục hệ thống mới:** `textbook/`  
> **Đích đến cuối cùng (Ultimate Goal):** Nạp dữ liệu và phục vụ vận hành hoàn hảo trên **`review-station`**  
> **Trạng thái:** Thiết kế kiến trúc & Kế hoạch triển khai hoàn chỉnh (Master Blueprint)  

---

## 1. MỤC ĐÍCH TỐI THƯỢNG & ĐÍCH ĐẾN CUỐI CÙNG (`review-station`)

### 1.1. Mục đích cốt lõi của `review-station`
Trạm thẩm định [review-station/](file:///d:/code/textbook-glossary/review-station) là cổng kiểm định chất lượng (Verification & Review Workspace) tập trung của toàn bộ dự án, nơi giáo viên và chuyên gia học liệu thực hiện:
1. **Duyệt khung "Yêu cầu cần đạt" (YCCĐ):** Hiển thị ngay đầu mỗi bài học với các mục tiêu kiến thức nguyên văn từ SGK/SGV.
2. **Kiểm định Thẻ thuật ngữ (Term Cards):** Đánh giá từng khái niệm, định nghĩa, công thức toán học/sinh học (KaTeX LaTeX), tính chất, quy tắc, ký hiệu, dải trang nguồn PDF/trang in thực tế.
3. **Thao tác thẩm định:** Phê duyệt `[A]`, Đánh dấu Cần sửa `[R]` kèm lý do chi tiết, hoặc Hiệu đính trực tiếp `[E]`.
4. **Xuất bản học liệu (`dict_md.py`):** Xuất bảng từ điển thuật ngữ tiêu chuẩn phục vụ trực tiếp cho việc sinh đề thi, câu hỏi trắc nghiệm 4 lựa chọn và phiếu điền khuyết.
5. **Cơ sở dữ liệu chân lý (Ground Truth):** Đảm bảo toàn bộ nội dung học liệu sinh ra sau này tuyệt đối không bị AI "bịa đặt" (hallucination).

### 1.2. Tại sao quy trình cũ tạo nội dung cho `review-station` thất bại?
Trước đây, để đưa dữ liệu vào `review-station`, quy trình cũ trong `glossary/` yêu cầu:
- Người dùng bóc tách từng mẩu định nghĩa rời rạc, gõ vào file lô `lo.json` tạm $\rightarrow$ chạy `python add_terms.py` $\rightarrow$ validate JSON schema $\rightarrow$ check bigram OCR.
- **Hệ quả tiêu cực:** 
  - Mất hoàn toàn ngữ cảnh học thuật: Các định nghĩa bị bóc tách vụn vặt, mất dòng chảy sư phạm, mất các bước suy luận, câu hỏi tư duy và bài tập áp dụng.
  - Hoàn toàn không có hình ảnh minh họa: Môn Sinh học, Hóa học hay Vật lí có hàng trăm sơ đồ cơ chế phân tử, cấu trúc giải phẫu, đồ thị, hình vẽ thí nghiệm. Thiếu hình ảnh khiến nội dung trên Review Station trở nên khô cứng, khiếm khuyết.
  - Tốn quá nhiều nhân lực, dễ sai sót số trang và rất khó mở rộng sang các môn học khác.

### 1.3. Mô hình mới: "Kiến trúc hai tầng" (Dual-Layer Architecture)
Hệ thống mới thay thế `glossary/` được tổ chức chặt chẽ theo hai tầng kế thừa nhau:

```
                       [PDF NGUỒN GỐC TRONG sgk/]
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: KHO BÀI HỌC NGUYÊN BẢN (TEXTBOOK VERBATIM MARKDOWN)            │
│ - Lưu trong: textbook/khoi_<lop>/<unit>/lessons/                       │
│ - Mỗi bài học là 1 file Markdown hoàn chỉnh theo chuẩn _SGK-Nguyen-ban:│
│   Frontmatter, YCCĐ, Mở đầu, I/II/III, Suy ngẫm, Cốt lõi, Luyện tập.  │
│ - Cắt tự động ảnh minh họa gốc ≥ 300 DPI (img/) và raw text (_raw_ocr/)│
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
        (Trích xuất & chuẩn hóa thuật ngữ từ các file Markdown Tầng 1)
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TẦNG 2: BỘ TỪ ĐIỂN THUẬT NGỮ CHUẨN HÓA & CẤP NGUỒN CHO REVIEW STATION │
│                                                                        │
│ 1. Bộ Từ điển Markdown chuẩn theo mẫu _Huong-dan/Từ điển Sinh học 12:  │
│    - File: textbook/khoi_<lop>/<unit>/Tu-dien-<mon>-<lop>.md           │
│    - Frontmatter: tên, mô tả, lớp, phần, chương, bài_số, nguồn, draft. │
│    - Quy ước sử dụng: viết tắt, in nghiêng gene, dùng "gene", RNA.    │
│    - Bảng 4 cột: Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng.│
│    - Giải nghĩa chỉ lấy từ Bài 1–6 (hoặc chương tương ứng).            │
│    - 5 mục không có trong nguồn ghi rõ "Ngoài nguồn" (chống bịa).      │
│    - Phần "Ghi chú nguồn cần kiểm tra" nêu rõ 5 chỗ cần đối chiếu sách.│
│                                                                        │
│ 2. Dữ liệu cấu trúc cấp cho Review Station:                            │
│    - <unit>.json: parse tự động từ từ điển (terms) và bài học (lessons)│
│    - progress.json: mục lục chuẩn và dải trang PDF                     │
│    - Đồng bộ tự động sang review-station/data/glossary/                │
│    ⟹ Vận hành trơn tru trên Review Station (cổng 8080)                 │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. NGHIÊN CỨU & RÚT RA CÁC QUY TẮC CHUNG TỪ `_SGK-Nguyen-ban` (BENCHMARK)

Thư mục `_SGK-Nguyen-ban/` (đặc biệt là các bài `B01-DNA-va-co-che-tai-ban-DNA.md` và `B02-Gene-...md`) được xác định là **Benchmark mẫu** do người dùng đã làm tay. Qua phân tích, chúng ta rút ra **5 quy tắc tổng quát áp dụng cho mọi môn học**:

### Quy tắc 1: Cấu trúc siêu dữ liệu Frontmatter YAML
Mọi bài học của bất kỳ môn nào đều phải chứa các trường chuẩn:
```yaml
---
lop: 12                          # Khối lớp: 10, 11, 12
mon: "sinh"                      # Mã môn học: toan, vat_ly, hoa, sinh, lich_su, dia_li...
ten_mon: "Sinh học"              # Tên hiển thị đầy đủ của môn học
phan: "Phần 5: Di truyền học"     # Tên phần
phan_sgk_goc: "Phần Bốn"         # Ghi chú đối chiếu tên phần trong SGK gốc
chuong: "Chương 1: Di truyền phân tử" # Tên chương chuẩn theo progress.json
bai_so: 1                        # Số thứ tự bài học trong chương trình
ten_bai: "DNA và cơ chế tái bản DNA" # Tên bài học
bo_sach: "SGK"                   # SGK, SCD, SBT, GV
trang_sgk: "5-8"                 # Số trang in hiển thị trên sách
pdf_pages: [7, 10]               # Số thứ tự trang thực tế trong file PDF
trang_thai: "draft"              # draft (chờ duyệt) | approved (đã duyệt trên review-station)
loai_bai: "ly_thuyet"            # ly_thuyet | thuc_hanh | du_an | on_tap | tom_tat
---
```

### Quy tắc 2: Phân cấp sư phạm chuẩn tắc (Pedagogical Hierarchy)
Cấu trúc bài viết bắt buộc phải tuân thủ chuẩn sau để parser có thể tự động bóc tách sang dữ liệu Review Station:
1. `# BÀI <X>: <TÊN BÀI IN HOA>`
2. `## 🎯 Yêu cầu cần đạt`: Chứa danh sách gạch đầu dòng mục tiêu. Parser sẽ lấy khối này đưa vào trường `lessons` (objectives) của `<unit>.json` cho Review Station.
3. `## 🔴 Mở đầu`: Câu hỏi/tình huống khởi động.
4. `## I. <LA MÃ>`, `### 1. <Số Ả Rập>`, `**a) Chữ thường**`: Nội dung phân tích toàn vẹn. Các thuật ngữ trọng tâm được **in đậm**, các công thức viết bằng LaTeX `$5' \rightarrow 3'$`, `$A = T$`.
5. `## ❓ Dừng lại và suy ngẫm (sau mục X)`: Câu hỏi tư duy giữa bài.
6. `## 🔬 Khoa học và đời sống` hoặc `## 💡 Em có biết`: Hộp kiến thức thực tiễn.
7. `## 📌 Kiến thức cốt lõi`: Khối tóm tắt kiến thức quan trọng nhất.
8. `## ✏️ Luyện tập và vận dụng`: Câu hỏi, bài tập cuối bài.
9. `---` và `## 📷 Danh sách hình trong bài`: Bảng kê khai mã hình, vị trí, chú thích gốc.

### Quy tắc 3: Chuẩn hóa đa phương tiện & Quy ước đặt tên ảnh
- **Cú pháp chèn ảnh trong bài Markdown:**
  ```markdown
  ![H12-P5-C1-B1-01](img/H12-P5-C1-B1-01.png)

  > **Vị trí:** cuối mục I, minh họa cấu trúc DNA (đầu trang 6)
  > **Chú thích gốc SGK:** "Hình 1.1(*). Mô hình cấu trúc DNA theo Watson và Crick" — (*) Nguồn hình: Phạm Minh Kiên
  ```
- **Quy ước đặt tên ảnh tổng quát cho mọi môn:**
  `H<Lop>-<Mon>-C<Chuong>-B<Bai>-<STT>.png`
  - Với Sinh 12: Kế thừa mã ngắn gọn đã dùng `H12-P<Phan>-C<Chuong>-B<Bai>-<STT>.png` (ví dụ: `H12-P5-C1-B1-01.png`).
  - Định dạng: `.png` chất lượng cao, độ phân giải gốc hoặc render $\ge 300\text{ DPI}$.

### Quy tắc 4: Chuẩn chính tả & Công thức khoa học đa môn
- Dấu thanh đặt ở chữ "o": viết `hòa`, `hóa`, `họa` (không viết `hoà`, `hoá`, `hoạ`).
- Môn Sinh học: Tên gene viết *in nghiêng* (*lacZ*), protein viết thường đứng (lacI).
- Môn Toán học & Vật lí: Toàn bộ công thức, ký hiệu toán học viết chuẩn KaTeX trong cặp `$ ... $` hoặc `$$ ... $$`.
- Môn Hóa học: Công thức phản ứng, phương trình ion viết bằng LaTeX/KaTeX `$\text{Fe} + 2\text{HCl} \rightarrow \text{FeCl}_2 + \text{H}_2 \uparrow$`.
- Thuật ngữ quốc tế giữ nguyên gốc Latin/Anh, không tự tiện phiên âm tiếng Việt.

### Quy tắc 5: Lưu vết kiểm định trung thực (Raw Traceability)
Mỗi bài học đều có một file text thô tương ứng lưu tại `_raw_ocr/B<XX>_raw.md` lấy từ lớp văn bản số của PDF gốc để làm căn cứ đối soát diff 1:1.

---

## 3. THIẾT KẾ CẤU TRÚC HỆ THỐNG MỚI THAY THẾ `glossary/`

Thư mục mới được đặt tên là `textbook/`, được thiết kế theo dạng module hóa đa môn học (Multi-Subject Scalability):

```
d:\code\textbook-glossary\
├── sgk/                                    # Nguồn PDF gốc (chỉ đọc)
│   ├── khoi_10/
│   ├── khoi_11/
│   └── khoi_12/
│       ├── SGK SINH HOC 12 - KNTT.pdf
│       └── toan_12/, vat_ly_12/...
│
├── _SGK-Nguyen-ban/                        # [BENCHMARK] Tài liệu đối chiếu nguyên tắc
├── _Huong-dan/                             # Quy chuẩn học liệu & mẫu từ điển gốc
│   └── Từ điển Sinh học 12.md             # Mẫu chuẩn cho Từ điển Tầng 2
│
├── review-station/                         # [REVIEW STATION] Trạm kiểm định học liệu
│   ├── data/
│   │   └── glossary/
│   │       ├── progress/<unit>.json        # Mục lục & dải trang chuẩn của từng môn
│   │       └── units/<unit>.json           # Dữ liệu thuật ngữ & YCCĐ phục vụ giao diện
│   └── review_station.py                   # Server web trạm kiểm định (cổng 8080)
│
└── textbook/                               # [NEW ARCHITECTURE] THƯ MỤC HỆ THỐNG MỚI
    ├── core/                               # Bộ công cụ lõi dùng chung cho mọi môn
    │   ├── __init__.py
    │   ├── pdf_extractor.py                # Bóc tách text layer kỹ thuật số và ảnh 300 DPI
    │   ├── markdown_builder.py             # Dựng bài học Markdown nguyên bản bám sát benchmark
    │   ├── dictionary_generator.py         # Sinh Bộ từ điển Markdown Tầng 2 chuẩn _Huong-dan
    │   ├── glossary_parser.py              # Parser chuyển đổi từ điển sang JSON <unit>.json
    │   └── sync_station.py                 # Tự động đồng bộ sang review-station
    │
    ├── dataset/                            # Kho lưu trữ JSON tập trung của mọi môn học
    │   ├── sinh_12.json                    # File JSON nạp cho Review Station
    │   ├── toan_12.json
    │   └── ...
    │
    └── khoi_12/                            # Phân cấp theo khối lớp
        └── sinh_12/                        # Đơn vị môn học cụ thể
            ├── DESCRIPTION.md              # Hồ sơ kỹ thuật môn học
            ├── progress.json               # Mục lục, dải trang PDF và tiến độ chuẩn
            ├── sinh_12.json                # Dữ liệu terms + lessons chuẩn của bộ
            │
            ├── Tu-dien-Sinh-hoc-12-Chuong-1.md # [TẦNG 2] Bộ từ điển chuẩn mẫu _Huong-dan
            │
            ├── Phan-05-Di-truyen-hoc/      # [TẦNG 1] Dữ liệu bài học Markdown nguyên bản
            │   ├── Chuong-01-Di-truyen-phan-tu/
            │   │   ├── B01-DNA-va-co-che-tai-ban-DNA.md
            │   │   ├── B02-Gene-he-gene-va-qua-trinh-truyen-dat-thong-tin-di-truyen.md
            │   │   ├── ...
            │   │   ├── B06-Thuc-hanh-tach-chiet-DNA.md
            │   │   ├── Tom-tat-chuong-1.md
            │   │   ├── img/                # Toàn bộ ảnh minh họa trích xuất ≥ 300 DPI
            │   │   │   ├── H12-P5-C1-B1-01.png
            │   │   │   └── ...
            │   │   └── _raw_ocr/           # File text thô từ PDF gốc
            │   │       ├── B01_raw.md
            │   │       └── ...
            │   ├── Chuong-02-Di-truyen-nhiem-sac-the/
            │   ├── Chuong-03-Mo-rong-hoc-thuyet-di-truyen-nhiem-sac-the/
            │   └── Chuong-04-Di-truyen-quan-the/
            │
            ├── Phan-06-Tien-hoa/
            │   └── Chuong-05-Bang-chung-va-cac-hoc-thuyet-tien-hoa/ (Bài 19–22)
            │
            ├── Phan-07-Sinh-thai-hoc-va-moi-truong/ (Bài 23–35)
            └── Glossary-Thuat-ngu-cuoi-sach.md # Bảng giải thích thuật ngữ cuối SGK
```

---

## 4. QUY TRÌNH CHUẨN TẠO MÔN MỚI (STANDARD OPERATING PROCEDURE - SOP)

Kế hoạch này được thiết kế để **người dùng hoặc Claude Code có thể lấy làm mẫu và viết code tạo bất kỳ môn học nào mới** (`<unit> = {mon}_{lop}`). Quy trình 5 bước chuẩn tắc:

```
[BƯỚC 1: TIẾP NHẬN SÁCH & LẬP PROGRESS.JSON]
 ├── Đọc mục lục sách PDF nguồn trong sgk/
 └── Lập progress.json: xác định dải trang in và dải trang PDF chuẩn cho từng bài
                     │
                     ▼
[BƯỚC 2: TỰ ĐỘNG BÓC TÁCH TÀI NGUYÊN BẰNG PYTHON]
 ├── Trích xuất Text blocks từ digital layer ⟹ lưu _raw_ocr/B<XX>_raw.md
 └── Trích xuất/crop ảnh minh họa ≥ 300 DPI ⟹ lưu img/H<Lop>-...png
                     │
                     ▼
[BƯỚC 3: DỰNG BÀI HỌC MARKDOWN NGUYÊN BẢN (TẦNG 1)]
 ├── Dựng đầy đủ Frontmatter, YCCĐ, Mở đầu, I/II/III, Suy ngẫm, Cốt lõi, Luyện tập
 └── Nhúng ảnh chính xác vị trí ngữ cảnh và lập Bảng danh mục hình ảnh
                     │
                     ▼
[BƯỚC 4: SINH TỪ ĐIỂN TẦNG 2 & BÓC TÁCH CHO REVIEW STATION]
 ├── Sinh file Từ điển Markdown Tu-dien-<mon>-<lop>.md theo chuẩn _Huong-dan
 ├── Ghi nhận 5 mục "Ngoài nguồn" và 5 điểm đối chiếu nguồn kiểm tra
 ├── glossary_parser.py chuyển đổi từ điển & bài học ⟹ <unit>.json
 └── Ghi ra textbook/dataset/<unit>.json
                     │
                     ▼
[BƯỚC 5: ĐỒNG BỘ & KIỂM ĐỊNH TRÊN REVIEW-STATION]
 ├── Chạy sync_station.py ⟹ đẩy dữ liệu sang review-station/data/glossary/
 └── Mở Review Station (http://localhost:8080) duyệt thẻ thuật ngữ trực quan
```

---

## 5. THIẾT KẾ ĐẶC TẢ TẦNG 2: BỘ TỪ ĐIỂN THUẬT NGỮ CHUẨN HÓA
### Theo cấu trúc của `_Huong-dan/Từ điển Sinh học 12.md`

Tầng 2 được xây dựng trực tiếp dựa trên các file Markdown đã bóc tách từ Tầng 1. Đối với môn thí điểm Sinh học 12 (trước mắt áp dụng cho Chương 1: Di truyền phân tử, Bài 1–6), cấu trúc file từ điển `Tu-dien-Sinh-hoc-12-Chuong-1.md` phải tuân thủ nghiêm ngặt 5 thành phần sau:

### 5.1. Cấu trúc YAML Frontmatter
```yaml
---
name: tu-dien-sinh-hoc-12
description: Từ điển thuật ngữ Sinh học 12, Phần 5 Di truyền học, Chương 1 Di truyền phân tử (Bài 1–6). Tham chiếu chuẩn hoá thuật ngữ và bối cảnh cho mọi học liệu trong dự án Tạo học liệu. Đọc trước khi tạo hoặc sửa bất kỳ học liệu nào.
loai_hoc_lieu: tu-dien-thuat-ngu
mon: Sinh học
lop: 12
phan: "Phần 5: Di truyền học"
chuong: "Chương 1: Di truyền phân tử"
bai_so: "1-6"
nguon: "SGK Sinh học 12, Phần 5 Di truyền học, Chương 1 (Bài 1–6), file markdown trong textbook/"
ngay_tao: 2026-10-26
ngay_cap_nhat: 2026-10-26
trang_thai: draft
---
```

### 5.2. Phần "Quy ước sử dụng"
```markdown
## Quy ước sử dụng
- Dùng đúng thuật ngữ ở cột "Thuật ngữ", không thay bằng từ đồng nghĩa.
- Khi một từ có nhiều nghĩa (ví dụ "mạch", "vùng", "đoạn"), chọn nghĩa theo cột "Bối cảnh sử dụng".
- Cột "Tiếng Anh" dùng để đối chiếu tài liệu quốc tế, không đưa vào học liệu cho học sinh trừ khi cần.
- Viết tắt: NTBS = nguyên tắc bổ sung; NST = nhiễm sắc thể; Ori = điểm khởi đầu sao chép. Lần đầu xuất hiện trong mỗi học liệu thì viết đầy đủ.
- Tên gene viết in nghiêng (ví dụ *lacZ*, *lacY*, *lacI*); sản phẩm protein viết không in nghiêng (ví dụ protein lacI, enzyme DNA polymerase).
- Viết "gene" (không dùng "gen"). Dùng "công nghệ gene" thống nhất.
- Ký hiệu RNA giữ nguyên: mRNA, tRNA, rRNA, miRNA, siRNA.
- Tên Latin của các bậc phân loại sinh giới được in nghiêng (ví dụ *Escherichia coli*).
```

### 5.3. Bảng thuật ngữ 4 cột theo từng bài
Bảng thuật ngữ được chia tách rõ ràng theo từng bài học (kèm mục dùng chung), mỗi bảng gồm đúng 4 cột:
`| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |`

Ví dụ cấu trúc bảng cho Chương 1:
```markdown
## Thuật ngữ dùng chung

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Sinh vật nhân sơ | prokaryote | Sinh vật không có màng nhân, gene không phân mảnh (ví dụ vi khuẩn). | Đối chiếu với sinh vật nhân thực trong Bài 1, 2, 3. |
| Sinh vật nhân thực | eukaryote | Sinh vật có nhân tế bào; phần lớn gene quy định protein phân mảnh gồm exon và intron. | So sánh cấu trúc gene, tái bản, phiên mã (Bài 1, 2). |
| Nhiễm sắc thể (NST) | chromosome | Cấu trúc mang DNA trong nhân tế bào. | Bài 2 (hệ gene người, đầu mút NST). |
| Kiểu gene | genotype | Ngoài nguồn định nghĩa chi tiết trong Bài 1–6. | Bài 5 (thay đổi kiểu gene). |
| Kiểu hình | phenotype | Ngoài nguồn định nghĩa chi tiết trong Bài 1–6. | Bài 4, Bài 5. |
| Allele | allele | Ngoài nguồn định nghĩa chi tiết trong Bài 1–6. | Bài 4 (vai trò của đột biến). |
| Trội / lặn | dominant / recessive | Ngoài nguồn định nghĩa chi tiết trong Bài 1–6. | Đột biến gene, biểu hiện thể đột biến. |
| Thụ tinh nhân tạo | artificial fertilization | Ngoài nguồn định nghĩa chi tiết trong Bài 1–6. | Ứng dụng công nghệ sinh học. |

## Bài 1: DNA và cơ chế tái bản DNA

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Tái bản DNA | DNA replication | Quá trình nhân đôi phân tử DNA, xảy ra trong nhân của tế bào. Kết quả tạo ra 2 phân tử DNA giống nhau và giống DNA mẹ. | Khi đề cập đến truyền đạt thông tin qua các thế hệ tế bào. |
| Đa phân | polymer | Kiểu cấu trúc của DNA: được tạo từ nhiều đơn phân là các nucleotide. | Mô tả cấu trúc DNA (Bài 1 mục I). |
| Nucleotide | nucleotide | Đơn phân cấu tạo DNA gồm 4 loại A, T, G, C; đóng vai trò như các "chữ cái" ghi mã thông tin di truyền. | Thành phần và đơn phân của DNA. |
| Nguyên tắc bổ sung (NTBS) | complementary base pairing | Các nucleotide liên kết đặc hiệu theo cặp: A–T và G–C trong DNA; A–U, T–A, G–C, C–G trong phiên mã. | Cơ sở của tái bản, phiên mã, dịch mã. |
| Nguyên tắc bán bảo toàn | semi-conservative replication | Mỗi DNA con gồm một mạch cũ của DNA mẹ và một mạch mới được tổng hợp. | Mô tả kết quả của tái bản DNA. |
| Điểm khởi đầu sao chép (Ori) | origin of replication | Vị trí nhất định mà tái bản DNA bắt đầu; quá trình tiến hành theo hai hướng ngược nhau. | Nhân sơ: có 1 Ori; nhân thực: có nhiều Ori. |
| Đoạn Okazaki | Okazaki fragment | Các đoạn ngắn tổng hợp nên mạch gián đoạn, sau đó được ligase nối lại. | Chỉ dùng cho mạch gián đoạn trong tái bản. |

## Bài 2: Gene, hệ gene và quá trình truyền đạt thông tin di truyền
... (Các thuật ngữ: Gene, Mạch khuôn, Mạch mã hoá, Promoter, Exon, Intron, Hệ gene, Phiên mã, mRNA, tRNA, Anticodon, rRNA, Ribosome, Phiên mã ngược, cDNA, Telomerase, Codon, Bộ ba mở đầu, Bộ ba kết thúc...)

## Bài 3: Điều hoà biểu hiện gene
... (Operon, Operon lac, Promoter P, Operator O, Gene cấu trúc lacZ-lacY-lacA, Protein ức chế lacI, Allolactose...)

## Bài 4: Đột biến gene
... (Đột biến gene, Đột biến điểm, Thay thế cặp nu, Thêm/mất cặp nu, Thể đột biến, Tác nhân đột biến...)

## Bài 5: Công nghệ gene
... (Công nghệ gene, DNA tái tổ hợp, Vector chuyển gene/Plasmid, Enzyme cắt giới hạn Restriction enzyme, Thể truyền, Sinh vật biến đổi gene GMO...)

## Bài 6: Thực hành: Tách chiết DNA
... (Mẫu vật sống, Phá vỡ màng tế bào, Nước rửa chén, Dịch chiết dứa/Protease, Cồn ethanol lạnh, Kết tủa DNA...)
```

### 5.4. Nguyên tắc trích xuất giải nghĩa & Xử lý 5 mục "Ngoài nguồn"
- **Nguyên tắc bất biến:** Giải nghĩa **chỉ lấy từ nội dung Bài 1–6** trong các file Markdown nguyên bản đã được bóc tách. Tuyệt đối không tự suy diễn hay lấy kiến thức ngoài sách.
- **5 mục quan trọng không có định nghĩa chính thức trong nguồn Bài 1–6** được ghi nhận dứt khoát là **"Ngoài nguồn"**:
  1. **Kiểu gene (genotype):** Được nhắc đến trong Bài 5 nhưng không có định nghĩa tại Chương 1 $\rightarrow$ Ghi: *"Ngoài nguồn định nghĩa chi tiết trong Bài 1–6."*
  2. **Kiểu hình (phenotype):** Được nhắc đến trong Bài 4 và Bài 5 nhưng không định nghĩa tại Chương 1 $\rightarrow$ Ghi: *"Ngoài nguồn định nghĩa chi tiết trong Bài 1–6."*
  3. **Allele (allele):** Được nhắc đến trong Bài 4 khi nói về đột biến tạo allele mới nhưng chưa được định nghĩa $\rightarrow$ Ghi: *"Ngoài nguồn định nghĩa chi tiết trong Bài 1–6."*
  4. **Trội / Lặn (dominant / recessive):** Xuất hiện khi nói về biểu hiện thể đột biến lặn nhưng không định nghĩa $\rightarrow$ Ghi: *"Ngoài nguồn định nghĩa chi tiết trong Bài 1–6."*
  5. **Thụ tinh nhân tạo (artificial fertilization / IVF):** Xuất hiện trong ứng dụng sinh học nhưng không có định nghĩa $\rightarrow$ Ghi: *"Ngoài nguồn định nghĩa chi tiết trong Bài 1–6."*
- **Ý nghĩa sư phạm:** Đánh dấu "Ngoài nguồn" giúp giáo viên và các tác vụ AI sinh câu hỏi không tự ý bịa đặt định nghĩa ngoài sách, tránh gây hoang mang cho học sinh khi làm bài kiểm tra.

### 5.5. Phần "Ghi chú nguồn cần kiểm tra"
Ở cuối file từ điển, thiết lập mục cảnh báo học thuật nêu rõ **5 chỗ cần đối chiếu trực tiếp với sách in**:
```markdown
## Ghi chú nguồn cần kiểm tra
1. Bài 2 (mục III.4.a): Câu mô tả về tính thoái hoá của mã di truyền và alanine trong nguồn có đoạn bị mờ/khó đọc ("alanine có tới 4 bộ ba khác nhau quy định"). Bảng mã di truyền cho thấy alanine có 4 bộ ba (GCU, GCC, GCA, GCG). Cần đối chiếu sách in trước khi trích dẫn nguyên văn.
2. Bài 3 (mục I.1): Chức năng của enzyme transacetylase được nguồn diễn đạt chưa thật rõ ràng ("khử các chất độc vào tế bào"). Cần đối chiếu sách in để xác nhận chuẩn xác câu chữ của tác giả.
3. Bài 4 (mục II.1): Bản ghi nguồn có dấu hiệu ghép khái niệm "chất độc màu cam" (chứa dioxin) với tác nhân hóa học "acridine orange" (chất gây đột biến thêm/mất nucleotide). Cần đối chiếu sách in trước khi nêu tên tác nhân trong học liệu để tránh sai lệch kiến thức hóa sinh.
4. Bài 5: Tiêu đề bài và phần Mở đầu dùng cụm từ "công nghệ gene", nhưng phần Kiến thức cốt lõi lại dùng "công nghệ di truyền". Từ điển thống nhất chuẩn hóa theo tiêu đề chính thức là "công nghệ gene", cần đối chiếu lại sách in.
5. Năm khái niệm nền tảng (kiểu gene, kiểu hình, allele, trội/lặn, thụ tinh nhân tạo): Được sử dụng trong bài nhưng chưa có khung định nghĩa tại Chương 1. Khi tạo câu hỏi học liệu, cần đối chiếu với chương trình Sinh học 10 hoặc Chương 2 Sinh học 12 (Di truyền NST) trước khi sử dụng.
```

### 5.6. Chuyển đổi sang dữ liệu có cấu trúc cho Review Station (`<unit>.json`)
Module `glossary_parser.py` sẽ tự động đọc file Từ điển Markdown Tầng 2 này kết hợp với các bài học Tầng 1 để sinh ra `<unit>.json` tương thích 100% với Review Station:
- Mỗi dòng trong bảng từ điển được chuyển thành 1 phần tử `terms`:
  - `term`: Lấy từ cột "Thuật ngữ".
  - `aliases`: Tự động nhận diện từ tên gọi phụ trong ngoặc đơn hoặc cột Tiếng Anh.
  - `type`: Tự động phân loại `dinh_nghia`, `tinh_chat`, `quy_tac`, `cong_thuc`...
  - `definition`: Lấy từ cột "Giải nghĩa" (giữ nguyên LaTeX `$ ... $`).
  - `chapter`, `lesson`: Ánh xạ chính xác theo đề mục của bài trong `progress.json`.
  - `notes`: Nếu thuộc mục "Ngoài nguồn" hoặc có trong "Ghi chú nguồn cần kiểm tra", tự động điền vào trường `notes` để gắn cờ trên Review Station.
- Khối `## 🎯 Yêu cầu cần đạt` từ Tầng 1 được ánh xạ thành mảng `lessons` tương ứng.

---

## 6. LỘ TRÌNH THỰC THI 4 GIAI ĐOẠN ĐỐI VỚI MÔN THÍ ĐIỂM SINH HỌC 12

### Giai đoạn 1: Xây dựng bộ công cụ lõi `textbook/core/`
1. Cài đặt `pymupdf` cho môi trường Python (`python -m pip install pymupdf`).
2. Viết module `pdf_extractor.py`:
   - Bóc tách text blocks kỹ thuật số ra `_raw_ocr/`.
   - Cắt ảnh raster và crop vector ở 300 DPI ra `img/` theo mã `H12-P...-C...-B...-XX.png`.
3. Viết module `dictionary_generator.py`:
   - Sinh file từ điển Markdown Tầng 2 theo đúng cấu trúc `_Huong-dan/Từ điển Sinh học 12.md`.
4. Viết module `glossary_parser.py` & `sync_station.py`:
   - Chuyển đổi từ điển Markdown thành `<unit>.json` và đẩy vào `review-station/data/glossary/`.

### Giai đoạn 2: Chuẩn hóa & Nạp dữ liệu Benchmark từ `_SGK-Nguyen-ban`
1. Khởi tạo thư mục `textbook/khoi_12/sinh_12/`.
2. Chuyển giao có chuẩn hóa các bài 1 đến 18 từ `_SGK-Nguyen-ban/Sinh-12/Phan-05-Di-truyen-hoc/` vào cấu trúc mới.
3. Sinh file từ điển Tầng 2 cho Chương 1 (Bài 1–6) với đầy đủ 5 mục Ngoài nguồn và 5 ghi chú nguồn cần kiểm tra.
4. Chạy `glossary_parser.py` sinh `sinh_12.json` và đồng bộ sang `review-station` để kiểm tra hiển thị.

### Giai đoạn 3: Tự động trích xuất các phần còn lại của Sinh học 12
1. Trích xuất **Phần 6: Tiến hoá** (Chương 5: Bài 19, 20, 21, 22 + Tóm tắt chương 5).
2. Trích xuất **Phần 7: Sinh thái học** (Chương 6 đến Chương 9: Bài 23 đến Bài 35).
3. Trích xuất Bảng thuật ngữ cuối sách (trang PDF 196–197).
4. Mở rộng bộ từ điển Tầng 2 cho toàn bộ các chương tiếp theo và đẩy vào `review-station`.

### Giai đoạn 4: Nghiệm thu trên Review Station & Đóng gói Framework đa môn
1. Mở `review-station` trên trình duyệt (http://localhost:8080), kiểm tra toàn bộ thẻ thuật ngữ và khung YCCĐ của Sinh học 12.
2. Kiểm tra tính năng xuất từ điển Markdown dạng bảng qua `dict_md.py`.
3. Đóng gói tài liệu hướng dẫn áp dụng Framework này để sẵn sàng code cho các môn tiếp theo (Toán 12, Vật lí 12, Hóa học 12...).

---

## 7. BƯỚC HÀNH ĐỘNG CỤ THỂ KHI BẮT ĐẦU CODE

Khi bạn xác nhận bản kế hoạch kiến trúc này, các bước code đầu tiên sẽ được triển khai ngay lập tức:
1. **Khởi tạo cấu trúc thư mục mới `textbook/core/` và `textbook/khoi_12/sinh_12/`**.
2. **Cài đặt thư viện `pymupdf`**.
3. **Lập trình các module Python lõi trong `textbook/core/`**.
4. **Chạy thử nghiệm toàn trình trên Bài 1–6 (Chương 1)**: Dựng bài Markdown nguyên bản Tầng 1 $\rightarrow$ Cắt ảnh 300 DPI $\rightarrow$ Sinh file Từ điển Tầng 2 chuẩn mẫu $\rightarrow$ Đẩy sang Review Station $\rightarrow$ Bật server Review Station để kiểm tra giao diện trực quan.
