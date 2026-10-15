# Bộ thuật ngữ `tin_hoc_10` — Tin học 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/tin_hoc_10/tin_hoc_10.json`, gồm **266 thuật ngữ** (cập nhật 2026-10-15). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `tin_hoc_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Tin hoc 10.pdf | sgk | 170 | Nguồn chính, Chủ đề 1–6 (34 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD Tin hoc 10 - Khoa hoc may tinh.pdf | scd | 74 | Chuyên đề định hướng Khoa học máy tính (CS): robot giáo dục, 3 chuyên đề, 14 bài, `level: chuyen_de` | Không (ảnh, OCR) |
| SCD Tin hoc 10 - Tin hoc ung dung.pdf | scd | 82 | Chuyên đề định hướng Tin học ứng dụng (ICT): văn bản, bảng tính, trình chiếu, 3 chuyên đề, 15 bài, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV TIN HOC 10.pdf | gv | 150 | Mục tiêu từng bài, phân phối tiết, lưu ý giảng dạy (mục 4–5); nguồn `gv` cho 21 thuật ngữ | Không (ảnh, OCR) |
| SGV CD TIN HOC - Khoa hoc may tinh.pdf | gv | 74 | Yêu cầu cần đạt, lưu ý giảng dạy chuyên đề CS (mục 4–5); nguồn `gv` cho 5 thuật ngữ | Không (ảnh, OCR) |
| SGV CD TIN HOC - Tin hoc ung ung.pdf | gv | 78 | Mục tiêu, danh sách bài chuyên đề ICT (mục 4); nguồn `gv` cho 1 thuật ngữ. Tên file gõ nhầm "ung ung" — giữ nguyên vì thư mục nguồn chỉ đọc | Không (ảnh, OCR) |
| SBT TIN HOC 10.pdf | sbt | 150 | Câu hỏi, bài tập (PDF 5–70) kèm "Tóm tắt kiến thức" đầu mỗi bài; đáp án (PDF 71–148). Bổ sung 5 mục SGK chưa phát biểu tường minh, thêm nguồn `sbt` cho 3 mục | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Tin học 10.pdf | gv | 85 | Khái quát CT 2018, thời lượng, ma trận nội dung – năng lực (mục 4) | Có (đọc trực tiếp) |

- Ở bảy sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- Chủ đề dùng nguyên tên trong SGK (`chapter` = `Chủ đề N. …`); hai SCD dùng `Chuyên đề N. …`.
- **Hai SCD đều đánh số "Chuyên đề 1, 2, 3"**, nhưng tên chuyên đề khác nhau nên chuỗi `chapter` vẫn duy nhất. SCD Khoa học máy tính đánh số bài liên tục (Bài 1–14). SCD Tin học ứng dụng **đánh lại "Bài 1" ở mỗi chuyên đề**. Khi lọc, luôn kèm tên chuyên đề, ví dụ `--chapter "bảng tính" --lesson "Bài 1."`.
- SGK và SCD đều có "Bảng giải thích thuật ngữ": SGK PDF 167–168 (29 mục), SCD KHMT PDF 72 (7 mục), SCD ICT PDF 80 (10 mục). Cả 46 mục đều có trong glossary và mang nguồn trang bảng. Có 7 mục lấy định nghĩa từ bảng thuật ngữ vì thân bài không phát biểu tường minh, nên nguồn bảng đứng đầu `sources`: `ham`, `bug-va-debug`, `stem`, `chip-vi-dieu-khien`, `cam-bien-sieu-am`, `ma-gia`, `ham-tim-kiem-du-lieu`. OCR mặc định của bốn trang bảng (SGK 102, 167, 168; SCD KHMT 72; SCD ICT 80) dính chữ, nên cache `.ocr/` được nối thêm bản OCR 400 dpi (psm 4).
- `stem` nêu ở Lời nói đầu SCD KHMT (PDF 4), không thuộc bài nào; được gán vào Chuyên đề 1, Bài 1.
- Bài 0 mục: SGK Bài 15 (thực hành hoàn thiện đồ hoạ) và Bài 32 (ôn tập); SCD KHMT Bài 4, 7, 8, 12, 14 (thực hành); SCD ICT Chuyên đề 2 Bài 5, 7 (thực hành). Các bài thực hành còn lại chỉ lấy khái niệm được nêu tường minh trong khung kiến thức (ví dụ Bài 7 `tro-thu-so-ca-nhan`, Bài 10 `ngon-ngu-nguon-va-ngon-ngu-dich`, Bài 31 `cau-truc-if-elif-else`). Không lấy các bước thao tác phần mềm trong phần "Thực hành".
- Theo SGV (PDF 13): HS định hướng **ICT không học Bài 3–6**, HS định hướng **CS không học Bài 12–15**. Agent ra đề cần lọc theo định hướng.

