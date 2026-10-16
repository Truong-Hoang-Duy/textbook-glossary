# Bộ thuật ngữ `toan_10` — Toán 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_10/toan_10/toan_10.json` (tập trung: `glossary/dataset/toan_10.json`), gồm **197 thuật ngữ** (cập nhật 2026-10-14). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_10/toan_10/`, bộ sách điện tử Kết nối tri thức (vniteach.com).

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Toan 10 Tap 1.pdf | sgk | 106 | Nguồn chính, Chương I–V, `level: co_ban` | Không (ảnh, OCR) |
| SGK Toan 10 Tap 2.pdf | sgk | 102 | Nguồn chính, Chương VI–IX, `level: co_ban` | Không (ảnh, OCR) |
| SCD Toan 10.pdf | scd | 66 | Chuyên đề 1–3, `level: chuyen_de` | Không (ảnh, OCR) |
| SBT TOAN 10 TAP 1.pdf | sbt | 130 | Chỉ bổ sung khái niệm SGK không nêu tường minh (Chương I–V) | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Toán 10.pdf | gv | 69 | Mục tiêu, yêu cầu cần đạt, điểm cần lưu ý (mục 4–5) | Có |
| SGV CD TOAN 10.pdf | gv | 90 | SGV Chuyên đề (`level: chuyen_de`): mục tiêu, điểm cần lưu ý từng bài Chuyên đề 1–3 (mục 4–5); nguồn `gv` phụ cho 10 thuật ngữ chuyên đề | Không (ảnh, OCR) |

- Ở cả năm sách dạng ảnh (gồm SGV CD): **trang PDF = trang in + 1**.
- Không có SGV cho phần cơ bản (SGK); phần cơ bản chỉ dựa vào Tài liệu bồi dưỡng GV.
- Không có SBT Tập 2, nên Chương VI–IX không có phần bổ sung từ SBT.
- Mục lục dùng chung số "Bài 1, 2, …" cho cả SGK và SCD. Khi lọc, kết hợp `--chapter` hoặc `--level`. Ví dụ: `--lesson "Bài 1." --level co_ban` là Bài 1 SGK; `--lesson "Bài 1." --level chuyen_de` là Bài 1 Chuyên đề.

## 2. Chương/bài và số thuật ngữ

Cột "Tổng" đã gồm các mục bổ sung từ SBT, đếm riêng ở cột cuối.

| Chương / Chuyên đề | Bài | Tổng | Từ SBT |
|---|---|---|---|
| Chương I. Mệnh đề và tập hợp | Bài 1. Mệnh đề | 13 | 2 |
| | Bài 2. Tập hợp và các phép toán trên tập hợp | 23 | |
| Chương II. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn | Bài 3. Bất phương trình bậc nhất hai ẩn | 5 | |
| | Bài 4. Hệ bất phương trình bậc nhất hai ẩn | 6 | 1 |
| Chương III. Hệ thức lượng trong tam giác | Bài 5. Giá trị lượng giác của một góc từ 0° đến 180° | 10 | 3 |
| | Bài 6. Hệ thức lượng trong tam giác | 11 | 2 |
| Chương IV. Vectơ | Bài 7. Các khái niệm mở đầu | 10 | 1 |
| | Bài 8. Tổng và hiệu của hai vectơ | 7 | |
| | Bài 9. Tích của một vectơ với một số | 8 | 2 |
| | Bài 10. Vectơ trong mặt phẳng toạ độ | 8 | |
| | Bài 11. Tích vô hướng của hai vectơ | 6 | |
| Chương V. Các số đặc trưng của mẫu số liệu không ghép nhóm | Bài 12. Số gần đúng và sai số | 6 | |
| | Bài 13. Các số đặc trưng đo xu thế trung tâm | 5 | 1 |
| | Bài 14. Các số đặc trưng đo độ phân tán | 6 | 1 |
| Chương VI. Hàm số, đồ thị và ứng dụng | Bài 15. Hàm số | 5 | |
| | Bài 16. Hàm số bậc hai | 4 | |
| | Bài 17. Dấu của tam thức bậc hai | 3 | |
| | Bài 18. Phương trình quy về phương trình bậc hai | 2 | |
| Chương VII. Phương pháp toạ độ trong mặt phẳng | Bài 19. Phương trình đường thẳng | 4 | |
| | Bài 20. Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách | 5 | |
| | Bài 21. Đường tròn trong mặt phẳng toạ độ | 3 | |
| | Bài 22. Ba đường conic | 8 | |
| Chương VIII. Đại số tổ hợp | Bài 23. Quy tắc đếm | 3 | |
| | Bài 24. Hoán vị, chỉnh hợp và tổ hợp | 4 | |
| | Bài 25. Nhị thức Newton | 1 | |
| Chương IX. Tính xác suất theo định nghĩa cổ điển | Bài 26. Biến cố và định nghĩa cổ điển của xác suất | 7 | |
| | Bài 27. Thực hành tính xác suất theo định nghĩa cổ điển | 1 | |
| Chuyên đề 1. Hệ phương trình bậc nhất ba ẩn | Bài 1. Hệ phương trình bậc nhất ba ẩn | 5 | |
| | Bài 2. Ứng dụng của hệ phương trình bậc nhất ba ẩn | 2 | |
| Chuyên đề 2. Phương pháp quy nạp toán học. Nhị thức Newton | Bài 3. Phương pháp quy nạp toán học | 1 | |
| | Bài 4. Nhị thức Newton | 5 | |
| Chuyên đề 3. Ba đường conic và ứng dụng | Bài 5. Elip | 3 | |
| | Bài 6. Hypebol | 3 | |
| | Bài 7. Parabol | 2 | |
| | Bài 8. Sự thống nhất giữa ba đường conic | 2 | |

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 117 |
| tinh_chat | 26 |
| cong_thuc | 23 |
| quy_tac | 18 |
| ky_hieu | 10 |
| dinh_ly | 3 |

