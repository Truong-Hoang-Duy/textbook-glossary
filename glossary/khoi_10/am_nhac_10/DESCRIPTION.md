# Bộ thuật ngữ `am_nhac_10` — Âm nhạc 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_10/am_nhac_10/am_nhac_10.json` (tập trung: `glossary/dataset/am_nhac_10.json`), gồm **116 thuật ngữ** (cập nhật 2026-10-16). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_10/am_nhac_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Am nhac 10.pdf | sgk | 94 | Nguồn chính. Phần một (4 chủ đề, mỗi chủ đề có 5 mạch nội dung), Phần hai: A – Hát (4 bài), B – Nhạc cụ (8 bài, đàn guitar); `level: co_ban` | Không (ảnh, OCR) |
| SCD Am nhac 10.pdf | scd | 58 | Chuyên đề 1–3 (13 bài): hợp âm, xác định giọng và đặt hợp âm đệm, tiết điệu đệm; `level: chuyen_de` | Không (ảnh, OCR) |
| SGV AM NHAC 10.pdf | gv | 119 | Mục tiêu từng chủ đề/bài (mục 4); lưu ý sư phạm (mục 5); nguồn `gv` cho 4 thuật ngữ | Không (ảnh, OCR) |
| SGV CD AM NHAC 10.pdf | gv | 46 | Mục tiêu từng bài của chuyên đề (mục 4) | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Âm nhạc 10.pdf | gv | 54 | Thời lượng, cấu trúc SGK/SCD (mục 4) | Có (đọc trực tiếp) |

- Ở bốn sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- Bộ không có SBT.
- SGK Phần một: `chapter` = `Chủ đề N. …`; `lesson` = mạch nội dung (`Lí thuyết âm nhạc`, `Đọc nhạc`, `Hát`, `Nhạc cụ`, `Nghe nhạc` hoặc `Thưởng thức âm nhạc`; Chủ đề 1 và 3 có mạch Nghe nhạc, Chủ đề 2 và 4 có mạch Thưởng thức âm nhạc). Phần hai: `chapter` = `Phương án lựa chọn A. Hát` / `Phương án lựa chọn B. Nhạc cụ`, `lesson` = `Bài N. …` (A và B đánh số bài riêng, đều bắt đầu từ Bài 1 — luôn lọc kèm `--chapter`). SCD: `chapter` = `Chuyên đề N. …`, `lesson` = `Bài N. …`.
- SGK có mục **Giải thích một số thuật ngữ** (PDF 93, 9 mục) và SCD có mục tương tự (PDF 56, 6 mục). Cả 15 mục đều có trong glossary; nguồn trang bảng đứng đầu (SGK) hoặc đứng sau trang thân bài (SCD, xem mục 6), kèm trang thân bài.
- Mạch **Đọc nhạc, Hát, Nhạc cụ** của Phần một chủ yếu là bài tập, ca khúc, bản nhạc, mẫu luyện — **không có định nghĩa tường minh** nên 0 mục. Phần hai nêu kĩ thuật (tư thế, hơi thở, phát âm, cách bấm gảy guitar), được ghi thành mục `quy_tac`/`dinh_nghia`/`ky_hieu` sát câu chữ SGK; không lấy ví dụ minh hoạ, nốt nhạc, hình thế bấm hợp âm, tiểu sử ca khúc.
- Các mục nội dung tiết điệu ở SGK (Waltz, Fox) và SCD (Waltz, Polka, March, Boston, Ballad, Slow Rock, Disco) được tách theo từng tiết điệu. `tiet-dieu-waltz` (SGK, `co_ban`) giữ câu của SGK; phần mô tả điệu nhảy và tiết tấu Waltz của SCD tách thành `tiet-dieu-waltz-dieu-nhay` (`chuyen_de`) vì `check_sources.py` so khớp toàn bộ `definition` với trang của nguồn đứng đầu.
- Trùng id với bộ khác trong môn: không có (đây là bộ Âm nhạc đầu tiên).

## 2. Chương/bài và số thuật ngữ

SGK (69 mục)

