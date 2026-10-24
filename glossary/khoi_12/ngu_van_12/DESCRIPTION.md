# Bộ thuật ngữ `ngu_van_12` — Ngữ văn 12 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_12/ngu_van_12/ngu_van_12.json` (tập trung: `glossary/dataset/ngu_van_12.json`), gồm **78 thuật ngữ** (SGK 60, hoàn thành 2026-10-20; SCD 18, bổ sung 2026-10-24). Truy vấn bằng `python glossary/scripts/query.py ngu_van_12`; không nạp cả file.

---

## 1. Phạm vi & Căn cứ tài liệu

Nguồn dữ liệu: thư mục `sgk/khoi_12/ngu_van_12/`, bộ sách Kết nối tri thức với cuộc sống (Nhà xuất bản Giáo dục Việt Nam).

| File | Loại sách | Phân loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|---|
| `SGK NGỮ VĂN 12-TẬP 1-KNTT.pdf` | sgk | `('sgk', 'co_ban')` | 174 | Nguồn chính Tập 1 (Bài 1 – Bài 5) | Không (ảnh, OCR) |
| `SGK NGỮ VĂN 12-TẬP 2-KNTT.pdf` | sgk | `('sgk', 'co_ban')` | 145 | Nguồn chính Tập 2 (Bài 6 – Bài 9) | Không (ảnh, OCR) |
| `SCD van 12.pdf` | scd | `('scd', 'chuyen_de')` | 95 | Chuyên đề 1–3 (mỗi chuyên đề 3 Phần); bổ sung 2026-10-24. `trang PDF = trang in + 2`. 15 thuật ngữ lấy từ Bảng giải thích một số thuật ngữ (PDF 86–87), 12 mục `lessons` (khung "Yêu cầu cần đạt" ở đầu mỗi chuyên đề và khung "Yêu cầu" ở đầu mỗi Phần). `chapter` = `Chuyên đề N. …`, `lesson` = `Phần N. …` hoặc `null` (khung của cả chuyên đề) | Không (ảnh, OCR) |
| `SGV Ngữ văn 12 - Tập 1.pdf`, `SGV Ngữ văn 12 - Tập 2.pdf` | gv | `('gv', 'co_ban')` | 146 / 114 | Đã đăng kí vào `progress.json` theo bài (trang PDF = trang in + 1); chưa trích mục 4–5 vào DESCRIPTION | Không (ảnh, OCR) |

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
| **Tổng SGK** | **9 bài học** | **60** | **Toàn bộ chương trình Ngữ văn 12 KNTT** |

**Chuyên đề học tập (SCD, `level: chuyen_de`, 18 mục):** thuật ngữ gắn với `Phần 1` của mỗi chuyên đề (phần "Tri thức tổng quát" và Bảng giải thích đứng trước Phần 1).

| Chuyên đề | Lesson | Số thuật ngữ | Thuật ngữ |
|---|---|:---:|---|
| Chuyên đề 1. Tập nghiên cứu và viết báo cáo về một vấn đề văn học hiện đại | Phần 1. Tìm hiểu một số hướng nghiên cứu văn học hiện đại | 11 | cách tân, cảm quan hiện đại, chủ nghĩa hậu hiện đại, chủ nghĩa hiện đại, chủ nghĩa hiện thực, chủ nghĩa siêu thực, chủ nghĩa tượng trưng, lối viết tự động, trào lưu văn học, trường phái văn học, văn học hiện đại |
| Chuyên đề 2. Tìm hiểu về một tác phẩm nghệ thuật chuyển thể từ văn học | Phần 1. Thưởng thức một tác phẩm nghệ thuật được chuyển thể từ văn học | 4 | chuyển thể tác phẩm văn học, chuyển thể, chuyển thể bám sát tác phẩm gốc, chuyển thể ít bám sát tác phẩm gốc |
| Chuyên đề 3. Tìm hiểu phong cách sáng tác của một trường phái văn học: cổ điển, hiện thực hoặc lãng mạn | Phần 1. Tìm hiểu cách nghiên cứu phong cách sáng tác của một trường phái văn học | 3 | chủ nghĩa cổ điển, chủ nghĩa lãng mạn, phong cách sáng tác (của một trường phái văn học) |
| **Tổng SCD** | | **18** | 15 mục từ Bảng giải thích thuật ngữ (SCD PDF 86–87) + 3 mục từ "Tri thức tổng quát" của Chuyên đề 2 (PDF 36–37) |

