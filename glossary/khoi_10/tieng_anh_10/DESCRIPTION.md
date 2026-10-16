# Bộ thuật ngữ `tieng_anh_10` — Tiếng Anh 10 Global Success (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_10/tieng_anh_10/tieng_anh_10.json` (tập trung: `glossary/dataset/tieng_anh_10.json`), gồm **261 mục** (cập nhật 2026-10-14). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_10/tieng_anh_10/`, bộ Tiếng Anh 10 Global Success (NXB Giáo dục Việt Nam – Pearson).

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Tieng Anh 10 Global Success.pdf | sgk | 132 | Nguồn chính, `level: co_ban`: bảng Glossary cuối sách, ô Remember!/Tips ở phần Language, định nghĩa nêu tường minh trong bài Reading/CLIL | Không (ảnh, OCR) |
| SGV TIENG ANH 10 Global Success.pdf | gv | 226 | Mục tiêu từng Unit (mục 4), lưu ý dạy học (mục 5); nguồn `gv` phụ cho 9 mục; định nghĩa của 1 mục (`rhythm`) | Không (ảnh, OCR) |
| SBT TIENG ANH 10 Global Success.pdf | sbt | 118 | Đã rà soát toàn bộ: chỉ có bài tập và đáp án, không có khái niệm mới (0 mục) | Không (ảnh, OCR) |
| Slide tập huấn TA10 - Global Success.pptx.pdf | gv | 56 | Slide tập huấn GV: yêu cầu kiến thức ngôn ngữ, kĩ năng, phân phối tiết (mục 4). Không thêm nguồn cho mục nào | Có |

- Ở cả ba sách dạng ảnh: **trang PDF = trang in + 1**.
- `classify_book` (`_common.py`) được bổ sung tiền tố `Slide tập huấn …` → `gv/co_ban` (coi như Tài liệu bồi dưỡng GV) để không phải đổi tên file nguồn; README mục 5 đã ghi thêm dòng này.
- **Cấu trúc `chapter`/`lesson`:** `chapter` = `Unit N. <Tên unit>` (10 unit) hoặc `Review N`; `lesson` = 8 tiết chuẩn của mỗi unit theo SGV (`Lesson 1. Getting started`, `Lesson 2. Language`, `Lesson 3. Reading`, `Lesson 4. Speaking`, `Lesson 5. Listening`, `Lesson 6. Writing`, `Lesson 7. Communication and culture / CLIL`, `Lesson 8. Looking back and project`) cộng `Glossary` (bảng từ vựng cuối SGK, tr.124–131). Review chia `Language`/`Skills`. Ví dụ lọc: `--chapter "Unit 5."`, `--chapter "Unit 5." --lesson Glossary`, `--lesson "Lesson 2."`.
- **Ba nhóm mục:**
  1. **Từ vựng (217 mục, lesson `Glossary`)**: mỗi dòng của bảng Glossary là một mục `dinh_nghia`. `term` = từ/cụm từ tiếng Anh; `definition` = nghĩa tiếng Việt **đúng nguyên văn** bảng; `notation` = loại từ + phiên âm IPA như sách, ví dụ `(n) /ˈbenɪfɪt/` (mục không ghi loại từ thì chỉ có IPA: `3D printing`, `moon-shaped lute`, `AI`, `RAM`). Phiên âm chép theo sách, kể cả chỗ sách khác từ điển (`/rɪsˈpɒnsəbl/`, `/ɪksˈplɔː/`); kí tự nối `ʧ`/`ʤ` của sách được viết thành `tʃ`/`dʒ`. Từ viết tắt có tên đầy đủ trong ngoặc (`AI`, `RAM`) thì tên đầy đủ để ở `aliases`.
  2. **Ngữ pháp và phát âm (34 mục, chủ yếu `Lesson 2. Language`)**: chép từ ô **Remember!** (ngữ pháp, ngữ điệu) và **Tips** (trọng âm, hậu tố tính từ) bằng tiếng Anh, giữ nguyên câu ví dụ của sách. Cấu trúc công thức (`have / has + past participle`, `Modal + be + past participle`, `If + past simple, ... (would) ...`) để ở `notation`. Phần phát âm không có quy tắc (chỉ có bảng từ Listen and repeat) được ghi dạng `ky_hieu` kèm danh sách từ của sách và `notes` nói rõ SGK không nêu quy tắc.
  3. **Định nghĩa tiếng Anh trong bài đọc/CLIL (10 mục)**: các câu định nghĩa tường minh ("X is …") ở Reading/CLIL: `carbon-footprint-clil`, `ai-reading`, `processor-clil`, `ram-clil`, `storage-space-clil`, `global-warming`, `mass-tourism`, `ecotourism-clil`, `sustainable-tourism`, `responsible-tourism`. Với từ đã có trong Glossary thì giữ **hai mục** (nghĩa tiếng Việt ở Glossary và định nghĩa tiếng Anh ở bài học), nối nhau bằng `related_terms`, theo tiền lệ `nhan-vat`/`nhan-vat-van-hoc` của `ngu_van_10`.