| Chương | Bài / Mạch | Số mục |
|---|---|---|
| Chủ đề 1. Giai điệu quê hương | Lí thuyết âm nhạc (PDF 8–10: quãng) | 7 |
| | Đọc nhạc, Hát, Nhạc cụ, Nghe nhạc | 0 |
| Chủ đề 2. Cuộc sống mến thương | Lí thuyết âm nhạc (PDF 17–19: điệu thức, giọng) | 7 |
| | Thưởng thức âm nhạc (PDF 24–25: giao hưởng) | 3 |
| | Đọc nhạc, Hát, Nhạc cụ | 0 |
| Chủ đề 3. Về miền kí ức | Lí thuyết âm nhạc (PDF 27–28: giọng Son trưởng, Mi thứ) | 3 |
| | Nghe nhạc (PDF 34: vocalise) | 1 |
| | Đọc nhạc, Hát, Nhạc cụ | 0 |
| Chủ đề 4. Giai điệu bốn phương | Lí thuyết âm nhạc (PDF 36–38: hợp âm ba chính) | 2 |
| | Thưởng thức âm nhạc (PDF 43–47: lịch sử âm nhạc phương Tây) | 17 |
| | Đọc nhạc, Hát, Nhạc cụ | 0 |
| Phương án lựa chọn A. Hát | Bài 1. Tư thế hát và miệng hát | 3 |
| | Bài 2. Làm chủ hơi thở | 3 |
| | Bài 3. Phát âm rõ chữ | 4 |
| | Bài 4. Hát giọng chuyển | 2 |
| Phương án lựa chọn B. Nhạc cụ | Bài 1. Giới thiệu đàn guitar và kĩ thuật bấm, gảy trên dây 5, dây 4 | 8 |
| | Bài 2. Kĩ thuật bấm, gảy trên dây 3, dây 2 | 2 |
| | Bài 3. Kĩ thuật bấm, gảy trên dây 6, dây 1 | 2 |
| | Bài 4. Kĩ thuật gảy quãng hoà âm | 1 |
| | Bài 5. Cách đệm tiết điệu Waltz | 2 |
| | Bài 6. Cách đệm tiết điệu Fox | 1 |
| | Bài 7. Hoà tấu tiểu phẩm âm nhạc Việt Nam | 1 |
| | Bài 8. Hoà tấu tiểu phẩm âm nhạc nước ngoài | 0 |

SCD (47 mục)

| Chuyên đề | Bài | Số mục |
|---|---|---|
| Chuyên đề 1. Hệ thống các hợp âm ba, hợp âm bảy của điệu thức | Bài 1. Hợp âm ba, các hợp âm ba chính trong điệu trưởng và điệu thứ | 9 |
| | Bài 2. Các hợp âm ba phụ trong điệu trưởng và điệu thứ | 3 |
| | Bài 3. Hợp âm bảy át | 4 |
| | Bài 4. Hợp âm bảy thứ, bảy trưởng | 4 |
| Chuyên đề 2. Phương pháp xác định giọng và đặt hợp âm đệm cho ca khúc, bản nhạc | Bài 1. Phương pháp xác định giọng cho ca khúc, bản nhạc | 2 |
| | Bài 2. Phương pháp xác định cấu trúc của ca khúc, bản nhạc | 5 |
| | Bài 3. Vòng hợp âm đệm cho ca khúc, bản nhạc | 2 |
| | Bài 4. Phương pháp đặt hợp âm đệm cho ca khúc, bản nhạc | 2 |
| Chuyên đề 3. Phương pháp xác định tiết điệu đệm | Bài 1. Tiết điệu đệm và những tiết điệu phổ biến | 12 |
| | Bài 2. Xác định tiết điệu đệm cho ca khúc, bản nhạc nhịp 2/4 | 1 |
| | Bài 3. Xác định tiết điệu đệm cho ca khúc, bản nhạc nhịp 3/4 | 1 |
| | Bài 4. Xác định tiết điệu đệm cho ca khúc, bản nhạc nhịp 4/4 | 1 |
| | Bài 5. Xác định tiết điệu đệm cho ca khúc, bản nhạc nhịp 6/8 | 1 |

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 77 |
| quy_tac | 25 |
| tinh_chat | 10 |
| ky_hieu | 4 |
| cong_thuc | 0 |
| dinh_ly | 0 |

