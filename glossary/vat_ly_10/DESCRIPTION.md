# Bộ thuật ngữ `vat_ly_10` — Vật lí 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/vat_ly_10/vat_ly_10.json`, gồm **241 thuật ngữ** (cập nhật 2026-10-15). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `vat_ly_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Vat li 10.pdf | sgk | 142 | Nguồn chính, Chương I–VII (34 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD Vat li 10.pdf | scd | 82 | Chuyên đề 1–3 (10 bài), `level: chuyen_de` | Không (ảnh, OCR) |
| SGV VAT LI 10.pdf | gv | 134 | Mục tiêu từng bài, thông tin bổ sung, sai lầm thường gặp (mục 4–5); nguồn `gv` cho 10 thuật ngữ | Không (ảnh, OCR) |
| SGV CD VAT LI 10.pdf | gv | 66 | Bảng yêu cầu cần đạt và mục tiêu từng bài chuyên đề (mục 4); nguồn `gv` cho 2 thuật ngữ | Không (ảnh, OCR) |
| SBT VAT LI 10.pdf | sbt | 122 | Chỉ gồm câu hỏi, bài tập và lời giải; **không có khái niệm mới** → 0 mục | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Vật lí 10.pdf | gv | 61 | So sánh chương trình 2006 – 2018, cấu trúc SGK, chuyên đề (mục 4) | Có nhưng lỗi font, phải OCR ảnh |

- Ở năm sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- SGK (trang in 136–139, PDF 137–140) có bảng "Giải thích một số thuật ngữ dùng trong sách" (32 mục). Cả 32 mục đều đã có trong glossary và mang nguồn trang bảng. Bốn mục lấy định nghĩa trực tiếp từ bảng vì thân bài không định nghĩa: `co-hoc`, `dong-luc-hoc`, `hai-luc-can-bang`, `he-si` (kết hợp bảng đơn vị SI ở trang in 5). `luc-nang-cua-chat-luu` bổ sung một câu từ bảng.
- SCD (trang in 79, PDF 80) có "Bảng giải thích một số thuật ngữ" (9 mục), đều đã có trong glossary. `cach-mang-cong-nghiep` và `hieu-ung-nha-kinh` lấy định nghĩa từ bảng. Cột "Trang" của bảng SCD ghi lệch so với thân bài ở một số mục (Thuỷ triều ghi 28, thực tế ở trang in 53); `sources` dùng trang thật.
- Các bài thực hành (3, 6, 11, 22, 30) chủ yếu là quy trình đo. Chỉ trích khái niệm và quy tắc được nêu tường minh: sai số, cách ghi kết quả đo (Bài 3), dụng cụ đo thời gian (Bài 6). Bài 30 có 0 mục.
- SGK và SCD đều đánh số "Bài 1, 2, …". Khi lọc, kết hợp `--level` hoặc `--chapter`. Ví dụ: `--lesson "Bài 5." --level co_ban` là Bài 5 SGK (Tốc độ và vận tốc); `--lesson "Bài 5." --level chuyen_de` là Bài 5 Chuyên đề (thiên thể trên nền trời sao).

## 2. Chương/bài và số thuật ngữ

Bài không liệt kê (Bài 30) có 0 mục. SBT không bổ sung mục nào.

