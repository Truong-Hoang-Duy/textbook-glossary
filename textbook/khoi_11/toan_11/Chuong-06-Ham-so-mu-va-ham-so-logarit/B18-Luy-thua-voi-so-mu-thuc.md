---
unit: toan_11
lesson_id: b18
toc_path:
  - "Chương VI. Hàm số mũ và hàm số lôgarit"
  - "Bài 18. Luỹ thừa với số mũ thực"
source_file: "SGK TOAN 11 - KNTT - TAP 2.pdf"
pdf_pages: [5, 10]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:5 -->

<!-- Phần giới thiệu Chương VI (in chung đầu trang PDF 5): CHƯƠNG VI. HÀM SỐ MŨ VÀ HÀM SỐ LÔGARIT -->

Trong chương này, luỹ thừa với số mũ nguyên được mở rộng cho số mũ hữu tỉ, số mũ thực và từ đó hình thành khái niệm lôgarit. Đây là những phép tính được sử dụng nhiều trong khoa học, kĩ thuật và đời sống. Trên cơ sở đó, hai hàm số quan trọng là hàm số mũ và hàm số lôgarit được giới thiệu. Phần cuối chương trình bày cách giải một số phương trình, bất phương trình mũ và lôgarit đơn giản.

# BÀI 18: LUỸ THỪA VỚI SỐ MŨ THỰC

## 🔤 Thuật ngữ

- Cơ số
- Căn bậc $n$
- Luỹ thừa với số mũ nguyên
- Luỹ thừa với số mũ hữu tỉ
- Luỹ thừa với số mũ thực
- Số mũ

## 🎯 Kiến thức, kĩ năng

- Nhận biết khái niệm luỹ thừa với số mũ nguyên của một số thực khác $0$; luỹ thừa với số mũ hữu tỉ và luỹ thừa với số mũ thực của một số thực dương.
- Giải thích các tính chất của luỹ thừa với số mũ nguyên, luỹ thừa với số mũ hữu tỉ và luỹ thừa với số mũ thực.
- Sử dụng tính chất của phép tính luỹ thừa trong tính toán các biểu thức số và rút gọn các biểu thức chứa biến.
- Tính giá trị biểu thức số có chứa phép tính luỹ thừa bằng cách sử dụng máy tính cầm tay.
- Giải quyết một số vấn đề có liên quan đến môn học khác hoặc thực tiễn gắn với phép tính luỹ thừa.

## 🔴 Mở đầu

<!-- term: Công thức lãi kép -->
Ngân hàng thường tính lãi suất cho khách hàng theo thể thức *lãi kép theo định kì*, tức là nếu đến kì hạn người gửi không rút lãi ra thì tiền lãi được tính vào vốn của kì kế tiếp. Nếu một người gửi số tiền $P$ với lãi suất $r$ mỗi kì thì sau $N$ kì, số tiền người đó thu được (cả vốn lẫn lãi) được tính theo *công thức lãi kép* sau:

$A = P(1 + r)^N.$

![Minh hoạ gửi tiết kiệm lãi kép](img/H11-toan-b18-01.png)

<!-- pdf:6 -->

Bác Minh gửi tiết kiệm số tiền $100$ triệu đồng kì hạn $12$ tháng với lãi suất $6\%$ một năm. Giả sử lãi suất không thay đổi. Tính số tiền (cả vốn lẫn lãi) bác Minh thu được sau $3$ năm.

## 1. LUỸ THỪA VỚI SỐ MŨ NGUYÊN

**HĐ1:** Nhận biết luỹ thừa với số mũ nguyên

Tính: $(1,5)^2$; $\left(-\frac{2}{3}\right)^3$; $(\sqrt{2})^4$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, dòng toàn công thức toán học -->

<!-- term: Luỹ thừa với số mũ nguyên -->
> - Cho $n$ là một số nguyên dương. Ta định nghĩa:
>   Với $a$ là số thực tuỳ ý:
>   $a^n = \underbrace{a \cdot a \cdots a}_{n \text{ thừa số}}.$
>   Với $a$ là số thực khác $0$:
>   $a^0 = 1;\ a^{-n} = \frac{1}{a^n}.$
> - Trong biểu thức $a^m$, $a$ gọi là **cơ số**, $m$ gọi là **số mũ**.

> $0^0$ và $0^{-n}\ (n \in \mathbb{N}^*)$ không có nghĩa.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, hộp bóng thoại nhân vật Pi -->

