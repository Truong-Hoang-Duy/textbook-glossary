# Bộ thuật ngữ `lich_su_10` — Lịch sử 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_10/lich_su_10/lich_su_10.json` (tập trung: `glossary/dataset/lich_su_10.json`), gồm **261 thuật ngữ** (cập nhật 2026-10-16). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_10/lich_su_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Lich su 10.pdf | sgk | 150 | Nguồn chính, Chủ đề 1–7 (14 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD Lich su 10.pdf | scd | 66 | Chuyên đề 1–3, mỗi chuyên đề chia mục I–III, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV LICH SU 10.pdf | gv | 206 | Mục tiêu, lưu ý từng bài (mục 4–5); nguồn `gv` cho 12 thuật ngữ | Không (ảnh, OCR) |
| SGV CD LICH SU 10.pdf | gv | 74 | Mục tiêu, lưu ý từng chuyên đề (mục 4–5); nguồn `gv` cho 6 thuật ngữ | Không (ảnh, OCR) |
| SBT LICH SU 10.pdf | sbt | 122 | Câu hỏi, bài tập (PDF 6–94), đáp án (PDF 95–121); bổ sung 1 khái niệm SGK chưa định nghĩa (`bao-vat-quoc-gia`) | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Lịch sử 10.pdf | gv | 41 | Cấu trúc SGK/SCD, điểm mới, kế hoạch dạy chuyên đề (mục 4) | Có (đọc trực tiếp) |

- Ở năm sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- SGK chia **Chủ đề** (không có “Chương”): `chapter` = `Chủ đề N. …`, `lesson` = `Bài N. …`. SCD: `chapter` = `Chuyên đề N. …`, `lesson` = mục La Mã `I. …`/`II. …`/`III. …` của chuyên đề.
- SGK có **Bảng tra cứu khái niệm, thuật ngữ** (PDF 144–145, 37 mục) và SCD có bảng tương tự (PDF 63–64, 25 mục). Toàn bộ 62 mục đều có trong glossary, định nghĩa lấy nguyên văn bảng; nguồn trang bảng đứng đầu, kèm nguồn trang thân bài nơi khái niệm xuất hiện. Mục trùng ở cả hai bảng (`tin-nguong`, `ton-giao`, `truc-thoi-gian`) giữ định nghĩa SGK, thêm nguồn `scd`.
- Lịch sử ít khái niệm “định nghĩa” thuần; phần lớn nội dung là **cơ sở hình thành, thành tựu, ý nghĩa, tác động**. Các nội dung trọng tâm này (theo yêu cầu cần đạt) được tách thành mục `tinh_chat`, tóm lược sát câu chữ SGK. Không lấy tư liệu trích dẫn, câu hỏi, hoạt động.
- Môn không có công thức, kí hiệu: 0 mục `cong_thuc`/`ky_hieu`/`dinh_ly`, 0 mục có `notation` (trừ $\pi$ trong mô tả thành tựu toán học cổ đại).
- File dữ liệu 307 KB, vượt ngưỡng cảnh báo 300 KB của `validate.py` (chỉ là cảnh báo) do nhiều mục `tinh_chat` dài.

## 2. Chủ đề/bài và số thuật ngữ

