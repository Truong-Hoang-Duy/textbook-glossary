---
unit: toan_9
lesson_id: b21
toc_path:
  - "Chương VI. Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn"
  - "Bài 21. Giải bài toán bằng cách lập phương trình"
source_file: "SGK TOAN 9 TAP 2 - KNTT.pdf"
pdf_pages: [27, 29]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:27 -->

# BÀI 21: GIẢI BÀI TOÁN BẰNG CÁCH LẬP PHƯƠNG TRÌNH

## 🔤 Khái niệm, thuật ngữ

- Giải toán bằng cách lập phương trình

## 🎯 Kiến thức, kĩ năng

- Giải quyết một số vấn đề thực tiễn gắn với phương trình bậc hai một ẩn.

## 🔴 Mở đầu

Bác Lan gửi tiết kiệm $100$ triệu đồng vào ngân hàng với kì hạn $12$ tháng theo thể thức lãi kép. Sau năm thứ nhất, do chưa có nhu cầu sử dụng nên bác Lan không rút tiền ra mà tiếp tục gửi $12$ tháng nữa, với lãi suất như cũ. Sau hai năm bác Lan rút tiền ra thì nhận được $118,81$ triệu đồng cả vốn lẫn lãi. Hỏi lãi suất gửi tiết kiệm là bao nhiêu?

**Giải toán bằng cách lập phương trình**

Xét bài toán ở *tình huống mở đầu*.

**HĐ1:** Gọi $x$ là lãi suất gửi tiết kiệm của bác Lan ($x$ được cho dưới dạng số thập phân). Hãy biểu thị số tiền thu được (cả vốn lẫn lãi) của bác Lan sau kì gửi thứ nhất theo $x$.

**HĐ2:** Hết kì gửi thứ nhất, bác Lan không rút tiền ra mà tiếp tục gửi tiết kiệm kì thứ hai với lãi suất như cũ. Hãy biểu thị số tiền thu được (cả vốn lẫn lãi) của bác Lan sau kì gửi thứ hai theo $x$.

**HĐ3:** Dựa vào đề bài, viết phương trình ẩn $x$ thu được và giải phương trình này để tìm $x$. Từ đó, trả lời câu hỏi trong *tình huống mở đầu*.

<!-- term: Các bước giải bài toán bằng cách lập phương trình -->
**Nhận xét.** Các bước giải một bài toán bằng cách lập phương trình:
*Bước 1.* Lập phương trình:
- Chọn ẩn số và đặt điều kiện thích hợp cho ẩn số.
- Biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết.
- Lập phương trình biểu thị mối quan hệ giữa các đại lượng.
*Bước 2.* Giải phương trình.
*Bước 3.* Trả lời: Kiểm tra xem trong các nghiệm của phương trình, nghiệm nào thoả mãn điều kiện của ẩn, nghiệm nào không, rồi kết luận.

**Ví dụ 1:** Một sân bóng đá $7$ người có chiều rộng nhỏ hơn chiều dài $30\text{ m}$ và có diện tích bằng $1\ 800\text{ m}^2$. Tính chiều dài và chiều rộng của sân bóng đó.

**Giải**

Gọi $x$ ($\text{m}$) là chiều rộng của sân bóng. Điều kiện: $x > 0$.

<!-- pdf:28 -->

Khi đó, chiều dài của sân bóng là $x + 30$ ($\text{m}$).

Theo đề bài, ta có phương trình:

$x(x + 30) = 1\ 800$ hay $x^2 + 30x - 1\ 800 = 0.$

Ta có: $\Delta' = 15^2 + 1\ 800 = 2\ 025, \sqrt{\Delta'} = 45$.

Suy ra phương trình có hai nghiệm phân biệt:

$x_1 = \dfrac{-15 - 45}{1} = -60$ (loại); $x_2 = \dfrac{-15 + 45}{1} = 30$ (thoả mãn điều kiện).

Vậy sân bóng có chiều dài $60\text{ m}$ và chiều rộng $30\text{ m}$.
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 28, OCR bỏ sót dòng kết luận của Ví dụ 1 -->

**Ví dụ 2:** Khoảng cách giữa hai bến sông A và B là $36\text{ km}$. Một tàu du lịch đi từ bến A đến bến B, nghỉ $30$ phút ở bến B rồi quay lại bến A. Thời gian kể từ lúc khởi hành đến khi về đến bến A là $5,5$ giờ. Hãy tìm vận tốc thực của tàu du lịch (tức là vận tốc của tàu khi nước yên lặng), biết rằng vận tốc của dòng nước là $3\text{ km/h}$.

**Giải**

Gọi $x$ ($\text{km/h}$) là vận tốc thực của tàu du lịch. Vì vận tốc của dòng nước là $3\text{ km/h}$ nên phải có điều kiện $x > 3$ để tàu có thể chạy ngược dòng.

Vận tốc của tàu khi xuôi dòng là $x + 3$ ($\text{km/h}$), thời gian để tàu đi xuôi dòng là $\dfrac{36}{x + 3}$ (giờ).

