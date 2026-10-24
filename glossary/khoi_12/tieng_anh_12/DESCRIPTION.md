# Bộ thuật ngữ `tieng_anh_12` — Tiếng Anh 12 Global Success (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_12/tieng_anh_12/tieng_anh_12.json` (tập trung: `glossary/dataset/tieng_anh_12.json`), gồm **284 mục** (cập nhật 2026-10-23). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_12/tieng_anh_12/`, bộ Tiếng Anh 12 Global Success (NXB Giáo dục Việt Nam – Pearson).

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK TIẾNG ANH 12- GLOBAL SUCCEESS.pdf | sgk | 160 | Nguồn chính, `level: co_ban`: bảng Glossary cuối sách (PDF 149–157), ô Remember! ở phần Language, định nghĩa nêu tường minh ở mục Culture | Không (ảnh, OCR) |
| SGV TIENG ANH 12 Global Success.pdf | gv | 282 | OBJECTIVES từng Unit (mục 4, `lessons`) | Không (ảnh, OCR) |

- **Sách trong thư mục:** SGK và `SGV TIENG ANH 12 Global Success.pdf` (gv, 282 trang, dạng ảnh, trang PDF = trang in + 1; bổ sung 2026-10-24, dùng cho `lessons` ở mục 4). Chưa có SBT, Slide tập huấn. Mục 5 (sai lầm thường gặp) chưa điền: chưa đọc SGV theo hướng này.
- Trang PDF = trang in + 2 (đã đối chiếu số in ở chân trang tại PDF 11, 23, 35, 52, 64, 80, 92, 104, 120, 132 và các trang Glossary). Tên file SGK viết sai chính tả `SUCCEESS` (giữ nguyên tên file gốc).
- **Cấu trúc `chapter`/`lesson`** (giống `tieng_anh_10`): `chapter` = `Unit N. <Tên unit>` (10 unit) hoặc `Review N` (4 Review); `lesson` = 8 tiết chuẩn của mỗi unit (`Lesson 1. Getting started`, `Lesson 2. Language`, `Lesson 3. Reading`, `Lesson 4. Speaking`, `Lesson 5. Listening`, `Lesson 6. Writing`, `Lesson 7. Communication and culture / CLIL`, `Lesson 8. Looking back and project`) cộng `Glossary` (bảng từ vựng cuối SGK). Review chia `Language`/`Skills`. Mục lục lấy từ Book Map (PDF 6–9) của sách. Ví dụ lọc: `--chapter "Unit 5."`, `--chapter "Unit 5." --lesson Glossary`, `--lesson "Lesson 2."`.
- **Ba nhóm mục:**
  1. **Từ vựng (247 mục, lesson `Glossary`)**: mỗi dòng của bảng Glossary là một mục `dinh_nghia`. `term` = từ/cụm từ tiếng Anh; `definition` = nghĩa tiếng Việt **đúng nguyên văn** bảng; `notation` = loại từ + phiên âm IPA như sách, ví dụ `(n) /əˈkaʊnt/` (mục không ghi loại từ thì chỉ có IPA: `carry out`, `rush hour`, `CV`). Phiên âm chép theo sách; kí tự nối `ʧ`/`ʤ` của sách được viết `tʃ`/`dʒ`. Từ viết tắt có tên đầy đủ trong sách (`artificial intelligence (AI)`, `CV (curriculum vitae)`) thì dạng còn lại để ở `aliases`; phiên âm tên đầy đủ ghi trong ngoặc ở `notation`.
  2. **Ngữ pháp và phát âm (36 mục, lesson `Lesson 2. Language`)**: chép từ ô **Remember!** bằng tiếng Anh, giữ nguyên câu ví dụ của sách. Công thức (`have + someone + bare infinitive`, `have/get + something + past participle`, hai cấu trúc present perfect) để ở `notation`. Phần phát âm chỉ có bảng từ (Listen and repeat) được ghi dạng `ky_hieu` kèm `notes` nói rõ SGK không nêu quy tắc.
  3. **Định nghĩa tiếng Anh ở mục Culture (1 mục)**: `culture-shock-culture` (Unit 2, PDF 31), nối với mục Glossary `culture-shock` bằng `related_terms`, theo tiền lệ `tieng_anh_10`.
