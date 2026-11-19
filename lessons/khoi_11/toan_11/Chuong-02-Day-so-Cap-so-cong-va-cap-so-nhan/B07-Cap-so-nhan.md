---
unit: toan_11
lesson_id: b07
toc_path:
  - "Chương II. Dãy số. Cấp số cộng và cấp số nhân"
  - "Bài 7. Cấp số nhân"
source_file: "SGK TOAN 11 - KNTT - TAP 1.pdf"
pdf_pages: [53, 56]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:53 -->

# BÀI 7: CẤP SỐ NHÂN

## 🔤 Thuật ngữ

- Cấp số nhân
- Công bội
- Số hạng tổng quát
- Tổng của $n$ số hạng đầu

## 🎯 Kiến thức, kĩ năng

- Nhận biết một dãy số là cấp số nhân.
- Giải thích công thức xác định số hạng tổng quát của cấp số nhân.
- Tính tổng của $n$ số hạng đầu của cấp số nhân.
- Giải quyết một số vấn đề thực tiễn gắn với cấp số nhân để giải một số bài toán liên quan đến thực tiễn.

## 🔴 Mở đầu

Một công ty tuyển một chuyên gia về công nghệ thông tin với mức lương năm đầu là $240$ triệu đồng và cam kết sẽ tăng thêm $5\%$ lương mỗi năm so với năm liền trước đó. Tính tổng số lương mà chuyên gia đó nhận được sau khi làm việc cho công ty $10$ năm (làm tròn đến triệu đồng).

## 1. ĐỊNH NGHĨA

**HĐ1:** Nhận biết cấp số nhân

Cho dãy số $(u_n)$ với $u_n = 3 \cdot 2^n$.

a) Viết năm số hạng đầu của dãy số này.

b) Dự đoán hệ thức truy hồi liên hệ giữa $u_n$ và $u_{n-1}$.

> Hãy xét tỉ số $\frac{u_n}{u_{n-1}}$.

> - **Cấp số nhân** là một dãy số (hữu hạn hay vô hạn), trong đó kể từ số hạng thứ hai, mỗi số hạng đều là tích của số hạng đứng ngay trước nó với một số không đổi $q$.
>   Số $q$ được gọi là **công bội** của cấp số nhân.
> - Cấp số nhân $(u_n)$ với công bội $q$ được cho bởi hệ thức truy hồi
>   $u_n = u_{n-1} \cdot q$ với $n \ge 2$.

> ❓ Dãy số không đổi $a, a, a, \dots$ có phải là một cấp số nhân không?

**Ví dụ 1:** Cho cấp số nhân có số hạng đầu $u_1 = 5$ và công bội $q = -2$. Viết năm số hạng đầu của cấp số nhân này.

**Giải:**

Năm số hạng đầu của cấp số nhân này là:

$u_1 = 5, u_2 = u_1 \cdot q = 5 \cdot (-2) = -10, u_3 = u_2 \cdot q = (-10) \cdot (-2) = 20,$

$u_4 = u_3 \cdot q = 20 \cdot (-2) = -40, u_5 = u_4 \cdot q = (-40) \cdot (-2) = 80.$

**Ví dụ 2:** Cho dãy số $(u_n)$ với $u_n = \frac{1}{3^{n-1}}$. Chứng minh rằng dãy số này là một cấp số nhân. Xác định số hạng đầu và công bội của nó.

<!-- pdf:54 -->

**Giải:**

> Để chứng minh dãy số $(u_n)$ gồm các số khác $0$ là một cấp số nhân, hãy chứng minh tỉ số $\frac{u_n}{u_{n-1}}$ không đổi.

Với mọi $n \ge 2$, ta có

$\frac{u_n}{u_{n-1}} = \frac{1}{3^{n-1}} \cdot \frac{3^{n-2}}{1} = \frac{1}{3},$

tức là $u_n = \frac{1}{3} \cdot u_{n-1}$ với mọi $n \ge 2$.

Vậy $(u_n)$ là một cấp số nhân với số hạng đầu $u_1 = \frac{1}{3^0} = 1$ và công bội $q = \frac{1}{3}$.

**Luyện tập 1:** Cho dãy số $(u_n)$ với $u_n = 2 \cdot 5^n$. Chứng minh rằng dãy số này là một cấp số nhân. Xác định số hạng đầu và công bội của nó.

## 2. SỐ HẠNG TỔNG QUÁT

**HĐ2:** Công thức số hạng tổng quát của cấp số nhân

Cho cấp số nhân $(u_n)$ với số hạng đầu $u_1$ và công bội $q$.