| Chương / Chuyên đề | Bài | Số mục |
|---|---|---|
| Chương I. Mở đầu | Bài 1. Làm quen với Vật lí | 8 |
|  | Bài 2. Các quy tắc an toàn trong phòng thực hành Vật lí | 7 |
|  | Bài 3. Thực hành tính sai số trong phép đo. Ghi kết quả đo | 12 |
| Chương II. Động học | Bài 4. Độ dịch chuyển và quãng đường đi được | 10 |
|  | Bài 5. Tốc độ và vận tốc | 7 |
|  | Bài 6. Thực hành: Đo tốc độ của vật chuyển động | 4 |
|  | Bài 7. Đồ thị độ dịch chuyển – thời gian | 3 |
|  | Bài 8. Chuyển động biến đổi. Gia tốc | 4 |
|  | Bài 9. Chuyển động thẳng biến đổi đều | 5 |
|  | Bài 10. Sự rơi tự do | 5 |
|  | Bài 11. Thực hành: Đo gia tốc rơi tự do | 1 |
|  | Bài 12. Chuyển động ném | 5 |
| Chương III. Động lực học | Bài 13. Tổng hợp và phân tích lực. Cân bằng lực | 7 |
|  | Bài 14. Định luật 1 Newton | 2 |
|  | Bài 15. Định luật 2 Newton | 3 |
|  | Bài 16. Định luật 3 Newton | 3 |
|  | Bài 17. Trọng lực và lực căng | 5 |
|  | Bài 18. Lực ma sát | 4 |
|  | Bài 19. Lực cản và lực nâng | 6 |
|  | Bài 20. Một số ví dụ về cách giải các bài toán thuộc phần động lực học | 1 |
|  | Bài 21. Moment lực. Cân bằng của vật rắn | 6 |
|  | Bài 22. Thực hành: Tổng hợp lực | 2 |
| Chương IV. Năng lượng, công, công suất | Bài 23. Năng lượng. Công cơ học | 7 |
|  | Bài 24. Công suất | 3 |
|  | Bài 25. Động năng, thế năng | 5 |
|  | Bài 26. Cơ năng và định luật bảo toàn cơ năng | 2 |
|  | Bài 27. Hiệu suất | 3 |
| Chương V. Động lượng | Bài 28. Động lượng | 4 |
|  | Bài 29. Định luật bảo toàn động lượng | 5 |
| Chương VI. Chuyển động tròn | Bài 31. Động học của chuyển động tròn đều | 6 |
|  | Bài 32. Lực hướng tâm và gia tốc hướng tâm | 3 |
| Chương VII. Biến dạng của vật rắn. Áp suất chất lỏng | Bài 33. Biến dạng của vật rắn | 8 |
|  | Bài 34. Khối lượng riêng. Áp suất chất lỏng | 5 |
| Chuyên đề 1. Vật lí trong một số ngành nghề | Bài 1. Sơ lược về sự phát triển của Vật lí học | 10 |
|  | Bài 2. Giới thiệu các lĩnh vực nghiên cứu trong Vật lí học | 15 |
|  | Bài 3. Giới thiệu các ứng dụng của Vật lí trong một số ngành nghề | 8 |
| Chuyên đề 2. Trái Đất và bầu trời | Bài 4. Xác định phương hướng | 8 |
|  | Bài 5. Đặc điểm chuyển động nhìn thấy của một số thiên thể trên nền trời sao | 9 |
|  | Bài 6. Nhật thực, nguyệt thực, thuỷ triều | 6 |
| Chuyên đề 3. Vật lí với giáo dục bảo vệ môi trường | Bài 7. Sự cần thiết phải bảo vệ môi trường | 4 |
|  | Bài 8. Tác động của việc sử dụng năng lượng hiện nay đối với Việt Nam | 5 |
|  | Bài 9. Sơ lược về các chất gây ô nhiễm môi trường | 7 |
|  | Bài 10. Năng lượng tái tạo và một số công nghệ thu năng lượng tái tạo | 8 |

Bốn mục chỉ có trong bảng thuật ngữ SGK được xếp vào bài gần nhất: `co-hoc` → Bài 1, `he-si` → Bài 3 (kèm nguồn trang "Một số đơn vị cơ bản và dẫn xuất", PDF 6), `dong-luc-hoc` và `hai-luc-can-bang` → Bài 13.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 150 |
| cong_thuc | 37 |
| tinh_chat | 25 |
| quy_tac | 16 |
| dinh_ly | 10 |
| ky_hieu | 3 |

- Theo `level`: `co_ban` 161, `chuyen_de` 80.
- Theo nguồn định nghĩa: SGK 161, SCD 80, SBT 0. 12 mục mang thêm nguồn `gv` (10 từ SGV, 2 từ SGV CD); định nghĩa vẫn giữ theo SGK/SCD.
- 79 mục có `notation` (LaTeX). Kí hiệu vận tốc theo SGK: $\upsilon$ (tốc độ, đại lượng vô hướng) khác $v$ / $\vec{v}$ (vận tốc). Công suất dùng $\mathscr{P}$; động năng $W_đ$.
- `dinh_ly`: định luật 1, 2, 3 Newton, dạng tổng quát định luật 2 Newton, liên hệ xung lượng – độ biến thiên động lượng, định luật bảo toàn năng lượng, cơ năng, động lượng, định luật Hooke, phương trình cơ bản của chất lưu đứng yên.
- 4 mục có `notes` (xem mục 6).

## 4. Yêu cầu cần đạt theo chương

