# Bộ thuật ngữ `ngu_van_12` — Ngữ văn 12 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_12/ngu_van_12/ngu_van_12.json` (tập trung: `glossary/dataset/ngu_van_12.json`), gồm **60 thuật ngữ** (hoàn thành 2026-10-20). Truy vấn bằng `python glossary/scripts/query.py ngu_van_12`; không nạp cả file.

---

## 1. Phạm vi & Căn cứ tài liệu

Nguồn dữ liệu: thư mục `sgk/khoi_12/ngu_van_12/`, bộ sách Kết nối tri thức với cuộc sống (Nhà xuất bản Giáo dục Việt Nam).

| File | Loại sách | Phân loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|---|
| `SGK NGỮ VĂN 12-TẬP 1-KNTT.pdf` | sgk | `('sgk', 'co_ban')` | 174 | Nguồn chính Tập 1 (Bài 1 – Bài 5) | Không (ảnh, OCR) |
| `SGK NGỮ VĂN 12-TẬP 2-KNTT.pdf` | sgk | `('sgk', 'co_ban')` | 145 | Nguồn chính Tập 2 (Bài 6 – Bài 9) | Không (ảnh, OCR) |

### Quy tắc kỹ thuật đặc thù
- **Quy tắc offset số trang:** Cả Tập 1 và Tập 2 đều áp dụng đồng nhất quy tắc **`trang PDF = trang in + 4`**:
  + *Tập 1:* Tri thức ngữ văn Bài 1 (trang in 7–8) tại PDF trang 11–12; Bảng tra cứu thuật ngữ (trang in 161) tại PDF trang 165; Bảng giải thích thuật ngữ (trang in 162–163) tại PDF trang 166–167.
  + *Tập 2:* Tri thức ngữ văn Bài 6 (trang in 2–3) tại PDF trang 6–7; Bảng tra cứu thuật ngữ (trang in 132) tại PDF trang 136; Bảng giải thích thuật ngữ (trang in 133–134) tại PDF trang 137–138.
- **Cấu trúc phân cấp:** Môn Ngữ văn không chia chương mà chia theo Tập và Bài:
  + `chapter`: `"Tập một"` (chứa Bài 1 đến Bài 5) và `"Tập hai"` (chứa Bài 6 đến Bài 9).
  + `lesson`: Đặt tên chính xác theo mục lục SGK (`"Bài 1. Khả năng lớn lao của tiểu thuyết"`, v.v.).
- **Khai thác 100% hai Bảng giải thích thuật ngữ chuẩn SGK:**
  + *Tập 1 (PDF 166–167):* 21 thuật ngữ lý luận văn học & tiếng Việt then chốt (*Biểu tượng, Bút pháp dòng ý thức, Câu mơ hồ, Hài kịch, Nghịch ngữ, Ngôn ngữ hài kịch, Nhân vật hài kịch, Nói mỉa, Phong cách cổ điển, Phong cách hiện thực, Phong cách lãng mạn, Thao tác nghị luận, Thủ pháp đồng hiện, Thủ pháp trào phúng, Tiểu thuyết, Tiểu thuyết hiện đại, Tình huống hài kịch, Truyện truyền kì, Xung đột hài kịch, Yếu tố kì ảo, Yếu tố siêu thực*).
  + *Tập 2 (PDF 137–138):* 15 thuật ngữ (*Bài tập dự án, Dữ liệu sơ cấp, Dữ liệu thứ cấp, Giá trị giáo dục, Giá trị nhận thức, Giá trị thẩm mĩ, Giá trị văn hoá, Hồi kí, Loại hình văn học cách mạng, Ngôn ngữ thân mật, Ngôn ngữ trang trọng, Phóng sự, Quan điểm sáng tác, Quyền sở hữu trí tuệ, Thư từ*).
  + Tất cả 36 thuật ngữ này đều có mặt trong dataset, ưu tiên giữ nguyên văn định nghĩa từ Bảng và trích dẫn cả nguồn trang bảng lẫn nguồn trang bài học.

---

## 2. Danh mục bài và số thuật ngữ