- Từ lặp trong Glossary ở hai unit được tách mục, mục sau thêm hậu tố unit: `admire` (Unit 1, nghĩa "ngưỡng mộ") / `admire-unit-2` (nghĩa "ngắm nhìn, chiêm ngưỡng"); `reliable` (Unit 4, "đáng tin cậy") / `reliable-unit-7` ("xác thực").
- Không trích: hội thoại, bài đọc, đề bài và đáp án, bài "Match the words with their meanings" (bài tập ghép nghĩa), Everyday English, tên tổ chức/nhân vật, Appendix 1–2 (PDF 146–148: chiến lược làm bài, mẹo thi), mục "This unit includes" ở trang mở Unit (danh mục nội dung, không phải yêu cầu cần đạt), giải thích từ nguyên của "robot" trong CLIL Unit 6 (không phải định nghĩa thuật ngữ).
- Từ vựng giữ nguyên cách SGK ghi, kể cả chỗ lệch từ điển: `rapidly` ghi `(v)` trong khi là phó từ (có `notes`); `programme (v)`; `proportion` v.v.

## 2. Bài và số thuật ngữ

| Chapter | Glossary | Lesson 2. Language | Lesson 7 | Ghi chú |
|---|---|---|---|---|
| Unit 1. Life stories we admire | 33 | 4 | | diphthongs /eɪ/ và /əʊ/; past simple, past continuous và so sánh hai thì |
| Unit 2. A multicultural world | 28 | 5 | 1 | diphthongs /ɔɪ/, /aɪ/, /aʊ/; articles (a/an, the, no article); culture shock |
| Unit 3. Green living | 22 | 4 | | diphthongs /ɪə/, /eə/, /ʊə/; verbs with prepositions; phrasal verbs; relative clauses referring to a whole sentence |
| Unit 4. Urbanisation | 16 | 5 | | unstressed words in connected speech; present perfect (3 mục); double comparatives |
| Unit 5. The world of work | 20 | 4 | | stressing auxiliary and modal verbs; simple, compound, complex sentences |
| Unit 6. Artificial intelligence | 23 | 3 | | homophones; active/passive causatives |
| Unit 7. The world of mass media | 30 | 4 | | linking /r/; adverbial clauses (manner, result) |
| Unit 8. Wildlife conservation | 28 | 3 | | assimilation; adverbial clauses (condition, comparison) |
| Unit 9. Career paths | 23 | 2 | | sentence stress and rhythm; three-word phrasal verbs |
| Unit 10. Lifelong learning | 24 | 2 | | intonation in questions; reported speech (orders, requests, offers, advice) |

Review 1–4, Lesson 1, 3–6 và 8 không có khái niệm mới (0 mục). Glossary theo trang PDF: Unit 1 tr.149–150; Unit 2 tr.150; Unit 3 tr.151; Unit 4 tr.151–152; Unit 5 tr.152–153; Unit 6 tr.153; Unit 7 tr.154–155; Unit 8 tr.155–156; Unit 9 tr.156; Unit 10 tr.157. Bảng Glossary của SGK 12 không có mục nào cho Review.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 256 (247 từ vựng Glossary + 8 định nghĩa ngữ pháp/phát âm ở Language + 1 định nghĩa ở mục Culture) |
| quy_tac | 21 |
| cong_thuc | 4 |
| ky_hieu | 3 |
| dinh_ly, tinh_chat | 0 |

- Theo `level`: `co_ban` 284 (bộ không có sách chuyên đề). Theo nguồn: SGK 284 (chưa có nguồn `gv`).
- 256 mục có `notation` (247 phiên âm từ vựng + 9 công thức/kí hiệu).
- 5 mục có `notes`: `rapidly` (SGK ghi loại từ (v)); 3 mục diphthongs (SGK chỉ đưa bảng từ, không nêu quy tắc); `assimilation` (phiên âm các ví dụ trong bảng được lược khỏi `definition`). Agent **không** được tự suy ra quy tắc phát âm cho các mục diphthongs.

## 4. Yêu cầu cần đạt theo bài

Nguồn: mục "OBJECTIVES – By the end of this unit, students will be able to" ở trang mở đầu mỗi Unit trong `SGV TIENG ANH 12 Global Success.pdf` (trang in = trang PDF − 1). Đã nhập vào `lessons` (10 mục, `lesson: null`, `book_type: gv`, `label: "OBJECTIVES"`, chép nguyên văn tiếng Anh). 4 Review không có khung mục tiêu. Truy vấn: `query.py tieng_anh_12 --lessons --chapter "Unit 5."`.