Nguồn: `SGV VAT LI 10.pdf`, phần "I. Mục tiêu" đầu mỗi bài (số trang PDF trong ngoặc). Số tiết theo bảng cấu trúc SGK trong SGV (trang in 10, PDF 11). Đây là tổng số tiết của các bài, chưa tính ôn tập và kiểm tra. Trích rút gọn.

- **Chương I. Mở đầu** (4 tiết; SGV tr.13–23): Nêu đối tượng nghiên cứu của Vật lí. Phân tích ảnh hưởng của Vật lí đến công nghệ và cuộc sống. Nêu ví dụ về phương pháp thực nghiệm và phương pháp mô hình. Đọc kí hiệu, thông số trên thiết bị thí nghiệm; nêu quy tắc an toàn và nguy cơ mất an toàn. Nhận biết phép đo trực tiếp và gián tiếp; nêu các loại sai số và nguyên nhân; tính sai số tuyệt đối, sai số tỉ đối; ghi đúng kết quả đo.
- **Chương II. Động học** (16 tiết; SGV tr.23–50): Định nghĩa độ dịch chuyển, phân biệt với quãng đường; tổng hợp độ dịch chuyển hai chuyển động vuông góc. Tính tốc độ trung bình; tốc độ tức thời; định nghĩa vận tốc, phân biệt tốc độ – vận tốc; tổng hợp hai vận tốc cùng phương hoặc vuông góc. Mô tả và vẽ đồ thị d – t. Định nghĩa gia tốc; phân biệt nhanh dần – chậm dần theo vận tốc và gia tốc. Công thức và đồ thị v – t của chuyển động thẳng biến đổi đều. Sự rơi tự do và đặc điểm. Phân tích chuyển động ném thành hai chuyển động thành phần vuông góc. Thực hành đo tốc độ và đo gia tốc rơi tự do bằng đồng hồ hiện số và cổng quang điện.
- **Chương III. Động lực học** (18 tiết; SGV tr.51–88): Tổng hợp, phân tích lực; quy tắc hình bình hành; lực cân bằng và không cân bằng. Nhận biết lực **không** cần để duy trì chuyển động; định luật 1 Newton, quán tính. Định luật 2 Newton; khối lượng là số đo mức quán tính. Định luật 3 Newton: tác dụng luôn tương hỗ; chỉ ra cặp lực trực đối cân bằng và không cân bằng. Trọng lực, trọng lượng $P = mg$, trọng tâm, lực căng. Lực ma sát nghỉ, trượt, lăn; công thức $F_{ms} = \mu N$. Lực cản, lực nâng; phân biệt lực đẩy Archimedes với lực nâng lên vật chuyển động. Phương pháp động lực học. Moment lực, quy tắc moment, ngẫu lực, điều kiện cân bằng. Thực hành tổng hợp hai lực đồng quy và song song.
- **Chương IV. Năng lượng, công, công suất** (10 tiết; SGV tr.89–106): Các dạng năng lượng và sự chuyển hoá; định luật bảo toàn năng lượng. Định nghĩa, công thức, đơn vị công; công phát động, công cản. Công suất (tốc độ sinh công), liên hệ $\mathscr{P} = F.\upsilon$. Động năng, thế năng; liên hệ với công. Cơ năng, định luật bảo toàn cơ năng. Năng lượng có ích, hao phí; hiệu suất.
- **Chương V. Động lượng** (6 tiết; SGV tr.107–115): Định nghĩa và ý nghĩa của động lượng. Liên hệ lực với tốc độ biến thiên động lượng (dạng thứ hai của định luật 2 Newton). Định luật bảo toàn động lượng trong hệ kín. Năng lượng trong va chạm. Thực hành xác định động lượng trước và sau va chạm.
- **Chương VI. Chuyển động tròn** (4 tiết; SGV tr.116–123): Định nghĩa rađian, biểu diễn độ dịch chuyển góc theo rađian; tốc độ góc. Vận dụng biểu thức gia tốc hướng tâm $a_{ht} = \upsilon^2/r = \omega^2 r$ và lực hướng tâm. Giải pháp an toàn cho chuyển động tròn thực tế.
- **Chương VII. Biến dạng của vật rắn. Áp suất chất lỏng** (4 tiết; SGV tr.124–134): Biến dạng kéo, nén; giới hạn đàn hồi, độ dãn, độ cứng; định luật Hooke. Khối lượng riêng; áp lực, áp suất; $p = \rho g h$; phương trình cơ bản của thuỷ tĩnh học $\Delta p = \rho g \Delta h$.