## 2. Chương/bài và số thuật ngữ

Số mục tính theo `chapter` + `lesson` (kể cả mục bổ sung từ SBT). Bài không liệt kê có 0 mục.

| Chủ đề / Chuyên đề | Bài | Số mục |
|---|---|---|
| Chủ đề 1. Máy tính và xã hội tri thức | Bài 1. Thông tin và xử lí thông tin | 10 |
|  | Bài 2. Vai trò của thiết bị thông minh và tin học đối với xã hội | 7 |
|  | Bài 3. Một số kiểu dữ liệu và dữ liệu văn bản | 6 |
|  | Bài 4. Hệ nhị phân và dữ liệu số nguyên | 8 |
|  | Bài 5. Dữ liệu lôgic | 11 |
|  | Bài 6. Dữ liệu âm thanh và hình ảnh | 14 |
|  | Bài 7. Thực hành sử dụng thiết bị số thông dụng | 2 |
| Chủ đề 2. Mạng máy tính và Internet | Bài 8. Mạng máy tính trong cuộc sống hiện đại | 14 |
|  | Bài 9. An toàn trên không gian mạng | 16 |
|  | Bài 10. Thực hành khai thác tài nguyên trên Internet | 1 |
| Chủ đề 3. Đạo đức, pháp luật và văn hoá trong môi trường số | Bài 11. Ứng xử trên môi trường số. Nghĩa vụ tôn trọng bản quyền | 14 |
| Chủ đề 4. Ứng dụng tin học | Bài 12. Phần mềm thiết kế đồ hoạ | 10 |
|  | Bài 13. Bổ sung các đối tượng đồ hoạ | 3 |
|  | Bài 14. Làm việc với đối tượng đường và văn bản | 8 |
| Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính | Bài 16. Ngôn ngữ lập trình bậc cao và Python | 7 |
|  | Bài 17. Biến và lệnh gán | 8 |
|  | Bài 18. Các lệnh vào ra đơn giản | 4 |
|  | Bài 19. Câu lệnh rẽ nhánh if | 6 |
|  | Bài 20. Câu lệnh lặp for | 3 |
|  | Bài 21. Câu lệnh lặp while | 3 |
|  | Bài 22. Kiểu dữ liệu danh sách | 5 |
|  | Bài 23. Một số lệnh làm việc với dữ liệu danh sách | 4 |
|  | Bài 24. Xâu kí tự | 3 |
|  | Bài 25. Một số lệnh làm việc với xâu kí tự | 4 |
|  | Bài 26. Hàm trong Python | 4 |
|  | Bài 27. Tham số của hàm | 4 |
|  | Bài 28. Phạm vi của biến | 3 |
|  | Bài 29. Nhận biết lỗi chương trình | 6 |
|  | Bài 30. Kiểm thử và gỡ lỗi chương trình | 5 |
|  | Bài 31. Thực hành viết chương trình đơn giản | 1 |
| Chủ đề 6. Hướng nghiệp với tin học | Bài 33. Nghề thiết kế đồ hoạ máy tính | 3 |
|  | Bài 34. Nghề phát triển phần mềm | 4 |
| Chuyên đề 1. Thực hành với các bộ phận của robot giáo dục (CS) | Bài 1. Cấu tạo chung của robot giáo dục | 6 |
|  | Bài 2. Bảng mạch điều khiển và cơ cấu chấp hành | 7 |
|  | Bài 3. Cảm biến và phụ kiện dùng trong robot | 9 |
| Chuyên đề 2. Kết nối robot với máy tính (CS) | Bài 5. Phần mềm lập trình điều khiển robot | 4 |
|  | Bài 6. Chương trình điều khiển robot | 3 |
| Chuyên đề 3. Lập trình điều khiển robot (CS) | Bài 9. Điều khiển robot chuyển động | 5 |
|  | Bài 10. Điều khiển robot nhận biết vật cản | 1 |
|  | Bài 11. Dẫn đường tự động cho robot | 3 |
|  | Bài 13. Lập trình điều khiển một số phụ kiện | 3 |
| Chuyên đề 1. Thực hành làm việc với các tệp văn bản (ICT) | Bài 1. Lập dàn ý và định dạng với các công cụ nâng cao | 3 |
|  | Bài 2. Trình bày văn bản với định dạng ảnh nâng cao | 2 |
|  | Bài 3. Trình bày văn bản với hình khối và hộp văn bản | 2 |
|  | Bài 4. Tạo mục lục và xuất bản văn bản | 3 |
| Chuyên đề 2. Thực hành sử dụng phần mềm bảng tính (ICT) | Bài 1. Tạo dữ liệu ban đầu với công cụ định dạng bảng | 2 |
|  | Bài 2. Tạo biểu mẫu khách hàng với hộp kiểm | 1 |
|  | Bài 3. Xây dựng dự toán với hàm điều kiện | 1 |
|  | Bài 4. Hoàn thiện dự toán với hàm tìm kiếm | 2 |
|  | Bài 6. Tạo và xuất báo giá với hàm thời gian | 1 |
| Chuyên đề 3. Thực hành sử dụng phần mềm trình chiếu (ICT) | Bài 1. Xây dựng ý tưởng, cấu trúc bài trình chiếu | 1 |
|  | Bài 2. Tạo ấn tượng với minh hoạ bằng video | 2 |
|  | Bài 3. Thu hút khách hàng với trò chơi tương tác | 2 |
|  | Bài 4. Hoàn thiện và xuất bản sản phẩm truyền thông | 2 |

