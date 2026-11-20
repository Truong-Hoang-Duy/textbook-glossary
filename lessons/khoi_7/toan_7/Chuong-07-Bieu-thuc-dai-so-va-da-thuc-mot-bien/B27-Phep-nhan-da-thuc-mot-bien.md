---
unit: toan_7
lesson_id: b27
toc_path:
  - "Chương VII. Biểu thức đại số và đa thức một biến"
  - "Bài 27. Phép nhân đa thức một biến"
source_file: "SGK Toan 7 Tap 2.pdf"
pdf_pages: [37, 39]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:37 -->

# BÀI 27: PHÉP NHÂN ĐA THỨC MỘT BIẾN

## 🔤 Khái niệm, thuật ngữ

- Tích của hai đa thức

## 🎯 Kiến thức, kĩ năng

- Thực hiện các phép tính nhân hai đa thức cùng biến.
- Nhận biết và vận dụng các tính chất của các phép tính về đa thức trong tính toán.

## 🔴 Mở đầu

*Bài toán đoán tuổi.*

> Em hãy:
> - Lấy tuổi của mình cộng với $1$ rồi bình phương lên. Số nhận được gọi là kết quả thứ nhất.
> - Lại lấy tuổi của mình trừ đi $1$ rồi bình phương lên. Số nhận được gọi là kết quả thứ hai.
> - Lấy kết quả thứ nhất trừ đi kết quả thứ hai và cho anh biết kết quả cuối cùng.
>
> Anh sẽ đoán được tuổi của em.

Không biết anh Pi làm thế nào nhỉ? Học xong bài này em sẽ khám phá được bí mật đó.

## 1. NHÂN ĐƠN THỨC VỚI ĐA THỨC

**Quy tắc nhân đơn thức với đa thức**

**HĐ1:** Hãy nhắc lại cách nhân hai đơn thức và tính $(12x^3) \cdot (-5x^2)$.

**HĐ2:** Áp dụng tính chất phân phối của phép nhân đối với phép cộng, hãy tìm tích $2x \cdot (3x^2 - 8x + 1)$ bằng cách nhân $2x$ với từng hạng tử của đa thức $3x^2 - 8x + 1$ rồi cộng các tích tìm được.

Tổng quát, ta có quy tắc sau:

<!-- term: Nhân đơn thức với đa thức -->
> Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích với nhau.

**Ví dụ 1:**

Tính $(-2x^3) \cdot \left(\dfrac{1}{2}x^2 + 3x - 5\right)$.

**Giải:**

Ta có: $(-2x^3) \cdot \left(\dfrac{1}{2}x^2 + 3x - 5\right) = (-2x^3) \cdot \left(\dfrac{1}{2}x^2\right) + (-2x^3) \cdot (3x) + (-2x^3) \cdot (-5) = -x^5 - 6x^4 + 10x^3$.

**Luyện tập 1:**

Tính $(-2x^2) \cdot (3x - 4x^3 + 7 - x^2)$.

<!-- pdf:38 -->

**Vận dụng 1:**

a) Rút gọn biểu thức $P(x) = 7x^2(x^2 - 5x + 2) - 5x(x^3 - 7x^2 + 3x)$.

b) Tính giá trị của biểu thức $P(x)$ khi $x = -\dfrac{1}{2}$.

**Thử thách nhỏ:**

Rút gọn biểu thức $x^3(x + 2) - x(x^3 + 2^3) - 2x(x^2 - 2^2)$.

## 2. NHÂN ĐA THỨC VỚI ĐA THỨC

**Nhân hai đa thức tuỳ ý**

**HĐ3:** Tính $(2x - 3) \cdot (x^2 - 5x + 1)$ bằng cách thực hiện các bước sau:
- *Bước 1.* Nhân $2x$ với đa thức $x^2 - 5x + 1$.
- *Bước 2.* Nhân $-3$ với đa thức $x^2 - 5x + 1$.
- *Bước 3.* Cộng các đa thức thu được ở hai bước trên và thu gọn.

<!-- term: Tích của hai đa thức -->
Kết quả thu được là *tích* của đa thức $2x - 3$ với đa thức $x^2 - 5x + 1$.

Tổng quát, ta có quy tắc sau:

<!-- term: Tích của hai đa thức -->
> Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.

**Ví dụ 2:**

Thực hiện phép nhân: $(x + 3) \cdot (2x^2 - 3x - 5)$.

**Giải:**

$(x + 3) \cdot (2x^2 - 3x - 5) = x \cdot (2x^2 - 3x - 5) + 3 \cdot (2x^2 - 3x - 5)$

$= x \cdot 2x^2 + x \cdot (-3x) + x \cdot (-5) + 3 \cdot 2x^2 + 3 \cdot (-3x) + 3 \cdot (-5)$

$= 2x^3 - 3x^2 - 5x + 6x^2 - 9x - 15$

$= 2x^3 - 3x^2 + 6x^2 - 5x - 9x - 15$ ($\leftarrow$ Đổi chỗ)