| Chủ đề / Chuyên đề | Bài / Mục | Số mục |
|---|---|---|
| Chủ đề 1. Lịch sử và sử học | Bài 1. Hiện thực lịch sử và nhận thức lịch sử | 25 |
|  | Bài 2. Tri thức lịch sử và cuộc sống | 3 |
| Chủ đề 2. Vai trò của sử học | Bài 3. Sử học với các lĩnh vực khoa học | 7 |
|  | Bài 4. Sử học với một số lĩnh vực, ngành nghề hiện đại | 14 |
| Chủ đề 3. Một số nền văn minh thế giới thời kì cổ – trung đại | Bài 5. Khái niệm văn minh. Một số nền văn minh phương Đông … | 23 |
|  | Bài 6. Một số nền văn minh phương Tây thời kì cổ – trung đại | 14 |
| Chủ đề 4. Các cuộc cách mạng công nghiệp trong lịch sử thế giới | Bài 7. … thời kì cận đại | 12 |
|  | Bài 8. … thời kì hiện đại | 13 |
| Chủ đề 5. Văn minh Đông Nam Á | Bài 9. Cơ sở hình thành văn minh Đông Nam Á … | 7 |
|  | Bài 10. Hành trình phát triển và thành tựu của văn minh Đông Nam Á … | 8 |
| Chủ đề 6. Một số nền văn minh trên đất nước Việt Nam (trước năm 1858) | Bài 11. Một số nền văn minh cổ trên đất nước Việt Nam | 16 |
|  | Bài 12. Văn minh Đại Việt | 26 (1 từ SBT) |
| Chủ đề 7. Cộng đồng các dân tộc Việt Nam | Bài 13. Đời sống vật chất và tinh thần … | 11 |
|  | Bài 14. Khối đại đoàn kết dân tộc trong lịch sử Việt Nam | 5 |
| Chuyên đề 1. Các lĩnh vực của sử học | I. Thông sử và lịch sử theo lĩnh vực | 7 |
|  | II. Một số lĩnh vực của lịch sử Việt Nam | 12 |
| Chuyên đề 2. Bảo tồn và phát huy giá trị di sản văn hoá ở Việt Nam | I. Di sản văn hoá | 7 |
|  | II. Bảo tồn và phát huy giá trị di sản văn hoá | 6 |
|  | III. Một số di sản văn hoá tiêu biểu ở Việt Nam | 14 |
| Chuyên đề 3. Nhà nước và pháp luật Việt Nam trong lịch sử | I. Nhà nước và pháp luật … (trước năm 1858) | 18 |
|  | II. Nhà nước Việt Nam từ năm 1945 đến nay | 5 |
|  | III. Một số bản Hiến pháp Việt Nam từ năm 1946 đến nay | 8 |

Khi lọc: `--chapter "Chủ đề 3"` hoặc `--lesson "Bài 5."` (SGK); `--chapter "Chuyên đề 2" --lesson "I."` (SCD). Mục SCD không trùng tên “Bài”, nhưng `--lesson "I."` khớp cả `II.`/`III.` — nên dùng tên mục đầy đủ.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 164 |
| tinh_chat | 88 |
| quy_tac | 9 |
| dinh_ly, cong_thuc, ky_hieu | 0 |

- Theo `level`: `co_ban` 184, `chuyen_de` 77.
- Theo nguồn định nghĩa: SGK 183, SCD 77, SBT 1. 18 mục mang thêm nguồn `gv` (12 SGV, 6 SGV CD); định nghĩa vẫn giữ theo SGK/SCD. 23 mục có nguồn từ hơn một file.
- Khái niệm trùng giữa SGK và SCD được **gộp vào mục SGK**, thêm nguồn `scd` (6 mục: `di-san-van-hoa`, `di-san-van-hoa-vat-the`, `di-san-van-hoa-phi-vat-the`, `tin-nguong`, `ton-giao`, `truc-thoi-gian`). Phần SCD mở rộng được tách riêng: `bao-ton-di-san-van-hoa` (SCD) ↔ `bao-ton` (SGK, bảng tra cứu); `nha-nuoc-quan-chu` (SCD) ↔ `thiet-che-chinh-tri-dai-viet` (SGK).
- `quy_tac` (9): ba nguyên tắc cơ bản của Sử học, phân loại sử liệu, điều cốt lõi trong bảo tồn di sản, phân loại theo dân số, phân loại và xếp hạng di sản/di tích, ba nguyên tắc chính sách dân tộc.
- 1 mục có `notes`: `chu-tuong-hinh` (bảng tra cứu ghi xuất hiện “khoảng thiên niên kỉ III TCN”, thân bài ghi “từ khoảng hơn 3 000 năm TCN”).

## 4. Yêu cầu cần đạt theo chủ đề

Nguồn: `SGV LICH SU 10.pdf`, phần “I. Mục tiêu – 1. Về kiến thức” đầu mỗi bài (số trang PDF trong ngoặc). Thời lượng theo “Một số lưu ý về nội dung và phương pháp”. Trích rút gọn.

