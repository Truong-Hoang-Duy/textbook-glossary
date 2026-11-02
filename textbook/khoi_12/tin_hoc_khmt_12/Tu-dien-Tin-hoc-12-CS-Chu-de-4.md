---
name: tu-dien-tin-hoc-12-cs-chu-de-4
description: Từ điển thuật ngữ Tin học 12 CS Chủ đề 4 — Giải quyết vấn đề với sự trợ giúp của máy tính (HTML & CSS).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Tin học
lop: 12
chuong: "Chủ đề 4. Giải quyết vấn đề với sự trợ giúp của máy tính"
bai_so: "Bài 7 – Bài 18"
nguon: "SGK Tin học 12 Định hướng Khoa học máy tính – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: "2026-11-02"
ngay_cap_nhat: "2026-11-02"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TIN HỌC 12 ĐỊNH HƯỚNG KHOA HỌC MÁY TÍNH — CHỦ ĐỀ 4: GIẢI QUYẾT VẤN ĐỀ VỚI SỰ TRỢ GIÚP CỦA MÁY TÍNH

## Quy ước sử dụng

- **Nguồn**: Chắt lọc và chuẩn hoá theo SGK *Tin học 12 Định hướng Khoa học máy tính – Kết nối tri thức với cuộc sống* (Chủ đề 4: Bài 7 – Bài 18, trang PDF 41–107) và Bảng giải thích thuật ngữ cuối sách (trang PDF 166).
- **Cột 2 (Tiếng Anh)**: Ghi thuật ngữ tiếng Anh hoặc cú pháp thẻ/thuộc tính/bộ chọn HTML & CSS tương ứng, hoặc `—` nếu không có.
- **Phân nhóm thuật ngữ**:
  - **Thuật ngữ có định nghĩa trực tiếp (`in_source`)**: Giải nghĩa bám sát câu định nghĩa có cụm từ in đậm ở Tầng 1 hoặc Bảng giải thích thuật ngữ cuối sách.
  - **Thuật ngữ mô tả (`described`)**: Cột Bối cảnh sử dụng mở đầu bằng `[mô tả] `; Giải nghĩa tổng hợp từ đoạn văn gắn nhãn `<!-- term: ... -->` ở Tầng 1.
  - **Thuật ngữ ngoài nguồn (`out_of_source`)**: Khái niệm xuất hiện trong bài học nhưng đã được định nghĩa ở các lớp/chủ đề khác, ghi theo mẫu `Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: ...`.

