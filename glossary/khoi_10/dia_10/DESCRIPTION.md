# Bộ thuật ngữ `dia_10` — Địa lí 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_10/dia_10/dia_10.json` (tập trung: `glossary/dataset/dia_10.json`), gồm **294 thuật ngữ** (cập nhật 2026-10-16). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_10/dia_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Dia li 10.pdf | sgk | 118 | Nguồn chính, Phần một + Chương 1–13 (40 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD Dia li 10.pdf | scd | 38 | Chuyên đề 10.1–10.3, chia mục La Mã, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV DIA LI 10.pdf | gv | 230 | Mục tiêu từng bài (mục 4–5); nguồn `gv` cho 14 thuật ngữ, nguồn chính cho 1 công thức (GNI–GDP) | Không (ảnh, OCR) |
| SGV CD DIA LI 10.pdf | gv | 50 | Yêu cầu cần đạt, mục tiêu từng chuyên đề (mục 4–5); nguồn `gv` cho 1 thuật ngữ | Không (ảnh, OCR) |
| SBT DIA LI 10.pdf | sbt | 122 | Câu hỏi, bài tập (PDF 6–96), gợi ý trả lời (PDF 97–122); chỉ nhắc lại khái niệm SGK → 0 mục | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Địa lí 10.pdf | gv | 45 | Thời lượng, cấu trúc SGK/SCD, thứ tự dạy chuyên đề (mục 4) | Có (đọc trực tiếp) |

- Ở năm sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- SGK: `chapter` = `Phần một. Một số vấn đề chung` (chỉ Bài 1) hoặc `Chương N. …`; `lesson` = `Bài N. …` (đánh số liên tục 1–40). SCD: `chapter` = `Chuyên đề 10.N. …`, `lesson` = mục La Mã `I. …`/`II. …`.
- SGK có **Bảng tra cứu thuật ngữ** (PDF 114, 22 mục) và SCD có bảng tương tự (PDF 34–35, 16 mục). Toàn bộ 38 mục đều có trong glossary, định nghĩa nguyên văn bảng; nguồn trang bảng đứng đầu, kèm trang thân bài. Mục trùng ở hai bảng (`bung-no-dan-so`, `khi-nha-kinh`, `nang-luong-tai-tao`) giữ định nghĩa SGK, thêm nguồn `scd` (khí nhà kính: SCD liệt kê thêm $O_3$, hơi nước — ghi ở `notation`; năng lượng tái tạo: nối thêm câu định nghĩa SCD).
- Nhiều nội dung trọng tâm của môn là **vai trò, đặc điểm, nhân tố ảnh hưởng, phân bố** của từng ngành; theo yêu cầu cần đạt, các nội dung này được tách thành mục `tinh_chat`, tóm lược sát câu chữ SGK. Không lấy số liệu thống kê minh hoạ, câu hỏi, bài thực hành (trừ chú giải bản đồ các đới khí hậu ở Bài 10).
- Bài thực hành (8, 10, 13, 16, 27, 32, 38) gần như không có khái niệm mới: Bài 8 có 1 mục (Nam Đại Dương, theo bảng tra cứu), Bài 10 có 1 mục; các bài còn lại 0 mục.
- Trùng id với bộ khác trong môn: không có (đây là bộ Địa lí đầu tiên). Hai khái niệm “gió địa phương” trong bài được đặt id `gio-dia-phuong-khi-quyen` để phân biệt với `gio-dia-phuong` (giờ địa phương).

## 2. Chương/bài và số thuật ngữ

