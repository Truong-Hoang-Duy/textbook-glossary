# Glossary sách giáo khoa — hướng dẫn cho Claude (đọc đầu mỗi phiên)

Trả lời người dùng bằng **tiếng Việt**.

## 1. Mục đích

Xây dựng bộ thuật ngữ (định nghĩa, định lí, tính chất, công thức, kí hiệu, quy tắc) theo từng môn và lớp, trích từ PDF sách Kết nối tri thức. Glossary là **ground truth** cho agent sinh câu hỏi ôn tập/kiểm tra. Agent đó không được bịa định nghĩa.

## 2. Bộ (unit) và cấu trúc thư mục

**Bộ** = một môn của một lớp, tên `{mon}_{lop}`: viết thường, không dấu, nối bằng `_` (`toan_10`, `vat_ly_10`, `hoa_hoc_11`). `{mon}` là phần đứng trước số lớp.

Gốc dự án là thư mục `book/` này:

```
book/                         # GỐC
├── README.md, CLAUDE.md
├── sgk/                      # NGUỒN SÁCH PDF THEO KHỐI LỚP (chỉ đọc)
│   ├── khoi_10/              # Khối 10: toan_10/, hoa_10/, lich_su_10/, sinh_10/, ...
│   ├── khoi_11/              # Khối 11
│   └── khoi_12/              # Khối 12
└── glossary/                 # KẾT QUẢ
    ├── schema.json           # nguồn duy nhất về định dạng
    ├── tessdata/             # dữ liệu OCR tiếng Việt cho tesseract
    ├── scripts/              # add_terms.py, query.py, validate.py, check_sources.py, _common.py
    ├── dataset/              # TẬP TRUNG: chứa tất cả file JSON dữ liệu (<unit>.json)
    ├── khoi_10/              # Khối 10: toan_10/, hoa_10/, lich_su_10/, sinh_10/, ...
    │   └── toan_10/
    │       ├── toan_10.json  # dữ liệu: glossary/khoi_<lop>/<unit>/<unit>.json
    │       ├── progress.json # tiến độ + danh sách chương/bài CHUẨN
    │       ├── DESCRIPTION.md# mô tả bộ
    │       └── .ocr/         # cache OCR (tự sinh, xóa được)
    ├── khoi_11/              # Khối 11
    └── khoi_12/              # Khối 12
```

Mỗi bộ có **hai** bản lưu JSON: một bản nằm ở `glossary/khoi_<lop>/<unit>/<unit>.json` và một bản tập trung ở `glossary/dataset/<unit>.json` (được tự động đồng bộ khi chạy script). Không chia nhỏ theo chương hay bài. Nguồn của bộ `<unit>` nằm ở `sgk/khoi_<lop>/<unit>/`.

## 3. Đầu mỗi phiên

1. Xác định bộ đang làm. Hỏi người dùng nếu chưa rõ. **Chỉ làm một bộ mỗi phiên.**
2. Đọc `glossary/khoi_<lop>/<unit>/progress.json`, rồi `glossary/khoi_<lop>/<unit>/DESCRIPTION.md`.
3. Làm tiếp phần đang dở. Không làm lại phần đã `done`.
4. **Không mở cả file `<unit>.json` để đọc.** Dùng `query.py` để xem dữ liệu.
5. **Không sửa `<unit>.json` bằng tay.** Chỉ dùng `add_terms.py` (sửa thì thêm `--update`).
6. Cuối phiên: cập nhật `progress.json` (status, `terms_added`, `last_session_note`).

Các lệnh chạy từ thư mục gốc `book/`:

```
python glossary/scripts/add_terms.py <unit> <lo.json> [--update]
python glossary/scripts/query.py <unit|mon> [--lesson T] [--chapter T] [--type T] [--level L] [--q T] [--id ...] [--has-notes] [--fields a,b|all] [--sample N --seed S] [--count] [--format json|text|md] [--out FILE]
python glossary/scripts/query.py <unit> --audit [--seed S]   # xuất mẫu kiểm tra Giai đoạn 4 ra glossary/<unit>/sample_audit.md [--format json|text|md] [--audit] [--out file]
python glossary/scripts/validate.py [<unit>|<mon>]
python glossary/scripts/check_sources.py <unit> [--threshold 0.65] [--lesson T] [--id ...] [--no-accent] [--verbose]
```

