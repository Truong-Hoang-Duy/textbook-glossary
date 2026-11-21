---
name: tu-dien-toan-8-chuong-8
description: Từ điển thuật ngữ Toán 8 Chương VIII — Mở đầu về tính xác suất của biến cố (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 8
chuong: "Chương VIII. Mở đầu về tính xác suất của biến cố"
bai_so: "Bài 30–32"
nguon: "SGK TOAN 8 TAP 2 - KNTT.pdf, Chương VIII (Tầng 1 trong lessons/khoi_8/toan_8/)"
ngay_tao: "2026-11-21"
ngay_cap_nhat: "2026-11-21"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 8 — CHƯƠNG VIII: MỞ ĐẦU VỀ TÍNH XÁC SUẤT CỦA BIẾN CỐ

## Quy ước sử dụng

- **Phạm vi:** Chương VIII (Bài 30 đến Bài 32, Luyện tập chung và Bài tập cuối chương VIII), Tập hai, SGK Toán 8 (bộ Kết nối tri thức với cuộc sống), đối chiếu đầy đủ Bảng tra cứu thuật ngữ (trang in 138, PDF 139) và Bảng giải thích thuật ngữ cuối Tập hai (trang in 139, PDF 140).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Tiếng Anh` | `Giải nghĩa` | `Bối cảnh sử dụng`.
- **Kí hiệu toán học:** Biến cố thường kí hiệu bằng chữ cái in hoa ($A, B, E, F, \dots$); xác suất của biến cố $E$ kí hiệu là $P(E)$. Mọi công thức, tỉ số, xấp xỉ viết bằng LaTeX trong cặp dấu `$...$`.
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm có thuật ngữ in đậm ở Tầng 1 hoặc Bảng giải thích thuật ngữ cuối sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp sát nguyên văn nhận xét, quy tắc, công thức gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.
  - *Ngoài nguồn:* khái niệm đã học ở lớp dưới được sử dụng trực tiếp trong Chương VIII nhưng không định nghĩa lại.

## Bài 30: Kết quả có thể và kết quả thuận lợi

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Kết quả có thể (kết quả có thể của hành động, thực nghiệm; kết quả có thể của một phép thử) | Possible outcome | Trong thực tế, ta thường gặp các hành động, thực nghiệm mà kết quả của chúng không thể biết trước khi thực hiện. Tuy nhiên, trong nhiều trường hợp ta có thể xác định được tất cả các kết quả có thể xảy ra (gọi tắt là các kết quả có thể) của hành động, thực nghiệm đó. | Mục 1 (trang 60, PDF 61) và Bảng tra cứu thuật ngữ (trang 138, PDF 139). |
| Kết quả thuận lợi (kết quả thuận lợi cho một biến cố) | Favorable outcome | Xét một biến cố $E$, mà $E$ có xảy ra hay không xảy ra tuỳ thuộc vào kết quả của hành động, thực nghiệm $T$. Một kết quả có thể của $T$ để biến cố $E$ xảy ra được gọi là kết quả thuận lợi cho biến cố $E$. | Mục 2, khung kiến thức trọng tâm (trang 61, PDF 62) và Bảng tra cứu thuật ngữ (trang 138, PDF 139). |
| Biến cố | Event; $E$ | Ngoài nguồn — chưa định nghĩa trong Chương VIII. Xem: Toán 7 Tập hai, Bài 29 Làm quen với biến cố, PDF 49 | Khái niệm nền tảng từ lớp 7 được dùng xuyên suốt các bài trong Chương VIII để xét kết quả thuận lợi và tính xác suất. |

## Bài 31: Cách tính xác suất của biến cố bằng tỉ số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Đồng khả năng | Equally likely | Giả thiết rằng các kết quả có thể của một hành động hay thực nghiệm là đồng khả năng (có cùng khả năng xảy ra như nhau); khi đó xác suất của biến cố $E$ bằng tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và tổng số kết quả có thể. | Mục Cách tính xác suất bằng tỉ số, khung kiến thức trọng tâm (trang 63, PDF 64). |
| Xác suất của một biến cố (trường hợp cổ điển; xác suất của biến cố; xác suất; công thức tính xác suất) | Probability of an event (classical definition); $P(E)$ | Giả thiết rằng các kết quả có thể của một hành động hay thực nghiệm là đồng khả năng. Khi đó, xác suất của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và tổng số kết quả có thể. | Khung kiến thức trọng tâm (trang 63, PDF 64), Bảng tra cứu thuật ngữ (trang 138, PDF 139) và Bảng giải thích thuật ngữ cuối sách (trang 139, PDF 140). |
| Các bước tính xác suất của biến cố bằng tỉ số | Steps to calculate classical probability | Việc tính xác suất của một biến cố $E$ trong một hành động hay thực nghiệm đồng khả năng sẽ gồm các bước sau: Bước 1. Đếm các kết quả có thể (thường bằng cách liệt kê); Bước 2. Chỉ ra các kết quả có thể là đồng khả năng; Bước 3. Đếm các kết quả thuận lợi cho biến cố $E$; Bước 4. Lập tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và tổng số kết quả có thể. | [mô tả] Nhận xét đầu trang 64 (PDF 65). |

## Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Xác suất thực nghiệm của một biến cố (xác suất thực nghiệm; xác suất thực nghiệm của biến cố) | Empirical (experimental) probability of an event; $\dfrac{k}{n}$ | Giả sử trong $n$ lần thực nghiệm hoặc $n$ lần theo dõi (quan sát) một hiện tượng ta thấy biến cố $E$ xảy ra $k$ lần. Khi đó xác suất thực nghiệm của biến cố $E$ bằng $\dfrac{k}{n}$, tức là bằng tỉ số giữa số lần xuất hiện biến cố $E$ và số lần thực hiện thực nghiệm hoặc theo dõi hiện tượng đó. | Mục 1, khung kiến thức trọng tâm (trang 67, PDF 68), Bảng tra cứu thuật ngữ (trang 138, PDF 139) và Bảng giải thích thuật ngữ cuối sách (trang 139, PDF 140). |
| Ước lượng xác suất của một biến cố bằng xác suất thực nghiệm | Estimating probability using empirical probability; $P(E) \approx \dfrac{k}{n}$ | Xác suất của biến cố $E$ được ước lượng bằng xác suất thực nghiệm của $E$: $P(E) \approx \dfrac{k}{n}$; trong đó $n$ là số lần thực nghiệm hay theo dõi một hiện tượng, $k$ là số lần biến cố $E$ xảy ra. | [mô tả] Mục 2, khung kiến thức ước lượng xác suất của biến cố (trang 68, PDF 69). |
| Ứng dụng của xác suất thực nghiệm | Application of empirical probability | Xác suất thực nghiệm có thể sử dụng để đưa ra dự báo số lần xảy ra một sự kiện, hiện tượng trong tương lai. | [mô tả] Mục 3, câu trọng tâm về ứng dụng dự báo của xác suất thực nghiệm (trang 69, PDF 70). |

### Luyện tập chung (trang 74)

Bài luyện tập tổng hợp tính xác suất bằng tỉ số (khi các kết quả có thể đồng khả năng), tính xác suất thực nghiệm và dự đoán số lần xảy ra biến cố trong tương lai; không giới thiệu thuật ngữ toán học mới.

### Bài tập cuối chương VIII

Hệ thống bài tập trắc nghiệm và tự luận ôn tập toàn bộ kiến thức Chương VIII về kết quả có thể, kết quả thuận lợi, xác suất của biến cố bằng tỉ số và xác suất thực nghiệm; không giới thiệu thuật ngữ mới.

## Đã xét, không tạo mục

- số $\pi$ — chỉ nhắc tên: kiến thức số vô tỉ ở lớp 7 nhắc lại trong mục Em có biết? (Bài 32, PDF 74)

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bài 31 (Tranh luận, pdf:66) — Thuật ngữ: Kết quả có thể — Đề bài nêu túi có $8$ viên bi màu đỏ, $5$ viên bi màu xanh và $4$ viên bi màu vàng, nhưng trong bóng thoại của nhân vật Vuông sách in là “viên bi màu đỏ, viên bi màu trắng và viên bi màu vàng” → Đã đối chiếu ảnh trang PDF 66, giữ nguyên văn chữ “màu trắng” theo quy tắc bảo toàn bản in gốc ở Tầng 1 (2026-11-21)
