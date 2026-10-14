# Bộ thuật ngữ `ngu_van_10` — Ngữ văn 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/ngu_van_10/ngu_van_10.json`, gồm **191 thuật ngữ** (cập nhật 2026-10-14). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `ngu_van_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Ngu van 10 Tap 1.pdf | sgk | 170 | Nguồn chính, Bài 1–5, `level: co_ban` | Không (ảnh, OCR) |
| SGK Ngu van 10 Tap 2.pdf | sgk | 138 | Nguồn chính, Bài 6–9, `level: co_ban` | Không (ảnh, OCR) |
| SCD Ngu van 10.pdf | scd | 106 | Chuyên đề 1–3, `level: chuyen_de` | Không (ảnh, OCR) |
| SGV NGU VAN 10 TAP 1.pdf | gv | 166 | Yêu cầu cần đạt, tri thức mở rộng, lưu ý Bài 1–5 (mục 4–5); nguồn `gv` phụ; định nghĩa của 1 mục (`tinh-huong-truyen`) | Không (ảnh, OCR) |
| SGV NGU VAN 10 TAP 2.pdf | gv | 118 | Như trên, Bài 6–9 | Không (ảnh, OCR) |
| SGV CD NGU VAN 10.pdf | gv | 82 | SGV Chuyên đề: yêu cầu cần đạt, số tiết, lưu ý từng chuyên đề; nguồn `gv` phụ cho 4 mục chuyên đề | Không (ảnh, OCR) |
| SBT NGU VAN 10 TAP 1.pdf | sbt | 86 | Bổ sung 1 khái niệm SGK không nêu (`luc-bat-bien-the`) | Không (ảnh, OCR) |
| SBT NGU VAN 10 TAP 2.pdf | sbt | 74 | Đã rà soát, không có khái niệm mới (chỉ đề bài và gợi ý đáp án) | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Ngữ văn 10.pdf | gv | 77 | Phân bổ số tiết (mục 4), lưu ý dạy từng kiểu bài viết (mục 5) | Có |

- Ở cả tám sách dạng ảnh: **trang PDF = trang in + 1**.
- **Ngữ văn không chia chương.** Trường `chapter` là `Tập một` / `Tập hai` (SGK) hoặc `Chuyên đề N. …` (SCD); `lesson` là `Bài N. …` (SGK) hoặc `Phần N. …` (SCD). Ví dụ lọc: `--lesson "Bài 2."`, `--chapter "Chuyên đề 2."`. SGK đánh số bài liên tục 1–9 nên không trùng với SCD (SCD dùng "Phần").
- Nguồn định nghĩa chính là ô **Tri thức ngữ văn** đầu mỗi bài (SGK) / **Tri thức tổng quát** (SCD), các ô kiến thức ở phần Thực hành tiếng Việt, khung **Yêu cầu** của mỗi kiểu bài Viết, và **Bảng giải thích một số thuật ngữ** cuối sách (SGK tập một tr.162–163, tập hai tr.130–131, SCD tr.98–100). Toàn bộ mục trong ba bảng giải thích (48 + 26 + 38 dòng) đều có trong glossary; `cận thể`, `Đường luật` (bảng tập một) là alias của `tho-duong-luat`, `tích truyện` là alias của `tich-tro`. 80 mục lấy định nghĩa trực tiếp từ bảng (nguồn đầu là trang bảng), 108 mục có ít nhất một nguồn là trang bảng.
- Các mục `quy_tac` gồm: lỗi dùng từ/trật tự từ/mạch lạc/liên kết, cách dùng trích dẫn, nhận biết biện pháp chêm xen/liệt kê, luật thơ thất ngôn bát cú, và **yêu cầu của từng kiểu bài viết** (tên bắt đầu bằng "yêu cầu đối với kiểu bài …"), chép theo khung "Yêu cầu" của SGK.
- Không trích nội dung văn bản đọc (tác phẩm), câu hỏi, gợi ý trả lời, "Bài viết tham khảo", hướng dẫn quy trình viết/nói.
- Bảng tra cứu yếu tố Hán Việt (SCD tr.101) và Bảng tra cứu tên riêng nước ngoài không đưa vào (không phải thuật ngữ).

## 2. Bài và số thuật ngữ