- Không trích: hội thoại, bài đọc, đề bài và đáp án, bài "Match the words with their meanings" (là bài tập ghép nghĩa), Everyday English (mẫu câu giao tiếp), Tips kĩ năng (ví dụ cách làm bài điền sơ đồ, tr.57), tên tổ chức (UN, WWF, Save the Children…).
- Từ lặp trong Glossary ở hai unit được tách mục, mục sau thêm hậu tố unit: `communicate` (Unit 5) / `communicate-unit-8`, `practical` (Unit 4) / `practical-unit-9`.

## 2. Bài và số thuật ngữ

| Chapter | Glossary | Lesson 2. Language | Lesson khác | Ghi chú |
|---|---|---|---|---|
| Unit 1. Family life | 21 | 3 | | /br/ /kr/ /tr/; present simple vs. present continuous |
| Unit 2. Humans and the environment | 23 | 4 | Lesson 7: 1 | /kl/ /pl/ /gr/ /pr/; will / be going to; passive voice; CLIL carbon footprint |
| Unit 3. Music | 20 | 3 | | trọng âm từ 2 âm tiết; compound sentences; to-infinitives và bare infinitives |
| Unit 4. For a better community | 22 | 2 | Lesson 1: 2 | hậu tố tính từ (-ful/-less, -ed/-ing, Tips ở Getting started); trọng âm từ 2 âm tiết cùng chính tả; past simple vs. past continuous với when/while |
| Unit 5. Inventions | 28 | 4 | Lesson 3: 1; Lesson 7: 3 | trọng âm danh từ 3 âm tiết; present perfect; gerunds; to-infinitives; AI; computer hardware |
| Unit 6. Gender equality | 21 | 2 | | trọng âm tính từ, động từ 3 âm tiết; passive voice with modals |
| Unit 7. Viet Nam and international organisations | 21 | 4 | | trọng âm phụ; trọng âm từ trên 3 âm tiết; comparative, superlative adjectives |
| Unit 8. New ways to learn | 18 | 4 | | sentence stress; relative clause, defining / non-defining |
| Unit 9. Protecting the environment | 20 | 3 | Lesson 3: 1 | rhythm (định nghĩa theo SGV); reported speech; reported questions; global warming |
| Unit 10. Ecotourism | 23 | 3 | Lesson 7: 4 | intonation; conditional sentences Type 1, Type 2; mass / eco- / sustainable / responsible tourism |

Review 1–4, Lesson 4–6 và Lesson 8 không có khái niệm mới (0 mục). Glossary theo trang PDF: Unit 1 tr.125; Unit 2 tr.125–126; Unit 3 tr.126; Unit 4 tr.127; Unit 5 tr.128; Unit 6 tr.129; Unit 7 tr.129–130; Unit 8 tr.130–131; Unit 9 tr.131; Unit 10 tr.132.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 234 (217 từ vựng Glossary + 7 định nghĩa ngữ pháp/phát âm + 10 định nghĩa bài đọc/CLIL) |
| quy_tac | 19 |
| ky_hieu | 5 |
| cong_thuc | 3 |
| dinh_ly, tinh_chat | 0 |

- Theo `level`: `co_ban` 261 (bộ không có sách chuyên đề).
- Theo nguồn định nghĩa: SGK 260, SGV 1 (`rhythm`). Có 9 mục mang thêm nguồn `gv` (SGV giải thích rõ hơn): `passive-voice`, `passive-voice-with-modals`, `adjective-suffixes-ful-less`, `stress-in-three-syllable-nouns`, `stress-in-three-syllable-adjectives-and-verbs`, `comparative-adjectives`, `reported-speech`, `intonation`, `ai-reading`.
- 228 mục có `notation` (217 phiên âm từ vựng + 11 công thức/kí hiệu).
- 6 mục có `notes`: 5 mục phát âm SGK chỉ đưa bảng từ, không nêu quy tắc (`consonant-blends-br-kr-tr`, `consonant-blends-kl-pl-gr-pr`, `stress-in-three-syllable-nouns`, `stress-in-three-syllable-adjectives-and-verbs`, `stress-in-words-with-more-than-three-syllables`) và `rhythm` (định nghĩa lấy từ SGV). Agent **không** được tự suy ra quy tắc trọng âm cho các mục này.

