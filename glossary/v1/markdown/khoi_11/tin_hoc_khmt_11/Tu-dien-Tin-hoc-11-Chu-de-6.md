---
name: tu-dien-tin-hoc-11-chu-de-6
description: "Từ điển thuật ngữ Tin học 11 – Định hướng Khoa học máy tính — Chủ đề 6. Kĩ thuật lập trình (Bài 17–31) theo SGK Kết nối tri thức với cuộc sống"
loai_hoc_lieu: tu_dien_thuat_ngu
mon: "Tin học – Định hướng Khoa học máy tính"
lop: 11
chuong: "Chủ đề 6. Kĩ thuật lập trình"
bai_so: [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
nguon: "SGK TIN HOC 11 CS - KNTT.pdf, Bài 17–31 (Tầng 1 trong textbook/khoi_11/tin_hoc_khmt_11/Chu-de-06-Ki-thuat-lap-trinh/)"
ngay_tao: 2026-11-06
ngay_cap_nhat: 2026-11-06
trang_thai: verified
---

# Từ điển thuật ngữ — Tin học 11 – Định hướng Khoa học máy tính: Chủ đề 6. Kĩ thuật lập trình

> Tài liệu này tổng hợp thuật ngữ, khái niệm và cấu trúc lập trình của Chủ đề 6 (Bài 17–31) thuộc SGK Tin học 11 – Định hướng Khoa học máy tính (Kết nối tri thức với cuộc sống), trích xuất đối chiếu trực tiếp từ văn bản Tầng 1 và Bảng giải thích thuật ngữ cuối sách.

## Quy ước sử dụng

- **Thuật ngữ**: Tên khái niệm hoặc nhãn mô tả nội dung; tên gọi thay thế trong SGK được ghi trong ngoặc đơn `(...)`.
- **Tiếng Anh**: Thuật ngữ tiếng Anh hoặc tên hàm/từ khoá Python tương ứng nếu SGK có nêu; ghi `—` nếu SGK không nêu.
- **Giải nghĩa**: Trích sát định nghĩa hoặc câu mô tả từ văn bản SGK Tầng 1 và Bảng giải thích thuật ngữ cuối sách; không suy diễn ngoài phạm vi SGK.
- **Bối cảnh sử dụng**: Ngữ cảnh xuất hiện trong bài học. Nhãn `[mô tả]` ở đầu cột này đánh dấu mục từ được gắn qua thẻ `<!-- term: ... -->` cho đoạn mô tả/hộp kiến thức không in đậm tên khái niệm trong SGK.

---

## Bài 17: Dữ liệu mảng một chiều và hai chiều

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Dữ liệu mảng một chiều (Cấu trúc dữ liệu tuyến tính) | — | Trong Tin học, dữ liệu mảng một chiều, thường được gọi là cấu trúc dữ liệu tuyến tính, là cấu trúc dữ liệu bao gồm một dãy các phần tử dữ liệu có cùng kiểu. Các phần tử của mảng sẽ được truy cập theo chỉ số, cho phép các thao tác đơn giản như cập nhật và thay đổi giá trị. | Thiết lập và truy cập mảng một chiều bằng kiểu dữ liệu danh sách (list) trong Python (Mục 1, trang 81). |
| Cấu trúc dữ liệu mảng một chiều trong Python | — | Cấu trúc dữ liệu mảng một chiều trong Python có thể biểu diễn bằng kiểu dữ liệu danh sách (list) với chức năng truy cập dễ dàng từng phần tử theo chỉ số, truy cập theo vùng chỉ số. Toán tử in và lệnh for .. in sẽ hỗ trợ duyệt từng phần tử của mảng. | [mô tả] Hộp kiến thức tổng kết về cấu trúc dữ liệu mảng một chiều trong Python (Mục 1, trang 82). |
| Mô hình dữ liệu danh sách trong danh sách | — | Python hỗ trợ mô hình dữ liệu danh sách trong danh sách, tức là mỗi phần tử của danh sách là một đối tượng dạng danh sách khác. | Biểu diễn bảng điểm của học sinh hoặc ma trận trong Python (Mục 2, Hoạt động 2, trang 83). |
| Cấu trúc dữ liệu hai chiều (Bảng) | — | Trong tin học, một cấu trúc dữ liệu hai chiều được hiểu là một bảng hay còn gọi là ma trận, bao gồm các hàng và cột dữ liệu. Bảng có thể có kích thước vuông $n \times n$ hoặc kích thước bất kì $m \times n$. | Khái niệm mảng hai chiều và ma trận kích thước $m \times n$ (Mục 2, Hoạt động 3, trang 83). |
| Cấu trúc dữ liệu 2 chiều trong Python | — | Trong Python cấu trúc dữ liệu 2 chiều có thể được biểu diễn bằng mô hình list trong list. Có thể truy cập từng phần tử và duyệt cấu trúc dữ liệu 2 chiều bằng 2 lệnh for lồng nhau. | [mô tả] Hộp kiến thức tổng kết về cấu trúc dữ liệu hai chiều trong Python (Mục 2, trang 84). |

---

## Bài 18: Thực hành dữ liệu mảng một chiều và hai chiều

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Duyệt mảng một chiều bằng cấu trúc for | — | Nhiệm vụ này có thể được thực hiện bằng cách sử dụng mảng một chiều, cụ thể là sử dụng danh sách trong python. Sau khi đã có danh sách các đầu điểm, dùng cấu trúc for để lặp qua các phần tử của mảng để tính tổng điểm, thống kê điểm cao nhất, thấp nhất. | [mô tả] Phân tích chương trình `qldiem.py` quản lí điểm kiểm tra một môn học của một học sinh (Nhiệm vụ 1, trang 86). |
| Duyệt mảng hai chiều bằng vòng lặp | — | Nhiệm vụ này có thể được thực hiện bằng cách sử dụng một mảng hai chiều để lưu tất cả điểm của học sinh trong lớp, mỗi hàng là điểm của một sinh viên, điểm cụ thể là các phần tử của hàng. Để thống kê cần dùng vòng lặp để duyệt qua từng hàng, tính trung bình từng hàng và xét từng điểm để tìm ra đầu điểm thấp nhất. | [mô tả] Phân tích chương trình `qldiem_ca_lop.py` quản lí điểm kiểm tra của tất cả học sinh trong lớp (Nhiệm vụ 2, trang 87). |

---

## Bài 19: Bài toán tìm kiếm

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Bài toán tìm kiếm (Miền dữ liệu) | — | Có thể nói bài toán tìm kiếm là một trong những bài toán quan trọng nhất của Tin học. Việc thiết kế thuật toán tìm kiếm sẽ phụ thuộc vào cấu trúc của miền dữ liệu cần tìm kiếm và tiêu chí cụ thể của bài toán tìm kiếm. | Tìm hiểu bài toán tìm kiếm trên thực tế và xác định miền dữ liệu, kết quả tìm kiếm (Mục 1, trang 89). |
| Tìm kiếm tuần tự | — | Cách An lần lượt lật các thẻ từ đầu đến cuối trong phần khởi động chính là việc thực hiện tìm kiếm tuần tự trong các thẻ bài. Đây là một trường hợp riêng của việc tìm kiếm trên mô hình dữ liệu là một dãy các đối tượng (danh sách) và thuật toán được thực hiện một cách tuần tự. | Giới thiệu bài toán tìm kiếm phần tử bằng K trên dãy số (Mục 2, trang 90). |
| Thuật toán tìm kiếm tuần tự | LinearSeach | Thuật toán tìm kiếm tuần tự được thực hiện bằng cách duyệt lần lượt các phần tử của dãy từ đầu đến cuối để tìm phần tử có giá trị bằng giá trị cần tìm. | Hộp kiến thức tổng kết thuật toán tìm kiếm tuần tự trên dãy số (Mục 2, trang 91). |
| Tìm kiếm nhị phân | — | Khác với bài toán tìm kiếm tuần tự, bài toán tìm kiếm nhị phân tìm kiếm với dãy số đã được sắp xếp. Khi duyệt một phần tử bất kì của dãy số, em có thể xác định được phần tử cần tìm sẽ nằm ở bên trái hay bên phải phần tử đang duyệt, từ đó quyết định tìm tiếp theo hướng nào mà không cần duyệt tất cả các phần tử của dãy số. | Phân tích bài toán tìm kiếm trên dãy số đã được sắp xếp (Mục 3.a, trang 91). |
| Thuật toán tìm kiếm nhị phân | BinarySearch | Thuật toán tìm kiếm nhị phân được áp dụng cho các dãy được sắp xếp theo thứ tự xác định. Sau mỗi bước lặp của thuật toán phạm vi tìm kiếm được thu hẹp dần. Ví dụ với dãy tăng dần, nếu giá trị cần tìm nhỏ hơn giá trị của phần tử ở giữa của dãy thì phạm vi tìm kiếm thu hẹp vào nửa đầu của dãy, ngược lại, phạm vi tìm kiếm là nửa cuối của dãy. Cứ tiếp tục như vậy cho đến khi tìm thấy hoặc phạm vi tìm kiếm bằng rỗng. | Hộp kiến thức tổng kết thuật toán tìm kiếm nhị phân trên dãy đã sắp xếp (Mục 3.c, trang 93). |

---

## Bài 20: Thực hành bài toán tìm kiếm

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Đối tượng tệp | text file | Python cho phép đọc, ghi dữ liệu với tệp văn bản (text file) rất dễ dàng. Các tệp đều được mở để đọc và ghi dưới dạng văn bản. Đối tượng tệp được tạo ra bằng lệnh `open()`. | Mở tệp văn bản để đọc (`"r"`), ghi từ đầu (`"w"`) hoặc ghi tiếp (`"a"`) trong Python (Nhiệm vụ 1.a, trang 94). |
| Đóng đối tượng tệp trong Python | — | Sau khi mở tệp thì có thể tiến hành đọc (hoặc ghi) dữ liệu. Sau khi thực hiện xong các thao tác đọc, ghi thì cần đóng đối tượng tệp bằng lệnh `f.close()`. | [mô tả] Đóng đối tượng tệp sau khi hoàn tất đọc, ghi dữ liệu (Nhiệm vụ 1.a, trang 94). |
| Các lệnh đọc dữ liệu từ tệp văn bản | — | Dữ liệu trong các tệp văn bản được lưu dưới dạng các dòng, mỗi dòng là một xâu kí tự. Sau khi mở tệp bằng lệnh `open()`, con trỏ đọc mặc định ở đầu của tệp sẵn sàng chờ lệnh đọc. | [mô tả] Sử dụng `f.readline()`, `f.readlines()`, `list(f)`, `for line in f:` để đọc tệp văn bản (Nhiệm vụ 1.b, trang 95). |
| Ghi dữ liệu ra tệp văn bản bằng lệnh print() | — | Việc ghi dữ liệu ra tệp văn bản đơn giản nhất là sử dụng lệnh `print()`. | [mô tả] Đưa dữ liệu ra tệp văn bản bằng lệnh `print()` với tham số `file` bắt buộc trong Python (Nhiệm vụ 1.c, trang 96). |

---

## Bài 21: Các thuật toán sắp xếp đơn giản

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Bài toán sắp xếp (Bài toán sắp xếp cơ bản) | — | Bài toán sắp xếp cơ bản có dạng: Cho dãy A gồm n phần tử `A[0], A[1], ..., A[n-1]`, cần xếp dãy A theo thứ tự tăng dần `A[0] ≤ A[1] ≤ ... ≤ A[n-1]`. | Đặt vấn đề về bài toán sắp xếp dãy số theo thứ tự tăng dần (Khởi động, trang 99). |
| Thuật toán sắp xếp chèn | InsertionSort(A) | Ý tưởng của thuật toán sắp xếp chèn là cho chỉ số i chạy từ 1 (phần tử thứ hai của dãy) đến n – 1 (phần tử cuối của dãy). Mỗi vòng như vậy sẽ "chèn" phần tử A[i] vào vị trí đúng của dãy con đã sắp xếp A[0], A[1],..., A[i-1]. Như vậy sau n – 1 bước lặp thì dãy được sắp xếp xong. | Mô phỏng và cài đặt hàm `InsertionSort(A)` sắp xếp dãy số (Mục 1, trang 100). |
| Thuật toán sắp xếp chọn | SelectionSort(A) | Thuật toán sắp xếp chọn thực hiện một vòng lặp với chỉ số i chạy từ 0 (phần tử đầu tiên) đến n – 2 (phần tử gần cuối). Tại mỗi bước lặp, chọn phần tử nhỏ nhất nằm trong dãy A[i], A[i+1],..., A[n-1] và đổi chỗ phần tử này với A[i]. | Mô phỏng và cài đặt hàm `SelectionSort(A)` sắp xếp dãy số (Mục 2, trang 101–102). |
| Thuật toán sắp xếp nổi bọt | BubbleSort(A) | Thuật toán sắp xếp nổi bọt thực hiện nhiều vòng lặp, kiểm tra hai phần tử cạnh nhau, nếu chúng chưa sắp xếp đúng thì đổi chỗ. Có nhiều cách thể hiện thuật toán này, nhưng cách thường dùng là sử dụng hai vòng lặp lồng nhau, vòng lặp trong thực hiện thao tác đổi chỗ hai phần tử cạnh nhau cho đến khi dãy được sắp xếp xong. | Mô phỏng và cài đặt hàm `BubbleSort(A)` sắp xếp dãy số (Mục 3, trang 102–103). |

---

## Bài 22: Thực hành bài toán sắp xếp

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Sắp xếp danh sách tăng dần bằng thuật toán sắp xếp chèn | — | Chúng ta có thể sử dụng thuật toán sắp xếp chèn đã học ở bài học trước để sắp xếp các phần tử trong danh sách số lượng mặt hàng theo thứ tự tăng dần. Bài toán này bao gồm các bước sau: Đầu tiên, chúng ta đọc số lượng các mặt hàng trong kho từ tệp văn bản; Sau đó sử dụng thuật toán sắp xếp chèn để sắp xếp số lượng các mặt hàng; Cuối cùng là in số lượng các mặt hàng đã sắp xếp ra màn hình. | [mô tả] Chương trình `quanlykho.py` sắp xếp số lượng các mặt hàng trong kho theo thứ tự tăng dần (Nhiệm vụ 1, trang 104). |
| Sắp xếp danh sách giảm dần bằng thuật toán sắp xếp chọn | — | Chúng ta có thể sử dụng thuật toán sắp xếp chọn đã học ở bài học trước để sắp xếp danh sách điểm số theo thứ tự điểm trung bình giảm dần. Do đó ở mỗi vòng lặp của thuật toán sắp xếp chọn, chúng ta phải tìm kiếm phần tử có giá trị cao nhất, thay vì tìm phần tử có giá trị bé nhất. | [mô tả] Chương trình `sapxepdiem.py` sắp xếp điểm trung bình theo thứ tự giảm dần (Nhiệm vụ 2, trang 105). |

---

## Bài 23: Kiểm thử và đánh giá chương trình

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Vai trò của kiểm thử chương trình | — | Kiểm thử sẽ giúp tăng độ tin cậy của chương trình nhưng chưa chứng minh được tính đúng của thuật toán và chương trình. | [mô tả] Hộp kiến thức về vai trò và giới hạn của các phương pháp kiểm thử chương trình (Mục 1, trang 107). |
| Bất biến vòng lặp | — | Trong khoa học máy tính, việc kiểm tra tính đúng của thuật toán đều phải chứng minh bằng lôgic toán học. Một phương pháp chứng minh thường dùng là bất biến vòng lặp. | Kiểm tra và chứng minh tính đúng của thuật toán sắp xếp chèn (Mục 2, Trao đổi 3, trang 107). |
| Chứng minh tính đúng của thuật toán | — | Tính đúng của thuật toán cần được chứng minh bằng lập luận toán học. Sử dụng các bộ dữ liệu kiểm thử có thể làm tăng độ tin cậy của chương trình nhưng chưa chứng minh được tính đúng của thuật toán. | [mô tả] Hộp kiến thức tổng kết về kiểm tra tính đúng của chương trình (Mục 2, trang 108). |
| Độ phức tạp tính toán | computational complexity | Hiệu quả hay tính tối ưu của chương trình thường được xem xét trên cơ sở đánh giá độ phức tạp tính toán (computational complexity) là lượng tài nguyên (amounts of resources) cần thiết để thực hiện chương trình. | Tiêu chí đánh giá tính hiệu quả của chương trình/thuật toán (Mục 3, trang 109). |
| Độ phức tạp thời gian | time complexity | Độ phức tạp thời gian (time complexity) được xác định là thời gian thực hiện chương trình/thuật toán. Thời gian này phụ thuộc vào khối lượng của dữ liệu cần phải lưu trữ trong quá trình thực hiện chương trình/thuật toán, đặc biệt liên quan tới các bước giải quyết một vấn đề cụ thể đưa ra trong chương trình/thuật toán. | Phân biệt hai loại độ phức tạp tính toán phổ biến nhất (Mục 3, trang 109). |
| Độ phức tạp không gian | space complexity | Độ phức tạp không gian (space complexity) được xác định là tài nguyên của máy tính trong đó có phần bộ nhớ được sử dụng để thực hiện chương trình. | Phân biệt hai loại độ phức tạp tính toán phổ biến nhất (Mục 3, trang 109). |
| Hiệu quả | efficient | Một chương trình/thuật toán là hiệu quả (efficient) nếu độ phức tạp của thuật toán này là thấp, nghĩa là tốn ít thời gian và tốn ít bộ nhớ cần thiết để thực hiện chương trình/thuật toán. | Đánh giá tính tối ưu của chương trình/thuật toán (Mục 3, trang 109). |
| perf_counter() | perf_counter() | Hàm perf_counter() đo nhịp xung CPU tại thời điểm thực hiện, đơn vị tính thời gian là giây. | Đo thời gian chạy thực tế của hàm `InsertionSort(A)` bằng thư viện `time` trong Python (Mục 3, trang 109). |

---

## Bài 24: Đánh giá độ phức tạp thời gian thuật toán

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Đơn vị thời gian (Đơn vị thời gian thực hiện chương trình) | — | Khi tính thời gian chạy chương trình, có thể coi tất cả các lệnh đơn (ví dụ lệnh gán) và các phép tính đơn (ví dụ phép tính số học, phép so sánh) có thời gian chạy như nhau, được gọi chung là một đơn vị thời gian. Cách tính này sẽ làm đơn giản hoá cách phân tích thời gian tính toán nhưng vẫn bảo đảm độ chính xác của tính toán. | Ước lượng thời gian thực hiện chương trình mà không cần cài đặt và chạy thực tế (Mục 1, trang 111). |
| Nguyên tắc khung đánh giá thời gian chạy chương trình | — | Cách đánh giá thời gian chạy chương trình được dựa trên một bộ khung các nguyên tắc dùng làm căn cứ để tính toán: các phép toán số học đơn giản, phép toán lôgic cơ bản và các lệnh đơn tính là 1 đơn vị thời gian; vòng lặp `for` hoặc `while` tính bằng tổng đơn vị thời gian thực hiện của mỗi bước lặp; lệnh `if` với nhiều trường hợp rẽ nhánh tính bằng đơn vị thời gian lớn nhất của các lệnh nhánh. | [mô tả] Bộ khung 5 nguyên tắc ước lượng thời gian thực hiện chương trình (Mục 1, trang 112). |
| Phép toán tích cực | — | Trong một chương trình, phép toán được thực hiện nhiều nhất và đóng vai trò chính khi thực hiện tính thời gian, được gọi là phép toán tích cực. | Xác định phép toán đóng vai trò chính khi phân tích thời gian chạy chương trình (Mục 1, trang 112). |
| Độ phức tạp thời gian thuật toán | — | Trong phạm vi kiến thức phổ thông có thể hiểu độ phức tạp thời gian thuật toán là khối lượng thời gian cần thiết để chạy chương trình thể hiện thuật toán. Độ phức tạp thời gian, trong trường hợp tổng quát, có thể coi là một hàm số $T(n)$, với $n$ là 1 số tự nhiên được xác định tuỳ thuộc từng bài toán cụ thể liên quan tới dữ liệu đầu vào. | Phân loại thuật toán dựa trên việc ước lượng hàm thời gian $T(n)$ (Mục 2, trang 113). |
| Kí hiệu O-lớn | big-O | Kí hiệu O-lớn (big-O) dùng để so sánh và phân tích bậc của hàm thời gian $T(n)$ khi $n$ tăng lên vô cùng. | Biểu diễn bậc tăng của hàm thời gian $T(n)$ khi kích thước dữ liệu đầu vào tiến tới vô cùng (Mục 2, trang 113). |
| Bậc O-lớn | — | Cho $f(n)$ và $g(n)$ là hai hàm có đối số tự nhiên. Ta viết $f(n) = O(g(n))$ và nói $f(n)$ có bậc O-lớn của $g(n)$ nếu tồn tại hằng số $c > 0$ và số tự nhiên $n_0 \ge 1$ sao cho với mọi $n \ge n_0$ ta có $f(n) \le c \cdot g(n)$. | Định nghĩa toán học của kí hiệu O-lớn (Mục 2, trang 113). |
| O-lớn | big-O | Kí hiệu dùng để biểu diễn độ phức tạp thời gian của thuật toán theo bậc của dữ liệu. | Giải thích thuật ngữ cuối sách (trang 113, 158) và đánh giá độ phức tạp thời gian thuật toán (Mục 2, Bài 24). |
| Các hàm chuẩn của kí hiệu O-lớn | — | Kí hiệu O-lớn dùng để đánh giá và phân loại độ phức tạp thời gian của thuật toán khi kích thước đầu vào của bài toán tăng lên vô cùng. Các thuật toán sẽ được đánh giá qua độ phức tạp của một số hàm chuẩn như: $O(1)$ – hằng số, $O(\log n)$ – logarit, $O(n)$ – tuyến tính, $O(n\log n)$ tuyến tính logarit, $O(n^2)$ – bình phương, $O(n^k)$ – đa thức, $O(a^n)$ – luỹ thừa, $O(n!)$ – giai thừa. | [mô tả] Hộp kiến thức về các lớp độ phức tạp thời gian chuẩn của thuật toán (Mục 2, trang 113). |
| Quy tắc cộng | — | $O(f(n) + g(n)) = O(\max(f(n), g(n)))$. Quy tắc này được áp dụng khi tính độ phức tạp thời gian cho hai chương trình được thực hiện nối tiếp nhau. | Quy tắc thực hành tính độ phức tạp thời gian thuật toán QT1 (Mục 3, trang 114). |
| Quy tắc nhân | — | Phép nhân với hằng số: $O(C \cdot f(n)) = O(f(n))$, với $C$ là hằng số bất kì. | Quy tắc thực hành tính độ phức tạp thời gian thuật toán QT2 gồm phép nhân với hằng số và phép nhân với hàm số (Mục 3, trang 114). |

---

## Bài 25: Thực hành xác định độ phức tạp thời gian thuật toán

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Độ phức tạp tuyến tính | — | Vậy thuật toán tìm kiếm tuần tự có độ phức tạp tuyến tính. | Xác định độ phức tạp O-lớn $T(n) = n + 1 = O(n)$ của thuật toán tìm kiếm tuần tự `LinearSearch(A, K)` (Nhiệm vụ 1, trang 115). |
| Ý tưởng của thuật toán sắp xếp chọn | — | Ý tưởng của thuật toán sắp xếp chọn là tại mỗi bước thứ $i$ của vòng lặp sẽ tìm chính xác phần tử tại vị trí thứ $i$, tức là sẽ tìm phần tử nhỏ nhất trong dãy từ $A[i], A[i + 1], \dots, A[n - 1]$ và đổi chỗ phần tử nhỏ nhất này với $A[i]$. | [mô tả] Nhắc lại ý tưởng thuật toán `SelectionSort(A)` trước khi phân tích số đơn vị thời gian (Nhiệm vụ 2, trang 116). |
| Độ phức tạp thời gian bình phương | — | Vậy thuật toán sắp xếp chọn có độ phức tạp thời gian bình phương. | Tổng hợp hàm thời gian $T(n) = n^2 + 3n - 3$ và kết luận bậc O-lớn $O(n^2)$ của thuật toán sắp xếp chọn (Nhiệm vụ 2, trang 117). |

---

## Bài 26: Phương pháp làm mịn dần trong thiết kế chương trình

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Phương pháp làm mịn dần (Phương pháp làm mịn dần trong thiết kế chương trình) | — | Phương pháp làm mịn dần trong thiết kế chương trình là quá trình chi tiết hóa từ ý tưởng của các bước trước thành những hành động cụ thể hơn ở các bước sau. Ở bước cuối cùng, các hành động tương ứng với các câu lệnh của ngôn ngữ lập trình để viết chương trình hoàn chỉnh. | Hộp kiến thức định nghĩa phương pháp thiết kế làm mịn dần qua bài toán sắp xếp chèn (Mục 1.c, trang 120). |
| Cặp phần tử nghịch đảo (Nghịch đảo) | — | Cho trước dãy số $A$: $A[0], A[1], \dots, A[n-1]$. Cặp phần tử $A[i], A[j]$ được gọi là nghịch đảo nếu $i < j$ nhưng $A[i] > A[j]$. | Bài toán đếm số các cặp nghịch đảo của dãy $A$ bằng phương pháp làm mịn dần (Mục 2, trang 120). |
| Quy trình và nguyên tắc của phương pháp làm mịn dần (Quy trình và nguyên tắc) | — | Phương pháp làm mịn dần trong thiết kế chương trình phải tuân thủ các quy trình và nguyên tắc sau: Chia việc thiết kế thành từng bước và thực hiện lần lượt các bước; Mỗi bước lớn có thể được chia thành nhiều bước nhỏ hơn để giải quyết độc lập; Tiếp cận bài toán từ tổng quan đến chi tiết, mỗi bước tiếp theo sẽ phải là thiết kế chi tiết hơn bước trước đó. Quá trình như vậy sẽ tiếp tục cho đến khi viết xong toàn bộ các câu lệnh của chương trình giải bài toán đã cho. | Hộp kiến thức tổng kết quy trình và nguyên tắc thiết kế làm mịn dần (Mục 2.c, trang 122). |

---

## Bài 27: Thực hành thiết kế chương trình theo phương pháp làm mịn dần

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Hoán vị (Bài toán kiểm tra hoán vị) | — | Cho trước một dãy $n$ số, các số được kí hiệu $A[0], A[1], \dots, A[n-1]$. Cần thiết kế chương trình kiểm tra xem dãy trên có phải là một hoán vị của dãy số $1, 2, \dots, n$ hay không. Chương trình cần thông báo kết quả là CÓ hoặc KHÔNG. | Thiết kế hàm `kt_hoanvi(A)` theo phương pháp làm mịn dần (Nhiệm vụ 1, trang 123). |
| Số lần lặp (Bài toán đếm số lần lặp) | — | Cho trước dãy số $A[0], A[1], \dots, A[n-1]$. Cần tính được mỗi giá trị của các phần tử của dãy trên được lặp lại bao nhiêu lần trong dãy đó. Kết quả cần được đưa ra dãy $B$. Như vậy dãy $B$ sẽ có ý nghĩa như sau: $B[k] =$ số lần lặp của phần tử $A[k]$ trong dãy $A$. | Thiết kế hai hàm `lap(x, A)` và `tinh_lap(A)` theo phương pháp làm mịn dần (Nhiệm vụ 2, trang 125). |
| Xâu kí tự đối xứng (Xâu kí tự được gọi là đối xứng) | — | Xâu kí tự được gọi là đối xứng nếu thay đổi thứ tự ngược lại các kí tự của xâu thì vẫn nhận được dãy ban đầu. Ví dụ xâu “abcdcba” là đối xứng, còn xâu “1011” không là đối xứng. | Bài toán kiểm tra một xâu kí tự cho trước có là đối xứng hay không (Vận dụng, Câu 2, trang 126). |

---

## Bài 28: Thiết kế chương trình theo mô đun

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Mô đun con (Mô đun con của chương trình) | — | Mỗi công việc chính được đặt ra ban đầu được viết thành một hàm riêng biệt, độc lập với nhau. Các hàm này được gọi là các mô đun con của chương trình. | Tách bài toán quản lí cửa hàng thành các hàm độc lập `NhapDL(fin)`, `Sapxep(A, B)`, `GhiDL(P, S, fout)` (Mục 1, Bước 4, trang 129). |
| Phương pháp thiết kế chương trình theo mô đun (Mô đun) | — | Phương pháp thiết kế chương trình theo mô đun sẽ tách bài toán lớn thành các bài toán nhỏ hơn, hay thành các mô đun, tương đối độc lập với nhau, sau đó tiến hành thiết kế thuật toán và chương trình cho từng mô đun con. Mỗi mô đun có thể là một số hàm hoặc thủ tục độc lập. Chương trình chính là một bản ghép nối các hàm và thủ tục con. | Hộp kiến thức định nghĩa phương pháp thiết kế chương trình theo mô đun (Mục 1, trang 129). |
| Thiết kế thuật toán và chương trình theo mô đun (Ưu điểm của thiết kế chương trình theo mô đun) | — | Thiết kế thuật toán và chương trình theo mô đun có các ưu điểm sau: Chương trình ngắn gọn, sáng sủa, dễ hiểu; Các mô đun được thiết lập một lần và sử dụng nhiều lần; Dễ dàng nâng cấp, thay đổi, chỉnh sửa mà không mất công sửa lại toàn bộ chương trình; Dễ dàng bổ sung các mô đun mới; Có thể chia sẻ trong môi trường làm việc nhóm, ví dụ phân công mỗi người một công việc độc lập. | Hộp kiến thức tổng kết lợi ích của phương pháp thiết kế theo mô đun (Mục 2, trang 130). |

---

## Bài 29: Thực hành thiết kế chương trình theo mô đun

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Mô đun nhập dữ liệu | nhapDL() | Mô đun nhập dữ liệu này được thiết lập bằng hàm nhapDL() với tham số đầu vào là tên tệp dữ liệu. Hàm sẽ trả lại hai mảng `DS` và `Diem`. Khi đọc dữ liệu từ tệp, với mỗi dòng, phần tử đầu tiên chính là mã số của vận động viên, sẽ được đưa vào mảng `DS`, dãy các giá trị còn lại chính là dãy điểm và được đưa vào mảng `Diem`. | Thiết kế mô đun đọc dữ liệu từ tệp `SeaGames.inp` (Mục b, trang 133). |
| Mô đun xử lí dữ liệu chính | diem_gk(), Xuly() | Mục đích của mô đun xử lí dữ liệu chính này là tính điểm tổng hợp cho mỗi vận động viên. | Thiết kế mô đun tính điểm tổng hợp của vận động viên gồm hai hàm `diem_gk()` và `Xuly()` (Mục c, trang 134). |
| Mô đun đưa kết quả ra | ghiDL() | Cuối cùng là mô đun đưa kết quả ra tệp đầu ra theo yêu cầu của bài toán. | Thiết kế mô đun ghi kết quả điểm tổng hợp ra tệp `ketqua.out` bằng hàm `ghiDL(fout, A, B)` (Mục d, trang 134). |

---

## Bài 30: Thiết lập thư viện cho chương trình

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Cấu trúc danh sách liên kết (Danh sách móc nối) | linked list | Cấu trúc danh sách liên kết (hay danh sách móc nối, linked list) là đối tượng có cấu trúc gần giống với mảng nhưng có liên kết không chặt chẽ như mảng. | Giới thiệu cấu trúc dữ liệu danh sách liên kết so sánh với cấu trúc mảng (Khởi động, trang 137). |
| Thư viện math trong Python (math) | math | math là một thư viện các hàm chuẩn của Python liên quan đến các tính toán toán học. Ví dụ một số hàm thường dùng của thư viện `math` là hàm tính căn bậc hai sqrt(), làm tròn xuống floor() và làm tròn lên ceil(). | Tìm hiểu một số hàm chuẩn của thư viện `math` và lệnh `import` (Mục 1.a, trang 137). |
| Thư viện chương trình | import | Thư viện chương trình là tập hợp các hàm được đặt trong các mô đun độc lập để dùng chung cho nhiều chương trình khác nhau. Các thư viện này có thể được dùng nhiều lần và có thể cập nhật, nâng cấp bất cứ lúc nào. Trong Python, lệnh import có chức năng đưa thư viện vào bộ nhớ để sẵn sàng sử dụng. | Hộp kiến thức định nghĩa thư viện chương trình và lệnh `import` (Mục 1.b, trang 138). |
| Cấu trúc Node | Node | Cấu trúc Node mô tả các phần tử độc lập của danh sách. Tối thiểu mỗi node cần có thông tin dữ liệu key (khoá) và thuộc tính next dùng để kết nối sang phần tử tiếp theo trong danh sách. | Thành phần phần tử của cấu trúc danh sách liên kết (Mục 2, trang 139). |
| Cấu trúc LL (head) | LL | Cấu trúc LL (linked list) sẽ có thông tin head (đầu) sẽ luôn chỉ vào node đầu tiên của danh sách liên kết. | Thành phần quản lí đầu danh sách của cấu trúc danh sách liên kết (Mục 2, trang 139). |
| Danh sách liên kết | LinkedList | Danh sách liên kết là cấu trúc dữ liệu bao gồm: Cấu trúc node mô tả các phần tử của danh sách. Mỗi node sẽ có dữ liệu khoá (key) là thông tin chính và thông tin next để kết nối sang phần tử tiếp theo của danh sách; Cấu trúc head là đầu của mỗi danh sách liên kết. Head luôn chỉ vào node đầu tiên của danh sách; Node cuối cùng của danh sách sẽ có thông tin `next = None` (dữ liệu rỗng). | Hộp kiến thức tổng kết về cấu trúc dữ liệu danh sách liên kết (Mục 2, trang 142). |

---

## Bài 31: Thực hành thiết lập thư viện chương trình

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
|---|---|---|---|
| Thư viện hinh_tron (Thư viện hinh_tron tính chu vi và diện tích hình tròn) | hinh_tron.py | Viết thư viện hinh_tron gồm hai hàm để tính chu vi và diện tích của hình tròn với tham số của hàm số là bán kính. Trong thư viện này, hãy sử dụng hằng số `math.pi` là giá trị của số `Pi` được định nghĩa ở thư viện `math`. | Thiết lập thư viện `hinh_tron.py` gồm hai hàm `tinhChuVi(r)` và `tinhDienTich(r)` (Nhiệm vụ 1, trang 143). |
| Điện trở tương đương (Thư viện cong_thuc_ly) | cong_thuc_ly.py | Tạo thư viện cong_thuc_ly gồm hai hàm `machSongSong(dsDienTro)` và `machNoiTiep(dsDienTro)` để tính điện trở tương đương của mạch nối tiếp và song song gồm các điện trở được cho giá trị tính theo Ohm trong mảng `dsDienTro`. | Thiết lập thư viện `cong_thuc_ly.py` tính điện trở tương đương của mạch điện (Nhiệm vụ 2, trang 144). |
| Nguyên tử khối trung bình (Thư viện cong_thuc_hoa tính nguyên tử khối trung bình) | cong_thuc_hoa.py | Định nghĩa hàm `tinhNtkTB(dsNtk, dstyLe)` trong file cong_thuc_hoa.py để tính nguyên tử khối trung bình của một nguyên tố hoá học trong đó tham số `dsNtk` là mảng giá trị các nguyên tử khối của các đồng vị và `dstyLe` là tỉ lệ phần trăm số nguyên tử của các đồng vị của nguyên tố đó. | Thiết lập thư viện `cong_thuc_hoa.py` tính nguyên tử khối trung bình của nguyên tố hoá học (Nhiệm vụ 3, trang 144). |

---

## Đã xét, không tạo mục

- in — chỉ nhắc tên: Toán tử kiểm tra phần tử thuộc danh sách trong Python đã học ở lớp 10 (Bài 17).
- for — chỉ nhắc tên: Câu lệnh lặp duyệt phần tử trong Python đã học ở lớp 10 (Bài 17, 25).
- append — chỉ nhắc tên: Phương thức bổ sung phần tử vào cuối danh sách trong Python đã học ở lớp 10 (Bài 17).
- remove — chỉ nhắc tên: Phương thức xoá một phần tử của danh sách trong Python đã học ở lớp 10 (Bài 17).
- insert — chỉ nhắc tên: Phương thức bổ sung phần tử vào vị trí bất kì của danh sách trong Python đã học ở lớp 10 (Bài 17).
- clear — chỉ nhắc tên: Phương thức xoá toàn bộ các phần tử của danh sách trong Python đã học ở lớp 10 (Bài 17).
- for .. in — chỉ nhắc tên: Cú pháp lệnh lặp duyệt danh sách trong Python đã học ở lớp 10 (Bài 17).
- Câu hỏi — tiêu đề, không phải thuật ngữ: Tiêu đề hộp câu hỏi củng cố cuối các mục trong bài học (Bài 17–30).
- ma trận — tên khác của Cấu trúc dữ liệu hai chiều: Tên gọi khác của bảng dữ liệu gồm các hàng và cột (Bài 17).
- mảng một chiều — tên khác của Dữ liệu mảng một chiều: Đã định nghĩa tại Bài 17, nhắc lại trong phần hướng dẫn thực hành (Bài 18).
- mảng hai chiều — tên khác của Cấu trúc dữ liệu hai chiều: Đã định nghĩa tại Bài 17, nhắc lại trong phần hướng dẫn thực hành (Bài 18).
- Trò chơi lật thẻ — tiêu đề, không phải thuật ngữ: Tiêu đề tình huống khởi động minh hoạ tìm kiếm trên bộ thẻ (Bài 19).
- Hoạt động 1: Bài toán tìm kiếm — tiêu đề, không phải thuật ngữ: Tiêu đề hộp hoạt động tìm hiểu bài toán tìm kiếm (Bài 19).
- Bảng 20.1. — tiêu đề, không phải thuật ngữ: Nhãn số hiệu bảng tổng hợp các lệnh đọc tệp trong Python (Bài 20).
- Ví dụ 1. — tiêu đề, không phải thuật ngữ: Nhãn dẫn nhập ví dụ đọc tệp văn bản (Bài 20).
- Ví dụ 2. — tiêu đề, không phải thuật ngữ: Nhãn dẫn nhập ví dụ ghi tệp văn bản (Bài 20).
- InsertionSort(A) — gộp vào Thuật toán sắp xếp chèn: Tên hàm Python cài đặt thuật toán sắp xếp chèn (Bài 21).
- SelectionSort(A) — gộp vào Thuật toán sắp xếp chọn: Tên hàm Python cài đặt thuật toán sắp xếp chọn (Bài 21).
- BubbleSort(A) — gộp vào Thuật toán sắp xếp nổi bọt: Tên hàm Python cài đặt thuật toán sắp xếp nổi bọt (Bài 21).
- Trao đổi 1. — tiêu đề, không phải thuật ngữ: Nhãn đoạn thảo luận kiểm thử bằng bộ dữ liệu mẫu (Bài 23).
- Trao đổi 2. — tiêu đề, không phải thuật ngữ: Nhãn đoạn thảo luận suy luận lôgic cho sắp xếp chèn (Bài 23).
- Trao đổi 3. — tiêu đề, không phải thuật ngữ: Nhãn đoạn thảo luận chứng minh bằng bất biến vòng lặp (Bài 23).
- Chương trình 1. — tiêu đề, không phải thuật ngữ: Nhãn đoạn phân tích thời gian chạy của Chương trình 1 (Bài 24).
- Chương trình 2. — tiêu đề, không phải thuật ngữ: Nhãn đoạn phân tích thời gian chạy của Chương trình 2 (Bài 24).
- QT1. — tiêu đề, không phải thuật ngữ: Kí hiệu đánh số Quy tắc cộng tính độ phức tạp thời gian (Bài 24).
- QT2. — tiêu đề, không phải thuật ngữ: Kí hiệu đánh số Quy tắc nhân tính độ phức tạp thời gian (Bài 24).
- Độ phức tạp thời gian của thuật toán tìm kiếm tuần tự — gộp vào Độ phức tạp tuyến tính: Nhãn mô tả bước tính độ phức tạp của thuật toán tìm kiếm tuần tự (Bài 25).
- Độ phức tạp thời gian của thuật toán sắp xếp chọn — gộp vào Độ phức tạp thời gian bình phương: Nhãn mô tả bước tính độ phức tạp của thuật toán sắp xếp chọn (Bài 25).
- Bài toán gốc. — tiêu đề, không phải thuật ngữ: Nhãn mở đầu mô tả bài toán sắp xếp dãy A (Bài 26).
- Bước 1. — tiêu đề, không phải thuật ngữ: Nhãn bước thiết kế trong quy trình làm mịn dần (Bài 26, 27).
- Bước 2. — tiêu đề, không phải thuật ngữ: Nhãn bước thiết kế trong quy trình làm mịn dần (Bài 26, 27).
- Bước 3. — tiêu đề, không phải thuật ngữ: Nhãn bước thiết kế trong quy trình làm mịn dần (Bài 26, 27).
- Bước 4. — tiêu đề, không phải thuật ngữ: Nhãn bước thiết kế trong quy trình làm mịn dần (Bài 26, 27).
- Bước 5. — tiêu đề, không phải thuật ngữ: Nhãn bước thiết kế trong quy trình làm mịn dần (Bài 26, 27).
- value — chỉ có trong ví dụ, bài tập: Tên biến trung gian lưu giá trị `A[i]` trong ví dụ làm mịn thuật toán sắp xếp chèn (Bài 26).
- làm mịn dần các phân tích — gộp vào Phương pháp làm mịn dần: Cụm diễn đạt quá trình chi tiết hoá các phân tích của bước trước đó (Bài 26).
- Bài toán. — tiêu đề, không phải thuật ngữ: Nhãn mở đầu bài toán đếm cặp nghịch đảo (Bài 26).
- Cặp phần tử — gộp vào Cặp phần tử nghịch đảo: Cụm từ mở đầu câu định nghĩa cặp phần tử nghịch đảo (Bài 26).
- thiết kế theo mô đun — tên khác của Phương pháp thiết kế chương trình theo mô đun: Cách gọi ngắn gọn của phương pháp thiết kế chương trình theo mô đun (Bài 28).
- Mô đun 1 — chỉ có trong ví dụ, bài tập: Nhãn công việc đọc dữ liệu từ tệp trong bài thực hành Sea Games (Bài 29).
- Mô đun 2 — chỉ có trong ví dụ, bài tập: Nhãn công việc xử lí dữ liệu trong bài thực hành Sea Games (Bài 29).
- Mô đun 3 — chỉ có trong ví dụ, bài tập: Nhãn công việc ghi dữ liệu ra tệp trong bài thực hành Sea Games (Bài 29).
- DS — chỉ có trong ví dụ, bài tập: Tên biến mảng lưu danh sách mã số vận động viên trong bài thực hành (Bài 29).
- Diem — chỉ có trong ví dụ, bài tập: Tên biến mảng lưu dãy điểm số của vận động viên trong bài thực hành (Bài 29).
- nhapDL() — gộp vào Mô đun nhập dữ liệu: Tên hàm Python của mô đun nhập dữ liệu trong bài thực hành (Bài 29).
- nhapDL(fin) — gộp vào Mô đun nhập dữ liệu: Cú pháp khai báo hàm nhập dữ liệu trong bài thực hành (Bài 29).
- diem_gk() — gộp vào Mô đun xử lí dữ liệu chính: Tên hàm tính điểm tổng hợp của một vận động viên trong bài thực hành (Bài 29).
- Xuly() — gộp vào Mô đun xử lí dữ liệu chính: Tên hàm tính điểm tổng hợp cho tất cả vận động viên trong bài thực hành (Bài 29).
- kq — chỉ có trong ví dụ, bài tập: Tên biến mảng lưu kết quả điểm tổng hợp trong bài thực hành (Bài 29).
- fout — chỉ có trong ví dụ, bài tập: Tên tham số chỉ tệp dữ liệu đầu ra của hàm `ghiDL()` (Bài 29).
- linked list — tên khác của Cấu trúc danh sách liên kết: Thuật ngữ tiếng Anh của cấu trúc danh sách liên kết (Bài 30).
- Danh sách liên kết (linked list) — gộp vào Cấu trúc danh sách liên kết: Nhãn mô tả đoạn khởi động giới thiệu danh sách liên kết (Bài 30).
- Cấu trúc Node và cấu trúc LL của danh sách liên kết — gộp vào Danh sách liên kết: Nhãn dẫn nhập hai cấu trúc dữ liệu thành phần Node và LL (Bài 30).
- sqrt() — gộp vào Thư viện math trong Python: Hàm tính căn bậc hai trong thư viện `math` (Bài 30).
- floor() — gộp vào Thư viện math trong Python: Hàm làm tròn xuống trong thư viện `math` (Bài 30).
- ceil() — gộp vào Thư viện math trong Python: Hàm làm tròn lên trong thư viện `math` (Bài 30).
- lib.py — chỉ có trong ví dụ, bài tập: Tên tệp thư viện minh hoạ trong ví dụ tự thiết lập thư viện (Bài 30).
- import — gộp vào Thư viện chương trình: Lệnh đưa thư viện vào bộ nhớ trong Python (Bài 30).
- key — gộp vào Cấu trúc Node: Thuộc tính lưu dữ liệu khoá của một phần tử trong danh sách liên kết (Bài 30).
- next — gộp vào Cấu trúc Node: Thuộc tính kết nối sang phần tử tiếp theo trong danh sách liên kết (Bài 30).
- delete_first(L) — chỉ có trong ví dụ, bài tập: Hàm xoá node đầu tiên của danh sách liên kết `L` (Bài 30).
- None — chỉ nhắc tên: Giá trị rỗng đặc biệt trong Python dùng để biểu thị cuối danh sách liên kết hoặc không tìm thấy (Bài 30).
- show(L) — chỉ có trong ví dụ, bài tập: Hàm hiển thị toàn bộ thông tin của danh sách liên kết `L` (Bài 30).
- node — tên khác của Cấu trúc Node: Cách viết thường của phần tử trong danh sách liên kết (Bài 30).
- Thư viện cong_thuc_ly tính điện trở tương đương — gộp vào Điện trở tương đương: Nhãn mô tả Nhiệm vụ 2 tạo thư viện `cong_thuc_ly` (Bài 31).
- cong_thuc_hoa.py — gộp vào Nguyên tử khối trung bình: Tên tệp thư viện chứa hàm `tinhNtkTB()` trong bài thực hành (Bài 31).

## Ghi chú nguồn cần kiểm tra

- **Bài 19 (trang 90, mục 2)**: Trong đoạn mã nguồn hàm tìm kiếm tuần tự của SGK gốc, tên hàm được in là `def LinearSeach(A,K):` (thiếu chữ `r` so với `LinearSearch`). Tầng 1 và Từ điển giữ nguyên theo đúng bản in SGK.
- **Bài 31 (trang 144, Nhiệm vụ 2)**: Trong tệp `cong_thuc_ly.py` của SGK gốc, nội dung hai hàm `machSongSong` (tính tổng `sum(dsDienTro)`) và `machNoiTiep` (tính nghịch đảo của tổng nghịch đảo) bị đặt ngược tên so với công thức vật lí nêu ở phần Hướng dẫn. Tầng 1 giữ nguyên mã nguồn theo bản in SGK.