File lô (`lo.json`) để ở scratchpad, không để trong `glossary/`.

## 4. Schema (tóm tắt — chi tiết ở `glossary/schema.json`)

`{ "meta": {unit, subject, subject_name, grade, last_updated, term_count}, "terms": [...] }`

Mỗi thuật ngữ có **đủ** các trường sau. Không thêm trường lạ: `additionalProperties: false`.

| Trường | Quy tắc |
|---|---|
| `id` | `{unit với _ đổi thành -}-{slug-khong-dau}`, ví dụ `toan-10-menh-de`, `vat-ly-10-...`. Phải duy nhất trong toàn môn, xuyên các lớp. Nếu trùng tên nhưng khác nghĩa thì thêm hậu tố ngữ cảnh, ví dụ `-hinh-hoc` |
| `term`, `aliases` | Tên thuật ngữ; `aliases` là mảng các tên khác (có thể rỗng) |
| `type` | `dinh_nghia` \| `dinh_ly` \| `tinh_chat` \| `cong_thuc` \| `ky_hieu` \| `quy_tac` |
| `definition` | **Bám sát nguyên văn sách.** Được rút gọn, nhưng không diễn giải sai, không thêm kiến thức ngoài sách. Công thức viết bằng LaTeX `$...$` |
| `notation` | Kí hiệu (LaTeX) hoặc `null` |
| `chapter`, `lesson` | **Đúng chuỗi trong `progress.json`**. Ví dụ `Chương I. Mệnh đề và tập hợp`, `Bài 1. Mệnh đề`, `Chuyên đề 1. ...` |
| `level` | `co_ban` (SGK, SBT) \| `chuyen_de` (SCD) |
| `related_terms` | Các `id` đã tồn tại trong toàn môn, kể cả bộ khác |
| `sources` | Mảng `{book_type: sgk/scd/gv/sbt, file, pdf_page, printed_page}`. **`pdf_page` là số thứ tự trang trong file PDF và phải đúng thật**; `printed_page` là số in trên trang, hoặc `null` |
| `notes` | Ghi khi **không chắc** (chữ mờ, công thức khó đọc, định nghĩa bị ngắt trang...); nếu chắc thì để `null` |

**Quy tắc chống bịa:**
- Chỉ trích những gì sách **nêu rõ** là định nghĩa, khái niệm, định lí, tính chất, công thức, kí hiệu hoặc quy tắc. Không lấy ví dụ, bài tập, lời giải, hoạt động khám phá.
- Không dựa vào trí nhớ. Mỗi mục phải đọc từ trang nguồn và có số trang thật.
- Sách dạng ảnh thì đọc trang dưới dạng ảnh (render PyMuPDF khoảng 130–150 dpi). Có thể dùng cache OCR để tham khảo, nhưng **ảnh là chuẩn**.
- Không chắc thì ghi `notes`, không đoán.
- Sách có bản quyền, chỉ dùng nội bộ. Trích ngắn kèm nguồn, không chép đoạn dài.

## 5. Vai trò từng loại sách

Thứ tự ưu tiên khi xung đột định nghĩa: **SGK > SCD > Tài liệu GV > SBT**.

| Loại | Dùng để |
|---|---|
| SGK | Nguồn chính, `level: co_ban` |
| SCD | Khái niệm nâng cao/mở rộng, `level: chuyen_de` |
| SGV / Tài liệu GV | Bắt buộc đọc. Ghi mục tiêu, yêu cầu cần đạt (DESCRIPTION mục 4) và sai lầm thường gặp của học sinh (mục 5). Bổ sung nguồn `gv` cho thuật ngữ đã có (xem dưới) |
| SBT | Chỉ bổ sung khái niệm SGK chưa có. Không trích đề bài |

Trong cùng một bộ, nếu một khái niệm xuất hiện ở nhiều sách thì **gộp thành một mục**: giữ định nghĩa của sách ưu tiên cao hơn và thêm nguồn vào `sources`.

