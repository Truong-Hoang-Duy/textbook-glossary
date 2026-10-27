# Plan thí điểm: Sinh học 12 theo `SPEC-TEXTBOOK-01`

> **Mã:** `PLAN-SINH12-PILOT-01`, cập nhật 2026-10-27, trạng thái **nháp, chờ duyệt**
> **Spec:** [2026-10-27-textbook-framework-spec.md](../specs/2026-10-27-textbook-framework-spec.md).
> **Nguồn:** chỉ SGK. Các sách khác sẽ mở rộng sau. Plan này chỉ ghi phần riêng của Sinh 12: việc cần làm, thứ tự, tiêu chí hoàn thành và rủi ro.
> **Mục tiêu kép:** (1) Sinh 12 có đủ Tầng 1, Tầng 2 và JSON hợp lệ theo `unit.schema.json`. (2) Viết xong và chạy thử bộ script dùng chung cho mọi môn.

---

## 1. Hiện trạng (kiểm tra ngày 2026-10-27)

| Hạng mục | Hiện trạng |
|---|---|
| Nguồn PDF | `sgk/khoi_12/sinh_12/SGK SINH HOC 12 - KNTT.pdf`, 199 trang. Sách quét, text layer trống. Trang PDF = trang in + 2. |
| `textbook/` | Đã dọn sạch ngày 2026-10-27. Chỉ còn `schema/` (`unit.schema.json`, `progress.schema.json`) và `tessdata/`. Chưa có cache OCR, phải OCR lại từ đầu. |
| Mẫu Tầng 1 | `_SGK-Nguyen-ban/Sinh-12/Phan-05-Di-truyen-hoc/` có Bài 1–18 kèm `img/`, do người dùng làm tay. Các file này chưa có mốc trang, frontmatter khác spec, tên hình chưa có mã môn. |
| Mẫu Tầng 2 | `_Huong-dan/Từ điển Sinh học 12.md` (Bài 1–18). |
| Script | Chưa có. |

**Đã kiểm tra trên ảnh trang:**

- Trang đầu bài ghi "Phần bốn. Di truyền học", "Chương 1. Di truyền phân tử", "Bài 1. DNA và cơ chế tái bản DNA", "Bài 5. Công nghệ gene".
- Mục lục (PDF 6) lại ghi "Chương I" và "Bài 5. Công nghệ di truyền". Theo spec mục 3, lấy theo trang đầu bài.
- Bảng "Một số thuật ngữ sử dụng trong sách" bắt đầu ở trang in 194 (PDF 196).

**Điểm cần sửa trong mẫu `_Huong-dan/Từ điển Sinh học 12.md` khi dùng làm bản nháp:**

1. Các dòng "Ngoài nguồn" (151, 166, 206–207, 224, 319, 325, 388) phần lớn vẫn kèm câu giải thích, có dòng ghi luôn định nghĩa (P, F₁, F₂). Phải đổi về đúng mẫu ở spec mục 5.2.
2. Ghi chú số 9 đề nghị đối chiếu Luật Hôn nhân và Gia đình. Đây là nguồn ngoài SGK nên chỉ được trích đúng câu trong SGK.
3. Ghi chú số 3 ("công nghệ gene" hay "công nghệ di truyền"): trang đầu bài đã ghi "Công nghệ gene". Còn phải xem phần Kiến thức cốt lõi trên ảnh trang.
4. Ghi chú 1, 2, 4, 6, 7, 8: chuyển sang định dạng ở spec mục 5.3 rồi đối chiếu ảnh để đóng.

## 2. Phạm vi và các đợt

| Đợt | Nội dung | PDF | Điều kiện bắt đầu |
|---|---|---|---|
| 1 | Chương 1 (Bài 1–6) | 7–37 | Giai đoạn 0–1 xong |
| 2 | Chương 2–4 (Bài 7–18) | 38–98 | Cổng G2 đạt |
| 3 | Phần năm, sáu (Chương 5–8, Bài 19–35) và bảng thuật ngữ cuối sách | 99–197 | Đợt 2 qua kiểm tra mẫu |

## 3. Các giai đoạn

### Giai đoạn 0: Dựng khung

- [ ] Mở ảnh trang đầu từng Phần, từng chương và từng bài (3 Phần, 8 chương, 35 bài) để lập `textbook/khoi_12/sinh_12/progress.json` theo spec mục 3 (cây `toc`: Phần → Chương → Bài), gồm `label` và `title` đúng như in, `id`, `pdf_pages`, `printed_offset: 2` và `dir`/`file`. Kiểm tra bằng `progress.schema.json`.
- [ ] Đổi cấp Phần của mẫu `_SGK-Nguyen-ban` (đang đặt là `Phần 5`, `Phan-05`) thành `Phần bốn` (`Phan-04`) khi chép sang.
- [ ] Ghi vào `notes` của `progress.json` các chỗ mục lục khác trang đầu ("Chương I" / "Chương 1", "Công nghệ di truyền" / "Công nghệ gene").

**Xong khi:** `progress.json` hợp lệ theo schema, có đủ 3 Phần, 8 chương, 35 bài; đã đối chiếu ảnh tên 3 Phần, 8 chương và 35 bài.

### Giai đoạn 1: Script