| Chương / Chuyên đề | Bài / Mục | Số mục |
|---|---|---|
| Phần một. Một số vấn đề chung | Bài 1. Môn Địa lí với định hướng nghề nghiệp | 3 |
| Chương 1. Sử dụng bản đồ | Bài 2. Một số phương pháp biểu hiện các đối tượng địa lí trên bản đồ | 5 |
|  | Bài 3. Sử dụng bản đồ …, GPS và bản đồ số | 5 |
| Chương 2. Trái Đất | Bài 4. Sự hình thành Trái Đất, vỏ Trái Đất … | 15 |
|  | Bài 5. Hệ quả địa lí các chuyển động của Trái Đất | 8 |
| Chương 3. Thạch quyển | Bài 6. Thạch quyển, thuyết kiến tạo mảng | 6 |
|  | Bài 7. Nội lực và ngoại lực | 20 |
|  | Bài 8. Thực hành: … vành đai động đất, núi lửa | 1 |
| Chương 4. Khí quyển | Bài 9. Khí quyển, các yếu tố khí hậu | 19 |
|  | Bài 10. Thực hành: Đọc bản đồ các đới và các kiểu khí hậu … | 1 |
| Chương 5. Thuỷ quyển | Bài 11. Thuỷ quyển, nước trên lục địa | 12 |
|  | Bài 12. Nước biển và đại dương | 9 |
| Chương 6. Sinh quyển | Bài 14. Đất trên Trái Đất | 5 |
|  | Bài 15. Sinh quyển | 3 |
| Chương 7. Một số quy luật của vỏ địa lí | Bài 17. Vỏ địa lí, quy luật thống nhất và hoàn chỉnh | 2 |
|  | Bài 18. Quy luật địa đới và quy luật phi địa đới | 5 |
| Chương 8. Địa lí dân cư | Bài 19. Quy mô dân số, gia tăng dân số và cơ cấu dân số | 21 |
|  | Bài 20. Phân bố dân cư và đô thị hoá | 6 |
| Chương 9. Các nguồn lực, một số tiêu chí … | Bài 21. Các nguồn lực phát triển kinh tế | 3 |
|  | Bài 22. Cơ cấu kinh tế, GDP và GNI | 8 (1 từ SGV) |
| Chương 10. Địa lí ngành nông nghiệp, lâm nghiệp, thuỷ sản | Bài 23. Vai trò, đặc điểm, các nhân tố … | 6 |
|  | Bài 24. Địa lí ngành nông nghiệp | 8 |
|  | Bài 25. Địa lí ngành lâm nghiệp và ngành thuỷ sản | 8 |
|  | Bài 26. Tổ chức lãnh thổ nông nghiệp … | 6 |
| Chương 11. Địa lí ngành công nghiệp | Bài 28. Vai trò, đặc điểm, cơ cấu … | 7 |
|  | Bài 29. Địa lí một số ngành công nghiệp | 7 |
|  | Bài 30. Tổ chức lãnh thổ công nghiệp | 4 |
|  | Bài 31. Tác động của công nghiệp đối với môi trường … | 4 |
| Chương 12. Địa lí ngành dịch vụ | Bài 33. Cơ cấu, vai trò, đặc điểm … dịch vụ | 4 |
|  | Bài 34. Địa lí ngành giao thông vận tải | 9 |
|  | Bài 35. Địa lí ngành bưu chính viễn thông | 4 |
|  | Bài 36. Địa lí ngành du lịch | 4 |
|  | Bài 37. Địa lí ngành thương mại và ngành tài chính ngân hàng | 9 |
| Chương 13. Phát triển bền vững và tăng trưởng xanh | Bài 39. Môi trường và tài nguyên thiên nhiên | 8 |
|  | Bài 40. Phát triển bền vững và tăng trưởng xanh | 4 |
| Chuyên đề 10.1. Biến đổi khí hậu | I. Khái niệm và biểu hiện … | 4 |
|  | II. Nguyên nhân gây biến đổi khí hậu | 7 |
|  | III. Tác động và hậu quả … | 5 |
|  | IV. Ứng phó với biến đổi khí hậu | 7 |
| Chuyên đề 10.2. Đô thị hoá | I. Khái niệm | 2 |
|  | II. Đô thị hoá ở các nước phát triển | 7 |
|  | III. Đô thị hoá ở các nước đang phát triển | 3 |
|  | IV. Tác động của đô thị hoá ở các nước đang phát triển | 3 |
| Chuyên đề 10.3. Phương pháp viết báo cáo địa lí | I. Những vấn đề chung về báo cáo địa lí | 2 |
|  | II. Các bước viết báo cáo địa lí | 5 |

