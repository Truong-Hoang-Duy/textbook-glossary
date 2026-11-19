---
name: tu-dien-toan-12-chuong-6
description: Từ điển thuật ngữ Toán 12 Chương VI — Xác suất có điều kiện (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 12
chuong: "Chương VI. Xác suất có điều kiện"
bai_so: "Bài 18 – Bài 19"
nguon: "SGK Toán 12 Tập 2 – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: "2026-11-02"
ngay_cap_nhat: "2026-11-02"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 12 — CHƯƠNG VI: XÁC SUẤT CÓ ĐIỀU KIỆN

## Quy ước sử dụng

- **Phạm vi:** Chương VI (Bài 18, Bài 19, Bài tập cuối chương VI, 2 chủ đề Hoạt động thực hành trải nghiệm và Bài tập ôn tập cuối năm), SGK Toán 12 Tập 2 (bộ Kết nối tri thức với cuộc sống), tích hợp các mục tương ứng trong Bảng giải thích thuật ngữ cuối Tập 2 (trang in 95, PDF 97).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Tiếng Anh` | `Giải nghĩa` | `Bối cảnh sử dụng` (cột 2 ghi kí hiệu hoặc công thức toán học đặc trưng theo hồ sơ môn Toán).
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm, chú ý định nghĩa hoặc bảng giải thích thuật ngữ cuối sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp từ đoạn văn/công thức gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.
  - *Ngoài nguồn:* các khái niệm xác suất từ lớp 10–11 hoặc thuật ngữ ứng dụng được nhắc tới nhưng không định nghĩa trong Chương VI.

## Bài 18: Xác suất có điều kiện

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Xác suất có điều kiện (xác suất của $A$ với điều kiện $B$) | $P(A \mid B)$ | Cho hai biến cố $A$ và $B$. Xác suất của biến cố $A$, tính trong điều kiện biết rằng biến cố $B$ đã xảy ra, được gọi là xác suất của $A$ với điều kiện $B$ và kí hiệu là $P(A \mid B)$. | Trong Ví dụ 1, hộp có 20 viên bi trắng và 10 viên bi đen; khi Bình đã lấy được viên bi trắng (biến cố $B$ xảy ra) thì trong hộp còn 29 viên bi với 19 viên bi trắng, do đó xác suất để An lấy được viên bi trắng là $P(A \mid B) = \frac{19}{29}$ (Bài 18, mục 1, Ví dụ 1, trang 65, PDF 67; Bảng giải thích thuật ngữ Tập 2, trang 95, PDF 97). |
| Công thức tính xác suất có điều kiện | $P(A \mid B) = \frac{P(AB)}{P(B)} \ (P(B) > 0)$ | Cho hai biến cố $A$ và $B$ bất kì, với $P(B) > 0$. Khi đó $P(A \mid B) = \frac{P(AB)}{P(B)}$. | [mô tả] Nhờ công thức $P(A \mid B) = \frac{P(AB)}{P(B)} = \frac{n(AB)}{n(B)}$ khi các kết quả đồng khả năng, ta tính được $P(A \mid B) = \frac{20 \cdot 19}{20 \cdot 29} = \frac{19}{29}$ trong Ví dụ 1 và chứng minh được nếu $A, B$ độc lập thì $P(A \mid B) = P(A)$ trong Ví dụ 2 (Bài 18, mục 1, Ví dụ 1–2, trang 65–66, PDF 67–68). |
| Bảng dữ liệu thống kê $2 \times 2$ | — | Kết quả trên được trình bày dưới dạng bảng gồm 2 dòng và 2 cột như dưới đây, được gọi là bảng dữ liệu thống kê $2 \times 2$. | Trong Ví dụ 3, bảng dữ liệu thống kê $2 \times 2$ phân loại $577\,006$ vụ tai nạn giao thông theo hai tiêu chí (có/không thắt dây an toàn và tử vong/sống sót), giúp tính và so sánh hai xác suất có điều kiện $P(A \mid B) \approx 7,9 \cdot P(A \mid \overline{B})$ (Bài 18, mục 1, Ví dụ 3 và Luyện tập 3, trang 66–68, PDF 68–70). |
| Công thức nhân xác suất | $P(AB) = P(B) \cdot P(A \mid B)$ | Với hai biến cố $A$ và $B$ bất kì, ta có $P(AB) = P(B) \cdot P(A \mid B)$. Công thức trên được gọi là công thức nhân xác suất. | Vì $AB = BA$ nên ta cũng có $P(AB) = P(A) \cdot P(B \mid A)$; trong Ví dụ 4, xác suất để Sơn lấy được bút bi đen và Tùng lấy được bút bi xanh là $P(AB) = P(A) \cdot P(B \mid A) = \frac{5}{12} \cdot \frac{7}{11} = \frac{35}{132}$ (Bài 18, mục 2, Ví dụ 4, trang 68–69, PDF 70–71). |
| Công nghệ cập nhật Bayesian (Bayesian updating; công nghệ Bayesian updating) | $P(E_i \mid H), \ P(E_i \mid H, G)$ | Khi có thông tin mới $H$, ta cập nhật hiểu biết về $A$ bằng cách tính các xác suất có điều kiện xảy ra $A$ với điều kiện $H$: $P(E_1 \mid H), \dots, P(E_n \mid H)$. Cứ như thế, sử dụng các thông tin mới, ta liên tục cập nhật các hiểu biết về $A$. Quy trình này được gọi là công nghệ cập nhật Bayesian (công nghệ Bayesian updating). | Công nghệ cập nhật Bayesian được ứng dụng trong phần mềm tìm kiếm cứu nạn Sarops của Lực lượng bảo vệ bờ biển Mỹ để liên tục cập nhật vị trí và cứu sống ngư dân mất tích trên biển (Bài 18, mục Em có biết?, trang 71, PDF 73). |
| Biến cố độc lập | $P(AB) = P(A) \cdot P(B)$ | Ngoài nguồn — chưa định nghĩa trong Chương VI Toán 12. Xem: SGK Toán 11 Tập 2, Chương VIII | Trong Bài 18 (Ví dụ 2 và Luyện tập 2, trang 66, PDF 68), hai biến cố $A$ và $B$ độc lập có tính chất $P(AB) = P(A) \cdot P(B)$, suy ra việc xảy ra biến cố này không ảnh hưởng tới xác suất của biến cố kia: $P(A \mid B) = P(A)$ và $P(B \mid A) = P(B)$. |
| Biến cố đối | $\overline{A}, \ P(\overline{A}) = 1 - P(A)$ | Ngoài nguồn — chưa định nghĩa trong Chương VI Toán 12. Xem: SGK Toán 10 Tập 2, Chương IX | Trong Chương VI, biến cố đối $\overline{A}$ của biến cố $A$ được dùng thường xuyên trong xác suất có điều kiện $P(A \mid \overline{B})$, công thức xác suất toàn phần và công thức Bayes (Bài 18–19, trang 66–77, PDF 68–79). |
| Biến cố giao | $AB$ | Ngoài nguồn — chưa định nghĩa trong Chương VI Toán 12. Xem: SGK Toán 11 Tập 2, Chương VIII | Biến cố giao $AB$ (cả hai biến cố $A$ và $B$ cùng xảy ra) xuất hiện ở tử số của công thức tính xác suất có điều kiện $P(A \mid B) = \frac{P(AB)}{P(B)}$ và vế trái của công thức nhân xác suất (Bài 18, mục 1–2, trang 65–68, PDF 67–70). |

## Bài 19: Công thức xác suất toàn phần và công thức Bayes

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Công thức xác suất toàn phần | $P(B) = P(A) \cdot P(B \mid A) + P(\overline{A}) \cdot P(B \mid \overline{A})$ | Cho hai biến cố $A$ và $B$. Khi đó, ta có công thức sau: $P(B) = P(A) \cdot P(B \mid A) + P(\overline{A}) \cdot P(B \mid \overline{A})$. Công thức trên được gọi là công thức xác suất toàn phần. | Trong Ví dụ 1, biết thứ Hai ông An đi làm bằng xe buýt nên xác suất thứ Ba đi xe máy là $P(A) = 0,4$ và đi xe buýt là $P(\overline{A}) = 0,6$; áp dụng công thức xác suất toàn phần tính được xác suất thứ Tư ông An đi xe máy là $P(B) = 0,4 \cdot 0,3 + 0,6 \cdot 0,4 = 0,36$ (Bài 19, mục 1, Ví dụ 1, trang 72–73, PDF 74–75). |
| Sơ đồ hình cây | — | Một phương pháp mô tả trực quan công thức xác suất toàn phần là dùng sơ đồ hình cây. | [mô tả] Trên sơ đồ hình cây (Hình 6.2), nhánh cấp một $OA, O\overline{A}$ ghi $P(A), P(\overline{A})$ và nhánh cấp hai ghi các xác suất có điều kiện tương ứng, giúp nhận diện hai nhánh dẫn tới biến cố $B$ là $OAB$ và $O\overline{A}B$ (Bài 19, mục 1, Chú ý, trang 73–74, PDF 75–76). |
| Công thức Bayes | $P(A \mid B) = \frac{P(A) \cdot P(B \mid A)}{P(A) \cdot P(B \mid A) + P(\overline{A}) \cdot P(B \mid \overline{A})}$ | Cho $A$ và $B$ là hai biến cố, với $P(B) > 0$. Khi đó, ta có công thức sau: $P(A \mid B) = \frac{P(A) \cdot P(B \mid A)}{P(A) \cdot P(B \mid A) + P(\overline{A}) \cdot P(B \mid \overline{A})}$. Công thức trên có tên là công thức Bayes. | Công thức Bayes còn viết dưới dạng $P(A \mid B) = \frac{P(A) \cdot P(B \mid A)}{P(B)}$, cho phép tính lại xác suất xảy ra của biến cố $A$ khi biết sự kiện liên quan $B$ đã xảy ra, ví dụ tính xác suất học sinh đỗ đại học đã chọn tổ hợp A00 hoặc xác suất mắc bệnh khi xét nghiệm dương tính (Bài 19, mục 2, Ví dụ 2–4, trang 75–77, PDF 77–79; Bảng giải thích thuật ngữ Tập 2, trang 95, PDF 97). |
| Ý nghĩa của công thức Bayes | $P(A) = p \to P(A \mid B)$ | Một nhà nghiên cứu quan tâm đến xác suất xảy ra của biến cố $A$. Theo tính toán ban đầu $A$ có xác suất là $P(A) = p$. Sau đó, nhà nghiên cứu có được thông tin rằng: “Biến cố $B$ đã xảy ra”. Với thông tin mới này, nhà nghiên cứu sẽ cập nhật lại hiểu biết của mình về khả năng xảy ra biến cố $A$, bằng cách tính $P(A \mid B)$, xác suất của $A$ khi biết $B$ đã xảy ra. Công thức Bayes cho ta tính $P(A \mid B)$. | [mô tả] Trong Ví dụ 4, trước khi xét nghiệm xác suất không mắc bệnh Y của bà N là $P(\overline{A}) = 99,5\%$; sau khi có kết quả xét nghiệm âm tính ($\overline{B}$ xảy ra), công thức Bayes cập nhật xác suất không mắc bệnh của bà N tăng lên thành $P(\overline{A} \mid \overline{B}) \approx 99,97\%$ (Bài 19, mục 2, trang 75–77, PDF 77–79). |
| Dương tính giả và âm tính giả | $P(B \mid \overline{A}), \ P(\overline{B} \mid A)$ | Ngoài nguồn — chưa định nghĩa trong Chương VI Toán 12. Xem: Bài 19, mục 2 | Trong các bài toán chẩn đoán y học (Bài 19, mục 2, Ví dụ 3–4, trang 75–77, PDF 77–79), dương tính giả (xét nghiệm dương tính nhưng thực tế không mắc bệnh) và âm tính giả (xét nghiệm âm tính nhưng thực tế mắc bệnh) được biểu diễn bằng các xác suất có điều kiện $P(B \mid \overline{A})$ và $P(\overline{B} \mid A)$. |
| Kiểu gene và kiểu hình | $BB, \ Bb, \ bb$ | Ngoài nguồn — chưa định nghĩa trong Chương VI Toán 12. Xem: Bài 19, Vận dụng | Trong bài toán di truyền học ở đậu Hà Lan (Bài 19, mục 1, Vận dụng và Luyện tập 3, trang 74, PDF 76), công thức xác suất toàn phần được dùng để tính xác suất cây con nhận alen lặn $b$ từ bố mẹ và ước lượng tỉ lệ các kiểu gene $bb, BB, Bb$ ở thế hệ con. |

## Đã xét, không tạo mục

- xác suất — gộp vào Xác suất có điều kiện: cụm từ tách tự động từ định nghĩa xác suất của $A$ với điều kiện $B$ trong Bài 18
- phương pháp hình thang — chỉ có trong ví dụ, bài tập: phương pháp tính gần đúng tích phân trong bài Hoạt động thực hành trải nghiệm cuối Tập 2
- mặt Mobius — chỉ có trong ví dụ, bài tập: đối tượng hình học minh hoạ lệnh vẽ mặt cong 3D bằng phần mềm GeoGebra trong bài Hoạt động thực hành trải nghiệm cuối Tập 2

## Ghi chú nguồn cần kiểm tra

Không có ghi chú nguồn mở.
