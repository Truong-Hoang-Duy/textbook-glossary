---
unit: toan_9
lesson_id: b07
toc_path:
  - "Chương III. Căn bậc hai và căn bậc ba"
  - "Bài 7. Căn bậc hai và căn thức bậc hai"
source_file: "SGK TOAN 9 TAP 1 - KNTT.pdf"
pdf_pages: [46, 50]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:46 -->
<!-- Phần giới thiệu đầu Chương III (nửa trên trang PDF 46): ĐẠI SỐ — CHƯƠNG III: CĂN BẬC HAI VÀ CĂN BẬC BA -->

Ở lớp $7$, các em đã làm quen với khái niệm căn bậc hai số học; biết cách tìm căn bậc hai số học của một số thực không âm và biết cách so sánh các căn bậc hai số học của hai số không âm. Trong chương này, chúng ta sẽ mở rộng khái niệm căn bậc hai số học.

# BÀI 7: CĂN BẬC HAI VÀ CĂN THỨC BẬC HAI

## 🔤 Khái niệm, thuật ngữ

- Căn bậc hai
- Căn thức bậc hai
- Điều kiện xác định của căn thức bậc hai

## 🎯 Kiến thức, kĩ năng

- Nhận biết căn bậc hai của một số thực không âm. Tính được giá trị đúng (hoặc gần đúng) căn bậc hai của một số thực dương bằng máy tính cầm tay.
- Nhận biết căn thức bậc hai của một biểu thức đại số, điều kiện xác định của căn thức bậc hai; tính được giá trị căn thức bậc hai tại những giá trị đã cho của biến.
- Sử dụng hằng đẳng thức căn bậc hai của một bình phương để đơn giản căn thức bậc hai.

## 🔴 Mở đầu

Trong Vật lí, quãng đường $S$ (tính bằng mét) của một vật rơi tự do được cho bởi công thức $S = 4,9t^2$, trong đó $t$ là thời gian rơi (tính bằng giây).

Hỏi sau bao nhiêu giây thì vật sẽ chạm đất nếu được thả rơi tự do từ độ cao $122,5$ mét?

<!-- pdf:47 -->

## 1. CĂN BẬC HAI

**Tìm hiểu khái niệm căn bậc hai**

**HĐ1:** Tìm các số thực $x$ sao cho $x^2 = 49$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 47, OCR bỏ sót nhãn HĐ1 và đọc nhầm Tìm thành Tim -->

> **Căn bậc hai** của số thực không âm $a$ là số thực $x$ sao cho $x^2 = a$.

> **Nhận xét**
>
> - Số âm không có căn bậc hai;
> - Số $0$ có một căn bậc hai duy nhất là $0$;
> - Số dương $a$ có đúng hai căn bậc hai đối nhau là $\sqrt{a}$ (căn bậc hai số học của $a$) và $-\sqrt{a}$.

**Ví dụ 1:** Tìm căn bậc hai của $81$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 47, OCR bỏ sót dòng đề Ví dụ 1 -->

**Giải**

Ta có $\sqrt{81} = 9$ nên $81$ có hai căn bậc hai là $9$ và $-9$.

**Luyện tập 1:** Tìm căn bậc hai của $121$.

**Tính căn bậc hai của một số bằng máy tính cầm tay**

Để tính các căn bậc hai của một số $a > 0$, chỉ cần tính $\sqrt{a}$. Có thể dễ dàng làm điều này bằng cách sử dụng MTCT.

**Ví dụ 2**

Sử dụng MTCT, tính căn bậc hai của $11,1$ (làm tròn đến chữ số thập phân thứ hai).

**Giải**

Bấm các phím `√■` `1` `1` `.` `1` `=` `S⇔D` màn hình hiện kết quả là $3,33166625$. Làm tròn kết quả đến chữ số thập phân thứ hai ta được $\sqrt{11,1} \approx 3,33$.

Vậy căn bậc hai của $11,1$ (làm tròn đến chữ số thập phân thứ hai) là $3,33$ và $-3,33$.