| Chapter | Lesson | Số mục | Ghi chú |
|---|---|---|---|
| Tập một | Bài 1. Sức hấp dẫn của truyện kể | 17 | gồm 1 mục định nghĩa theo SGV (`tinh-huong-truyen`) |
| | Bài 2. Vẻ đẹp của thơ ca | 34 | thơ, thi luật, thơ Đường luật, hai-cư, Thơ mới; lỗi dùng từ, trật tự từ |
| | Bài 3. Nghệ thuật thuyết phục trong văn nghị luận | 13 | |
| | Bài 4. Sức sống của sử thi | 20 | |
| | Bài 5. Tích trò sân khấu dân gian | 10 | gồm 1 mục từ SBT (`luc-bat-bien-the`) |
| Tập hai | Bài 6. Nguyễn Trãi – “Dành còn để trợ dân này” | 15 | |
| | Bài 7. Quyền năng của người kể chuyện | 16 | |
| | Bài 8. Thế giới đa dạng của thông tin | 9 | |
| | Bài 9. Hành trang cuộc sống | 5 | |
| Chuyên đề 1. Tập nghiên cứu và viết báo cáo về một vấn đề văn học dân gian | Phần 1. Tập nghiên cứu | 26 | |
| | Phần 2. Viết báo cáo nghiên cứu về một vấn đề văn học dân gian | 3 | |
| Chuyên đề 2. Sân khấu hoá tác phẩm văn học | Phần 1. Tìm hiểu về sân khấu hoá tác phẩm văn học | 8 | |
| | Phần 2. Thực hành sân khấu hoá tác phẩm văn học | 2 | |
| Chuyên đề 3. Đọc, viết, giới thiệu một tập thơ, một tập truyện ngắn hoặc một tiểu thuyết | Phần 1. Đọc một tập thơ, một tập truyện ngắn hoặc một tiểu thuyết | 13 | |

Ôn tập học kì I, II và Phần 2, 3 của Chuyên đề 3 không có khái niệm mới (0 mục).

Một số mục trong Bảng giải thích thuật ngữ không gắn với một bài cụ thể; chúng được xếp vào bài mà Bảng tra cứu thuật ngữ ghi trang xuất hiện đầu tiên (ví dụ `tinh-cach-nhan-vat` → Bài 1, `chuyen-the` → Bài 4, `bieu-do`/`so-do` → Bài 9, `ban-ke`/`hai-kich`/`van-phong-khoa-hoc` → Chuyên đề 1 Phần 2).

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 146 |
| quy_tac | 24 |
| tinh_chat | 21 |
| dinh_ly, cong_thuc, ky_hieu | 0 |

- Theo `level`: `co_ban` 139, `chuyen_de` 52.
- Theo nguồn định nghĩa: SGK 137, SCD 52, SGV 1, SBT 1. Có 30 mục mang thêm nguồn `gv` (SGV giải thích rõ hoặc mở rộng), 32 mục có nguồn từ hơn một file.
- Ngữ văn không có công thức; chỉ 1 mục có `notation` (`phan-bi-tinh-luoc`: `[...]`).
- Khái niệm trùng giữa SGK và SCD với phát biểu khác nhau được tách hai mục (hậu tố `-chuyen-de`): `tho` / `tho-chuyen-de`, `bao-cao-nghien-cuu` / `bao-cao-nghien-cuu-chuyen-de`. Khái niệm trùng với phát biểu tương đương được gộp (SCD là nguồn phụ): `chuyen-the`, `bao-cao-ket-qua-nghien-cuu`.
- `nhan-vat` (SGK Tri thức ngữ văn Bài 1) và `nhan-vat-van-hoc` (Bảng giải thích, tập hai) là hai phát biểu khác nhau của cùng khái niệm, giữ cả hai và nối bằng `related_terms`.

## 4. Yêu cầu cần đạt theo bài

Nguồn: mục "I. Yêu cầu cần đạt" đầu mỗi bài trong SGV (trùng với khung "Yêu cầu cần đạt" của SGK); số tiết theo SGV và Tài liệu bồi dưỡng GV mục 7 (trang PDF 30–31; tổng 105 tiết/năm). Trích rút gọn.