SCD đánh số trang `PDF = in + 2`. Lọc: `query.py ngu_van_12 --level chuyen_de`.
---

## 3. Thống kê chi tiết theo `type`, `level`, nguồn

### Phân bố theo loại thuật ngữ (`type`)
| Loại thuật ngữ | Số lượng | Tỉ lệ | Mô tả |
|---|:---:|:---:|---|
| `dinh_nghia` | 67 | 85.9% | Định nghĩa khái niệm thể loại, lý luận văn học, tiếng Việt, kiểu văn bản (SGK 49, SCD 18) |
| `quy_tac` | 10 | 12.8% | Yêu cầu và quy tắc đối với các kiểu bài viết (nghị luận, báo cáo, thư từ, phát biểu) và chuẩn mực giữ gìn tiếng Việt (chỉ SGK) |
| `tinh_chat` | 1 | 1.3% | Tính chất song hành khẳng định - phủ định trong văn bản nghị luận (chỉ SGK) |
| `cong_thuc` | 0 | 0.0% | Đặc thù môn Ngữ văn không có công thức toán/lý/hoá |
| `ky_hieu` | 0 | 0.0% | Không có ký hiệu toán học |
| **Tổng cộng** | **78** | **100%** | |

### Phân bố theo cấp độ (`level`)
- `co_ban`: 60 thuật ngữ (76.9%), nguồn SGK.
- `chuyen_de`: 18 thuật ngữ (23.1%), nguồn `SCD van 12.pdf`.

### Phân bố theo nguồn sách
- `SGK NGỮ VĂN 12-TẬP 1-KNTT.pdf`: 56 lượt trích dẫn nguồn.
- `SGK NGỮ VĂN 12-TẬP 2-KNTT.pdf`: 40 lượt trích dẫn nguồn.
- `SCD van 12.pdf`: 20 lượt trích dẫn nguồn.
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

3. **Chuyên đề học tập Ngữ văn 12 (SCD, 12 mục `lessons` `chuyen_de`):** nguồn là khung "Yêu cầu cần đạt" ở đầu mỗi chuyên đề (`lesson: null`) và khung "Yêu cầu" ở đầu mỗi Phần (`lesson: Phần N. …`), theo cách đã làm ở `ngu_van_10`.
   - *Chuyên đề 1 (SCD PDF 6):* biết yêu cầu và cách thức nghiên cứu một vấn đề văn học hiện đại; viết báo cáo nghiên cứu; vận dụng hiểu biết để đọc, viết về văn học hiện đại; thuyết trình về vấn đề đã tìm hiểu.
   - *Chuyên đề 2 (PDF 36):* hiểu thế nào là chuyển thể tác phẩm văn học; biết cách tìm hiểu, giới thiệu, thuyết trình về tác phẩm nghệ thuật chuyển thể; nêu ý tưởng và cách thức chuyển thể.
   - *Chuyên đề 3 (PDF 58):* nhận biết phong cách sáng tác của một trường phái (trào lưu) qua đặc điểm cơ bản; biết viết bài giới thiệu; vận dụng để tìm hiểu trường phái khác; biết thuyết trình.
   - Truy vấn: `query.py ngu_van_12 --lessons --level chuyen_de`.

