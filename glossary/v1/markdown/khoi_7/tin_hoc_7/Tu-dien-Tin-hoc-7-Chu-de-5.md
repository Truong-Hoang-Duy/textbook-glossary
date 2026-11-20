---
name: tu-dien-tin-hoc-7-chu-de-5
description: "Từ điển thuật ngữ Tin học 7 — Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính (Bài 14–16) theo SGK Kết nối tri thức với cuộc sống"
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Tin học
lop: 7
chuong: "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính"
bai_so: "Bài 14–16"
nguon: "SGK Tin học 7 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: 2026-11-20
ngay_cap_nhat: 2026-11-20
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TIN HỌC 7 — CHỦ ĐỀ 5: GIẢI QUYẾT VẤN ĐỀ VỚI SỰ TRỢ GIÚP CỦA MÁY TÍNH

## Quy ước sử dụng

- Thuật ngữ được trình bày theo từng bài học của Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính (Bài 14–16), bám sát nguyên văn SGK Tin học 7 (Kết nối tri thức với cuộc sống).
- Cột **Bối cảnh sử dụng** ghi tiền tố `[mô tả]` đối với các thuật ngữ, bài toán và quy trình mô tả thuật toán được SGK diễn giải trong đoạn văn hoặc khung ghi chú nhưng không in đậm thành mục định nghĩa riêng.

## Bài 14: Thuật toán tìm kiếm tuần tự

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Bài toán tìm kiếm (thuật toán tìm kiếm) | Search problem (Search algorithm) | Trong tình huống khởi động, công việc mà An cần làm có thể nêu thành bài toán tìm kiếm như sau: Đầu vào: danh sách khách hàng; họ tên khách hàng cần tìm. Đầu ra: địa chỉ của khách hàng cần tìm. | [mô tả] Bài 14, mục 1 (trang 71, PDF 72) — xác định đầu vào và đầu ra của bài toán tìm kiếm dữ liệu trong danh sách để thu được thông tin cần thiết một cách hiệu quả. |
| Thuật toán tìm kiếm tuần tự (tìm kiếm tuần tự) | Sequential search algorithm (Linear search) | Thuật toán tìm kiếm tuần tự thực hiện tìm lần lượt từ đầu đến cuối danh sách, chừng nào chưa tìm thấy và chưa tìm hết thì còn tìm tiếp. | Bài 14, mục 1 (trang 71–73, PDF 72–74) — định nghĩa và sơ đồ khối (Hình 14.1) của thuật toán tìm kiếm lần lượt từng phần tử từ đầu đến cuối danh sách sử dụng cấu trúc lặp với hai điều kiện dừng. |
| Mô tả thuật toán tìm kiếm tuần tự | Natural-language description of sequential search | Bước 1. Xét phần tử đầu tiên của danh sách. Bước 2. Nếu giá trị của phần tử đang xét bằng giá trị cần tìm thì chuyển sang Bước 4, nếu không thì thực hiện bước tiếp theo (Bước 3). Bước 3. Kiểm tra đã hết danh sách chưa. Nếu đã hết danh sách thì chuyển sang Bước 5, nếu chưa thì lặp lại từ Bước 2. Bước 4. Trả lời “Tìm thấy” và chỉ ra vị trí phần tử tìm được; Kết thúc. Bước 5. Trả lời “không tìm thấy”; Kết thúc. | [mô tả] Bài 14, mục 1 (trang 73, PDF 74) — 5 bước liệt kê thuật toán tìm kiếm tuần tự bằng ngôn ngữ tự nhiên. |

