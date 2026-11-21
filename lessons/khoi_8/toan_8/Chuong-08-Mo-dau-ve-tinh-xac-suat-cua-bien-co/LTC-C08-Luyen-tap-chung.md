---
unit: toan_8
lesson_id: ltc-c08
toc_path:
  - "Chương VIII. Mở đầu về tính xác suất của biến cố"
  - "Luyện tập chung (trang 74)"
source_file: "SGK TOAN 8 TAP 2 - KNTT.pdf"
pdf_pages: [75, 76]
lesson_type: on_tap
status: verified
---

<!-- pdf:75 -->

# LUYỆN TẬP CHUNG (TRANG 74)

**Ví dụ 1:** Một hộp đựng $36$ tấm thẻ giống nhau được đánh số $1; 2; 3; \dots; 36$. Bạn Nam rút ngẫu nhiên một tấm thẻ trong hộp. Tính xác suất của các biến cố sau:

a) $E$: “Rút được tấm thẻ ghi số chia hết cho $4$”;

b) $F$: “Rút được tấm thẻ ghi số là bội của $4$ hoặc $6$”;

c) $G$: “Rút được tấm thẻ ghi số nguyên tố”.

**Giải**

Có $36$ kết quả có thể, đó là $1; 2; 3; \dots; 36$. Do rút ngẫu nhiên nên các kết quả có thể này là đồng khả năng.

a) Có $9$ kết quả thuận lợi cho biến cố $E$ là: $4; 8; 12; 16; 20; 24; 28; 32; 36$.

Vậy $P(E) = \dfrac{9}{36} = \dfrac{1}{4}$.

b) Có $12$ kết quả thuận lợi cho biến cố $F$ là: $4; 6; 8; 12; 16; 18; 20; 24; 28; 30; 32; 36$.

Vậy $P(F) = \dfrac{12}{36} = \dfrac{1}{3}$.

c) Có $11$ kết quả thuận lợi cho biến cố $G$ là: $2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31$.

Vậy $P(G) = \dfrac{11}{36}$.

**Ví dụ 2:** Một cơ quan quản lí đã thống kê được số lượt khách đến tham quan di tích X trong năm qua như sau:

| Tháng | $1; 2$ | $3; 4$ | $5; 6$ | $7; 8$ | $9; 10$ | $11; 12$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Số lượt khách | $137$ | $181$ | $148$ | $117$ | $116$ | $111$ |

a) Tính xác suất thực nghiệm của biến cố $E$: “Khách đến tham quan di tích trong tháng $7$ và tháng $8$”;

b) Tính xác suất thực nghiệm của biến cố $F$: “Khách đến tham quan di tích trong thời gian từ tháng $7$ đến tháng $12$”;

c) Giả sử năm tới có $1\,196$ lượt khách đến tham quan di tích. Hãy dự đoán xem:

- Có bao nhiêu lượt khách đến tham quan di tích trong tháng $7$ và tháng $8$.
- Có bao nhiêu lượt khách đến tham quan di tích trong thời gian từ tháng $7$ đến tháng $12$.

**Giải**

a) Số lượt khách tham quan di tích trong năm qua là

$137 + 181 + 148 + 117 + 116 + 111 = 810.$

Có $117$ lượt khách tham quan vào tháng $7$, tháng $8$.

Vậy xác suất thực nghiệm của biến cố $E$ là $\dfrac{117}{810} \approx 0,144$.

<!-- pdf:76 -->

b) Số lượt khách tham quan di tích từ tháng $7$ đến tháng $12$ trong năm qua là

$117 + 116 + 111 = 344.$

Vậy xác suất thực nghiệm của biến cố $F$ là $\dfrac{344}{810} \approx 0,425$.

c) Ta có $1\,196 \cdot \dfrac{117}{810} \approx 172,76$. Vậy ta dự đoán trong năm tới có khoảng $173$ lượt khách tham quan di tích vào tháng $7$ và tháng $8$.

Ta có $1\,196 \cdot \dfrac{344}{810} \approx 507,93$. Vậy ta dự đoán trong năm tới có khoảng $508$ lượt khách tham quan di tích trong thời gian từ tháng $7$ đến tháng $12$.

## BÀI TẬP

8.14. Gieo một con xúc xắc cân đối. Tính xác suất của các biến cố sau:

a) $A$: “Số chấm xuất hiện trên con xúc xắc khác $6$”;

b) $B$: “Số chấm xuất hiện trên con xúc xắc bé hơn $3$”;

c) $C$: “Số chấm xuất hiện trên con xúc xắc lớn hơn $2$”;

d) $D$: “Số chấm xuất hiện trên con xúc xắc là số nguyên tố”.

8.15. Một túi đựng các quả bóng giống hệt nhau, chỉ khác màu, trong đó có $15$ quả bóng màu xanh, $13$ quả bóng màu đỏ và $17$ quả bóng màu trắng. Lấy ngẫu nhiên một quả bóng từ trong túi. Tính xác suất của các biến cố sau:

a) $C$: “Lấy được quả bóng màu xanh”;

b) $D$: “Lấy được quả bóng màu đỏ”;

c) $E$: “Không lấy được quả bóng màu trắng”.

8.16. Trong trò chơi “Xúc xắc may mắn”, ở mỗi ván chơi, người chơi gieo đồng thời hai con xúc xắc và ghi lại tổng số chấm xuất hiện trên hai con xúc xắc. Một người chơi $80$ ván và ghi lại kết quả trong bảng sau:

| Tổng số chấm | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Số ván | $2$ | $5$ | $6$ | $8$ | $11$ | $14$ | $12$ | $9$ | $6$ | $4$ | $3$ |

a) Giả sử người chơi thắng nếu tổng số chấm xuất hiện trên hai con xúc xắc là $5$ hoặc $7$. Tính xác suất thực nghiệm của biến cố $E$: “Người chơi thắng trong một ván chơi”.

b) Giả sử người chơi thắng nếu tổng số chấm xuất hiện trên hai con xúc xắc nhỏ nhất là $10$. Tính xác suất thực nghiệm của biến cố $F$: “Người chơi thắng trong một ván chơi”.

8.17. Thống kê số vụ tai nạn giao thông trong hai tháng $8$ và $9$ của thành phố X được kết quả như bảng sau:

| Số vụ tai nạn giao thông xảy ra trong một ngày | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $\ge 8$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Số ngày | $4$ | $9$ | $15$ | $10$ | $8$ | $6$ | $4$ | $3$ | $2$ |

Từ bảng thống kê trên, hãy dự đoán xem trong ba tháng $10; 11; 12$ tới tại thành phố X:

a) Có bao nhiêu ngày có nhiều nhất $3$ vụ tai nạn giao thông.

b) Có bao nhiêu ngày có ít nhất $5$ vụ tai nạn giao thông.