- Theo `level`: `co_ban` 69, `chuyen_de` 47.
- Theo nguồn định nghĩa (nguồn đứng đầu): SGK 69, SCD 47. 4 mục có thêm nguồn `gv` (`mieng-hat`, `tu-the-ngoi-choi-dan-guitar`, `ban-tay-trai-khi-choi-guitar`, `ban-tay-phai-gay-moc-day`; SGV giải thích thêm về mặt sư phạm, `definition` vẫn theo SGK); 4 mục có nguồn từ hơn một file.
- `ky_hieu` (4): quy ước kí hiệu ngón tay khi chơi guitar, kí hiệu cường độ p và f trên guitar, kí hiệu O/X trong sơ đồ hợp âm guitar.
- `quy_tac` (25): chủ yếu là kĩ thuật hát và chơi guitar (SGK Phần hai) và cách xác định giọng, đặt hợp âm, chọn tiết điệu đệm (SCD). Không có `cong_thuc`, `dinh_ly`: môn không có công thức hay định lí; kí hiệu hợp âm đi kèm ở trường `notation` của từng loại hợp âm.
- 1 mục có `notes`: `hop-am-ba-chinh-trong-giong-hoa-thanh` (câu về giọng trưởng hoà thanh được SCD trình bày dưới nhãn “Ví dụ”).
- Các mục `quy_tac` về chọn tiết điệu đệm (`chon-tiet-dieu-dem-nhip-2-4`, `-3-4`, `-4-4`, `-6-8`) gộp nhiều quy tắc theo nhịp độ/tính chất của cùng một loại nhịp; tên mục do người trích đặt theo tiêu đề bài.

## 4. Yêu cầu cần đạt theo chương

Nguồn: phần “Mục tiêu” (Kiến thức, Năng lực, Phẩm chất) đầu từng mạch/bài của `SGV AM NHAC 10.pdf` và `SGV CD AM NHAC 10.pdf` (trang PDF trong ngoặc). Trích rút gọn.

**SGV Âm nhạc 10 (SGK)**