Luỹ thừa với số mũ nguyên có các tính chất tương tự như luỹ thừa với số mũ nguyên dương.

<!-- term: Tính chất của luỹ thừa với số mũ nguyên -->
> Với $a \ne 0, b \ne 0$ và $m, n$ là các số nguyên, ta có:
> $a^m \cdot a^n = a^{m+n}; \qquad \frac{a^m}{a^n} = a^{m-n};$
> $(a^m)^n = a^{mn}; \qquad (ab)^m = a^m b^m;$
> $\left(\frac{a}{b}\right)^m = \frac{a^m}{b^m}.$

**Chú ý:**

- Nếu $a > 1$ thì $a^m > a^n$ khi và chỉ khi $m > n$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, OCR dính chữ Nếéua>1thì và khim>n -->
- Nếu $0 < a < 1$ thì $a^m > a^n$ khi và chỉ khi $m < n$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, OCR dính chữ Nếu0<a<1thì và khim<n -->

**Ví dụ 1:** Tính giá trị của biểu thức:

$A = \left(\frac{1}{2}\right)^{-8} \cdot 8^{-2} + (0,2)^{-4} \cdot 25^{-2}.$

**Giải:**

$A = 2^8 \cdot \frac{1}{8^2} + \frac{1}{0,2^4} \cdot \frac{1}{25^2} = 2^8 \cdot \frac{1}{2^6} + \frac{1}{0,2^4 \cdot 5^4} = 2^2 + \frac{1}{(0,2 \cdot 5)^4} = 4 + 1 = 5.$

**Luyện tập 1:** Một số dương $x$ được gọi là viết dưới dạng **kí hiệu khoa học** nếu $x = a \cdot 10^m$, ở đó $1 \le a < 10$ và $m$ là một số nguyên. Hãy viết các số liệu sau dưới dạng kí hiệu khoa học:

a) Khối lượng của Trái Đất khoảng $5\,980\,000\,000\,000\,000\,000\,000\,000\text{ kg}$;
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, OCR đọc sai Đất thành Đắt -->

b) Khối lượng của hạt proton khoảng $0,000\,000\,000\,000\,000\,000\,000\,000\,001\,67262\text{ kg}$.

*(Theo SGK Vật lí 12, Nhà Xuất bản Giáo dục Việt Nam, 2020)*

<!-- pdf:7 -->

## 2. LUỸ THỪA VỚI SỐ MŨ HỮU TỈ

**HĐ2:** Nhận biết khái niệm căn bậc $n$

a) Tìm tất cả các số thực $x$ sao cho $x^2 = 4$.

b) Tìm tất cả các số thực $x$ sao cho $x^3 = -8$.

> Cho số thực $a$ và số nguyên dương $n$. Số $b$ được gọi là **căn bậc $n$** của số $a$ nếu $b^n = a$.

**Nhận xét:** Khi $n$ là số lẻ, mỗi số thực $a$ chỉ có một căn bậc $n$ và kí hiệu là $\sqrt[n]{a}$. Căn bậc $1$ của số $a$ chính là $a$.

Khi $n$ là số chẵn, mỗi số thực dương có đúng hai căn bậc $n$ là hai số đối nhau, giá trị dương kí hiệu là $\sqrt[n]{a}$ (gọi là **căn số học bậc $n$** của $a$), giá trị âm kí hiệu là $-\sqrt[n]{a}$.

> $\sqrt[n]{0} = 0\ (n \in \mathbb{N}^*).$

> ❓ Số âm có căn bậc chẵn không? Vì sao?

**Ví dụ 2:** Tính: a) $\sqrt[3]{-64}$; $\qquad$ b) $\sqrt[4]{\frac{1}{16}}$.

**Giải:**

a) $\sqrt[3]{-64} = \sqrt[3]{(-4)^3} = -4$. $\qquad$ b) $\sqrt[4]{\frac{1}{16}} = \sqrt[4]{\left(\frac{1}{2}\right)^4} = \frac{1}{2}$.

**Luyện tập 2:** Tính: a) $\sqrt[3]{-125}$; $\qquad$ b) $\sqrt[4]{\frac{1}{81}}$.

**HĐ3:** Nhận biết tính chất của căn bậc $n$
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 7, OCR đọc sai tính thành tĩnh -->

