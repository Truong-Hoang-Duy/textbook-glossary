---
unit: toan_9
lesson_id: b03
toc_path:
  - "Chương I. Phương trình và hệ hai phương trình bậc nhất hai ẩn"
  - "Bài 3. Giải bài toán bằng cách lập hệ phương trình"
source_file: "SGK TOAN 9 TAP 1 - KNTT.pdf"
pdf_pages: [23, 25]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:23 -->

# BÀI 3: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH

## 🎯 Kiến thức, kĩ năng

Giải một số bài toán bằng cách lập hệ phương trình bậc nhất hai ẩn.

## 🔴 Mở đầu

***Bài toán.*** Một vật có khối lượng $124\text{ g}$ và thể tích $15\text{ cm}^3$ là hợp kim của đồng và kẽm. Tính xem trong đó có bao nhiêu gam đồng và bao nhiêu gam kẽm, biết rằng $1\text{ cm}^3$ đồng nặng $8,9\text{ g}$ và $1\text{ cm}^3$ kẽm nặng $7\text{ g}$.

**Giải bài toán bằng cách lập hệ phương trình**

Xét bài toán ở *Tình huống mở đầu*. Gọi $x$ là số gam đồng, $y$ là số gam kẽm cần tính.

**HĐ1:** Biểu thị khối lượng của vật qua $x$ và $y$.

**HĐ2:** Biểu thị thể tích của vật qua $x$ và $y$.

**HĐ3:** Giải hệ gồm hai phương trình bậc nhất hai ẩn $x, y$ nhận được ở HĐ1 và HĐ2. Từ đó trả lời câu hỏi ở *Tình huống mở đầu*.

<!-- term: Các bước giải bài toán bằng cách lập hệ phương trình -->
> **Nhận xét.** các bước giải một bài toán bằng cách lập hệ phương trình:
>
> *Bước 1.* Lập hệ phương trình:
> - Chọn ẩn số (thường chọn hai ẩn số) và đặt điều kiện thích hợp cho các ẩn số;
> - Biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết;
> - Lập hệ phương trình biểu thị mối quan hệ giữa các đại lượng.
>
> *Bước 2.* Giải hệ phương trình.
>
> *Bước 3.* Trả lời: Kiểm tra xem trong các nghiệm tìm được của hệ phương trình, nghiệm nào thoả mãn, nghiệm nào không thoả mãn điều kiện của ẩn, rồi kết luận.

**Ví dụ 1**

Tìm hai số tự nhiên có tổng bằng $1\,006$, biết rằng nếu lấy số lớn chia cho số nhỏ thì được thương là $2$ và số dư là $124$.

**Giải**

- Gọi hai số cần tìm là $x$ và $y$, trong đó $x < y$. Số dư trong phép chia $y$ cho $x$ là $124$ nên $x > 124$. Vậy điều kiện của hai ẩn là $x, y \in \mathbb{N}$ và $124 < x < y$.

Tổng hai số bằng $1\,006$ nên ta có phương trình $x + y = 1\,006$.

Khi chia $y$ cho $x$ ta được thương là $2$, dư $124$ nên ta có phương trình $y = 2x + 124$.

Do đó, ta có hệ phương trình $\begin{cases} x + y = 1\,006 \quad (1) \\ y = 2x + 124. \quad (2) \end{cases}$

<!-- pdf:24 -->

- Giải hệ phương trình:

Từ $(2)$ thế $y = 2x + 124$ vào $(1)$, ta được $3x + 124 = 1\,006$ hay $3x = 882$, suy ra $x = 294$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 24, câu chứa nhiều biểu thức toán học trong LaTeX -->

Từ đó ta được $y = 2 \cdot 294 + 124 = 712$.

- Các giá trị $x = 294$ và $y = 712$ thoả mãn các điều kiện của ẩn.

Vậy hai số cần tìm là $294$ và $712$.

**Luyện tập 1**

Một chiếc xe khách đi từ Thành phố Hồ Chí Minh đến Cần Thơ, quãng đường dài $170\text{ km}$. Sau khi xe khách xuất phát $1$ giờ $40$ phút, một chiếc xe tải bắt đầu đi từ Cần Thơ về Thành phố Hồ Chí Minh và gặp xe khách sau đó $40$ phút. Tính vận tốc của mỗi xe, biết rằng mỗi giờ xe khách đi nhanh hơn xe tải $15\text{ km}$.

*Hướng dẫn.* Gọi $x\text{ (km/h)}$ là vận tốc của xe tải và $y\text{ (km/h)}$ là vận tốc xe khách ($x, y > 0$). Chú ý rằng hai xe (đi ngược chiều) gặp nhau khi tổng quãng đường hai xe đã đi bằng $170\text{ km}$.

**Ví dụ 2**

Hai đội công nhân cùng làm một đoạn đường trong $24$ ngày thì xong. Mỗi ngày, đội I làm được nhiều gấp rưỡi đội II. Hỏi nếu làm một mình thì mỗi đội làm xong đoạn đường đó trong bao lâu? (Giả sử năng suất của mỗi đội là không đổi).