- **Chủ đề 1. Lịch sử và Sử học** (Bài 1: 3 tiết, SGV tr.24–25; Bài 2: 3 tiết, tr.37–38): Trình bày khái niệm lịch sử; phân biệt hiện thực lịch sử và nhận thức lịch sử; giải thích khái niệm Sử học; đối tượng nghiên cứu, chức năng, nhiệm vụ, một số nguyên tắc cơ bản và phương pháp cơ bản của Sử học (ở mức độ đơn giản); phân biệt các nguồn sử liệu, biết sưu tầm, xử lí thông tin sử liệu. Nêu vai trò, ý nghĩa của tri thức lịch sử; giải thích sự cần thiết phải học tập lịch sử suốt đời.
- **Chủ đề 2. Vai trò của Sử học** (Bài 3: 3 tiết, tr.44–45; Bài 4: 3 tiết, tr.54–55): Giải thích Sử học là khoa học có tính liên ngành; mối liên hệ với khoa học xã hội và nhân văn; vai trò của khoa học tự nhiên và công nghệ đối với nghiên cứu lịch sử và ngược lại. Mối quan hệ giữa Sử học với bảo tồn, phát huy giá trị di sản văn hoá, di sản thiên nhiên; vai trò của Sử học với công nghiệp văn hoá; vai trò của lịch sử, văn hoá với du lịch và tác động của du lịch với bảo tồn di tích. SGV lưu ý du lịch là một ngành của công nghiệp văn hoá; mục 2 và 3 của Bài 4 có thể dạy gộp (tr.55).
- **Chủ đề 3. Một số nền văn minh thế giới thời kì cổ – trung đại** (Bài 5, tr.71; Bài 6, tr.84): Giải thích và phân biệt khái niệm văn hoá, văn minh; trình bày sự phát triển các nền văn minh trên trục thời gian; phân tích cơ sở hình thành văn minh phương Đông, phương Tây; nêu ý nghĩa thành tựu tiêu biểu của văn minh Ai Cập, Trung Hoa, Ấn Độ, Hy Lạp – La Mã và Tây Âu thời Phục hưng. **Giới hạn**: không sa đà giới thiệu chi tiết thành tựu; trọng tâm là giá trị, ý nghĩa của thành tựu (tr.72); chỉ yêu cầu hiểu khái quát khái niệm văn hoá để làm cơ sở hiểu khái niệm văn minh (tr.74).
- **Chủ đề 4. Các cuộc cách mạng công nghiệp** (Bài 7, tr.93; Bài 8, tr.104): Bối cảnh lịch sử, thành tựu cơ bản, ý nghĩa và tác động (kinh tế, văn hoá, xã hội) của bốn cuộc cách mạng công nghiệp. SGV lưu ý cách mạng công nghiệp lần thứ ba và thứ tư có liên hệ mật thiết (tr.105); cần phân tích cả tác động tiêu cực (tr.101).
- **Chủ đề 5. Văn minh Đông Nam Á** (Bài 9: 3 tiết, tr.115–116; Bài 10: 3 tiết, tr.127–128): Phân tích cơ sở tự nhiên, xã hội và ảnh hưởng của văn minh Ấn Độ, Trung Hoa; trình bày các thời kì phát triển trên trục thời gian; thành tựu về tín ngưỡng, tôn giáo, chữ viết, văn học, kiến trúc, điêu khắc.
- **Chủ đề 6. Một số nền văn minh trên đất nước Việt Nam (trước năm 1858)** (Bài 11: 6 tiết, tr.141–142; Bài 12, tr.159–160): Cơ sở hình thành và thành tựu tiêu biểu của văn minh Văn Lang – Âu Lạc, Chăm-pa, Phù Nam; khái niệm, cơ sở hình thành, tiến trình, thành tựu, ý nghĩa văn minh Đại Việt. **Giới hạn**: Bài 11 chỉ cần nêu một số thành tựu tiêu biểu, không cần nêu đầy đủ đời sống vật chất, tinh thần; không tìm hiểu về các quốc gia cổ (đã học ở lớp 6) mà về thành tựu văn minh (tr.142). Bài 12 chỉ chú trọng thành tựu, không liệt kê tình hình văn hoá qua từng triều đại (tr.160).
- **Chủ đề 7. Cộng đồng các dân tộc Việt Nam** (Bài 13, tr.177; Bài 14, tr.193): Thành phần tộc người theo dân số; khái niệm ngữ hệ và phân chia tộc người theo ngữ hệ; đời sống vật chất, tinh thần. Sự hình thành, vai trò của khối đại đoàn kết dân tộc; quan điểm nhất quán và nội dung cơ bản của chính sách dân tộc. SGV lưu ý đây là nội dung hoàn toàn mới so với chương trình cũ, cần đảm bảo vừa sức (tr.178).