a) Tính và so sánh: $\sqrt[3]{-8} \cdot \sqrt[3]{27}$ và $\sqrt[3]{(-8) \cdot 27}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 7, OCR đọc sai Tính thành Tĩnh -->

b) Tính và so sánh: $\frac{\sqrt[3]{-8}}{\sqrt[3]{27}}$ và $\sqrt[3]{\frac{-8}{27}}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 7, OCR đọc sai Tính thành Tĩnh -->

<!-- term: Tính chất của căn bậc n -->
> Giả sử $n, k$ là các số nguyên dương, $m$ là số nguyên. Khi đó:
> $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{ab};$
> $\frac{\sqrt[n]{a}}{\sqrt[n]{b}} = \sqrt[n]{\frac{a}{b}};$
> $(\sqrt[n]{a})^m = \sqrt[n]{a^m};$
> $\sqrt[n]{a^n} = \begin{cases} a & \text{khi } n \text{ lẻ} \\ |a| & \text{khi } n \text{ chẵn}; \end{cases}$
> $\sqrt[n]{\sqrt[k]{a}} = \sqrt[nk]{a}.$
> (Giả thiết các biểu thức ở trên đều có nghĩa).

<!-- pdf:8 -->

**Ví dụ 3:** Tính: a) $\sqrt[5]{4} \cdot \sqrt[5]{-8}$; $\qquad$ b) $\sqrt[3]{-3\sqrt{3}}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 8, OCR đọc sai Ví dụ 3 và Tính -->

**Giải:**

a) $\sqrt[5]{4} \cdot \sqrt[5]{-8} = \sqrt[5]{4 \cdot (-8)} = \sqrt[5]{-32} = \sqrt[5]{(-2)^5} = -2$.

b) $\sqrt[3]{-3\sqrt{3}} = \sqrt[3]{-(\sqrt{3})^3} = \sqrt[3]{(-\sqrt{3})^3} = -\sqrt{3}$.

**Luyện tập 3:** Tính: a) $\sqrt[3]{5} : \sqrt[3]{625}$; $\qquad$ b) $\sqrt[5]{-25\sqrt{5}}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 8, OCR đọc nhầm số 3 thành 5 -->

**HĐ4:** Nhận biết luỹ thừa với số mũ hữu tỉ

Cho $a$ là một số thực dương.

> Lưu ý: $(\sqrt[n]{a})^n = a$.

a) Với $n$ là số nguyên dương, hãy thử định nghĩa $a^{\frac{1}{n}}$ sao cho $\left(a^{\frac{1}{n}}\right)^n = a$.

b) Từ kết quả của câu a, hãy thử định nghĩa $a^{\frac{m}{n}}$, với $m$ là số nguyên và $n$ là số nguyên dương, sao cho $a^{\frac{m}{n}} = \left(a^{\frac{1}{n}}\right)^m$.

<!-- term: Luỹ thừa với số mũ hữu tỉ -->
> Cho số thực $a$ dương và số hữu tỉ $r = \frac{m}{n}$, trong đó $m$ là một số nguyên và $n$ là số nguyên dương. **Luỹ thừa của $a$ với số mũ $r$**, kí hiệu là $a^r$, xác định bởi $a^r = a^{\frac{m}{n}} = \sqrt[n]{a^m}$.

> ❓ Vì sao trong định nghĩa luỹ thừa với số mũ hữu tỉ lại cần điều kiện cơ số $a > 0$?

**Chú ý:** Luỹ thừa với số mũ hữu tỉ (của một số thực dương) có đầy đủ các tính chất như luỹ thừa với số mũ nguyên đã nêu trong Mục 1.

**Ví dụ 4:** Tính: a) $16^{\frac{3}{2}}$; $\qquad$ b) $8^{\frac{-2}{3}}$.

**Giải:**

a) $16^{\frac{3}{2}} = \sqrt{16^3} = \sqrt{(4^2)^3} = \sqrt{(4^3)^2} = 4^3 = 64$.

b) $8^{\frac{-2}{3}} = \sqrt[3]{8^{-2}} = \sqrt[3]{(2^3)^{-2}} = \sqrt[3]{(2^{-2})^3} = 2^{-2} = \frac{1}{4}$.

**Luyện tập 4:** Rút gọn biểu thức: $A = \frac{x^{\frac{3}{2}}y + xy^{\frac{3}{2}}}{\sqrt{x} + \sqrt{y}}\ (x, y > 0)$.

