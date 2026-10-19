# Bộ thuật ngữ `dia_11` — Địa lí 11 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_11/dia_11/dia_11.json` (tập trung: `glossary/dataset/dia_11.json`), gồm **103 thuật ngữ** (cập nhật 2026-10-19). Truy vấn bằng `query.py`; không nạp cả file vào ngữ cảnh prompt.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_11/dia_11/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK DIA LI 11 - KNTT.pdf | sgk | 171 | Nguồn chính, Phần một (Bài 1–5) + Phần hai (Bài 6–31), `level: co_ban` | Không (ảnh, OCR) |
| SCD DIA LI 11 - KNTT.pdf | scd | 65 | Chuyên đề 1–3, chia mục La Mã, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV Dia li 11 KNTT.pdf | gv | 214 | Mục tiêu từng bài, định hướng sư phạm (mục 4–5) | Không (ảnh, OCR) |

- **Quy tắc offset số trang:**
  + **SGK:** **`trang PDF = trang in + 2`** (Ví dụ: Bài 1 trang in 5 tại PDF 7; Bài 2 trang in 9 tại PDF 11; Bảng tra cứu thuật ngữ trang in 165 tại PDF 167).
  + **SCD:** **`trang PDF = trang in + 2`** (Ví dụ: Chuyên đề 1 mục I trang in 5 tại PDF 7; Bảng tra cứu thuật ngữ trang in 59 tại PDF 61).
  + **SGV:** **`trang PDF = trang in + 1`** (Ví dụ: Hướng dẫn dạy học từng bài trang in 25 tại PDF 26).
- **Cấu trúc phân cấp:**
  + SGK: `chapter` = `"Phần một. Một số vấn đề về kinh tế - xã hội thế giới"` (Bài 1 đến 5) hoặc `"Phần hai. Địa lí khu vực và quốc gia"` (Bài 6 đến 31); `lesson` = `"Bài N. …"` (đánh số liên tục 1–31).
  + SCD: `chapter` = `"Chuyên đề 1. Một số vấn đề về khu vực Đông Nam Á"`, `"Chuyên đề 2. Một số vấn đề về du lịch thế giới"`, `"Chuyên đề 3. Cuộc cách mạng công nghiệp lần thứ tư (4.0)"`; `lesson` = mục La Mã đầy đủ (`"I. Uỷ hội sông Mê Công (MRC)"`, `"II. Hợp tác hoà bình trong khai thác Biển Đông"`, ...).
- **Bảng tra cứu thuật ngữ cuối sách:**
  + SGK có bảng giải thích thuật ngữ ở PDF 167 (trang in 165, 9 thuật ngữ then chốt: *Hàng rào phi thuế quan, Bảo hộ mậu dịch/thương mại, Cải cách kinh tế, Chuỗi giá trị toàn cầu, Chuyển dịch cơ cấu kinh tế, Công nghệ, Công ty đa quốc gia, Dân tộc, Kinh tế tri thức*).
  + SCD có bảng ở PDF 61 (trang in 59, 8 thuật ngữ chuyên đề 4.0 & du lịch: *Cách mạng công nghiệp, Công nghệ cao, Công nghệ thực tế ảo, Đổi mới sáng tạo, Kinh tế chia sẻ, Kinh tế xanh, Loại hình du lịch, Mô hình tăng trưởng kinh tế*).
  + Toàn bộ 17 thuật ngữ từ 2 bảng tra cứu đều có mặt trong glossary, giữ nguyên văn định nghĩa từ bảng, mang cấu trúc nguồn kép: trích dẫn cả trang bảng tra cứu (`rank 0`, bigram 1.00) lẫn trang bài học tương ứng trong thân bài (`rank 1`).

## 2. Chương/bài và số thuật ngữ