## Bài 15: Thuật toán tìm kiếm nhị phân

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Thuật toán tìm kiếm nhị phân (tìm kiếm nhị phân; chia đôi) | Binary search algorithm (Binary search) | Thực hiện trên danh sách đã được sắp xếp. Bắt đầu từ vị trí ở giữa danh sách. Tại mỗi bước, so sánh giá trị cần tìm với giá trị của vị trí giữa danh sách, nếu lớn hơn thì tìm trong nửa sau của danh sách, nếu nhỏ hơn thì tìm trong nửa trước của danh sách, nếu bằng thì dừng lại. Chừng nào chưa tìm thấy và chưa hết danh sách thì còn tìm tiếp. | Bài 15, mục 1 (trang 74–76, PDF 75–77) — định nghĩa và minh hoạ hoạt động thu hẹp phạm vi tìm kiếm chỉ còn một nửa tại mỗi bước lặp trên danh sách đã sắp xếp (Hình 15.1). |
| Vùng tìm kiếm | Search range (Search interval) | Trong phần mô tả sau đây, ta giả sử danh sách (dãy) đã được sắp xếp theo thứ tự từ nhỏ đến lớn và gọi vùng tìm kiếm là đoạn danh sách mà thuật toán tìm kiếm trên đó. Ban đầu, vùng tìm kiếm là toàn bộ danh sách. | [mô tả] Bài 15, mục 1 (trang 76, PDF 77) — đoạn danh sách đang được xét trong mỗi bước lặp của thuật toán tìm kiếm nhị phân, được chia thành nửa trước và nửa sau không gồm phần tử giữa (Hình 15.2). |
| Vị trí giữa của vùng tìm kiếm (vị trí giữa) | Middle position | Vị trí giữa của vùng tìm kiếm bằng phần nguyên của (vị trí đầu + vị trí cuối)/2. | [mô tả] Bài 15, mục 1 (trang 76, PDF 77) — công thức xác định vị trí phần tử ở giữa để chia vùng tìm kiếm thành hai nửa trong cả trường hợp lẻ hoặc chẵn phần tử. |
| Mô tả thuật toán tìm kiếm nhị phân | Natural-language description of binary search | Bước 1. Nếu vùng tìm kiếm không có phần tử nào thì kết luận không tìm thấy và thuật toán kết thúc. Bước 2. Xác định vị trí giữa của vùng tìm kiếm. Vị trí này chia vùng tìm kiếm thành hai nửa: nửa trước và nửa sau vị trí giữa. Bước 3. Nếu giá trị cần tìm bằng giá trị của vị trí giữa thì kết luận “giá trị cần tìm xuất hiện tại vị trí giữa” và kết thúc. Bước 4. Nếu giá trị cần tìm nhỏ hơn giá trị của vị trí giữa thì vùng tìm kiếm mới được thu hẹp lại, chỉ còn nửa trước của dãy; ngược lại vùng tìm kiếm mới được thu hẹp lại, chỉ còn nửa sau của dãy. Bước 5. Lặp lại từ Bước 1 đến Bước 4 cho đến khi tìm thấy giá trị cần tìm (Bước 3) hoặc vùng tìm kiếm không còn phần tử nào (Bước 1). | [mô tả] Bài 15, mục 1 (trang 76, PDF 77) — 5 bước liệt kê thuật toán tìm kiếm nhị phân bằng ngôn ngữ tự nhiên trên dãy đã sắp xếp tăng dần. |
| Quy ước so sánh kí tự | Character comparison convention | Trong trường hợp so sánh kí tự thì kí tự đứng trước là “nhỏ hơn” kí tự đứng sau trong bảng chữ cái. | [mô tả] Bài 15, mục 1 (trang 76, PDF 77) — quy tắc so sánh thứ tự chữ cái khi áp dụng thuật toán tìm kiếm nhị phân cho dữ liệu dạng tên hoặc từ. |
| Mối liên quan giữa sắp xếp và tìm kiếm | Relationship between sorting and searching | Sắp xếp giúp cho việc tìm kiếm được thực hiện nhanh hơn. Nhờ việc danh sách đã được sắp xếp, tại mỗi bước, thuật toán tìm kiếm nhị phân thu hẹp được phạm vi tìm kiếm chỉ còn một nửa. | [mô tả] Bài 15, mục 2 (trang 76–77, PDF 77–78) — giải thích ưu điểm về tốc độ của tìm kiếm nhị phân so với tìm kiếm tuần tự khi dữ liệu đầu vào đã được sắp xếp. |

