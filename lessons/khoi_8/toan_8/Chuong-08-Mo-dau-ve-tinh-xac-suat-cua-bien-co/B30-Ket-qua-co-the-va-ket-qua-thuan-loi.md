---
unit: toan_8
lesson_id: b30
toc_path:
  - "Chương VIII. Mở đầu về tính xác suất của biến cố"
  - "Bài 30. Kết quả có thể và kết quả thuận lợi"
source_file: "SGK TOAN 8 TAP 2 - KNTT.pdf"
pdf_pages: [60, 63]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:60 -->
<!-- Phần giới thiệu đầu Chương VIII (nửa trên trang PDF 60): XÁC SUẤT — CHƯƠNG VIII: MỞ ĐẦU VỀ TÍNH XÁC SUẤT CỦA BIẾN CỐ -->

Trong chương này các em sẽ được biết cách tính xác suất của một số biến cố đơn giản và ước lượng xác suất của biến cố bằng xác suất thực nghiệm.

# BÀI 30: KẾT QUẢ CÓ THỂ VÀ KẾT QUẢ THUẬN LỢI

## 🔤 Khái niệm, thuật ngữ

- Kết quả có thể
- Kết quả thuận lợi

## 🎯 Kiến thức, kĩ năng

- Xác định các kết quả có thể của hành động, thực nghiệm.
- Xác định các kết quả thuận lợi cho một biến cố liên quan tới hành động, thực nghiệm.

## 🔴 Mở đầu

Tại vòng chung kết cuộc thi *Chinh phục tri thức*, ban tổ chức soạn $20$ câu hỏi thuộc các lĩnh vực khác nhau, mỗi câu hỏi được viết trong một phiếu và được đánh số từ $1$ đến $20$. Các câu hỏi từ số $1$ đến số $4$ thuộc lĩnh vực Lịch sử – Địa lí, từ số $5$ đến số $12$ thuộc lĩnh vực Khoa học tự nhiên, từ số $13$ đến số $18$ thuộc lĩnh vực Văn học; từ số $19$ đến số $20$ thuộc lĩnh vực Toán học.

Bạn Sơn rút ngẫu nhiên một phiếu từ hộp đựng các phiếu câu hỏi. Sơn học giỏi môn Lịch sử nên mong rút được câu hỏi thuộc lĩnh vực Lịch sử – Địa lí.

Liệu bạn Sơn có rút được phiếu câu hỏi mình mong muốn không?

<!-- pdf:61 -->

## 1. KẾT QUẢ CÓ THỂ CỦA HÀNH ĐỘNG, THỰC NGHIỆM

**Kết quả có thể**

**HĐ1:** Trong *tình huống mở đầu*, em hãy cho biết:

a) Bạn Sơn có chắc chắn rút được phiếu câu hỏi số $2$ hay không?

b) Khi bạn Sơn rút một phiếu bất kì thì có bao nhiêu kết quả có thể xảy ra?

Trong thực tế, ta thường gặp các hành động, thực nghiệm mà kết quả của chúng không thể biết trước khi thực hiện. Tuy nhiên, trong nhiều trường hợp ta có thể xác định được tất cả các kết quả có thể xảy ra (gọi tắt là các **kết quả có thể**) của hành động, thực nghiệm đó.

**Ví dụ 1:** Một hộp đựng $5$ quả cầu màu xanh được đánh số $1; 2; 3; 4; 5$ và $4$ quả cầu màu đỏ được đánh số $1; 2; 3; 4$. Lấy ngẫu nhiên một quả cầu trong hộp. Liệt kê tất cả các kết quả có thể của hành động này. Có bao nhiêu kết quả có thể?

![Minh hoạ 5 quả cầu màu xanh và 4 quả cầu màu đỏ](img/H8-toan-b30-01.png)

**Giải**

Kí hiệu $5$ quả cầu màu xanh được đánh số $1; 2; 3; 4; 5$ là $\text{X1, X2, X3, X4, X5}$ và $4$ quả cầu màu đỏ được đánh số $1; 2; 3; 4$ là $\text{D1, D2, D3, D4}$.

Các kết quả có thể của hành động này là $\text{X1, X2, X3, X4, X5, D1, D2, D3, D4}$.

Có tất cả $9$ kết quả có thể.

**Luyện tập 1:** Chọn ngẫu nhiên một chữ cái trong cụm từ “TOÁN HỌC VÀ TUỔI TRẺ”. Liệt kê tất cả các kết quả có thể của hành động này.

![Bảng chữ cái tiếng Việt](img/H8-toan-b30-02.png)

**Tranh luận**

Một túi đựng $12$ viên bi có hình dạng như nhau, chỉ khác màu, trong đó có $5$ viên bi màu đỏ, $4$ viên bi màu xanh và $3$ viên bi màu vàng. Lấy ngẫu nhiên một viên bi trong túi. Hỏi có tất cả bao nhiêu kết quả có thể?

- **Tròn:** Có $12$ viên bi nên có $12$ kết quả có thể.
- **Vuông:** Không đúng! Các viên bi có hình dạng như nhau, chỉ khác màu nên có $3$ kết quả có thể là bi màu đỏ, bi màu xanh và bi màu vàng.

Theo em, bạn nào nói đúng?

<!-- pdf:62 -->

## 2. KẾT QUẢ THUẬN LỢI CHO MỘT BIẾN CỐ

**Kết quả thuận lợi**