Các bài 13, 16, 27, 32, 38 (thực hành) có 0 mục. Khi lọc: `--lesson "Bài 19."` (SGK, số bài duy nhất); `--chapter "Chuyên đề 10.1" --lesson "II."` (SCD). `--lesson "I."` khớp cả `II.`/`III.`/`IV.` — nên dùng tên mục đầy đủ.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 168 |
| tinh_chat | 102 |
| quy_tac | 20 |
| cong_thuc | 3 |
| dinh_ly | 1 |
| ky_hieu | 0 |

- Theo `level`: `co_ban` 249, `chuyen_de` 45.
- Theo nguồn định nghĩa: SGK 248, SCD 45, SGV 1 (`quan-he-gdp-va-gni`: SGK chỉ đặt câu hỏi so sánh GDP–GNI, SGV nêu rõ quan hệ và công thức tính GNI từ GDP).
- 16 mục mang nguồn `gv` (15 SGV, 1 SGV CD); 18 mục có nguồn từ hơn một file.
- `cong_thuc` (3): GDP/GNI bình quân đầu người, tỉ lệ dân thành thị (SCD), quan hệ GNI–GDP (SGV). Thêm công thức tỉ suất sinh thô, tử thô, nhập cư, xuất cư (SGV PDF 109) vào `notation` của 4 mục `dinh_nghia` tương ứng. 23 mục có `notation`.
- `dinh_ly` (1): thuyết kiến tạo mảng.
- `quy_tac` (20): phân loại (đá, hồ, nguồn lực, tài nguyên, cây công nghiệp, quy mô đô thị, khối khí, đới khí hậu, chế độ triều), ngưỡng dân số trẻ/già/vàng, tiêu chí đánh giá giao thông vận tải, đường chuyển ngày quốc tế, các bước/cấu trúc/yêu cầu báo cáo địa lí, giải pháp bảo vệ nước ngọt, nhóm giải pháp ứng phó biến đổi khí hậu.
- 1 mục có `notes`: `cac-doi-khi-hau-tren-trai-dat` (trích từ chú giải bản đồ Hình 10.1, chữ nhỏ).

## 4. Yêu cầu cần đạt theo chương

Nguồn: `SGV DIA LI 10.pdf`, phần “I. Mục tiêu – 1. Về kiến thức, kĩ năng” đầu mỗi bài (trang PDF trong ngoặc). Trích rút gọn.

