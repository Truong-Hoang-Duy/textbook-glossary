---
unit: toan_6
lesson_id: b12
toc_path:
  - "Chương II. Tính chia hết trong tập hợp các số tự nhiên"
  - "Bài 12. Bội chung. Bội chung nhỏ nhất"
source_file: "SGK TOAN 6-1 KNTT.pdf"
pdf_pages: [54, 58]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:54 -->

# BÀI 12: BỘI CHUNG. BỘI CHUNG NHỎ NHẤT

## 🔤 Khái niệm, thuật ngữ

- Bội chung
- Bội chung nhỏ nhất

## 🎯 Kiến thức, kĩ năng

- Tìm bội chung, bội chung nhỏ nhất của hai hoặc ba số tự nhiên.
- Sử dụng bội chung nhỏ nhất để quy đồng mẫu các phân số và cộng, trừ phân số.

## 🔴 Mở đầu

Mai cần mua đĩa giấy, cốc giấy để chuẩn bị cho một bữa tiệc sinh nhật. Đĩa và cốc được đóng thành từng gói với số lượng mỗi loại khác nhau: gói $4$ cái đĩa và gói $6$ cái cốc. Cửa hàng chỉ bán từng gói mà không bán lẻ. Mai muốn mua số đĩa và số cốc bằng nhau thì phải mua ít nhất bao nhiêu gói mỗi loại?

![Đĩa giấy và cốc giấy](img/H6-toan-b12-01.png)

## 1. BỘI CHUNG VÀ BỘI CHUNG NHỎ NHẤT

**Bội chung và bội chung nhỏ nhất của hai hay nhiều số**

**HĐ1:** Tìm các tập hợp $\text{B}(6)$, $\text{B}(9)$.

**HĐ2:** Gọi $\text{BC}(6, 9)$ là tập hợp các số vừa là bội của $6$, vừa là bội của $9$. Hãy viết tập $\text{BC}(6, 9)$.

**HĐ3:** Tìm số nhỏ nhất khác $0$ trong tập $\text{BC}(6, 9)$.

> **Bội chung** của hai hay nhiều số là bội của tất cả các số đó.
>
> **Bội chung nhỏ nhất** của hai hay nhiều số là số nhỏ nhất khác $0$ trong tập hợp các bội chung của các số đó.

Ta kí hiệu:

- $\text{BC}(a, b)$ là tập hợp các bội chung của $a$ và $b$;
- $\text{BCNN}(a, b)$ là bội chung nhỏ nhất của $a$ và $b$.

**Chú ý:** Ta chỉ xét bội chung của các số khác $0$.

**Ví dụ 1:** Tìm bội chung và bội chung nhỏ nhất của $4$ và $6$.

**Giải:**

Ta có: $\text{B}(4) = \{0; 4; 8; 12; 16; 20; 24; 28; \dots\}$; $\text{B}(6) = \{0; 12; 18; 24; 30; \dots\}$.

Các số $0; 12; 24; \dots$ vừa là bội của $4$, vừa là bội của $6$ nên $\text{BC}(4, 6) = \{0; 12; 24; \dots\}$.

Số nhỏ nhất khác $0$ trong tập hợp các bội chung của $4$ và $6$ là $12$ nên $\text{BCNN}(4, 6) = 12$.

> **Tròn:**
> - $x \in \text{BC}(a, b)$ nếu $x \vdots a$, $x \vdots b$.
> - $x \in \text{BC}(a, b, c)$ nếu $x \vdots a$, $x \vdots b$, $x \vdots c$.

<!-- pdf:55 -->

**Ví dụ 2:** *Trở lại tình huống mở đầu của bài*, để mua cùng số lượng $n$ cái mỗi loại thì $n \in \text{BC}(4, 6)$. Để mua ít nhất thì $n = \text{BCNN}(4, 6) = 12$.

Vậy bạn Mai có thể mua ít nhất $12$ cái mỗi loại hay mua $3$ gói đĩa và $2$ gói cốc.

**Tìm bội chung nhỏ nhất trong trường hợp đặc biệt**

- **Pi:** Các em hãy tìm $\text{BCNN}(7, 21)$?
- **Tròn:** Ta có $\text{B}(7) = \{0; 7; 14; 21; 28; 35; 42; 49; \dots\}$, $\text{B}(21) = \{0; 21; 42; 63; \dots\}$ nên $\text{BC}(7, 21) = \{0; 21; 42; \dots\}$, do đó $\text{BCNN}(7, 21) = 21$.
- **Vuông:** Em có cách khác ngắn hơn. Vì $21 \vdots 7$ nên $\text{BCNN}(7, 21) = 21$.
- **Pi:** Tròn và Vuông đều làm rất tốt!
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 55, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