**Chuyên đề** (nguồn: `SGV CD VAT LI 10.pdf`, bảng yêu cầu cần đạt PDF 8–9 và mục tiêu từng bài):
- **Chuyên đề 1. Vật lí trong một số ngành nghề** (SGV CD tr.12–25): Nêu sơ lược sự ra đời và thành tựu ban đầu của vật lí thực nghiệm, vai trò của cơ học Newton. Liệt kê các nhánh chính của vật lí cổ điển. Nêu sự khủng hoảng cuối thế kỉ XIX, tiền đề cho vật lí hiện đại. Liệt kê lĩnh vực chính của vật lí hiện đại, đối tượng nghiên cứu, mô hình lí thuyết và phương pháp thực nghiệm. Mô tả ví dụ ứng dụng vật lí trong quân sự, công nghiệp hạt nhân, khí tượng, nông nghiệp, lâm nghiệp, tài chính, điện tử, cơ khí – tự động hoá, thông tin – truyền thông.
- **Chuyên đề 2. Trái Đất và bầu trời** (SGV CD tr.26–43): Dùng bản đồ sao xác định chòm Gấu Lớn, Gấu Bé, Thiên Hậu và sao Bắc Cực. Dùng mô hình hệ Mặt Trời và hệ nhật tâm Copernic giải thích chuyển động nhìn thấy của Mặt Trời, Mặt Trăng, Kim tinh, Thuỷ tinh. Giải thích **sơ lược, định tính** nhật thực, nguyệt thực, thuỷ triều.
- **Chuyên đề 3. Vật lí với giáo dục bảo vệ môi trường** (SGV CD tr.44–65): Sự cần thiết bảo vệ môi trường và vai trò của cá nhân, cộng đồng. Tác động của việc sử dụng năng lượng đến môi trường, kinh tế, khí hậu Việt Nam. Chất ô nhiễm trong nhiên liệu hoá thạch, mưa acid, năng lượng hạt nhân, suy giảm tầng ozone, biến đổi khí hậu. Phân loại năng lượng hoá thạch – tái tạo; vai trò và công nghệ thu năng lượng tái tạo.

**Giới hạn và trọng tâm theo SGV.** Agent sinh câu hỏi lưu ý:
- Chương trình 2018 **không yêu cầu dùng hệ toạ độ, hệ quy chiếu, phương trình toạ độ – thời gian**. Chỉ dùng độ dịch chuyển và đồ thị "độ dịch chuyển – thời gian" (SGV tr.23). Không ra câu hỏi về phương trình $x = x_0 + vt$ hay "độ dời".
- **Không học định luật vạn vật hấp dẫn** ở lớp 10; công thức $F = G\frac{m_1 m_2}{r^2}$ chỉ có ở chuyên đề lớp 11 (SGV tr.71). Trọng lực được giới thiệu qua hiện tượng.
- Sai số phép đo gián tiếp: chỉ dùng quy tắc trong SGK (tổng/hiệu → cộng sai số tuyệt đối; tích/thương → cộng sai số tỉ đối). Không dùng phương pháp vi phân (SGV tr.21).
- Chuyển động ném được phân tích thành hai chuyển động thành phần vuông góc (chiếu vectơ độ dịch chuyển lên hai trục). SGV lưu ý không dùng "Nguyên lí độc lập của chuyển động" (SGV tr.47).
- Động năng, thế năng dạy ở mức đơn giản (xét trường hợp vật đứng yên được tăng tốc, nâng đều) (SGV tr.97).
- Chuyên đề 2: chỉ giải thích sơ lược, định tính (SGV CD tr.40).

## 5. Sai lầm thường gặp của học sinh

