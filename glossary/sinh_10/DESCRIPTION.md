# Bộ thuật ngữ `sinh_10` — Sinh học 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/sinh_10/sinh_10.json`, gồm **299 thuật ngữ** (cập nhật 2026-10-14). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sinh_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Sinh hoc 10.pdf | sgk | 162 | Nguồn chính, Phần mở đầu và Chương 1–7, `level: co_ban` | Không (ảnh, OCR) |
| SCD Sinh hoc 10.pdf | scd | 78 | Chuyên đề 1–3, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV SINH HOC 10.pdf | gv | 154 | SGV phần cơ bản: mục tiêu từng chương, điểm cần lưu ý (mục 4–5); nguồn `gv` phụ cho 7 thuật ngữ | Không (ảnh, OCR) |
| SBT SINH HOC 10.pdf | sbt | 94 | Bổ sung 4 khái niệm SGK không nêu tường minh; thêm nguồn `sbt` cho 2 mục. Chia theo chương, không theo bài | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Sinh học 10.pdf | gv | 49 | Nội dung chương trình, khung kế hoạch 70 tiết (mục 4) | Có |

- Ở cả bốn sách dạng ảnh: **trang PDF = trang in + 1**.
- SGK (trang in 158–159) và SCD (trang in 75) có bảng "Giải thích một số thuật ngữ dùng trong sách". Các mục trong bảng đều đã có trong glossary; 10 mục lấy định nghĩa trực tiếp từ bảng (`lien-ket-cong-hoa-tri`, `lien-ket-hydrogen`, `biet-hoa`, `ho-hap-ki-khi`, `probiotics` ở SGK; `bien-nap`, `tham-tich`, `thanh-trung`, `kim-loai-nang`, `bui-min` ở SCD).
- SGV không có bài 26 (thực hành) và không có SGV Chuyên đề. Mỗi chương SGV có phần mở đầu chương (`intro_pdf_pages` trong `progress.json`).
- Các bài thực hành (6, 9, 11, 15, 18, 23, 26) và bài dự án chuyên đề (4, 8, 12) chủ yếu là quy trình; chỉ Bài 6 có khái niệm (ba phép thử nhận biết).
- Mục lục dùng chung số "Bài 1, 2, …" cho cả SGK và SCD. Khi lọc, kết hợp `--chapter` hoặc `--level`. Ví dụ: `--lesson "Bài 5." --level co_ban` là Bài 5 SGK (Các phân tử sinh học); `--lesson "Bài 5." --level chuyen_de` là Bài 5 Chuyên đề (Khái quát về công nghệ enzyme).

## 2. Chương/bài và số thuật ngữ

Cột "Tổng" đã gồm các mục bổ sung từ SBT, đếm riêng ở cột cuối. Bài không liệt kê (thực hành/dự án) có 0 mục.