- **Phần một – Bài 1** (SGV tr.23): Khái quát đặc điểm cơ bản, vai trò của môn Địa lí; xác định các ngành nghề liên quan đến kiến thức địa lí.
- **Chương 1. Sử dụng bản đồ** (tr.27, 32): Phân biệt các phương pháp biểu hiện đối tượng địa lí trên bản đồ (kí hiệu, kí hiệu đường chuyển động, bản đồ – biểu đồ, chấm điểm, khoanh vùng); sử dụng bản đồ trong học tập và đời sống; xác định một số ứng dụng của GPS và bản đồ số.
- **Chương 2. Trái Đất** (tr.37, 42): Trình bày nguồn gốc hình thành Trái Đất, đặc điểm vỏ Trái Đất, vật liệu cấu tạo; phân biệt khoáng vật và đá, các nhóm đá theo nguồn gốc. Phân tích hệ quả địa lí của chuyển động tự quay (luân phiên ngày đêm, giờ) và quanh Mặt Trời (các mùa, ngày đêm dài ngắn theo vĩ độ).
- **Chương 3. Thạch quyển** (tr.48, 52, 56): Khái niệm thạch quyển, **phân biệt thạch quyển với vỏ Trái Đất**; khái quát thuyết kiến tạo mảng, vận dụng giải thích vùng núi trẻ, vành đai động đất, núi lửa; khái niệm, nguyên nhân nội lực và ngoại lực, tác động đến địa hình.
- **Chương 4. Khí quyển** (tr.59, 67): Khái niệm khí quyển; phân bố nhiệt độ theo vĩ độ, lục địa – đại dương, địa hình; các đai khí áp, nguyên nhân thay đổi khí áp; gió chính, gió địa phương; nhân tố ảnh hưởng và phân bố lượng mưa; đọc bản đồ các đới, kiểu khí hậu.
- **Chương 5. Thuỷ quyển** (tr.71, 77, 83): Khái niệm thuỷ quyển; nhân tố ảnh hưởng chế độ nước sông; phân biệt các loại hồ theo nguồn gốc; đặc điểm nước băng tuyết, nước ngầm; giải pháp bảo vệ nước ngọt; tính chất nước biển; giải thích sóng, thuỷ triều; chuyển động dòng biển; vai trò của biển và đại dương.
- **Chương 6. Sinh quyển** (tr.85, 89): Khái niệm đất, **phân biệt đất và vỏ phong hoá**, xác định các tầng đất, phân tích năm nhân tố hình thành đất; khái niệm, đặc điểm, giới hạn sinh quyển; nhân tố ảnh hưởng đến sinh vật.
- **Chương 7. Một số quy luật của vỏ địa lí** (tr.97, 101): Khái niệm vỏ địa lí, **phân biệt vỏ địa lí và vỏ Trái Đất**; khái niệm, biểu hiện, ý nghĩa thực tiễn của quy luật thống nhất và hoàn chỉnh, quy luật địa đới và phi địa đới.
- **Chương 8. Địa lí dân cư** (tr.106, 115): Đặc điểm, tình hình phát triển dân số; **phân biệt gia tăng tự nhiên và cơ học**, khái niệm gia tăng thực tế; nhân tố tác động; các loại cơ cấu dân số (sinh học, xã hội); so sánh tháp dân số; nhân tố tác động phân bố dân cư; khái niệm, nhân tố, ảnh hưởng của đô thị hoá.
- **Chương 9. Nguồn lực, tiêu chí đánh giá** (tr.122, 127): Khái niệm, phân loại, vai trò nguồn lực; khái niệm cơ cấu kinh tế, phân biệt cơ cấu theo ngành/thành phần/lãnh thổ; **so sánh GDP, GNI, GDP và GNI bình quân đầu người**.
- **Chương 10. Nông nghiệp, lâm nghiệp, thuỷ sản** (tr.132, 137, 143, 148): Vai trò, đặc điểm, nhân tố ảnh hưởng; vai trò, đặc điểm các ngành trồng trọt, chăn nuôi, lâm nghiệp, thuỷ sản; phân bố cây trồng, vật nuôi chính; quan niệm, vai trò tổ chức lãnh thổ nông nghiệp, phân biệt các hình thức; vấn đề nông nghiệp hiện đại, định hướng tương lai.
- **Chương 11. Công nghiệp** (tr.156, 161, 169, 174): Vai trò, đặc điểm, cơ cấu, nhân tố ảnh hưởng; vai trò, đặc điểm, phân bố các ngành khai thác than, dầu khí, quặng kim loại, điện lực, điện tử – tin học, hàng tiêu dùng, thực phẩm; tổ chức lãnh thổ công nghiệp; tác động đến môi trường, sự cần thiết phát triển năng lượng tái tạo, định hướng tương lai.
- **Chương 12. Dịch vụ** (tr.180, 187, 194, 200, 205): Cơ cấu, vai trò, đặc điểm, nhân tố ảnh hưởng của dịch vụ và từng ngành (giao thông vận tải, bưu chính viễn thông, du lịch, thương mại, tài chính ngân hàng); tình hình phát triển và phân bố trên thế giới.
- **Chương 13. Phát triển bền vững và tăng trưởng xanh** (tr.214, 221): Phân biệt khái niệm, đặc điểm môi trường và tài nguyên thiên nhiên, vai trò của chúng; khái niệm và sự cần thiết của phát triển bền vững; khái niệm, biểu hiện của tăng trưởng xanh.