- Theo `level`: `co_ban` 174, `chuyen_de` 23.
- Theo nguồn định nghĩa: SGK 161, SCD 23, SBT 13.
- 119 mục có `notation`; 2 mục có `notes`.
- SGK Toán 10 ít khi gọi tên "định lí". Chỉ định lí côsin, định lí sin và định lí về dấu của tam thức bậc hai được gắn `dinh_ly`. Các kết quả khác sách nêu dưới dạng khung kiến thức, nên được ghi là `tinh_chat` hoặc `cong_thuc`.

## 4. Yêu cầu cần đạt theo chương

Nguồn: Tài liệu bồi dưỡng GV, mục 1.3, trang PDF 5–10. Trích rút gọn.

- **Chương I. Mệnh đề và tập hợp:** Thiết lập và phát biểu các mệnh đề toán học: mệnh đề phủ định, mệnh đề đảo, mệnh đề tương đương, mệnh đề chứa ∀, ∃, điều kiện cần, điều kiện đủ, điều kiện cần và đủ. Xác định tính đúng/sai của mệnh đề trong trường hợp đơn giản. Nhận biết tập con, hai tập hợp bằng nhau, tập rỗng; sử dụng các kí hiệu ⊂, ∈, ∅. Thực hiện các phép hợp, giao, hiệu, phần bù và biểu diễn bằng biểu đồ Ven. Giải bài toán thực tiễn đếm số phần tử của hợp các tập hợp.
- **Chương II. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn:** Nhận biết bất phương trình và hệ bất phương trình bậc nhất hai ẩn. Biểu diễn miền nghiệm trên mặt phẳng toạ độ. Vận dụng vào bài toán thực tiễn, ví dụ tìm cực trị của F = ax + by trên một miền đa giác.
- **Chương III. Hệ thức lượng trong tam giác:** Nhận biết giá trị lượng giác của góc từ 0° đến 180° và tính bằng máy tính cầm tay. Giải thích hệ thức giữa giá trị lượng giác của các góc phụ nhau, bù nhau. Giải thích định lí côsin, định lí sin và các công thức diện tích tam giác. Mô tả cách giải tam giác và vận dụng vào thực tiễn.
- **Chương IV. Vectơ:** Nhận biết vectơ, vectơ bằng nhau, vectơ-không. Thực hiện tổng, hiệu, tích với một số và tích vô hướng. Mô tả ba điểm thẳng hàng, trung điểm, trọng tâm bằng vectơ. Biểu thị đại lượng vật lí bằng vectơ. Nhận biết toạ độ của vectơ, tính độ dài, dùng biểu thức toạ độ của các phép toán.
- **Chương V. Các số đặc trưng của mẫu số liệu không ghép nhóm:** Hiểu số gần đúng, sai số tuyệt đối, sai số tương đối, số quy tròn với độ chính xác cho trước. Tính các số đặc trưng đo xu thế trung tâm (số trung bình, trung vị, tứ phân vị, mốt) và đo độ phân tán (khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn). Giải thích ý nghĩa các số đặc trưng. Phát hiện số liệu không chính xác.
- **Chương VI. Hàm số, đồ thị và ứng dụng:** Mô tả hàm số, tập xác định, tập giá trị, đồng biến, nghịch biến, đồ thị. Vẽ parabol, nhận biết đỉnh và trục đối xứng, nhận biết tính chất hàm số bậc hai qua đồ thị. Giải thích định lí về dấu của tam thức bậc hai từ đồ thị. Giải bất phương trình bậc hai và hai dạng phương trình chứa căn thức quy về phương trình bậc hai.
- **Chương VII. Phương pháp toạ độ trong mặt phẳng:** Mô tả phương trình tổng quát và phương trình tham số của đường thẳng; lập phương trình khi biết điểm và vectơ pháp tuyến/chỉ phương, hoặc biết hai điểm. Nhận biết vị trí tương đối, tính góc giữa hai đường thẳng, khoảng cách từ điểm đến đường thẳng. Lập phương trình đường tròn và tiếp tuyến tại một điểm. Nhận biết ba đường conic bằng hình học và qua phương trình chính tắc.
- **Chương VIII. Đại số tổ hợp:** Vận dụng quy tắc cộng, quy tắc nhân và sơ đồ hình cây. Tính số hoán vị, chỉnh hợp, tổ hợp, kể cả bằng máy tính cầm tay. Khai triển (a + b)ⁿ với n = 4 hoặc 5 bằng cách vận dụng tổ hợp.
- **Chương IX. Tính xác suất theo định nghĩa cổ điển:** Nhận biết phép thử ngẫu nhiên, không gian mẫu, biến cố (là tập con của không gian mẫu), biến cố đối, định nghĩa cổ điển của xác suất, nguyên lí xác suất bé. Tính xác suất bằng phương pháp tổ hợp và sơ đồ hình cây. Tính xác suất của biến cố đối.
**Chuyên đề — mục tiêu từng bài** (nguồn: `SGV CD TOAN 10.pdf`, phần "I. Mục tiêu — Về kiến thức, kĩ năng"; trang PDF ghi trong ngoặc):