a) Tính các số hạng $u_2, u_3, u_4, u_5$ theo $u_1$ và $q$.

b) Dự đoán công thức tính số hạng thứ $n$ theo $u_1$ và $q$.

<!-- term: Số hạng tổng quát của cấp số nhân -->
> Nếu một cấp số nhân có số hạng đầu $u_1$ và công bội $q$ thì **số hạng tổng quát** $u_n$ của nó được xác định bởi công thức
>
> $u_n = u_1 \cdot q^{n-1}$ với $n \ge 2$.

**Ví dụ 3:** Tìm năm số hạng đầu và số hạng thứ $100$ của cấp số nhân: $8, -4, \dots$

**Giải:**

Cấp số nhân này có số hạng đầu $u_1 = 8$ và công bội $q = \frac{-4}{8} = -\frac{1}{2}$.

Do đó năm số hạng đầu là: $8, -4, 2, -1, \frac{1}{2}$.

Số hạng thứ $100$ là: $u_{100} = u_1 \cdot q^{99} = 8 \cdot \left(-\frac{1}{2}\right)^{99} = -\frac{1}{2^{96}}$.

**Ví dụ 4:** Cho một cấp số nhân gồm các số hạng dương. Biết số hạng thứ $10$ bằng $1\,536$ và số hạng thứ $12$ bằng $6\,144$. Tìm số hạng thứ $20$ của cấp số nhân đó.

**Giải:**

Giả sử $u_1$ là số hạng đầu và $q$ là công bội của cấp số nhân đã cho. Ta có:

$\begin{cases} u_{10} = u_1 \cdot q^9 = 1\,536 \\ u_{12} = u_1 \cdot q^{11} = 6\,144. \end{cases}$

Từ đây suy ra $q^2 = 4$, tức là $q = 2$ hoặc $q = -2$.

Với $q = 2$, ta tính được $u_1 = 3$.

Với $q = -2$ ta tính được $u_1 = -3$ (trường hợp này loại vì $u_1 > 0$ theo giả thiết).

<!-- pdf:55 -->

Do đó $u_1 = 3$ và $q = 2$.

Vậy số hạng thứ $20$ của cấp số nhân đã cho là $u_{20} = u_1 \cdot q^{19} = 3 \cdot 2^{19} = 1\,572\,864$.

**Luyện tập 2:** Trong một lọ nuôi cấy vi khuẩn, ban đầu có $5\,000$ con vi khuẩn và số lượng vi khuẩn tăng lên thêm $8\%$ mỗi giờ. Hỏi sau $5$ giờ thì số lượng vi khuẩn là bao nhiêu?

## 3. TỔNG CỦA $n$ SỐ HẠNG ĐẦU CỦA MỘT CẤP SỐ NHÂN

**HĐ3:** Xây dựng công thức tính tổng $n$ số hạng đầu của cấp số nhân

Cho cấp số nhân $(u_n)$ với số hạng đầu $u_1 = a$ và công bội $q \ne 1$.

Để tính tổng của $n$ số hạng đầu

$S_n = u_1 + u_2 + \dots + u_{n-1} + u_n,$

thực hiện lần lượt các yêu cầu sau:

a) Biểu diễn mỗi số hạng trong tổng trên theo $u_1$ và $q$ để được biểu thức tính tổng $S_n$ chỉ chứa $u_1$ và $q$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 55, OCR đọc sai dấu mỗi, tổng, để -->

b) Từ kết quả phần a, nhân cả hai vế với $q$ để được biểu thức tính tích $q \cdot S_n$ chỉ chứa $u_1$ và $q$.

c) Trừ từng vế hai đẳng thức nhận được ở a và b và giản ước các số hạng đồng dạng để tính $(1 - q)S_n$ theo $u_1$ và $q$. Từ đó suy ra công thức tính $S_n$.

<!-- term: Tổng của n số hạng đầu của cấp số nhân -->
> Cho cấp số nhân $(u_n)$ với công bội $q \ne 1$. Đặt $S_n = u_1 + u_2 + \dots + u_n$. Khi đó
>
> $S_n = \frac{u_1(1 - q^n)}{1 - q}.$

> ❓ Nếu cấp số nhân có công bội $q = 1$ thì tổng $n$ số hạng đầu $S_n$ của nó bằng bao nhiêu?

**Ví dụ 5:** Giải bài toán ở *tình huống mở đầu*.

**Giải:**