**Chuyên đề** (nguồn: `SGV CD DIA LI 10.pdf` PDF 8–9 “Nội dung và yêu cầu cần đạt”, mục tiêu PDF 14, 25, 42):
- **Chuyên đề 10.1. Biến đổi khí hậu** (10 tiết): Khái niệm, biểu hiện; giải thích nguyên nhân; phân tích tác động và hậu quả trên phạm vi toàn cầu; giải thích tầm quan trọng, sự cấp bách của ứng phó; hệ thống hoá các nhóm giải pháp (giảm nhẹ, thích ứng).
- **Chuyên đề 10.2. Đô thị hoá** (15 tiết): Khái niệm đô thị hoá theo nghĩa hẹp và nghĩa rộng; ý nghĩa của tỉ lệ dân thành thị; đặc điểm, xu hướng đô thị hoá ở nước phát triển và đang phát triển, so sánh hai nhóm nước; phân biệt quy mô đô thị; tác động tích cực, tiêu cực ở nước đang phát triển, liên hệ Việt Nam.
- **Chuyên đề 10.3. Phương pháp viết báo cáo địa lí** (10 tiết): Quan niệm, cấu trúc báo cáo địa lí; các bước: chọn đề tài, xây dựng đề cương, thu thập – xử lí – hệ thống hoá thông tin, trình bày báo cáo.

**Giới hạn chung** (`Tài liệu bồi dưỡng GV …` PDF 5–9; SGV PDF 22): SGK 70 tiết (8 tiết ôn tập, kiểm tra), 3 phần, 13 chương, 40 bài; chuyên đề 35 tiết, là kiến thức mở rộng, nên dạy sau phần cơ bản. Chuyên đề 10.1 nên dạy sau chương Khí quyển; Chuyên đề 10.3 nên bố trí đầu năm. Môn Địa lí THPT theo CT 2018 là môn **tự chọn**. Kiến thức địa lí tự nhiên đại cương đã học kĩ ở lớp 6 “về nguyên tắc sẽ không lặp lại ở lớp 10” — GV gợi mở để HS tái hiện. SGK theo hướng tinh giản: không mở rộng ngoài yêu cầu cần đạt. Chương Sử dụng bản đồ được đưa vào Phần một (khác SGK cũ).

## 5. Sai lầm thường gặp của học sinh

SGV và SGV CD bộ này **không có mục “sai lầm thường gặp” riêng**. Bảng dưới tổng hợp các yêu cầu “phân biệt”, “nhấn mạnh”, “lưu ý” chỉ ra điểm HS dễ nhầm (cột Nguồn: trang PDF của `SGV DIA LI 10.pdf`, hoặc `SGV CD` cho `SGV CD DIA LI 10.pdf`).

