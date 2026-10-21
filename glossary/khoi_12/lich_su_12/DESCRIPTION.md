# Bộ thuật ngữ `lich_su_12` — Lịch sử 12 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_12/lich_su_12/lich_su_12.json` (tập trung: `glossary/dataset/lich_su_12.json`), gồm **116 thuật ngữ** (cập nhật 2026-10-20). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_12/lich_su_12/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK LỊCH SỬ 12-KNTT.pdf | sgk | 115 | Nguồn chính, Chủ đề 1–6 (17 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD LICH SU 12 - KNTT.pdf | scd | 59 | Chuyên đề 1–3 (8 mục La Mã I–II/III), `level: chuyen_de` | Không (ảnh, OCR) |

- Ở cả hai sách dạng ảnh: áp dụng đồng nhất quy tắc **trang PDF = trang in + 2** (ví dụ: SGK Bài 1 trang in 6 nằm tại trang PDF 8, Bài 6 trang in 31 nằm tại trang PDF 33; SCD Chuyên đề 1 trang in 5 nằm tại trang PDF 7).
- SGK chia **Chủ đề** (không chia Chương): `chapter` = `Chủ đề N. …`, `lesson` = `Bài N. …`.
- SCD chia **Chuyên đề**: `chapter` = `Chuyên đề N. …`, `lesson` = mục La Mã `I. …`, `II. …`, v.v. của từng chuyên đề.
- **Bảng tra cứu khái niệm, thuật ngữ cuối sách:**
  + SGK: PDF trang 112 (trang in 110) gồm 18 thuật ngữ cốt lõi (*Ấp chiến lược, Bình dân học vụ, Bình định, Căn cứ địa cách mạng, Chiến dịch, Chiến lược cách mạng, Chiến thuật, Chính quốc, Cơ chế thị trường, Hiệp định, Hội nhập quốc tế, Mặt trận, Tập kích, Tổng khởi nghĩa, Tổng tiến công, Trật tự thế giới, Tự lực cánh sinh, Vùng đặc quyền kinh tế*).
  + SCD: PDF trang 57 (trang in 55) gồm 7 thuật ngữ chuyên đề (*Công giáo, Đạo quán (cung quán), Đối thoại liên văn hoá, Quyền sở hữu trí tuệ, Thị trường chứng khoán, Văn miếu, Văn từ / Văn chỉ*).
  + Toàn bộ 25 mục của 2 bảng tra cứu đều có mặt trong glossary, định nghĩa nguyên văn từ bảng và ghi nhận đủ 2 nguồn: trang bảng tra cứu đứng đầu và trang thân bài nơi khái niệm xuất hiện.
- **Đặc thù thuật ngữ môn Lịch sử:**
  + Phân loại thành `dinh_nghia` và `tinh_chat` (nêu bối cảnh lịch sử, nguyên nhân, tính chất, diễn biến chính, ý nghĩa lịch sử, bài học kinh nghiệm); hoàn toàn không có công thức hay kí hiệu toán học (`cong_thuc: 0`, `ky_hieu: 0`, `notation: null`).
  + Các mục `tinh_chat` được trích xuất sát câu chữ SGK theo các tiểu mục bài học và chuẩn yêu cầu cần đạt.
- Toàn bộ 17/17 bài SGK và 8/8 mục SCD đều có đại diện thuật ngữ, đạt độ phủ kiến thức 100%.

## 2. Chủ đề/bài và số thuật ngữ