- **Chủ đề 1 – Lí thuyết** (PDF 11): nhận biết quãng hoà thanh, quãng giai điệu, quãng đơn, quãng diatonic; nhận biết tính chất thuận, nghịch của quãng; thành lập và xác định các quãng trong giai điệu bản nhạc, ca khúc. **Hát** (PDF 17): miệng mở tự nhiên, cơ thể thả lỏng, hát đúng cao độ, trường độ. **Nhạc cụ** (PDF 20): thể hiện đúng cao độ, trường độ bài tập giai điệu, duy trì tốc độ ổn định. **Nghe nhạc** (PDF 22–23): nêu năm ra đời, tác giả, tính chất và chủ đề bài hát *Tiếng hát giữa rừng Pác Bó*.
- **Chủ đề 2 – Lí thuyết** (PDF 25): trình bày khái niệm điệu thức, gam, kí hiệu các bậc, các loại điệu thức phổ biến nhất; khái niệm giọng, tính chất giọng trưởng và giọng thứ. **Hát** (PDF 31): thả lỏng miệng và các cơ khi hát. **Thưởng thức** (PDF 37): nêu đặc điểm thể loại giao hưởng, kể tên nhạc cụ trong mỗi bộ của dàn nhạc giao hưởng, nhận biết bản *Đồng quê* qua câu chủ đề.
- **Chủ đề 3 – Lí thuyết** (PDF 40): nhận biết bản nhạc viết ở giọng Son trưởng và Mi thứ, vận dụng vào tìm hiểu bản nhạc, học hát, chơi nhạc cụ, đọc nhạc. **Đọc nhạc** (PDF 42): đọc đúng cao độ gam Mi thứ và Bài đọc nhạc số 3. **Hát** (PDF 45), **Nhạc cụ** (PDF 48), **Nghe nhạc** (PDF 51): hát ca khúc hoạt bát với âm thanh đều đặn; cảm nhận sự hoà quyện của nhạc cụ giai điệu, nhạc cụ gõ và giọng hát; chia sẻ cảm xúc khi nghe bài *Trở về dòng sông tuổi thơ*.
- **Chủ đề 4 – Lí thuyết** (PDF 54): nhận biết một số hợp âm của giọng Son trưởng và Mi thứ; dùng các hợp âm ba chính để đặt hợp âm đệm cho bản nhạc đơn giản; biết cách ghi chép bản nhạc. Hoạt động Vận dụng sáng tạo của mạch Lí thuyết (PDF 56): đặt được hợp âm ba chính cho Bài đọc nhạc số 1 và số 4. **Thưởng thức** (PDF 66): nêu vài nét các giai đoạn lịch sử âm nhạc thế giới, kể tên nhạc sĩ tiêu biểu từng giai đoạn, hệ thống các thời kì lịch sử âm nhạc phương Tây.
- **Phương án A – Hát**: Bài 1 (PDF 69) biết đứng, ngồi hát đúng tư thế, mở miệng phù hợp; Bài 2 (PDF 72) nhận biết cách lấy hơi, giữ hơi, đẩy hơi khi hát; Bài 3 (PDF 75) phân tích và vận dụng cách phát âm rõ chữ; Bài 4 (PDF 79) nhận biết cách chuyển giọng hát giữa các âm khu, hát chuyển giọng từ âm thấp lên âm cao và ngược lại.
- **Phương án B – Nhạc cụ (guitar)**: Bài 1 (PDF 82) nắm kiến thức cơ bản về đàn guitar (tư thế ngồi, quy ước hai bàn tay), làm quen thế tay thứ nhất trên dây 5, dây 4; Bài 2 (PDF 87) bảo quản đàn, điều chỉnh âm thanh, thể hiện thế tay thứ nhất trên dây 3, dây 2, ứng tác, biến tấu đơn giản; Bài 3 (PDF 92) thể hiện đúng cao độ, trường độ, sắc thái, điều chỉnh cường độ trên dây 6, dây 1; Bài 4 (PDF 95) gảy được quãng hoà âm; Bài 5 (PDF 99) nắm âm hình cơ bản tiết điệu Waltz, đặt hợp âm ba chính cho bài hát; Bài 6 (PDF 102) tương tự với tiết điệu Fox ở giọng Mi thứ; Bài 7 (PDF 106) và Bài 8 (PDF 113) biết chơi nhạc cụ dưới hình thức hoà tấu, điều chỉnh cường độ để tạo sự hài hoà, dàn dựng và biểu diễn.

**SGV CD Âm nhạc 10 (SCD)**

- **Chuyên đề 1** – Bài 1 (PDF 10): trình bày cấu tạo cơ bản, cấu tạo, tính chất, kí hiệu của hợp âm ba; vị trí, tính chất, kí hiệu hợp âm ba chính trong điệu trưởng và điệu thứ; biết xây dựng và thực hành trên nhạc cụ. Bài 2 (PDF 13): vị trí, cấu tạo, tính chất hợp âm ba phụ; phân biệt sự ổn định và không ổn định của các hợp âm ba (chính, phụ). Bài 3 (PDF 16): vị trí, cấu tạo, tính chất, kí hiệu và cách xây dựng hợp âm bảy át. Bài 4 (PDF 18): vị trí, cấu tạo, tính chất, kí hiệu hợp âm bảy thứ và bảy trưởng.
- **Chuyên đề 2** – Bài 1 (PDF 22): khái niệm xác định giọng và phương pháp xác định giọng. Bài 2 (PDF 24): khái niệm và cấu trúc của câu nhạc, đoạn nhạc; phân tích cấu trúc và tính chất âm nhạc. Bài 3 (PDF 27): khái niệm vòng hợp âm, một số vòng hợp âm đệm phổ biến. Bài 4 (PDF 29): các bước đặt hợp âm cho ca khúc, bản nhạc.
- **Chuyên đề 3** – Bài 1 (PDF 32): khái niệm tiết điệu, tiết điệu đệm, các yếu tố tạo nên tiết điệu đệm, tiết tấu đặc trưng và tính chất của các tiết điệu phổ biến. Bài 2–5 (PDF 34, 37, 39, 42): nắm các loại nhịp độ và tính chất âm nhạc của ca khúc, bản nhạc nhịp 2/4, 3/4, 4/4, 6/8, từ đó chọn tiết điệu đệm phù hợp và đệm trên nhạc cụ.