| Nội dung | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Phương pháp biểu hiện bản đồ (Bài 2) | Lẫn các phương pháp; SGV yêu cầu lập bảng phân biệt theo đối tượng, hình thức, khả năng thể hiện. | SGV tr.30 |
| Thạch quyển (Bài 6) | Đồng nhất thạch quyển với vỏ Trái Đất: thạch quyển gồm vỏ Trái Đất **và** phần cứng mỏng phía trên của manti, dày khoảng 100 km; vỏ Trái Đất chỉ dày 5–70 km, giới hạn dưới là mặt Mô-hô. | SGV tr.50; SGK PDF 22 |
| Vận động của nước biển (Bài 12) | Lẫn sóng, thuỷ triều, dòng biển: sóng chủ yếu do gió; thuỷ triều do lực hấp dẫn Mặt Trăng, Mặt Trời và lực li tâm; dòng biển do gió thường xuyên, chênh lệch nhiệt độ, độ muối. | SGV tr.82; SGK PDF 42–44 |
| Đất (Bài 14) | Đồng nhất đất với vỏ phong hoá: vỏ phong hoá là sản phẩm phong hoá đá gốc; đất là lớp vật chất mỏng có độ phì, cung cấp dinh dưỡng cho thực vật. Con người không tham gia hình thành đất tự nhiên (SGK) dù SGV liệt kê “con người” trong các nhân tố. | SGV tr.87; SGK PDF 47 |
| Vỏ địa lí (Bài 17) | Đồng nhất vỏ địa lí với vỏ Trái Đất: vỏ địa lí (30–35 km) gồm các quyển xâm nhập lẫn nhau. Quy luật thống nhất và hoàn chỉnh là khái niệm trừu tượng, cần ví dụ cụ thể. | SGV tr.99; SGK PDF 52 |
| Gia tăng dân số (Bài 19) | Coi gia tăng cơ học làm tăng dân số thế giới: gia tăng cơ học chỉ là thay đổi nơi cư trú, không ảnh hưởng dân số toàn thế giới; gia tăng tự nhiên mới là động lực. Dân số một năm lấy số dân trung bình (giữa năm). | SGV tr.108–109 |
| Đô thị hoá (Bài 20) | Coi điều kiện tự nhiên là nhân tố quyết định: chỉ tạo thuận lợi/khó khăn; nhân tố kinh tế – xã hội mới có tính quyết định. | SGV tr.118 |
| GDP – GNI (Bài 22) | Nhầm phạm vi tính: GDP theo **lãnh thổ** quốc gia, GNI theo **quyền sở hữu của công dân**. Ví dụ nhà máy Samsung ở Việt Nam: giá trị tính vào GDP Việt Nam và GNI Hàn Quốc. SGV đánh giá đây là nội dung khó, khô khan. | SGV tr.129–130 |
| Hiệu ứng nhà kính (CĐ 10.1) | Coi hiệu ứng nhà kính là có hại: đây là hiện tượng tự nhiên giữ Trái Đất đủ ấm; sự **gia tăng** khí nhà kính mới gây biến đổi khí hậu. | SCD PDF 8; SGV CD tr.24 |
| Biến đổi khí hậu (CĐ 10.1) | Cho rằng biến đổi khí hậu mang tính cục bộ: khí nhà kính được hoàn lưu khí quyển xáo trộn đều nên biến đổi khí hậu mang tính toàn cầu. | SGV CD tr.24 |
| Quy mô đô thị (CĐ 10.2) | Áp ngưỡng phân loại quy mô đô thị chung cho mọi nước: bảng phân loại nhỏ/trung bình/lớn/siêu đô thị trong SCD là cách phân loại **ở các nước phát triển**. | SGV CD tr.9, 30–31; SCD PDF 20 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Năm sách nguồn là PDF dạng ảnh. Định nghĩa đọc từ ảnh trang (85–130 dpi) đối chiếu OCR (tesseract `vie`, 300 dpi, cache ở `.ocr/`).
- Bổ sung cache OCR (nối thêm OCR 400 dpi vùng cắt): SGK PDF 36 (chú giải bản đồ khí hậu), PDF 57 (hộp “Em có biết?” di cư quốc tế), PDF 114 (bảng tra cứu: OCR cột tên và cột định nghĩa theo dải), SCD PDF 34–35 (bảng tra cứu). Nếu xoá `.ocr/`, `check_sources.py` có thể gắn cờ lại các mục bảng tra cứu.
- Mục `tinh_chat` là tóm lược sát câu chữ SGK; tên mục do người trích đặt theo đề mục sách. 27 cảnh báo tên (`tinh_chat`/`quy_tac`/`cong_thuc` không có nguyên văn tên trong trang) — nội dung đều đạt bigram ≥ 0.65.
- `check_sources.py` so khớp trong cửa sổ 3 trang (trang nguồn ± 1), nên **không phát hiện lệch trang 1 đơn vị**. Đã bổ sung một lần rà riêng (so bigram định nghĩa trên trang nguồn với trang lân cận) — xem dưới.
- SGV liệt kê “con người” là nhân tố hình thành đất, SGK nói con người không tham gia hình thành đất tự nhiên; glossary giữ theo SGK.

