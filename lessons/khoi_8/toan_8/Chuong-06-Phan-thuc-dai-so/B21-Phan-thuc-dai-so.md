---
unit: toan_8
lesson_id: b21
toc_path:
  - "Chương VI. Phân thức đại số"
  - "Bài 21. Phân thức đại số"
source_file: "SGK TOAN 8 TAP 2 - KNTT.pdf"
pdf_pages: [5, 8]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:5 -->
<!-- Trang mở đầu Chương VI (PDF 5): Chương VI. PHÂN THỨC ĐẠI SỐ (ĐẠI SỐ) — Ở lớp 7, từ tập hợp Z các số nguyên ta đã xây dựng tập hợp Q các số hữu tỉ mà mọi số nguyên cũng đều là số hữu tỉ. Tương tự, từ tập hợp các đa thức ta cũng có thể xây dựng một tập hợp mới gồm các phân thức đại số mà mọi đa thức cũng đều là phân thức đại số. Trong chương này các em sẽ biết thế nào là phân thức đại số, biết cách cộng, trừ, nhân, chia các phân thức đại số tương tự như cộng, trừ, nhân, chia các phân số. -->

# BÀI 21: PHÂN THỨC ĐẠI SỐ

## 🔤 Khái niệm, thuật ngữ

- Phân thức đại số
- Tử thức, mẫu thức
- Hai phân thức bằng nhau
- Điều kiện xác định của phân thức
- Giá trị của phân thức

## 🎯 Kiến thức, kĩ năng

- Nhận biết phân thức đại số, tử thức và mẫu thức của một phân thức.
- Viết điều kiện xác định của phân thức và tính giá trị của phân thức tại giá trị của biến thoả mãn điều kiện xác định.
- Nhận biết hai phân thức bằng nhau.

## 🔴 Mở đầu

Trong một cuộc đua xe đạp, các vận động viên phải hoàn thành ba chặng đua bao gồm $9\text{ km}$ leo dốc; $5\text{ km}$ xuống dốc và $36\text{ km}$ đường bằng phẳng. Vận tốc trung bình của một vận động viên trên chặng đường bằng phẳng hơn vận tốc leo dốc $5\text{ km/h}$ và kém vận tốc xuống dốc $10\text{ km/h}$. Nếu biết vận tốc trung bình của vận động viên trên chặng đường bằng phẳng thì có tính được thời gian hoàn thành cuộc đua của vận động viên đó không?

![Minh hoạ cuộc đua xe đạp](img/H8-toan-b21-01.png)

<!-- pdf:6 -->

## 1. PHÂN THỨC ĐẠI SỐ

**Phân thức đại số là gì?**

**HĐ1:** Trong *tình huống mở đầu*, giả sử vận tốc trung bình của một vận động viên đi xe đạp trên $36\text{ km}$ đường bằng phẳng là $x\text{ (km/h)}$. Hãy viết biểu thức biểu thị thời gian vận động viên đó hoàn thành chặng leo dốc, chặng xuống dốc, chặng đường bằng phẳng.

**HĐ2:** Viết biểu thức biểu thị tỉ số giữa chiều rộng và chiều dài của một hình chữ nhật có chiều rộng là $x\text{ (cm)}$ và chiều dài là $y\text{ (cm)}$.

Các biểu thức nhận được ở HĐ1, HĐ2 và các biểu thức như $\dfrac{2x - 1}{3x + 1}; \dfrac{x^2 - x + 1}{2x + 1}; \dots$ được gọi là những *phân thức đại số*. Tổng quát, ta có định nghĩa:

> Một **phân thức đại số** (hay nói gọn là **phân thức**) là một biểu thức có dạng $\dfrac{A}{B}$, trong đó $A, B$ là hai đa thức và $B$ khác đa thức $0$.
>
> $A$ được gọi là **tử thức** (hoặc **tử**) và $B$ được gọi là **mẫu thức** (hoặc **mẫu**).

