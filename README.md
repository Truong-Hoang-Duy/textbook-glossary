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
├── specs/                         # spec định dạng (chuẩn duy nhất)
├── plans/                         # plan thí điểm theo bộ
├── sgk/khoi_<lop>/<unit>/SGK*.pdf # NGUỒN: hiện chỉ SGK (chỉ đọc, không đưa vào git)
├── _SGK-Nguyen-ban/, _Huong-dan/  # mẫu tham chiếu do người dùng làm tay (repo riêng)
└── textbook/                      # KẾT QUẢ
    ├── schema/                    # unit.schema.json (JSON xuất), progress.schema.json (mục lục)
    ├── tessdata/                  # dữ liệu OCR tesseract (vie, eng)
    ├── scripts/                   # công cụ (spec mục 9)
    ├── dataset/<unit>.json        # JSON xuất tự động, KHÔNG sửa tay
    └── khoi_<lop>/<unit>/
        ├── progress.json          # hồ sơ duy nhất của bộ: cây mục lục, dải trang, tiến độ, ghi chú, kết quả kiểm tra
        ├── Tu-dien-<Mon>-<lop>-<Kind>-N.md          # Tầng 2 (mỗi Chương/Chủ đề/Unit… một file)
        ├── <Kind>-NN-…/[<Kind>-NN-…/]<Mã>-….md      # Tầng 1, thư mục theo cây mục lục
        │   ├── img/  +  figures.json
        └── .ocr/<tên pdf>/pNNNN.txt                  # cache OCR (tự sinh, không đưa vào git)
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
- Tầng 2 chỉ lấy những gì sách **nêu rõ** là định nghĩa, khái niệm, định lí, tính chất, công thức, kí hiệu hoặc quy tắc. Không lấy định nghĩa từ ví dụ, bài tập hay hoạt động.
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
3. `export_unit.py`: JSON hợp lệ theo `unit.schema.json`.
4. **Kiểm tra mẫu**: Claude tự lấy 20–30 mục (gồm mục ngẫu nhiên và mục công thức/định nghĩa trọng tâm), đối chiếu với ảnh trang, yêu cầu tỉ lệ sai ≤ 5% (mục tiêu 0%), ghi kết quả vào `audits` của `progress.json`.
Trước cổng 1, `progress.json` phải hợp lệ theo `progress.schema.json` (cổng 0).

**Không tự đổi các file trong `textbook/schema/`.** Muốn đổi phải hỏi người dùng.

## 8. Lệnh

Cài môi trường khi đổi máy: `python -m pip install -r requirements.txt`, cộng thêm Tesseract OCR 5.x (xem chú thích trong `requirements.txt`).

Chạy từ gốc dự án. Các script đang được viết theo plan thí điểm Sinh 12; chưa viết xong thì chưa có.

```
python textbook/scripts/ocr_pages.py <unit> [--file F] [--pages a-b]        # render + OCR, ghi cache .ocr/
python textbook/scripts/crop_figures.py <unit> <thư mục nhóm>                # cắt hình theo figures.json
python textbook/scripts/check_lesson.py <unit> [--lesson T]                  # cổng 1
python textbook/scripts/check_dict.py <unit> [--file Tu-dien-….md]           # cổng 2
python textbook/scripts/export_unit.py <unit>                                # cổng 3 → textbook/dataset/<unit>.json
```

## 9. Trạng thái các bộ

| Bộ | Trạng thái | Ghi chú |
|---|---|---|
| `sinh_12` | Thí điểm: đang dựng khung | Có SGK (sách ảnh, trang PDF = trang in + 2). Có sẵn mẫu Tầng 1 Bài 1–18 trong `_SGK-Nguyen-ban` và mẫu từ điển Bài 1–18 trong `_Huong-dan`. Plan: [plans/2026-10-26-bio12-extraction-plan.md](plans/2026-10-26-bio12-extraction-plan.md) |

Các bộ khác chưa bắt đầu.

Trạng thái gồm: chưa bắt đầu / đang dựng khung / Tầng 1 / Tầng 2 / đã kiểm tra cuối (<số mục>; mẫu <n>, <số sai> sai — YYYY-MM-DD).

## 10. Agent sinh câu hỏi dùng dữ liệu thế nào

- Đọc từ điển Tầng 2 của đúng lớp và đúng chương. Cần ngữ cảnh thì đọc file bài học Tầng 1 tương ứng. Không nạp cả `dataset/<unit>.json`.
- Phạm vi và mức độ câu hỏi bám theo khối `🎯 Yêu cầu cần đạt` của bài.
- Mục "Ngoài nguồn" và mục còn ghi chú đang `mở` thì **không dùng làm đáp án**.
