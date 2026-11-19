---
unit: toan_11
lesson_id: b08
toc_path:
  - "Chương III. Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm"
  - "Bài 8. Mẫu số liệu ghép nhóm"
source_file: "SGK TOAN 11 - KNTT - TAP 1.pdf"
pdf_pages: [59, 62]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:59 -->

<!-- Phần giới thiệu Chương III (in chung đầu trang PDF 59): CHƯƠNG III. CÁC SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM CỦA MẪU SỐ LIỆU GHÉP NHÓM -->

Ở lớp 10 ta đã được làm quen với các số đặc trưng của mẫu số liệu không ghép nhóm. Trong nhiều trường hợp, ta chỉ có số liệu dưới dạng ghép nhóm. Chương này giới thiệu về mẫu số liệu ghép nhóm và cách tính các số đặc trưng đo xu thế trung tâm cho mẫu số liệu này.

# BÀI 8: MẪU SỐ LIỆU GHÉP NHÓM

## 🔤 Thuật ngữ

- Mẫu số liệu ghép nhóm

## 🎯 Kiến thức, kĩ năng

- Đọc và giải thích mẫu số liệu ghép nhóm.
- Ghép nhóm mẫu số liệu.

## 🔴 Mở đầu

Trong kì thi tốt nghiệp Trung học phổ thông năm 2021 đợt 1 có $344\,752$ thí sinh dự thi cả ba môn Toán, Vật lí, Hoá học (theo: *vietnamnet.vn, ngày 26/07/2021*). Giả sử điểm thi của các thí sinh này được cho trong bảng số liệu sau:

| STT | Điểm Toán | Điểm Vật lí | Điểm Hoá học | Tổng điểm |
| --- | :---: | :---: | :---: | :---: |
| $1$ | $8,00$ | $7,25$ | $7,75$ | $23,00$ |
| $2$ | $6,00$ | $7,75$ | $6,50$ | $20,25$ |
| $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| $344\,752$ | $4,50$ | $5,75$ | $6,25$ | $16,50$ |

Các trường đại học, cao đẳng tuyển sinh theo tổ hợp A00 quan tâm đến tổng điểm ba môn của các thí sinh này. Biểu diễn dãy số liệu về tổng điểm ba môn của các thí sinh này thế nào để các trường thấy được bức tranh tổng thể về kết quả thi?

<!-- pdf:60 -->

## 1. GIỚI THIỆU VỀ MẪU SỐ LIỆU GHÉP NHÓM

**HĐ1:** Xét dữ liệu cho trong *tình huống mở đầu*.

a) Mẫu số liệu về tổng điểm, kí hiệu là $(T)$, có bao nhiêu giá trị?

b) Nếu lập bảng tần số cho mẫu số liệu $(T)$ thì có dễ hình dung được bức tranh tổng thể về kết quả thi không? Vì sao?

c) Mẫu số liệu $(T)$ được mô tả dưới dạng bảng thống kê sau:

| Tổng điểm | $< 6$ | $[6; 7)$ | $[7; 8)$ | $\dots$ | $[28; 29)$ | $[29; 30]$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Số thí sinh | $23$ | $69$ | $192$ | $\dots$ | $216$ | $12$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 60, OCR đọc lỗi kí hiệu khoảng và dấu chấm lửng trong bảng -->

Hãy đọc và giải thích số liệu được biểu diễn trong bảng thống kê.

> **Mẫu số liệu ghép nhóm** là mẫu số liệu cho dưới dạng bảng tần số của các **nhóm số liệu**. Mỗi nhóm số liệu là tập hợp gồm các giá trị của số liệu được ghép nhóm theo một tiêu chí xác định. Nhóm số liệu thường được cho dưới dạng $[a; b)$, trong đó $a$ là **đầu mút trái**, $b$ là **đầu mút phải**.

**Nhận xét:**

- Mẫu số liệu ghép nhóm được dùng khi ta không thể thu thập được số liệu chính xác hoặc do yêu cầu của bài toán mà ta phải biểu diễn mẫu số liệu dưới dạng ghép nhóm để thuận lợi cho việc tổ chức, đọc và phân tích số liệu.
- Trong một số trường hợp, nhóm số liệu cuối cùng có thể lấy đầu mút bên phải.

**Ví dụ 1:** Mẫu số liệu sau cho biết phân bố theo độ tuổi của dân số Việt Nam năm 2019.

| Độ tuổi | Dưới $15$ | Từ $15$ đến dưới $65$ tuổi | Từ $65$ tuổi trở lên |
| --- | :---: | :---: | :---: |
| Số người | $23\,371\,882$ | $65\,420\,451$ | $7\,416\,651$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 60, OCR đọc dính chữ trong bảng Ví dụ 1 -->

