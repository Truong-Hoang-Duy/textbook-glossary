@README.md

## Lệnh kích hoạt bộ môn mới (New Unit Trigger)

Khi người dùng ra lệnh:
👉 **`Bắt đầu làm bộ <unit>`** (hoặc **`Khởi tạo và xử lý bộ <unit>`**, ví dụ: `Bắt đầu làm bộ sinh_10`):

Claude phải tự động triển khai đầy đủ quy trình 5 giai đoạn chuẩn mực giống hệt như đã làm với `toan_10`:

### 1. Giai đoạn 1 — Dựng khung bộ mới
- Quét toàn bộ file PDF trong thư mục `sgk/khoi_<lop>/<unit>/`. Phân loại chính xác:
  * `SGK` (`level: co_ban`)
  * `SCD` (`level: chuyen_de`)
  * `SBT` (`book_type: sbt`)
  * `SGV` hoặc `Tài liệu bồi dưỡng GV` (`book_type: gv`, phân loại `level: co_ban` cho SGK hoặc `chuyen_de` cho SCD).
- Tạo thư mục `glossary/khoi_<lop>/<unit>/` gồm 3 file:
  * `<unit>.json`: Khung JSON chuẩn theo `schema.json` (term_count = 0).
  * `progress.json`: Lập mục lục chi tiết mọi chương/bài từ PDF nguồn, xác định sẵn `pdf_pages: [đầu, cuối]`.
  * `DESCRIPTION.md`: Khung tài liệu kỹ thuật theo cấu trúc chuẩn của `toan_10`.
- Đồng thời copy `<unit>.json` vào thư mục tập trung `glossary/dataset/<unit>.json`.
- Thêm một dòng trạng thái mới vào bảng ở Mục 9 `README.md`.
- Chạy `python glossary/scripts/validate.py <unit>` để đảm bảo khung hợp lệ 100%.

### 2. Giai đoạn 2 & 3 — Trích xuất thuật ngữ
- Trích xuất bám sát nguyên văn theo thứ tự ưu tiên: **SGK > SCD > SGV > SBT**.
- Quy tắc `id`: `{unit với _ đổi thành -}-{slug-khong-dau}` (ví dụ: `sinh-10-te-bao`).
- Nhập dữ liệu qua file lô tạm bằng `python glossary/scripts/add_terms.py <unit> <lo.json>`.
- Đọc kỹ tài liệu `SGV` để trích xuất Mục 4 (Yêu cầu cần đạt, giới hạn kiến thức) và Mục 5 (Sai lầm thường gặp của học sinh) vào `DESCRIPTION.md`.
- Cập nhật tiến độ `status: done` và `terms_added` cho từng bài học trong `progress.json`.

### 3. Giai đoạn 4 — Kiểm tra chất lượng tự động
- Chạy kiểm tra tính hợp lệ của dữ liệu:
  * `python glossary/scripts/validate.py <unit>` (yêu cầu 0 lỗi).
- Chạy kiểm tra đối soát nguồn trích dẫn:
  * `python glossary/scripts/check_sources.py <unit>` (ngưỡng bigram 0.65 có dấu tiếng Việt, xử lý sạch 100% các mục bị gắn cờ nhầm).

### 4. Giai đoạn 5 — Tự động kiểm định mẫu, kết luận & Nghiệm thu
- **Máy tự động kiểm tra, so sánh và kết luận trực tiếp (Không cần xuất file hay chờ người kiểm tra thủ công):**
  * Tự động lấy mẫu chuẩn 20–30 thuật ngữ (gồm các mục ngẫu nhiên và các mục công thức/kí hiệu/định nghĩa trọng tâm).
  * Máy tự động đối chiếu trực tiếp định nghĩa, công thức (`notation`), số trang (`pdf_page`, `printed_page`) với nội dung trang PDF nguồn tương ứng (dưới dạng ảnh/OCR).
  * Tự động đánh giá sai số và đưa ra kết luận kiểm định ngay trong phiên (yêu cầu tỉ lệ sai ≤ 5%, mục tiêu 0% sai sót).
  * Không cần giữ lại file `sample_audit.md` (nếu có sinh ra tạm thời thì tự động xóa sạch).
- **Hoàn tất hồ sơ & Trạng thái:**
  * Cập nhật đầy đủ kết luận kiểm định chất lượng vào Mục 6 của `DESCRIPTION.md`.
  * Đổi trạng thái trong bảng Mục 9 `README.md` thành `Đã kiểm tra cuối (<số mục>; mẫu <số mục mẫu>, 0 sai — YYYY-MM-DD)`.
  * Báo cáo tổng kết toàn diện kết quả kiểm tra cho người dùng và hoàn thành nhiệm vụ.

---

## Git & Commit Rules

1. **Commit Messages:**
   - Write commit messages in **concise English** (following Conventional Commits, e.g., `feat: ...`, `fix: ...`, `docs: ...`, `refactor: ...`).
   - Keep the summary line short, clear, and under 72 characters.
   - **STRICTLY PROHIBITED:** Never include `Co-authored-by: Claude`, `Co-authored-by: Assistant`, or any AI/assistant attribution footers or signatures.

2. **Commit & Push Execution:**
   - **NEVER** run `git commit` or `git push` autonomously.
   - Only propose or execute commit/push commands when explicitly requested or confirmed by the user.