4. **Cấu trúc và tỉ lệ thời gian (SGV Ngữ văn 12 Tập 1, tr.12–13, PDF 13–14):** SGV có bảng phân phối tiết cho 9 bài + 2 lần kiểm tra/ôn tập (Bài 1: 11 tiết; Bài 2: 11; Bài 3: 10; Bài 4: 9; Bài 5: 8; Bài 6 (HCM): 12; Bài 7: 11; Bài 8: 11; Bài 9: 11; Kiểm tra giữa kì và cuối kì I, ôn tập: 2+1+2 = tổng 54 tiết học kì I; học kì II tổng 51 tiết). Mỗi bài chia ba nhóm hoạt động Đọc, Viết, Nói và nghe; Đọc có phần Thực hành tiếng Việt.

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
  -> **KẾT QUẢ: OK (60 thuật ngữ, 0 lỗi); cập nhật 2026-10-24 sau khi thêm SCD: OK (78 thuật ngữ, 23 bài YCCĐ, 0 lỗi).**
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

### Lưu ý sư phạm từ SGV Ngữ văn 12 (Tập 1 PDF 13–16, tức SGV tr.12–15)

SGV không có mục riêng về sai lầm của học sinh. Các điểm dưới đây là chỉ dẫn sư phạm SGV nêu rõ, agent sinh câu hỏi cần lưu ý:
- **Câu hỏi đọc không dồn vào bước "Củng cố, luyện tập"**: các câu hỏi cuối chuỗi câu hỏi đọc thường có độ khó cao hơn và nên dùng cho bước Củng cố, luyện tập và Vận dụng (SGV tr.12).
- **Mối liên hệ giữa các bài**: Bài 2 (thơ) chạm tới phong cách cổ điển, lãng mạn, yếu tố tượng trưng, siêu thực mà HS đã tích luỹ ở lớp 10, 11; kiểu bài viết ở Bài 3 và Bài 7 tương tự nhau (SGV tr.14). Câu hỏi nên kiểm tra khả năng kết nối, không chỉ ghi nhớ một bài.
- **Đánh giá**: SGV nhấn mạnh đánh giá hằng ngày, bám sát hoạt động của HS, không quy gọn vào chấm bài theo nghĩa cổ điển (SGV tr.15).
- Bộ chỉ chứa khái niệm xuất hiện trong SGK/SCD của bộ; SGV Ngữ văn 12 chỉ dùng để xác định yêu cầu cần đạt và phạm vi dạy học, không bổ sung thuật ngữ mới.

### Phần Chuyên đề học tập (SCD)
- **Nguồn thuật ngữ SCD:** chủ yếu Bảng giải thích một số thuật ngữ (PDF 86–87; 15 mục) và khung "Tri thức tổng quát" của Chuyên đề 2 (PDF 36–37; 3 mục). Phần "Tri thức tổng quát" của Chuyên đề 1 và 3 là văn bản diễn giải dài (đặc trưng của văn học hiện đại, các trường phái) **không được tách thành mục** để tránh diễn giải sai; khái niệm trọng tâm của chúng đã có trong Bảng giải thích.
- **Thuật ngữ trùng lớp 10:** `chủ nghĩa lãng mạn`, `trường phái văn học`, `biểu tượng`, ... xuất hiện ở lớp 10, 11; mỗi lớp giữ định nghĩa theo sách lớp đó (README mục 6), chưa nối `related_terms` chéo lớp cho các mục SCD.

### Kiểm tra phần Chuyên đề học tập (SCD) — 2026-10-24
| Hạng mục | Kết quả |
|---|---|
| `check_sources.py` | Cả bộ: 78 mục, 73 đạt, 5 gắn cờ (đều ở SCD PDF 87: tên thuật ngữ xuống dòng trong ô bảng nên OCR không khớp cụm; định nghĩa khớp bigram 0,93–0,98; đã đối chiếu ảnh và ghi `notes`). YCCĐ: 23/23 đạt |
| Kiểm tra mẫu | 18/18 mục SCD (100%): đối chiếu từng mục với ảnh Bảng giải thích PDF 86–87 và khung Tri thức tổng quát PDF 36–37 (nguyên văn, trang PDF, `printed_page = PDF − 2`). Số mục sai: **0** |
| Kiểm tra độc lập | Chưa làm |