**Chuyên đề** (nguồn: `SGV CD LICH SU 10.pdf`; `Tài liệu bồi dưỡng GV …` tr.37–38):
- **Chuyên đề 1. Các lĩnh vực của sử học** (10 tiết; SGV CD tr.13–14): Tóm tắt một số cách trình bày lịch sử truyền thống; phạm vi, đối tượng, nội dung của thông sử và một số lĩnh vực của lịch sử Việt Nam (văn hoá, tư tưởng, xã hội, kinh tế); giải thích “thông sử”, “lịch sử dân tộc”, “lịch sử thế giới”. Nên dạy sau Chủ đề 1 và 2.
- **Chuyên đề 2. Bảo tồn và phát huy giá trị di sản văn hoá ở Việt Nam** (15 tiết, thiên về trải nghiệm; tr.31–32): Khái niệm di sản văn hoá, bảo tồn di sản văn hoá, ý nghĩa; mục đích, ý nghĩa của phân loại, xếp hạng; mối quan hệ bảo tồn – phát huy; giải pháp, trách nhiệm các bên; vị trí và nét cơ bản của một số di sản tiêu biểu. Chương trình yêu cầu biết ba di sản văn hoá vật thể tiêu biểu: Thánh địa Mỹ Sơn, Đô thị cổ Hội An, Khu di tích trung tâm Hoàng thành Thăng Long – Hà Nội (tr.49).
- **Chuyên đề 3. Nhà nước và pháp luật Việt Nam trong lịch sử** (10 tiết; tr.51–52): Đặc điểm mô hình nhà nước quân chủ thời Lý – Trần, Lê sơ, Nguyễn; nét chính của Quốc triều hình luật và Hoàng Việt luật lệ; bối cảnh, ý nghĩa, đặc điểm, tính chất, vai trò của Nhà nước Việt Nam Dân chủ Cộng hoà và Nhà nước Cộng hoà xã hội chủ nghĩa Việt Nam; điểm chung các bản hiến pháp; nội dung Hiến pháp 1946, 1992 và điểm mới của Hiến pháp 2013. SGV đánh giá đây là chuyên đề khó (tên cơ quan, chức quan cổ). Nên dạy sau Chủ đề 6.

**Giới hạn chung** (Tài liệu bồi dưỡng GV tr.5, 9): SGK 70 tiết, 7 chủ đề × 2 bài, mỗi bài 3–6 tiết; lần đầu tiên THPT học theo **chủ đề** thay cho thông sử. Chuyên đề 35 tiết.

## 5. Sai lầm thường gặp của học sinh