## 4. Yêu cầu cần đạt theo bài

Nguồn: mục "OBJECTIVES" đầu mỗi unit trong SGV (trang in = trang PDF − 1), yêu cầu kiến thức ngôn ngữ và phân phối tiết trong Slide tập huấn (tr.8, 31). Trích rút gọn phần ngôn ngữ.

**Phân phối chương trình** (Slide tập huấn tr.31): 35 tuần × 3 tiết = 105 tiết; 8 tiết/unit × 10 unit = 80 tiết; ôn tập 2 tiết × 4 Review = 8 tiết; kiểm tra giữa kì, cuối kì 8 tiết; ôn tập kiểm tra học kì 4 tiết; dự phòng 5 tiết.

**Yêu cầu kiến thức ngôn ngữ cả năm** (Slide tập huấn tr.8): Ngữ âm: 7 tổ hợp phụ âm /tr/, /kr/, /br/, /kl/, /pl/, /gr/, /pr/; trọng âm từ 2 âm tiết, 3 âm tiết, trên 3 âm tiết; trọng âm câu, nhịp điệu, ngữ điệu. Từ vựng: 200–250 từ thông dụng theo chủ đề. Ngữ pháp: hiện tại đơn, hiện tại tiếp diễn, hiện tại hoàn thành, tương lai đơn, quá khứ đơn, quá khứ tiếp diễn, động từ nguyên thể, danh động từ, câu bị động, câu ghép, mệnh đề quan hệ, câu điều kiện, so sánh hơn và so sánh nhất, mạo từ…; giới thiệu quá khứ đơn/quá khứ tiếp diễn với when, while, câu bị động với động từ tình thái, câu điều kiện loại 2, câu tường thuật, tính từ chỉ thái độ.

| Unit | SGV (trang in) | Ngữ âm | Từ vựng | Ngữ pháp |
|---|---|---|---|---|
| 1. Family life | tr.7 | phát âm đúng /br/, /kr/, /tr/ trong từ và câu | family life | present simple (việc lặp lại thường xuyên ở hiện tại) và present continuous (việc đang diễn ra lúc nói) |
| 2. Humans and the environment | tr.28 | /kl/, /pl/, /gr/, /pr/ | human activities and the environment | will và be going to nói về tương lai; passive voice |
| 3. Music | tr.47 | trọng âm từ 2 âm tiết | music | dùng liên từ tạo compound sentences; to-infinitives và bare infinitives sau một số động từ |
| 4. For a better community | tr.70 | trọng âm từ 2 âm tiết cùng chính tả | community development; hậu tố -ed/-ing, -ful/-less | past simple và past continuous với when, while |
| 5. Inventions | tr.89 | trọng âm danh từ 3 âm tiết thông dụng | inventions | present perfect, gerunds, to-infinitives |
| 6. Gender equality | tr.114 | trọng âm tính từ và động từ 3 âm tiết | gender equality | passive voice with modals |
| 7. Viet Nam and international organisations | tr.134 | trọng âm từ trên 3 âm tiết | international organisations | comparative và superlative adjectives |
| 8. New ways to learn | tr.153 | nhận biết, dùng đúng sentence stress | different ways of learning | defining và non-defining relative clauses với who, that, which, whose |
| 9. Protecting the environment | tr.178 | dùng sentence stress để nói đúng rhythm | the environment and ways to protect it | reported speech |
| 10. Ecotourism | tr.198 | nhận biết, dùng đúng intonation (giọng lên/xuống) | ecotourism | conditional sentences Type 1 và Type 2 |

**Giới hạn và trọng tâm theo SGV.** Agent sinh câu hỏi lưu ý:
- Trọng âm từ trên 3 âm tiết: HS **chỉ cần đánh dấu trọng âm chính** (primary stress); trọng âm phụ chỉ là thử thách cho lớp khá (SGV tr.138).
- Reported speech: quy tắc không lùi thì khi nội dung vẫn đúng, và việc might, could, would, should, ought to không đổi, chỉ dạy cho **lớp khá** (SGV tr.184). Đề cơ bản nên theo quy tắc đổi đại từ, thì, trạng từ thời gian của SGK.
- Từ cùng chính tả đổi trọng âm theo từ loại: các cặp conduct, conflict, content, contract, desert, produce, progress là phần mở rộng cho lớp khá (SGV tr.74), không có trong SGK.
- Ngữ điệu: chương trình chỉ yêu cầu 3 mẫu (câu trần thuật và câu hỏi Wh- xuống giọng, câu hỏi Yes-No lên giọng). Giọng lên ở cụm mở đầu (Well, So, When travelling…) chỉ là giải thích thêm trong phần Looking back (SGV tr.215).
- Mạo từ và tính từ chỉ thái độ có trong yêu cầu chương trình (Slide tr.8) nhưng **SGK 10 không có ô Remember! nào** cho hai mục này, nên glossary không có mục tương ứng.