Viết theo spec mục 9, chạy thử trên Bài 1 sau mỗi script:

- [ ] `_common.py`, `ocr_pages.py`. OCR toàn bộ 199 trang SGK để có cache.
- [ ] `check_lesson.py`, `crop_figures.py`
- [ ] `check_dict.py`, `export_unit.py`

**Xong khi:** chạy trọn chuỗi trên Bài 1 (`progress.json` → Tầng 1 → Tầng 2 → JSON) và kết quả khớp khi đối chiếu tay. Mỗi script phải bắt được ít nhất một lỗi cố tình cài vào.

### Giai đoạn 2: Tầng 1, Chương 1

- [ ] Lấy `_SGK-Nguyen-ban/…/Chuong-01-…/B01…B06` làm **bản nháp** và chép sang `textbook/khoi_12/sinh_12/Phan-04-Di-truyen-hoc/Chuong-01-Di-truyen-phan-tu/`. Không sửa bản gốc trong `_SGK-Nguyen-ban`.
- [ ] Đổi frontmatter và heading theo spec mục 4.1–4.2.
- [ ] Đọc ảnh từng trang: chèn mốc `<!-- pdf:N -->`, sửa câu chữ lệch so với sách, in đậm đúng câu định nghĩa.
- [ ] Đo bbox cho từng hình, ghi `figures.json`, chạy `crop_figures.py` (đặt tên theo dạng `H12-sinh-b0<n>-<stt>.png`).
- [ ] Chạy `check_lesson.py` đến khi sạch, đổi các bài sang `layer1`.

**Xong khi:** 6 bài ở `layer1` và đã đếm số đoạn mà mẫu cũ lệch so với sách (dùng cho chỉ số ở Cổng G2).

### Giai đoạn 3: Tầng 2, Chương 1

- [ ] Lấy phần Bài 1–6 trong `_Huong-dan/Từ điển Sinh học 12.md` làm bản nháp, tạo `textbook/khoi_12/sinh_12/Tu-dien-Sinh-hoc-12-Chuong-1.md`. Sửa frontmatter và tiêu đề mục theo `progress.json`. Không sửa bản gốc trong `_Huong-dan`.
- [ ] Sửa các điểm 1–4 ở mục 1 cho phần thuộc Chương 1.
- [ ] Đối chiếu ảnh để đóng các ghi chú về alanine (Bài 2), transacetylase (Bài 3), "chất độc màu cam"/acridine (Bài 4) và Bài 5.
- [ ] Chạy `check_dict.py` đến khi sạch, đổi các bài sang `layer2`.

**Xong khi:** từ điển ở `trang_thai: verified`.

### Giai đoạn 4: Xuất và kiểm tra mẫu Chương 1

- [ ] Chạy `export_unit.py sinh_12` (cổng 3). Mở `textbook/dataset/sinh_12.json` kiểm tra cấu trúc Phần → Chương → Bài, `terms` và `source_notes` của Chương 1.
- [ ] Kiểm tra mẫu 20–30 mục, đối chiếu ảnh (cổng 4). Ghi kết quả vào `audits` của `progress.json`.

### Cổng G2: Đánh giá thí điểm (điểm dừng, người dùng quyết định)

| Chỉ số | Cách đo |
|---|---|
| Số thuật ngữ và số mục Ngoài nguồn của Chương 1 | `export_unit.py`, từ điển |
| Tỉ lệ sai của mẫu | Cổng 4 |
| Tỉ lệ đoạn trong mẫu `_SGK-Nguyen-ban` bị lệch so với sách | Giai đoạn 2 |
| Số lần `check_lesson`/`check_dict` gắn cờ và số lần sai thật | Kết quả script |
| Thời gian cho mỗi bài | Ghi lại trong khi làm |

Người dùng chọn một trong ba: **mở rộng** sang Đợt 2, **điều chỉnh spec** rồi thử lại, hoặc **dừng**.

### Giai đoạn 5: Mở rộng

Lặp lại Giai đoạn 2–4 cho Đợt 2 và Đợt 3. Đợt 3 không có mẫu Tầng 1 sẵn, nên viết từ ảnh trang ngay từ đầu. Mỗi đợt có một lần kiểm tra mẫu riêng. Xong Đợt 3 thì cập nhật dòng `sinh_12` ở README mục 9 thành "Đã kiểm tra cuối".

## 4. Rủi ro

| Rủi ro | Ảnh hưởng | Giảm thiểu |
|---|---|---|
| OCR tiếng Việt trên ảnh quét sai nhiều nên gắn cờ nhầm | Tốn thời gian rà | Tính ngưỡng theo từng đoạn; đoạn bị gắn cờ thì đọc ảnh, ảnh là chuẩn |
| Mẫu làm tay lệch câu chữ so với sách | Sai ngay từ gốc | Coi mẫu là bản nháp; `check_lesson` là cổng bắt buộc |
| Đo bbox cho hàng trăm hình tốn công | Chậm Đợt 2–3 | Đo trên ảnh 150 dpi rồi quy đổi sang point; G2 đo thời gian thực tế để quyết định |

## 5. Không làm trong plan này

- Không làm các bộ khác.
- Không đổi các file trong `textbook/schema/`.
- Không tích hợp với review-station.
- Không commit hoặc push khi người dùng chưa yêu cầu.
