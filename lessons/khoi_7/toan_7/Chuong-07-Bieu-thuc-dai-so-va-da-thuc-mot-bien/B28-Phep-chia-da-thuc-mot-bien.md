---
unit: toan_7
lesson_id: b28
toc_path:
  - "Chương VII. Biểu thức đại số và đa thức một biến"
  - "Bài 28. Phép chia đa thức một biến"
source_file: "SGK Toan 7 Tap 2.pdf"
pdf_pages: [40, 44]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:40 -->

# BÀI 28: PHÉP CHIA ĐA THỨC MỘT BIẾN

## 🔤 Khái niệm, thuật ngữ

- Phép chia hết
- Phép chia có dư
- Thương, dư (trong phép chia đa thức)

## 🎯 Kiến thức, kĩ năng

- Thực hiện các phép tính chia hai đa thức một biến.
- Nhận biết và vận dụng các tính chất của các phép tính về đa thức trong tính toán.

## 🔴 Mở đầu

*Bài toán:* Tìm đa thức $P$ sao cho $A = B \cdot P$, trong đó $A = 2x^4 - 3x^3 - 3x^2 + 6x - 2$ và $B = x^2 - 2$.

> - Mình nghĩ mãi mà chưa giải được bài toán này. Vuông có cách nào giải không?
> - Ừ nhỉ! nếu $A$ và $B$ là hai số thì chỉ việc lấy $A$ chia cho $B$ là xong nhưng $A$ và $B$ lại là hai đa thức.
> - Cũng thế thôi các em ạ. Trước hết các em phải tìm hiểu cách chia hai đa thức.

## 1. LÀM QUEN VỚI PHÉP CHIA ĐA THỨC

> **Phép chia hết**
>
> 1. Xét hai đơn thức $6x^4$ và $-2x^3$, ta thấy $6x^4 = (-2x^3) \cdot (-3x)$.
> Từ đó, tương tự như đối với các số, ta cũng có thể viết:
> $6x^4 : (-2x^3) = -3x$, hay $\dfrac{6x^4}{-2x^3} = -3x$
> và nói rằng đó là một *phép chia hết*.
>
> 2. Một cách tổng quát, cho hai đa thức $A$ và $B$ với $B \ne 0$. Nếu có một đa thức $Q$ sao cho $A = B \cdot Q$ thì ta có **phép chia hết**:
> $A : B = Q$ hay $\dfrac{A}{B} = Q$, trong đó:
> - $A$ là **đa thức bị chia**;
> - $B$ là **đa thức chia**;
> - $Q$ là **đa thức thương** (gọi tắt là **thương**).
> Khi đó ta còn nói đa thức $A$ *chia hết cho* đa thức $B$.

> Kí hiệu $B \ne 0$ có nghĩa $B$ không phải là *đa thức không*.

<!-- pdf:41 -->

> 3. Để thực hiện phép chia $6x^4$ cho $(-2x^3)$, ta làm như sau:
> - Chia hai hệ số: $6 : (-2) = -3$.
> - Chia hai luỹ thừa của biến: $x^4 : x^3 = x$.
> - Nhân hai kết quả trên, ta tìm được thương là $-3x$.

> Nhớ lại quy tắc chia hai luỹ thừa cùng cơ số nhé!

**Khi nào thì $ax^n$ chia hết cho $bx^m$?**

**HĐ1:** Tìm thương của mỗi phép chia hết sau:

a) $12x^3 : 4x$;

b) $(-2x^4) : x^4$;

c) $2x^5 : 5x^2$.

> $12x^3 : 4x$ được hiểu là $12x^3 : (4x)$.

**HĐ2:** Giả sử $x \ne 0$. Hãy cho biết:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 41, OCR đọc sai nhãn HĐ2 và chữ Giả sử -->

a) Với điều kiện nào (của hai số mũ) thì thương hai luỹ thừa của $x$ cũng là một luỹ thừa của $x$ với số mũ nguyên dương?

b) Thương hai luỹ thừa của $x$ cùng bậc bằng bao nhiêu?

<!-- term: Chia đơn thức cho đơn thức -->
> Cho hai đơn thức $ax^m$ và $bx^n$ ($m, n \in \mathbb{N}$; $a, b \in \mathbb{R}$ và $b \ne 0$). Khi đó nếu $m \ge n$ thì phép chia $ax^m$ cho $bx^n$ là *phép chia hết* và ta có:
> $ax^m : bx^n = \dfrac{a}{b}x^{m - n}$ (quy ước: $x^0 = 1$).

**Luyện tập 1:**

Thực hiện các phép chia sau:

a) $3x^7 : \dfrac{1}{2}x^4$;

b) $(-2x) : x$;

c) $0,25x^5 : (-5x^2)$.