Vận tốc của tàu khi ngược dòng là $x - 3$ ($\text{km/h}$), thời gian để tàu đi ngược dòng là $\dfrac{36}{x - 3}$ (giờ).

Thời gian tàu nghỉ tại bến B là $30$ phút $= 0,5$ giờ.

Theo đề bài, ta có phương trình:

$\dfrac{36}{x + 3} + 0,5 + \dfrac{36}{x - 3} = 5,5$ hay $\dfrac{36}{x + 3} + \dfrac{36}{x - 3} = 5.$

Để giải phương trình này, ta quy đồng mẫu vế trái của phương trình:

$\dfrac{36(x - 3) + 36(x + 3)}{(x + 3)(x - 3)} = 5.$

Nhân cả hai vế của phương trình với $(x + 3)(x - 3)$ để khử mẫu, ta được phương trình bậc hai

$36(x - 3) + 36(x + 3) = 5(x + 3)(x - 3)$, hay $5x^2 - 72x - 45 = 0.$

Ta có: $\Delta' = 36^2 - 5 \cdot (-45) = 1\ 521; \sqrt{\Delta'} = \sqrt{1\ 521} = 39$.

Suy ra phương trình có hai nghiệm phân biệt:

$x_1 = \dfrac{36 - 39}{5} = \dfrac{-3}{5}$ (loại); $x_2 = \dfrac{36 + 39}{5} = 15$ (thoả mãn điều kiện).

Vậy vận tốc thực của tàu du lịch là $15\text{ km/h}$.

<!-- pdf:29 -->

**Luyện tập:** Một đội xe gồm các xe tải cùng loại, cần phải chở $120$ tấn hàng. Tuy nhiên khi làm việc, có hai xe phải điều chuyển đi nơi khác nên mỗi xe phải chở thêm $3$ tấn hàng. Hỏi đội xe đó có bao nhiêu chiếc xe tải?

## BÀI TẬP

6.28. Một mảnh đất hình chữ nhật có diện tích $360\text{ m}^2$. Nếu tăng chiều rộng $3\text{ m}$ và giảm chiều dài $4\text{ m}$ thì diện tích mảnh đất không đổi. Tìm các kích thước của mảnh đất đó.

6.29. Sau hai năm, số dân của một thành phố tăng từ $1\ 200\ 000$ người lên $1\ 452\ 000$ người. Hỏi trung bình mỗi năm dân số của thành phố đó tăng bao nhiêu phần trăm?

6.30. Một thanh sô cô la có dạng hình hộp chữ nhật với chiều dài $12\text{ cm}$, chiều rộng $7\text{ cm}$ và độ dày $3\text{ cm}$. Do giá nguyên liệu ca cao tăng nhưng vẫn muốn giữ nguyên giá bán nên nhà sản xuất quyết định giảm $10\%$ thể tích của mỗi thanh sô cô la. Để thực hiện việc này, nhà sản xuất dự định làm thanh sô cô la mới có cùng độ dày $3\text{ cm}$ như thanh cũ, nhưng chiều dài và chiều rộng sẽ giảm đi cùng một số centimét. Hỏi kích thước của thanh sô cô la mới là bao nhiêu?

6.31. Một máy bay khởi hành từ Hà Nội vào Thành phố Hồ Chí Minh, sau đó nghỉ $96$ phút và tiếp tục bay về Hà Nội với vận tốc lớn hơn vận tốc lúc đi là $100\text{ km/h}$. Tổng thời gian của cả hành trình, kể từ khi xuất phát từ Hà Nội đến khi quay về Hà Nội là $6$ giờ. Tính vận tốc của máy bay lúc đi, biết quãng đường bay Hà Nội – Thành phố Hồ Chí Minh dài khoảng $1\ 200\text{ km}$.

6.32. Một ô tô khách khởi hành từ Hà Nội đi Hải Phòng. Sau đó $30$ phút, một ô tô con xuất phát từ cùng địa điểm ở Hà Nội và cũng đi về Hải Phòng trên cùng tuyến đường, với vận tốc lớn hơn vận tốc của ô tô khách là $20\text{ km/h}$. Hai xe đến cùng một địa điểm ở Hải Phòng tại cùng một thời điểm. Hãy tính vận tốc của mỗi ô tô, biết rằng quãng đường Hà Nội – Hải Phòng dài khoảng $120\text{ km}$.

6.33. Một xưởng may phải may $1\ 500$ chiếc áo trong thời gian quy định. Để hoàn thành sớm kế hoạch, mỗi ngày xưởng đã may được nhiều hơn $10$ chiếc áo so với số áo phải may trong một ngày theo kế hoạch. Do đó, ba ngày trước khi hết thời hạn, xưởng đã may được $1\ 320$ áo. Hỏi theo kế hoạch, mỗi ngày xưởng đó phải may xong bao nhiêu chiếc áo?