$= 2x^3 - (3x^2 - 6x^2) - (5x + 9x) - 15$ ($\leftarrow$ Nhóm các hạng tử cùng bậc)

$= 2x^3 + 3x^2 - 14x - 15$.

**Chú ý:**

- Ta có thể trình bày phép nhân trên bằng cách đặt tính nhân:
  $\begin{array}{r@{\;}r@{\;}r@{\;}r@{\;}r} & & 2x^2 & -\,3x & -\,5 \\ \times & & & x & +\,3 \\ \hline & & 6x^2 & -\,9x & -\,15 \\ + & 2x^3 & -\,3x^2 & -\,5x & \\ \hline & 2x^3 & +\,3x^2 & -\,14x & -\,15 \end{array}$ ($\leftarrow$ Nhân $3$ với $2x^2 - 3x - 5$; $\leftarrow$ Nhân $x$ với $2x^2 - 3x - 5$)

> Khi nhân các hạng tử ở dòng dưới với đa thức ở dòng trên, bạn nên nhân các hạng tử theo thứ tự từ bậc thấp đến bậc cao.

Khi trình bày theo cách này ta cần:
- Nhân lần lượt mỗi hạng tử ở dòng dưới với đa thức ở dòng trên và viết kết quả trong một dòng riêng.
- Viết các dòng sao cho các hạng tử cùng bậc thẳng cột với nhau (để thực hiện phép cộng theo cột).

<!-- pdf:39 -->

<!-- term: Tính chất của phép nhân đa thức -->
- Phép nhân đa thức cũng có các tính chất:
  - *Giao hoán*: $A \cdot B = B \cdot A$.
  - *Kết hợp*: $(A \cdot B) \cdot C = A \cdot (B \cdot C)$.
  - *Phân phối đối với phép cộng*: $A \cdot (B + C) = A \cdot B + A \cdot C$.

**Luyện tập 2:**

Tính $(x^3 - 2x^2 + x - 1)(3x - 2)$. Trình bày lời giải theo hai cách.

**Vận dụng 2:**

Rút gọn biểu thức $(x - 2)(2x^3 - x^2 + 1) + (x - 2)x^2(1 - 2x)$.

**Vận dụng 3:** Trở lại *bài toán đoán tuổi*, để giải thích bí mật trong bài toán đoán tuổi của anh Pi, em hãy thực hiện các yêu cầu sau:
- Gọi $x$ là tuổi cần đoán. Tìm hai đa thức (biến $x$) biểu thị kết quả thứ nhất và kết quả thứ hai.
- Tìm đa thức biểu thị kết quả cuối cùng.

Từ đó hãy nêu cách tìm $x$.

## BÀI TẬP

7.23. Thực hiện các phép nhân sau:

a) $6x^2 \cdot (2x^3 - 3x^2 + 5x - 4)$;

b) $(-1,2x^2) \cdot (2,5x^4 - 2x^3 + x^2 - 1,5)$.

7.24. Rút gọn các biểu thức sau:

a) $4x^2(5x^2 + 3) - 6x(3x^3 - 2x + 1) - 5x^3(2x - 1)$;

b) $\dfrac{3}{2}x\left(x^2 - \dfrac{2}{3}x + 2\right) - \dfrac{5}{3}x^2\left(x + \dfrac{6}{5}\right)$.

7.25. Thực hiện các phép nhân sau:

a) $(x^2 - x) \cdot (2x^2 - x - 10)$;

b) $(0,2x^2 - 3x) \cdot 5(x^2 - 7x + 3)$.

7.26.

a) Tính $(x^2 - 2x + 5) \cdot (x - 2)$.

b) Từ đó hãy suy ra kết quả của phép nhân $(x^2 - 2x + 5) \cdot (2 - x)$. Giải thích cách làm.

7.27. Giả sử ba kích thước của một hình hộp chữ nhật là $x$; $x + 1$; $x - 1\text{ (cm)}$ với $x > 1$. Tìm đa thức biểu thị thể tích (đơn vị: $\text{cm}^3$) của hình hộp chữ nhật đó.

7.28. Thực hiện các phép nhân hai đa thức sau:

a) $5x^3 - 2x^2 + 4x - 4$ và $x^3 + 3x^2 - 5$;

b) $-2,5x^4 + 0,5x^2 + 1$ và $4x^3 - 2x + 6$.

7.29. Người ta dùng những chiếc cọc để rào một mảnh vườn hình chữ nhật sao cho mỗi góc vườn đều có một chiếc cọc và hai cọc liên tiếp cắm cách nhau $0,1\text{ m}$. Biết rằng số cọc dùng để rào hết chiều dài của vườn nhiều hơn số cọc dùng để rào hết chiều rộng là $20$ chiếc. Gọi số cọc dùng để rào hết chiều rộng là $x$. Tìm đa thức biểu thị diện tích của mảnh vườn đó.
