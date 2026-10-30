# Học liệu SGK Kết nối tri thức — hướng dẫn cho Claude (đọc đầu mỗi phiên)

Trả lời người dùng bằng **tiếng Việt**.

## 1. Mục đích

Dựng từ PDF sách Kết nối tri thức (KNTT) hai lớp nội dung cho từng môn của từng lớp:

- **Tầng 1: bài học nguyên văn.** Mỗi bài một file Markdown, giữ đủ mạch bài, công thức và hình minh họa.
- **Tầng 2: từ điển thuật ngữ.** Bảng thuật ngữ chuẩn hóa, rút ra từ Tầng 1.

Từ hai tầng này, script xuất ra JSON theo schema riêng của dự án để làm **ground truth** cho agent sinh câu hỏi và cho các hệ thống khác đọc. Agent sinh câu hỏi không được tự bịa định nghĩa.

Định dạng chi tiết của từng tầng nằm ở **[Spec](specs/2026-10-27-textbook-framework-spec.md)**. README này chỉ tóm tắt quy tắc và cách làm việc.

> Ngày 2026-10-27 dự án đã bỏ hệ thống `glossary/` cũ và làm lại từ đầu. Dữ liệu cũ chỉ còn trong lịch sử git. **Không dùng dữ liệu cũ làm nguồn.**

## 2. Bộ (unit) và cấu trúc thư mục

**Bộ** là một môn của một lớp, đặt tên `{mon}_{lop}`: viết thường, không dấu, nối bằng `_` (ví dụ `sinh_12`, `toan_10`).

```
textbook/                          # GỐC DỰ ÁN (repo)
├── README.md, CLAUDE.md
├── specs/                         # spec lõi (chuẩn duy nhất) + profiles/<mon>.json (hồ sơ từng môn)
├── plans/                         # plan thí điểm theo bộ
├── sgk/khoi_<lop>/<unit>/SGK*.pdf # NGUỒN: hiện chỉ SGK (chỉ đọc, không đưa vào git)
├── _SGK-Nguyen-ban/, _Huong-dan/  # mẫu tham chiếu do người dùng làm tay (repo riêng)
├── cache/ocr/<unit>/<pdf>/pNNNN.txt # cache OCR: chữ thô từng trang, chỉ để máy kiểm tra Tầng 1 (tự sinh, không đưa vào git)
├── cache/figures/<unit>/           # lưới đo bbox và ảnh kiểm tra khung cắt hình (tự sinh)
└── textbook/                      # KẾT QUẢ
    ├── schema/                    # unit.schema.json (JSON xuất), progress.schema.json (mục lục), profile.schema.json (hồ sơ môn)
    ├── tessdata/                  # dữ liệu OCR tesseract (vie, eng)
    ├── scripts/                   # công cụ (spec mục 9)
    ├── dataset/<unit>.json        # JSON xuất tự động, KHÔNG sửa tay
    └── khoi_<lop>/<unit>/
        ├── progress.json          # hồ sơ duy nhất của bộ: cây mục lục, dải trang, tiến độ, ghi chú, kết quả kiểm tra
        ├── Tu-dien-<Mon>-<lop>-<Kind>-N.md          # Tầng 2 (mỗi Chương/Chủ đề/Unit… một file)
        ├── <Kind>-NN-…/[<Kind>-NN-…/]<Mã>-….md      # Tầng 1, thư mục theo cây mục lục
        └── … /img/  +  figures.json                 # hình cắt từ trang sách
```

## 3. Đầu mỗi phiên

1. Xác định bộ đang làm. Nếu chưa rõ thì hỏi người dùng. **Mỗi phiên chỉ làm một bộ.**
2. Đọc `textbook/khoi_<lop>/<unit>/progress.json` (kể cả `notes`, `audits`, `last_session_note`), sau đó đọc plan của bộ trong `plans/` (nếu có).
3. Làm tiếp phần đang dở. Không làm lại bài đã `verified`.
4. **Không sửa tay `textbook/dataset/*.json`.** Muốn sửa thì sửa Tầng 1 hoặc Tầng 2, rồi chạy lại script xuất.
5. Cuối phiên: cập nhật `progress.json` (`status`, `last_session_note`) và bảng ở mục 9.