| Chương / Chuyên đề | Bài / Mục | Số mục |
|---|---|---|
| **Phần một. Một số vấn đề về kinh tế - xã hội thế giới** | Bài 1. Sự khác biệt về trình độ phát triển kinh tế - xã hội của các nhóm nước | 7 |
|  | Bài 2. Toàn cầu hoá và khu vực hoá kinh tế | 6 |
|  | Bài 3. Thực hành: Tìm hiểu về cơ hội và thách thức của toàn cầu hoá và khu vực hoá kinh tế | 1 |
|  | Bài 4. Một số tổ chức quốc tế và khu vực, an ninh toàn cầu | 10 |
|  | Bài 5. Thực hành: Viết báo cáo về đặc điểm và biểu hiện của nền kinh tế tri thức | 2 |
| **Phần hai. Địa lí khu vực và quốc gia** | Bài 6. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội khu vực Mỹ La-tinh | 3 |
|  | Bài 7. Kinh tế khu vực Mỹ La-tinh | 3 |
|  | Bài 8. Thực hành: Viết báo cáo về tình hình phát triển kinh tế - xã hội ở Cộng hoà Liên bang Bra-xin | 1 |
|  | Bài 9. Liên minh châu Âu - Một liên kết kinh tế khu vực lớn | 5 |
|  | Bài 10. Thực hành: Viết báo cáo về sự phát triển công nghiệp của Cộng hoà Liên bang Đức | 1 |
|  | Bài 11. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội khu vực Đông Nam Á | 4 |
|  | Bài 12. Kinh tế khu vực Đông Nam Á | 3 |
|  | Bài 13. Hiệp hội các quốc gia Đông Nam Á (ASEAN) | 3 |
|  | Bài 14. Thực hành: Tìm hiểu hoạt động kinh tế đối ngoại của khu vực Đông Nam Á | 1 |
|  | Bài 15. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội khu vực Tây Nam Á | 3 |
|  | Bài 16. Kinh tế khu vực Tây Nam Á | 1 |
|  | Bài 17. Thực hành: Viết báo cáo về vấn đề dầu khí của khu vực Tây Nam Á | 1 |
|  | Bài 18. Vị trí địa lí, điều kiện tự nhiên và dân cư Hoa Kỳ | 2 |
|  | Bài 19. Kinh tế Hoa Kỳ | 2 |
|  | Bài 20. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội Liên bang Nga | 2 |
|  | Bài 21. Kinh tế Liên bang Nga | 2 |
|  | Bài 22. Thực hành: Tìm hiểu về công nghiệp khai thác dầu khí của Liên bang Nga | 1 |
|  | Bài 23. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội Nhật Bản | 2 |
|  | Bài 24. Kinh tế Nhật Bản | 1 |
|  | Bài 25. Thực hành: Viết báo cáo về hoạt động kinh tế đối ngoại của Nhật Bản | 1 |
|  | Bài 26. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội Trung Quốc | 3 |
|  | Bài 27. Kinh tế Trung Quốc | 1 |
|  | Bài 28. Thực hành: Viết báo cáo về sự thay đổi của kinh tế vùng duyên hải Trung Quốc | 1 |
|  | Bài 29. Thực hành: Tìm hiểu về kinh tế của Ô-xtrây-li-a | 1 |
|  | Bài 30. Vị trí địa lí, điều kiện tự nhiên, dân cư và xã hội Cộng hoà Nam Phi | 1 |
|  | Bài 31. Kinh tế Cộng hoà Nam Phi | 2 |
| **Chuyên đề 1. Một số vấn đề về khu vực Đông Nam Á** | I. Uỷ hội sông Mê Công (MRC) | 2 |
|  | II. Hợp tác hoà bình trong khai thác Biển Đông | 4 |
| **Chuyên đề 2. Một số vấn đề về du lịch thế giới** | I. Tài nguyên du lịch thế giới | 2 |
|  | II. Một số loại hình du lịch phổ biến trên thế giới | 7 |
|  | III. Xu hướng phát triển du lịch trên thế giới và định hướng phát triển du lịch ở Việt Nam | 2 |
|  | IV. Định hướng nghề nghiệp | 3 |
| **Chuyên đề 3. Cuộc cách mạng công nghiệp lần thứ tư (4.0)** | I. Nội dung chủ yếu | 4 |
|  | II. Tác động của cách mạng công nghiệp 4.0 đến phát triển kinh tế - xã hội thế giới | 1 |
|  | III. Một số xu hướng chính của cuộc cách mạng công nghiệp 4.0 | 1 |