| Chương / Chuyên đề | Bài | Tổng | Từ SBT |
|---|---|---|---|
| Phần mở đầu | Bài 1. Giới thiệu khái quát môn Sinh học | 11 | |
| | Bài 2. Phương pháp nghiên cứu và học tập môn Sinh học | 17 | |
| | Bài 3. Các cấp độ tổ chức của thế giới sống | 12 | |
| Chương 1. Thành phần hoá học của tế bào | Bài 4. Các nguyên tố hoá học và nước | 10 | |
| | Bài 5. Các phân tử sinh học | 35 | 1 |
| | Bài 6. Thực hành: Nhận biết một số phân tử sinh học | 3 | |
| Chương 2. Cấu trúc tế bào | Bài 7. Tế bào nhân sơ | 10 | |
| | Bài 8. Tế bào nhân thực | 24 | |
| Chương 3. Trao đổi chất qua màng và truyền tin tế bào | Bài 10. Trao đổi chất qua màng tế bào | 16 | |
| | Bài 12. Truyền tin tế bào | 6 | |
| Chương 4. Chuyển hoá năng lượng trong tế bào | Bài 13. Khái quát về chuyển hoá vật chất và năng lượng | 13 | |
| | Bài 14. Phân giải và tổng hợp các chất trong tế bào | 19 | 2 |
| Chương 5. Chu kì tế bào và phân bào | Bài 16. Chu kì tế bào và nguyên phân | 9 | |
| | Bài 17. Giảm phân | 6 | |
| | Bài 19. Công nghệ tế bào | 10 | |
| Chương 6. Sinh học vi sinh vật | Bài 20. Sự đa dạng và phương pháp nghiên cứu vi sinh vật | 8 | |
| | Bài 21. Trao đổi chất, sinh trưởng và sinh sản ở vi sinh vật | 17 | |
| | Bài 22. Vai trò và ứng dụng của vi sinh vật | 6 | |
| Chương 7. Virus | Bài 24. Khái quát về virus | 7 | |
| | Bài 25. Một số bệnh do virus và các thành tựu nghiên cứu ứng dụng virus | 10 | 1 |
| Chuyên đề 1. Công nghệ tế bào và một số thành tựu | Bài 1. Công nghệ tế bào thực vật và thành tựu | 5 | |
| | Bài 2. Tế bào gốc và một số thành tựu | 6 | |
| | Bài 3. Công nghệ tế bào động vật và thành tựu | 6 | |
| Chuyên đề 2. Công nghệ enzyme và ứng dụng | Bài 5. Khái quát về công nghệ enzyme | 6 | |
| | Bài 6. Quy trình công nghệ sản xuất enzyme | 8 | |
| | Bài 7. Ứng dụng của enzyme | 4 | |
| Chuyên đề 3. Công nghệ vi sinh vật trong xử lí ô nhiễm môi trường | Bài 9. Vai trò của vi sinh vật trong xử lí ô nhiễm môi trường | 5 | |
| | Bài 10. Vi sinh vật trong phân giải các hợp chất làm ô nhiễm môi trường | 5 | |
| | Bài 11. Công nghệ ứng dụng vi sinh vật trong xử lí ô nhiễm môi trường | 5 | |

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 239 |
| tinh_chat | 40 |
| quy_tac | 17 |
| cong_thuc | 2 |
| dinh_ly | 1 |
| ky_hieu | 0 |

- Theo `level`: `co_ban` 249, `chuyen_de` 50.
- Theo nguồn định nghĩa: SGK 245, SCD 50, SBT 4. Có 7 mục mang thêm nguồn `gv`, 2 mục mang thêm nguồn `sbt` phụ.
- 20 mục có `notation`; 1 mục có `notes` (`sinh-10-polymer`).
- Sinh học ít công thức: chỉ `phuong-trinh-ho-hap` và `cong-thuc-so-te-bao` là `cong_thuc`; các phương trình khác (quang hợp, hoá tổng hợp, phép thử Benedict, nguyên tắc bổ sung) nằm trong `notation`. Chỉ "Học thuyết tế bào" được gắn `dinh_ly`.
- Một số khái niệm xuất hiện ở cả SGK và SCD với phát biểu khác nhau được tách thành hai mục (hậu tố `-chuyen-de`): công nghệ tế bào thực vật/động vật, tế bào gốc, liệu pháp tế bào gốc, liệu pháp gene. Hai mục nối nhau bằng `related_terms`.

## 4. Yêu cầu cần đạt theo chương

Nguồn: `SGV SINH HOC 10.pdf`, phần "I. Mục tiêu — 1. Kiến thức" ở đầu mỗi chương (trang PDF ghi trong ngoặc); số tiết theo Tài liệu bồi dưỡng GV, mục 2.4 (trang PDF 18–19). Trích rút gọn.

