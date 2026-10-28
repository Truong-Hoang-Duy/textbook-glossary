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
| `textbook/` | Đã dọn sạch ngày 2026-10-27. Chỉ còn `schema/` (`unit.schema.json`, `progress.schema.json`) và `tessdata/`. Đã có `khoi_12/sinh_12/progress.json` (2026-10-27). Cache OCR 199 trang nằm riêng ở `cache/ocr/sinh_12/`, không thuộc kết quả. |
| Mẫu Tầng 1 | `_SGK-Nguyen-ban/Sinh-12/Phan-05-Di-truyen-hoc/` có Bài 1–18 kèm `img/`, do người dùng làm tay. Các file này chưa có mốc trang, frontmatter khác spec, tên hình chưa có mã môn. **Mẫu không khớp file PDF trong `sgk/`**: câu chữ lệch nhiều chỗ, và hình lấy từ bản in khác (Hình 1.3 mẫu ghi "Enzyme ligase", PDF ghi "Enzyme nối"). Chỉ dùng mẫu để tham khảo bố cục; chữ và hình phải lấy từ PDF. |
| Mẫu Tầng 2 | `_Huong-dan/Từ điển Sinh học 12.md` (Bài 1–18). |
| Script | `_common.py`, `ocr_pages.py` (2026-10-27). |

**Đã kiểm tra trên ảnh trang:**

- Trang đầu bài ghi "Phần bốn. Di truyền học", "Chương 1. Di truyền phân tử", "Bài 1. DNA và cơ chế tái bản DNA", "Bài 5. Công nghệ gene".
- Mục lục (PDF 6) lại ghi "Chương I" và "Bài 5. Công nghệ di truyền". Theo spec mục 3, lấy theo trang đầu bài.
- Trang thuật ngữ cuối sách ghi "Giải thích một số thuật ngữ trong sách" (mục lục ghi "Một số thuật ngữ sử dụng trong sách"), PDF 196–197.
- Danh sách đầy đủ các chỗ mục lục lệch nằm trong `notes` của `progress.json`.

**Điểm cần sửa trong mẫu `_Huong-dan/Từ điển Sinh học 12.md` khi dùng làm bản nháp:**

1. Các dòng "Ngoài nguồn" (151, 166, 206–207, 224, 319, 325, 388) phần lớn vẫn kèm câu giải thích, có dòng ghi luôn định nghĩa (P, F₁, F₂). Phải đổi về đúng mẫu ở spec mục 5.2.
2. Ghi chú số 9 đề nghị đối chiếu Luật Hôn nhân và Gia đình. Đây là nguồn ngoài SGK nên chỉ được trích đúng câu trong SGK.
3. Ghi chú số 3 ("công nghệ gene" hay "công nghệ di truyền"): trang đầu bài đã ghi "Công nghệ gene". Còn phải xem phần Kiến thức cốt lõi trên ảnh trang.
4. Ghi chú 1, 2, 4, 6, 7, 8: chuyển sang định dạng ở spec mục 5.6 rồi đối chiếu ảnh để đóng.

## 2. Phạm vi và các đợt

| Đợt | Nội dung | PDF | Điều kiện bắt đầu |
|---|---|---|---|
| 1 | Chương 1 (Bài 1–6) | 7–37 | Giai đoạn 0–1 xong |
| 2 | Chương 2–4 (Bài 7–18) | 38–98 | Cổng G2 đạt |
| 3 | Phần năm, sáu (Chương 5–8, Bài 19–35) và bảng thuật ngữ cuối sách | 99–197 | Đợt 2 qua kiểm tra mẫu |

## 3. Các giai đoạn

### Giai đoạn 0: Dựng khung

- [x] Mở ảnh trang đầu từng Phần, từng chương và từng bài (3 Phần, 8 chương, 35 bài) để lập `textbook/khoi_12/sinh_12/progress.json` theo spec mục 3 (cây `toc`: Phần → Chương → Bài), gồm `label` và `title` đúng như in, `id`, `pdf_pages`, `printed_offset: 2` và `dir`/`file`. Kiểm tra bằng `progress.schema.json`.
- [ ] Đổi cấp Phần của mẫu `_SGK-Nguyen-ban` (đang đặt là `Phần 5`, `Phan-05`) thành `Phần bốn` (`Phan-04`) khi chép sang.
- [x] Ghi vào `notes` của `progress.json` các chỗ mục lục khác trang đầu. → 2026-10-27: 8 ghi chú. Mục lục lệch ở 8 tên (Bài 5, 8, 18, 25, 30, 33, 35, trang thuật ngữ cuối sách) và ghi sai trang Bài 6 (in 34, thật là 32).