Gộp mục: khái niệm xuất hiện ở nhiều bài thì giữ một mục ở bài có phát biểu tường minh nhất và thêm nguồn các trang khác. Ví dụ `internet-van-vat` nêu sơ lược ở Bài 2 (PDF 13–14) nhưng định nghĩa đầy đủ ở Bài 8 (PDF 43–44), nên mục thuộc Bài 8. `thiet-ke-do-hoa` (Bài 12) mang thêm nguồn Bài 33 (PDF 157). Các khái niệm gần nhau nhưng khác ngữ cảnh được tách riêng: `bieu-thuc-logic` (lôgic mệnh đề, Bài 5) và `bieu-thuc-logic-trong-python` (Bài 19); `hinh-khoi-va-doi-tuong-duong` (Inkscape) và `hinh-khoi-van-ban` (Word, SCD ICT); `do-sau-mau` (ảnh) và `do-sau-bit-am-thanh` (âm thanh, SBT).

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 140 |
| quy_tac | 73 |
| tinh_chat | 43 |
| ky_hieu | 6 |
| cong_thuc | 4 |

- Theo `level`: `co_ban` 201, `chuyen_de` 65 (SCD KHMT 41, SCD ICT 24).
- Theo nguồn định nghĩa (nguồn đầu tiên): SGK 196, SCD KHMT 41, SCD ICT 24, SBT 5 (`mang-may-tinh`, `ngon-ngu-lap-trinh`, `dien-thoai-thong-minh`, `do-hoa-may-tinh`, `do-sau-bit-am-thanh`). 27 mục mang thêm nguồn `gv` (21 từ SGV, 5 từ SGV CD KHMT, 1 từ SGV CD ICT); định nghĩa vẫn giữ theo SGK/SCD. 3 mục SGK mang thêm nguồn `sbt` (`quyen-tai-san`, `quyen-nhan-than`, `tac-pham-phai-sinh`).
- `quy_tac` nhiều vì môn có nhiều cú pháp lệnh Python, lệnh robot, thao tác công cụ được SGK chốt trong khung kiến thức. Cú pháp lệnh được ghi ở `notation` bằng `$\texttt{…}$`, ví dụ `print(v1, v2, ..., vn)`, `<biến> = <biểu thức>`, `range(start, stop)`, `VLOOKUP(lookup_value; table_array; col_index_num; [range_lookup])`.
- 61 mục có `notation`. `cong_thuc` (4): đổi nhị phân → thập phân, hàm `IF`, hàm `VLOOKUP`, hàm `NOW`/`TODAY`. `ky_hieu` (6): đơn vị lưu trữ dữ liệu (Bảng 1.1, $2^{10}$), kí hiệu `#` chú thích, phép so sánh trong Python, mã lỗi ngoại lệ, lệnh mã giả cơ bản (Bảng 6.1 SCD), lệnh tích hợp điều khiển chuyển động (Bảng 9.2 SCD).
- 0 mục có `notes`.

## 4. Yêu cầu cần đạt theo chủ đề