Toàn bộ 31 bài học SGK và 9 mục chuyên đề đều có thuật ngữ đại diện (độ phủ 100%).

## 3. Thống kê theo `type`, `level`, nguồn

| Phân loại | Số lượng | Tỉ lệ |
|---|---|---|
| **Theo `type`** | | |
| `tinh_chat` | 69 | 67.0% |
| `dinh_nghia` | 34 | 33.0% |
| `cong_thuc` | 0 | 0% |
| `quy_tac` | 0 | 0% |
| `dinh_ly` | 0 | 0% |
| `ky_hieu` | 0 | 0% |
| **Theo `level`** | | |
| `co_ban` (SGK) | 77 | 74.8% |
| `chuyen_de` (SCD) | 26 | 25.2% |
| **Theo nguồn trích dẫn** | | |
| SGK làm nguồn chính | 77 | 74.8% |
| SCD làm nguồn chính | 26 | 25.2% |
| Nguồn kép (trang bảng tra cứu + trang bài học) | 17 | 16.5% |

Đặc thù môn Địa lí 11 là Địa lí kinh tế - xã hội khu vực và thế giới: các khái niệm định chế, tổ chức quốc tế và các chỉ số kinh tế xã hội được phân định vào `dinh_nghia`; các đặc điểm tự nhiên, dân cư, phân bố kinh tế, hoạt động ngoại thương và xu thế phát triển ngành/khu vực được chuẩn hoá thành `tinh_chat`.

## 4. Yêu cầu cần đạt theo chương

Nguồn: `SGV Dia li 11 KNTT.pdf` (phần “I. Mục tiêu và nội dung chương trình Địa lí 11”, PDF tr.7–11 và phần hướng dẫn từng bài):

- **Phần một. Một số vấn đề về kinh tế - xã hội thế giới** (Bài 1–5):
  + Phân biệt được các nhóm nước phát triển và đang phát triển dựa trên chỉ tiêu GNI/người, cơ cấu kinh tế và chỉ số phát triển con người (HDI).
  + Trình bày được các biểu hiện, hệ quả của toàn cầu hoá và khu vực hoá kinh tế; cơ hội và thách thức đối với các nước đang phát triển.
  + Nắm vững vai trò của các tổ chức quốc tế lớn (UN, WTO, IMF, WB) và diễn đàn khu vực (APEC); nhận diện các vấn đề an ninh toàn cầu (an ninh năng lượng, lương thực, nguồn nước, an ninh mạng) và an ninh con người.
  + Phân tích được khái niệm, đặc điểm và các biểu hiện chủ yếu của nền kinh tế tri thức.