## 2. CHIA ĐA THỨC CHO ĐA THỨC, TRƯỜNG HỢP CHIA HẾT

> **Cách đặt tính chia**
>
> Để chia đa thức $A = 2x^4 - 13x^3 + 15x^2 + 11x - 3$ cho đa thức $B = x^2 - 4x - 3$, ta làm như sau:
> - *Bước 1. Đặt tính chia* tương tự chia hai số tự nhiên. Lấy hạng tử bậc cao nhất của $A$ chia cho hạng tử bậc cao nhất của $B$:
>   $2x^4 : x^2 = 2x^2$.
> - *Bước 2.* Lấy $A$ trừ đi tích $B \cdot (2x^2)$, ta được dư thứ nhất là $-5x^3 + 21x^2 + 11x - 3$:
>   $\begin{array}{r@{\;}l|l} & 2x^4 - 13x^3 + 15x^2 + 11x - 3 & x^2 - 4x - 3 \\ \cline{3-3} B \cdot (2x^2) \rightarrow - & 2x^4 - \phantom{1}8x^3 - \phantom{1}6x^2 & 2x^2 \quad \leftarrow 2x^4 : x^2 = 2x^2 \\ \cline{1-2} A - B \cdot (2x^2) \rightarrow \phantom{-} & \phantom{2x^4} - 5x^3 + 21x^2 + 11x - 3 & \\ & \phantom{2x^4}\text{(Dư thứ nhất)} & \end{array}$

<!-- pdf:42 -->

> - *Bước 3.* Lấy hạng tử bậc cao nhất của dư thứ nhất chia cho hạng tử bậc cao nhất của $B$:
>   $(-5x^3) : x^2 = -5x$.
> - *Bước 4.* Lấy dư thứ nhất trừ đi tích $B \cdot (-5x)$, ta được dư thứ hai là $x^2 - 4x - 3$:
>   $\begin{array}{r@{\;}l|l} & 2x^4 - 13x^3 + 15x^2 + 11x - 3 & x^2 - 4x - 3 \\ \cline{3-3} - & 2x^4 - \phantom{1}8x^3 - \phantom{1}6x^2 & 2x^2 - 5x \quad \leftarrow (-5x^3) : x^2 = -5x \\ \cline{1-2} & \phantom{2x^4} - 5x^3 + 21x^2 + 11x - 3 & \\ B \cdot (-5x) \rightarrow - & \phantom{2x^4} - 5x^3 + 20x^2 + 15x & \\ \cline{1-2} \text{(Dư thứ nhất)} - B \cdot (-5x) \rightarrow \phantom{-} & \phantom{2x^4 - 13x^3 + \;} x^2 - \phantom{1}4x - 3 & \\ & \phantom{2x^4 - 13x^3}\text{(Dư thứ hai)} & \end{array}$
> - *Bước 5.* Làm tương tự như trên, ta được:
>   $\begin{array}{r@{\;}l|l} & 2x^4 - 13x^3 + 15x^2 + 11x - 3 & x^2 - 4x - 3 \\ \cline{3-3} - & 2x^4 - \phantom{1}8x^3 - \phantom{1}6x^2 & 2x^2 - 5x + 1 \\ \cline{1-2} & \phantom{2x^4} - 5x^3 + 21x^2 + 11x - 3 & \\ - & \phantom{2x^4} - 5x^3 + 20x^2 + 15x & \\ \cline{1-2} & \phantom{2x^4 - 13x^3 + \;} x^2 - \phantom{1}4x - 3 & \\ - & \phantom{2x^4 - 13x^3 + \;} x^2 - \phantom{1}4x - 3 & \\ \cline{1-2} & \phantom{2x^4 - 13x^3 + 15x^2 + 11x} 0 & \end{array}$
>
> Dư cuối cùng bằng $0$ nên quá trình chia kết thúc.
> Ta được thương là đa thức $2x^2 - 5x + 1$.

> ❓ Kiểm tra lại rằng ta có phép chia hết $A : B = 2x^2 - 5x + 1$, nghĩa là xảy ra:
> $A = B \cdot (2x^2 - 5x + 1)$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 42, OCR lệch thứ tự do phần đặt tính chia nhiều cột -->

**Chú ý:** Khi chia đa thức cho một đơn thức thì ta có thể không cần đặt tính chia. Cách làm như trong ví dụ sau:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 42, đúng nguyên văn mục Chú ý -->

$(-6x^5 + 7x^4 - 6x^3) : 3x^3 = (-6x^5 : 3x^3) + (7x^4 : 3x^3) + (-6x^3 : 3x^3) = -2x^2 + \dfrac{7}{3}x - 2$.

**Luyện tập 2:**

Thực hiện phép chia:

a) $(-x^6 + 5x^4 - 2x^3) : 0,5x^2$.