**Xong khi:** `progress.json` hợp lệ theo schema, có đủ 3 Phần, 8 chương, 35 bài; đã đối chiếu ảnh tên 3 Phần, 8 chương và 35 bài.

→ 2026-10-27: xong. `toc` có 47 nút lá: 35 bài, 8 trang "Sơ đồ tóm tắt kiến thức chương" (không có trong mục lục), 3 trang đầu sách (`skip`), 1 trang thuật ngữ cuối sách. Trang liên tục từ PDF 4 đến 197.

### Giai đoạn 1: Script

Viết theo spec mục 9, chạy thử trên Bài 1 sau mỗi script:

- [x] `_common.py`, `ocr_pages.py`. OCR toàn bộ 199 trang SGK để có cache. → 2026-10-27: 199/199 trang, 300 dpi, `vie`, khoảng 6 phút.
- [x] `check_lesson.py`, `crop_figures.py` → 2026-10-27. `crop_figures.py` viết lại sau khi Hình 1.3 bị cắt thiếu mép phải: thêm `--grid` để đo khung và kiểm tra cạnh khung (spec 4.4). Bản tự nới khung theo nét vẽ đã thử và bỏ, vì nó nuốt cả chú thích và chữ bên cạnh.
- [x] `check_dict.py` → 2026-10-27, bắt được 5/5 lỗi cài cố ý (Ngoài nguồn kèm định nghĩa, Giải nghĩa bịa, thuật ngữ không có chỗ in đậm, ghi chú sai dạng, mục bài sai tên).
- [x] `export_unit.py` → 2026-10-27, bắt lỗi cài cố ý (thuật ngữ không có chỗ in đậm).

**Xong khi:** chạy trọn chuỗi trên Bài 1 (`progress.json` → Tầng 1 → Tầng 2 → JSON) và kết quả khớp khi đối chiếu tay. Mỗi script phải bắt được ít nhất một lỗi cố tình cài vào.

### Giai đoạn 2: Tầng 1, Chương 1

Làm theo spec mục 4. Chữ chép **từ ảnh trang** (110 dpi đọc được, phóng to chỗ chữ nhỏ); mẫu `_SGK-Nguyen-ban` chỉ để tham khảo bố cục.

- [x] Viết `B01`…`B06` và `So-do-tom-tat-chuong-1.md` vào `textbook/khoi_12/sinh_12/Phan-04-Di-truyen-hoc/Chuong-01-Di-truyen-phan-tu/`.
- [x] Đo bbox trên lưới (`crop_figures.py --grid`), khai báo `figures.json` (khung gồm cả chú thích hình, hoặc tiêu đề và chú thích bảng), cắt đến khi hết lỗi cạnh khung, xem ảnh kiểm tra.
- [x] Chạy `check_lesson.py` đến khi sạch, rồi `--mark` để đổi các bài sang `layer1`.

→ 2026-10-27 (làm lại từ đầu): 7 file ở `layer1`; 20 hình (gồm Bảng 2.1 và sơ đồ tóm tắt xoay ngang), cả 20 không lỗi cạnh khung và đã xem ảnh kiểm tra. `check_lesson.py` có 5 chỗ `ocr-ok` (tiêu đề in đậm nghiêng, Bảng 2.1, sơ đồ tóm tắt) — đều đã đối chiếu ảnh.
- Công cụ bổ sung khi làm: `crop_figures.py` thêm `"rotate"`, ngưỡng cạnh khung siết về 0 điểm (bắt được nhãn "Đời con" bị cắt ở Hình 5.2); `ocr_pages.py` thêm `--psm`; `check_lesson.py` bỏ qua tiêu đề `#` và ghi chú `<!-- -->` khi so OCR.
- Lỗi in của sách (giữ nguyên): "của tế có thể", "đảo bảo" (B01); "nuleotide", "ribosme", "amio acid", "7-Methyguanine", mục III có hai mục số 4 (B02); "không có latose", "β–galatosidase" (B03); chữ dẫn "(H 4.2)" nhưng hình in là Hình 4.1 (B04); "từ các từ loài khác", "ngươi tiêu dùng", "đầu từ" (B05).
- Ghi chú cho Tầng 2: B05 tiêu đề dùng "Công nghệ gene", Kiến thức cốt lõi dùng "Công nghệ di truyền". B03 ghi transacetylase "có chức năng khử các chất độc vào tế bào" — đúng như sách in.