## Bài 16: Thuật toán sắp xếp

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Bài toán sắp xếp (thuật toán sắp xếp) | Sorting problem (Sorting algorithm) | Máy tính cũng thường xuyên phải thực hiện thuật toán sắp xếp khi người sử dụng yêu cầu. Ví dụ: Sắp xếp điểm trung bình của học sinh trong lớp bằng chương trình bảng tính; Sắp xếp tên tệp trong thư mục;... Có nhiều thuật toán sắp xếp khác nhau. | [mô tả] Bài 16, mục 1 (trang 78, PDF 79) — bài toán đưa các phần tử của dãy dữ liệu về đúng thứ tự yêu cầu (tăng dần hoặc giảm dần) để hỗ trợ tra cứu, tìm kiếm dễ dàng. |
| Thuật toán sắp xếp nổi bọt (sắp xếp nổi bọt) | Bubble sort algorithm (Bubble sort) | Nổi bọt là thuật toán sắp xếp được thực hiện bằng cách hoán đổi nhiều lần các phần tử liền kề nếu giá trị của chúng không đúng thứ tự. | Bài 16, mục 1 (trang 78–80, PDF 79–81) — định nghĩa và mô phỏng các vòng lặp đưa phần tử nhỏ nhất chưa xét “nổi” dần từ cuối dãy lên đầu dãy (Hình 16.2–16.4). |
| Mô tả thuật toán sắp xếp nổi bọt | Natural-language description of bubble sort | Với phần tử đầu tiên, thực hiện một vòng lặp: so sánh hai phần tử đứng cạnh nhau theo thứ tự từ cuối dãy lên phần tử đầu tiên; nếu phần tử đứng sau nhỏ hơn phần tử đứng trước thì đổi chỗ chúng cho nhau; cuối vòng lặp nhận được dãy số với phần tử nhỏ nhất nổi lên vị trí đầu tiên. Thực hiện tương tự với phần tử thứ hai, thứ ba, thứ tư,... đến phần tử trước phần tử cuối cùng để nhận được dãy số đã được sắp xếp theo thứ tự từ nhỏ đến lớn. | [mô tả] Bài 16, mục 1 (trang 80, PDF 81) — các bước liệt kê thuật toán sắp xếp nổi bọt theo thứ tự tăng dần bằng ngôn ngữ tự nhiên. |
| Thuật toán sắp xếp chọn (sắp xếp chọn) | Selection sort algorithm (Selection sort) | Thuật toán sắp xếp chọn xét từng vị trí từ đầu đến cuối dãy, so sánh trực tiếp phần tử ở vị trí được xét với những phần tử ở phía sau nó và hoán đổi nếu chúng chưa đúng thứ tự. | Bài 16, mục 2 (trang 80–82, PDF 81–83) — định nghĩa và mô phỏng hoạt động chọn đưa phần tử nhỏ nhất trong các phần tử phía sau về từng vị trí từ đầu đến cuối dãy (Hình 16.5). |
| Mô tả thuật toán sắp xếp chọn | Natural-language description of selection sort | Với phần tử đầu tiên, thực hiện một vòng lặp: so sánh từng phần tử (kể từ phần tử thứ hai đến phần tử cuối cùng) với phần tử đầu tiên; nếu phần tử được xét nhỏ hơn phần tử đầu tiên thì hoán đổi nó với phần tử đầu tiên; cuối vòng lặp, nhận được dãy số với phần tử nhỏ nhất được đưa về vị trí đầu tiên. Thực hiện tương tự với phần tử thứ hai, thứ ba, thứ tư,... đến phần tử trước phần tử cuối cùng để nhận được dãy số đã được sắp xếp theo thứ tự từ nhỏ đến lớn. | [mô tả] Bài 16, mục 2 (trang 81, PDF 82) — các bước liệt kê thuật toán sắp xếp chọn theo thứ tự từ nhỏ đến lớn bằng ngôn ngữ tự nhiên. |
| Bài toán hoán đổi giá trị (hoán đổi giá trị hai phần tử; hoán đổi) | Swap problem (Swapping two elements) | Trong quá trình thực hiện cả hai thuật toán sắp xếp nổi bọt và sắp xếp chọn, ta đều thấy xuất hiện nhiều lần thuật toán đơn giản hơn: hoán đổi giá trị hai phần tử. Như vậy, bài toán sắp xếp đã được giải quyết dựa trên lời giải của bài toán nhỏ hơn là bài toán hoán đổi giá trị. | [mô tả] Bài 16, Khởi động và mục 3 (trang 78, 82; PDF 79, 83) — bài toán con đổi chỗ giá trị của hai phần tử thông qua phần tử trung gian (Hình 16.1), được sử dụng lặp lại trong các thuật toán sắp xếp. |
| Chia bài toán thành những bài toán nhỏ hơn (chia một bài toán thành những bài toán nhỏ hơn; chia để trị) | Problem decomposition (Divide and conquer) | Việc chia một bài toán thành những bài toán nhỏ hơn giúp việc giải bài toán đó dễ dàng hơn, đồng thời việc mô tả thuật toán dễ hiểu và dễ thực hiện hơn. | [mô tả] Bài 16, mục 3 (trang 82, PDF 83) — phương pháp giải quyết bài toán dựa trên lời giải của những bài toán nhỏ hơn (như thu hẹp vùng tìm kiếm còn một nửa trong tìm kiếm nhị phân hoặc sử dụng bài toán hoán đổi giá trị trong sắp xếp). |

## Đã xét, không tạo mục

- Hoạt động 1: Tìm địa chỉ — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 14
- Hoạt động 1: Sắp xếp và tìm kiếm — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 15
- Hoạt động 2: Trò chơi tìm số — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 15
- Hoạt động 1: Mô phỏng thuật toán sắp xếp nổi bọt — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 16
- Hoạt động 2: Sắp xếp chọn — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 16
- Câu hỏi — tiêu đề, không phải thuật ngữ: nhãn hộp câu hỏi củng cố trong Bài 14–16

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bảng giải thích thuật ngữ trang 83 (PDF 84) — Thuật ngữ: Chủ đề 5 (Bài 14–16) — Đã đối chiếu toàn bộ 10 mục trong Bảng giải thích thuật ngữ cuối sách (trang in 10–68 thuộc Chủ đề 1–4) → Không có mục nào thuộc Chủ đề 5 (trang in 71–82), toàn bộ thuật ngữ của Chủ đề 5 được trích xuất trực tiếp từ nội dung Bài 14–16 (2026-11-20)