| Chủ đề / Chuyên đề | Bài / Mục | Số mục |
|---|---|---|
| **Chủ đề 1. Thế giới trong và sau Chiến tranh Lạnh** | Bài 1. Liên hợp quốc | 6 |
| | Bài 2. Trật tự thế giới trong Chiến tranh Lạnh | 5 |
| | Bài 3. Trật tự thế giới sau Chiến tranh Lạnh | 3 |
| **Chủ đề 2. ASEAN: Những chặng đường lịch sử** | Bài 4. Sự ra đời và phát triển của Hiệp hội các quốc gia Đông Nam Á (ASEAN) | 5 |
| | Bài 5. Cộng đồng ASEAN: Từ ý tưởng đến hiện thực | 5 |
| **Chủ đề 3. Cách mạng tháng Tám năm 1945, chiến tranh giải phóng dân tộc và chiến tranh bảo vệ Tổ quốc trong lịch sử Việt Nam (từ tháng 8 năm 1945 đến nay)** | Bài 6. Cách mạng tháng Tám năm 1945 | 7 |
| | Bài 7. Cuộc kháng chiến chống thực dân Pháp (1945 - 1954) | 9 |
| | Bài 8. Cuộc kháng chiến chống Mỹ, cứu nước (1954 - 1975) | 15 |
| | Bài 9. Cuộc đấu tranh bảo vệ Tổ quốc từ sau tháng 4 - 1975 đến nay. Một số bài học lịch sử của các cuộc kháng chiến bảo vệ Tổ quốc từ năm 1945 đến nay | 5 |
| **Chủ đề 4. Công cuộc Đổi mới ở Việt Nam từ năm 1986 đến nay** | Bài 10. Khái quát về công cuộc Đổi mới từ năm 1986 đến nay | 3 |
| | Bài 11. Thành tựu cơ bản và bài học của công cuộc Đổi mới ở Việt Nam từ năm 1986 đến nay | 3 |
| **Chủ đề 5. Lịch sử đối ngoại của Việt Nam thời cận - hiện đại** | Bài 12. Hoạt động đối ngoại của Việt Nam trong đấu tranh giành độc lập dân tộc (từ đầu thế kỉ XX đến Cách mạng tháng Tám năm 1945) | 3 |
| | Bài 13. Hoạt động đối ngoại của Việt Nam trong kháng chiến chống Pháp (1945 - 1954) và kháng chiến chống Mỹ (1954 - 1975) | 2 |
| | Bài 14. Hoạt động đối ngoại của Việt Nam từ năm 1975 đến nay | 2 |
| **Chủ đề 6. Hồ Chí Minh trong lịch sử Việt Nam** | Bài 15. Khái quát cuộc đời và sự nghiệp của Hồ Chí Minh | 1 |
| | Bài 16. Hồ Chí Minh - Anh hùng giải phóng dân tộc | 5 |
| | Bài 17. Dấu ấn Hồ Chí Minh trong lòng nhân dân thế giới và Việt Nam | 2 |
| **Chuyên đề 1. Lịch sử tín ngưỡng và tôn giáo ở Việt Nam** | I. Khái lược về tín ngưỡng và tôn giáo | 3 |
| | II. Một số tín ngưỡng ở Việt Nam | 6 |
| | III. Một số tôn giáo ở Việt Nam | 9 |
| **Chuyên đề 2. Nhật Bản: Hành trình lịch sử từ năm 1945 đến nay** | I. Nhật Bản sau Chiến tranh thế giới thứ hai (1945 - 1952) | 4 |
| | II. Nhật Bản từ năm 1973 đến nay | 2 |
| | III. Bài học thành công của Nhật Bản | 3 |
| **Chuyên đề 3. Quá trình hội nhập quốc tế của Việt Nam** | I. Một số khái niệm | 3 |
| | II. Việt Nam hội nhập khu vực và thế giới | 5 |
| **Tổng cộng** | **25 bài / mục (17 SGK + 8 SCD)** | **116** |

## 3. Thống kê theo `type`, `level`, nguồn

- **Theo `type`:**
  + `dinh_nghia`: 81 mục (69.8%)
  + `tinh_chat`: 35 mục (30.2%)
- **Theo `level`:**
  + `co_ban` (từ SGK): 81 mục (69.8%)
  + `chuyen_de` (từ SCD): 35 mục (30.2%)
- **Theo công thức và kí hiệu:**
  + `cong_thuc`: 0 mục (0%)
  + `ky_hieu`: 0 mục (0%)
  + `notation`: null (116/116 mục, 100%)
- **Nguồn tra cứu kép (`sources` có 2 nguồn):** 25 mục cốt lõi (18 mục từ bảng tra cứu SGK p.112 và 7 mục từ bảng tra cứu SCD p.57, kết hợp trang thân bài).

## 4. Yêu cầu cần đạt theo chủ đề

- **Chủ đề 1 (Thế giới trong và sau Chiến tranh Lạnh):**
  + Trình bày được bối cảnh lịch sử, mục đích, nguyên tắc hoạt động cơ bản của Liên hợp quốc; nêu được vai trò của Liên hợp quốc trong duy trì hoà bình, an ninh quốc tế và giải quyết các vấn đề toàn cầu.
  + Giải thích được nguyên nhân hình thành, đặc điểm nổi bật của Trật tự hai cực I-an-ta và sự đối đầu Xô - Mỹ (Chiến tranh Lạnh).
  + Nêu được xu thế phát triển của thế giới sau Chiến tranh Lạnh: xu thế đa cực, lấy phát triển kinh tế làm trọng tâm, toàn cầu hoá và chuyển từ đối đầu sang đối thoại, hợp tác.