## Bài 7: HTML và cấu trúc trang web

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| HTML (ngôn ngữ đánh dấu siêu văn bản HTML) | Hypertext Markup Language | Viết tắt của cụm từ Hypertext Markup Language (ngôn ngữ đánh dấu siêu văn bản), là một bộ quy tắc dùng để thiết lập cấu trúc và hiển thị nội dung trang web. | Khái niệm trung tâm về ngôn ngữ tạo lập trang web (Mục 1a, trang PDF 41–42). |
| Trang html (.html; .htm) | HTML page | Trang web được thiết lập từ các tệp văn bản thường có phần mở rộng là `.html` hoặc `.htm` được gọi là trang html. | Phân biệt tệp văn bản nguồn của trang web (Mục 1a, trang PDF 41). |
| Thẻ đánh dấu HTML (thẻ HTML; tag; thẻ) | HTML tag | Các thành phần chính tạo thành ngôn ngữ đánh dấu siêu văn bản; mỗi loại thẻ có một tên riêng và có ý nghĩa nhất định dùng để định dạng và hiển thị nội dung trên trang web, được viết trong cặp dấu `<` và `>`. | Cú pháp cơ bản của ngôn ngữ HTML (Mục 1a và 1b, trang PDF 41–42). |
| Thẻ đôi (thẻ bắt đầu; thẻ kết thúc) | Paired tag (opening tag, closing tag) | Phần lớn các thẻ đều là thẻ đôi, tức là có thẻ bắt đầu (opening tag) và thẻ kết thúc (closing tag). Vị trí kết thúc thẻ có thêm dấu `/` chẳng hạn `</p>`. | Phân loại thẻ đánh dấu HTML (Mục 1b, trang PDF 42). |
| Thẻ đơn | Empty tag / Single tag | Tuy nhiên có một số loại thẻ đơn, tức là chỉ có thẻ bắt đầu. Các thẻ đơn thường có dạng `<tên thẻ>` hoặc `<tên thẻ/>`, ví dụ `<hr/>` (dòng kẻ ngang), `<br/>` (ngắt xuống dòng). | Phân loại thẻ đánh dấu HTML (Mục 1b, trang PDF 42). |
| Phần tử HTML | HTML element | Khái niệm cơ bản của trang html; thông thường, một phần tử được định nghĩa bởi thẻ bắt đầu, thẻ kết thúc và phần nội dung nằm giữa cặp thẻ này (hoặc chỉ gồm thẻ đơn). | Cấu tạo của một tệp HTML (Mục 1c, trang PDF 43). |
| Cây thông tin các phần tử HTML | DOM / HTML element tree | Cấu trúc chung của một trang web có thể hình dung như một cây thông tin các phần tử HTML có quan hệ cha con (lồng nhau), nút gốc chính là phần tử `<html>`. | Mô tả cấu trúc phân cấp của tệp HTML (Mục 2, trang PDF 44). |
| Cấu trúc cơ bản của tệp HTML | `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, `<body>`, `<meta>` | Dòng đầu tiên `<!DOCTYPE html>` thông báo cho trình duyệt biết đây là tệp có định dạng html; phần tử `<html>` là bắt buộc, là phần tử gốc và chứa tất cả các phần tử HTML còn lại của trang web (thường chứa hai phần tử con `<head>` và `<body>`); phần tử `<head>` chứa các phần tử có liên quan chung đến toàn bộ trang web như `<title>`, `<meta>`, `<style>` và `<script>`; phần tử `<body>` chứa tất cả các phần tử còn lại là thông tin của trang web. | [mô tả] Giải thích các thành phần trong cấu trúc cơ bản của một tệp HTML (Mục 2, trang PDF 44). |
| Trình duyệt web | Web browser | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: SGK Tin học 6, Chủ đề C — Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin. | Phần mềm đọc tệp văn bản nguồn HTML và hiển thị trang web trên màn hình (Mục 1, trang PDF 41). |

## Bài 8: Định dạng văn bản

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Thuộc tính | Attribute | Mọi phần tử HTML đều có thể có thuộc tính. Thuộc tính của thẻ có tác dụng bổ sung thông tin, làm rõ các điều khiển được thẻ chỉ định hoặc làm rõ cách xử lí cho thẻ chứa nó. | Cú pháp mở rộng điều khiển của thẻ HTML (Mục 1, trang PDF 48–49). |
| Thuộc tính `style` | `style` attribute | Một trong những thuộc tính được sử dụng thường xuyên nhất là thuộc tính `style`, dùng để thiết lập định dạng văn bản như chọn màu sắc, phông chữ, cỡ chữ, kiểu chữ, căn lề, tạo khung,... | Định dạng phông chữ và văn bản trực tiếp trong thẻ HTML (Mục 1 và 3b, trang PDF 49, 51). |
| Tiêu đề (thẻ dạng `<hx>`) | Heading (`<h1>`..`<h6>`) | Để định dạng tiêu đề và các tiêu đề con xuất hiện trong văn bản, ta sử dụng các thẻ dạng `<hx>` trong đó `x` nhận một trong các giá trị từ 1 đến 6, thể hiện độ quan trọng giảm dần của nội dung. | Định dạng tiêu đề văn bản trên trang web (Mục 2a, trang PDF 49–50). |
| Đoạn văn bản (cặp thẻ `<p>Nội dung</p>`) | Paragraph (`<p>`) | Cách đơn giản nhất để xác định đoạn là đặt nội dung đoạn trong cặp thẻ `<p>Nội dung</p>`. Khi gặp cặp thẻ `<p>...</p>` trình duyệt sẽ hiển thị nội dung đoạn trên dòng mới kèm với khoảng trống nhỏ trước và sau đoạn. | Định dạng đoạn văn bản trên trang web (Mục 2b, trang PDF 50). |
| Khối (phần tử `<div>`; thẻ `<span>`) | Block (`<div>`, `<span>`) | Khi cần thao tác với nhiều loại nội dung, ta có thể sử dụng phần tử `<div>` và thẻ `<span>`. Cặp thẻ `<div>...</div>` hay `<span>...</span>` tạo một khối chứa nội dung bất kì đặt ở giữa hai thẻ. Phần tử `<div>` là một khối, bắt đầu trên dòng mới, trong khi phần tử `<span>` sử dụng cho quy mô nhỏ hơn, nội dung khối hiển thị trên cùng dòng đang viết. | Nhóm và định dạng các vùng nội dung trên trang web (Mục 2b, trang PDF 50). |
| Thẻ <br> và thẻ <hr> | `<br>`, `<hr>` | Ngoài các thẻ định dạng đoạn và khối kể trên, còn có hai thẻ `<br>` và `<hr>` để xuống dòng hoặc tạo ra một đường kẻ ngang trên trang web. | [mô tả] Ngắt dòng và kẻ đường phân cách ngang trong văn bản HTML (Mục 2b, trang PDF 50). |
| Các thẻ định dạng kiểu chữ trong HTML | `<strong>`, `<b>`, `<em>`, `<i>`, `<u>`, `<mark>`, `<small>`, `<sup>`, `<sub>`, `<del>` | Một số kiểu chữ thường dùng bao gồm: đậm, nghiêng, gạch chân, đánh dấu (highlight),... Các đoạn chữ cần được thiết lập kiểu chữ và được đặt trong cặp thẻ tương ứng, cụ thể như trong Bảng 8.1. | [mô tả] Tổng hợp các thẻ HTML định dạng kiểu chữ thường dùng (Mục 3a, trang PDF 50–51). |

## Bài 9: Tạo danh sách, bảng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Danh sách | List | Danh sách trong html cho phép nhóm và liệt kê tập hợp các mục tương tự nhau thành một danh sách để hiển thị. Các dạng danh sách trong html gồm danh sách có thứ tự, danh sách không có thứ tự và danh sách mô tả. | Tổ chức dữ liệu dạng liệt kê trên trang web (Mục 1, trang PDF 54–55). |
| Danh sách có thứ tự | Ordered list (`<ol>`) | Để tạo danh sách có thứ tự, dùng cặp thẻ `<ol></ol>`. Để chọn kiểu đánh thứ tự và giá trị bắt đầu, dùng thuộc tính `type` (xác định kiểu đánh số) và `start` (xác định giá trị bắt đầu đánh số). | Liệt kê các mục theo thứ tự số hoặc chữ cái (Mục 1, trang PDF 54). |
| Danh sách không có thứ tự (không có thứ tự) | Unordered list (`<ul>`) | Để tạo danh sách không có thứ tự, dùng cặp thẻ `<ul></ul>`. Để chọn kí tự đầu dòng, ta thiết lập giá trị của đặc tính `list-style-type` trong thuộc tính `style` bằng một trong 4 giá trị `disc`, `circle`, `square` và `none`. | Liệt kê các mục dùng kí tự đầu dòng (Mục 1, trang PDF 54). |
| Danh sách mô tả | Description list (`<dl>`) | Danh sách mô tả dùng để liệt kê các mục kèm với mô tả cho từng mục. Để tạo danh sách mô tả, em dùng ba thẻ `<dl>`, `<dt>` và `<dd>`. | Liệt kê danh mục kèm giải thích chi tiết (Mục 1, trang PDF 55). |
| Phần tử bảng | Table (`<table>`) | Phần tử bảng dùng để biểu diễn dữ liệu có cấu trúc dạng bảng. Phần tử bảng được tạo bởi các thẻ chính là `<table>`, `<tr>`, `<td>` và `<th>`; trình bày bảng bằng thuộc tính `style`. | Trình bày dữ liệu dạng bảng trên trang web (Mục 2, trang PDF 56–57). |
| Thuộc tính định dạng bảng HTML | `rowspan`, `colspan`, `border`, `width`, `height` | Sử dụng thuộc tính `rowspan` (cho hàng) và `colspan` (cho cột) để gộp ô; bản chất của việc gộp ô là mở rộng một ô bằng cách thêm một số hàng hoặc một số cột tương ứng với giá trị của hai thuộc tính này. | [mô tả] Gộp hàng, gộp cột và định dạng bảng trong HTML (Mục 2, trang PDF 56–57). |

## Bài 10: Tạo liên kết

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Siêu văn bản | Hypertext | Loại văn bản mà nội dung của nó không chỉ chứa văn bản mà còn có thể chứa nhiều dạng dữ liệu khác như âm thanh, hình ảnh, video,... và đặc biệt là chứa các siêu liên kết tới siêu văn bản khác. | Khái niệm nền tảng của trang web và liên kết web (Mục 1a, trang PDF 59). |
| Siêu liên kết (liên kết) | Hyperlink | Một tham chiếu để liên kết tới siêu văn bản khác; người dùng có thể dễ dàng truy cập đến các trang web khác bằng cách nháy chuột vào một vị trí được thiết lập siêu liên kết trên màn hình. | Cơ chế kết nối các trang web trên Internet (Mục 1b, trang PDF 59). |
| URL | Uniform Resource Locator | Địa chỉ (đường dẫn) tham chiếu tới tài liệu được liên kết; thuộc tính `href` dùng để cung cấp địa chỉ của trang web hay tài nguyên được liên kết tới, có hai dạng URL chính là đường dẫn tuyệt đối và đường dẫn tương đối. | Chỉ định đích đến của siêu liên kết trong thẻ `<a>` (Mục 1c, trang PDF 59). |
| Thẻ <a> và thuộc tính href | `<a href="URL">` | Trong đó URL là địa chỉ (đường dẫn) tham chiếu tới tài liệu được liên kết. Thuộc tính `href` dùng để cung cấp địa chỉ của trang web hay tài nguyên được liên kết tới. Có hai dạng URL chính là đường dẫn tuyệt đối và đường dẫn tương đối. | [mô tả] Cú pháp thẻ `<a>` và thuộc tính `href` tạo siêu liên kết (Mục 1c, trang PDF 59). |
| Đường dẫn tuyệt đối | Absolute path / URL | Đường dẫn cung cấp một địa chỉ đầy đủ bao gồm cả giao thức (`http://` hoặc `https://`), tên miền (domain name) và tên đường dẫn chi tiết đến tài liệu cần truy cập. | Tạo liên kết tới tài nguyên ngoài trên Internet (Mục 1c, trang PDF 59). |
| Đường dẫn tương đối | Relative path | Đường dẫn mô tả cách truy cập tài liệu được liên kết từ vị trí của tài liệu hiện tại, không yêu cầu giao thức hay tên miền mà chỉ gồm tên đường dẫn tới tài liệu cần truy cập. | Tạo liên kết tới các trang và tệp trong cùng website (Mục 1c, trang PDF 60). |
| Liên kết ngoài | External link | Liên kết từ một trang web tới một trang web khác trên Internet được gọi là liên kết ngoài. Để tạo liên kết ngoài, ta sử dụng thẻ `<a>` và truyền một đường dẫn tuyệt đối cho thuộc tính `href`. | Phân loại cách tạo liên kết trong HTML (Mục 2a, trang PDF 60). |
| Liên kết trong | Internal link | Liên kết trỏ tới các trang trong website của mình được gọi là liên kết trong. Các liên kết trong thường sử dụng đường dẫn tương đối. | Phân loại cách tạo liên kết trong cùng website (Mục 2b, trang PDF 60–61). |
| Mã định danh đoạn | Fragment identifier (`#id`) | Việc thiết lập thuộc tính `id` cho thẻ HTML tại vị trí cần liên kết giống như việc cắm cờ trong tài liệu để có thể quay lại dễ dàng; để là vị trí đích, thuộc tính `id` cần được đặt tên duy nhất (chỉ xuất hiện duy nhất một lần trong toàn bộ trang web) và được gọi là mã định danh đoạn. | Liên kết tới một vị trí cụ thể trong trang web (Mục 2d, trang PDF 62). |