**Tài liệu bồi dưỡng GV** (PDF 5): SGK Âm nhạc 10 có 70 tiết (7 tiết kiểm tra, đánh giá): Phần Kiến thức chung 28 tiết (4 chủ đề), Phương án lựa chọn 35 tiết (hát hoặc guitar). SCD gồm 35 tiết, mở rộng và nâng cao so với Phương án; có thể bắt đầu học SCD khi đã học 1–2 chủ đề ở Kiến thức chung.

## 5. Sai lầm thường gặp của học sinh

SGV Âm nhạc 10, SGV CD và Tài liệu bồi dưỡng GV **không có mục “sai lầm thường gặp của học sinh”**. Dưới đây là các lưu ý sư phạm của SGV nhằm tránh lỗi HS dễ mắc (trích rút gọn, kèm trang PDF):

| Nội dung | Lưu ý của SGV | Nguồn |
|---|---|---|
| Chơi guitar – tay phải | Không tì ngón tay hoặc cổ tay lên mặt đàn, không tì ngón tay lên dây đàn (làm chậm tốc độ, gây nhầm dây gảy, giảm độ ngân); không để ngón tay vào dây quá sâu (phát ra tạp âm); ngón vừa gảy không tì vào dây bên cạnh (vô tình thành kĩ thuật gảy ép dây) | SGV PDF 91 |
| Chơi guitar – tay trái | Bấm vuông góc với phím đàn, không bấm ở đầu phím (tốn lực) mà bấm gần miếng kim loại ngăn phím để âm rõ, tròn, không tạp âm | SGV PDF 84 |
| Chơi guitar – cổ tay | Giữ yên cổ tay, chỉ dùng lực từ các khớp ngón tay; có thể để cổ tay hơi cong lên, cách mặt đàn khoảng 3–5 cm | SGV PDF 84 |
| Chọn đàn | Nên dùng guitar classic (dây nilon) vì dễ bấm hơn dây kim loại | SGV PDF 83 |
| Hát – miệng, cơ thể | Nhắc HS thường xuyên mở miệng rộng, thả lỏng môi, lưỡi, hàm ếch mềm, cằm và cơ thể | SGV PDF 61, 71 |
| Hát – lấy hơi | Chỉ lấy hơi ở chỗ ngắt ý, ngắt câu | SGV PDF 74 |
| Đọc nhạc – luyện quãng 2 | Mẫu luyện đọc quãng hai chỉ là cách đọc khác của gam Son trưởng, nhằm giờ học sinh động (không phải khái niệm mới) | SGV PDF 14 |
| Luyện tiết tấu | HS cần cảm nhận sự chuyển động luân phiên giữa phách mạnh và phách yếu | SGV PDF 15, 21 |
| Đặt hợp âm | Chỉ đặt hợp âm ba chính cho những âm ở đầu phách của nhịp và chọn hợp âm phù hợp với giai điệu | SGV PDF 56 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Bốn sách nguồn là PDF dạng ảnh. Định nghĩa đọc từ ảnh trang (90–100 dpi) đối chiếu OCR (tesseract `vie`, 300 dpi, cache ở `.ocr/`). OCR bản nhạc và sơ đồ hợp âm rất nhiễu; chỉ phần chữ dùng được.
- Bổ sung cache OCR (nối thêm OCR 400 dpi vùng cắt): SCD PDF 56 (cột tên và cột giải thích của bảng thuật ngữ), SGK PDF 68 (danh sách thứ tự dây buông), SGK PDF 77 (chú thích dấu O/X). Nếu xoá `.ocr/`, `check_sources.py` có thể gắn cờ lại các mục này.
- Số trang ở cột “Trang” của hai bảng Giải thích thuật ngữ là trang in của thân bài; ở SCD có mục lệch với thân bài (ví dụ Hợp âm ba chính, Hợp âm bảy ghi “5” nhưng nội dung ở trang in 8 và 14; Hợp âm ba phụ ghi “10”, thân bài ở trang in 11). Glossary dùng trang thân bài thực tế.
- SGK viết “bộ gỗ” (nhóm kèn gỗ: flute, oboe,…) và “bộ gõ” (timpani,…) trong định nghĩa dàn nhạc giao hưởng; giữ nguyên văn.
- SGK Phần một có định nghĩa tường minh chỉ ở mạch Lí thuyết âm nhạc, Thưởng thức/Nghe nhạc và bảng thuật ngữ; các mạch khác 0 mục.
- Mục `tinh_chat`/`quy_tac`/`ky_hieu` có tên do người trích đặt; 18 cảnh báo tên (tên không có nguyên văn trong trang) — nội dung đều đạt bigram ≥ 0.65.
- `check_sources.py` so khớp trong cửa sổ 3 trang, nên không phát hiện lệch trang 1 đơn vị. Trang nguồn được ghi theo ảnh trang khi đọc.
- Các mục lịch sử âm nhạc phương Tây (SGK PDF 43–46) được rút gọn từ đoạn mô tả từng thời kì; bỏ tên nhạc sĩ tiêu biểu và hình minh hoạ.