## 3. LUỸ THỪA VỚI SỐ MŨ THỰC

**a) Khái niệm luỹ thừa với số mũ thực**

**HĐ5:** Nhận biết luỹ thừa với số mũ thực

Ta biết rằng $\sqrt{2}$ là một số vô tỉ và $\sqrt{2} = 1,4142135624\dots$

Gọi $(r_n)$ là dãy số hữu tỉ dùng để xấp xỉ số $\sqrt{2}$, với $r_1 = 1$; $r_2 = 1,4$; $r_3 = 1,41$; $r_4 = 1,4142; \dots$

> $\lim_{n \to +\infty} r_n = \sqrt{2}.$

<!-- pdf:9 -->

a) Dùng máy tính cầm tay, hãy tính: $3^{r_1}$; $3^{r_2}$; $3^{r_3}$; $3^{r_4}$ và $3^{\sqrt{2}}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 9, OCR đọc sai cầm thành cằm -->

b) Có nhận xét gì về sai số tuyệt đối giữa $3^{\sqrt{2}}$ và $3^{r_n}$, tức là $|3^{\sqrt{2}} - 3^{r_n}|$, khi $n$ càng lớn?
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 9, OCR đọc sai đối thành đói -->

<!-- term: Luỹ thừa với số mũ thực -->
> Cho $a$ là số thực dương và $\alpha$ là một số vô tỉ. Xét dãy số hữu tỉ $(r_n)$ mà $\lim_{n \to +\infty} r_n = \alpha$. Khi đó, dãy số $(a^{r_n})$ có giới hạn xác định và không phụ thuộc vào dãy số hữu tỉ $(r_n)$ đã chọn. Giới hạn đó gọi là **luỹ thừa của $a$ với số mũ $\alpha$**, kí hiệu là $a^\alpha$.
> $a^\alpha = \lim_{n \to +\infty} a^{r_n}.$

**Chú ý:** Luỹ thừa với số mũ thực (của một số dương) có đầy đủ các tính chất như luỹ thừa với số mũ nguyên đã nêu trong Mục 1.

**Ví dụ 5:** Rút gọn biểu thức: $A = \frac{a^{\sqrt{5}-1} \cdot a^{3-\sqrt{5}}}{\left(a^{\sqrt{3}+1}\right)^{\sqrt{3}-1}}\ (a > 0)$.

**Giải:**

$A = \frac{a^{\sqrt{5}-1} \cdot a^{3-\sqrt{5}}}{\left(a^{\sqrt{3}+1}\right)^{\sqrt{3}-1}} = \frac{a^{\sqrt{5}-1+3-\sqrt{5}}}{a^{(\sqrt{3}+1)(\sqrt{3}-1)}} = \frac{a^2}{a^{3-1}} = \frac{a^2}{a^2} = 1.$

**Ví dụ 6:** Không sử dụng máy tính, hãy so sánh các số $8^{\sqrt{3}}$ và $4^{2\sqrt{3}}$.

**Giải:**

Ta có: $8^{\sqrt{3}} = (2^3)^{\sqrt{3}} = 2^{3\sqrt{3}}$ và $4^{2\sqrt{3}} = (2^2)^{2\sqrt{3}} = 2^{4\sqrt{3}}$.

Vì $3\sqrt{3} < 4\sqrt{3}$ và $2 > 1$ nên $2^{3\sqrt{3}} < 2^{4\sqrt{3}}$. Vậy $8^{\sqrt{3}} < 4^{2\sqrt{3}}$.

> Ta đưa về so sánh hai luỹ thừa cùng cơ số.

**Luyện tập 5:** Rút gọn biểu thức: $A = \frac{\left(a^{\sqrt{2}-1}\right)^{1+\sqrt{2}}}{a^{\sqrt{5}-1} \cdot a^{3-\sqrt{5}}}\ (a > 0)$.

**Vận dụng:** Giải bài toán trong *tình huống mở đầu*.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 9, OCR đọc sai tình huống thành fình huồng -->

**b) Tính luỹ thừa với số mũ thực bằng máy tính cầm tay**

Có thể sử dụng máy tính cầm tay để tính căn bậc $n$ và luỹ thừa với số mũ thực.