## 4. Quy tắc chống bịa

- **Nguồn là ảnh trang.** Sách KNTT là sách quét, không có text layer. Render trang bằng PyMuPDF (130–150 dpi để đọc, 300 dpi để cắt hình). OCR chỉ dùng để tham khảo và chạy kiểm tra tự động; khi OCR và ảnh khác nhau thì **ảnh là chuẩn**.
- Tầng 1 chép **đúng câu chữ sách**: không sửa chính tả, không diễn giải, không thêm ý.
- Tầng 2 lấy những gì sách **nêu rõ** là định nghĩa, khái niệm, định lí, tính chất, công thức, kí hiệu hoặc quy tắc (`in_source`), và thuật ngữ sách **có mô tả nhưng không định nghĩa** (`described`, ghi `[mô tả]`, giải nghĩa ghép nguyên văn câu mô tả). Không lấy từ ví dụ, bài tập hay hoạt động; thuật ngữ không có trong SGK thì không đưa vào.
- Thuật ngữ có dùng trong bài nhưng sách không định nghĩa thì đánh dấu **"Ngoài nguồn"**, và **không viết định nghĩa** (theo mẫu ở spec mục 5.2).
- Không dựa vào trí nhớ. Chỗ nào không chắc thì ghi vào "Ghi chú nguồn cần kiểm tra", không đoán.
- Repo được phép đẩy lên remote công khai (quyết định 2026-10-27), kể cả Tầng 1 và `img/`. Mỗi file Tầng 1 phải ghi nguồn sách trong frontmatter.

## 5. Nguồn sách

**Hiện chỉ làm với SGK** bộ Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam), đúng môn và đúng lớp. File đặt tên bắt đầu bằng `SGK …`, ví dụ `SGK SINH HOC 12 - KNTT.pdf`. SGK nhiều tập thì mỗi tập một file. Mọi nội dung có `book_type: sgk`, `level: co_ban`.

- Các sách khác (SCD, SGV, SBT, tài liệu bồi dưỡng GV) **chưa dùng**, sẽ mở rộng sau. Nếu thư mục `sgk/` có các file này thì bỏ qua.
- Không dùng văn bản Chương trình GDPT 2018, sách bộ khác hay các trang tổng hợp (VietJack, Loigiaihay…).
- Bộ nào chưa có SGK trong `sgk/khoi_<lop>/<unit>/` thì báo người dùng. **Không tự tải.**
- SGK không có khung yêu cầu cần đạt thì bỏ khối 🎯, không lấy từ nguồn khác.

## 6. Khái niệm lặp giữa các lớp

**Không gộp giữa các lớp.** "Hàm số" ở Toán 10 và ở Toán 12 là hai mục riêng, mỗi mục theo đúng sách của lớp đó.

## 7. Đảm bảo chất lượng

Các cổng phải qua theo thứ tự (chi tiết ở spec mục 7):

1. `check_lesson.py`: Tầng 1 đúng khung, đúng mốc trang, khớp OCR trang (bigram có dấu ≥ 0.65).
2. `check_dict.py`: Tầng 2 khớp Tầng 1; mục Ngoài nguồn không có định nghĩa; mọi ghi chú đều có trạng thái.
   `check_coverage.py` (2b): mọi ứng viên thuật ngữ (in đậm, nhãn mô tả, "được gọi là", từ điển mẫu) đều có dòng trong bảng hoặc trong mục "Đã xét, không tạo mục".