Nguồn: `SGV TIN HOC 10.pdf`, mục "Mục tiêu môn Tin học lớp 10" (PDF 8–10) và bảng danh sách bài (PDF 12–14); `Tài liệu bồi dưỡng GV môn Tin học 10.pdf` (PDF 8, 11–26: ma trận nội dung – năng lực). Trích rút gọn.

- **Thời lượng** (Tài liệu bồi dưỡng GV PDF 8; SGV PDF 12): SGK 70 tiết, trong đó 4 tiết kiểm tra, đánh giá; mỗi chuyên đề 35 tiết, trong đó 3 tiết kiểm tra. Phần lớn bài 2 tiết; Bài 11 dạy 4 tiết; Bài 23, 25, 27, 28 dạy 3 tiết. Mỗi định hướng ICT/CS dạy riêng 8 tiết: **ICT bỏ Bài 3–6, CS bỏ Bài 12–15**. Chủ đề 6 cần học sau Chủ đề 4 và 5. Chuyên đề chỉ đòi hỏi kiến thức giai đoạn cơ bản, có thể dạy độc lập, không bắt buộc sau SGK (Tài liệu bồi dưỡng GV PDF 7–8).
- **Chủ đề 1. Máy tính và xã hội tri thức** (SGV PDF 8): Phân biệt thông tin và dữ liệu; chuyển đổi đơn vị lưu trữ (B, KB, MB, …); nêu sự ưu việt của lưu trữ, xử lí, truyền thông tin bằng thiết bị số; nêu ví dụ thiết bị thông minh và vai trò trong CMCN 4.0; nhận biết thiết bị số thông dụng cũng là hệ thống xử lí thông tin; giới thiệu thành tựu nổi bật của tin học; thực hiện phép toán AND, OR, XOR, NOT; giải thích ứng dụng của hệ nhị phân, sơ lược việc số hoá văn bản, hình ảnh, âm thanh; chức năng của bảng mã quốc tế (Unicode). Bài 4 chỉ yêu cầu cộng và nhân nhị phân, biểu diễn số nguyên (Tài liệu bồi dưỡng GV PDF 12).
- **Chủ đề 2. Mạng máy tính và Internet** (SGV PDF 9): So sánh mạng LAN và Internet; nêu dịch vụ điện toán đám mây; nêu khái niệm IoT và ví dụ; dịch tự động văn bản, khai thác học liệu mở; nêu nguy cơ trên Internet, cách phòng vệ khi bị bắt nạt, bảo vệ dữ liệu cá nhân; trình bày sơ lược phần mềm độc hại và dùng công cụ diệt (Windows Defender).
- **Chủ đề 3. Đạo đức, pháp luật và văn hoá trong môi trường số** (SGV PDF 9): Nêu vấn đề pháp luật, đạo đức, văn hoá khi giao tiếp qua mạng; ví dụ vi phạm bản quyền và hậu quả; trình bày nội dung cơ bản của Luật Công nghệ thông tin, Luật An ninh mạng, nghị định liên quan; vận dụng để xác định tính hợp pháp của hành vi; biện pháp chia sẻ thông tin an toàn.
- **Chủ đề 4. Ứng dụng tin học** (SGV PDF 10): Sử dụng chức năng cơ bản của phần mềm thiết kế đồ hoạ (Inkscape); tạo sản phẩm số đơn giản như logo, banner, áp phích, thiệp.
- **Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính** (SGV PDF 10): Viết và thực hiện chương trình có dùng hằng, biến, cấu trúc điều khiển, toán tử, kiểu dữ liệu chuẩn và mảng (danh sách), lệnh vào ra; dùng chương trình con trong thư viện chuẩn; viết chương trình con biểu diễn thuật toán đơn giản; đọc hiểu chương trình; kiểm thử và gỡ lỗi; giải bài toán đơn giản có vận dụng kiến thức liên môn. Ngôn ngữ duy nhất là **Python**.
- **Chủ đề 6. Hướng nghiệp với tin học** (SGV PDF 10): Trình bày thông tin hướng nghiệp nhóm nghề Thiết kế và Lập trình (công việc chính, kiến thức kĩ năng, ngành học, nhu cầu nhân lực); tự tìm kiếm thông tin hướng nghiệp.