## 5. Sai lầm thường gặp của học sinh

SGV không có mục riêng về lỗi sai. Dưới đây là các điểm dễ nhầm do SGK (Note/Tips) và SGV nêu rõ. Cột Nguồn ghi trang in; trang PDF = trang in + 1.

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Present continuous (Unit 1) | Dùng thì tiếp diễn với động từ chỉ trạng thái (like, love, need, want, know, agree…). | SGK tr.10 (Note) |
| Will / be going to (Unit 2) | Nhầm hai cách: will cho kế hoạch quyết định ngay lúc nói và dự đoán theo suy nghĩ; be going to cho kế hoạch có trước lúc nói và dự đoán dựa vào điều nhìn thấy/biết. Cả hai đều dùng để dự đoán. | SGK tr.20; SGV tr.33 |
| Passive voice (Unit 2, 6) | Quên dạng be + past participle; ghi thừa "by them/by us". Khi chủ ngữ câu chủ động là they hoặc we thì không cần nêu tác nhân. Với động từ tình thái: Modal + be + past participle. | SGV tr.34, 119 |
| Hậu tố tính từ (Unit 4) | Ghép tuỳ tiện -ful/-less: không phải từ nào cũng có cả hai dạng (không nói *successless*, mà nói *unsuccessful*). Nhầm -ed (cảm giác của người) với -ing (vật/người gây ra cảm giác). | SGV tr.72; SGK tr.43 |
| Trọng âm từ cùng chính tả (Unit 4) | Mặc định mọi từ vừa là danh từ vừa là động từ đều đổi trọng âm. Có từ không đổi: an 'answer / to 'answer, a 'picture / to 'picture. | SGK tr.43 (Note) |
| When / while (Unit 4) | Ghép sai thì: when đi với past simple (hành động ngắn xen vào), while đi với past continuous (hành động dài đang diễn ra). | SGV tr.73, 76; SGK tr.44 |
| Gerund / to-infinitive (Unit 3, 5) | Nhầm động từ theo sau: avoid, enjoy, finish + V-ing; want, decide, allow + to V; make, let, hear, notice + V nguyên thể không to. like, love, hate dùng được cả hai dạng. | SGK tr.30, 54 (Note) |
| So sánh (Unit 7) | Không nhận ra less / the least là dạng so sánh của little, dùng với tính từ dài (less / the least interesting). | SGV tr.139 |
| Trọng âm 3 âm tiết trở lên (Unit 5–7) | HS lớp yếu đặt sai trọng âm vì chưa tách được âm tiết; SGV yêu cầu tách âm tiết trước (cel/e/brate, in/ter/na/tion/al). | SGV tr.118, 138 |
| Sentence stress (Unit 8) | Nhấn cả từ chức năng (we, the, for); chỉ nhấn từ nội dung (động từ chính, danh từ, tính từ, trạng từ). | SGV tr.156; SGK tr.87 (Tips) |
| Rhythm (Unit 9) | Ảnh hưởng tiếng mẹ đẻ: tiếng Việt là ngôn ngữ thanh điệu, từ nào cũng được nhấn, trong khi nhịp tiếng Anh dựa trên sự xen kẽ âm tiết nhấn/không nhấn; nguyên âm không nhấn thường đọc thành /ə/. | SGV tr.182 |
| Conditional Type 2 (Unit 10) | Băn khoăn was/were: sau If trong câu điều kiện loại 2 có thể dùng were thay cho was (If I were a bird…). | SGK tr.112 (Note) |
| Reported questions (Unit 9) | Giữ trật tự câu hỏi và dấu hỏi khi tường thuật; phải dùng ask, trật tự câu trần thuật, bỏ dấu hỏi, câu hỏi Yes/No dùng if. | SGK tr.102 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- SGK, SGV, SBT là PDF dạng ảnh. Dữ liệu được đọc trực tiếp từ ảnh trang (100–220 dpi). `check_sources.py` mặc định OCR bằng `vie` nên đọc rất kém chữ tiếng Anh (ví dụ "presenf", "†he"). Vì vậy cache `.ocr/` của 89 trang nguồn được tạo lại bằng `eng+vie` (psm 3, cả trang) ghép với OCR từng nửa trang (psm 6, psm 4). Các trang Glossary (PDF 125–132) được ghép thêm OCR `vie` thuần (psm 6/4, từng nửa trang) và OCR riêng cột nghĩa ở 400 dpi. Xoá `.ocr/` thì script sẽ OCR lại bằng `vie` và gắn cờ lại hàng loạt; khi đó phải dựng lại cache theo cách trên.
- Phiên âm IPA không được script kiểm tra (chỉ kiểm tra tên từ và nghĩa tiếng Việt); độ chính xác IPA dựa vào đọc ảnh và kiểm tra mẫu.
- Một số `definition` của mục phát âm/ngữ pháp có bảng được viết lại theo thứ tự **hàng** của bảng trong sách (ví dụ `(table rows /br/ - /kr/ - /tr/): breadwinner crash track; …`), để khớp cách OCR đọc bảng. Nội dung không đổi.
- Định nghĩa tiếng Anh là nguyên văn sách; câu dẫn "Stress in …", "Consonant blends …" là tên mục do người trích đặt.
- Nguồn `gv` (9 mục) chỉ được kiểm tra sự có mặt của tên thuật ngữ, không kiểm tra bigram (định nghĩa giữ theo SGK).

