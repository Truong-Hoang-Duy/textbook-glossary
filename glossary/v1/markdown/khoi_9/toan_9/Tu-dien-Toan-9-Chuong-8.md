---
name: tu-dien-toan-9-chuong-8
description: Từ điển thuật ngữ Toán 9 Chương VIII — Xác suất của biến cố trong một số mô hình xác suất đơn giản (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 9
chuong: "Chương VIII. Xác suất của biến cố trong một số mô hình xác suất đơn giản"
bai_so: "Bài 25–26"
nguon: "SGK TOAN 9 TAP 2 - KNTT.pdf, Chương VIII (Tầng 1 trong lessons/khoi_9/toan_9/)"
ngay_tao: "2026-11-21"
ngay_cap_nhat: "2026-11-21"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 9 — CHƯƠNG VIII: XÁC SUẤT CỦA BIẾN CỐ TRONG MỘT SỐ MÔ HÌNH XÁC SUẤT ĐƠN GIẢN

## Quy ước sử dụng

- **Phạm vi:** Chương VIII (Bài 25, Bài 26, Luyện tập chung trang 64 và Bài tập cuối chương VIII), Tập hai, SGK Toán 9 (bộ Kết nối tri thức với cuộc sống), đối chiếu đầy đủ với Bảng giải thích thuật ngữ Tập hai (trang in 131, PDF 133).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Tiếng Anh` | `Giải nghĩa` | `Bối cảnh sử dụng`.
- **Kí hiệu toán học:** Không gian mẫu của phép thử kí hiệu là $\Omega$, số phần tử của không gian mẫu kí hiệu là $n(\Omega)$; biến cố thường kí hiệu bằng chữ cái in hoa ($A, B, E, F, G, \dots$), số kết quả thuận lợi cho biến cố $E$ kí hiệu là $n(E)$, xác suất của biến cố $E$ kí hiệu là $P(E)$. Mọi công thức viết bằng LaTeX trong cặp dấu `$...$`.
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm có thuật ngữ in đậm ở Tầng 1 hoặc Bảng giải thích thuật ngữ cuối Tập hai.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp sát nguyên văn quy trình các bước tính xác suất gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.
  - *Ngoài nguồn:* các khái niệm biến cố, đồng khả năng đã học ở lớp 7, lớp 8 được vận dụng trực tiếp nhưng không định nghĩa lại trong Chương VIII.

## Bài 25: Phép thử ngẫu nhiên và không gian mẫu

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Phép thử ngẫu nhiên (phép thử) | Random experiment (trial) | Một hoặc một số hành động, thực nghiệm được tiến hành liên tiếp hay đồng thời mà kết quả của chúng không thể biết được trước khi thực hiện nhưng có thể liệt kê được tất cả các kết quả có thể xảy ra, được gọi là một phép thử ngẫu nhiên, gọi tắt là phép thử. | Khung kiến thức trọng tâm sau HĐ (trang 57, PDF 59). |
| Không gian mẫu của phép thử (không gian mẫu; không gian mẫu của một phép thử ngẫu nhiên; tập tất cả các kết quả có thể của phép thử) | Sample space; $\Omega$ | Tập hợp tất cả các kết quả có thể xảy ra của phép thử (gọi tắt là tập tất cả các kết quả có thể của phép thử) được gọi là không gian mẫu của phép thử. Không gian mẫu của phép thử được kí hiệu là $\Omega$. | Khung kiến thức trọng tâm sau HĐ (trang 57, PDF 59) và Bảng giải thích thuật ngữ Tập hai (trang 131, PDF 133). |

## Bài 26: Xác suất của biến cố liên quan tới phép thử

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Kết quả thuận lợi (kết quả thuận lợi cho biến cố; kết quả thuận lợi cho $E$) | Favorable outcome | Cho phép thử $T$. Xét biến cố $E$, ở đó việc xảy ra hay không xảy ra của $E$ tuỳ thuộc vào kết quả của phép thử $T$. Kết quả của phép thử $T$ làm cho biến cố $E$ xảy ra gọi là kết quả thuận lợi cho $E$. | Mục 1, khung kiến thức trọng tâm sau HĐ (trang 60, PDF 62). |
| Xác suất của biến cố liên quan tới phép thử (xác suất) | Probability of an event; $P(E) = \dfrac{n(E)}{n(\Omega)}$ | Giả sử rằng các kết quả có thể của phép thử $T$ là đồng khả năng. Khi đó xác suất $P(E)$ của biến cố $E$ bằng tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và số phần tử của tập $\Omega$: $P(E) = \dfrac{n(E)}{n(\Omega)}$, trong đó $\Omega$ là không gian mẫu của $T$; $n(E)$ là số kết quả thuận lợi cho biến cố $E$ và $n(\Omega)$ là số phần tử của tập $\Omega$. | Mục 2, khung kiến thức trọng tâm cuối trang 61 (PDF 63). |
| Các bước tính xác suất của một biến cố | Steps to calculate the probability of an event | Việc tính xác suất của một biến cố $E$ gồm các bước sau: Bước 1. Mô tả không gian mẫu của phép thử, từ đó xác định số phần tử của không gian mẫu $\Omega$; Bước 2. Chứng tỏ các kết quả có thể của phép thử là đồng khả năng; Bước 3. Mô tả các kết quả thuận lợi cho biến cố $E$, từ đó xác định số kết quả thuận lợi cho biến cố $E$; Bước 4. Lập tỉ số giữa số kết quả thuận lợi cho biến cố $E$ với số phần tử của không gian mẫu $\Omega$. | [mô tả] Mục 2, khung phương pháp đầu trang 62 (PDF 64). |
| Biến cố | Event; $E$ | Ngoài nguồn — chưa định nghĩa trong Chương VIII Toán 9. Xem: SGK Toán 7 Tập 2, Chương VIII, Bài 29 (PDF 49) | Khái niệm nền tảng được liệt kê trong khung thuật ngữ đầu Bài 26 và dùng xuyên suốt Chương VIII. |
| Đồng khả năng | Equally likely | Ngoài nguồn — chưa định nghĩa trong Chương VIII Toán 9. Xem: SGK Toán 8 Tập 2, Chương VIII, Bài 31 (PDF 64) | Điều kiện tiên quyết để áp dụng công thức $P(E) = \dfrac{n(E)}{n(\Omega)}$ trong Bài 26, Luyện tập chung và Bài tập cuối chương VIII. |

### Luyện tập chung (trang 64)

Bài luyện tập củng cố cách lập bảng liệt kê không gian mẫu $\Omega$ của phép thử gồm hai hành động độc lập hoặc liên tiếp, xác định số kết quả thuận lợi và tính xác suất $P(E) = \dfrac{n(E)}{n(\Omega)}$; không giới thiệu thuật ngữ toán học mới.

### Bài tập cuối chương VIII

Hệ thống câu hỏi trắc nghiệm và bài tập tự luận ôn tập toàn bộ kiến thức Chương VIII về phép thử ngẫu nhiên, không gian mẫu và xác suất của biến cố trong một số mô hình xác suất đơn giản; không giới thiệu thuật ngữ mới.

## Đã xét, không tạo mục

- kiểu hình (kiểu gene; allele trội; allele lặn) — chỉ có trong ví dụ, bài tập: ngữ liệu di truyền học đậu Hà Lan dùng trong phần Vận dụng Bài 25 (PDF 61), Mở đầu và Ví dụ 3 Bài 26 (PDF 62, 64–65)

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bài 25 (Mở đầu, pdf:58) — Thuật ngữ: Phép thử ngẫu nhiên — Câu gần cuối đoạn mở đầu Bài 25 (trang in 56, PDF 58) sách in "Hai khách hành có tên trong hai lá phiếu được rút ra..." ("khách hành" thay vì "khách hàng") → Đã đối chiếu trực tiếp ảnh trang PDF 58, giữ nguyên văn chữ in gốc ở Tầng 1 (2026-11-21)
2. [đóng] Bài 25 (Ví dụ 1b, pdf:59) — Thuật ngữ: Không gian mẫu của phép thử — Trong tập hợp không gian mẫu $\Omega$ ở lời giải Ví dụ 1b (trang in 57, PDF 59), sách in `{(1, S); (2, S); (3, S); (4, S) (5, S) (6, S); (1, N); ...}` (thiếu dấu chấm phẩy giữa ba phần tử `(4, S)`, `(5, S)` và `(6, S)`) → Đã đối chiếu trực tiếp ảnh trang PDF 59, giữ nguyên văn ở Tầng 1 theo quy tắc nguyên văn (2026-11-21)
