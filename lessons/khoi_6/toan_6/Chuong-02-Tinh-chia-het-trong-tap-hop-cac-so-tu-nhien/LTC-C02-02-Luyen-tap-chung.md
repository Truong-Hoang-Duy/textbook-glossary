---
unit: toan_6
lesson_id: ltc-c02-02
toc_path:
  - "Chương II. Tính chia hết trong tập hợp các số tự nhiên"
  - "Luyện tập chung"
source_file: "SGK TOAN 6-1 KNTT.pdf"
pdf_pages: [59, 60]
lesson_type: on_tap
status: verified
---

<!-- pdf:59 -->

# LUYỆN TẬP CHUNG

**Ví dụ 1**

Tìm ước chung lớn nhất của $60$ và $90$.

**Giải**

Phân tích $60$ và $90$ ra thừa số nguyên tố, ta có:

$60 = 2^2 \cdot 3 \cdot 5,$

$90 = 2 \cdot 3^2 \cdot 5.$

Do đó $\text{ƯCLN}(60, 90) = 2 \cdot 3 \cdot 5 = 30$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 59, OCR đọc sai ƯCLN thành ƯƠLN -->

**Ví dụ 2**

Tìm số tự nhiên $a$ lớn nhất sao cho $18 \vdots a$, $45 \vdots a$ và $135 \vdots a$.

**Giải**

Số tự nhiên $a$ lớn nhất cần tìm chính là $\text{ƯCLN}(18, 45, 135)$.

Phân tích ra thừa số nguyên tố, ta có:

$18 = 2 \cdot 3^2,$

$45 = 3^2 \cdot 5,$

$135 = 3^3 \cdot 5.$

Do đó $\text{ƯCLN}(18, 45, 135) = 3^2 = 9$.

Vậy $a = 9$.

**Ví dụ 3**

Có ba loại đèn trang trí, chúng phát sáng cùng lúc vào $6$ giờ sáng. Đèn thứ nhất cứ $6$ giây phát sáng một lần, đèn thứ hai cứ $8$ giây phát sáng một lần và đèn thứ ba cứ $10$ giây phát sáng một lần. Hỏi khi nào thì ba đèn cùng phát sáng lần tiếp theo?
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 59, OCR đọc sai chữ lần thành lằn -->

**Giải**

Gọi thời gian để sau đó ba đèn cùng phát sáng lần tiếp theo là $x$ (giây).

Khi đó $x = \text{BCNN}(6, 8, 10)$.

![Minh hoạ các bóng đèn trang trí Ví dụ 3](img/H6-toan-ltc-c02-02-01.png)

Phân tích ra thừa số nguyên tố, ta có: $6 = 2 \cdot 3$; $8 = 2^3$ và $10 = 2 \cdot 5$ nên

$\text{BCNN}(6, 8, 10) = 2^3 \cdot 3 \cdot 5 = 120.$

Ta có $x = 120$ giây.

Do đó sau $120$ giây $= 2$ phút, tức là vào lúc $6$ giờ $2$ phút thì ba đèn lại cùng phát sáng lần tiếp theo.

<!-- pdf:60 -->

## BÀI TẬP

2.45. Cho bảng sau:
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 60, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

| $a$ | $9$ | $34$ | $120$ | $15$ | $2987$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $b$ | $12$ | $51$ | $70$ | $28$ | $1$ |
| $\text{ƯCLN}(a, b)$ | $3$ | $?$ | $?$ | $?$ | $?$ |
| $\text{BCNN}(a, b)$ | $36$ | $?$ | $?$ | $?$ | $?$ |
| $\text{ƯCLN}(a, b) \cdot \text{BCNN}(a, b)$ | $108$ | $?$ | $?$ | $?$ | $?$ |
| $a \cdot b$ | $108$ | $?$ | $?$ | $?$ | $?$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 60, bảng gồm nhiều ô công thức và dấu hỏi -->

a) Tìm các số thích hợp thay vào ô trống của bảng;

b) So sánh tích $\text{ƯCLN}(a, b) \cdot \text{BCNN}(a, b)$ và $a \cdot b$.

Em rút ra kết luận gì?

2.46. Tìm ƯCLN và BCNN của:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 60, OCR đọc ƯCLN thành ƯƠCLN -->

a) $3 \cdot 5^2$ và $5^2 \cdot 7$;

b) $2^2 \cdot 3 \cdot 5$; $3^2 \cdot 7$ và $3 \cdot 5 \cdot 11$.

2.47. Các phân số sau đã tối giản chưa? Nếu chưa, hãy rút gọn về phân số tối giản.

a) $\frac{15}{17}$; $\qquad$ b) $\frac{70}{105}$.

2.48. Hai vận động viên chạy xung quanh một sân vận động. Hai vận động viên xuất phát tại cùng một thời điểm, cùng vị trí và chạy cùng chiều. Vận động viên thứ nhất chạy một vòng sân hết $360$ giây, vận động viên thứ hai chạy một vòng sân mất $420$ giây. Hỏi sau bao nhiêu phút họ gặp lại nhau, biết tốc độ di chuyển của họ không đổi?

2.49. Quy đồng mẫu các phân số sau:

a) $\frac{4}{9}$ và $\frac{7}{15}$; $\qquad$ b) $\frac{5}{12}, \frac{7}{15}$ và $\frac{4}{27}$.

2.50. Từ ba tấm gỗ có độ dài là $56\text{ dm}$, $48\text{ dm}$ và $40\text{ dm}$, bác thợ mộc muốn cắt thành các thanh gỗ có độ dài như nhau mà không để thừa mẩu gỗ nào. Hỏi bác cắt như thế nào để được các thanh gỗ có độ dài lớn nhất có thể?

2.51. Học sinh lớp 6A khi xếp thành hàng $2$, hàng $3$, hàng $7$ đều vừa đủ hàng. Hỏi số học sinh lớp 6A là bao nhiêu biết rằng số học sinh nhỏ hơn $45$.

2.52. Hai số có BCNN là $2^3 \cdot 3 \cdot 5^3$ và ƯCLN là $2^2 \cdot 5$. Biết một trong hai số bằng $2^2 \cdot 3 \cdot 5$, tìm số còn lại.

## 📷 Danh sách hình trong bài

| Mã hình | Trang PDF | Vị trí trong bài | Chú thích gốc |
| --- | :---: | --- | --- |
| H6-toan-ltc-c02-02-01 | 59 | Ví dụ 3 | (sách không đánh số, ảnh minh hoạ các bóng đèn trang trí phát sáng) |