## Bài 11: Chèn tệp tin đa phương tiện và khung nội tuyến vào trang web

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Thẻ `<img>` | `<img>` | Thẻ `<img>` là thẻ đơn, dùng để thêm ảnh vào trang web. Khi gặp thẻ `<img>`, trình duyệt hiểu là cần đặt một hình ảnh vào đây. | Chèn hình ảnh vào trang web (Mục 1a, trang PDF 64). |
| Văn bản thay thế | Alternative text (`alt`) | Trong các thuộc tính của thẻ `<img>`, thuộc tính `src` là bắt buộc để chỉ đường dẫn tới tệp ảnh; ngoài ra, thuộc tính quan trọng khác là `alt` nên được sử dụng kèm để cung cấp văn bản thay thế khi việc hiển thị ảnh bị lỗi. Văn bản thay thế cần có tác dụng giúp người đọc hình dung ra nội dung bức ảnh. | Thuộc tính quan trọng của thẻ `<img>` (Mục 1b, trang PDF 65). |
| Thuộc tính width và height của thẻ <img> | `width`, `height` | Để thiết lập kích thước cho ảnh ta sử dụng các thuộc tính `width`, `height` cho thẻ `img`. Thuộc tính `width`, `height` cho biết kích thước chiều rộng, chiều cao ảnh hiển thị trên màn hình. | [mô tả] Thiết lập kích thước hiển thị ảnh trên trang web (Mục 1c, trang PDF 65). |
| Thẻ `<video>` (thẻ `<audio>`) | `<video>`, `<audio>` | Thẻ `<video>` và thẻ `<audio>` dùng để chèn các tệp tin video và âm thanh vào trang web. Để các trình duyệt thể hiện đúng, các tệp tin video và âm thanh nên sử dụng các định dạng phổ biến, thông dụng. | Chèn tệp đa phương tiện video và âm thanh vào trang web (Mục 2, trang PDF 66–67). |
| Thuộc tính của thẻ <video> và <audio> | `src`, `controls`, `autoplay`, `muted` | `controls` là thuộc tính boolean, không cần có giá trị, để trình duyệt hiển thị các thành phần điều khiển như nút phát/tạm dừng, điều khiển âm lượng. | [mô tả] Các thuộc tính điều khiển phát video và âm thanh trên trang web (Mục 2a, trang PDF 66). |
| Khung nội tuyến (Thẻ `<iframe>`) | Inline frame (`<iframe>`) | Khung nội tuyến là một khung nhìn chứa tài nguyên web khác trong trang web hiện tại. Để tạo khung nội tuyến, ta sử dụng thẻ `<iframe>` (viết tắt của inline frame – khung nội tuyến) để chèn một trang web hoặc một tài nguyên web vào trong một trang web khác. | Nhúng trang web hoặc tài nguyên web khác vào trang hiện tại (Mục 3, trang PDF 67–68). |
| Đồ hoạ điểm ảnh | Bitmap / Raster graphics | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: SGK Tin học 10, Chủ đề F — Giải quyết vấn đề với sự trợ giúp của máy tính (hoặc chuyên đề Thiết kế đồ hoạ). | Phân loại các định dạng tệp ảnh PNG, JPG, GIF dùng trên trang web (Mục 1, trang PDF 64). |
| Đồ hoạ vectơ | Vector graphics | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: SGK Tin học 10, Chủ đề F — Giải quyết vấn đề với sự trợ giúp của máy tính (hoặc chuyên đề Thiết kế đồ hoạ). | Phân loại định dạng tệp ảnh SVG dùng trên trang web (Mục 1, trang PDF 64). |