Nguồn: các đoạn "Lưu ý", "Quan niệm sai lầm dễ gặp", "HS thường mắc sai lầm", "HS dễ nhầm lẫn" trong SGV (cột Nguồn: trang PDF của `SGV VAT LI 10.pdf`, hoặc `SGV CD` cho `SGV CD VAT LI 10.pdf`).

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Gia tốc (Bài 8, 9) | HS thường cho rằng chuyển động nhanh dần thì $a > 0$, chậm dần thì $a < 0$, và viết $v = v_0 - at$, $s = v_0t - \frac{1}{2}at^2$ cho chuyển động chậm dần. Đúng: nhanh dần khi $a.v > 0$, chậm dần khi $a.v < 0$ (dấu của $a$ phụ thuộc chiều dương đã chọn). | SGV tr.37 |
| Lực và chuyển động (Bài 14) | Quan niệm vốn có (của Aristotle): muốn vật duy trì chuyển động thì phải có lực tác dụng. Đúng: nếu không có ma sát thì không cần lực để duy trì chuyển động. | SGV tr.54, 57 |
| Sự rơi (Bài 10; Chuyên đề Bài 1) | Vật nặng rơi nhanh hơn vật nhẹ. Đúng: sự rơi nhanh hay chậm do lực cản không khí; trong chân không mọi vật rơi nhanh như nhau. | SGV tr.42; SGV CD tr.13 |
| Định luật 3 Newton (Bài 16) | Nhầm lẫn giữa các lực khi giải thích hiện tượng. Ví dụ quyển sách nằm trên bàn: trọng lực $\vec{P}$ (lên sách) và áp lực $\vec{P'}$ (lên bàn) có cùng giá, cùng chiều, cùng độ lớn nên HS rất dễ nhầm. $\vec{P}$ và $\vec{N}$ là cặp lực cân bằng (cùng đặt vào sách); $\vec{P'}$ và $\vec{N}$ là lực – phản lực, **không** cân bằng vì đặt vào hai vật khác nhau. | SGV tr.66–67, 70 |
| Trọng lượng – khối lượng (Bài 17) | Viết "1,2 kg = 12 N" hoặc "đổi 1,2 kg ra 12 N". Trọng lượng và khối lượng là hai đại lượng có bản chất khác nhau, không thể "đổi" số đo của đại lượng này sang đại lượng kia. | SGV tr.72 |
| Lực nâng (Bài 19) | Cho rằng máy bay hoặc chim không rơi là do lực đẩy Archimedes. Lực đẩy Archimedes do chênh lệch áp suất thuỷ tĩnh, tồn tại cả khi vật đứng yên. Lực nâng cánh máy bay chỉ có khi máy bay chuyển động (do chênh lệch áp suất vì vận tốc dòng khí khác nhau ở mặt trên và mặt dưới cánh). | SGV tr.79 |
| Moment lực (Bài 21) | Cho rằng tay đòn là khoảng cách từ trục quay đến **điểm đặt** của lực. Đúng: tay đòn là khoảng cách từ trục quay đến **giá** của lực (đẩy cửa với giá lực đi qua bản lề thì cửa không quay). | SGV tr.84 |
| Công (Bài 23) | Ở THCS chỉ học $A = F.s$. Ở chương trình mới, với chuyển động thẳng thì độ dịch chuyển bằng quãng đường nên viết được $A = F.d$; đơn vị $1 J = 1 N.1 m$. | SGV tr.92 |
| Hiệu suất (Bài 27) | Không bao giờ đạt $H = 100\%$, vì luôn có năng lượng hao phí. | SGV tr.106 |
| Dạng tổng quát định luật 2 Newton (Bài 28) | $\vec{F} = \frac{\Delta\vec{p}}{\Delta t}$ thường được gọi là "dạng thứ hai" của định luật 2 Newton, nhưng thực ra Newton thiết lập định luật 2 bắt đầu từ biểu thức này. | SGV tr.107 |
| Cấu tạo vật chất (Chuyên đề Bài 1) | Quan niệm "nguyên tử là cái nhỏ nhất, không thể phân chia" bị đảo lộn khi phát hiện electron (1897). | SGV CD tr.17 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Năm sách nguồn là PDF dạng ảnh. Định nghĩa được đọc từ ảnh trang (khoảng 100–110 dpi). `check_sources.py` đối chiếu với text OCR (tesseract `vie`, cache ở `.ocr/`). Tài liệu bồi dưỡng GV có text layer nhưng lỗi font (mã hoá sai), nên được OCR ảnh riêng để đọc, không lưu cache.
- OCR không đọc được công thức. Phần LaTeX trong `definition` và toàn bộ `notation` **không được kiểm tra tự động**; phần này dựa vào kiểm tra mẫu.
- Tên các mục `tinh_chat`, `quy_tac`, `cong_thuc` thường do người trích đặt. Lần chạy gần nhất có 19 mục bị cảnh báo vì tên không có nguyên văn trong trang; nội dung các mục này vẫn đạt (bigram ≥ 0.75).
- Nguồn `gv` (12 mục) chỉ được kiểm tra sự có mặt của tên thuật ngữ; định nghĩa giữ theo SGK/SCD. Đã thêm alias `tay đòn`, `lực đẩy Archimede`, `dạng thứ hai của định luật 2 Newton` để khớp cách gọi của SGV.
- 4 mục có `notes`:
  - `mo-hinh-li-thuyet`: SGK chỉ minh hoạ bằng ví dụ (chất điểm, tia sáng), không định nghĩa tường minh.
  - `tong-hop-hai-luc-song-song-cung-chieu`: công thức chỉ xuất hiện trong bước tiến hành bài thực hành.
  - `thuy-trieu`: bảng thuật ngữ SCD phát biểu hơi khác thân bài.
  - `bui-min`: SCD chỉ liệt kê các loại bụi cực nhỏ (TSP, PM10, PM2,5). Tên hiển thị là "Bụi cực nhỏ"; id giữ slug `bui-min`.