| Unit | SGV (PDF) | Ngữ âm | Từ vựng | Ngữ pháp |
|---|---|---|---|---|
| 1. Life stories we admire | 9 | nguyên âm đôi /eɪ/, /əʊ/ | life stories | past simple, past continuous |
| 2. A multicultural world | 29 | nguyên âm đôi /ɔɪ/, /aɪ/, /aʊ/ | cultural diversity | definite and indefinite articles |
| 3. Green living | 51 | nguyên âm đôi /ɪə/, /eə/, /ʊə/ | green living | verbs with prepositions; relative clauses referring to a whole sentence |
| 4. Urbanisation | 81 | unstressed words in connected speech | urbanisation | present perfect (It/This/That … the first/best …); double comparatives |
| 5. The world of work | 103 | stressed auxiliary and modal verbs | work | simple, compound, complex sentences |
| 6. Artificial intelligence | 132 | homophones | science and technology | active and passive causatives |
| 7. The world of mass media | 152 | linking /r/ | the mass media | adverbial clauses of manner and result |
| 8. Wildlife conservation | 174 | assimilation | conserving wildlife | adverbial clauses of condition and comparison |
| 9. Career paths | 203 | sentence stress and natural rhythm | choosing a career path | three-word phrasal verbs |
| 10. Lifelong learning | 223 | rising and falling intonation in questions | lifelong learning | reported speech (orders, requests, offers, advice) |

Mục tiêu kĩ năng (đọc, nói, nghe, viết, giao tiếp, văn hoá, dự án) của từng Unit nằm trong `objectives` của `lessons`. Mọi Unit đều kết thúc bằng một nhiệm vụ dự án/trình bày nhóm.

## 5. Sai lầm thường gặp của học sinh

SGV Tiếng Anh 12 không có mục riêng về lỗi sai của học sinh (giống `tieng_anh_10`). Dưới đây là các điểm dễ nhầm và lưu ý dạy học mà SGV nêu rõ. Cột Nguồn ghi trang in của SGV; trang PDF = trang in + 1.

| Chủ đề | Điểm dễ nhầm / lưu ý | Nguồn |
|---|---|---|
| Từ nhiều nghĩa (Unit 3) | HS đã học từ `waste` với một nghĩa; ở Glossary Unit 3 nghĩa là vật liệu không còn cần dùng, bị vứt đi (rác thải). Cần phân biệt các nghĩa của cùng một từ. | SGV tr.54 |
| Mệnh đề trạng ngữ chỉ kết quả (Unit 7) | Không dùng `so` với cụm danh từ bắt đầu bằng a(n). Câu hỏi sửa lỗi lấy lỗi này làm đáp án sai. | SGV tr.170 |
| Trọng âm trong lời nói liền (Unit 4–5) | Từ chức năng (mạo từ, giới từ, trợ động từ, động từ tình thái,...) thường không nhấn, nhưng trợ động từ và động từ tình thái **được nhấn** trong một số trường hợp (Unit 5). Không khái quát "luôn không nhấn". | SGV tr.98 (Unit 4), tr.106 (Unit 5) |
| Câu hỏi đọc hiểu nhiều lựa chọn (Unit 10) | Phải loại các phương án gây nhiễu: không được nhắc trong bài (irrelevant), không đúng theo bài (incorrect), quá hẹp, chỉ nêu một phần bài (too narrow). Câu hỏi có từ phủ định NOT: trước hết loại các phương án có thông tin được nêu trong bài. | SGV tr.229 |
| Bài tập ngữ pháp dạng đề thi (Unit 8, 10) | Xác định cấu trúc ngữ pháp đang được kiểm tra, rồi loại phương án sai ngữ pháp hoặc vô nghĩa; với câu tường thuật chọn câu không đổi nghĩa so với câu gốc. | SGV tr.190 (Unit 8), tr.238 (Unit 10) |
| Từ đồng nghĩa, trái nghĩa (Review 2, 3) | Dạng câu hỏi này xuất hiện trong đề thi tốt nghiệp THPT; HS nên học từ đồng nghĩa hoặc gần nghĩa và từ trái nghĩa theo cặp. | SGV tr.124 (Review 2), tr.195 (Review 3) |
| Nghe | Phương án trong đề thường **diễn đạt lại** (paraphrase) nội dung bài nghe, nên cần nghe từ đồng nghĩa hoặc cụm có nghĩa tương tự, và lời nói thể hiện thích, không thích, đồng ý, không đồng ý. | SGV tr.40 (Unit 2), tr.142 (Unit 6), tr.163 (Unit 7) |
| Viết | GV nên ghi lại các lỗi thường gặp trong bài viết của lớp, chép lên bảng ẩn danh rồi cho cả lớp sửa. | SGV tr.115 (Unit 5, viết thư xin việc) |
| Ghi chép | HS viết đáp án và ghi chú vào vở, **không** viết vào SGK. | SGV tr.7 |