## Bài 12: Tạo biểu mẫu

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Biểu mẫu web (biểu mẫu) | Web form (`<form>`) | Biểu mẫu web hay phần tử `form` của HTML là một công cụ dùng để thu thập dữ liệu. Dữ liệu được người dùng nhập vào form và xử lí tại chỗ hoặc gửi về máy chủ. Ta thường xuyên gặp các biểu mẫu (form) khi đăng kí tài khoản, mua hàng, tìm kiếm thông tin. | Tạo giao diện thu thập thông tin người dùng trên trang web (Mục 1, trang PDF 69–71). |
| `label` | `<label>` | Phần tử `label` định nghĩa nhãn, có cấu trúc như sau. | Tạo nhãn mô tả cho ô nhập dữ liệu trong biểu mẫu (Mục 1, trang PDF 69). |
| `input` | `<input>` | Phần tử `input` xác định vùng nhập dữ liệu. `input` xác định bởi thẻ đơn, không cần thẻ kết thúc. | Tạo các trường nhập văn bản, mật khẩu, nút chọn, nút gửi trong biểu mẫu (Mục 1, trang PDF 69–70). |
| Các loại phần tử input thông dụng | `text`, `password`, `radio`, `checkbox`, `submit`, `button` | `text` tạo ra trường nhập văn bản; `password` tạo ra trường nhập mật khẩu, dùng để nhập văn bản nhưng bị che thông tin; `radio` tạo ra ô chọn 1 giá trị duy nhất trong các phần tử cùng tên; `checkbox` tạo ra ô lựa chọn giá trị có hoặc không; `button` tạo ra một nút bấm; `file` tạo ra nút để chọn một tệp tin và tải lên máy chủ; `submit` tạo ra nút để gửi thông tin đến máy chủ. | [mô tả] Bảng tổng hợp các giá trị thuộc tính `type` của phần tử `input` (Mục 1, trang PDF 70). |
| `select` | `<select>`, `<option>` | Phần tử `select` có tác dụng cho phép người dùng chọn một trong các lựa chọn trong danh sách thả xuống. Phần tử `select` chứa nhiều thẻ con `option`, mỗi thẻ `option` định nghĩa một lựa chọn. | Tạo danh sách thả xuống trong biểu mẫu (Mục 1, trang PDF 70–71). |
| `textarea` | `<textarea>` | Phần tử `textarea` xác định một vùng nhập văn bản có nhiều dòng và cột. Cấu trúc của phần tử `textarea` gồm thuộc tính `rows` và `cols`. | Tạo ô nhập đoạn văn bản dài trong biểu mẫu (Mục 1, trang PDF 71). |
| `fieldset` (`legend`) | `<fieldset>`, `<legend>` | Phần tử `fieldset` được dùng để nhóm các phần tử có liên quan trong biểu mẫu bằng cách vẽ một hình chữ nhật bao quanh các phần tử đặt giữa cặp thẻ `<fieldset></fieldset>`, kết hợp với thẻ con `<legend>` để mô tả tên nhóm. | Nhóm trực quan các trường thông tin liên quan trong biểu mẫu (Mục 1, trang PDF 71). |

## Bài 13: Khái niệm, vai trò của CSS

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| CSS (Cascading Style Sheet) | Cascading Style Sheets | Ngôn ngữ đặc biệt dùng để thiết lập các mẫu định dạng cho trang web. Các mẫu định dạng này được gọi là Cascading Style Sheet và viết tắt là CSS. | Ngôn ngữ định dạng trang web (Mục 1, trang PDF 74). |
| Mẫu định dạng CSS | CSS rule / Style sheet | Công cụ hỗ trợ giúp định dạng nội dung trang web nhanh hơn, thuận tiện hơn bằng cách định nghĩa một lần và sử dụng nhiều lần; ngôn ngữ định dạng CSS hoàn toàn độc lập với ngôn ngữ HTML. | Đơn vị quy tắc định dạng trong CSS (Mục 1, trang PDF 74). |
| Bộ chọn (của CSS; bộ chọn) | Selector | Thành phần chính của định dạng CSS chỉ ra phạm vi các phần tử HTML sẽ được áp dụng định dạng này. | Cấu trúc tổng quát của một mẫu định dạng CSS (Mục 2, trang PDF 74; Bảng giải thích thuật ngữ cuối sách, trang PDF 166). |
| Vùng mô tả | Declaration block | Cấu trúc tổng quát của một mẫu định dạng CSS có hai phần: bộ chọn (selector) và vùng mô tả (declaration block). Vùng mô tả bao gồm một hay nhiều quy định có dạng `{thuộc tính : giá trị ;}`, các quy định được viết cách nhau bởi dấu `;`. | Cấu trúc tổng quát của một mẫu định dạng CSS (Mục 2, trang PDF 74–75). |
| Quy tắc định dạng thuộc tính CSS | `thuộc tính : giá trị;` | Cấu trúc tổng quát của một mẫu định dạng CSS có hai phần: bộ chọn (selector) và vùng mô tả (declaration block). Vùng mô tả bao gồm một hay nhiều quy định có dạng `{thuộc tính : giá trị ;}`, các quy định được viết cách nhau bởi dấu `;`. Bộ chọn sẽ quy định những thẻ HTML nào được chọn để áp dụng định dạng này. | [mô tả] Cú pháp khai báo thuộc tính và giá trị trong vùng mô tả CSS (Mục 2, trang PDF 74). |
| CSS trong (CSS ngoài; CSS nội tuyến) | Internal CSS, External CSS, Inline CSS | Có ba cách thiết lập CSS là CSS trong (internal CSS), CSS ngoài (external CSS) và CSS nội tuyến (inline CSS). | Ba cách thiết lập CSS cho trang web (Mục 2, trang PDF 75). |