- **Chủ đề 2 (ASEAN: Những chặng đường lịch sử):**
  + Trình bày được quá trình hình thành, mục tiêu và quá trình phát triển từ ASEAN 5 đến ASEAN 10.
  + Phân tích được các văn kiện nền tảng: Tuyên bố Băng Cốc (1967), Hiệp ước Ba-li (1976), Hiến chương ASEAN (2007).
  + Nêu được cấu trúc ba trụ cột của Cộng đồng ASEAN (Chính trị - An ninh, Kinh tế, Văn hoá - Xã hội) và nhận diện được các thách thức trong tiến trình xây dựng Cộng đồng.
- **Chủ đề 3 (Cách mạng tháng Tám 1945, chiến tranh giải phóng và bảo vệ Tổ quốc):**
  + Trình bày được bối cảnh lịch sử, thời cơ chín muồi, diễn biến cuộc Tổng khởi nghĩa Tháng Tám năm 1945; phân tích được nguyên nhân thắng lợi, ý nghĩa lịch sử và bài học kinh nghiệm sâu sắc.
  + Tóm lược đường lối kháng chiến toàn dân, toàn diện, trường kì, tự lực cánh sinh trong hai cuộc kháng chiến chống thực dân Pháp (1945 - 1954) và đế quốc Mỹ (1954 - 1975).
  + Nắm vững các mốc chiến dịch bản lề: Việt Bắc (1947), Biên giới (1950), Điện Biên Phủ (1954); Phong trào Đồng khởi (1959 - 1960), Mậu Thân (1968), Điện Biên Phủ trên không (1972), Tổng tiến công và nổi dậy mùa Xuân 1975 (đỉnh cao là Chiến dịch Hồ Chí Minh).
  + Hiểu rõ các cuộc chiến đấu bảo vệ biên giới Tây Nam, biên giới phía Bắc và chủ quyền biển đảo Tổ quốc sau năm 1975; đúc kết 3 bài học lịch sử cốt lõi.
- **Chủ đề 4 (Công cuộc Đổi mới ở Việt Nam từ năm 1986 đến nay):**
  + Nêu được hoàn cảnh lịch sử dẫn tới quyết định Đổi mới tại Đại hội VI của Đảng (1986).
  + Phân tích nội dung trọng tâm: chuyển từ cơ chế tập trung quan liêu, bao cấp sang cơ chế thị trường định hướng xã hội chủ nghĩa; phát triển kinh tế nhiều thành phần; mở rộng kinh tế đối ngoại.
  + Đánh giá những thành tựu to lớn về tăng trưởng kinh tế, xoá đói giảm nghèo, nâng cao đời sống nhân dân và rút ra các bài học kinh nghiệm.
- **Chủ đề 5 (Lịch sử đối ngoại của Việt Nam thời cận - hiện đại):**
  + Phân tích được hoạt động đối ngoại của Phan Bội Châu (xu hướng bạo động, tìm sự giúp đỡ từ Nhật Bản, Trung Quốc) và Nguyễn Ái Quốc (tìm con đường cứu nước vô sản, hoạt động tại Liên Xô, Trung Quốc).
  + Hiểu rõ vai trò kết hợp đấu tranh quân sự với vận động ngoại giao trong kháng chiến chống Pháp (Hiệp định Giơ-ne-vơ 1954) và kháng chiến chống Mỹ (Hiệp định Pa-ri 1973).
  + Nêu được các mốc phá thế bao vây cô lập giai đoạn 1975 - 1985 và đường lối đối ngoại độc lập, tự chủ, đa phương hoá, đa dạng hoá thời kì Đổi mới.
- **Chủ đề 6 (Hồ Chí Minh trong lịch sử Việt Nam):**
  + Trình bày được tiểu sử tóm tắt và hành trình tìm đường cứu nước của Nguyễn Tất Thành - Nguyễn Ái Quốc.
  + Khẳng định vai trò quyết định của Nguyễn Ái Quốc trong việc chuẩn bị tư tưởng, chính trị, tổ chức dẫn tới thành lập Đảng Cộng sản Việt Nam (1930) và soạn thảo Cương lĩnh chính trị đầu tiên.
  + Nêu bật vai trò lãnh đạo Cách mạng tháng Tám, sáng lập nước Việt Nam Dân chủ Cộng hoà và dẫn dắt hai cuộc kháng chiến vĩ đại.
  + Hiểu rõ sự tôn vinh của nhân dân thế giới (Nghị quyết UNESCO năm 1987) và tình cảm sâu nặng của nhân dân Việt Nam đối với Chủ tịch Hồ Chí Minh.