- **Bài 1. Sức hấp dẫn của truyện kể** (11 tiết; SGV tập 1 tr.38): Nhận biết và phân tích một số yếu tố của truyện nói chung và thần thoại nói riêng: cốt truyện, không gian, thời gian, nhân vật, lời người kể chuyện ngôi thứ ba và lời nhân vật. Phân tích, đánh giá chủ đề, tư tưởng, thông điệp; căn cứ xác định chủ đề. Viết văn bản nghị luận phân tích, đánh giá chủ đề và nét đặc sắc nghệ thuật của một tác phẩm truyện. Thuyết trình về nội dung và nghệ thuật của một tác phẩm truyện.
- **Bài 2. Vẻ đẹp của thơ ca** (11 tiết; SGV tập 1 tr.59): Phân tích, đánh giá giá trị thẩm mĩ của từ ngữ, hình ảnh, vần, nhịp, đối, nhân vật trữ tình (chủ thể trữ tình). Liên hệ điểm gần gũi về nội dung giữa thơ của hai nền văn hoá. Nhận biết và sửa lỗi dùng từ, lỗi trật tự từ. Viết văn bản nghị luận phân tích, đánh giá một tác phẩm thơ; thuyết trình về một tác phẩm thơ.
- **Bài 3. Nghệ thuật thuyết phục trong văn nghị luận** (11 tiết; SGV tập 1 tr.91): Nhận biết, phân tích luận đề, luận điểm, lí lẽ, bằng chứng và mối quan hệ giữa chúng; mục đích, quan điểm người viết. Nhận ra và khắc phục lỗi mạch lạc, liên kết. Viết bài luận thuyết phục người khác từ bỏ một thói quen hay một quan niệm. Thảo luận về vấn đề có ý kiến khác nhau.
- **Bài 4. Sức sống của sử thi** (9 tiết; SGV tập 1 tr.114): Nhận biết, phân tích không gian, thời gian, cốt truyện, nhân vật, lời người kể chuyện và lời nhân vật trong sử thi. Hiểu cách đánh dấu phần bị tỉnh lược, chú thích trích dẫn, ghi cước chú. Viết báo cáo nghiên cứu có trích dẫn, cước chú; hiểu quyền sở hữu trí tuệ, tránh đạo văn. Trình bày báo cáo kết quả nghiên cứu.
- **Bài 5. Tích trò sân khấu dân gian** (7 tiết; SGV tập 1 tr.138): Nhận biết, phân tích đề tài, tính vô danh, tích truyện, nhân vật, lời thoại, phương thức lưu truyền của văn bản chèo hoặc tuồng. Viết báo cáo nghiên cứu (vấn đề văn hoá truyền thống) có trích dẫn, cước chú, phương tiện hỗ trợ. Lắng nghe và phản hồi bài thuyết trình kết quả nghiên cứu.
- **Bài 6. Nguyễn Trãi – “Dành còn để trợ dân này”** (12 tiết; SGV tập 2 tr.6): Vận dụng hiểu biết về tác gia Nguyễn Trãi để đọc hiểu tác phẩm; phân tích bối cảnh lịch sử – văn hoá trong văn bản văn học; cách sắp xếp luận điểm, lí lẽ, bằng chứng và vai trò của yếu tố biểu cảm trong văn bản nghị luận. Viết văn bản nghị luận về một vấn đề xã hội. Thảo luận về vấn đề có ý kiến khác nhau.
- **Bài 7. Quyền năng của người kể chuyện** (12 tiết; SGV tập 2 tr.38): Nhận biết, phân tích người kể chuyện ngôi thứ ba và ngôi thứ nhất, điểm nhìn, lời người kể chuyện, lời nhân vật; cảm hứng chủ đạo. Hiểu tác dụng và vận dụng biện pháp chêm xen, liệt kê. Viết bài nghị luận phân tích, đánh giá chủ đề và nhân vật trong tác phẩm truyện.
- **Bài 8. Thế giới đa dạng của thông tin** (11 tiết; SGV tập 2 tr.70): Phân tích đề tài, thông tin cơ bản, cách đặt nhan đề, mục đích người viết của văn bản thông tin; nhận biết văn bản thông tin lồng ghép thuyết minh với miêu tả, tự sự, biểu cảm, nghị luận; kết hợp phương tiện ngôn ngữ và phi ngôn ngữ. Đánh giá cách đưa tin và quan điểm người viết ở bản tin. Viết bản nội quy hoặc bản hướng dẫn nơi công cộng.
- **Bài 9. Hành trang cuộc sống** (11 tiết; SGV tập 2 tr.90): Nhận biết bối cảnh lịch sử, văn hoá, xã hội của văn bản; đánh giá tác dụng của phương tiện phi ngôn ngữ. Viết bài luận về bản thân. Thuyết trình về một vấn đề xã hội có kết hợp phương tiện ngôn ngữ và phi ngôn ngữ.
- **Ôn tập học kì I, II** (SGV tập 1 tr.158, tập 2 tr.110): Hệ thống hoá kiến thức, vận dụng tổng hợp.