b) $(9x^2 - 4) : (3x + 2)$.

> Viết đa thức bị chia là: $9x^2 + 0x - 4$ sẽ dễ làm hơn.

**Vận dụng:**

Em hãy giải bài toán trong *tình huống mở đầu*.

<!-- pdf:43 -->

## 3. CHIA ĐA THỨC CHO ĐA THỨC, TRƯỜNG HỢP CHIA CÓ DƯ

**Phép chia có dư**

Bốn bước đầu tiên khi chia đa thức $D = 5x^3 - 3x^2 - x + 7$ cho đa thức $E = x^2 + 1$ được viết gọn như sau:

$\begin{array}{r@{\;}l|l} & 5x^3 - 3x^2 - \phantom{6}x + \phantom{1}7 & x^2 + 1 \\ \cline{3-3} - & 5x^3 \phantom{\,-\,3x^2} + 5x & 5x - 3 \\ \cline{1-2} \text{(Dư thứ nhất)} & \phantom{5x^3} - 3x^2 - 6x + \phantom{1}7 & \\ - & \phantom{5x^3} - 3x^2 \phantom{\,-\,6x} - \phantom{1}3 & \\ \cline{1-2} \text{(Dư thứ hai)} & \phantom{5x^3 - 3x^2} - 6x + 10 & \end{array}$

> Nếu đa thức ở một dòng khuyết một hạng tử bậc nào đó thì hãy để một khoảng trống ứng với hạng tử đó.

**HĐ3:** Hãy mô tả lại các bước đã thực hiện trong phép chia đa thức $D$ cho đa thức $E$.

**HĐ4:** Kí hiệu dư thứ hai là $G = -6x + 10$. Đa thức này có bậc bằng $1$. Lúc này phép chia có thể tiếp tục được không? Vì sao?

**HĐ5:** Hãy kiểm tra lại đẳng thức: $D = E \cdot (5x - 3) + G$.

Phép chia đa thức $D$ cho đa thức $E$ trong trường hợp này được gọi là **phép chia có dư** với *đa thức thương* là $5x - 3$ và *đa thức dư* là $G$.

<!-- term: Thương và dư trong phép chia đa thức -->
> Khi chia đa thức $A$ cho đa thức $B$:
> - Đa thức dư $R$ phải bằng $0$ hoặc có bậc nhỏ hơn bậc của $B$.
> - Nếu thương là đa thức $Q$, dư là $R$ thì ta có đẳng thức $A = BQ + R$.

**Luyện tập 3:**

Tìm dư $R$ và thương $Q$ trong phép chia đa thức $A = 3x^4 - 6x - 5$ cho đa thức $B = x^2 + 3x - 1$ rồi viết $A$ dưới dạng $A = B \cdot Q + R$.

**Thử thách nhỏ:**

> - Đố Vuông tìm được dư trong phép chia $x^3 - 3x^2 + x - 1$ cho $x^2 - 3x$.
> - Mình chỉ nhìn qua cũng biết được dư là $x - 1$.

Em có biết tại sao Vuông làm nhanh thế không?

<!-- pdf:44 -->

## BÀI TẬP

7.30. Tính:

a) $8x^5 : 4x^3$;

b) $120x^7 : (-24x^5)$;

c) $\dfrac{3}{4}(-x)^3 : \dfrac{1}{8}x$;

d) $-3,72x^4 : (-4x^2)$.

7.31. Thực hiện các phép chia đa thức sau:

a) $(-5x^3 + 15x^2 + 18x) : (-5x)$;

b) $(-2x^5 - 4x^3 + 3x^2) : 2x^2$.

7.32. Thực hiện các phép chia đa thức sau bằng cách đặt tính chia:

a) $(6x^3 - 2x^2 - 9x + 3) : (3x - 1)$;

b) $(4x^4 + 14x^3 - 21x - 9) : (2x^2 - 3)$.

7.33. Thực hiện phép chia $0,5x^5 + 3,2x^3 - 2x^2$ cho $0,25x^n$ trong mỗi trường hợp sau:

a) $n = 2$;

b) $n = 3$.

7.34. Trong mỗi trường hợp sau đây, tìm thương $Q(x)$ và dư $R(x)$ trong phép chia $F(x)$ cho $G(x)$ rồi biểu diễn $F(x)$ dưới dạng:

$F(x) = G(x) \cdot Q(x) + R(x)$.

a) $F(x) = 6x^4 - 3x^3 + 15x^2 + 2x - 1$; $G(x) = 3x^2$.

b) $F(x) = 12x^4 + 10x^3 - x - 3$; $G(x) = 3x^2 + x + 1$.

7.35. Bạn Tâm lúng túng khi muốn tìm thương và dư trong phép chia đa thức $21x - 4$ cho $3x^2$. Em có thể giúp bạn Tâm được không?