**Luyện tập 2:** Sử dụng MTCT tìm căn bậc hai của $\dfrac{7}{11}$ (làm tròn đến chữ số thập phân thứ hai).

**Tính chất của căn bậc hai**

**HĐ2:** Tính và so sánh $\sqrt{a^2}$ và $|a|$ trong mỗi trường hợp sau:

a) $a = 3$; $\qquad$ b) $a = -3$.

<!-- pdf:48 -->

Tính chất:

<!-- term: Tính chất căn bậc hai của một bình phương -->
> $\sqrt{a^2} = |a|$ với mọi số thực $a$.

**Ví dụ 3:** Không sử dụng MTCT, tính:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 48, OCR bỏ sót nhãn Ví dụ 3 nền xanh -->

a) $1 - \sqrt{2} + \sqrt{\left(1 + \sqrt{2}\right)^2}$; $\qquad$ b) $\sqrt{(-3)^2} + 3$.

**Giải**

a) Ta có $\sqrt{\left(1 + \sqrt{2}\right)^2} = \left|1 + \sqrt{2}\right| = 1 + \sqrt{2}$ nên $1 - \sqrt{2} + \sqrt{\left(1 + \sqrt{2}\right)^2} = 1 - \sqrt{2} + \left(1 + \sqrt{2}\right) = 2$.

b) Ta có $\sqrt{(-3)^2} = |-3| = 3$ nên $\sqrt{(-3)^2} + 3 = 3 + 3 = 6$.

**Luyện tập 3**

a) Không sử dụng MTCT, tính: $\sqrt{6^2}$; $\sqrt{(-5)^2}$; $\sqrt{5} - \sqrt{\left(\sqrt{5} - 1\right)^2}$.

b) So sánh $3$ với $\sqrt{10}$ bằng hai cách:

- Sử dụng MTCT;
- Sử dụng tính chất của căn bậc hai số học đã học ở lớp $7$: Nếu $0 \le a < b$ thì $\sqrt{a} < \sqrt{b}$.

## 2. CĂN THỨC BẬC HAI

**Căn thức bậc hai**

**HĐ3:** Viết biểu thức tính độ dài cạnh huyền $BC$ của tam giác vuông $ABC$, biết $AB = 3\text{ cm}$ và $AC = x\text{ cm}$.

Biểu thức nhận được trong HĐ3 có dạng $\sqrt{A}$, trong đó $A$ là một biểu thức đại số.

Tổng quát, ta có định nghĩa:

> **Căn thức bậc hai** là biểu thức có dạng $\sqrt{A}$, trong đó $A$ là một biểu thức đại số. $A$ được gọi là **biểu thức lấy căn** hoặc **biểu thức dưới dấu căn**.

**HĐ4:** Cho biểu thức $C = \sqrt{2x - 1}$.

a) Tính giá trị của biểu thức tại $x = 5$.

b) Tại $x = 0$ có tính được giá trị của biểu thức không? Vì sao?

> $\sqrt{A}$ xác định khi $A$ lấy giá trị không âm và ta thường viết là $A \ge 0$. Ta nói $A \ge 0$ là **điều kiện xác định** (hay **điều kiện có nghĩa**) của $\sqrt{A}$.

<!-- pdf:49 -->

**Ví dụ 4:** Xét căn thức $\sqrt{2x + 1}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 49, OCR bỏ sót nhãn Ví dụ 4 và đọc sai "căn" thành "cản" -->

a) Tìm điều kiện xác định của căn thức.

b) Tính giá trị của căn thức đã cho tại $x = 0$ và $x = 4$.

**Giải**

a) Điều kiện xác định của căn thức là $2x + 1 \ge 0$ hay $x \ge -\dfrac{1}{2}$.

b) Tại $x = 0$ (thoả mãn điều kiện xác định) căn thức có giá trị là $\sqrt{2 \cdot 0 + 1} = 1$.

Tại $x = 4$ (thoả mãn điều kiện xác định) căn thức có giá trị là $\sqrt{2 \cdot 4 + 1} = 3$.