*(Theo: Báo cáo số liệu tổng điều tra dân số năm 2019)*

a) Mẫu số liệu đã cho có là mẫu số liệu ghép nhóm hay không?

b) Nêu các nhóm và tần số tương ứng. Dân số Việt Nam năm 2019 là bao nhiêu?

**Giải:**

a) Mẫu số liệu đã cho là mẫu số liệu ghép nhóm.

b) Có ba nhóm là: Dưới $15$ tuổi, Từ $15$ đến dưới $65$ tuổi, Từ $65$ tuổi trở lên. Có $23\,371\,882$ người dưới $15$ tuổi; $65\,420\,451$ người từ $15$ đến dưới $65$ tuổi và $7\,416\,651$ người từ $65$ tuổi trở lên.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 60, các số có dấu cách phân tách hàng nghìn nằm trong LaTeX -->

Dân số Việt Nam năm 2019 là $23\,371\,882 + 65\,420\,451 + 7\,416\,651 = 96\,208\,984$ người.

**Luyện tập 1:** Cho mẫu số liệu ghép nhóm về thời gian (phút) đi từ nhà đến nơi làm việc của các nhân viên một công ty như sau:

| Thời gian | $[15; 20)$ | $[20; 25)$ | $[25; 30)$ | $[30; 35)$ | $[35; 40)$ | $[40; 45)$ | $[45; 50)$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Số nhân viên | $6$ | $14$ | $25$ | $37$ | $21$ | $13$ | $9$ |

Đọc và giải thích mẫu số liệu này.

<!-- pdf:61 -->

## 2. GHÉP NHÓM MẪU SỐ LIỆU

**HĐ2:** Chỉ số BMI (đo bằng $w/h^2$, trong đó $w$ là cân nặng đơn vị là kilôgam, $h$ là chiều cao đơn vị là mét) của các học sinh trong một tổ được cho như sau:

$19,2 \quad 21,1 \quad 16,8 \quad 23,5 \quad 20,6 \quad 25,2 \quad 18,7 \quad 19,1.$

Một người có chỉ số BMI nhỏ hơn $18,5$ được xem là thiếu cân; từ $18,5$ đến dưới $23$ là có cân nặng lí tưởng so với chiều cao; từ $23$ trở lên là thừa cân. Hãy lập mẫu số liệu ghép nhóm cho mẫu số liệu trên để biểu diễn tình trạng cân nặng so với chiều cao của các học sinh trong tổ.

<!-- term: Cách ghép nhóm mẫu số liệu -->
> Để chuyển mẫu số liệu không ghép nhóm sang mẫu số liệu ghép nhóm, ta làm như sau:
>
> *Bước 1.* Chia miền giá trị của mẫu số liệu thành một số nhóm theo tiêu chí cho trước.
>
> *Bước 2.* Đếm số giá trị của mẫu số liệu thuộc mỗi nhóm (tần số) và lập bảng thống kê cho mẫu số liệu ghép nhóm.

- **Độ dài của nhóm** $[a; b)$ là $b - a$.
- Không nên chia thành quá nhiều nhóm hoặc quá ít nhóm. Các nhóm không giao nhau, các nhóm nên có độ dài như nhau và tổng độ dài các nhóm lớn hơn khoảng biến thiên.

**Ví dụ 2:** Bảng thống kê sau cho biết thời gian chạy (phút) của $30$ vận động viên (VĐV) trong một giải chạy Marathon.

| Thời gian | $129$ | $130$ | $133$ | $134$ | $135$ | $136$ | $138$ | $141$ | $142$ | $143$ | $144$ | $145$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Số VĐV | $1$ | $2$ | $1$ | $1$ | $1$ | $2$ | $3$ | $3$ | $4$ | $5$ | $2$ | $5$ |

Hãy chuyển mẫu số liệu trên sang mẫu số liệu ghép nhóm gồm sáu nhóm có độ dài bằng nhau và bằng $3$.

**Giải:**

Giá trị nhỏ nhất là $129$, giá trị lớn nhất là $145$ nên khoảng biến thiên là $145 - 129 = 16$. Tổng độ dài của sáu nhóm là $18$. Để cho đối xứng, ta chọn đầu mút trái của nhóm đầu tiên là $27,5$ và đầu mút phải của nhóm cuối cùng là $145,5$ ta được các nhóm là $[127,5; 130,5)$, $[130,5; 133,5), \dots, [142,5; 145,5)$. Đếm số giá trị thuộc mỗi nhóm, ta có mẫu số liệu ghép nhóm như sau:
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 61, OCR đọc sai dấu mũ và chữ thuộc trong lời giải Ví dụ 2 -->

| Thời gian | $[127,5; 130,5)$ | $[130,5; 133,5)$ | $[133,5; 136,5)$ | $[136,5; 139,5)$ | $[139,5; 142,5)$ | $[142,5; 145,5)$ |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Số VĐV | $3$ | $1$ | $4$ | $3$ | $7$ | $12$ |