<!-- term: Bội chung nhỏ nhất trong trường hợp đặc biệt -->
> **Nhận xét:**
> - Trong các số đã cho, nếu số lớn nhất là bội của các số còn lại thì BCNN của các số đã cho chính là số lớn nhất đó. Nếu $a \vdots b$ thì $\text{BCNN}(a, b) = a$.
> - Mọi số tự nhiên đều là bội của $1$. Do đó với mọi số tự nhiên $a$ và $b$ (khác $0$), ta có: $\text{BCNN}(a, 1) = a$; $\text{BCNN}(a, b, 1) = \text{BCNN}(a, b)$.

> ❓ Tìm $\text{BCNN}(36, 9)$.

**Luyện tập 1:** Tìm bội chung nhỏ nhất của: $\quad$ a) $6$ và $8$; $\qquad$ b) $8, 9, 72$.

**Vận dụng:** Có hai chiếc máy A và B. Lịch bảo dưỡng định kì đối với máy A là $6$ tháng và đối với máy B là $9$ tháng. Hai máy vừa cùng được bảo dưỡng vào tháng $5$. Hỏi sau bao lâu thì hai máy lại được bảo dưỡng trong cùng một tháng?

## 2. CÁCH TÌM BỘI CHUNG NHỎ NHẤT

Ta có $\text{BCNN}(4, 6) = 12 = 2^2 \cdot 3$, trong đó $2$ và $3$ là các ước nguyên tố chung và riêng của $4$ và $6$. Vậy có sự liên hệ gì giữa BCNN của các số và các ước nguyên tố chung và riêng của chúng? Chúng ta cùng tìm hiểu nhé.

> **Pi:** Ta phân tích mỗi số ra thừa số nguyên tố để tìm các ước nguyên tố chung và riêng của các số đó.

<!-- pdf:56 -->

**Tìm bội chung nhỏ nhất bằng cách phân tích các số ra thừa số nguyên tố**

Để tìm $\text{BCNN}(75, 90)$ ta làm như sau:

1. Phân tích các số $75$ và $90$ ra thừa số nguyên tố, ta được:

   $75 = 3 \cdot 5 \cdot 5 = 3 \cdot 5^2$,

   $90 = 2 \cdot 3 \cdot 3 \cdot 5 = 2 \cdot 3^2 \cdot 5$.

2. Ta thấy các thừa số chung là $3$ và $5$; thừa số riêng là $2$.

3. Số mũ lớn nhất của $3$ là $2$, số mũ lớn nhất của $5$ là $2$, số mũ lớn nhất của $2$ là $1$.

   Khi đó $\text{BCNN}(75, 90) = 2 \cdot 3^2 \cdot 5^2 = 450$.

<!-- term: Cách tìm bội chung nhỏ nhất -->
> Các bước tìm BCNN của hai hay nhiều số lớn hơn $1$:
> 1. Phân tích mỗi số ra thừa số nguyên tố;
> 2. Chọn ra các thừa số nguyên tố chung và riêng;
> 3. Lập tích các thừa số đã chọn, mỗi thừa số lấy với số mũ lớn nhất. Tích đó là BCNN cần tìm.

> ❓ Tìm bội chung nhỏ nhất của $9$ và $15$, biết: $9 = 3^2$ và $15 = 3 \cdot 5$.
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 56, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

**Ví dụ 3:** Tìm $\text{BCNN}(18, 24, 40)$ bằng cách phân tích ra thừa số nguyên tố.

**Giải:**

Phân tích các số $18, 24, 40$ ra thừa số nguyên tố, ta được:

$18 = 2 \cdot 3^2; \qquad 24 = 2^3 \cdot 3; \qquad 40 = 2^3 \cdot 5.$

Thừa số nguyên tố chung là $2$ và riêng là $3$ và $5$.

Khi đó $\text{BCNN}(18, 24, 40) = 2^3 \cdot 3^2 \cdot 5 = 360$.

> **Tròn:** Ta thấy $18, 24, 40$ có thừa số chung là $2$ và các thừa số riêng là $3$ và $5$.
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 56, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

**Tìm bội chung từ bội chung nhỏ nhất**

Ta đã biết $\text{BC}(4, 6) = \{0; 12; 24; \dots\}$, $\text{BCNN}(4, 6) = 12$ và nhận thấy các số là bội chung của $4$ và $6$ đều là bội của $12$.