**Luyện tập 4:** Cho căn thức $\sqrt{5 - 2x}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 49, OCR bỏ sót nhãn Luyện tập 4 nền xanh -->

a) Tìm điều kiện xác định của căn thức.

b) Tính giá trị của căn thức tại $x = 2$.

**Hằng đẳng thức $\sqrt{A^2} = |A|$**

<!-- term: Hằng đẳng thức căn bậc hai của một bình phương -->
Tương tự như căn bậc hai của một số thực không âm, với $A$ là một biểu thức, ta cũng có:

<!-- term: Hằng đẳng thức căn bậc hai của một bình phương -->
> - Với $A \ge 0$ ta có $\sqrt{A} \ge 0$; $\left(\sqrt{A}\right)^2 = A$;
> - $\sqrt{A^2} = |A|$.

**Ví dụ 5:** Rút gọn các biểu thức sau:

a) $\left(\sqrt{1 - x}\right)^2$ với $x < 0$;

b) $\sqrt{1 - 2x + x^2}$ với $x > 2$.

**Giải**

a) Từ giả thiết $x < 0$ suy ra $1 - x > 0$. Do đó

$\left(\sqrt{1 - x}\right)^2 = 1 - x. \quad \leftarrow \text{hằng đẳng thức } \left(\sqrt{A}\right)^2 = A \text{ với mọi } A \ge 0$

b) Áp dụng hằng đẳng thức bình phương của một hiệu và hằng đẳng thức $\sqrt{A^2} = |A|$, ta có $\sqrt{1 - 2x + x^2} = \sqrt{(1 - x)^2} = |1 - x|$.

Do giả thiết $x > 2$ suy ra $1 - x < 0$ nên $|1 - x| = -(1 - x) = x - 1$. Vì vậy
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 49, câu chứa nhiều biểu thức giá trị tuyệt đối trong LaTeX -->

$\sqrt{1 - 2x + x^2} = \sqrt{(1 - x)^2} = x - 1$ với $x > 2$.

<!-- pdf:50 -->

**Luyện tập 5**

a) Rút gọn biểu thức $x\sqrt{x^6}$ ($x < 0$).

b) Rút gọn và tính giá trị của biểu thức $x + \sqrt{4x^2 - 4x + 1}$ tại $x = -2,5$.

**Vận dụng:** Trở lại *tình huống mở đầu*.

a) Viết công thức tính thời gian $t$ (giây) cần thiết để vật rơi được quãng đường $S$ (mét).

b) Sử dụng công thức tìm được trong câu a, hãy trả lời câu hỏi trong tình huống mở đầu.

## BÀI TẬP

3.1. Tìm căn bậc hai của mỗi số sau (làm tròn đến chữ số thập phân thứ hai):

a) $24,5$; $\qquad$ b) $\dfrac{9}{10}$.

3.2. Để chuẩn bị trồng cây trên vỉa hè, người ta để lại những ô đất hình tròn có diện tích khoảng $2\text{ m}^2$. Em hãy ước lượng (với độ chính xác $0,005$) đường kính của các ô đất đó khoảng bao nhiêu mét?

3.3. Tìm điều kiện xác định của $\sqrt{x + 10}$ và tính giá trị của căn thức tại $x = -1$.

3.4. Tính:

$\sqrt{5,1^2}; \quad \sqrt{(-4,9)^2}; \quad -\sqrt{(-0,001)^2}.$

3.5. Rút gọn các biểu thức sau:

a) $\sqrt{\left(2 - \sqrt{5}\right)^2}$;

b) $3\sqrt{x^2} - x + 1$ ($x < 0$);

c) $\sqrt{x^2 - 4x + 4}$ ($x < 2$).

3.6. Không dùng MTCT, chứng tỏ biểu thức $A$ có giá trị là số nguyên:

$A = \sqrt{\left(1 + 2\sqrt{2}\right)^2} - \sqrt{\left(1 - 2\sqrt{2}\right)^2}.$