| Tính (làm tròn kết quả đến chữ số thập phân thứ tư) | Bấm phím | Màn hình hiện | Kết quả |
| :---: | :---: | :---: | :---: |
| $\sqrt{20,15}$ | `[√■] [2] [0] [.] [1] [5] [=]` | `4.488875137` | $\sqrt{20,15} \approx 4,4889$ |
| $\sqrt[5]{320}$ | `[SHIFT] [x^■] [5] [▶] [3] [2] [0] [=]` | `3.169786385` | $\sqrt[5]{320} \approx 3,1698$ |
| $15^{3,2}$ | `[1] [5] [x^■] [3] [.] [2] [=]` | `5800.855256` | $15^{3,2} \approx 5\,800,8553$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 9, bảng bấm phím máy tính cầm tay -->

<!-- pdf:10 -->

## ✏️ Bài tập

**6.1.** Tính:

a) $\left(\frac{1}{5}\right)^{-2}$; $\qquad$ b) $4^{\frac{3}{2}}$; $\qquad$ c) $\left(\frac{1}{8}\right)^{-\frac{2}{3}}$; $\qquad$ d) $\left(\frac{1}{16}\right)^{-0,75}$.

**6.2.** Thực hiện phép tính:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 10, OCR mất nhãn 6.2 -->

a) $27^{\frac{2}{3}} + 81^{-0,75} - 25^{0,5}$; $\qquad$ b) $4^{2-3\sqrt{7}} \cdot 8^{2\sqrt{7}}$.

**6.3.** Rút gọn các biểu thức sau:

a) $A = \frac{x^5 y^{-2}}{x^3 y}\ (x, y \ne 0)$; $\qquad$ b) $B = \frac{x^2 y^{-3}}{\left(x^{-1} y^4\right)^{-3}}\ (x, y \ne 0)$.

**6.4.** Cho $x, y$ là các số thực dương. Rút gọn các biểu thức sau:

a) $A = \frac{x^{\frac{1}{3}}\sqrt{y} + y^{\frac{1}{3}}\sqrt{x}}{\sqrt[6]{x} + \sqrt[6]{y}}$; $\qquad$ b) $B = \left(\frac{x^{\sqrt{3}}}{y^{\sqrt{3}-1}}\right)^{\sqrt{3}+1} \cdot \frac{x^{-\sqrt{3}-1}}{y^{-2}}$.

**6.5.** Chứng minh rằng: $\sqrt{4 + 2\sqrt{3}} - \sqrt{4 - 2\sqrt{3}} = 2$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 10, OCR mất nhãn 6.5 -->

**6.6.** Không sử dụng máy tính cầm tay, hãy so sánh:

a) $5^{6\sqrt{3}}$ và $5^{3\sqrt{6}}$; $\qquad$ b) $\left(\frac{1}{2}\right)^{-\frac{4}{3}}$ và $\sqrt{2} \cdot 2^{\frac{2}{3}}$.

**6.7.** Nếu một khoản tiền gốc $P$ được gửi ngân hàng với lãi suất hằng năm $r$ ($r$ được biểu thị dưới dạng số thập phân), được tính lãi $n$ lần trong một năm, thì tổng số tiền $A$ nhận được (cả vốn lẫn lãi) sau $N$ kì gửi cho bởi công thức sau:

$A = P\left(1 + \frac{r}{n}\right)^N.$

Hỏi nếu bác An gửi tiết kiệm số tiền $120$ triệu đồng theo kì hạn $6$ tháng với lãi suất không đổi là $5\%$ một năm, thì số tiền thu được (cả vốn lẫn lãi) của bác An sau $2$ năm là bao nhiêu?

**6.8.** Năm 2021, dân số của một quốc gia ở châu Á là $19$ triệu người. Người ta ước tính rằng dân số của quốc gia này sẽ tăng gấp đôi sau $30$ năm nữa. Khi đó dân số $A$ (triệu người) của quốc gia đó sau $t$ năm kể từ năm 2021 được ước tính bằng công thức $A = 19 \cdot 2^{\frac{t}{30}}$. Hỏi với tốc độ tăng dân số như vậy thì sau $20$ năm nữa dân số của quốc gia này sẽ là bao nhiêu? (Làm tròn kết quả đến chữ số hàng triệu).

## 📷 Danh sách hình trong bài

| Mã hình | Trang PDF | Vị trí trong bài | Chú thích gốc |
| --- | :---: | --- | --- |
| H11-toan-b18-01 | 5 | Mở đầu | (sách không đánh số, ảnh minh hoạ gửi tiết kiệm lãi kép) |