| Tập | Bài học | Số thuật ngữ | Các thuật ngữ tiêu biểu |
|---|---|:---:|---|
| **Tập một** | Bài 1. Khả năng lớn lao của tiểu thuyết | 8 | tiểu thuyết, tiểu thuyết hiện đại, phong cách hiện thực, nói mỉa, nghịch ngữ, bút pháp dòng ý thức, thủ pháp đồng hiện, yêu cầu bài văn nghị luận so sánh đánh giá hai tác phẩm truyện |
| | Bài 2. Những thế giới thơ | 5 | biểu tượng, yếu tố siêu thực (trong thơ), phong cách cổ điển, phong cách lãng mạn, yêu cầu bài văn nghị luận so sánh đánh giá hai tác phẩm thơ |
| | Bài 3. Lập luận trong văn bản nghị luận | 11 | lập luận trong văn bản nghị luận, thao tác nghị luận, thao tác chứng minh, thao tác bình luận, thao tác bác bỏ, thao tác giải thích, thao tác phân tích, thao tác so sánh, lỗi logic của câu, câu mơ hồ, yêu cầu bài văn nghị luận về tuổi trẻ |
| | Bài 4. Yếu tố kì ảo trong truyện kể | 4 | truyện truyền kì, yếu tố kì ảo, nhân vật kì ảo, yêu cầu bài văn nghị luận về việc vay mượn - cải biến - sáng tạo |
| | Bài 5. Tiếng cười của hài kịch | 7 | hài kịch, nhân vật hài kịch, tình huống hài kịch, xung đột hài kịch, ngôn ngữ hài kịch, thủ pháp trào phúng (trong hài kịch), yêu cầu báo cáo nghiên cứu về một vấn đề tự nhiên xã hội |
| **Tập hai** | Bài 6. Hồ Chí Minh - "Văn hoá phải soi đường cho quốc dân đi" | 5 | quan điểm sáng tác, loại hình văn học cách mạng, tính khẳng định phủ định trong văn bản nghị luận, bài tập dự án, yêu cầu báo cáo kết quả của bài tập dự án |
| | Bài 7. Sự thật trong tác phẩm kí | 5 | phóng sự, hồi kí, ngôn ngữ trang trọng, ngôn ngữ thân mật, yêu cầu bài văn nghị luận bàn về cách ứng xử của tuổi trẻ |
| | Bài 8. Dữ liệu trong văn bản thông tin | 6 | dữ liệu trong văn bản thông tin, dữ liệu sơ cấp, dữ liệu thứ cấp, quyền sở hữu trí tuệ, thư từ, yêu cầu viết thư trao đổi về công việc |
| | Bài 9. Văn học và cuộc đời | 9 | giá trị nhận thức, giá trị giáo dục, giá trị thẩm mĩ, giá trị văn hoá, chủ đề, tư tưởng, cảm hứng, giữ gìn và phát triển tiếng Việt, yêu cầu bài phát biểu phát động phong trào |
| **Tổng** | **9 bài học** | **60** | **Toàn bộ chương trình Ngữ văn 12 KNTT** |

---

## 3. Thống kê chi tiết theo `type`, `level`, nguồn

### Phân bố theo loại thuật ngữ (`type`)
| Loại thuật ngữ | Số lượng | Tỉ lệ | Mô tả |
|---|:---:|:---:|---|
| `dinh_nghia` | 49 | 81.7% | Định nghĩa khái niệm thể loại, lý luận văn học, tiếng Việt, kiểu văn bản |
| `quy_tac` | 10 | 16.7% | Yêu cầu và quy tắc đối với các kiểu bài viết (nghị luận, báo cáo, thư từ, phát biểu) và chuẩn mực giữ gìn tiếng Việt |
| `tinh_chat` | 1 | 1.6% | Tính chất song hành khẳng định - phủ định trong văn bản nghị luận |
| `cong_thuc` | 0 | 0.0% | Đặc thù môn Ngữ văn không có công thức toán/lý/hoá |
| `ky_hieu` | 0 | 0.0% | Không có ký hiệu toán học |
| **Tổng cộng** | **60** | **100%** | |

### Phân bố theo cấp độ (`level`)
- `co_ban`: 60 thuật ngữ (100.0%). Toàn bộ nguồn từ SGK chuẩn cơ bản.

### Phân bố theo nguồn sách
- `SGK NGỮ VĂN 12-TẬP 1-KNTT.pdf`: 56 lượt trích dẫn nguồn.
- `SGK NGỮ VĂN 12-TẬP 2-KNTT.pdf`: 40 lượt trích dẫn nguồn.
- Đa số các thuật ngữ lý luận then chốt có 2 nguồn song song: nguồn từ Khung tri thức bài học và nguồn từ Bảng giải thích thuật ngữ cuối sách.

---

## 4. Yêu cầu cần đạt và cấu trúc sư phạm môn Ngữ văn 12