**Nhận diện loại sách theo tên file** (`validate.py` kiểm tra tự động):

| Tiền tố tên file | `book_type` | `level` |
|---|---|---|
| `SGK …` | `sgk` | `co_ban` |
| `SBT …` | `sbt` | `co_ban` |
| `SCD …` | `scd` | `chuyen_de` |
| `SGV CD …` (SGV Chuyên đề, ví dụ `SGV CD TOAN 10.pdf`) | `gv` | `chuyen_de` |
| `SGV …` (ví dụ `SGV SINH HOC 10.pdf`) | `gv` | `co_ban` |
| `Tài liệu bồi dưỡng GV …` | `gv` | `co_ban` |
| `Slide tập huấn …` (slide tập huấn GV, coi như Tài liệu bồi dưỡng GV) | `gv` | `co_ban` |

**Quy tắc đọc SGV / Tài liệu GV:**
1. Luôn thêm mọi file SGV và Tài liệu GV của bộ vào `books` trong `progress.json`. SGV đi theo bài nên điền chương/bài giống sách học sinh tương ứng: SGV → SGK, SGV CD → SCD. Nhờ vậy tiến độ đọc được theo dõi từng bài. Tài liệu bồi dưỡng GV có thể để `chapters: {}`.
2. Bắt buộc trích từ SGV vào `DESCRIPTION.md`: mục tiêu và yêu cầu cần đạt theo chương/bài (mục 4); sai lầm thường gặp của học sinh, kèm file và trang PDF (mục 5).
3. Khi SGV giải thích rõ một thuật ngữ đã có, **thêm nguồn `gv`** vào `sources` của thuật ngữ đó bằng `add_terms.py --update`. Áp dụng cho hai trường hợp: SGK chưa nêu rõ định nghĩa, hoặc định nghĩa cần chuẩn hoá về mặt sư phạm. `definition` vẫn giữ theo sách ưu tiên cao nhất (SGK > SCD > GV > SBT). Chỉ khi SGK/SCD không có phát biểu tường minh thì `definition` mới lấy theo SGV, và khi đó nguồn `gv` đứng đầu `sources`.
4. Không tạo thuật ngữ mới chỉ từ SGV nếu khái niệm đó không xuất hiện trong sách học sinh của bộ.

## 6. Khái niệm lặp giữa các lớp

**Không gộp giữa các lớp.** Ví dụ "hàm số" ở Toán 10 và Toán 12 là hai thuật ngữ riêng (`toan-10-ham-so`, `toan-12-ham-so`), mỗi cái theo định nghĩa của sách lớp đó, nối nhau bằng `related_terms`.

## 7. Đảm bảo chất lượng

- Sau **mỗi sách**: chạy `validate.py <unit>` và `check_sources.py <unit>`. Xử lý ngay các mục gắn cờ: mở lại đúng trang nguồn dưới dạng ảnh, rồi sửa bằng `add_terms.py --update` hoặc ghi `notes`.
- `check_sources.py` so khớp **có dấu tiếng Việt** với text trang (text layer hoặc OCR tesseract `vie`, cache ở `glossary/khoi_<lop>/<unit>/.ocr/`). Độ đo chính là tỉ lệ **cặp từ liên tiếp (bigram)**, ngưỡng 0.65 (chọn từ thí điểm: dữ liệu đúng ≥ 0.70, sai trang/bịa phần lớn < 0.5). Tên thuật ngữ được so cả bản bỏ khoảng trắng (chịu lỗi OCR dính chữ). Với `cong_thuc`/`quy_tac`/`ky_hieu`/`tinh_chat`, tên không có nguyên văn trong trang chỉ là cảnh báo. Script chỉ phát hiện định nghĩa bịa hoặc sai trang, không phát hiện sai sót nhỏ trong công thức.
- File dữ liệu được `add_terms.py` ghi theo dạng mỗi thuật ngữ một dòng (tự động đồng bộ vào cả thư mục bộ và `glossary/dataset/`; thư mục `dataset/` chỉ lưu file `.json`, không chứa file `.bak`).
- Khi xong một bộ: **kiểm tra mẫu độc lập ở một phiên mới**. Chạy lệnh kiểm định chuyên dụng để tự động xuất file mẫu:
  `python glossary/scripts/query.py <unit> --audit`
  Lệnh này tự động chọn đúng 30 mục chuẩn (20 mục ngẫu nhiên seed 2026 + 10 mục công thức/kí hiệu) và xuất ra file `glossary/khoi_<lop>/<unit>/sample_audit.md` chuẩn UTF-8.
  Người kiểm tra mở `sample_audit.md` trong VS Code (nhấn `Ctrl + Shift + V` để xem trực quan), đối chiếu trực tiếp với trang nguồn **dưới dạng ảnh** và so với `definition`/`notation`. Nếu tỉ lệ sai > 5% thì DỪNG và báo người dùng. Xong kiểm tra thì xóa file `sample_audit.md`.