**Giải**

- Gọi $x$ là số ngày để đội I hoàn thành công việc nếu làm riêng một mình; $y$ là số ngày để đội II hoàn thành công việc nếu làm riêng một mình. Điều kiện: $x > 0$ và $y > 0$.

Mỗi ngày đội I làm được $\dfrac{1}{x}$ (công việc) và đội II làm được $\dfrac{1}{y}$ (công việc).

Mỗi ngày đội I làm được nhiều gấp rưỡi đội II nên ta có phương trình $\dfrac{1}{x} = 1,5 \cdot \dfrac{1}{y}$ hay $\dfrac{1}{x} = \dfrac{3}{2} \cdot \dfrac{1}{y}$. $\quad (1)$

Hai đội làm chung trong $24$ ngày thì xong công việc nên mỗi ngày, hai đội làm chung thì được $\dfrac{1}{24}$ (công việc). Ta có phương trình

$\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{24}. \quad (2)$

Từ $(1)$ và $(2)$, ta có hệ phương trình $(\text{I}) \quad \begin{cases} \dfrac{1}{x} = \dfrac{3}{2} \cdot \dfrac{1}{y} \\ \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{24}. \end{cases}$

- Nếu đặt $u = \dfrac{1}{x}$ và $v = \dfrac{1}{y}$ thì ta có hệ phương trình bậc nhất hai ẩn mới là $u$ và $v$:

$(\text{II}) \quad \begin{cases} u = \dfrac{3}{2}v \quad (3) \\ u + v = \dfrac{1}{24}. \quad (4) \end{cases}$

<!-- pdf:25 -->

Giải hệ $(\text{II})$: Thế $u = \dfrac{3}{2}v$ vào phương trình $(4)$, ta được $\dfrac{3}{2}v + v = \dfrac{1}{24}$, hay $\dfrac{5}{2}v = \dfrac{1}{24}$, suy ra $v = \dfrac{1}{60}$. Do đó $u = \dfrac{3}{2}v = \dfrac{3}{2} \cdot \dfrac{1}{60} = \dfrac{1}{40}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 25, OCR đọc sai từ "Thế" thành "Thố" và phân số -->

Từ đó, ta có:

$u = \dfrac{1}{x} = \dfrac{1}{40}$ suy ra $x = 40$; $\quad v = \dfrac{1}{y} = \dfrac{1}{60}$ suy ra $y = 60$.

- Các giá trị tìm được của $x$ và $y$ thoả mãn điều kiện của ẩn.

*Trả lời:* Nếu làm một mình thì đội I làm xong đoạn đường đó trong $40$ ngày, còn đội II làm xong trong $60$ ngày.

**Luyện tập 2**

Nếu hai vòi nước cùng chảy vào một bể không có nước thì bể sẽ đầy trong $1$ giờ $20$ phút. Nếu mở riêng vòi thứ nhất trong $10$ phút và vòi thứ hai trong $12$ phút thì chỉ được $\dfrac{2}{15}$ bể nước. Hỏi nếu mở riêng từng vòi thì thời gian để mỗi vòi chảy đầy bể nước là bao nhiêu phút?

## BÀI TẬP

1.15. Tìm số tự nhiên $N$ có hai chữ số, biết rằng tổng của hai chữ số đó bằng $12$, và nếu viết hai chữ số đó theo thứ tự ngược lại thì được một số lớn hơn $N$ là $36$ đơn vị.

1.16. Điểm số trung bình của một vận động viên bắn súng sau $100$ lần bắn là $8,69$ điểm. Kết quả cụ thể được ghi trong bảng sau, trong đó có hai ô bị mờ không đọc được (đánh dấu "$?$"):

| Điểm số của mỗi lần bắn | $10$ | $9$ | $8$ | $7$ | $6$ |
| --- | :---: | :---: | :---: | :---: | :---: |
| Số lần bắn | $25$ | $42$ | $?$ | $15$ | $?$ |

Em hãy tìm lại các số bị mờ trong hai ô đó.

1.17. Năm ngoái, hai đơn vị sản xuất nông nghiệp thu hoạch được $3\,600$ tấn thóc. Năm nay, hai đơn vị thu hoạch được $4\,095$ tấn thóc. Hỏi năm nay, mỗi đơn vị thu hoạch được bao nhiêu tấn thóc, biết rằng năm nay, đơn vị thứ nhất làm vượt mức $15\%$, đơn vị thứ hai làm vượt mức $12\%$ so với năm ngoái?

Hãy dùng máy tính cầm tay để kiểm tra lại kết quả thu được.

1.18. Hai người thợ cùng làm một công việc trong $16$ giờ thì xong. Nếu người thứ nhất làm trong $3$ giờ và người thứ hai làm trong $6$ giờ thì chỉ hoàn thành được $25\%$ công việc. Hỏi nếu làm riêng thì mỗi người hoàn thành công việc trong bao lâu?