**Chuyên đề** (nguồn: SGV CD tr.7–8, trang PDF):
- **Chuyên đề 1. Tập nghiên cứu và viết báo cáo về một vấn đề văn học dân gian** (10 tiết): Biết yêu cầu và cách thức nghiên cứu một vấn đề văn học dân gian; viết báo cáo nghiên cứu; vận dụng hiểu biết để đọc hiểu, viết về văn học dân gian; thuyết trình về một vấn đề văn học dân gian. Báo cáo của HS lớp 10 là "tập nghiên cứu", dung lượng tối thiểu khoảng 8 trang A4 (SGV CD tr.16).
- **Chuyên đề 2. Sân khấu hoá tác phẩm văn học** (15 tiết): Hiểu thế nào là sân khấu hoá; biết tiến hành sân khấu hoá; đóng vai và biểu diễn; nhận biết khác biệt giữa ngôn ngữ văn bản văn học và ngôn ngữ sân khấu.
- **Chuyên đề 3. Đọc, viết, giới thiệu một tập thơ, một tập truyện ngắn hoặc một tiểu thuyết** (10 tiết): Biết cách đọc, viết bài giới thiệu và trình bày, giới thiệu một tập thơ, tập truyện ngắn hoặc tiểu thuyết.

**Giới hạn và trọng tâm theo SGV.** Agent sinh câu hỏi lưu ý:
- Chèo, tuồng: chương trình chỉ dạy **chèo, tuồng dân gian**. Không ra câu hỏi về đặc trưng riêng của tuồng cung đình/tuồng bác học (phục trang, đạo cụ, tính ước lệ cao…) (SGV tập 1 tr.139, 159).
- Thơ hai-cư: quy định 17 âm tiết là của thơ hai-cư Nhật Bản cổ điển; bản dịch tiếng Việt không giữ thi luật này (SGV tập 1 tr.61). Không hỏi đếm âm tiết trên bản dịch.
- Thần thoại: đặc điểm "thời gian phiếm chỉ, không gian vũ trụ" không khớp hoàn toàn với mọi hệ thần thoại (ví dụ Tê-dê – thần thoại Hy Lạp) (SGV tập 1 tr.158).
- Toàn tri / hạn tri chỉ là dấu hiệu bề ngoài dễ nhận biết của ngôi kể, không hàm ý đánh giá ngôi kể nào hơn (SGV tập 2 tr.110–111).
- Văn bản nghị luận: không chỉ có hai tiểu loại nghị luận xã hội và nghị luận văn học; có văn bản khó xếp loại (ví dụ *Yêu và đồng cảm*) (SGV tập 1 tr.159).

## 5. Sai lầm thường gặp của học sinh