**Nhận xét.** Mỗi đa thức cũng được coi là một phân thức với mẫu thức bằng $1$. Đặc biệt, số $0$ và số $1$ cũng là những phân thức đại số.

**Ví dụ 1:**

a) Cách viết nào sau đây **không** cho một phân thức?

$\dfrac{6y^3z}{x^2}; \quad \dfrac{xy + z}{-3}; \quad \dfrac{y + z}{0}; \quad \dfrac{0}{x + 1}; \quad x^3 - xy.$

b) Viết mẫu thức của mỗi phân thức trong các cách viết trên.

**Giải**

a) Trong các cách viết trên, $\dfrac{y + z}{0}$ không phải là một phân thức.

b) Các phân thức $\dfrac{6y^3z}{x^2}; \dfrac{xy + z}{-3}; \dfrac{0}{x + 1}; x^3 - xy$ có mẫu thức lần lượt là: $x^2; -3; x + 1; 1$.

**Luyện tập 1:**

Trong các cặp phân thức sau, cặp phân thức nào có cùng mẫu thức?

a) $\dfrac{-20x}{3y^2}$ và $\dfrac{4x^3}{5y^2}$; $\qquad$ b) $\dfrac{5x - 10}{x^2 + 1}$ và $\dfrac{5x - 10}{x^2 - 1}$; $\qquad$ c) $\dfrac{5x + 10}{4x - 8}$ và $\dfrac{4 - 2x}{4(x - 2)}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 6, ba cặp phân thức của Luyện tập 1 -->

<!-- pdf:7 -->

**Tranh luận**

- **Tròn:** $\dfrac{3 - 2x}{3 + \dfrac{1}{x}}$ không phải là phân thức.
- **Vuông:** $\dfrac{3 - 2x}{3 + \dfrac{1}{x}}$ là phân thức chứ!
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 7, hai bóng thoại của Tròn và Vuông đặt ngang nhau -->

Theo em, bạn nào đúng?

## 2. HAI PHÂN THỨC BẰNG NHAU

Ở lớp 6 các em đã học quy tắc bằng nhau của hai phân số. Tương tự ta có:

> Hai phân thức $\dfrac{A}{B}$ và $\dfrac{C}{D}$ gọi là **bằng nhau** nếu $AD = BC$.
>
> $\dfrac{A}{B} = \dfrac{C}{D}$ nếu $AD = BC$.

**Ví dụ 2:**

Giải thích vì sao $\dfrac{1 + x}{1 - x^2} = \dfrac{1}{1 - x}$.

**Giải**

Vì $(1 + x)(1 - x) = (1 - x^2) \cdot 1$ nên $\dfrac{1 + x}{1 - x^2} = \dfrac{1}{1 - x}$.

**Luyện tập 2:** Khẳng định sau đúng hay sai? Vì sao?

$\dfrac{1}{x^2 + x + 1} = \dfrac{1 - x}{1 - x^3}.$

## 3. ĐIỀU KIỆN XÁC ĐỊNH VÀ GIÁ TRỊ CỦA PHÂN THỨC TẠI MỘT GIÁ TRỊ ĐÃ CHO CỦA BIẾN

**Giá trị của phân thức tại một giá trị đã cho của biến**

Khi thay các biến trong một phân thức đại số bằng các số, ta được một biểu thức số (nếu mẫu số nhận được là số khác $0$). Giá trị của biểu thức số đó gọi là **giá trị của phân thức** tại các giá trị đã cho của biến.

Như vậy, để tính giá trị của phân thức tại những giá trị cho trước của biến ta thay các giá trị cho trước của biến vào phân thức đó rồi tính giá trị của biểu thức số nhận được.

**Ví dụ 3:** Tính giá trị của phân thức $\dfrac{x^2 - x - 1}{x^2 + 3x}$ tại $x = 2; x = 1$.

**Giải**

Tại $x = 2$, phân thức có giá trị là $\dfrac{2^2 - 2 - 1}{2^2 + 3 \cdot 2} = \dfrac{1}{10}$.