**Kiểm tra tự động** (2026-10-15, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py vat_ly_10` | 0 lỗi; 241 thuật ngữ |
| `check_sources.py vat_ly_10` | 241 đạt, 0 gắn cờ, 0 không kiểm tra được, 19 cảnh báo về tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 10 mục: 2 do bảng ảnh (Bảng 2.1, Hình 2.8) được viết lại theo đúng thứ tự trong bảng; 1 do tên (`don-vi-newton` → "Đơn vị lực (N)"); 1 do thiếu alias (`luc-nang-cua-chat-luu`); 6 do nguồn đầu là trang bảng thuật ngữ trong khi định nghĩa lấy chủ yếu từ thân bài (đổi thứ tự nguồn). Không mục nào sai nội dung. |
| Kiểm tra trang chính xác (mọi nguồn so với hai trang kề) | Phát hiện **24 mục SCD Bài 1–2 và 1 mục SCD Bài 10 lệch +1 trang** (khi trích đã lấy số file OCR làm trang in). Thêm 1 nguồn bảng thuật ngữ SGK lệch 1 trang (`do-dich-chuyen-goc`) và 1 nguồn thừa (`hoang-dao` tr.51). Tất cả đã sửa bằng `--update`; chạy lại không còn mục lệch. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-15, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/241 (12%): 20 ngẫu nhiên + 10 mục `cong_thuc`/`dinh_ly`/có `notation` |
| Cách chọn | `query.py vat_ly_10 --audit` (seed 2026), danh sách ở `sample_audit.md` |
| Đối chiếu ảnh | 13 trang ảnh được mở lại (toàn bộ mục có công thức hoặc kí hiệu: SGK PDF 14, 18, 28, 29, 30, 43, 76, 77, 112, 113, 122, 124, 132). Các mục văn bản còn lại (SCD tr.26, 38, 39, 54, 61, 68, 70) đã đối chiếu ảnh khi trích, đạt bigram ≥ 0.86 ở đúng trang. |
| Số mục sai | 1 (3,3%, dưới ngưỡng 5%): `cong-thuc-cong-van-toc` có hai trường hợp riêng (cùng phương; vuông góc) lấy từ **lời giải bài tập ví dụ**, vi phạm quy tắc không trích lời giải. Công thức vẫn đúng. |
| Sửa thêm (không tính là sai) | `sai-so-he-thong`: kí hiệu $\Delta A_{dc}$ nằm ở trang kế tiếp; đã thêm nguồn PDF 19. |
| Số mục đã sửa | 2 |
| Kiểm tra độc lập | Đã hoàn thành (người dùng đã kiểm tra độc lập file mẫu 30 mục ở phiên riêng, đạt yêu cầu; đã xoá file mẫu). |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Vật lí 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Trọng lực, gia tốc rơi tự do (Bài 10, 17) → trường hấp dẫn, định luật vạn vật hấp dẫn (Chuyên đề lớp 11).
- Chuyển động tròn đều, tốc độ góc, chu kì, tần số (Bài 31) → dao động điều hoà (lớp 11).
- Năng lượng, bảo toàn năng lượng (Bài 23, 26) → nhiệt động lực học (lớp 12).
- Chuyên đề 1 (laser, vật lí hạt, năng lượng hạt nhân) → vật lí hạt nhân (lớp 12).