**Chuyên đề Khoa học máy tính** (nguồn: `SGV CD TIN HOC - Khoa hoc may tinh.pdf`, PDF 8–10):
- **Chuyên đề 1** (10 tiết): Trình bày sơ lược phân loại, vai trò, cơ chế hoạt động của các bộ phận chính của robot giáo dục (pin, động cơ DC, động cơ servo, bảng mạch, cảm biến, đèn LED, còi, dây cáp, bánh xe, thiết bị điều khiển từ xa); lắp ráp robot từ các bộ phận.
- **Chuyên đề 2** (8 tiết): Cài đặt phần mềm hỗ trợ, kết nối robot với máy tính, máy tính bảng, điện thoại qua wifi, bluetooth, USB; kiểm tra tình trạng sẵn sàng hoạt động của robot.
- **Chuyên đề 3** (14 tiết): Viết và thực hiện chương trình điều khiển robot làm thao tác đơn giản (cử động cánh tay, di chuyển tiến lùi). Bài toán điều khiển được thiết kế trên sa bàn. Lệnh được trình bày bằng **mã giả** chung, minh hoạ trên phần mềm GaraBlock (G-Robot); câu hỏi không nên phụ thuộc cú pháp riêng của một hãng robot.

**Chuyên đề Tin học ứng dụng** (nguồn: `SGV CD TIN HOC - Tin hoc ung ung.pdf`, PDF 6–9): Học theo **dự án** "Quảng bá dịch vụ du lịch" qua ba giai đoạn: Cẩm nang du lịch (soạn thảo văn bản: Styles, định dạng ảnh, hình khối, hộp văn bản, mục lục tự động, xuất .pdf); Chương trình báo giá (bảng tính: Format as Table, hộp kiểm, `IF`, `VLOOKUP`, `NOW`/`TODAY`, bảo vệ trang tính); truyền thông (trình chiếu: Slide Master, video, hiệu ứng nâng cao, Trigger, ghi âm, xuất video). Sách minh hoạ bằng Microsoft Office 365 (2021).

**Giới hạn và trọng tâm.** Agent sinh câu hỏi lưu ý:
- Bài 3–6 (biểu diễn dữ liệu, hệ nhị phân, lôgic, âm thanh – hình ảnh) chỉ dành cho định hướng CS; Bài 12–15 (Inkscape) chỉ dành cho ICT (SGV PDF 13).
- Hệ nhị phân: chỉ đổi số nguyên dương thập phân ↔ nhị phân, cộng và nhân nhị phân. Mã thuận, mã bù 1, mã bù 2 chỉ được giới thiệu qua ví dụ (SGK PDF 22). Đổi phần thập phân, mã bù 2 chi tiết thuộc phần Vận dụng (SGK PDF 24).
- Lôgic: bốn phép AND, OR, XOR, NOT; thứ tự ưu tiên: ngoặc → NOT → AND, OR ngang nhau, từ trái sang phải (SGK PDF 26). Trong Python chỉ có `and`, `or`, `not` (SGK PDF 102–103).
- Python: kiểu dữ liệu cơ bản int, float, str, bool, list. Không có kiểu kí tự riêng (SGK PDF 121). Lệnh lặp chỉ gồm `for … in range()` và `while`; `range` chỉ học dạng `range(stop)` và `range(start, stop)` (SGK PDF 107). Phương thức danh sách: `append`, `insert`, `remove`, `clear`; xâu: `find`, `split`, `join` (và `upper`, `lower`, `title` trong thực hành Bài 28).
- Luật: Luật Giao dịch điện tử (2005), Luật Công nghệ thông tin (2006), Luật An ninh mạng (2018), Luật Hình sự (2017); Nghị định 90/2008, 72/2013, 15/2020, 131/2013; Quyết định 874/QĐ-BTTTT (2021) (SGK PDF 58–62).

## 5. Sai lầm thường gặp của học sinh