- **Phần mở đầu** (6 tiết; SGV tr.19): Nêu đối tượng, lĩnh vực nghiên cứu, mục tiêu của sinh học; vai trò của sinh học với cuộc sống, phát triển bền vững và các vấn đề toàn cầu; triển vọng và ngành nghề liên quan. Trình bày định nghĩa phát triển bền vững; mối quan hệ sinh học với đạo đức sinh học, kinh tế, công nghệ. Trình bày và vận dụng phương pháp quan sát, phương pháp làm việc trong phòng thí nghiệm, phương pháp thực nghiệm khoa học; các kĩ năng trong tiến trình nghiên cứu (quan sát, xây dựng giả thuyết, thiết kế thí nghiệm, điều tra, báo cáo). Giới thiệu tin sinh học như công cụ nghiên cứu. Nêu các cấp độ tổ chức và đặc điểm chung của thế giới sống.
- **Chương 1. Thành phần hoá học của tế bào** (9 tiết; SGV tr.28): Nêu khái quát học thuyết tế bào; giải thích tế bào là đơn vị cấu trúc và chức năng. Liệt kê nguyên tố chính (C, H, O, N, S, P); vai trò nguyên tố đa lượng, vi lượng và của carbon. Cấu tạo phân tử nước quy định tính chất và vai trò sinh học của nước. Khái niệm phân tử sinh học; thành phần cấu tạo (nguyên tố, đơn phân) và vai trò của carbohydrate, lipid, protein, nucleic acid; mối quan hệ cấu tạo – vai trò. Thực hành nhận biết định tính protein, lipid, đường.
- **Chương 2. Cấu trúc tế bào** (9 tiết; SGV tr.49): Mô tả kích thước, cấu tạo, chức năng các thành phần tế bào nhân sơ. Phân tích quan hệ cấu tạo – chức năng các thành phần tế bào nhân thực (thành tế bào, các bào quan); cấu tạo, chức năng tế bào chất và nhân. Lập bảng so sánh tế bào nhân sơ – nhân thực, tế bào động vật – thực vật. Làm tiêu bản và quan sát tế bào.
- **Chương 3. Trao đổi chất qua màng và truyền tin tế bào** (6 tiết; SGV tr.73): Nêu khái niệm trao đổi chất ở tế bào. Phân biệt vận chuyển thụ động, chủ động; trình bày nhập bào, xuất bào qua biến dạng màng. Giải thích hiện tượng thực tiễn (muối dưa, muối cà). Thí nghiệm co và phản co nguyên sinh. Nêu khái niệm thông tin giữa các tế bào; trình bày ba quá trình tiếp nhận – truyền tin – đáp ứng.
- **Chương 4. Chuyển hoá năng lượng trong tế bào** (9 tiết; SGV tr.89): Khái niệm chuyển hoá năng lượng, các dạng năng lượng; năng lượng tích luỹ dạng hoá năng. Cấu tạo, chức năng ATP. Khái niệm chuyển hoá vật chất. Vai trò, cấu trúc, cơ chế tác động của enzyme; yếu tố ảnh hưởng hoạt tính enzyme. Khái niệm tổng hợp; vai trò quang hợp, hoá tổng hợp, quang khử. Khái niệm phân giải; các giai đoạn phân giải hiếu khí (hô hấp tế bào) và kị khí (lên men). Mối quan hệ tổng hợp – phân giải.
- **Chương 5. Chu kì tế bào và phân bào** (10 tiết; SGV tr.105): Khái niệm chu kì tế bào, các giai đoạn và mối quan hệ. Giải thích nguyên phân dựa vào nhân đôi và phân li NST; phân chia không bình thường dẫn đến ung thư, biện pháp phòng tránh. Giải thích giảm phân, thụ tinh cùng nguyên phân là cơ sở sinh sản hữu tính; nhân tố ảnh hưởng giảm phân; so sánh nguyên phân – giảm phân. Khái niệm, nguyên lí và thành tựu công nghệ tế bào thực vật, động vật.
- **Chương 6. Sinh học vi sinh vật** (13 tiết; SGV tr.118): Khái niệm vi sinh vật, các nhóm và kiểu dinh dưỡng. Phương pháp nghiên cứu vi sinh vật. Ví dụ tổng hợp và phân giải ở vi sinh vật. Khái niệm sinh trưởng, các pha sinh trưởng quần thể vi khuẩn, yếu tố ảnh hưởng. Ý nghĩa kháng sinh và tác hại của lạm dụng kháng sinh. Phân biệt hình thức sinh sản ở vi sinh vật nhân sơ và nhân thực. Vai trò, cơ sở khoa học và ứng dụng của vi sinh vật; thành tựu và triển vọng công nghệ vi sinh vật.
- **Chương 7. Virus** (8 tiết; SGV tr.140): Khái niệm, đặc điểm, cấu tạo virus. Các giai đoạn nhân lên, từ đó giải thích cơ chế gây bệnh. Thành tựu ứng dụng virus (chế phẩm sinh học, y học, nông nghiệp, thuốc trừ sâu). Phương thức lây truyền một số bệnh do virus (HIV, cúm, sởi...) và cách phòng chống; giải thích vì sao bệnh do virus lây lan nhanh, nhiều biến thể.

**Chuyên đề** (không có SGV Chuyên đề; nguồn là mục "Yêu cầu cần đạt" đầu mỗi bài trong `SCD Sinh hoc 10.pdf`):
- **Chuyên đề 1. Công nghệ tế bào và một số thành tựu:** nguyên lí công nghệ tế bào thực vật, tế bào gốc, công nghệ tế bào động vật và các thành tựu (vi nhân giống, nhân bản vô tính, liệu pháp tế bào gốc, liệu pháp gene).
- **Chuyên đề 2. Công nghệ enzyme và ứng dụng:** khái niệm, cơ sở khoa học của công nghệ enzyme; quy trình sản xuất enzyme (SCD tr.36); ứng dụng trong công nghệ thực phẩm, y dược, kĩ thuật di truyền và triển vọng (SCD tr.44).
- **Chuyên đề 3. Công nghệ vi sinh vật trong xử lí ô nhiễm môi trường:** vai trò của vi sinh vật trong xử lí ô nhiễm (SCD tr.57); ứng dụng phân giải hiếu khí, kị khí, lên men (tr.62); công nghệ xử lí đất, nước thải, khí sinh học, chất thải rắn (tr.66).