- **Chuyên đề 1. Hệ phương trình bậc nhất ba ẩn** (11 tiết):
  - Bài 1 (5 tiết, tr.18): nhận biết hệ phương trình bậc nhất ba ẩn và nghiệm của nó; giải bằng phương pháp Gauss; tìm nghiệm bằng máy tính cầm tay.
  - Bài 2 (4 tiết, tr.26): vận dụng hệ bậc nhất ba ẩn vào bài toán vật lí (điện trở, cường độ dòng điện), hoá học (cân bằng phản ứng), sinh học, và bài toán thực tiễn (cân bằng cung – cầu).
- **Chuyên đề 2. Phương pháp quy nạp toán học. Nhị thức Newton** (10 tiết):
  - Bài 3 (4 tiết, tr.36): mô tả các bước và chứng minh tính đúng đắn của mệnh đề bằng phương pháp quy nạp; vận dụng vào vấn đề thực tiễn.
  - Bài 4 (5 tiết, tr.44): xác định hệ số khai triển qua tam giác Pascal; khai triển (a + b)ⁿ bằng tam giác Pascal hoặc công thức số tổ hợp; xác định hệ số của xᵏ trong khai triển (ax + b)ⁿ.
- **Chuyên đề 3. Ba đường conic và ứng dụng** (11 tiết):
  - Bài 5 Elip (3 tiết, tr.57), Bài 6 Hypebol (3 tiết, tr.66), Bài 7 Parabol (2 tiết, tr.75): xác định các yếu tố đặc trưng khi biết phương trình chính tắc; giải quyết vấn đề thực tiễn gắn với đường đó.
  - Bài 8 Sự thống nhất giữa ba đường conic (2 tiết, tr.81): nhận biết đường conic là giao của mặt phẳng với mặt nón; vấn đề thực tiễn gắn với ba đường conic.