**Xong khi:** 6 bài ở `layer1` và đã đếm số đoạn mà mẫu cũ lệch so với sách (dùng cho chỉ số ở Cổng G2).

### Giai đoạn 3: Tầng 2, Chương 1

- [x] Viết `textbook/khoi_12/sinh_12/Tu-dien-Sinh-hoc-12-Chuong-1.md` theo mẫu `_Huong-dan` và spec mục 5. Giải nghĩa lấy từ câu in đậm ở Tầng 1, không chép từ từ điển mẫu.
- [x] Mục Ngoài nguồn đúng mẫu, không kèm định nghĩa (8 mục: sinh vật nhân sơ/nhân thực, NST, kiểu gene, kiểu hình, allele, trội/lặn, thụ tinh nhân tạo; `Xem: chưa xác định` — điền khi làm các chương sau).
- [x] Đóng 4 ghi chú nguồn bằng đối chiếu ảnh (alanine, transacetylase, chất độc màu cam/acridine, công nghệ gene/di truyền).
- [x] `check_dict.py` đạt, `--mark` đổi 7 nút của Chương 1 sang `layer2`.

→ 2026-10-27: 51 thuật ngữ có nguồn + 8 Ngoài nguồn, 0 ghi chú mở, `trang_thai: verified`. Tầng 1 B03 chuyển chỗ in đậm "operon" sang câu mô tả cấu trúc operon *lac* (mục I.2.a).

### Giai đoạn 4: Xuất và kiểm tra mẫu Chương 1

- [x] `export_unit.py sinh_12` → `textbook/dataset/sinh_12.json` hợp lệ `unit.schema.json` v2.1: 59 thuật ngữ (8 Ngoài nguồn), 43 nút bài, 20 hình, 4 ghi chú nguồn (đều đóng).
- [x] Kiểm tra mẫu 25/51 mục với ảnh trang: 1 sai ("Mạch liên tục"), đã sửa → tỉ lệ sai 4% (≤ 5%). Ghi vào `audits` của `progress.json`; 7 nút Chương 1 đổi sang `verified`.
- Lỗi công cụ phát hiện khi kiểm tra và đã sửa: `export_unit.py` mất mục La Mã sau hộp ❓ giữa mục (ghi `section: null`).

### Bổ sung phương án A (2026-10-27): thuật ngữ mô tả

So với từ điển mẫu, Chương 1 thiếu các thuật ngữ sách có mô tả nhưng không định nghĩa, vì quy tắc cũ chỉ nhận câu định nghĩa in đậm.
- [x] Thêm loại `described`: spec 4.3 (nhãn `<!-- term: … -->`), 5.2, 6; schema v2.2; `check_dict.py`, `export_unit.py`. `check_dict` bắt 4/4 lỗi cài cố ý.
- [x] Gắn 35 nhãn ở Tầng 1, thêm 28 dòng từ điển (26 mô tả, 2 định nghĩa từ tiêu đề in đậm Bài 4). Không thêm helicase, primase, ligase, allolactose (không có trong SGK). ~~miRNA/siRNA~~: ghi chú này sai, hai thuật ngữ có trong Bài 2 (Em có biết) — đã bổ sung ở lần sửa sau.
- [x] Kiểm tra mẫu bổ sung 12/28 mục: 0 sai. Từ điển 87 mục.

### Bổ sung phương án A lần 2 (2026-10-27): tiêu chí khách quan và cổng độ phủ

Tài liệu `sgk/so-sanh-v2.md` cho thấy tiêu chí "có mô tả" còn cảm tính và không cổng nào phát hiện bỏ sót.
- [x] Spec: tiêu chí gắn nhãn mô tả (4.3), đặt tên, tách gộp, lỗi in (5.3), mục "Đã xét, không tạo mục" (5.4), cổng 2b độ phủ (5.5, 7).
- [x] Viết `check_coverage.py`, bắt 2/2 lỗi cài cố ý (xoá một dòng, lý do loại sai dạng).
- [x] Chương 1: thêm 10 dòng mô tả, thêm tên khác cho 7 dòng, lập mục "Đã xét" 30 dòng, thêm ghi chú nguồn số 5 (β–galatosidase). Từ điển 96 mục; 128/128 ứng viên đã xử lý; kiểm tra 10/10 dòng mới với ảnh: 0 sai.

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