**Giới hạn và trọng tâm theo SGV.** Agent sinh câu hỏi lưu ý:
- Công nghệ tế bào (Bài 19): HS chưa học di truyền, nên "chỉ tập trung vào nguyên lí mà không quá chú trọng vào chi tiết" (SGV tr.115). Không ra câu hỏi về cơ chế điều hoà gene trong biệt hoá.
- Nguồn gốc sự sống trên Trái Đất được học ở lớp 12 (SGV tr.36), không ra đề ở lớp 10.
- Tế bào nhân sơ (Bài 7): trọng tâm là mối quan hệ cấu trúc – chức năng (SGV tr.51).

## 5. Sai lầm thường gặp của học sinh

SGV không có mục riêng về lỗi sai. Dưới đây là các sai lầm, điểm dễ nhầm được nêu rõ ("Lưu ý", "GV lưu ý HS", "không chính xác") trong SGV (cột Nguồn: trang PDF của `SGV SINH HOC 10.pdf`, đã đối chiếu ảnh trang 15, 27, 43, 62, 79, 82):

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Biến dị tổ hợp (Bài 17) | Hầu hết HS định nghĩa sai "biến dị tổ hợp là sự tổ hợp lại gene của bố mẹ làm xuất hiện tính trạng mới". Đúng: biến dị tổ hợp là loại biến dị hình thành do sự tổ hợp lại các gene thông qua giảm phân và thụ tinh; biến dị không đồng nghĩa với sự tổ hợp. | SGV tr.15 |
| Tổ chức thứ bậc (Bài 3) | HS cần hiểu vì sao các cấp tổ chức có đặc điểm chung: bậc cao hơn được hình thành từ bậc thấp hơn nên mang đặc điểm chung của đơn vị cấu thành, đồng thời có đặc điểm nổi trội mới. | SGV tr.27 |
| Đặc tính nổi trội (Bài 3) | Nhầm rằng đặc tính nổi trội chỉ có ở thế giới sống. Vật không sống cũng có (ví dụ xe đạp lắp hoàn chỉnh khác hộp linh kiện rời). | SGV tr.27 |
| Liên kết duy trì cấu trúc protein (Bài 5) | Liên kết S – S (disulphide) **không phải** liên kết yếu. Chức năng protein do cấu trúc bậc 2, 3, 4 quy định; phá vỡ liên kết yếu (không cần phá cấu trúc bậc 1) đã làm protein mất chức năng. | SGV tr.43 |
| Hệ thống nội màng (Bài 8) | Hệ thống nội màng gồm lưới nội chất, màng nhân, lysosome, bộ máy Golgi, không bào, cả màng tế bào. **Ti thể và lục lạp không thuộc** hệ thống nội màng. | SGV tr.62, 64 |
| Peroxysome (Bài 8) | Lysosome và không bào có nguồn gốc từ hệ thống màng nội bào, còn peroxysome thì không. | SGV tr.62 |
| Protein vận chuyển (Bài 10) | Các tên gọi khác nhau của protein vận chuyển đều thuộc hai nhóm: protein kênh và protein mang. Vận chuyển thụ động có thể cần hoặc không cần protein vận chuyển; vận chuyển chủ động luôn cần. | SGV tr.82 |
| Truyền tin tế bào (Bài 12) | Phân tử trong chuỗi chuyển đổi tín hiệu sau khi hoạt hoá phân tử kế tiếp sẽ trở về trạng thái bất hoạt ngay. Cùng một hormone (testosteron) có thể gây đáp ứng khác nhau ở các tế bào khác nhau. | SGV tr.79 |
| Quan sát nguyên phân, giảm phân (Bài 18) | Hình các kì dưới kính hiển vi rất khác hình vẽ SGK; ở tiêu bản ép, NST kì giữa có thể không xếp thành hàng, nhận biết qua NST co ngắn cực đại. | SGV tr.114–115 |
| Virus cúm và HIV (Bài 25) | Virus cúm chỉ có chu kì sinh tan, **không** tích hợp vào hệ gene tế bào người như HIV (chu kì tiềm tan). | SGV tr.149 |
| Kháng sinh (Bài 7, 21) | Dùng kháng sinh không đúng liều thì không khỏi bệnh, thậm chí nặng hơn, do vi khuẩn kháng thuốc. | SGV tr.59 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Bốn sách nguồn là PDF dạng ảnh. Định nghĩa được đọc trực tiếp từ ảnh trang (khoảng 105–115 dpi). `check_sources.py` đối chiếu với text OCR (tesseract `vie`), lưu cache ở `.ocr/`. Riêng `SCD Sinh hoc 10/p0076.txt` (bảng thuật ngữ cuối SCD) được OCR lại bằng `--psm 6` vì chế độ mặc định đọc sai bảng hai cột.
- OCR không đọc được công thức, nên phần LaTeX trong `definition` và toàn bộ `notation` **không được kiểm tra tự động**. Phần này dựa vào kiểm tra mẫu.
- Tên của các mục `tinh_chat`, `quy_tac`, `cong_thuc` thường do người trích đặt. Lần chạy gần nhất có 10 mục bị cảnh báo vì tên không có nguyên văn trong trang; nội dung các mục này vẫn đạt (bigram ≥ 0.92).
- Nguồn `gv` (7 mục) và nguồn `sbt` phụ chỉ được kiểm tra sự có mặt của tên thuật ngữ, không kiểm tra bigram (định nghĩa giữ theo SGK).
- Có 1 mục mang `notes`: `sinh-10-polymer` (SGK chỉ nêu ba loại đại phân tử "được gọi là các polymer"; định nghĩa tổng quát lấy từ phần trả lời của SBT).