3. `export_unit.py`: JSON hợp lệ theo `unit.schema.json`.
4. **Kiểm tra mẫu**: Claude tự lấy 20–30 mục (gồm mục ngẫu nhiên và mục công thức/định nghĩa trọng tâm), đối chiếu với ảnh trang, yêu cầu tỉ lệ sai ≤ 5% (mục tiêu 0%), ghi kết quả vào `audits` của `progress.json`.
Trước cổng 1, `progress.json` phải hợp lệ theo `progress.schema.json` (cổng 0).

**Không tự đổi các file trong `textbook/schema/`.** Muốn đổi phải hỏi người dùng.

## 8. Lệnh

Cài môi trường khi đổi máy: `python -m pip install -r requirements.txt`, cộng thêm Tesseract OCR 5.x (xem chú thích trong `requirements.txt`).

Chạy từ gốc dự án. Các script đang được viết theo plan thí điểm Sinh 12; chưa viết xong thì chưa có.

```
python textbook/scripts/ocr_pages.py <unit> [--file F] [--pages a-b]        # render + OCR, ghi cache/ocr/<unit>/
python textbook/scripts/crop_figures.py <unit> --grid <trang>...              # vẽ lưới 10 pt để đo bbox hình
python textbook/scripts/crop_figures.py <unit> <thư mục nhóm>                # cắt hình theo figures.json, kiểm tra cạnh khung
python textbook/scripts/check_lesson.py <unit> [--lesson T]                  # cổng 1
python textbook/scripts/check_dict.py <unit> [--file Tu-dien-….md]           # cổng 2
python textbook/scripts/check_coverage.py <unit> [--file Tu-dien-….md]       # cổng 2b (độ phủ)
python textbook/scripts/export_unit.py <unit>                                # cổng 3 → textbook/dataset/<unit>.json
```

## 9. Trạng thái các bộ