**Giới hạn chương trình lớp 10.** Nguồn: Tài liệu GV, trang PDF 11–13 và 37. Agent sinh câu hỏi **không ra câu hỏi** về các nội dung sau:
- Hàm số chẵn, hàm số lẻ, hàm số tuần hoàn: chưa đưa vào chương trình.
- Xét đồng biến, nghịch biến bằng định nghĩa và lập bảng biến thiên: không yêu cầu. Học sinh chỉ cần suy ra khoảng đồng biến, nghịch biến từ đồ thị.
- Chứng minh đại số định lí về dấu của tam thức bậc hai: không yêu cầu. Định lí được nhận biết qua đồ thị.
- Bất đẳng thức, bất phương trình và hệ bất phương trình bậc nhất một ẩn, các phép biến đổi tương đương hoặc hệ quả: không yêu cầu.
- Lượng giác (góc, cung lượng giác, công thức lượng giác): chuyển hết lên lớp 11. Lớp 10 chỉ có giá trị lượng giác của góc từ 0° đến 180°.
- Nhị thức Newton tổng quát, tam giác Pascal, quy nạp toán học: chỉ có trong Chuyên đề. SGK chỉ có trường hợp n = 4 và n = 5.
- Chứng minh công thức nhị thức Newton tổng quát bằng quy nạp: SGV CD chỉ áp dụng cho lớp khá, chưa yêu cầu đại trà (SGV CD tr.47).
- "Các elip (hypebol) có cùng tâm sai đều đồng dạng", "các parabol đồng dạng với nhau": SGV CD ghi GV không cần giải thích cho HS (tr.57, 66, 76) — không ra đề.

## 5. Sai lầm thường gặp của học sinh

Tài liệu GV và SGV CD không có mục riêng về lỗi sai. Dưới đây là các sai lầm, điểm dễ nhầm được nêu rõ trong hai tài liệu (cột Nguồn: TLBD = Tài liệu bồi dưỡng GV; SGV CD = `SGV CD TOAN 10.pdf`; số là trang PDF):

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Quy tắc cộng (Bài 23) và số phần tử của hợp hai tập hợp (Bài 2) | Áp dụng quy tắc cộng khi hai phương án **không độc lập** (có phần tử chung), ví dụ cộng 160 + 140 học sinh của hai câu lạc bộ mà không trừ 50 học sinh tham gia cả hai. Phải dùng $n(A \cup B) = n(A) + n(B) - n(A \cap B)$. | TLBD tr.51 (Ví dụ 3) |
| Hàm số cho bởi nhiều công thức (Bài 15) | Tính tiền điện 75 kWh theo một công thức duy nhất $y = 1{,}734x$, thay vì dùng đúng công thức của từng khoảng bậc thang. | TLBD tr.67 (bài soạn minh hoạ) |
| Đọc dấu hệ số parabol từ đồ thị (Bài 16) | Học sinh cần dựa vào hướng bề lõm (dấu của a), toạ độ đỉnh và giao điểm với trục tung (c) để xác định dấu của a, b, c. Đây là dạng câu hỏi dễ chọn sai. | TLBD tr.51 (Ví dụ 2) |
| Hệ bậc nhất ba ẩn (CĐ1 Bài 1) | Nhầm "bậc nhất ba ẩn": mỗi phương trình phải có bậc 1 và số ẩn phải là 3. | SGV CD tr.19 |
| Giải hệ bằng máy tính cầm tay (CĐ1 Bài 1) | Sai sót khi bấm máy; với hệ có **vô số nghiệm** máy tính không cho tập nghiệm, phải giải bằng tay (phương pháp Gauss). | SGV CD tr.23 |
| Cân bằng phản ứng hoá học (CĐ1 Bài 2) | Hệ thu được luôn có vô số nghiệm và thường có nhiều ẩn hơn số phương trình; cần chọn một nghiệm nguyên phù hợp. | SGV CD tr.28 |
| Quy nạp không hoàn toàn (CĐ2 Bài 3) | Kết luận từ vài trường hợp riêng: $p(n) = n^2 + n + 41$ nguyên tố với n = 1, 2, 3, 5… nhưng sai khi n = 41. Kiểm nghiệm nhiều trường hợp không thay cho chứng minh. | SGV CD tr.37 |
| Các bước quy nạp (CĐ2 Bài 3) | Chỉ kết luận mệnh đề đúng khi **cả hai bước** đều đúng; quên dùng giả thiết quy nạp ở Bước 2; với mệnh đề đúng từ $n \ge p$, Bước 1 phải kiểm tra $n = p$ (không phải n = 1). | SGV CD tr.36–38 |
| Lập luận quy nạp sai (CĐ2, Bài tập 2.8) | Lập luận sai ở bước khởi đầu: mệnh đề không thể bắt đầu với n = 1 khi nội dung cần ít nhất hai đối tượng. | SGV CD tr.43 |
| Bán kính qua tiêu của hypebol (CĐ3 Bài 6) | Công thức giống elip nhưng có **dấu giá trị tuyệt đối**; phải chia trường hợp điểm thuộc nhánh trái/phải khi phá trị tuyệt đối. | SGV CD tr.69 |
| Hình dạng hypebol, parabol (CĐ3 Bài 6–7) | Hypebol có hai nhánh và hai đường tiệm cận (elip không có); parabol chỉ có một nhánh, không bị giới hạn, không có tiệm cận. | SGV CD tr.67, 76 |
| Bài toán thực tế quỹ đạo (CĐ3 Bài 6) | Quên đổi đơn vị đo theo yêu cầu bài toán khi viết phương trình chính tắc. | SGV CD tr.71 |
| Phân loại conic theo tâm sai (CĐ3 Bài 8) | Phân biệt theo so sánh e với 1: elip $0 < e < 1$, parabol $e = 1$, hypebol $e > 1$. | SGV CD tr.82 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Bốn sách nguồn là PDF dạng ảnh. Định nghĩa được đọc trực tiếp từ ảnh trang (khoảng 135 dpi). `check_sources.py` đối chiếu với text OCR (tesseract `vie`), lưu cache ở `.ocr/`. OCR hay sai dấu ("bắt" thay cho "bất", "ân" thay cho "ẩn") và dính chữ ("Tậphợp"); script đã có cơ chế chịu các lỗi này.
- OCR không đọc được công thức, nên phần LaTeX trong `definition` và toàn bộ `notation` **không được kiểm tra tự động**. Phần này dựa vào kiểm tra mẫu.
- Tên của các mục `cong_thuc`, `quy_tac`, `ky_hieu`, `tinh_chat` thường do người trích đặt, vì sách không đặt tên. Lần chạy gần nhất có 37 mục bị cảnh báo vì tên không có nguyên văn trong trang; nội dung các mục này vẫn đạt.
- `toan-10-nhi-thuc-newton` (SGK Bài 25) chỉ gồm công thức nên không có tỉ lệ bigram. Script chỉ kiểm được tên thuật ngữ.
- SGV CD là PDF dạng ảnh; nguồn `gv` (10 mục) là nguồn phụ, chỉ được kiểm tra sự có mặt của tên thuật ngữ, không kiểm tra tỉ lệ bigram (định nghĩa giữ theo SCD).
- Có 2 mục mang `notes`: `toan-10-he-thuc-co-ban-luong-giac` và `toan-10-trung-diem-trong-tam-voi-moi-diem-o`. Cả hai là nội dung SGK chỉ nêu ở bài tập hoặc luyện tập; phát biểu tổng quát lấy từ SBT.