**Luyện tập 2:** Cân nặng ($\text{kg}$) của $35$ người trưởng thành tại một khu dân cư được cho như sau:

$43 \quad 51 \quad 47 \quad 62 \quad 48 \quad 40 \quad 50 \quad 62 \quad 53 \quad 56 \quad 40 \quad 48 \quad 56 \quad 53 \quad 50 \quad 42 \quad 55$

$52 \quad 48 \quad 46 \quad 45 \quad 54 \quad 52 \quad 50 \quad 47 \quad 44 \quad 54 \quad 55 \quad 60 \quad 63 \quad 58 \quad 55 \quad 60 \quad 58 \quad 53.$

Chuyển mẫu số liệu trên thành dạng ghép nhóm, các nhóm có độ dài bằng nhau, trong đó có nhóm $[40; 45)$.

<!-- pdf:62 -->

**Vận dụng:** Một công ty may quần áo đồng phục học sinh cho biết cỡ áo theo chiều cao của học sinh được tính như sau:

| Chiều cao ($\text{cm}$) | $[150; 160)$ | $[160; 167)$ | $[167; 170)$ | $[170; 175)$ | $[175; 180)$ |
| --- | :---: | :---: | :---: | :---: | :---: |
| Cỡ áo | S | M | L | XL | XXL |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 62, OCR đọc sai kí hiệu XL trong bảng Vận dụng -->

Công ty muốn ước lượng tỉ lệ các cỡ áo khi may cho học sinh lớp 11 đã đo chiều cao của $36$ học sinh nam khối 11 của một trường và thu được mẫu số liệu sau (đơn vị là centimét):

$160 \quad 161 \quad 161 \quad 162 \quad 162 \quad 162 \quad 163 \quad 163 \quad 163 \quad 164 \quad 164 \quad 164 \quad 164$

$165 \quad 165 \quad 165 \quad 165 \quad 165 \quad 166 \quad 166 \quad 166 \quad 166 \quad 167 \quad 167 \quad 168 \quad 168$

$168 \quad 168 \quad 169 \quad 169 \quad 170 \quad 171 \quad 171 \quad 172 \quad 172 \quad 174.$

a) Lập bảng tần số ghép nhóm của mẫu số liệu với các nhóm đã cho ở bảng trên.

b) Công ty may $500$ áo đồng phục cho học sinh lớp 11 thì nên may số lượng áo theo mỗi cỡ là bao nhiêu chiếc?

## ✏️ BÀI TẬP

**3.1.** Trong các mẫu số liệu sau, mẫu nào là mẫu số liệu ghép nhóm? Đọc và giải thích mẫu số liệu ghép nhóm đó.

a) Số tiền mà sinh viên chi cho thanh toán cước điện thoại trong tháng.

| Số tiền (nghìn đồng) | $[0; 50)$ | $[50; 100)$ | $[100; 150)$ | $[150; 200)$ | $[200; 250)$ |
| --- | :---: | :---: | :---: | :---: | :---: |
| Số sinh viên | $5$ | $12$ | $23$ | $17$ | $3$ |

b) Thống kê nhiệt độ tại một địa điểm trong $40$ ngày, ta có bảng số liệu sau:

| Nhiệt độ ($^\circ\text{C}$) | $[19; 22)$ | $[22; 25)$ | $[25; 28)$ | $[28; 31)$ |
| --- | :---: | :---: | :---: | :---: |
| Số ngày | $7$ | $15$ | $12$ | $6$ |

**3.2.** Số sản phẩm một công nhân làm được trong một ngày được cho như sau:

$18 \quad 25 \quad 39 \quad 12 \quad 54 \quad 27 \quad 46 \quad 25 \quad 19 \quad 8 \quad 36 \quad 22$

$20 \quad 19 \quad 17 \quad 44 \quad 5 \quad 18 \quad 23 \quad 28 \quad 25 \quad 34 \quad 46 \quad 27 \quad 16.$

Hãy chuyển mẫu số liệu sang dạng ghép nhóm với sáu nhóm có độ dài bằng nhau.

**3.3.** Thời gian ra sân (giờ) của một số cựu cầu thủ ở giải ngoại hạng Anh qua các thời kì được cho như sau:

$653 \quad 632 \quad 609 \quad 572 \quad 565 \quad 535 \quad 516 \quad 514 \quad 508 \quad 505 \quad 504 \quad 504 \quad 503 \quad 499 \quad 496 \quad 492.$

*(Theo: https://www.premierleague.com/)*

Hãy chuyển mẫu số liệu trên sang dạng ghép nhóm với bảy nhóm có độ dài bằng nhau.
