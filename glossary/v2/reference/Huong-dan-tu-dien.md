---
name: huong-dan-tu-dien
description: Hướng dẫn dùng từ điển thuật ngữ chung Tu-dien.md: các trường của mỗi mục, cách lấy từng trường, quy tắc chống trùng và thứ tự. Đọc trước khi thêm hoặc sửa mục.
sources: [claude]
---

# Hướng dẫn từ điển thuật ngữ

File dữ liệu: `Ver2/Tu-dien.md` (thư mục con `Ver2` của thư mục này). Từ điển dùng chung cho nhiều dự án, nên mọi thay đổi phải giữ đúng định dạng dưới đây.

## Các trường của một mục

| Trường           | Bắt buộc     | Cách lấy                                                                                              | Ví dụ                                              |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Tiêu đề `### `   | Có           | Thuật ngữ tiếng Anh đúng như trong nguồn, giữ viết hoa theo nguồn                                     | `### Gel electrophoresis (DNA)`                    |
| Tiếng Việt       | Có           | Thuật ngữ tiếng Việt chuẩn. Nếu nguồn Việt có dùng thì lấy theo nguồn đó. Nếu không có, giữ tiếng Anh | `Điện di DNA (điện di trên gel)`                   |
| Chuyên ngành gốc | Có           | Ngành mà khái niệm sinh ra: Toán học / Vật lí / Hóa học / Sinh học                                    | `Sinh học`                                         |
| Giải thích (EN)  | Có           | Một đến hai câu, lấy ý từ nguồn, không thêm kiến thức ngoài nguồn                                     | `Technique separating DNA fragments by size...`    |
| Giải thích (VI)  | Có           | Bản dịch tiếng Việt của giải thích EN                                                                 | `Kỹ thuật tách các đoạn DNA theo kích thước...`    |
| Bối cảnh         | Có           | Lĩnh vực đang dùng thuật ngữ. Nếu một từ có nhiều nghĩa, mỗi nghĩa một gạch con                       | `Công nghệ gene / Sinh học phân tử`                |
| Nguồn            | Có (mục mới) | Tài liệu, unit, chương, bài và số trang lấy thuật ngữ. Xem định dạng bên dưới                         | `Campbell Biology, Unit 2, Chương 05, B1, tr. 152` |

### Định dạng trường Nguồn

`<Tên sách> <edition nếu có>, Unit <n>, Chương <NN>, B<n>, tr. <số trang>`

- Ví dụ: `Campbell Biology, Unit 2, Chương 05, B1, tr. 152`
- Nếu một thuật ngữ xuất hiện ở nhiều trang, ghi các trang cách nhau bằng dấu phẩy: `tr. 152, 158`.
- Nếu mục đã có nguồn khác, nối thêm bằng dấu chấm phẩy: `Campbell Biology, Unit 2, Chương 05, B1, tr. 152; Campbell Biology, Unit 3, Chương 10, B2, tr. 201`.
- Mục cũ chưa có trường Nguồn: để nguyên, không tự điền. Khi cần, ghi `Nguồn: chưa rõ (nhập trước khi có trường này)`.

## Cách lấy các trường từ sách

1. Mở đúng trang sách (file `.txt` hoặc PDF chương) và tìm thuật ngữ **in đậm** hoặc **in nghiêng** trong sách. Đây thường là thuật ngữ mới.
2. Lấy tên tiếng Anh đúng như sách viết. Không đổi sang từ đồng nghĩa.
3. Lấy định nghĩa trong sách làm Giải thích (EN). Dịch sang Giải thích (VI).
4. Ghi Chuyên ngành gốc theo ngành của chương. Ví dụ chương di truyền thì ghi Sinh học.
5. Ghi Nguồn theo vị trí tìm thấy.
6. Nếu sách không có định nghĩa rõ, ghi thuật ngữ đó vào danh sách xem xét và không tự viết định nghĩa.

## Quy tắc chống trùng

Khi thêm một thuật ngữ, kiểm tra theo thứ tự:

1. **Trùng tiếng Anh** (không phân biệt hoa thường) với một mục: cập nhật mục đó. Tiếng Anh là khóa chính.
2. **Không trùng tiếng Anh nhưng trùng tiếng Việt** với một mục: cập nhật mục đó.
3. **Không trùng cả hai**: thêm mục mới.
4. **Tiếng Anh trùng mục X nhưng tiếng Việt trùng mục Y khác X**: cập nhật X theo tiếng Anh, không sửa Y, và ghi vào danh sách xung đột để giáo viên xử lý.

Khi cập nhật một mục đã có:
- Không ghi đè nội dung cũ.
- Điền các trường còn trống.
- Nếu bối cảnh đã có, thêm nguồn mới vào trường Nguồn.
- Nếu bối cảnh khác, thêm một gạch con mới vào Bối cảnh (không xóa gạch cũ).
- Nếu giải thích khác với mục cũ, ghi thêm "Giải thích khác (nguồn ...)" thay vì thay thế.

### Thuật ngữ trùng giữa các lĩnh vực

- **Cùng một khái niệm, khác ngữ cảnh ứng dụng**: chỉ thêm gạch con vào "Bối cảnh" của mục đó. Không tạo mục mới. Ví dụ: `Derivative` (Toán gốc, dùng trong mô hình quần thể Sinh học).
- **Cùng tên nhưng hai khái niệm khác hẳn nhau** (ví dụ `vector` trong Toán và trong Sinh học):
  1. Giữ một mục, thêm gạch "Lưu ý" trong "Bối cảnh" để nhắc nguy cơ nhầm lẫn và nêu nghĩa ở lĩnh vực kia.
  2. Tạo thêm mục tương ứng cho lĩnh vực kia, có ghi lĩnh vực trong ngoặc ở tiêu đề tiếng Anh (ví dụ `Vector (mathematics)`), để tiêu đề không trùng với mục đã có.
- **Ngoại lệ đã quyết định**: mục `Vector` hiện có chỉ giữ gạch "Lưu ý" về Toán, chưa tách mục. Các trường hợp sau này áp dụng đủ hai bước trên.

## Thứ tự và định dạng file

- Các mục sắp xếp A–Z theo tiếng Anh.
- Giữ nguyên phần tiêu đề và dòng ghi chú `<!-- ... -->` ở cuối file.
- Dùng `$...$` cho công thức như các mục hiện có.

## Ví dụ một mục đầy đủ

```
### Gene
- **Tiếng Việt:** Gen
- **Chuyên ngành gốc:** Sinh học
- **Giải thích (EN):** A segment of DNA that codes for a functional product, usually a protein.
- **Giải thích (VI):** Đoạn DNA mã hóa một sản phẩm có chức năng, thường là protein.
- **Bối cảnh:** Sinh học (di truyền học).
- **Nguồn:** Campbell Biology, Unit 2, Chương 05, B1, tr. 152
```

## Lưu ý

- Chỉ thêm thuật ngữ có trong nguồn. Ngoài nguồn thì ghi "Ngoài nguồn" và hỏi lại.
- Không sửa các mục toán thống kê khi làm việc với sách sinh học, trừ khi có xung đột đã báo cáo.