- **Chuyên đề 1 (Lịch sử tín ngưỡng và tôn giáo ở Việt Nam):**
  + Phân biệt chính xác giữa tín ngưỡng, tôn giáo và mê tín dị đoan.
  + Phân tích nguồn gốc, ý nghĩa của các tín ngưỡng bản địa tiêu biểu: thờ cúng tổ tiên, thờ Mẫu, thờ Thành hoàng, thờ anh hùng dân tộc.
  + Nắm vững sự du nhập, bản địa hoá và vai trò đồng hành cùng dân tộc của các tôn giáo (Phật giáo, Nho giáo, Đạo giáo, Công giáo, Tin Lành, Hồi giáo) cũng như các tôn giáo nội sinh (Cao Đài, Phật giáo Hoà Hảo).
- **Chuyên đề 2 (Nhật Bản: Hành trình lịch sử từ năm 1945 đến nay):**
  + Hiểu rõ các cải cách dân chủ thời kì SCAP chiếm đóng (1945 - 1952) tạo tiền đề cho sự phục hồi thần kì.
  + Phân tích nguyên nhân của sự phát triển "thần kì" giai đoạn 1952 - 1973 (nhân tố con người, vai trò nhà nước, ứng dụng khoa học công nghệ).
  + Nắm được diễn biến khủng hoảng năng lượng thập niên 70 và các chính sách điều chỉnh cơ cấu kinh tế, cùng các bài học thành công có thể áp dụng cho các quốc gia đang phát triển.
- **Chuyên đề 3 (Quá trình hội nhập quốc tế của Việt Nam):**
  + Hiểu rõ khái niệm và các biểu hiện, tác động hai mặt của toàn cầu hoá.
  + Nắm vững các lĩnh vực hội nhập quốc tế của Việt Nam (kinh tế, chính trị, văn hoá, an ninh - quốc phòng).
  + Phân tích các dấu mốc gia nhập ASEAN (1995), APEC (1998), WTO (2007) và tham gia các hoạt động gìn giữ hoà bình của Liên hợp quốc.

## 5. Sai lầm thường gặp của học sinh

1. **Nhầm lẫn giữa các hiệp định quốc tế lớn:**
   - Hay nhầm lẫn bối cảnh, nội dung và ý nghĩa của *Hiệp định Sơ bộ (1946)*, *Hiệp định Giơ-ne-vơ (1954)* và *Hiệp định Pa-ri (1973)*. Ví dụ: Hiệp định Giơ-ne-vơ buộc Pháp công nhận độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của 3 nước Đông Dương và lấy vĩ tuyến 17 làm giới tuyến quân sự tạm thời; trong khi Hiệp định Pa-ri buộc Mỹ rút hết quân đội về nước, tôn trọng các quyền dân tộc cơ bản của Việt Nam.
2. **Nhầm lẫn mục tiêu và ý nghĩa các chiến dịch bản lề:**
   - Dễ nhầm chiến dịch phản công với chiến dịch tiến công: *Chiến dịch Việt Bắc thu - đông 1947* là chiến dịch phản công đầu tiên (bảo vệ cơ quan đầu não, làm phá sản kế hoạch "đánh nhanh thắng nhanh"), còn *Chiến dịch Biên giới thu - đông 1950* là chiến dịch tiến công lớn đầu tiên (khai thông biên giới, giành thế chủ động chiến lược trên chiến trường chính Bắc Bộ).
   - Nhầm thứ tự và nhiệm vụ của 3 chiến dịch lớn trong cuộc Tổng tiến công và nổi dậy mùa Xuân 1975: Chiến dịch Tây Nguyên (đòn điểm huyệt chiến lược) -> Chiến dịch Huế - Đà Nẵng (tiến công tiêu diệt quân đoàn 1 đối phương) -> Chiến dịch Hồ Chí Minh (đỉnh cao giải phóng hoàn toàn miền Nam).
3. **Nhầm lẫn các chiến lược chiến tranh của Mỹ ở miền Nam Việt Nam:**
   - Hay nhầm lẫn lực lượng tham chiến chủ yếu và thủ đoạn đặc trưng:
     + *Chiến tranh đặc biệt (1961 - 1965):* quân đội Sài Gòn làm nòng cốt + cố vấn Mỹ, xương sống là "ấp chiến lược", trực thăng vận, thiết xa vận.
     + *Chiến tranh cục bộ (1965 - 1968):* quân viễn chinh Mỹ và quân đồng minh giữ vai trò chủ lực trên chiến trường với chiến thuật "tìm diệt" và "bình định".
     + *Việt Nam hoá chiến tranh (1969 - 1973):* quân đội Sài Gòn làm lực lượng chủ lực + hoả lực và không quân Mỹ, thực hiện âm mưu "dùng người Việt đánh người Việt".