SGV không có mục riêng về lỗi sai. Dưới đây là các điểm dễ nhầm được SGV và Tài liệu bồi dưỡng GV nêu rõ ("lưu ý", "tránh", "nhầm", "phân biệt"). Cột Nguồn ghi trang PDF; đã đối chiếu ảnh trang.

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Thơ và thơ trữ tình (Bài 2) | Đánh đồng thơ với thơ trữ tình. Thơ còn gồm thơ tự sự và thơ mang hình thức kịch; thơ trữ tình chỉ là một "thể" của thơ. | SGV tập 1 tr.60, 158 |
| Nhân vật trữ tình (Bài 2) | Nhầm nhân vật trữ tình với nhân vật **trong** thơ trữ tình. Nhân vật trong thơ trữ tình không phải chủ thể cảm xúc mà chỉ là đối tượng khơi gợi cảm xúc (ví dụ ông đồ trong *Ông đồ* không phải nhân vật trữ tình). Nhân vật trữ tình không hoàn toàn đồng nhất với tác giả. | SGV tập 1 tr.60 |
| Luật thơ Đường (Bài 2) | Coi mọi trường hợp phạm luật, thất niêm, thất đối, thất vận là lỗi. Nhiều trường hợp là phá cách có ý thức; nhiều câu, bài thất luật vẫn là thơ hay. | SGV tập 1 tr.70 |
| Lỗi dùng từ, trật tự từ (Bài 2) | Không phân biệt lỗi dùng từ, lỗi trật tự từ với biện pháp tu từ (điệp ngữ, đảo ngữ) trong văn bản văn học. | SGV tập 1 tr.84; SGK tập 1 tr.59–61 |
| Từ Hán Việt (Bài 1) | Dùng sai do nhầm ngữ âm, chính tả (*trí thức* → *tri thức*); dùng sai nghĩa (*hàn sĩ* chỉ người trí thức nghèo, không chỉ sự cứng cỏi); hiểu sai yếu tố cấu tạo (*yếu điểm* = điểm quan trọng, khác *điểm yếu*). | SGV tập 1 tr.54 |
| Mạch lạc và liên kết (Bài 3) | Nhầm lặp từ với liên kết: lặp lại một từ ở mọi câu nhưng các câu không cùng chủ đề thì đoạn văn vẫn thiếu mạch lạc. Cố ý lặp từ không đồng nghĩa với dùng phép lặp. | SGV tập 1 tr.109 |
| Sử thi (Bài 4) | Nhiều HS nghĩ sử thi được kể bằng văn xuôi (do đọc qua bản dịch). Thực tế sử thi được sáng tác bằng văn vần hoặc văn xuôi có nhịp điệu riêng. | SGV tập 1 tr.159 |
| Truyện và sử thi (Ôn tập I) | Nhầm lẫn truyện với sử thi khi kể thể loại đã học; cần phân biệt truyện ngắn trung đại với truyện ngắn hiện đại. | SGV tập 1 tr.160 |
| Chèo và tuồng (Bài 5) | *Nghêu, Sò, Ốc, Hến* có bản chuyển thể thành chèo; khi xem vở diễn phải phân biệt đâu là tuồng, đâu là chèo. | SGV tập 1 tr.139 |
| Đề tài và vấn đề (Bài 5) | Không phân biệt đề tài với vấn đề nghiên cứu. Vấn đề là câu hỏi mà báo cáo phải giải đáp qua hệ thống luận điểm. | SGV tập 1 tr.154 |
| Người kể chuyện (Bài 7) | Nhận biết được ngôi kể nhưng không phân biệt được quyền năng của người kể chuyện ngôi thứ ba so với ngôi thứ nhất; chưa hiểu quan hệ giữa quyền năng người kể với lời kể, điểm nhìn, cảm hứng chủ đạo. | SGV tập 2 tr.42 |
| Cảm hứng chủ đạo (Bài 7) | Nhầm tư tưởng chủ đề (nội dung tư tưởng xuyên suốt) với cảm hứng chủ đạo (tình cảm, thái độ nổi bật). | SGV tập 2 tr.39 |
| Bản dịch thơ (Bài 6) | Hiểu theo bản dịch thơ dẫn đến sai nghĩa (ví dụ *cảnh tiên* trong *Dục Thuý sơn* dễ bị hiểu nhầm là phong cảnh, trong khi "cảnh" là cõi, bờ cõi). Cần đối chiếu bản dịch nghĩa. | SGV tập 2 tr.29 |
| Phương tiện phi ngôn ngữ (Bài 8–9) | Coi sơ đồ, biểu đồ, hình ảnh chỉ là phần minh hoạ thêm; thực tế chúng là thông tin quan trọng, không thể thiếu của văn bản thông tin đa phương thức. | SGV tập 2 tr.111 |
| Bài luận về bản thân (Bài 9) | Đánh đồng bài luận về bản thân với văn bản tự giới thiệu (sở thích, điểm mạnh, điểm yếu) khi xin việc, ứng cử. | Tài liệu bồi dưỡng GV tr.53 |
| Phân tích tác phẩm thơ (Bài 2) | Lạm dụng thán từ, nhận định chung chung thiếu căn cứ; áp mô hình "mạch cảm xúc" cho mọi bài thơ (chỉ phù hợp với thơ hiện đại viết theo bút pháp lãng mạn). | Tài liệu bồi dưỡng GV tr.52 |
| Cải biên (Chuyên đề 2) | Coi tiếp thu và cải biên là loại trừ nhau. | SGV CD tr.42 |
| Đọc tập sách (Chuyên đề 3) | Nắm sơ sài thông tin hình thức (nhan đề, năm xuất bản, nhà xuất bản…) dẫn đến nhầm tập này với tập khác của cùng tác giả. | SGV CD tr.58 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Tám sách nguồn là PDF dạng ảnh. Định nghĩa được đọc trực tiếp từ ảnh trang (110–130 dpi). `check_sources.py` đối chiếu với text OCR (tesseract `vie`), lưu cache ở `.ocr/`. Cache của các trang Bảng giải thích thuật ngữ (SGK tập một p0163–p0164, tập hai p0131–p0132, SCD p0099–p0101) được tạo lại bằng ba chế độ `--psm 3/6/4` cộng OCR riêng từng cột (cắt ảnh theo cột), vì chế độ mặc định trộn cột tên với cột giải thích và không đọc được tên thuật ngữ xuống dòng.
- OCR hay sai dấu (thể/thẻ, để/đề, vần/vân…). Bigram có dấu vẫn đạt nhưng sai sót nhỏ về dấu trong `definition` chỉ được phát hiện qua kiểm tra ảnh.
- Tên của các mục `quy_tac`/`tinh_chat` thường do người trích đặt (ví dụ "yêu cầu đối với kiểu bài …", "đặc điểm của thần thoại"). Lần chạy gần nhất có 12 cảnh báo tên; nội dung các mục này đạt bigram ≥ 0.85.
- Nguồn `gv` (30 mục) và nguồn phụ chỉ được kiểm tra sự có mặt của tên thuật ngữ, không kiểm tra bigram (định nghĩa giữ theo SGK/SCD).
- Có 2 mục mang `notes`: `tinh-huong-truyen` (SGK không định nghĩa, lấy theo SGV), `luc-bat-bien-the` (lấy từ phần gợi ý đáp án SBT).
- `query.py --audit` chỉ chọn được 21 mục vì bộ không có `cong_thuc`/`ky_hieu`/notation (trừ 1 mục); 9 mục còn lại chọn thủ công (seed 2026) từ `quy_tac`/`tinh_chat`/`dinh_nghia` và nối vào `sample_audit.md`.

