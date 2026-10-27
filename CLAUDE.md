@README.md

## Lệnh kích hoạt bộ mới

Khi người dùng nói **`Bắt đầu làm bộ <unit>`** (hoặc `Khởi tạo và xử lý bộ <unit>`), làm lần lượt các giai đoạn dưới đây. Định dạng chi tiết theo [Spec](specs/2026-10-27-textbook-framework-spec.md).

### Giai đoạn 1: Dựng khung

- Tìm file `SGK …` trong `sgk/khoi_<lop>/<unit>/` (README mục 5). Hiện chỉ làm SGK, các sách khác bỏ qua. Không có SGK thì báo người dùng. Không tự tải, không dùng nguồn ngoài KNTT.
- Tạo `textbook/khoi_<lop>/<unit>/`:
  * `progress.json`: cây mục lục theo đúng kiểu của sách (Phần/Chương/Chủ đề/Unit… → Bài/Lesson), **đọc từ ảnh trang** (tiền tố và tên đúng như in), `pdf_pages` cho từng bài, `status: pending`. Kiểm tra bằng `progress.schema.json`. Điểm đặc thù của sách (mục lục khác trang đầu…) ghi vào `notes`.
- Chạy `ocr_pages.py <unit>` để có cache OCR.
- Thêm một dòng vào bảng README mục 9.

### Giai đoạn 2: Tầng 1 (bài học nguyên văn)

- Đọc ảnh từng trang rồi viết file bài `<Mã>-<slug>.md` theo spec mục 4: frontmatter, khung heading, mốc `<!-- pdf:N -->`, in đậm thuật ngữ tại câu định nghĩa, công thức LaTeX.
- Khai báo hình trong `figures.json` và chạy `crop_figures.py`.
- Chạy `check_lesson.py` đến khi sạch thì đổi bài sang `status: layer1`.

### Giai đoạn 3: Tầng 2 (từ điển)

- Viết `Tu-dien-<Mon>-<lop>-<Kind>-N.md` (mỗi nhóm chứa bài một file) theo spec mục 5. Nội dung chỉ lấy từ Tầng 1. Mục Ngoài nguồn không kèm định nghĩa.
- Chạy `check_dict.py` đến khi sạch.

### Giai đoạn 4: Xuất và nghiệm thu

- Chạy `export_unit.py <unit>` (0 lỗi schema, không trùng `id`).
- Lấy mẫu 20–30 mục (gồm mục ngẫu nhiên và mục công thức/định nghĩa trọng tâm), đối chiếu với ảnh trang: giải nghĩa, công thức, `pdf_page`, `printed_page`. Yêu cầu tỉ lệ sai ≤ 5%, mục tiêu 0%. Sai thì sửa ở Tầng 1 hoặc Tầng 2 rồi xuất lại. Không giữ file kiểm tra tạm.
- Ghi kết quả vào `audits` của `progress.json`, đổi trạng thái ở README mục 9 thành `Đã kiểm tra cuối (<số mục>; mẫu <n>, 0 sai — YYYY-MM-DD)`, rồi báo cáo tổng kết cho người dùng.

---

## Git & Commit Rules

1. **Commit Messages:**
   - Write commit messages in **concise English** (following Conventional Commits, e.g., `feat: ...`, `fix: ...`, `docs: ...`, `refactor: ...`).
   - Keep the summary line short, clear, and under 72 characters.
   - **STRICTLY PROHIBITED:** Never include `Co-authored-by: Claude`, `Co-authored-by: Assistant`, or any AI/assistant attribution footers or signatures.

2. **Commit & Push Execution:**
   - **NEVER** run `git commit` or `git push` autonomously.
   - Only propose or execute commit/push commands when explicitly requested or confirmed by the user.