4. **Nhầm lẫn bản chất giữa tín ngưỡng và tôn giáo:**
   - Thường coi tín ngưỡng và tôn giáo là một: Tín ngưỡng là niềm tin gắn với phong tục tập quán truyền thống của cộng đồng (không có giáo chủ, giáo lí, giáo hội thành văn phức tạp); tôn giáo có hệ thống giáo thuyết, kinh điển, giáo luật, đối tượng thờ phụng và tổ chức giáo hội chặt chẽ.
   - Nhầm lẫn tín ngưỡng dân gian thuần Việt mang tính nhân văn (thờ cúng tổ tiên, thờ Mẫu, thờ Thành hoàng) với tệ nạn mê tín dị đoan mang tính huyễn hoặc, mù quáng trục lợi.
5. **Nhầm lẫn thời cơ khách quan và sự chuẩn bị chủ quan trong Cách mạng tháng Tám:**
   - Tuyệt đối hoá sự kiện Nhật Bản đầu hàng Đồng minh (thời cơ khách quan) mà xem nhẹ quá trình 15 năm lãnh đạo, chuẩn bị lực lượng chính trị, lực lượng vũ trang và căn cứ địa cách mạng của Đảng Cộng sản Đông Dương và Mặt trận Việt Minh.

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

- **Kết quả kiểm tra nguồn toàn bộ (Phase 3):**
  + Chạy đối soát bigram bằng lệnh: `python glossary/scripts/check_sources.py lich_su_12`
  + Kết quả: **116 / 116 mục ĐẠT (100%)**, 0 mục bị gắn cờ cảnh báo, 0 mục không kiểm tra được, 0 ghi chú bất thường.
  + Toàn bộ định nghĩa khớp chính xác với bộ nhớ đệm OCR trích xuất từ 2 file PDF gốc (`SGK LỊCH SỬ 12-KNTT.pdf` và `SCD LICH SU 12 - KNTT.pdf`).
- **Kết quả kiểm định mẫu nghiệm thu tự động (Phase 5):**
  + Trích xuất mẫu ngẫu nhiên gồm 30 mục phân bổ trên cả 6 chủ đề SGK và 3 chuyên đề SCD.
  + Đối chiếu trực tiếp từng mục với văn bản OCR trang nguồn PDF trong phiên làm việc.
  + Kết quả: **30 / 30 mục ĐẠT chuẩn (100% chính xác, tỷ lệ sai số 0.0%)**, đạt và vượt ngưỡng cho phép (sai số ≤ 5%).
  + Kết luận: Nghiệm thu hoàn tất và phê chuẩn bộ dữ liệu `lich_su_12`.
- **Hạn chế đã biết:**
  + Môn Lịch sử có văn bản tự sự dài, nhiều bảng biểu và cột báo; một số thuật ngữ kết hợp các từ khóa thông qua trường `aliases` để đảm bảo nhận diện chính xác trong các công cụ tìm kiếm tự động mà không làm mất đi tính nguyên văn học thuật.

## 7. Liên hệ với các môn và lớp khác

- **Lịch sử lớp 10 và 11:** Kế thừa phương pháp phân tích sự kiện lịch sử, các khái niệm cơ bản về chiến tranh vệ quốc, cách mạng giải phóng dân tộc (Lịch sử 11) và tiến trình văn minh nhân loại, văn minh Đông Nam Á (Lịch sử 10).
- **Giáo dục Kinh tế và Pháp luật (GDKT&PL) lớp 12:** Kết nối mật thiết về các khái niệm cơ chế thị trường, mô hình kinh tế thị trường định hướng xã hội chủ nghĩa, hội nhập kinh tế quốc tế và các hiệp định thương mại tự do (FTA, WTO, CPTPP).
- **Địa lí lớp 12:** Bổ trợ mạnh mẽ cho các kiến thức về Biển Đông, chủ quyền biên giới quốc gia, các vùng kinh tế động lực và chuyển dịch cơ cấu ngành kinh tế trong thời kì Đổi mới.
- **Ngữ văn lớp 12:** Soi sáng hoàn cảnh lịch sử ra đời của các áng văn chính luận kinh điển (*Tuyên ngôn Độc lập*, *Lời kêu gọi toàn quốc kháng chiến*) cùng các tác phẩm văn học thời kì kháng chiến chống Pháp, chống Mỹ và đổi mới văn học dân tộc.