**Kiểm tra tự động** (2026-10-14, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py ngu_van_10` | 0 lỗi; 191 thuật ngữ |
| `check_sources.py ngu_van_10` | 191 đạt, 0 gắn cờ, 0 không kiểm tra được, 12 cảnh báo về tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 13: 10 do OCR không đọc được tên trong bảng thuật ngữ hai cột (OCR lại theo cột); 2 do định nghĩa ghép từ hai trang (`loi-mach-lac`: đổi thứ tự nguồn; `loi-ve-trat-tu-tu`: bỏ câu thuộc trang khác); 1 do alias không xuất hiện ở trang nguồn (`van-ban-thong-tin-tong-hop`: bỏ alias và nguồn phụ). Không mục nào sai nội dung. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-14, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/191 (15,7%): 21 từ `query.py --audit` (seed 2026) + 9 mục bổ sung (6 `quy_tac`/`tinh_chat`, 3 `dinh_nghia`) |
| Cách đối chiếu | So từng từ của `definition` với OCR trang nguồn (difflib): mọi chênh lệch đều là lỗi dấu của OCR. Đọc lại ảnh trang (170 dpi) cho các mục dài/ghép đoạn: `luat-tho-that-ngon-bat-cu-duong-luat`, `phan-loai-tho`, `tinh-tap-the`, cùng các mục SCD tr.4–5 liên quan |
| Số mục sai nội dung | 0 |
| Số mục sửa diễn đạt | 1: `tinh-tap-the` có câu dẫn do người trích đặt, sửa sát nguyên văn hơn. Ngoài ra sửa `than-thoai-sang-tao` (bỏ ngoặc đơn không có trong bảng) khi đối chiếu bảng thuật ngữ |
| Kiểm tra độc lập | **Chưa làm.** Chờ người dùng đối chiếu `sample_audit.md` với ảnh trang nguồn ở phiên riêng, sau đó xoá file |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Ngữ văn 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Người kể chuyện, điểm nhìn, lời người kể chuyện (Bài 1, 7) → truyện ngắn, tiểu thuyết hiện đại.
- Thơ, thể thơ, thơ Đường luật, Thơ mới (Bài 2, 6) → thơ trữ tình hiện đại.
- Văn bản nghị luận, luận đề, luận điểm (Bài 3, 6) → nghị luận văn học, nghị luận xã hội ở lớp trên.
- Văn bản thông tin (Bài 8, 9) → văn bản thông tin tổng hợp.