- **Phần hai. Địa lí khu vực và quốc gia** (Bài 6–31):
  + **Mỹ La-tinh (Bài 6–8):** Phân tích vị trí chiến lược, tài nguyên thiên nhiên phong phú (khoáng sản, rừng A-ma-dôn, đất đai), vấn đề đô thị hoá tự phát và chênh lệch giàu nghèo; nắm bắt tình hình kinh tế Bra-xin.
  + **Liên minh châu Âu - EU (Bài 9–10):** Trình bày mục tiêu, thể chế hoạt động, bốn mặt tự do lưu thông và vai trò là trung tâm kinh tế, thương mại hàng đầu thế giới; tình hình phát triển công nghiệp CHLB Đức.
  + **Khu vực Đông Nam Á (Bài 11–14):** Đánh giá vị trí cầu nối, tài nguyên nhiệt đới ẩm, đặc điểm dân cư - nguồn lao động; quá trình chuyển dịch kinh tế (nông nghiệp, công nghiệp, dịch vụ - du lịch); mục tiêu và ba trụ cột của Cộng đồng ASEAN.
  + **Khu vực Tây Nam Á (Bài 15–17):** Vị trí ngã ba ba châu lục, đặc điểm hoang mạc khô hạn, nguồn tài nguyên dầu mỏ khí đốt chiến lược và vấn đề an ninh năng lượng toàn cầu.
  + **Hoa Kỳ (Bài 18–19):** Phân tích vị trí cô lập thuận lợi, nguồn tài nguyên dồi dào, dân cư nhập cư đa dạng; quy mô nền kinh tế số 1 thế giới, thế mạnh công nghiệp công nghệ cao và dịch vụ hiện đại.
  + **Liên bang Nga (Bài 20–22):** Quy mô lãnh thổ rộng nhất thế giới, giàu khoáng sản và rừng taiga; các ngành kinh tế then chốt (năng lượng dầu khí, luyện kim, chế tạo máy) và sự phân hoá 12 vùng kinh tế.
  + **Nhật Bản (Bài 23–25):** Quốc đảo nghèo khoáng sản, nhiều thiên tai; cơ cấu dân số già; sức mạnh kinh tế dựa trên khoa học - công nghệ, hoạt động kinh tế đối ngoại năng động.
  + **Trung Quốc (Bài 26–28):** Đất nước rộng lớn, đông dân; sự tương phản sâu sắc giữa miền Đông phát triển và miền Tây nội lục; thành tựu cải cách mở cửa và các vùng kinh tế ven biển.
  + **Ô-xtrây-li-a (Bài 29):** Lục địa độc đáo, kinh tế phát triển cao, thế mạnh về khai khoáng và dịch vụ hiện đại.
  + **Cộng hoà Nam Phi (Bài 30–31):** Quốc gia ở mỏm nam châu Phi, giàu khoáng sản kim loại quý (bạch kim, vàng, kim cương), nền kinh tế công nghiệp - khai khoáng phát triển nhất châu Phi.
- **Chuyên đề học tập Địa lí 11** (SCD CĐ 1–3):
  + **Chuyên đề 1:** Khái quát cơ chế quản trị và phát triển bền vững tài nguyên nước lưu vực sông Mê Công của MRC; vị trí chiến lược của Biển Đông, khuôn khổ UNCLOS 1982, DOC và tiến trình xây dựng COC.
  + **Chuyên đề 2:** Phân loại tài nguyên du lịch (tự nhiên và văn hoá), các loại hình du lịch phổ biến (sinh thái, văn hoá, nghỉ dưỡng, mạo hiểm); xu hướng du lịch bền vững và phát triển du lịch xanh.
  + **Chuyên đề 3:** Nội dung then chốt của Cách mạng 4.0 (trí tuệ nhân tạo, Big Data, IoT, in 3D), tác động sâu rộng đến cơ cấu kinh tế - xã hội, các mô hình kinh tế mới (kinh tế chia sẻ, kinh tế tuần hoàn, kinh tế số) và định hướng nghề nghiệp.

## 5. Sai lầm thường gặp của học sinh

Tổng hợp từ các lưu ý sư phạm trong `SGV Dia li 11 KNTT.pdf`:

| Nội dung | Sai lầm / điểm dễ nhầm | Nguồn tham chiếu |
|---|---|---|
| **Phân loại nhóm nước (Bài 1)** | Căn cứ đơn thuần vào quy mô GDP để xếp loại nước phát triển: thực tế nhóm nước phát triển được xác định dựa trên **GNI bình quân đầu người cao, cơ cấu kinh tế dịch vụ/công nghiệp hiện đại và chỉ số HDI rất cao (≥ 0,800)**. Các nước quy mô GDP lớn như Trung Quốc, Ấn Độ vẫn là nước đang phát triển do GNI/người ở mức trung bình. | SGV tr.26–28; SGK tr.7–10 |
| **Toàn cầu hoá và khu vực hoá (Bài 2)** | Cho rằng khu vực hoá kinh tế đối lập hoặc cản trở toàn cầu hoá: thực chất khu vực hoá vừa thúc đẩy hợp tác sâu rộng nội khối, vừa là bước đệm bổ trợ và nâng cao năng lực hội nhập toàn cầu. | SGV tr.33–35; SGK tr.11–14 |
| **Bảo hộ thương mại (Bài 2)** | Nhầm bảo hộ thương mại là cấm vận xuất nhập khẩu: thực chất là việc chính phủ áp dụng các rào cản thuế quan (thuế nhập khẩu cao) và phi thuế quan (tiêu chuẩn kĩ thuật, vệ sinh, kiểm dịch) nhằm bảo vệ sản xuất nội địa. | SGK tr.14, 167 |
| **An ninh phi truyền thống (Bài 4)** | Đồng nhất an ninh quốc gia chỉ là an ninh chính trị - quân sự: Địa lí 11 nhấn mạnh an ninh phi truyền thống (an ninh lương thực, năng lượng, nguồn nước, an ninh mạng, biến đổi khí hậu) có tính xuyên quốc gia, đe dọa trực tiếp sự tồn vong của nhân loại. | SGV tr.43–45; SGK tr.18–21 |
| **Cơ cấu kinh tế Hoa Kỳ (Bài 19)** | Cho rằng nông nghiệp Hoa Kỳ lạc hậu do chỉ chiếm khoảng 1% GDP: thực tế nông nghiệp Hoa Kỳ hiện đại hoá cao độ, ứng dụng công nghệ sinh học và cơ giới hoá mạnh mẽ, là nước xuất khẩu nông sản hàng đầu thế giới. | SGV tr.131–133; SGK tr.90–95 |
| **Miền Đông và miền Tây Trung Quốc (Bài 26–27)** | Nhầm lẫn điều kiện và trình độ phát triển giữa hai miền: Miền Đông (đồng bằng phì nhiêu, khí hậu gió mùa, tập trung trên 90% dân số và các đô thị lớn, công nghiệp phát triển); Miền Tây (núi cao, hoang mạc khô hạn, dân cư thưa thớt, kinh tế chủ yếu nông nghiệp truyền thống). | SGV tr.174–178; SGK tr.133–144 |
| **Biển Đông & Thể chế pháp lí (CĐ 1)** | Đồng nhất tính chất của DOC và COC: DOC (2002) là Tuyên bố chính trị về ứng xử nhằm xây dựng lòng tin, không mang tính ràng buộc pháp lí; COC là Bộ Quy tắc ứng xử có hiệu lực pháp lí bắt buộc mà ASEAN và Trung Quốc đang tích cực đàm phán xây dựng. | SCD tr.25–28; SGV tr.104–106 |
| **Mô hình Cách mạng 4.0 (CĐ 3)** | Coi Cách mạng 4.0 chỉ là ứng dụng máy tính và internet: bản chất của 4.0 là sự tích hợp sâu rộng mang tính đột phá giữa thế giới số, thế giới vật lí và thế giới sinh học (AI, IoT, Big Data, in 3D, công nghệ sinh học). | SCD tr.50–55 |
| **Kinh tế chia sẻ & Kinh tế tuần hoàn (CĐ 3)** | Lẫn lộn giữa kinh tế chia sẻ (tối ưu hoá quyền sử dụng tài sản nhàn rỗi thông qua nền tảng số) và kinh tế tuần hoàn (chu trình khép kín giảm thiểu chất thải, tái sử dụng và tái chế tài nguyên). | SCD tr.53, 61 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Cả 3 file sách nguồn (`SGK DIA LI 11 - KNTT.pdf`, `SCD DIA LI 11 - KNTT.pdf`, `SGV Dia li 11 KNTT.pdf`) đều là PDF dạng ảnh quét (scanned image). Toàn bộ nội dung trích xuất đã được đối soát qua hệ thống OCR tesseract 300 dpi được tiền xử lý và lưu đệm tại thư mục `.ocr/`.
- File Chuyên đề học tập ban đầu có tên `SGK CHUYEN DE DIA LI 11 - KNTT.pdf` (tiền tố `SGK`) đã được đổi tên thành chuẩn `SCD DIA LI 11 - KNTT.pdf` để tương thích hoàn toàn với bộ phân loại `classify_book` trong `glossary/scripts/_common.py`.
- Các mục `tinh_chat` được trích lọc bám sát chuẩn hoá câu chữ của sách giáo khoa; các thuật ngữ có tên đề mục dài được bổ sung alias định danh chuẩn xác để đạt kết quả đối soát tối ưu.