SGV và SGV CD bộ này **không có mục "sai lầm thường gặp" riêng**. Bảng dưới tổng hợp các đoạn "GV nhấn mạnh", "GV chú ý HS", "dễ bị nhầm lẫn", "Lưu ý" chỉ ra điểm HS dễ hiểu sai. Cột Nguồn ghi trang PDF; `SGV` = `SGV TIN HOC 10.pdf`, `SGV CD KHMT` = `SGV CD TIN HOC - Khoa hoc may tinh.pdf`.

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Thông tin và dữ liệu (Bài 1) | Đồng nhất thông tin với dữ liệu. Một thông tin có nhiều dạng dữ liệu; cùng một dữ liệu ("39°C") mang thông tin khác nhau tuỳ hoàn cảnh; thiếu dữ liệu làm thông tin sai lệch (tính toàn vẹn). Máy tính xử lí dữ liệu; con người chuyển thông tin thành dữ liệu khi nhập và diễn giải dữ liệu thành thông tin khi nhận kết quả. | SGV PDF 18 |
| Kết nối vạn vật (Bài 8) | Cách nói "Internet vạn vật" gây hiểu lầm là mọi thứ kết nối qua Internet. IoT có thể dùng bất kì môi trường mạng nào (mạng cục bộ, vệ tinh, bluetooth, sóng radio, hồng ngoại). Điện toán đám mây mới bắt buộc dùng Internet. | SGV PDF 53 |
| Phép toán trên bit (Bài 5) | Kết quả phép toán lôgic chỉ phụ thuộc giá trị lôgic, không phụ thuộc nội dung mệnh đề. Phép toán trên dãy bit thực hiện từng cặp bit tương ứng, hai dãy phải cùng độ dài. | SGV PDF 40 |
| Hệ nhị phân (Bài 4) | Đổi phần thập phân sang nhị phân có thể không bao giờ kết thúc, phải dừng và chịu sai số làm tròn. | SGV PDF 38 |
| Bản quyền (Bài 11) | Nhầm "bản quyền" với "quyền tác giả": Luật Sở hữu trí tuệ chỉ dùng thuật ngữ quyền tác giả; bản quyền ưu tiên quyền lợi kinh tế của chủ sở hữu. Tác giả không nhất thiết là chủ sở hữu (lập trình viên được trả lương không có quyền bán phần mềm). Mua quyền sử dụng (licence) ≠ mua bản quyền; cài phần mềm mua cho một máy sang máy thứ hai là vi phạm. Chia sẻ lại tin vi phạm luật cũng là vi phạm luật. | SGV PDF 67; SGK PDF 60, 62 |
| Biến, lệnh gán (Bài 17) | Biến Python không khai báo kiểu, có thể nhận giá trị kiểu khác nhau tại các thời điểm khác nhau. Không cộng số với xâu (lỗi). Số biến bên trái lệnh gán đồng thời phải bằng số giá trị bên phải. Đặt tên biến bắt đầu bằng chữ số hoặc trùng từ khoá (`if`, `with`) gây lỗi. | SGV PDF 95; SGK PDF 93, 94, 96 |
| Lệnh `input()` (Bài 18) | Quên rằng `input()` **luôn trả về xâu kí tự**; muốn nhập số phải dùng `int(input())` hoặc `float(input())`. `int()` không đổi được xâu chứa số thực ("10.35") hay xâu biểu thức ("12+45"). | SGV PDF 97–98; SGK PDF 100 |
| Lệnh `if`, khối lệnh (Bài 19) | Quên dấu `:` sau điều kiện, không thụt lề thẳng hàng khối lệnh (1 tab hoặc 4 dấu cách); `if` và `else` phải thẳng hàng. | SGV PDF 100; SGK PDF 103–104 |
| `range()` (Bài 20, 29) | `range(n)` bắt đầu từ 0, kết thúc ở n − 1; `range(3)` là 0, 1, 2 nên tính tổng 1 + 2 + 3 bằng `range(3)` cho kết quả sai (lỗi lôgic). `range(100, 1)` là vùng rỗng. | SGK PDF 107, 143 |
| Xâu kí tự (Bài 24) | Gán `s[0] = "A"` để sửa một kí tự của xâu gây lỗi: xâu không thay đổi được từng kí tự (khác danh sách). | SGK PDF 120–121 |
| Hàm (Bài 26) | Gọi hàm luôn phải có cặp ngoặc tròn. Phân biệt hàm có giá trị trả lại (`input()`, `int()`) và không có giá trị trả lại (`print()`). | SGV PDF 118 |
| Tham số và đối số (Bài 27) | Hai khái niệm **rất dễ bị nhầm lẫn**: tham số khai báo khi định nghĩa hàm, đối số là giá trị truyền vào khi gọi hàm; số đối số phải bằng số tham số. | SGV PDF 120; SGK PDF 133 |
| Phạm vi của biến (Bài 28) | Biến khai báo trong hàm là biến cục bộ: không làm thay đổi biến cùng tên bên ngoài, gọi từ ngoài hàm sẽ báo lỗi. Bên trong hàm "nhìn thấy" giá trị biến ngoài nhưng không thao tác được như biến thường, trừ khi khai báo `global`. | SGV PDF 123–124 |
| Lỗi chương trình (Bài 29–30) | Chương trình chạy không báo lỗi chưa chắc đúng (lỗi lôgic, bug). Cần nhiều bộ test, có bộ test ngẫu nhiên và bộ test ở vùng biên vì lỗi thường phát sinh tại vùng biên. Debug là tìm và gỡ bỏ bug, không chỉ là chạy thử. | SGK PDF 143, 146; SGV PDF 129 |
| Robot giáo dục (SCD CS) | Đồng nhất "robot giáo dục" với "robot", "robot công nghiệp": robot giáo dục chỉ là mô hình minh hoạ đơn giản. | SGV CD KHMT PDF 8, 15 |
| Động cơ DC (SCD CS Bài 9) | Cho rằng cùng tham số tốc độ thì hai động cơ chạy như nhau: động cơ DC có thể chạy tốc độ khác nhau với cùng thông số, phụ thuộc nguồn điện và mặt đường. Động cơ trái phải nối cổng M1, động cơ phải nối cổng M2; lắp sai thì robot chuyển động ngược với lệnh điều khiển. | SGV CD KHMT PDF 22, 44; SCD KHMT PDF 40, 57 |
| Lệnh `Đợi` (SCD CS Bài 9) | Bỏ lệnh `Đợi` giữa `Đi thẳng` và `Dừng lại` khiến robot đứng im vì chưa kịp chuyển động. | SCD KHMT PDF 41 |
| Cảm biến (SCD CS Bài 10–11) | Cảm biến siêu âm chỉ đo trong giới hạn; vật xa hơn thì trả về khoảng cách lớn nhất (Max), không phải 0. Mắt dò đường: vùng tối = 0, vùng sáng = 1 (dễ đảo ngược). Lệnh đọc cảm biến phải đặt trong vòng lặp vô tận `forever`. | SGV CD KHMT PDF 50, 55; SCD KHMT PDF 46 |
| `VLOOKUP` (SCD ICT CĐ2 Bài 4) | Cột chứa giá trị cần tìm phải là cột đầu tiên của vùng tìm kiếm; `col_index_num` đếm trong vùng tìm kiếm (B3:E10 thì cột B là 1), không đếm theo tên cột trang tính. Bỏ qua `range_lookup` là tìm gần đúng. | SCD ICT PDF 42–44 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Bảy sách nguồn là PDF dạng ảnh. Định nghĩa đọc từ OCR (tesseract `vie`, 300 dpi, cache ở `.ocr/`) và đối chiếu ảnh trang (75–130 dpi) với mọi trang có bảng, cú pháp lệnh, kí hiệu: SGK PDF 9, 19, 22, 26, 29, 70–71, 78, 95–96, 102–103, 144, 167–168; SCD KHMT PDF 31–32, 52, 72; SCD ICT PDF 14, 38, 42, 80. Tài liệu bồi dưỡng GV có text layer, đọc trực tiếp.
- OCR không đọc được công thức và chữ đơn cách trong khung mã. Phần LaTeX/`\texttt{}` trong `definition` và toàn bộ `notation` **không được kiểm tra tự động**; phần này dựa vào đối chiếu ảnh khi trích và kiểm tra mẫu.
- Bổ sung cache OCR: nối thêm OCR 400 dpi (psm 4) cho SGK PDF 102, 167, 168; SCD KHMT PDF 72; SCD ICT PDF 80. Nếu xoá `.ocr/`, `check_sources.py` sẽ OCR lại theo mặc định và có thể gắn cờ `ham`, `bug-va-debug`, `chip-vi-dieu-khien`, `cam-bien-sieu-am`, `ma-gia`.
- Tên các mục `tinh_chat`, `quy_tac`, `ky_hieu`, `cong_thuc` thường do người trích đặt. Lần chạy gần nhất có 30 cảnh báo tên; nội dung các mục này vẫn đạt (bigram ≥ 0.65 ở nguồn định nghĩa).
- Nguồn `gv` (27 mục) và `sbt` phụ chỉ được kiểm tra sự có mặt của tên thuật ngữ trong 3 trang.
- Khoảng trang `pdf_pages` của SBT trong `progress.json` chỉ tính phần câu hỏi (PDF 5–70); phần đáp án PDF 71–148 ghi ở `answers_pdf_pages`.