1. **Đọc - hiểu thể loại chuyên sâu cấp THPT:**
   - *Tiểu thuyết hiện đại:* Nắm vững cảm quan đời sống hiện đại, kết cấu đa tầng tuyến tính / phi tuyến tính, nhân vật "nếm trải", bút pháp dòng ý thức và thủ pháp đồng hiện.
   - *Thơ hiện đại & siêu thực:* Hiểu cách tổ chức hình ảnh thơ qua dòng tiềm thức, biểu tượng nghệ thuật, so sánh phong cách cổ điển và lãng mạn.
   - *Văn bản nghị luận:* Nhận diện và phối hợp nhuần nhuyễn 6 thao tác nghị luận (chứng minh, bình luận, bác bỏ, giải thích, phân tích, so sánh); tính khẳng định - phủ định; khắc phục lỗi logic và câu mơ hồ.
   - *Truyện truyền kì:* Hiểu bản chất yếu tố kì ảo, nhân vật kì ảo trong việc phản ánh hiện thực xã hội và tư tưởng nhân văn.
   - *Hài kịch:* Nắm vững tiếng cười châm biếm, xung đột hài kịch, tình huống hài kịch, nhân vật trào phúng và các thủ pháp tạo tiếng cười.
   - *Kí hiện đại (phóng sự, hồi kí):* Bản chất của sự thật đời sống trong tác phẩm kí; phân biệt và vận dụng ngôn ngữ trang trọng với ngôn ngữ thân mật.
   - *Văn bản thông tin:* Vai trò then chốt của dữ liệu; phân biệt chính xác dữ liệu sơ cấp và dữ liệu thứ cấp; tôn trọng quyền sở hữu trí tuệ.
   - *Các giá trị của văn học:* Bốn giá trị cốt lõi của tác phẩm văn học đối với cuộc sống: nhận thức, giáo dục, thẩm mĩ và văn hoá; mối liên hệ giữa chủ đề, tư tưởng và cảm hứng sáng tạo.

2. **Kĩ năng Viết & Nói - Nghe:**
   - Viết bài văn nghị luận so sánh, đánh giá hai tác phẩm truyện / thơ.
   - Viết bài văn nghị luận về một vấn đề liên quan đến tuổi trẻ (hoài bão, ước mơ, cách ứng xử trong các mối quan hệ).
   - Viết bài nghị luận về việc vay mượn - cải biến - sáng tạo văn học.
   - Viết báo cáo nghiên cứu về vấn đề tự nhiên, xã hội; báo cáo kết quả bài tập dự án.
   - Viết thư trao đổi công việc hoặc vấn đề xã hội theo quy chuẩn.
   - Viết bài phát biểu phát động phong trào, hoạt động cộng đồng.

---

## 5. Lưu ý phương pháp & đặc thù biên soạn môn Ngữ văn

1. **Tính nguyên văn và độ trung thực:**
   - Toàn bộ định nghĩa thuật ngữ được trích xuất nguyên văn 100% từ SGK (Khung Tri thức ngữ văn và Bảng giải thích thuật ngữ cuối sách), không tự ý viết lại hay diễn giải suy diễn.
   - Đối với các yêu cầu quy tắc viết, trích dẫn đầy đủ các tiêu chí cốt lõi trong khung Yêu cầu của bài học.
2. **Hệ thống bí danh (Aliases):**
   - Đảm bảo bổ sung aliases bao quát các cách diễn đạt tương đương thường dùng trong thân bài SGK: ví dụ `thao tác chứng minh` có alias `chứng minh`; `lập luận trong văn bản nghị luận` có alias `lập luận`; `thủ pháp trào phúng (trong hài kịch)` có alias `thủ pháp trào phúng`.
3. **Liên kết thuật ngữ liên cấp (`related_terms`):**
   - Kết nối có hệ thống giữa các thuật ngữ lớp 12 và lớp 10, 11 (ví dụ `ngu-van-10-tieu-thuyet`, mối quan hệ giữa `thao tác nghị luận` và các thao tác con, giữa `hài kịch` và các yếu tố cấu thành hài kịch).

---

## 6. Kết quả kiểm tra chất lượng & Kiểm định mẫu

- **Kiểm tra cú pháp & tính toàn vẹn (`validate.py`):**
  ```bash
  python glossary/scripts/validate.py ngu_van_12
  ```
  -> **KẾT QUẢ: OK (60 thuật ngữ, 0 lỗi).**
- **Kiểm tra trích dẫn nguồn PDF (`check_sources.py`):**
  ```bash
  python glossary/scripts/check_sources.py ngu_van_12
  ```
  -> **KẾT QUẢ:**
  + Tổng: 60 thuật ngữ.
  + **Đạt: 60 / 60 (100%).**
  + **Gắn cờ: 0 (0%).**
  + Không kiểm tra được: 0.
  + Cảnh báo: 9 mục (đều là các quy tắc viết kiểu bài văn/báo cáo có bigram rất cao từ 0.73 đến 1.00, hoàn toàn hợp lệ).
- **Kiểm định mẫu ngẫu nhiên độc lập (`query.py --audit --sample 30`):**
  + Mẫu kiểm định gồm 30 thuật ngữ ngẫu nhiên (50% toàn bộ dataset), đối soát trang in, số trang PDF, văn bản định nghĩa và liên kết bài học.
  + Tỉ lệ sai sót: **0.0%**.