<!-- term: Cách tìm bội chung từ bội chung nhỏ nhất -->
> Để tìm bội chung của các số đã cho ta có thể làm như sau:
> 1. Tìm BCNN của các số.
> 2. Tìm các bội của BCNN đó.

> ❓ Biết bội chung nhỏ nhất của $8$ và $6$ là $24$. Tìm các bội chung nhỏ hơn $100$ của $8$ và $6$.

**Ví dụ 4:**

Ta có $\text{BCNN}(18, 24, 40) = 360$.

Từ đó, ta suy ra $\text{BC}(18, 24, 40) = \{0; 360; 720; 1\,080; \dots\}$ nên bội chung nhỏ hơn $900$ của $18, 24$ và $40$ là $0, 360, 720$.

<!-- pdf:57 -->

**Luyện tập 2:** Tìm bội chung nhỏ nhất của $15$ và $54$. Từ đó, hãy tìm các bội chung nhỏ hơn $1\,000$ của $15$ và $54$.

**Thử thách nhỏ:** Lịch xuất bến của một số xe buýt tại bến xe Mỹ Đình (Hà Nội) được ghi ở bảng bên. Giả sử các xe buýt xuất bến cùng lúc vào $10$ giờ $35$ phút. Hỏi vào các thời điểm nào trong ngày (từ $10$ giờ $35$ phút đến $22$ giờ) các xe buýt này lại xuất bến cùng một lúc?

**Bến xe Mỹ Đình**

| Số xe | Thời gian |
| :---: | :---: |
| Xe $16$ | $15$ phút/chuyến |
| Xe $34$ | $9$ phút/chuyến |
| Xe $30$ | $10$ phút/chuyến |
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 57, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

## 3. QUY ĐỒNG MẪU CÁC PHÂN SỐ

**Tìm mẫu chung của hai phân số**

<!-- term: Quy đồng mẫu số các phân số -->
Để quy đồng mẫu hai phân số $\frac{a}{b}$ và $\frac{c}{d}$, ta phải tìm mẫu chung của hai phân số đó. Thông thường ta nên chọn mẫu chung là bội chung nhỏ nhất của hai mẫu.

Chẳng hạn, để quy đồng mẫu hai phân số $\frac{5}{8}$ và $\frac{7}{12}$, ta làm như sau:

Ta có $\text{BCNN}(8, 12) = 24$, nên $\frac{5}{8} = \frac{5 \cdot 3}{8 \cdot 3} = \frac{15}{24}$ và $\frac{7}{12} = \frac{7 \cdot 2}{12 \cdot 2} = \frac{14}{24}$.

> ❓ Quy đồng mẫu hai phân số: $\frac{7}{9}$ và $\frac{4}{15}$.

**Ví dụ 5:** Quy đồng mẫu các phân số sau: $\frac{3}{8}, \frac{5}{9}$ và $\frac{1}{6}$.

**Giải:**

Ta có $6 = 2 \cdot 3$; $8 = 2^3$; $9 = 3^2$ nên $\text{BCNN}(6, 8, 9) = 2^3 \cdot 3^2 = 72$.

Ta có thể lấy mẫu chung của ba phân số trên là $72$. Do đó

$\frac{3}{8} = \frac{3 \cdot 9}{8 \cdot 9} = \frac{27}{72}; \qquad \frac{5}{9} = \frac{5 \cdot 8}{9 \cdot 8} = \frac{40}{72}; \qquad \frac{1}{6} = \frac{1 \cdot 12}{6 \cdot 12} = \frac{12}{72}.$

<!-- term: Quy đồng mẫu số các phân số -->
> **Tròn:** Có thể chọn một bội chung bất kì của các mẫu làm mẫu chung. Tuy nhiên, người ta thường lấy bội chung nhỏ nhất làm mẫu chung.

**Ví dụ 6:** Thực hiện phép tính: $\quad$ a) $\frac{1}{4} + \frac{1}{6}$; $\qquad$ b) $\frac{11}{12} - \frac{3}{8}$.
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 57, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

**Giải:**

a) Ta có $\text{BCNN}(4, 6) = 12$ nên ta có thể lấy mẫu chung của hai phân số là $12$ và:
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 57, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

$\frac{1}{4} = \frac{1 \cdot 3}{4 \cdot 3} = \frac{3}{12}, \qquad \frac{1}{6} = \frac{1 \cdot 2}{6 \cdot 2} = \frac{2}{12}.$

<!-- pdf:58 -->

Vậy $\frac{1}{4} + \frac{1}{6} = \frac{3}{12} + \frac{2}{12} = \frac{5}{12}$.