**Kiểm tra tự động** (2026-10-15, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py tin_hoc_10` | 0 lỗi; 266 thuật ngữ |
| `check_sources.py tin_hoc_10` | 266 đạt, 0 gắn cờ, 0 không kiểm tra được, 30 cảnh báo về tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 18 lượt. 13 lượt do định nghĩa ghép câu thân bài với câu Bảng giải thích thuật ngữ ở trang xa: tách lại để mỗi mục dùng câu của một trang và đặt trang đó đầu `sources` (`ham`, `bug-va-debug`, `loi-ngoai-le`, `worm`, `chip-vi-dieu-khien`, `cam-bien-sieu-am`, `ma-gia`; tách thêm `ham-thiet-ke-san`, `nguyen-li-cam-bien-sieu-am`, `cam-bien-do-duong-bon-mat`). 2 lượt do OCR bảng dính chữ (`phep-so-sanh-trong-python`: chuyển nghĩa từng kí hiệu sang `notation`; bổ sung OCR 400 dpi). 1 lượt do tự diễn giải bảng chân lí (`phep-toan-logic-trong-python`: rút về câu nguyên văn, bảng chuyển sang `notation`). 1 lượt chen chữ "là loại trojan" (`backdoor`). 2 lượt tên không có nguyên văn (thêm alias "biểu thức lôgic", "thuộc tính cơ bản của ảnh"). 1 lượt thứ tự nguồn (`phan-mem-do-hoa`). Không mục nào sai nội dung. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-15, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/266 (11%): 20 ngẫu nhiên + 10 mục `cong_thuc`/`ky_hieu`/có `notation` |
| Cách chọn | `query.py tin_hoc_10 --audit` (seed 2026), danh sách ở `sample_audit.md` |
| Đối chiếu ảnh | 26 trang ảnh được mở lại (SGK PDF 8, 31, 35, 40, 68, 77, 88, 104, 107, 109, 110, 117, 118, 121, 125, 139; SCD KHMT PDF 11, 19, 41, 42, 45, 63; SCD ICT PDF 71; SBT PDF 18). Các trang còn lại của mẫu (SGK PDF 22, 26, 95, 103, 167, 168; SCD KHMT PDF 52; SCD ICT PDF 42, 80) đã đối chiếu ảnh khi trích. |
| Số mục sai | **2/30 (6,7%, vượt ngưỡng 5%)**: `lenh-range` ghi `range(10, 1)` thay vì `range(100, 1)` (SGK PDF 107); `dien-thoai-thong-minh` có `pdf_page` SBT lệch +1 (18 thay vì 17). Theo README mục 7 đã DỪNG và báo người dùng. Lỗi thứ hai là lỗi hệ thống: rà lại cả 8 nguồn `sbt` thì đều lệch +1 (đã sửa: `mang-may-tinh` 18, `ngon-ngu-lap-trinh` 35, `dien-thoai-thong-minh` 17, `do-hoa-may-tinh` 69, `do-sau-bit-am-thanh` 15, `tac-pham-phai-sinh` 25, `quyen-tai-san` 26, `quyen-nhan-than` 26). Cùng lúc sửa `lenh-if` ("thẳng lề trái" theo nguyên văn PDF 104) và thêm nguồn PDF 7 cho `thong-tin`. Nguồn SGK, SCD, SGV đánh số theo tên file cache OCR (= trang PDF) nên không mắc lỗi này. |
| Kiểm tra độc lập | Đã hoàn thành (người dùng đã kiểm tra lại mẫu độc lập sau khi sửa, đạt yêu cầu; đã xoá file mẫu). |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Tin học 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Kiểu dữ liệu danh sách, xâu, hàm (Bài 22–28) → mảng, thuật toán sắp xếp, tìm kiếm, độ phức tạp (lớp 11).
- Kiểm thử, gỡ lỗi (Bài 29–30) → kiểm thử và đánh giá chương trình (lớp 11).
- Mạng máy tính, Internet, IoT, điện toán đám mây (Bài 8) → thiết bị mạng, giao thức, kết nối (lớp 11, 12).
- Hệ quản trị cơ sở dữ liệu (Bài 2) → cơ sở dữ liệu (lớp 11).
- Quyền tác giả, luật CNTT (Bài 11) → đạo đức, pháp luật trong môi trường số các lớp sau.
- Liên môn: mệnh đề, giá trị chân lí, biểu thức lôgic (Bài 5) ↔ `toan_10` Chương I (Mệnh đề); sóng âm, tần số (Bài 6) ↔ `vat_ly_10`; động cơ, cảm biến robot (SCD CS) ↔ Công nghệ.