SGV và SGV CD bộ này **không có mục “sai lầm thường gặp” riêng**. Bảng dưới tổng hợp các đoạn “GV lưu ý HS”, “HS cần hiểu”, “nhấn mạnh” chỉ ra điểm HS dễ hiểu sai (cột Nguồn: trang PDF của `SGV LICH SU 10.pdf`, hoặc `SGV CD` cho `SGV CD LICH SU 10.pdf`).

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Lịch sử là gì (Bài 1) | Tư duy một chiều, coi lịch sử chỉ là môn học thuộc lòng kiến thức có sẵn, không cần khám phá, không vận dụng được. | SGV tr.24 |
| Sử học (Bài 1) | Nhầm Sử học với hiện thực lịch sử: Sử học thuộc nghĩa **nhận thức lịch sử**. Hiện thực lịch sử khách quan, không thể thay đổi; nhận thức lịch sử luôn có khoảng cách với hiện thực. | SGV tr.27, 33; SGK PDF 8 |
| Văn hoá – văn minh (Bài 5) | Đồng nhất hai khái niệm: văn hoá xuất hiện cùng loài người; văn minh là trạng thái phát triển cao của văn hoá, xuất hiện muộn (khoảng nửa sau thiên niên kỉ IV TCN), gắn với nhà nước, đô thị, chữ viết. | SGV tr.74; SGK PDF 35 |
| Văn minh Ấn Độ (Bài 5) | Nghĩ văn minh Ấn Độ chỉ thuộc thời cổ đại: kéo dài từ cổ đại sang trung đại, đến giữa thế kỉ XIX (năm 1857). | SGV tr.80; SGK PDF 36 |
| Cách mạng công nghiệp (Bài 7) | Nhầm thời điểm các phát minh; cần nắm mối liên hệ giữa các phát minh (dệt → kéo sợi → máy hơi nước → luyện kim → đầu máy xe lửa). Chỉ nêu tác động tích cực, bỏ qua tiêu cực. | SGV tr.98, 101 |
| Văn học Đại Việt (Bài 12) | Cho rằng khi có chữ Nôm thì văn học chữ Hán mất vị trí: văn học chữ Hán vẫn quan trọng (Nam quốc sơn hà, Hịch tướng sĩ, Truyền kì mạn lục…). | SGV tr.172 |
| Dân tộc (Bài 13) | Nhầm hai nghĩa của “dân tộc”: dân tộc – quốc gia (dân tộc Việt Nam) và dân tộc – tộc người (Kinh, Mường…). Kinh là dân tộc đa số; 53 dân tộc còn lại là thiểu số. | SGV tr.180–181; SGK PDF 124 |
| Đại đoàn kết (Bài 14) | Hiểu đoàn kết là thủ đoạn chính trị nhất thời: đây là tư tưởng cơ bản, nhất quán, xuyên suốt. | SGV tr.203 |
| Phân loại di sản (CĐ 2) | Cho rằng mọi di sản phân loại rạch ròi vật thể/phi vật thể: nhiều di sản mang cả hai giá trị. | SGV CD tr.36; SCD PDF 26 |
| Xếp hạng di sản (CĐ 2) | Áp xếp hạng thứ bậc cho di sản phi vật thể: di sản phi vật thể thuộc về cộng đồng, Công ước 2003 của UNESCO bác bỏ việc xếp hạng thứ bậc; chỉ di tích (vật thể) được xếp hạng cấp tỉnh/quốc gia/quốc gia đặc biệt. | SGV CD tr.36, 50 |
| Di sản vật thể (CĐ 2) | Cho rằng di sản vật thể (công trình, di tích) chỉ có giá trị kiến trúc: còn chứa giá trị lịch sử, văn hoá, nghệ thuật. | SGV CD tr.45 |
| Bảo tồn (CĐ 2) | Bảo tồn thụ động: di sản chịu nhiều tác động nên cần quản lí đồng bộ, chủ động; bảo tồn là nền tảng để phát huy. | SGV CD tr.38 |
| Nhà nước Lê sơ (CĐ 3) | Cho rằng nhà nước Lê sơ chỉ quan liêu, không còn thân dân: vẫn thi hành nhiều chính sách quan tâm nhân dân như thời Lý – Trần (miễn giảm tô thuế, ân xá…). | SGV CD tr.55 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Năm sách nguồn là PDF dạng ảnh. Định nghĩa đọc từ OCR (tesseract `vie`, 300 dpi, cache ở `.ocr/`) và **đối chiếu ảnh trang** (80–150 dpi) với mọi trang có niên đại, số La Mã, sơ đồ, bảng. OCR thường đọc sai số La Mã (ví dụ “thiên niên kỉ II” thay cho “III”) và bỏ sót bảng/sơ đồ chữ trắng trên nền màu; mọi niên đại trong `definition` đã đối chiếu ảnh.
- Bổ sung cache OCR (nối thêm OCR 400 dpi, ảnh màu hoặc vùng cắt): SGK PDF 81 (sơ đồ ngữ hệ Đông Nam Á), PDF 110 (sơ đồ tiến trình văn minh Đại Việt), SCD PDF 51 (hộp Ngũ hình). Nếu xoá `.ocr/`, `check_sources.py` có thể gắn cờ lại `cac-ngu-he-o-dong-nam-a`.
- Mục `tinh_chat` là tóm lược nhiều đoạn sát câu chữ SGK (đã lược ví dụ, tư liệu); tên mục do người trích đặt theo đề mục sách. 50 cảnh báo tên (`tinh_chat`/`quy_tac` không có nguyên văn tên trong trang) — nội dung đều đạt bigram ≥ 0.65.
- Nguồn `gv` (18 mục) chỉ kiểm tra sự có mặt của tên thuật ngữ; 2 mục (`tinh-lien-nganh-cua-su-hoc`, `phan-biet-van-hoa-va-van-minh`) cảnh báo tên ở trang SGV nhưng nội dung khớp.