**Kiểm tra tự động** (2026-10-16, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py am_nhac_10` | 0 lỗi; 116 thuật ngữ |
| `check_sources.py am_nhac_10` | 116 đạt, 0 gắn cờ, 0 không kiểm tra được, 18 cảnh báo tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 7 mục. 3 do OCR bảng tra cứu SCD PDF 56 tách dòng/bỏ sót tên (`hop-am-ba-phu`, `cau-nhac`, `doan-nhac`: bổ sung OCR vùng cắt 400 dpi và đặt trang thân bài đứng đầu `sources`); 1 do định nghĩa gộp câu SGK và SCD (`tiet-dieu-waltz`: tách thành hai mục); 2 do OCR sơ đồ guitar (`thu-tu-cac-day-buong-dan-guitar`, `ky-hieu-so-do-hop-am-guitar`: bổ sung OCR vùng cắt); 1 do tên không khớp tiêu đề thân bài (`truong-phai-tien-phong`: thêm alias `Trường phái Tiền phong`). |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-16, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 37/116 (31,9%) |
| Cách chọn | `query.py am_nhac_10 --audit --sample 30` (seed 2026: 30 mục ngẫu nhiên + 7 mục kí hiệu; bộ không có `cong_thuc`). Danh sách ở `sample_audit.md`. |
| Đối chiếu ảnh | Mở lại ảnh: SGK PDF 9, 18, 27, 28, 43, 44, 45, 49, 68, 69, 73, 75, 77; SCD PDF 7, 8, 9, 12, 15, 19, 21, 27, 30, 31, 32, 34, 38, 40, 56; SGV PDF 84. |
| Số mục sai | **0/37** |
| Kiểm tra độc lập | Đã hoàn thành (người dùng kiểm tra độc lập qua `sample_audit.md`: 37/37 mục đúng, 0 sai). File `sample_audit.md` đã xóa sau kiểm định. |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Âm nhạc 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Quãng, điệu thức, giọng, hợp âm ba chính (SGK Chủ đề 1–4) và hợp âm ba, hợp âm bảy, xác định giọng, đặt hợp âm đệm, tiết điệu đệm (SCD) → lí thuyết âm nhạc và chuyên đề ở lớp 11, 12.
- Kĩ thuật hát (Phương án A) và kĩ thuật guitar (Phương án B) → các bài hát, bài hoà tấu nâng cao ở lớp sau.
- Liên môn: lịch sử âm nhạc phương Tây ↔ `lich_su_10`; dàn nhạc, tiết tấu ↔ `ngu_van_10` (thơ, ca từ).