**Kiểm tra tự động** (2026-10-14, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py toan_10` | 0 lỗi; 197 thuật ngữ; 174.7 KB |
| `check_sources.py toan_10` | 197 đạt, 0 gắn cờ, 0 không kiểm tra được, 37 cảnh báo về tên (chạy lại sau khi thêm SGV CD) |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 14 (13 khi trích + 1 khi thêm nguồn SGV CD), đều do tên thuật ngữ do người trích đặt hoặc OCR dính chữ. Đã thêm alias hoặc đổi loại (`--update`). Không mục nào sai nội dung hay sai trang. |
| Mô phỏng độ nhạy trên toàn bộ dữ liệu | Dữ liệu đúng: 0/192 bị gắn cờ. Nguồn lệch 5–9 trang: bắt được 484/512 (95%). Gán định nghĩa của mục khác: bắt được 186/190 (98%). |

**Kiểm tra mẫu độc lập** (Giai đoạn 4, 2026-10-14, người dùng thực hiện ở phiên riêng, đọc ảnh trang nguồn):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/197 (15%): 20 ngẫu nhiên + 10 mục `cong_thuc`/`dinh_ly`/có `notation` |
| Cách chọn | `query.py toan_10 --audit` (seed 2026), danh sách ở `sample_audit.md` |
| Số mục sai | 0 (tỉ lệ sai 0%, dưới ngưỡng 5%) |
| Số mục đã sửa | 0 |


## 7. Liên hệ với các lớp khác

Phần này điền khi làm Toán 11 và Toán 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Giá trị lượng giác (Bài 5) → lượng giác của góc lượng giác (lớp 11).
- Hàm số, đồng biến/nghịch biến (Bài 15) → đạo hàm và khảo sát hàm số (lớp 11, 12).
- Xác suất cổ điển (Bài 26) → các quy tắc tính xác suất (lớp 11, 12).
- Vectơ trong mặt phẳng (Chương IV) → vectơ và toạ độ trong không gian (lớp 12).
- Số đặc trưng của mẫu số liệu không ghép nhóm (Chương V) → mẫu số liệu ghép nhóm (lớp 11, 12).
