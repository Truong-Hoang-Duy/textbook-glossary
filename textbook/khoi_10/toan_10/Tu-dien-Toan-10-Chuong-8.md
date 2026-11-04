---
name: tu-dien-toan-10-chuong-8
description: Từ điển thuật ngữ Toán 10 Chương VIII — Đại số tổ hợp (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 10
chuong: "Chương VIII. Đại số tổ hợp"
bai_so: "Bài 23 – Bài 25"
nguon: "SGK Toán 10 Tập 2 – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: "2026-11-04"
ngay_cap_nhat: "2026-11-04"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 10 — CHƯƠNG VIII: ĐẠI SỐ TỔ HỢP

## Quy ước sử dụng

- **Phạm vi:** Chương VIII (Bài 23 đến Bài 25 và Bài tập cuối chương VIII), Tập 2, SGK Toán 10 (bộ Kết nối tri thức với cuộc sống), tích hợp các mục tương ứng trong Bảng tra cứu thuật ngữ và Bảng giải thích thuật ngữ cuối Tập 2 (trang in 98–99, PDF 99–100).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Kí hiệu / Công thức` | `Định nghĩa / Giải nghĩa` | `Bối cảnh trong bài`.
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm, chú ý định nghĩa hoặc bảng giải thích thuật ngữ cuối sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp từ đoạn văn/định lí/quy tắc gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.
  - *Ngoài nguồn:* các khái niệm nền tảng từ lớp dưới hoặc chuyên đề học tập có liên quan nhưng không định nghĩa lại trong Chương VIII.

## Bài 23: Quy tắc đếm

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Quy tắc cộng | $n_1 + n_2$ (cách) | Giả sử một công việc có thể thực hiện theo một trong hai phương án khác nhau: Phương án một có $n_1$ cách thực hiện, Phương án hai có $n_2$ cách thực hiện (không trùng với bất kì cách thực hiện nào của phương án một). Khi đó số cách thực hiện công việc sẽ là: $n_1 + n_2$ cách. | Mục 1, khung kiến thức định nghĩa quy tắc cộng (trang 61, PDF 62). |
| Sơ đồ hình cây | — | Sơ đồ minh hoạ cách phân chia trường hợp như trong Hình 8.2 được gọi là sơ đồ hình cây. Trong các bài toán đếm, người ta thường dùng sơ đồ hình cây để minh hoạ, giúp cho việc đếm thuận tiện và không bỏ sót trường hợp. | Mục 1, chú ý giới thiệu sơ đồ hình cây (trang 61, PDF 62). |
| Quy tắc đếm số phần tử của hợp hai tập hợp hữu hạn | $n(A \cup B) = n(A) + n(B)$ khi $A \cap B = \varnothing$ | Ở câu b), nếu gọi $A$ là tập hợp gồm tất cả các quân cờ trắng, $B$ là tập hợp gồm tất cả các quân tốt thì các quân cờ Nam lấy ra chính là các phần tử của tập hợp $A \cup B$. Nếu ta áp dụng quy tắc cộng: $n(A \cup B) = n(A) + n(B) = 32$ (quân cờ), suy ra Nam lấy ra $32$ quân cờ. Kết luận khi đó là sai, vì $A \cap B \ne \varnothing$ nên ta không thể áp dụng quy tắc cộng để tính trong trường hợp này. | [mô tả] Mục 1, nhận xét về điều kiện rời nhau $A \cap B = \varnothing$ khi áp dụng quy tắc cộng cho hai tập hợp (trang 62, PDF 63). |
| Nguyên tố cùng nhau (hai số nguyên tố cùng nhau) | $\text{ƯCLN}(a, b) = 1$ | Hai số tự nhiên $a$ và $b$ gọi là nguyên tố cùng nhau nếu chúng có ước chung lớn nhất là $1$. | Mục 1, bóng nói nhắc lại khái niệm hai số tự nhiên nguyên tố cùng nhau ở Luyện tập 1 (trang 62, PDF 63). |
| Quy tắc nhân | $m_1 \cdot m_2$ (cách) | Giả sử một công việc phải hoàn thành qua hai công đoạn liên tiếp nhau: Công đoạn một có $m_1$ cách thực hiện, Với mỗi cách thực hiện công đoạn một, có $m_2$ cách thực hiện công đoạn hai. Khi đó số cách thực hiện công việc là: $m_1 \cdot m_2$ cách. | Mục 2, khung kiến thức định nghĩa quy tắc nhân (trang 63, PDF 64). |
| Phân biệt quy tắc cộng và quy tắc nhân | — | Quy tắc cộng được áp dụng khi công việc được chia thành các phương án phân biệt (thực hiện một trong các phương án để hoàn thành công việc). Quy tắc nhân được áp dụng khi công việc có nhiều công đoạn nối tiếp nhau (phải thực hiện tất cả các công đoạn để hoàn thành công việc). | [mô tả] Mục 3, chú ý tổng kết cách kết hợp và phân biệt quy tắc cộng với quy tắc nhân (trang 64, PDF 65). |
| Tập hợp (phần tử của tập hợp; giao và hợp của hai tập hợp) | $A \cap B, A \cup B, n(A)$ | Ngoài nguồn — chưa định nghĩa trong Chương VIII Toán 10. Xem: SGK Toán 10 Tập 1, Chương I | Khái niệm nền tảng dùng để biểu diễn và đếm số phần tử của các tập hợp hữu hạn. |

## Bài 24: Hoán vị, chỉnh hợp và tổ hợp

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Hoán vị (số các hoán vị) | $P_n = n \cdot (n - 1) \cdot (n - 2) \dots 2 \cdot 1 = n!$ | Một hoán vị của một tập hợp có $n$ phần tử là một cách sắp xếp có thứ tự $n$ phần tử đó (với $n$ là một số tự nhiên, $n \ge 1$). Số các hoán vị của tập hợp có $n$ phần tử, kí hiệu là $P_n$, được tính bằng công thức $P_n = n \cdot (n - 1) \cdot (n - 2) \dots 2 \cdot 1$. | Mục 1, khung kiến thức định nghĩa hoán vị và công thức tính số hoán vị (trang 67, PDF 68). |
| Giai thừa ($n$ giai thừa) | $n! = n \cdot (n - 1) \cdot (n - 2) \dots 2 \cdot 1$; $0! = 1$ | Kí hiệu $n \cdot (n - 1) \cdot (n - 2) \dots 2 \cdot 1$ là $n!$ (đọc là $n$ giai thừa), ta có: $P_n = n!$. Chẳng hạn $P_3 = 3! = 3 \cdot 2 \cdot 1 = 6$. Quy ước $0! = 1$. | Mục 1, chú ý về kí hiệu giai thừa và quy ước $0! = 1$ (trang 67, PDF 68). |
| Chỉnh hợp (chỉnh hợp chập $k$ của $n$; chỉnh hợp chập $2$ của $4$) | $A_n^k = n \cdot (n - 1) \dots (n - k + 1) = \frac{n!}{(n - k)!}$ ($1 \le k \le n$) | Một chỉnh hợp chập $k$ của $n$ là một cách sắp xếp có thứ tự $k$ phần tử từ một tập hợp $n$ phần tử (với $k, n$ là các số tự nhiên, $1 \le k \le n$). Số các chỉnh hợp chập $k$ của $n$, kí hiệu là $A_n^k$, được tính bằng công thức $A_n^k = n \cdot (n - 1) \dots (n - k + 1)$ hay $A_n^k = \frac{n!}{(n - k)!}$ ($1 \le k \le n$). | Mục 2, khung kiến thức định nghĩa chỉnh hợp chập $k$ của $n$ và công thức tính (trang 67, PDF 68). |
| Quan hệ giữa hoán vị và chỉnh hợp | $P_n = A_n^n$ | Hoán vị sắp xếp tất cả các phần tử của tập hợp, còn chỉnh hợp chọn ra một số phần tử và sắp xếp chúng. Mỗi hoán vị của $n$ phần tử cũng chính là một chỉnh hợp chập $n$ của $n$ phần tử đó. Vì vậy $P_n = A_n^n$. | [mô tả] Mục 2, chú ý so sánh hoán vị và chỉnh hợp (trang 68, PDF 69). |
| Tổ hợp (tổ hợp chập $k$ của $n$; tổ hợp chập $2$ của $4$) | $C_n^k = \frac{n!}{(n - k)!k!}$ ($0 \le k \le n$) | Một tổ hợp chập $k$ của $n$ là một cách chọn $k$ phần tử từ một tập hợp $n$ phần tử (với $k, n$ là các số tự nhiên, $0 \le k \le n$). Số các tổ hợp chập $k$ của $n$, kí hiệu là $C_n^k$, được tính bằng công thức $C_n^k = \frac{n!}{(n - k)!k!}$ ($0 \le k \le n$). | Mục 3, khung kiến thức định nghĩa tổ hợp chập $k$ của $n$ và công thức tính (trang 68, PDF 69). |
| Quan hệ giữa chỉnh hợp và tổ hợp | $C_n^k = \frac{A_n^k}{k!}$ | $C_n^k = \frac{A_n^k}{k!}$. Chỉnh hợp và tổ hợp có điểm giống nhau là đều chọn một số phần tử trong một tập hợp, nhưng khác nhau ở chỗ, chỉnh hợp là chọn có xếp thứ tự, còn tổ hợp là chọn không xếp thứ tự. | [mô tả] Mục 3, chú ý liên hệ công thức và phân biệt chỉnh hợp với tổ hợp (trang 68, PDF 69). |
| Dãy số Fibonacci | $F_0 = 0, F_1 = 1, F_{n+1} = F_n + F_{n-1} = \sum_{k+m=n} C_m^k$ | Trong cuốn sách *Liber Abaci* (*Sách tính*), Leonardo Fibonacci đã giới thiệu dãy số Fibonacci: $F_0 = 0, F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, \dots$ Trong dãy số này, kể từ số hạng thứ ba trở đi, mỗi số hạng bằng tổng của hai số hạng đứng ngay trước nó, tức là $F_{n+1} = F_n + F_{n-1}$, và liên hệ với số tổ hợp qua hằng đẳng thức $F_{n+1} = \sum_{k+m=n} C_m^k$. | [mô tả] Mục Em có biết?, giới thiệu lịch sử bài toán tổ hợp và dãy số Fibonacci (trang 71, PDF 72). |

## Bài 25: Nhị thức Newton

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Khai triển | $(a + b)^2 = a^2 + 2ab + b^2$; $(a + b) \cdot (c + d) = a \cdot c + a \cdot d + b \cdot c + b \cdot d$ | Ở lớp 8, khi học về hằng đẳng thức, ta đã biết khai triển: $(a + b)^2 = a^2 + 2ab + b^2$; $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$. Các tích nhận được từ sơ đồ hình cây của một tích các đa thức giống như cách lấy ra một đơn thức từ mỗi đa thức rồi nhân lại với nhau; tổng của chúng cho ta khai triển của tích các đa thức đã cho. | Mở đầu và Nhận xét, khái niệm khai triển tích các đa thức và luỹ thừa nhị thức (trang 72–73, PDF 73–74). |
| Nhị thức | $a + b, c + d$ | Trong sơ đồ hình cây của tích hai nhị thức $(a + b) \cdot (c + d)$ thì các tích nhận được là $a \cdot c, a \cdot d, b \cdot c, b \cdot d$ cũng chính là các tích nhận được khi ta lấy một hạng tử của nhị thức thứ nhất (là $a$ hoặc $b$) nhân với một hạng tử của nhị thức thứ hai (là $c$ hoặc $d$). | HĐ1 và Nhận xét, tích của hai nhị thức thông qua sơ đồ hình cây (trang 72–73, PDF 73–74). |
| Công thức khai triển $(a + b)^4$ | $(a + b)^4 = C_4^0 a^4 + C_4^1 a^3b + C_4^2 a^2b^2 + C_4^3 ab^3 + C_4^4 b^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$ | $(a + b)^4 = C_4^0 a^4 + C_4^1 a^3b + C_4^2 a^2b^2 + C_4^3 ab^3 + C_4^4 b^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$. Trong khai triển nhị thức Newton $(a + b)^4$, các đơn thức có bậc là $4$. | [mô tả] Khung kiến thức sau HĐ3, công thức khai triển nhị thức Newton với $n = 4$ (trang 73, PDF 74). |
| Công thức khai triển $(a + b)^5$ | $(a + b)^5 = C_5^0 a^5 + C_5^1 a^4b + C_5^2 a^3b^2 + C_5^3 a^2b^3 + C_5^4 ab^4 + C_5^5 b^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$ | $(a + b)^5 = C_5^0 a^5 + C_5^1 a^4b + C_5^2 a^3b^2 + C_5^3 a^2b^3 + C_5^4 ab^4 + C_5^5 b^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$. Trong khai triển nhị thức Newton $(a + b)^5$, các đơn thức có bậc là $5$. | [mô tả] Khung kiến thức sau HĐ4, công thức khai triển nhị thức Newton với $n = 5$ (trang 74, PDF 75). |
| Nhị thức Newton (công thức nhị thức Newton) | $(a + b)^4 = \sum_{k=0}^4 C_4^k a^{4-k}b^k$; $(a + b)^5 = \sum_{k=0}^5 C_5^k a^{5-k}b^k$ | Các công thức khai triển $(a + b)^n$, với $n \in \{4; 5\}$, gồm $(a + b)^4 = C_4^0 a^4 + C_4^1 a^3b + C_4^2 a^2b^2 + C_4^3 ab^3 + C_4^4 b^4$ (các đơn thức có bậc là $4$) và $(a + b)^5 = C_5^0 a^5 + C_5^1 a^4b + C_5^2 a^3b^2 + C_5^3 a^2b^3 + C_5^4 ab^4 + C_5^5 b^5$ (các đơn thức có bậc là $5$), là một công cụ hiệu quả để tính chính xác hoặc xấp xỉ một số đại lượng mà không cần dùng máy tính. | [mô tả] Khung kiến thức và Nhận xét về khai triển nhị thức Newton (trang 73–74, PDF 74–75) và Bảng tra cứu thuật ngữ (trang 98, PDF 99). |
| Nguyên lí Hardy – Weinberg | $(pA + qB)^n$; $C_{i+j}^j p^i q^j$ | Trong di truyền học quần thể, nguyên lí Hardy – Weinberg đưa ra công thức toán học tính tần số của các kiểu gene trong một quần thể ở các thế hệ. Trong trường hợp ở mỗi vị trí trên nhiễm sắc thể chỉ có hai alen $A$ và $B$ với các tần số khởi đầu lần lượt là $p$ và $q$ ($p + q = 1$), công thức của Hardy – Weinberg là tương ứng với khai triển nhị thức Newton; tổng quát, tần số kiểu gene gồm $i$ alen $A$ và $j$ alen $B$ là $C_{i+j}^j p^i q^j$. | [mô tả] Mục Em có biết?, ứng dụng khai triển nhị thức Newton trong di truyền học quần thể (trang 75, PDF 76). |
| Tam giác Pascal | — | Ngoài nguồn — chưa định nghĩa trong Chương VIII Toán 10. Xem: Chuyên đề học tập Toán 10, Chuyên đề 2 | Bảng hệ số nhị thức liên hệ trực tiếp với các hệ số $C_n^k$ trong khai triển nhị thức Newton. |
| Đa thức (đơn thức; hạng tử; đơn thức đồng dạng) | — | Ngoài nguồn — chưa định nghĩa trong Chương VIII Toán 10. Xem: SGK Toán 8 Tập 1, Chương I | Khái niệm nền tảng dùng khi nhân các đa thức và thu gọn các đơn thức đồng dạng trong khai triển nhị thức Newton. |

## Đã xét, không tạo mục

- nhãn (nhãn của mũi tên) — chỉ có trong ví dụ, bài tập: cách gọi tạm cho đơn thức gắn với mỗi mũi tên trong HĐ1 của Bài 25

## Ghi chú nguồn cần kiểm tra

Không có ghi chú nguồn mở.