## Bài 14: Định dạng văn bản bằng CSS

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| font-family (serif; sans-serif; monospace; cursive; fantasy) | `font-family` | CSS cho phép thiết lập mẫu định dạng chọn phông sử dụng thuộc tính `font-family`. Trên máy tính có thể cài đặt nhiều phông chữ khác nhau, mỗi phông chữ có một tên riêng. Tuy nhiên, các phông chữ có thể được chia làm năm loại sau: `serif` (chữ có chân); `sans-serif` (chữ không chân); `monospace` (chữ có chiều rộng đều nhau); `cursive` (chữ viết tay); `fantasy` (chữ trừu tượng). | Định dạng loại phông chữ bằng CSS (Mục 1a, trang PDF 78–79). |
| font-size | `font-size` | Thuộc tính này sẽ thiết lập cỡ chữ. Cú pháp của mẫu định dạng như sau. | Định dạng kích thước chữ bằng CSS (Mục 1a, trang PDF 79). |
| font-style (normal; italics) | `font-style` | Thuộc tính này thiết lập kiểu chữ thường hay kiểu chữ nghiêng của văn bản. Thuộc tính này có hai giá trị là `normal` (thường) và `italics` (nghiêng). | Định dạng kiểu chữ nghiêng bằng CSS (Mục 1a, trang PDF 79). |
| font-weight (bold) | `font-weight` | Thuộc tính này thiết lập kiểu chữ đậm của văn bản. Có thể đặt độ đậm bằng các số nguyên `100`, `200`,..., `900` hoặc đặt giá trị là `normal` (bình thường), `bold` (đậm). | Định dạng độ đậm của chữ bằng CSS (Mục 1a, trang PDF 79). |
| color | `color` | Thuộc tính `color` sẽ thiết lập màu chữ. Một số giá trị màu cơ bản cho thuộc tính này như sau: `black` (đen), `white` (trắng), `purple` (tím), `blue` (xanh dương), `orange` (cam), `red` (đỏ), `green` (xanh lá cây), `yellow` (vàng). | Định dạng màu chữ bằng CSS (Mục 1b, trang PDF 80; Bài 15, trang PDF 87). |
| Đường cơ sở | Baseline | Đường cơ sở (baseline) là đường ngang mà các chữ cái đứng thẳng trên nó. | Khái niệm cơ sở khi định dạng dòng văn bản trong CSS (Mục 1c, trang PDF 80). |
| Chiều cao dòng (line-height) | `line-height` | Chiều cao dòng văn bản là khoảng cách giữa các đường cơ sở của các dòng trong cùng một đoạn văn bản. CSS sẽ mặc định coi chiều cao = `2em` và thể hiện bằng cách bổ sung khoảng cách phía trên và dưới của văn bản. Thuộc tính `line-height` dùng để thiết lập chiều cao dòng cho bộ chọn của mẫu định dạng. | Định dạng khoảng cách dòng văn bản bằng CSS (Mục 1c, trang PDF 80). |
| text-align (left; center; right; justify) | `text-align` | Thuộc tính này thiết lập căn lề cho các phần tử được chọn. Các kiểu căn hàng bao gồm: `left`, `center`, `right`, `justify`. | Định dạng căn lề văn bản bằng CSS (Mục 1c, trang PDF 80). |
| text-decoration (none; underline; overline; line-through) | `text-decoration` | Thuộc tính này thiết lập tính chất trang trí dòng văn bản bằng các đường kẻ ngang trên, dưới hay giữa dòng. Thuộc tính này có bốn giá trị thường sử dụng là `none` (mặc định, không trang trí), `underline` (đường kẻ dưới chữ), `overline` (đường kẻ phía trên chữ) và `line-through` (kẻ giữa dòng chữ). | Trang trí đường kẻ ngang cho dòng văn bản bằng CSS (Mục 1c, trang PDF 80). |
| text-indent (thụt lề treo) | `text-indent` (hanging indent) | Thuộc tính định dạng thụt lề dòng đầu tiên. Nếu giá trị lớn hơn 0 thì dòng đầu tiên thụt vào. Nếu giá trị nhỏ hơn 0 thì dòng đầu tiên lùi ra ngoài còn gọi là thụt lề treo (hanging indent). | Định dạng thụt lề dòng đầu tiên bằng CSS (Mục 1c, trang PDF 80). |
| Tính kế thừa | Inheritance in CSS | Một tính chất rất quan trọng của CSS là tính kế thừa. Nếu một mẫu CSS áp dụng cho một phần tử HTML bất kì thì nó sẽ được tự động áp dụng cho tất cả các phần tử là con, cháu của phần tử đó trong mô hình cây HTML (trừ các ngoại lệ, ví dụ các phần tử với mẫu định dạng riêng). | Nguyên tắc áp dụng CSS trên cây HTML (Mục 2a, trang PDF 81–82). |
| Bộ chọn * | Universal selector (`*`) | Kí hiệu `*` dùng trong bộ chọn sẽ có ý nghĩa là phần tử bất kì. Nếu có một mẫu định dạng chứa kí hiệu `*` thì định dạng này sẽ áp dụng cho mọi phần tử trong trang web chưa được định dạng bởi các mẫu khác của CSS (vì bộ chọn `*` có trọng số ưu tiên thấp nhất). | [mô tả] Bộ chọn áp dụng cho mọi phần tử với độ ưu tiên thấp nhất (Mục 2c, trang PDF 82). |
| !important | `!important` | Kí hiệu `!important` nếu được sử dụng trong một mẫu định dạng thì mẫu này với thuộc tính tương ứng sẽ được ưu tiên cao nhất mà không phụ thuộc vào vị trí của mẫu trong CSS. Chú ý kí hiệu `!important` cần được viết ngay sau thuộc tính cần đánh dấu ưu tiên. Chỉ thuộc tính này của bộ chọn có thứ tự ưu tiên cao nhất. | Ghi đè mức ưu tiên cao nhất trong CSS (Mục 2c, trang PDF 82–83; Bài 17, trang PDF 100). |
| Chia để trị (Kĩ thuật chia để trị; Divide and Conquer) | Divide and Conquer | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: Chuyên đề học tập Tin học 11 Định hướng Khoa học máy tính, Chủ đề 1 — Kỹ thuật thiết kế thuật toán (Kỹ thuật chia để trị). | Nội dung văn bản mẫu dùng để thực hành định dạng CSS (Mục 3, trang PDF 83). |