**Kiểm tra tự động** (2026-10-14, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py sinh_10` | 0 lỗi; 299 thuật ngữ; 268 KB |
| `check_sources.py sinh_10` | 299 đạt, 0 gắn cờ, 0 không kiểm tra được, 10 cảnh báo về tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 7: 4 do OCR không đọc được bảng thuật ngữ SCD (bỏ nguồn trùng, OCR lại trang), 1 do định nghĩa ghép hai đoạn (`enzyme-gioi-han`, đổi thứ tự nguồn), 2 do SGV dùng tên khác (thêm alias). Không mục nào sai nội dung. |
| Kiểm tra trang chính xác (trang nguồn so với hai trang kề) | Phát hiện 8 mục Bài 20 và 1 mục Bài 12 lệch +1 trang (check_sources không bắt được vì xét cả 3 trang). Đã sửa bằng `--update`. Ngoài ra 24 mục Bài 5 lệch +1 trang được phát hiện và sửa trước khi nạp. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-14, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/299 (10%): 20 ngẫu nhiên + 10 mục `cong_thuc`/`dinh_ly`/có `notation` |
| Cách chọn | `query.py sinh_10 --audit` (seed 2026), danh sách ở `sample_audit.md` |
| Đối chiếu ảnh | 11 mục đọc lại ảnh trang nguồn (toàn bộ mục có công thức/kí hiệu + 4 mục văn bản); 19 mục còn lại đã đọc ảnh khi trích và đạt bigram ≥ 0.9 ở đúng trang |
| Số mục sai | 1 (3,3%, dưới ngưỡng 5%): `notation` của `hoa-tong-hop` thiếu chú thích "(chất cho H⁺)" và "Vi sinh vật" trên mũi tên |
| Số mục đã sửa | 1 |
| Kiểm tra độc lập | Người dùng đối chiếu 30 mục với ảnh trang nguồn ở phiên riêng (2026-10-14): 0 sai. Đã xoá `sample_audit.md` |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Sinh học 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Gene, DNA, RNA, nguyên tắc bổ sung (Bài 5) → cơ chế di truyền và biến dị (lớp 12).
- Biến dị tổ hợp, giảm phân (Bài 17) → quy luật di truyền (lớp 12).
- Quang hợp, hô hấp tế bào (Bài 14) → trao đổi chất và chuyển hoá năng lượng ở thực vật, động vật (lớp 11).
- Truyền tin tế bào, hormone (Bài 12) → cảm ứng, điều hoà ở sinh vật (lớp 11).
- Quần thể, quần xã, hệ sinh thái (Bài 3) → sinh thái học (lớp 12).
- Nguồn gốc sự sống (SGV tr.36) → tiến hoá (lớp 12).