| Bộ | Trạng thái | Ghi chú |
|---|---|---|
| `sinh_12` | Hoàn thành 100% (43 bài Tầng 1 verified; 8 từ điển Tầng 2 với 294 thuật ngữ: 139 định nghĩa, 133 mô tả, 22 Ngoài nguồn, 28 ghi chú nguồn đóng, 100% độ phủ; dataset/sinh_12.json đạt chuẩn; kiểm tra mẫu cuối 0% lỗi — 2026-10-28) | SGK sách ảnh, trang PDF = trang in + 2. Đầy đủ 3 Phần, 8 chương, 35 bài học, 8 sơ đồ tóm tắt kiến thức chương và bảng tra cứu thuật ngữ cuối sách. Toàn bộ hình vẽ được trích xuất sạch biên (0 edge ink). Plan: [plans/2026-10-26-bio12-extraction-plan.md](plans/2026-10-26-bio12-extraction-plan.md) |
| `hoa_12` | Hoàn thành 100% (30 bài Tầng 1 verified; 8 từ điển Tầng 2 với 213 thuật ngữ: 123 định nghĩa, 65 mô tả, 25 Ngoài nguồn, 0 ghi chú mở, 100% độ phủ; dataset/hoa_12.json đạt chuẩn; kiểm tra mẫu cuối 0% lỗi — 2026-10-29) | SGK sách ảnh, trang PDF = trang in + 2. Đầy đủ 8 chương, 30 bài học (kèm 8 bài ôn tập). Toàn bộ công thức hoá học $\ce{...}$, hình ảnh trích xuất chuẩn. Đã hoàn thành báo cáo thực nghiệm 40 câu trắc nghiệm đối chứng. |
| `dia_12` | Hoàn thành 100% (35 bài + Bảng giải thích thuật ngữ Tầng 1 verified; 5 từ điển Tầng 2 với 131 thuật ngữ: 9 định nghĩa in_source, 122 mô tả, 0 Ngoài nguồn, 1 ghi chú nguồn đóng, 100% độ phủ; dataset/dia_12.json đạt chuẩn; kiểm tra mẫu cuối 30 mục 0% lỗi — 2026-10-30) | SGK sách ảnh (181 trang PDF, có 2 trang ảnh ngoài lề tại PDF 52 và 103 đã xử lí offset theo bài). Đầy đủ 5 Phần, 35 Bài (26 lí thuyết, 9 thực hành) và Bảng giải thích thuật ngữ cuối sách. Toàn bộ 52 hình/bản đồ/biểu đồ được trích xuất sạch biên (0 lỗi mực sát mép). |
| `lich_su_12` | Hoàn thành 100% (17 bài + Bảng tra cứu khái niệm, thuật ngữ Tầng 1 verified; 6 từ điển Tầng 2 với 176 thuật ngữ: 18 định nghĩa in_source, 158 mô tả, 0 Ngoài nguồn, 6 ghi chú nguồn đóng, 100% độ phủ; dataset/lich_su_12.json đạt chuẩn; kiểm tra mẫu cuối 30 mục 0% lỗi — 2026-10-30) | SGK sách ảnh (115 trang PDF, trang PDF = trang in + 2). Đầy đủ 6 Chủ đề, 17 Bài học (Bài 1–17) và Bảng tra cứu khái niệm, thuật ngữ cuối sách (trang in 110). Toàn bộ 98 hình minh hoạ/sơ đồ/lược đồ được trích xuất sạch biên (0 lỗi mực sát mép). |
| `ngu_van_12` | Hoàn thành 100% (11 bài + 4 bảng thuật ngữ cuối sách Tầng 1 verified; 2 từ điển Tầng 2 với 92 thuật ngữ: 61 định nghĩa in_source, 8 mô tả, 23 Ngoài nguồn, 1 ghi chú nguồn đóng, 100% độ phủ; dataset/ngu_van_12.json đạt chuẩn; kiểm tra mẫu cuối 30 mục 0% lỗi — 2026-10-30) | SGK sách ảnh gồm 2 tập: Tập một (174 trang PDF, Bài 1–5 và Ôn tập học kì I) và Tập hai (145 trang PDF, Bài 6–9 và Ôn tập học kì II), mỗi tập có 2 trang ảnh ngoài lề (PDF 53, 103 ở Tập một; PDF 52, 103 ở Tập hai) đã xử lí offset theo bài. Toàn bộ 26 hình minh hoạ/chân dung/sơ đồ (13 hình Tập một, 13 hình Tập hai) được trích xuất sạch biên (0 lỗi mực sát mép). |
| `tieng_anh_12` | Hoàn thành 100% (14 bài gồm 10 Unit + 4 Review và bảng Glossary cuối sách Tầng 1 verified; 10 từ điển Tầng 2 với 289 thuật ngữ: 250 định nghĩa in_source, 39 mô tả, 0 Ngoài nguồn, 4 ghi chú nguồn đóng, 100% độ phủ; dataset/tieng_anh_12.json đạt chuẩn; kiểm tra mẫu cuối 30 mục 0% lỗi — 2026-10-30) | SGK Tiếng Anh 12 – Global Success (160 trang PDF, trang PDF = trang in + 2). Đầy đủ 10 Unit (Unit 1–10), 4 bài Review (Review 1–4) và bảng Glossary cuối sách (trang in 147–155, PDF 149–157). Toàn bộ 42 hình minh hoạ/biểu đồ/sơ đồ được trích xuất sạch biên. |

Các bộ khác chưa bắt đầu.

Trạng thái gồm: chưa bắt đầu / đang dựng khung / Tầng 1 / Tầng 2 / đã kiểm tra cuối (<số mục>; mẫu <n>, <số sai> sai — YYYY-MM-DD).

## 10. Agent sinh câu hỏi dùng dữ liệu thế nào

- Đọc từ điển Tầng 2 của đúng lớp và đúng chương. Cần ngữ cảnh thì đọc file bài học Tầng 1 tương ứng. Không nạp cả `dataset/<unit>.json`.
- Phạm vi và mức độ câu hỏi bám theo khối `🎯 Yêu cầu cần đạt` của bài.
- Mục "Ngoài nguồn" và mục còn ghi chú đang `mở` thì **không dùng làm đáp án**.