Trở lại *tình huống mở đầu*, kết quả của hành động rút ngẫu nhiên một phiếu câu hỏi của Sơn là một câu hỏi nào đó trong số $20$ câu hỏi được đánh số từ $1$ đến $20$. Có $20$ kết quả có thể là phiếu số $1$, phiếu số $2, \dots,$ phiếu số $20$.

Xét biến cố $E$: “Sơn rút được phiếu câu hỏi thuộc lĩnh vực Lịch sử – Địa lí”.

**HĐ2:** Em hãy xác định các kết quả có thể để biến cố $E$ xảy ra.

> Xét một biến cố $E$, mà $E$ có xảy ra hay không xảy ra tuỳ thuộc vào kết quả của hành động, thực nghiệm $T$.
>
> Một kết quả có thể của $T$ để biến cố $E$ xảy ra được gọi là **kết quả thuận lợi** cho biến cố $E$.

**Ví dụ 2:** Đội văn nghệ khối $8$ của một trường Trung học cơ sở có $14$ bạn, trong đó có $4$ bạn nam lớp 8A, $5$ bạn nữ lớp 8B, $3$ bạn nam lớp 8C và $2$ bạn nữ lớp 8D. Chọn ngẫu nhiên một bạn trong đội văn nghệ khối $8$ để tham gia tiết mục văn nghệ của trường.

a) Liệt kê tất cả các kết quả có thể của hành động trên. Có tất cả bao nhiêu kết quả có thể?

b) Liệt kê các kết quả thuận lợi cho các biến cố sau:

- $E$: “Chọn được một bạn lớp 8A”;
- $F$: “Chọn được một bạn nữ”.

**Giải**

Kí hiệu $4$ bạn nam lớp 8A là $\text{A1, A2, A3, A4}$;

$5$ bạn nữ lớp 8B là $\text{B1, B2, B3, B4, B5}$;

$3$ bạn nam lớp 8C là $\text{C1, C2, C3}$;
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 62, OCR đọc nhầm "8C" thành "8G" -->

$2$ bạn nữ lớp 8D là $\text{D1, D2}$.

<!-- pdf:63 -->

a) Các kết quả có thể của hành động trên là $\text{A1, A2, A3, A4, B1, B2, B3, B4, B5, C1, C2, C3, D1, D2}$. Có $14$ kết quả có thể.

b) Biến cố $E$ xảy ra khi ta chọn được một bạn lớp 8A. Do đó các kết quả thuận lợi cho biến cố $E$ là $\text{A1, A2, A3, A4}$.

Biến cố $F$ xảy ra khi ta chọn được một bạn nữ. Do đó các kết quả thuận lợi cho biến cố $F$ là $\text{B1, B2, B3, B4, B5, D1, D2}$.

**Luyện tập 2:** Trở lại Ví dụ 2, hãy liệt kê các kết quả thuận lợi cho các biến cố sau:

- $G$: “Chọn được một bạn nam”;
- $H$: “Chọn được một bạn lớp 8C hoặc 8D”.

## BÀI TẬP

8.1. Vuông thực nghiệm gieo một con xúc xắc.

a) Liệt kê các kết quả có thể của thực nghiệm trên.

b) Liệt kê các kết quả thuận lợi cho các biến cố sau:

- $A$: “Số chấm xuất hiện trên con xúc xắc là hợp số”;
- $B$: “Số chấm xuất hiện trên con xúc xắc nhỏ hơn $5$”;
- $C$: “Số chấm xuất hiện trên con xúc xắc là số lẻ”.

8.2. Một hộp đựng $12$ tấm thẻ, được ghi số $1; 2; \dots; 12$. Bạn Nam rút ngẫu nhiên một tấm thẻ từ trong hộp.

a) Liệt kê các kết quả có thể của hành động trên.

b) Liệt kê các kết quả thuận lợi cho các biến cố sau:

- $A$: “Rút được tấm thẻ ghi số chẵn”;
- $B$: “Rút được tấm thẻ ghi số nguyên tố”;
- $C$: “Rút được tấm thẻ ghi số chính phương”.

8.3. Bạn An có $16$ cuốn sách, trong đó có $4$ cuốn sách tiểu thuyết, $5$ cuốn sách Lịch sử, $3$ cuốn sách Khoa học tự nhiên và $4$ cuốn sách Toán. Các cuốn sách này được xếp tuỳ ý trong tủ sách. Bạn Bình đến chơi và lấy ngẫu nhiên một cuốn sách trong tủ sách của An.

a) Liệt kê các kết quả có thể của hành động trên.

b) Liệt kê các kết quả thuận lợi cho các biến cố sau:

- $E$: “Bình lấy được một cuốn sách tiểu thuyết”;
- $F$: “Bình lấy được một cuốn sách Khoa học tự nhiên hoặc cuốn sách Toán”;
- $G$: “Bình lấy được một cuốn sách không phải là sách Lịch sử”.

## 📷 Danh sách hình trong bài

| Mã hình | Trang PDF | Vị trí trong bài | Chú thích gốc |
| --- | :---: | --- | --- |
| H8-toan-b30-01 | 61 | Mục 1, Ví dụ 1 | (sách không đánh số, minh hoạ $5$ quả cầu màu xanh đánh số $1$–$5$ và $4$ quả cầu màu đỏ đánh số $1$–$4$) |
| H8-toan-b30-02 | 61 | Mục 1, Luyện tập 1 | (sách không đánh số, bảng $29$ chữ cái tiếng Việt) |