Lương hằng năm (triệu đồng) của chuyên gia lập thành một cấp số nhân, với số hạng đầu $u_1 = 240$ và công bội $q = 1,05$. Tổng số lương của chuyên gia đó sau $10$ năm chính là tổng của $10$ số hạng đầu của cấp số nhân này và bằng

$S_{10} = \frac{u_1(1 - q^{10})}{1 - q} = \frac{240\left[1 - (1,05)^{10}\right]}{1 - 1,05} \approx 3\,019.$

Vậy tổng số lương (làm tròn đến triệu đồng) của chuyên gia đó sau $10$ năm là $3\,019$ triệu đồng hay $3,019$ tỉ đồng.

**Ví dụ 6:** Cần lấy tổng của bao nhiêu số hạng đầu của cấp số nhân $2, 6, 18, \dots$ để được kết quả bằng $728$?

<!-- pdf:56 -->

**Giải:**

Cấp số nhân này có số hạng đầu $u_1 = 2$ và công bội $q = 3$. Gọi $n$ là số các số hạng đầu cần lấy. Ta có

$728 = S_n = u_1 + u_2 + \dots + u_n = \frac{u_1(1 - q^n)}{1 - q} = \frac{2(1 - 3^n)}{1 - 3} = 3^n - 1.$

Từ đây ta được $3^n = 729 = 3^6$. Suy ra $n = 6$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 56, OCR dính chữ Suyran -->

Vậy phải lấy $6$ số hạng đầu của cấp số nhân đã cho để được tổng bằng $728$.

**Vận dụng:** Một nhà máy tuyển thêm công nhân vào làm việc trong thời hạn ba năm và đưa ra hai phương án lựa chọn về lương như sau:

- Phương án 1: Lương tháng khởi điểm là $5$ triệu đồng và sau mỗi quý, lương tháng sẽ tăng thêm $500$ nghìn đồng.
- Phương án 2: Lương tháng khởi điểm là $5$ triệu đồng và sau mỗi quý, lương tháng sẽ tăng thêm $5\%$.

Với phương án nào thì tổng lương nhận được sau ba năm làm việc của người công nhân sẽ lớn hơn?

## ✏️ BÀI TẬP

**2.15.** Xác định công bội, số hạng thứ $5$, số hạng tổng quát và số hạng thứ $100$ của mỗi cấp số nhân sau:

a) $1, 4, 16, \dots$;

b) $2, -\frac{1}{2}, \frac{1}{8}, \dots$

**2.16.** Viết năm số hạng đầu của mỗi dãy số $(u_n)$ sau và xem nó có phải là cấp số nhân không. Nếu nó là cấp số nhân, hãy tìm công bội $q$ và viết công thức số hạng tổng quát của nó dưới dạng $u_n = u_1 \cdot q^{n-1}$.

a) $u_n = 5n$;

b) $u_n = 5^n$;

c) $u_1 = 1, u_n = nu_{n-1}$;

d) $u_1 = 1, u_n = 5u_{n-1}$.

**2.17.** Một cấp số nhân có số hạng thứ $6$ bằng $96$ và số hạng thứ $3$ bằng $12$. Tìm số hạng thứ $50$ của cấp số nhân này.

**2.18.** Một cấp số nhân có số hạng đầu bằng $5$ và công bội bằng $2$. Hỏi phải lấy tổng của bao nhiêu số hạng đầu của cấp số nhân này để có tổng bằng $5\,115$?

**2.19.** Một công ty xây dựng mua một chiếc máy ủi với giá $3$ tỉ đồng. Cứ sau mỗi năm sử dụng, giá trị của chiếc máy ủi này lại giảm $20\%$ so với giá trị của nó trong năm liền trước đó. Tìm giá trị còn lại của chiếc máy ủi đó sau $5$ năm sử dụng.

**2.20.** Vào năm 2020, dân số của một quốc gia là khoảng $97$ triệu người và tốc độ tăng trưởng dân số là $0,91\%$. Nếu tốc độ tăng trưởng dân số này được giữ nguyên hằng năm, hãy ước tính dân số của quốc gia đó vào năm 2030.

**2.21.** Một loại thuốc được dùng mỗi ngày một lần. Lúc đầu nồng độ thuốc trong máu của bệnh nhân tăng nhanh, nhưng mỗi liều kế tiếp có tác dụng ít hơn liều trước đó. Lượng thuốc trong máu ở ngày thứ nhất là $50\text{ mg}$, và mỗi ngày sau đó giảm chỉ còn một nửa so với ngày kề trước đó. Tính tổng lượng thuốc (tính bằng mg) trong máu của bệnh nhân sau khi dùng thuốc $10$ ngày liên tiếp.