## Bài 15: Tạo màu cho chữ và nền

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Hệ màu RGB (RGB; #rrggbb) | RGB color model (`rgb()`, `#rrggbb`) | HTML và CSS hỗ trợ hệ màu theo mẫu RGB (R – red, G – green, B – blue). Mỗi màu là một tổ hợp gồm ba giá trị `(r, g, b)`, trong đó mỗi giá trị biểu diễn cường độ của một màu cơ bản tương ứng và nhận giá trị trong khoảng từ 0 đến 255. | Thiết lập tham số màu trong HTML và CSS (Mục 1, trang PDF 85–86). |
| Hệ màu HSL (HSL) | HSL color model (`hsl()`) | Một hệ màu khác mà HTML và CSS hỗ trợ là HSL (Hue, Saturation, Lightness). H (Hue) là vòng tròn màu với giá trị từ 0 đến 360. S (Saturation) là độ bão hoà màu với giá trị từ 0% đến 100%. L (Lightness) là độ sáng với giá trị từ 0% đến 100%. | Thiết lập màu bằng hàm `hsl(hue, saturation, lightness)` trong CSS (Mục 1, trang PDF 86). |
| background-color (border) | `background-color`, `border` | CSS hỗ trợ định dạng màu chữ bằng thuộc tính `color`, màu nền bằng thuộc tính `background-color` và màu khung viền bằng thuộc tính `border`. Các thuộc tính định dạng màu chữ và màu nền đều có tính kế thừa, riêng thuộc tính `border` không có tính kế thừa. | Định dạng màu nền và màu khung viền bằng CSS (Mục 2, trang PDF 87). |
| Bộ chọn tổ hợp trong CSS | Combinator selectors (`E F`, `E > F`, `E + F`, `E ~ F`) | Quan hệ con cháu (`E F`) áp dụng cho các phần tử F với điều kiện F là phần tử con/cháu của E, tức là E phải ở phía trên F trong cây HTML; quan hệ cha con trực tiếp (`E > F`) áp dụng cho các phần tử F với điều kiện F là phần tử con của E; quan hệ anh em liền kề (`E + F`) áp dụng cho các phần tử F là phần tử liền kề ngay sau E, E và F phải có cùng phần tử cha; quan hệ anh em (`E ~ F`) áp dụng cho các phần tử F là phần tử đứng sau, không cần liên tục với E, E và F phải có cùng phần tử cha. | [mô tả] Bốn kiểu bộ chọn tổ hợp các phần tử có quan hệ trong cây HTML (Mục 3, trang PDF 87–89). |

## Bài 16: Định dạng khung

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Phần tử khối | Block-level element | Các phần tử khối thường bắt đầu từ đầu hàng và kéo dài suốt chiều rộng của trang web. | Phân loại phần tử HTML khi định dạng khung (Mục 1, trang PDF 91–92). |
| Phần tử nội tuyến (nội tuyến) | Inline-level element | Các phần tử nội tuyến là các phần tử nhúng bên trong một phần tử khác. Các phần tử HTML đều thuộc một trong hai loại khối (block) hoặc nội tuyến (inline). | Phân loại phần tử HTML khi định dạng khung (Mục 1, trang PDF 91–92). |
| `display` (block; inline) | `display: block / inline / none` | Chúng ta có thể thay đổi loại phần tử HTML bằng thuộc tính `display`. Các giá trị của thuộc tính này bao gồm `block`, `inline`, `none` (ẩn phần tử, không hiển thị). | Chuyển đổi qua lại giữa phần tử khối và phần tử nội tuyến (Mục 1, trang PDF 92). |
| Các thuộc tính khung trong CSS | `width`, `height`, `padding`, `margin`, `border-color`, `border-width`, `border-style` | `width` là chiều rộng của khung, `height` là chiều cao của khung (chỉ áp dụng cho phần tử dạng khối); `padding` là vùng đệm (khoảng cách từ vùng văn bản đến đường viền ngoài của khung); `margin` là lề khung (khoảng cách từ đường viền ngoài của khung đến văn bản xung quanh); `border-color`, `border-width`, `border-style` là màu sắc, độ dày và kiểu đường viền khung. | [mô tả] Các thông số và thuộc tính định dạng mô hình hộp (khung) của phần tử HTML (Mục 2, trang PDF 92–93). |
| Bộ chọn lớp (class) | Class selector (`.class`) | Trong thực tế, có thể có nhu cầu định dạng cho một nhóm phần tử có cùng ý nghĩa, ví dụ các đoạn văn bản có liên quan đến một sự kiện nào đó hoặc một số đoạn văn bản quan trọng cần nhấn mạnh. Trong các trường hợp này, thiết lập bộ chọn lớp (`class`) cho các phần tử đó để có thể thiết lập định dạng chung. | Định dạng nhóm phần tử HTML theo lớp (Mục 3a, trang PDF 94–95). |
| Mã định danh `id` (ID) | `id` attribute (`#id`) | Chúng ta đã biết cách thiết lập và gắn mã định danh `id` cho từng phần tử trong tệp HTML. Mỗi phần tử chỉ có một mã định danh `id` duy nhất trong toàn bộ trang web. | Định dạng phần tử HTML duy nhất theo mã định danh (Mục 3b, trang PDF 94–95). |
| Bộ chọn mã định danh | ID selector (`#id`) | CSS cho phép thiết lập các mẫu định dạng với các phần tử có id tương ứng như sau. | [mô tả] Cú pháp bộ chọn `#id` trong CSS (Mục 3b, trang PDF 94). |
| Bộ chọn là thuộc tính | Attribute selector (`[thuộc_tính]`) | Một tính chất quan trọng khác của CSS là có thể thiết lập bộ chọn là thuộc tính. Các định dạng này sẽ được thiết lập và áp dụng cho các phần tử nếu được gắn với thuộc tính cụ thể nào đó. | Định dạng các phần tử HTML dựa theo thuộc tính của thẻ (Mục 3c, trang PDF 94–95). |

## Bài 17: Các mức ưu tiên của bộ chọn

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Lớp giả (Pseudo-class) | Pseudo-class (`:pseudo-class`) | Pseudo-class (lớp giả) là khái niệm chỉ các trạng thái đặc biệt của phần tử HTML. Các trạng thái này không cần định nghĩa và mặc định được coi như một lớp có sẵn của CSS. | Định dạng phần tử HTML theo trạng thái tương tác như `:link`, `:visited`, `:hover` (Mục 1a, trang PDF 98–99). |
| Các lớp giả :link, :visited, :hover | `:link`, `:visited`, `:hover` | `:link` là tất cả các liên kết khi chưa được kích hoạt; `:visited` là tất cả các liên kết sau khi đã được kích hoạt một lần; `:hover` là tất cả các phần tử, khi người dùng di chuyển con trỏ chuột lên đối tượng. | [mô tả] Ý nghĩa và cách dùng các lớp giả thông dụng đối với liên kết và phần tử (Mục 1a, trang PDF 98). |
| Phần tử giả (Pseudo-element) | Pseudo-element (`::pseudo-element`) | Pseudo-element (phần tử giả) là khái niệm chỉ một phần (hoặc một thành phần) của các phần tử bình thường. Các phần này có thể coi là một phần tử giả và có thể thiết lập định dạng CSS riêng. | Định dạng dòng đầu tiên, chữ cái đầu tiên hoặc vùng văn bản được chọn (Mục 1b, trang PDF 99). |
| Các phần tử giả ::first-line, ::first-letter, ::selection | `::first-line`, `::first-letter`, `::selection` | `::first-line` là dòng đầu tiên của đối tượng; `::first-letter` là kí tự đầu tiên của đối tượng; `::selection` là phần được chọn (bằng cách kéo thả chuột trên màn hình) của đối tượng. | [mô tả] Ý nghĩa các phần tử giả thường dùng trong CSS (Mục 1b, trang PDF 99). |
| Thứ tự ưu tiên | Cascading priority order | Khi có nhiều mẫu định dạng có thể áp dụng cho một phần tử HTML nào đó trên trang web, CSS sẽ áp dụng định dạng theo thứ tự ưu tiên. Trong các bài học trước, em đã biết hai quy tắc ưu tiên là tính kế thừa và quy định về thứ tự cuối cùng (cascading). | Giải quyết xung đột khi nhiều mẫu CSS cùng áp dụng cho một phần tử (Mục 2, trang PDF 100). |
| Trọng số (của định dạng CSS; trọng số) | Specificity (of CSS selector) | Thứ tự ưu tiên từ cao xuống thấp khi được chọn mẫu định dạng của CSS. | Tính điểm ưu tiên của bộ chọn CSS (Mục 2, trang PDF 100–101; Bảng giải thích thuật ngữ cuối sách, trang PDF 166). |

## Bài 18: Thực hành tổng hợp thiết kế trang web

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Bố cục trang web | Web page layout | Với bố cục như Hình 18.2, mỗi thành phần (đầu trang, nội dung chính, cuối trang, banner, slogan, ảnh/nội dung) được định nghĩa bằng một lớp riêng hoặc sử dụng chung lớp nếu cùng định dạng. | [mô tả] Phân chia các vùng thành phần của trang web và định nghĩa lớp CSS tương ứng trong dự án thực hành (Mục 2, trang PDF 105). |
| Website | Website | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: SGK Tin học 6, Chủ đề C — Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin. | Tập hợp các trang web có liên kết với nhau và dùng chung tệp định dạng `style.css` trong dự án thực hành (Mục 1, trang PDF 104). |
| Trang chủ | Homepage (`index.html`) | Ngoài nguồn — chưa định nghĩa trong Chủ đề 4 Tin học 12 Định hướng Khoa học máy tính. Xem: SGK Tin học 6, Chủ đề C — Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin. | Trang mở đầu (`index.html`) chứa thông tin chung và liên kết tới các trang thành viên của website câu lạc bộ (Mục 1 và 2, trang PDF 104–106). |

## Đã xét, không tạo mục

- trang nguồn — chỉ có trong ví dụ, bài tập: cụm từ trong câu hỏi thảo luận ở Hoạt động 1 Bài 7.
- mã nguồn — chỉ có trong ví dụ, bài tập: cụm từ trong câu hỏi thảo luận ở Hoạt động 1 Bài 7.
- Enter — chỉ nhắc tên: tên phím bàn phím trong lưu ý ở Bài 7.
- Phần mềm Notepad++ — chỉ nhắc tên: tên phần mềm soạn thảo văn bản ở Bài 7.
- Language — chỉ nhắc tên: tên mục bảng chọn trong Notepad++ ở Bài 7.
- H — chỉ nhắc tên: tên mục bảng chọn trong Notepad++ ở Bài 7.
- Phần mềm Sublime Text — chỉ nhắc tên: tên phần mềm soạn thảo văn bản ở Bài 7.
- View — chỉ nhắc tên: tên mục bảng chọn trong Sublime Text ở Bài 7.
- Syntax — chỉ nhắc tên: tên mục bảng chọn trong Sublime Text ở Bài 7.
- Run — chỉ nhắc tên: tên nút lệnh chạy thử trên trang soạn thảo trực tuyến ở Bài 7.
- Lịch sử phát triển HTML — tiêu đề, không phải thuật ngữ: tiêu đề hộp đọc thêm ở cuối Bài 7.
- Hoạt động 1: Nhận biết thuộc tính thẻ — tiêu đề, không phải thuật ngữ: tiêu đề hộp hoạt động ở Bài 8.
- Hoạt động 1: Nhận biết siêu văn bản — tiêu đề, không phải thuật ngữ: tiêu đề hộp hoạt động ở Bài 10.
- Sách điện tử — chỉ có trong ví dụ, bài tập: văn bản hiển thị trong ví dụ liên kết ở Bài 10.
- Kết nối tri thức với cuộc sống — chỉ có trong ví dụ, bài tập: văn bản hiển thị trong ví dụ liên kết ở Bài 10.
- "trở lại thư mục trên một mức" — chỉ nhắc tên: cụm từ giải nghĩa kí hiệu đường dẫn `"../"` ở Bài 10.
- Hoạt động 1: Các định dạng tệp ảnh — tiêu đề, không phải thuật ngữ: tiêu đề hộp hoạt động ở Bài 11.
- Hoạt động 3: Trao đổi và nhận xét — tiêu đề, không phải thuật ngữ: tiêu đề hộp hoạt động ở Bài 11.
- 1. — tiêu đề, không phải thuật ngữ: số thứ tự câu hỏi trong các hộp hoạt động và câu hỏi củng cố ở Bài 13, 14, 15.
- 2. — tiêu đề, không phải thuật ngữ: số thứ tự câu hỏi trong các hộp hoạt động và câu hỏi củng cố ở Bài 13, 14, 15.
- 3. — tiêu đề, không phải thuật ngữ: số thứ tự câu hỏi trong hộp câu hỏi củng cố ở Bài 15.
- Lịch sử CSS — tiêu đề, không phải thuật ngữ: tiêu đề hộp đọc thêm ở cuối Bài 13.
- Lịch sử các phiên bản CSS đầu tiên — tiêu đề, không phải thuật ngữ: tiêu đề mục nhỏ trong hộp đọc thêm ở Bài 13.
- Các phiên bản CSS tiếp theo — tiêu đề, không phải thuật ngữ: tiêu đề mục nhỏ trong hộp đọc thêm ở Bài 13.
- cm — gộp vào font-size: đơn vị đo tuyệt đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- mm — gộp vào font-size: đơn vị đo tuyệt đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- in — gộp vào font-size: đơn vị đo tuyệt đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- px — gộp vào font-size: đơn vị đo tuyệt đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- pt — gộp vào font-size: đơn vị đo tuyệt đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- em — gộp vào font-size: đơn vị đo tương đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- ex — gộp vào font-size: đơn vị đo tương đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- rem — gộp vào font-size: đơn vị đo tương đối liệt kê trong thuộc tính `font-size` ở Bài 14.
- xx-small — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- x-small — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- small — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- medium — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- large — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- x-large — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- xx-large — gộp vào font-size: giá trị cỡ chữ thông dụng của `font-size` ở Bài 14.
- 100 — gộp vào font-weight: giá trị độ đậm của thuộc tính `font-weight` ở Bài 14.
- 200 — gộp vào font-weight: giá trị độ đậm của thuộc tính `font-weight` ở Bài 14.
- 900 — gộp vào font-weight: giá trị độ đậm của thuộc tính `font-weight` ở Bài 14.
- black — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- white — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- purple — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- blue — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- orange — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- red — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- green — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- yellow — gộp vào color: tên màu cơ bản trong thuộc tính `color` ở Bài 14.
- 2em — gộp vào Chiều cao dòng (line-height): giá trị mặc định của chiều cao dòng ở Bài 14.
- Ý tưởng của kĩ thuật chia để trị — tiêu đề, không phải thuật ngữ: tiêu đề đoạn văn bản mẫu trong Hình 14.8 ở Bài 14.
- font-variant — chỉ có trong ví dụ, bài tập: thuộc tính nêu trong phần Vận dụng ở Bài 14.
- letter-space — chỉ có trong ví dụ, bài tập: thuộc tính nêu trong phần Vận dụng ở Bài 14.
- word-space — chỉ có trong ví dụ, bài tập: thuộc tính nêu trong phần Vận dụng ở Bài 14.
- text-shadow — chỉ có trong ví dụ, bài tập: thuộc tính nêu trong phần Vận dụng ở Bài 14.
- rgb(x-red, x-green, x-blue) — gộp vào Hệ màu RGB (RGB; #rrggbb): cú pháp hàm thiết lập màu RGB ở Bài 15.
- rgb(x-red%, x-green%, x-blue%) — gộp vào Hệ màu RGB (RGB; #rrggbb): cú pháp hàm thiết lập màu RGB theo tỉ lệ phần trăm ở Bài 15.
- rgb(x,x,x) — gộp vào Hệ màu RGB (RGB; #rrggbb): cú pháp thiết lập màu xám trong hệ màu RGB ở Bài 15.
- hsl(h,0%,x%) — gộp vào Hệ màu HSL (HSL): cú pháp thiết lập màu xám trong hệ màu HSL ở Bài 15.
- E F — gộp vào Bộ chọn tổ hợp trong CSS: bộ chọn quan hệ con cháu ở Bài 15.
- E > F — gộp vào Bộ chọn tổ hợp trong CSS: bộ chọn quan hệ cha con trực tiếp ở Bài 15.
- E + F — gộp vào Bộ chọn tổ hợp trong CSS: bộ chọn quan hệ anh em liền kề ở Bài 15.
- E ~ F — gộp vào Bộ chọn tổ hợp trong CSS: bộ chọn quan hệ anh em ở Bài 15.
- LỢI ÍCH CỦA CSS — tiêu đề, không phải thuật ngữ: tiêu đề hộp đọc thêm ở cuối Bài 15.
- Trình bày chính xác. — tiêu đề, không phải thuật ngữ: ý tóm tắt trong hộp đọc thêm ở Bài 15.
- chính xác — chỉ nhắc tên: từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- máy in — chỉ nhắc tên: từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- Tiết kiệm công sức đáng kể. — tiêu đề, không phải thuật ngữ: ý tóm tắt trong hộp đọc thêm ở Bài 15.
- cả một website — chỉ nhắc tên: cụm từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- một tệp — chỉ nhắc tên: cụm từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- Điều khiển hiển thị đa dạng. — tiêu đề, không phải thuật ngữ: ý tóm tắt trong hộp đọc thêm ở Bài 15.
- máy tính màn hình lớn — chỉ nhắc tên: cụm từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- thiết bị di động — chỉ nhắc tên: cụm từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- theo ngữ nghĩa ngôn ngữ — chỉ nhắc tên: cụm từ nhấn mạnh trong hộp đọc thêm ở Bài 15.
- gì? — chỉ có trong ví dụ, bài tập: từ cuối câu hỏi thảo luận ở Bài 16.
- span — gộp vào Khối (phần tử `<div>`; thẻ `<span>`): tên thẻ `span` trong ví dụ thuộc tính `display` ở Bài 16.
- CSS là gì — chỉ có trong ví dụ, bài tập: tiêu đề trong nội dung trang web thực hành ở Bài 17.
- Giới thiệu HTML và CSS — chỉ có trong ví dụ, bài tập: tiêu đề trong nội dung trang web thực hành ở Bài 17.
- HTML là gì — chỉ có trong ví dụ, bài tập: tiêu đề trong nội dung trang web thực hành ở Bài 17.
- Hoạt động: Thảo luận theo nhóm — tiêu đề, không phải thuật ngữ: tiêu đề hộp hoạt động ở Bài 18.

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bài 13, trang PDF 166 — Thuật ngữ: Bộ chọn (của CSS) — Bảng giải thích thuật ngữ cuối sách ghi số trang tham chiếu là "(trang 72)" tương ứng trang in 72 (trang PDF 74) của Bài 13 → Đã đối chiếu ảnh trang PDF 74 và tích hợp đầy đủ vào mục Bài 13 (2026-11-02)
2. [đóng] Bài 14, trang PDF 80 — Thuật ngữ: text-align — Trong đoạn mã ví dụ của mục `text-align`, SGK in nhầm tên thuộc tính thành `p {line-align: right;}` thay vì `text-align` → Đã đối chiếu ảnh trang PDF 80, giữ nguyên văn đoạn mã trong Tầng 1 và chuẩn hoá tên thuộc tính `text-align` ở Tầng 2 (2026-11-02)