**Kiểm tra tự động** (2026-10-14, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py tieng_anh_10` | 0 lỗi; 261 mục |
| `check_sources.py tieng_anh_10` | 259 đạt, 2 gắn cờ (lỗi dấu OCR, đã đối chiếu ảnh), 0 không kiểm tra được, 2 cảnh báo tên (`adjective-suffixes-ful-less` ở nguồn SGV, `reported-questions`) |
| 2 cờ còn lại | `boost` (OCR "thúc đấy", ảnh tr.126 ghi "thúc đẩy") và `operation` (OCR "cuộcphấu", ảnh tr.128 ghi "cuộc phẫu thuật"). Cả hai đạt bigram 1.00 khi chạy `--no-accent` |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 68 ở lần chạy đầu: khoảng 40 do OCR `vie` đọc sai chữ tiếng Anh (dựng lại cache `eng+vie`); 20 mục Glossary do tiền tố loại từ "(n)/(adj)" trong `definition` làm hỏng bigram của nghĩa ngắn (chuyển loại từ sang `notation`); 4 mục bảng phát âm do thứ tự cột/hàng (viết lại theo hàng); `rhythm` do script luôn so với nguồn SGK trước (bỏ nguồn SGK, ghi trang SGK trong `notes`); 4 mục lỗi dấu OCR (thêm OCR `vie` cột nghĩa). Không mục nào sai nội dung |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-14, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/261 (11,5%) từ `query.py --audit` (seed 2026): 25 từ vựng Glossary, 3 định nghĩa/quy tắc, 2 định nghĩa CLIL |
| Cách đối chiếu | 25 mục Glossary: cắt đúng dòng bảng ở 200–220 dpi, so từ, loại từ, IPA, nghĩa. 5 mục câu chữ: so từng từ với OCR `eng` (difflib), mọi chênh lệch đọc lại trên ảnh. Ngoài mẫu: so từng từ cả 44 mục không thuộc Glossary với OCR `eng`, chênh lệch đều là nhiễu OCR hoặc do sắp lại bảng |
| Số mục sai nội dung | 0 |
| Kiểm tra độc lập | **Chưa làm.** Chờ người dùng đối chiếu `sample_audit.md` với ảnh trang nguồn ở phiên riêng, sau đó xoá file |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Tiếng Anh 11 và 12. Các nội dung dự kiến được mở rộng ở lớp sau:
- Trọng âm từ (Unit 3–7), sentence stress, rhythm, intonation (Unit 8–10) → trọng âm và ngữ điệu nâng cao.
- Passive voice, passive with modals (Unit 2, 6) → các dạng bị động khác.
- Relative clauses (Unit 8) → rút gọn mệnh đề quan hệ.
- Reported speech (Unit 9), conditional Type 1–2 (Unit 10) → tường thuật câu mệnh lệnh, điều kiện loại 3, câu điều kiện hỗn hợp.
- Gerunds / to-infinitives (Unit 3, 5) → các động từ có nghĩa khác nhau khi theo sau là V-ing hoặc to V.