**Kiểm tra tự động** (2026-10-16, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py lich_su_10` | 0 lỗi; 261 thuật ngữ; 1 cảnh báo dung lượng (307 KB) |
| `check_sources.py lich_su_10` | 261 đạt, 0 gắn cờ, 0 không kiểm tra được, 50 cảnh báo tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 14 mục: 8 do mục tổng hợp nhiều trang có nguồn đầu là trang ít chữ hoặc nhiều hình (đổi thứ tự nguồn: thành tựu Ai Cập, Ấn Độ, Trung Hoa, đời sống vật chất các dân tộc, nhà nước quân chủ, nhà nước tập quyền quan liêu, kĩ thuật lập pháp; tách thành tựu Hy Lạp – La Mã thành 2 mục); 1 do sơ đồ chữ trắng OCR kém (bổ sung OCR 400 dpi ảnh màu: ngữ hệ Đông Nam Á); 3 do tên thân bài khác tên bảng tra cứu (thêm alias: `chu-mien-co`, `van-hoa-tien-dong-son`, `ngu-hinh`); 2 do nguồn phụ không chứa tên (bỏ nguồn phụ: `kinh-te-nhieu-thanh-phan-theo-co-che-thi-truong` PDF 22, `tam-giao-dong-nguyen` PDF 110). Không mục nào sai nội dung. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-16, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/261 (11,5%), toàn bộ ngẫu nhiên |
| Cách chọn | `query.py lich_su_10 --audit --sample 30` (seed 2026). Bộ không có mục `cong_thuc`/`dinh_ly`/`notation` nên phần “10 mục công thức” của `--audit` rỗng; dùng `--sample 30` để đủ 30 mục. Danh sách ở `sample_audit.md`. |
| Đối chiếu ảnh | Mở lại ảnh trong phiên kiểm tra: SGK PDF 8, 14, 21, 35, 36 (150 dpi), 41 (150 dpi), 145; SCD PDF 10, 13, 16, 17, 18, 19, 22, 28, 44, 59. Các trang còn lại của mẫu (SGK PDF 52, 79–82, 90–92, 105–106, 110–111, 117–118, 121; SCD PDF 20, 32, 41–42, 55–56, 60–61, 63–64) đã đối chiếu ảnh khi trích. |
| Số mục sai | 0 (0%, dưới ngưỡng 5%). Mục 4 (`khai-quat-tien-trinh…`): OCR bỏ sót dòng “Lưỡng Hà cổ đại” và đọc sai “thiên niên kỉ II”; ảnh xác nhận dữ liệu đúng. |
| Kiểm tra độc lập | Chưa thực hiện. `sample_audit.md` được giữ lại cho người kiểm tra ở phiên riêng; xoá sau khi kiểm tra xong. |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Lịch sử 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Cách mạng công nghiệp (Chủ đề 4) → cách mạng tư sản, chủ nghĩa tư bản (lớp 11).
- Văn minh Đông Nam Á, văn minh Đại Việt (Chủ đề 5–6) → quá trình xâm lược thuộc địa và cải cách ở Đông Nam Á, Việt Nam (lớp 11).
- Khối đại đoàn kết dân tộc, Mặt trận dân tộc thống nhất (Bài 14) → cách mạng tháng Tám, các cuộc kháng chiến (lớp 12).
- Nhà nước Việt Nam Dân chủ Cộng hoà, Hiến pháp (Chuyên đề 3) → lịch sử Việt Nam hiện đại (lớp 12).
- Liên môn: di sản văn hoá ↔ `ngu_van_10` (văn học dân gian, chữ Nôm); ngữ hệ, Đông Nam Á ↔ Địa lí 10; tôn giáo, tín ngưỡng ↔ GD KTPL.