- **Không tự ý đổi schema.** Phải hỏi người dùng trước. Khi được đồng ý: sửa `schema.json`, cập nhật dữ liệu của **tất cả** các bộ trong cùng một lần, rồi chạy `validate.py` (không tham số) đến khi sạch.

## 8. Thêm bộ mới (ví dụ `toan_11`)

1. Đặt PDF vào `sgk/khoi_11/toan_11/`.
2. Tạo `glossary/khoi_11/toan_11/` gồm:
   - `toan_11.json`: `{"meta": {"unit": "toan_11", "subject": "toan", "subject_name": "Toán", "grade": 11, "last_updated": "...", "term_count": 0}, "terms": []}`
   - `progress.json`: điền chương/bài theo mục lục, mỗi bài có `status` và `pdf_pages`. Liệt kê **mọi** PDF của bộ, kể cả SGV và Tài liệu GV (xem mục 5).
   - `DESCRIPTION.md`: dùng khung giống `toan_10`.
   Đồng thời copy/tạo sẵn một bản `toan_11.json` vào `glossary/dataset/toan_11.json`.
3. Thêm một dòng vào bảng trạng thái bên dưới. Các script dùng chung, không cần sửa.

## 9. Trạng thái các bộ

| Bộ | Trạng thái | Ghi chú |
|---|---|---|
| `toan_10` | Đã kiểm tra cuối (197 mục; mẫu 30 mục, 0 sai — 2026-10-14) | Sách dạng ảnh; trang PDF = trang in + 1 |
| `sinh_10` | Đã kiểm tra cuối (299 mục; mẫu 30 mục, 0 sai sau khi sửa 1 lỗi kí hiệu — 2026-10-14) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1 |
| `ngu_van_10` | Đã kiểm tra cuối (191 mục; mẫu 30 mục, 0 sai — 2026-10-14; chờ kiểm tra độc lập) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; không chia chương: `chapter` = `Tập một`/`Tập hai` hoặc `Chuyên đề N. …`, `lesson` = `Bài N. …`/`Phần N. …` |
| `tieng_anh_10` | Đã kiểm tra cuối (261 mục; mẫu 30 mục, 0 sai — 2026-10-14; chờ kiểm tra độc lập) | Sách Global Success, dạng ảnh (trừ Slide tập huấn); trang PDF = trang in + 1; `chapter` = `Unit N. …`/`Review N`, `lesson` = `Lesson N. …` hoặc `Glossary`; từ vựng: nghĩa tiếng Việt ở `definition`, loại từ + IPA ở `notation`; cache `.ocr/` dựng bằng `eng+vie` |
| `vat_ly_10` | Đã kiểm tra cuối (241 mục; mẫu 30 mục, 1 sai đã sửa — 2026-10-15) | Sách dạng ảnh (Tài liệu GV có text layer nhưng lỗi font); trang PDF = trang in + 1; SBT chỉ có bài tập (0 mục) |
| `hoa_10` | Đã kiểm tra cuối (194 mục; mẫu 30 mục, 0 sai — 2026-10-15) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; SGK có phần `Mở đầu` không đánh số bài (`chapter` = `lesson` = `Mở đầu`) |
| `tin_hoc_10` | Đã kiểm tra cuối (266 mục; mẫu 30 mục, 2 sai đã sửa — 2026-10-15) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; 2 SCD (KHMT: robot; ICT: văn phòng) đều có `Chuyên đề 1–3`, SCD ICT đánh lại `Bài 1` mỗi chuyên đề — lọc kèm `--chapter`; ICT bỏ Bài 3–6, CS bỏ Bài 12–15 |
| `lich_su_10` | Đã kiểm tra cuối (261 mục; mẫu 30 mục, 0 sai — 2026-10-16; chờ kiểm tra độc lập) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; `chapter` = `Chủ đề N. …`/`Chuyên đề N. …`, SCD `lesson` = mục `I.`/`II.`/`III.`; không có công thức/kí hiệu — `--audit` dùng kèm `--sample 30` |
| `dia_10` | Đã kiểm tra cuối (294 mục; mẫu 30 mục, 1 sai đã sửa — 2026-10-16; chờ kiểm tra độc lập) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; `chapter` = `Phần một. …`/`Chương N. …`/`Chuyên đề 10.N. …`, SCD `lesson` = mục `I.`–`IV.`; SBT 0 mục |
| `am_nhac_10` | Đã kiểm tra cuối (116 mục; mẫu 37 mục, 0 sai — 2026-10-16) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; không có SBT; SGK `chapter` = `Chủ đề N. …`/`Phương án lựa chọn A. Hát`/`B. Nhạc cụ`, `lesson` = mạch nội dung (`Lí thuyết âm nhạc`, `Thưởng thức âm nhạc`, …) hoặc `Bài N. …` (A và B đều có Bài 1–… — lọc kèm `--chapter`); không có công thức — `--audit` dùng kèm `--sample 30` |
| `cong_nghe_cong_nghiep_10` | Đã kiểm tra cuối (173 mục; mẫu 30 mục, 0 sai — 2026-10-17) | Sách dạng ảnh (trừ Tài liệu GV); trang PDF = trang in + 1; không có SBT |
| `cong_nghe_nong_nghiep_10` | Đã kiểm tra cuối (240 mục; mẫu 23 mục, 0 sai — 2026-10-16) | Sách dạng ảnh (trừ Tài liệu GV); SGK trang PDF = trang in + 1, SCD trang PDF = trang in; không có SBT |
| `sinh_11` | Đã kiểm tra cuối (191 mục; mẫu 24 mục, 0 sai sau khi sửa 4 lỗi LaTeX — 2026-10-17) | Sách dạng ảnh; trang PDF = trang in + 1 |
| `hoa_11` | Đã kiểm tra cuối (153 mục; mẫu 30 mục, 0 sai — 2026-10-17) | Sách dạng ảnh; trang PDF = trang in + 1 |
| `sinh_12` | Đã kiểm tra cuối (164 mục; mẫu 27 mục, 0 sai — 2026-10-17) | Sách dạng ảnh; SGK trang PDF = trang in + 2, SCD trang PDF = trang in + 2 (phần lớn) |

Trạng thái: chưa bắt đầu / đang trích xuất / đã kiểm tra cuối.

## 10. Agent sinh câu hỏi dùng glossary thế nào

- Dùng `query.py` lọc theo lớp/bài/chương cần ra đề, ví dụ `query.py toan_10 --lesson "Bài 1." --level co_ban`. **Không nạp cả file.**
  SGK và Chuyên đề đều đánh số "Bài 1, 2, …", nên khi lọc theo bài luôn kèm `--level` hoặc `--chapter`.
- Định nghĩa dùng trong câu hỏi phải khớp `definition` của **đúng lớp đang ra đề**.
- Dữ liệu đã qua kiểm tra tự động và kiểm tra mẫu, nên không cần rà soát lại từng mục. Khi cần chắc chắn tuyệt đối về công thức hoặc định lí, đối chiếu lại trang nguồn trong `sources`.
- Mục có `notes` (lọc bằng `--has-notes`) coi là **chưa chắc chắn**, tránh dùng làm đáp án.