Tại $x = 1$, phân thức có giá trị là $\dfrac{1^2 - 1 - 1}{1^2 + 3 \cdot 1} = \dfrac{-1}{4}$.

<!-- pdf:8 -->

**Điều kiện xác định của phân thức**

Vì phép chia chỉ thực hiện được khi số chia khác $0$ nên chỉ có thể tính được giá trị của phân thức $\dfrac{x^2 - x - 1}{x^2 + 3x}$ khi $x$ thoả mãn điều kiện $x^2 + 3x \ne 0$.

Ta nói rằng $x^2 + 3x \ne 0$ là *điều kiện xác định* của phân thức $\dfrac{x^2 - x - 1}{x^2 + 3x}$.

> **Điều kiện xác định của phân thức** $\dfrac{A}{B}$ là điều kiện của biến để giá trị của mẫu thức $B$ khác $0$.

**Chú ý.** Ta chỉ cần quan tâm đến điều kiện xác định khi tính giá trị của phân thức.

**Ví dụ 4:**

Viết điều kiện xác định của phân thức $\dfrac{x - 3}{x + 2}$.

**Giải**

Điều kiện xác định của phân thức là $x + 2 \ne 0$ hay $x \ne -2$.

**Luyện tập 3:**

Viết điều kiện xác định của phân thức $\dfrac{x + 1}{x - 1}$ và tính giá trị của phân thức tại $x = 2$.

**Vận dụng**

Trở lại *tình huống mở đầu*. Nếu biết vận tốc của vận động viên trên chặng đường bằng phẳng là $30\text{ km/h}$, hãy tính thời gian vận động viên đó hoàn thành mỗi chặng đua và tính tổng thời gian để hoàn thành cuộc đua.

## BÀI TẬP

6.1. Viết tử thức và mẫu thức của phân thức $\dfrac{5x - 2}{3}$.

6.2. Trong các cặp phân thức sau, cặp phân thức nào có mẫu giống nhau?

a) $\dfrac{-20x}{3y^2}$ và $\dfrac{4x}{5y^2}$; $\qquad$ b) $\dfrac{3x - 1}{x^2 + 1}$ và $\dfrac{3x - 1}{x + 1}$; $\qquad$ c) $\dfrac{x - 1}{3x + 6}$ và $\dfrac{x + 1}{3(x + 2)}$.

6.3. Vì sao các kết luận sau đúng?

a) $\dfrac{-6}{-4y} = \dfrac{3y}{2y^2}$; $\qquad$ b) $\dfrac{x + 3}{5} = \dfrac{x^2 + 3x}{5x}$; $\qquad$ c) $\dfrac{3x(4x + 1)}{16x^2 - 1} = \dfrac{-3x}{1 - 4x}$.

6.4. Viết điều kiện xác định của phân thức $\dfrac{x^2 + x - 2}{x^3 + 2}$. Tính giá trị của phân thức trên lần lượt tại $x = 0; x = 1; x = 2$.

6.5. Cho $A$ là một đa thức khác $0$ tuỳ ý. Hãy giải thích vì sao $\dfrac{0}{A} = 0$ và $\dfrac{A}{A} = 1$.

6.6. Một ô tô chạy với vận tốc trung bình là $x\text{ (km/h)}$.

a) Viết biểu thức biểu thị thời gian ô tô (tính bằng giờ) chạy hết quãng đường $120\text{ km}$.

b) Tính thời gian ô tô đi được $120\text{ km}$ trong trường hợp vận tốc trung bình của ô tô là $60\text{ km/h}$.

## 📷 Danh sách hình trong bài

| Mã hình | Trang PDF | Vị trí trong bài | Chú thích gốc |
| --- | :---: | --- | --- |
| H8-toan-b21-01 | 5 | Mở đầu | (sách không đánh số, ảnh minh hoạ cuộc đua xe đạp) |