**Kiểm tra tự động** (2026-10-19, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả | Ghi chú |
|---|---|---|
| `validate.py dia_11` | **0 lỗi; 103 thuật ngữ** | Đạt 100% schema.json, ID cú pháp chuẩn, cấu trúc metadata đồng bộ. |
| `check_sources.py dia_11` | **103 đạt, 0 gắn cờ, 0 không kiểm tra được, 0 cảnh báo** | Toàn bộ 103/103 thuật ngữ đều đạt tỷ lệ trùng khớp bigram ≥ 0.65 (đa số 0.85–1.00). |
| Trích dẫn kép bảng thuật ngữ | **17/17 thuật ngữ đạt 1.00 bigram** | 9 mục SGK tr.167 và 8 mục SCD tr.61 được khử nhiễu OCR dải hẹp, đối soát kép chuẩn xác với thân bài. |

**Kiểm định mẫu độc lập** (Giai đoạn 5, 2026-10-19):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/103 thuật ngữ (29.1% tổng tập dữ liệu) |
| Phương pháp chọn mẫu | Thực thi `python glossary/scripts/query.py dia_11 --audit --sample 30` (xuất ra `sample_audit.md`). |
| Đối soát thực tế trang PDF | Rà soát 30 mục ngẫu nhiên đại diện đều khắp các bài SGK (Bài 2, 4, 6, 7, 11, 12, 13, 14, 17, 18, 19, 21, 22, 23, 25, 26, 27, 30) và các Chuyên đề (CĐ 1, CĐ 2, CĐ 3). |
| Số mục sai lệch | **0/30 (0.0%, ngưỡng cho phép ≤ 5%)**: Tất cả định nghĩa và số trang in / số trang PDF đều khớp chính xác nguyên văn với ảnh trang sách. |

## 7. Liên hệ với các lớp khác

- **Với Địa lí 10 (`dia_10`):**
  + Kế thừa và vận dụng hệ thống quy luật địa lí tự nhiên (địa đới, phi địa đới, thạch quyển, khí quyển, thuỷ quyển) để giải thích sự phân hoá tự nhiên của các khu vực và châu lục trên thế giới.
  + Khái niệm nguồn lực kinh tế, cơ cấu kinh tế, đô thị hoá, chỉ số GDP và GNI đại cương ở Địa lí 10 được cụ thể hoá thành các chỉ số phát triển kinh tế - xã hội cụ thể ở từng nhóm nước và từng quốc gia điển hình ở Địa lí 11.
- **Với Địa lí 12 (`dia_12`):**
  + Tạo nền tảng so sánh vị thế địa chính trị và kinh tế của Việt Nam trong mối tương quan với các nước ASEAN, Đông Nam Á và thế giới.
  + Các vấn đề Biển Đông, hội nhập kinh tế quốc tế, kinh tế số và phát triển du lịch bền vững ở Chuyên đề Địa lí 11 là tiền đề trực tiếp cho các chủ đề địa lí kinh tế và an ninh quốc phòng Việt Nam ở Địa lí 12.
- **Liên môn:**
  + **Lịch sử 11 (`lich_su_11`):** Quá trình phát triển của chủ nghĩa tư bản, các cuộc cách mạng công nghiệp cận - hiện đại, phong trào giải phóng dân tộc ở Mỹ La-tinh, châu Á và châu Phi; quá trình hình thành Liên minh châu Âu (EU) và ASEAN.
  + **Giáo dục Kinh tế và Pháp luật 11 (`ktpl_11`):** Hội nhập kinh tế quốc tế, tự do thương mại, rào cản thuế quan, liên kết kinh tế khu vực và toàn cầu.