Không có nguồn để nêu thêm sai lầm ngoài các điểm trên; các ô Remember!/Tips trong SGK đã được trích thành mục thuật ngữ (mục 1).

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- SGK là PDF dạng ảnh. Dữ liệu được đọc trực tiếp từ ảnh trang (90–150 dpi). Cache `.ocr/` được dựng bằng `eng+vie` (cả trang, 220 dpi, psm 3) rồi bổ sung OCR từng nửa trang/dải 300–400 dpi (psm 4, 6, 11) cho các trang Glossary (PDF 149–157) và một số bảng (PDF 11, 23, 35, 104). Xoá `.ocr/` thì `check_sources.py` sẽ OCR lại bằng `vie` và gắn cờ hàng loạt; khi đó phải dựng lại cache theo cách trên.
- Phiên âm IPA không được script kiểm tra (chỉ kiểm tra tên từ và nghĩa tiếng Việt); độ chính xác IPA dựa vào đọc ảnh và kiểm tra mẫu.
- Một số `definition` mục phát âm/bảng được viết lại theo thứ tự hàng của bảng sách và lược phiên âm để khớp OCR (`diphthongs`, `assimilation`). Nội dung từ ngữ không đổi.
- `definition` của các mục ngữ pháp là nguyên văn tiếng Anh của SGK; tên mục (ví dụ "present perfect with the first/the second time", "no article") là tên do người trích đặt, không có nguyên văn trong trang.

**Kiểm tra tự động** (2026-10-23, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py tieng_anh_12` | 0 lỗi; 284 mục |
| `check_sources.py tieng_anh_12` | 279 đạt, 5 gắn cờ (đều do OCR, đã đối chiếu ảnh), 0 không kiểm tra được, 7 cảnh báo tên (mục ngữ pháp do người trích đặt tên) |
| 5 cờ còn lại | `proportion` (OCR đọc "tỉ lệ" thành "tilệ"; ảnh PDF 152 ghi "tỉ lệ"); `facial-recognition` (tên bị ngắt thành hai dòng trong ô bảng, ảnh PDF 153 ghi "facial recognition (n)"); 3 mục `diphthongs-*` (chữ trắng/nhạt trên ô tô màu, OCR đọc không hết; đã đối chiếu từng hàng của bảng trên ảnh PDF 11, 23, 35) |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 23 ở lần chạy đầu (cache OCR `eng+vie` cả trang): do OCR đọc kém bảng nhiều cột tô màu. Bổ sung OCR nửa trang 300 dpi giảm còn 9, OCR dải 400 dpi còn 6, rồi còn 5 sau khi bỏ phiên âm khỏi `definition` của 3 mục `diphthongs-*` và `assimilation`. Không mục nào sai nội dung |

**Kiểm tra mẫu** (Giai đoạn 5, 2026-10-23, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/284 (10,6%) từ `query.py --sample 24 --seed 2026` (24 mục: 22 từ vựng Glossary, `verbs-with-prepositions`, `present-perfect-the-first-time`, `three-word-phrasal-verbs`, `diphthongs-oi-ai-and-au`) cộng 6 mục công thức/định nghĩa trọng tâm chọn thêm (`assimilation`, `active-causatives`, `double-comparatives`, `present-perfect-unique-experience`, `reported-speech-orders-requests-offers-advice`, `culture-shock-culture`) |
| Cách đối chiếu | Dựng lại ảnh các trang Glossary PDF 149, 150, 152, 153, 154, 156 (100 dpi) và so từng từ, loại từ, IPA, nghĩa của các mục mẫu; đối chiếu `definition`/`notation` của 8 mục ngữ pháp với ảnh trang nguồn (PDF 23, 36, 52, 81, 93, 104, 121, 133, 31) |
| Số mục sai nội dung | 0 |
| Kiểm tra độc lập | Chưa làm. Mục mẫu và toàn bộ bảng Glossary do cùng một phiên đọc và đối chiếu; nên có người kiểm tra độc lập (ưu tiên IPA, vì script không kiểm tra) |

## 7. Liên hệ với các lớp khác

`tieng_anh_10` và `tieng_anh_12` dùng chung cấu trúc dữ liệu nhưng không gộp mục. Năm mục lớp 12 đã nối `related_terms` sang mục lớp 10 tương ứng:
- `past-simple-vs-past-continuous` → `tieng-anh-10-past-simple-vs-past-continuous-with-when-and-while`.
- `present-perfect` → `tieng-anh-10-present-perfect` (lớp 12 thêm cấu trúc the first/the second time và trải nghiệm duy nhất).
- `sentence-stress-and-rhythm` → `tieng-anh-10-sentence-stress`, `tieng-anh-10-rhythm`.
- `intonation-in-questions` → `tieng-anh-10-intonation`.
- `reported-speech-orders-requests-offers-advice` → `tieng-anh-10-reported-speech` (lớp 12 mở rộng sang mệnh lệnh, yêu cầu, lời mời, lời khuyên).

Nội dung mới của lớp 12 (không có ở lớp 10): articles, causatives, adverbial clauses, relative clauses referring to a whole sentence, three-word phrasal verbs, assimilation, linking /r/, homophones. Khi làm Tiếng Anh 11, cân nhắc nối lại các mục lặp giữa ba lớp.