**Kiểm tra tự động** (2026-10-16, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py dia_10` | 0 lỗi; 294 thuật ngữ |
| `check_sources.py dia_10` | 294 đạt, 0 gắn cờ, 0 không kiểm tra được, 27 cảnh báo tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | Khoảng 20 mục, phân loại: đa số do OCR bảng tra cứu SGK/SCD tách dòng hoặc bỏ sót tên (bổ sung OCR vùng cắt 400 dpi); 4 do định nghĩa tóm lược lệch câu chữ (viết lại sát nguyên văn: `vo-dai-duong`, `vo-luc-dia`, `bung-no-dan-so`, `di-cu-quoc-te`); 1 do nguồn phụ sai trang (`bao-ve-moi-truong`: PDF 109 → 112); 1 do tên thân bài khác tên mục (thêm alias `Đô thị hoá` cho `quan-niem-ve-do-thi-hoa`). Một lỗi ghi dữ liệu (kí tự tab trong LaTeX `\text` ở 5 `notation`) đã sửa. |
| Rà lệch trang ±1 (ngoài `check_sources`) | Phát hiện 10 mục nguồn lệch +1 trang (9 mục Bài 37 thương mại – tài chính ngân hàng, 1 mục `phan-loai-cay-cong-nghiep`); đã sửa, chạy lại: 0 mục lệch. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-16, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/294 (10,2%) |
| Cách chọn | `query.py dia_10 --audit` (seed 2026: 20 mục ngẫu nhiên + 10 mục công thức/kí hiệu). Danh sách ở `sample_audit.md`. |
| Đối chiếu ảnh | Mở lại ảnh trong phiên kiểm tra: SGK PDF 6, 10, 24, 26, 27, 38, 42, 54, 57, 65, 67, 70, 89, 94, 97, 102, 106, 114; SGV PDF 129–130. Các trang SCD của mẫu (PDF 8, 9, 10, 12, 23–25, 28, 34, 35) đã đối chiếu ảnh khi trích. |
| Số mục sai | **1/30 (3,3%, dưới ngưỡng 5%)**: `to-chuc-thuong-mai-the-gioi` ghi PDF 106, thực tế PDF 105 (nội dung đúng). Truy nguyên ra lỗi hệ thống ở Bài 37 (xem dòng “Rà lệch trang”); đã sửa toàn bộ. |
| Kiểm tra độc lập | Chưa thực hiện. `sample_audit.md` (đã xuất lại sau khi sửa) được giữ lại cho người kiểm tra ở phiên riêng; xoá sau khi kiểm tra xong. |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Địa lí 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Đô thị hoá, dân số, cơ cấu kinh tế, GDP/GNI (Chương 8–9, Chuyên đề 10.2) → địa lí kinh tế – xã hội thế giới và các khu vực, quốc gia (lớp 11).
- Biến đổi khí hậu, thiên tai (Chuyên đề 10.1) → Chuyên đề 12.1 Thiên tai và biện pháp phòng chống (lớp 12).
- Nông nghiệp, công nghiệp, dịch vụ, tổ chức lãnh thổ (Chương 10–12) → địa lí các ngành kinh tế Việt Nam (lớp 12).
- Liên môn: GPS, bản đồ số ↔ `tin_hoc_10`; khí nhà kính, CO₂, CH₄ ↔ `hoa_10`; sinh quyển, hệ sinh thái, đa dạng sinh học ↔ `sinh_10`; Đông Nam Á, ngữ hệ ↔ `lich_su_10`.