b) Ta có $\text{BCNN}(8, 12) = 24$ nên: $\frac{11}{12} - \frac{3}{8} = \frac{11 \cdot 2}{12 \cdot 2} - \frac{3 \cdot 3}{8 \cdot 3} = \frac{22}{24} - \frac{9}{24} = \frac{13}{24}$.

**Luyện tập 3:**

1. Quy đồng mẫu các phân số sau: $\quad$ a) $\frac{5}{12}$ và $\frac{7}{15}$; $\qquad$ b) $\frac{2}{7}, \frac{4}{9}$ và $\frac{7}{12}$.

2. Thực hiện các phép tính sau: $\quad$ a) $\frac{3}{8} + \frac{5}{24}$; $\qquad$ b) $\frac{7}{16} - \frac{5}{12}$.

## BÀI TẬP

2.36. Tìm bội chung nhỏ hơn $200$ của
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 58, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

a) $5$ và $7$; $\qquad$ b) $3, 4$ và $10$.

2.37. Tìm BCNN của:
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 58, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

a) $2 \cdot 3^3$ và $3 \cdot 5$; $\qquad$ b) $2 \cdot 5 \cdot 7^2$ và $3 \cdot 5^2 \cdot 7$.

2.38. Tìm BCNN của các số sau:

a) $30$ và $45$; $\qquad$ b) $18, 27$ và $45$.

2.39. Tìm số tự nhiên $a$ nhỏ nhất khác $0$, biết rằng $a \vdots 28$ và $a \vdots 32$.
<!-- ocr-ok: đã đối chiếu trực tiếp ảnh trang PDF 58, khớp 100% chữ gốc (OCR rơi số hiệu màu nhạt / công thức / bảng) -->

2.40. Học sinh lớp 6A khi xếp thành $3$ hàng, $4$ hàng hay $9$ hàng đều vừa đủ. Biết số học sinh của lớp từ $30$ đến $40$. Tính số học sinh lớp 6A.

2.41. Hai đội công nhân trồng được một số cây như nhau. Mỗi công nhân đội I đã trồng $8$ cây, mỗi công nhân đội II đã trồng $11$ cây. Tính số cây mỗi đội đã trồng, biết rằng số cây đó trong khoảng từ $100$ đến $200$ cây.

2.42. Cứ $2$ ngày, Hà đi dạo cùng bạn cún yêu quý của mình. Cứ $7$ ngày, Hà lại tắm cho cún. Hôm nay, cún vừa được đi dạo, vừa được tắm. Hỏi sau ít nhất bao nhiêu ngày nữa thì cún vừa được đi dạo vừa được tắm?

2.43. Quy đồng mẫu các phân số sau:

a) $\frac{9}{12}$ và $\frac{7}{15}$; $\qquad$ b) $\frac{7}{10}, \frac{3}{4}$ và $\frac{9}{14}$.

2.44. Thực hiện các phép tính sau:

a) $\frac{7}{11} + \frac{5}{7}$; $\qquad$ b) $\frac{7}{20} - \frac{2}{15}$.

## 💡 Em có biết?

**LỊCH CAN CHI**

Nhiều nước phương Đông trong đó có Việt Nam, gọi tên năm âm lịch bằng cách ghép $10$ *can* theo thứ tự (Giáp, Ất, Bính, Đinh, Mậu, Kỉ, Canh, Tân, Nhâm, Quý) với $12$ *chi* (Tí, Sửu, Dần, Mão, Thìn, Tị, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi).

Đầu tiên Giáp được ghép với Tí thành năm Giáp Tí. Cứ $10$ năm Giáp lại được lặp lại; cứ $12$ năm Tí lại được lặp lại:

- Can: Giáp — Ất — Bính — Đinh — Mậu — Kỉ — Canh — Tân — Nhâm — Quý — Giáp — Ất — Bính — Đinh — $\dots$
- Chi: Tí — Sửu — Dần — Mão — Thìn — Tị — Ngọ — Mùi — Thân — Dậu — Tuất — Hợi — Tí — Sửu — $\dots$

Như vậy, cứ sau $60$ năm ($60$ là $\text{BCNN}$ của $10$ và $12$), năm Giáp Tí lại được lặp lại. Tên của các năm âm lịch khác cũng được lặp lại sau $60$ năm.

## 📷 Danh sách hình trong bài

| Mã hình | Trang PDF | Vị trí trong bài | Chú thích gốc |
| --- | :---: | --- | --- |
| H6-toan-b12-01 | 54 | Mở đầu | (sách không đánh số, hình đĩa giấy và cốc giấy) |
