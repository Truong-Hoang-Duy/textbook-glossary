---
name: tu-dien-tin-hoc-11-ict-chu-de-6
description: "Từ điển thuật ngữ Tin học 11 (Định hướng Tin học ứng dụng) — Chủ đề 6. Thực hành tạo và khai thác cơ sở dữ liệu (Bài 17–24) theo SGK Kết nối tri thức với cuộc sống"
loai_hoc_lieu: tu_dien_thuat_ngu
mon: tin_hoc_thud
lop: 11
chuong: "Chủ đề 6. Thực hành tạo và khai thác cơ sở dữ liệu"
bai_so: "17-24"
nguon: "SGK Tin hoc 11 Dinh huong Tin hoc ung dung KNTT.pdf"
ngay_tao: "2026-11-21"
ngay_cap_nhat: "2026-11-21"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TIN HỌC 11 (TIN HỌC ỨNG DỤNG) — CHỦ ĐỀ 6: THỰC HÀNH TẠO VÀ KHAI THÁC CƠ SỞ DỮ LIỆU

## Quy ước sử dụng

- Thuật ngữ được trình bày theo từng bài học của Chủ đề 6. Thực hành tạo và khai thác cơ sở dữ liệu (Bài 17–24), bám sát nguyên văn SGK Tin học 11 – Định hướng Tin học ứng dụng (Kết nối tri thức với cuộc sống).
- Cột **Bối cảnh sử dụng** ghi tiền tố `[mô tả]` đối với các thuật ngữ, quy trình thực hành được SGK diễn giải trong đoạn văn nhưng không in đậm thành mục định nghĩa riêng.
- Các thuật ngữ chỉ nhắc tên trong bài và được định nghĩa ở chủ đề khác được ghi theo mẫu `Ngoài nguồn — chưa định nghĩa trong ... Xem: ...`.

## Bài 17: Quản trị cơ sở dữ liệu trên máy tính

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Quản lí dữ liệu thủ công | Manual data management | Trước khi có máy tính và giải pháp quản trị CSDL trên máy tính, việc quản lí dữ liệu thủ công là công việc rất vất vả, khó kiểm soát, đòi hỏi nhiều công sức, đặc biệt với những dữ liệu không được phép sai sót dù rất nhỏ, chẳng hạn như với ngành ngân hàng. | Bài 17, mục 1 — nêu hạn chế của quản lí dữ liệu thủ công trên sổ sách so với quản trị CSDL trên máy tính. |
| Giao dịch trực tuyến | Online transaction | Nhiều hệ QTCSDL cho phép cài đặt bổ sung các dịch vụ (phần mềm) hỗ trợ giao dịch trực tuyến trên máy tính, điện thoại di động,... mà không cần yêu cầu khách hàng phải trực tiếp tới các chi nhánh ngân hàng. | Bài 17, mục 1 — lợi ích của hệ QTCSDL trong việc triển khai dịch vụ giao dịch trực tuyến. |
| Lợi ích của việc ứng dụng CSDL trong quản lí | Benefits of database application in management | Việc ứng dụng CSDL trong quản lí đem lại nhiều lợi ích to lớn: tiện lợi, kịp thời, nhanh chóng, hạn chế sai sót,... | [mô tả] Bài 17, mục 1 — hộp kiến thức trọng tâm tổng kết lợi ích của quản trị CSDL trên máy tính. |
| MySQL (Hệ quản trị cơ sở dữ liệu MySQL) | MySQL | Các hệ QTCSDL được dùng phổ biến nhất hiện nay có thể kể tới là ORACLE, MySQL, Microsoft SQL Server,... Trong số đó chỉ có MySQL là sản phẩm mã nguồn mở miễn phí. MySQL cũng được đánh giá là gọn nhẹ, tốc độ xử lí nhanh, hỗ trợ quản lí chặt chẽ sự nhất quán dữ liệu, đảm bảo an ninh và an toàn dữ liệu, thích hợp cho cả các bài toán quản trị CSDL lớn cũng như các bài toán quản trị CSDL trên Internet. | Bài 17, mục 2 — giới thiệu hệ quản trị CSDL mã nguồn mở miễn phí MySQL. |
| Tài khoản root (root; người dùng root) | Root user / Root account | Với bản cài đặt tự động, trong quá trình cài đặt sẽ có yêu cầu nhập mật khẩu cho người dùng root (tương tự administrator của hệ điều hành Windows). Cần ghi nhớ mật khẩu này để truy xuất MySQL. | Bài 17, mục 2.a — tài khoản quản trị cao nhất mặc định khi cài đặt và truy xuất MySQL. |
| Dịch vụ hệ thống (Service) | System service | Sau khi cài đặt, MySQL sẽ hoạt động như một dịch vụ hệ thống (Service). | Bài 17, mục 2.a — phương thức hoạt động nền của MySQL sau khi cài đặt trên hệ điều hành. |
| Phần mềm khách dòng lệnh mysql.exe (mysql.exe) | MySQL command-line client (mysql.exe) | MySQL có sẵn phần mềm khách giúp người dùng có thể kết nối, làm việc với MySQL, dùng giao diện dòng lệnh, có tên là mysql.exe trong thư mục bin của thư mục MySQL. | Bài 17, mục 2.a (Hình 17.1–17.3) — công cụ khách giao diện dòng lệnh đi kèm MySQL. |
| HeidiSQL (Phần mềm HeidiSQL) | HeidiSQL | HeidiSQL là một phần mềm mã nguồn mở, miễn phí, dùng giao diện đồ hoạ, giúp kết nối, làm việc với nhiều hệ QTCSDL như MySQL, MariaDB, Microsoft SQL Server, PostgreSQL,... và có hỗ trợ tiếng Việt. | Bài 17, mục 2.b (Hình 17.4, Hình 17.5) — phần mềm khách giao diện đồ hoạ hỗ trợ quản trị CSDL. |
| Bản Portable (Portable version) | Portable version | Bản Portable là bản nén dạng zip, chỉ cần giải nén vào một thư mục và chạy tệp heidisql.exe. Bản cài đặt tự động sẽ thêm biểu tượng HeidiSQL trên màn hình nền. | Bài 17, mục 2.b — phiên bản chạy trực tiếp không cần cài đặt của phần mềm HeidiSQL. |
| Đăng nhập phiên làm việc trong HeidiSQL | Logging into a HeidiSQL session | Các ô Kiểu mạng, Library được đặt các giá trị mặc định để kết nối với các hệ QTCSDL MySQL hay MariaDB; ô Tên máy chủ / IP dùng giá trị mặc định; ô Người dùng nhập root; ô Mật khẩu nhập mật khẩu của người dùng root; ô Cổng dùng giá trị mặc định là cổng giao tiếp dành cho các hệ QTCSDL; sau đó chọn Mở để vào cửa sổ làm việc. | [mô tả] Bài 17, mục 2.b (Hình 17.4, Hình 17.5) — các thông số kết nối và đăng nhập vào hệ QTCSDL trên HeidiSQL. |

## Bài 18: Thực hành xác định cấu trúc bảng và các trường khoá

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Mô tả cấu trúc bảng và trường khoá chính | Table schema and primary key specification | Tổng kết tất cả các thông tin cần quản lí, viết ra thành dãy: Số hiệu bản thu âm (STT), tên bản nhạc, tên nhạc sĩ sáng tác, tên ca sĩ thể hiện. Từ đó hình dung về một bảng dữ liệu tên là banthuam, với các trường idBanthuam, tenBannhac, tenNhacsi, tenCasi và viết mô tả ngắn gọn ở dạng banthuam(idBanthuam, tenBannhac, tenNhacsi, tenCasi). | [mô tả] Bài 18, mục 2 — cách biểu diễn lược đồ cấu trúc bảng và kí hiệu gạch chân trường khoá chính. |
| Tổ chức lại bảng dữ liệu để hạn chế lặp lại | Reorganizing tables to reduce data duplication | Để khắc phục hạn chế dữ liệu lặp lại, cách làm tốt hơn là lập bảng casi(idCasi, tenCasi) với trường khoá là idCasi và thay tenCasi trong bảng banthuam bởi idCasi. Như vậy, idCasi trong bảng banthuam sẽ là khoá ngoài tham chiếu đến khoá chính idCasi trong bảng casi. | [mô tả] Bài 18, mục 3 (Bảng 18.2–18.7, Hình 18.1) — tách bảng và dùng khoá ngoài tham chiếu để hạn chế dư thừa dữ liệu. |
| Khoá cấm trùng lặp giá trị (Unique; khoá cấm trùng lặp) | Unique key / Unique constraint | Cặp (tenBannhac, idNhacsi) trong bảng bannhac không được trùng lặp giá trị. Cặp (idBannhac, idCasi) cũng không được trùng lặp giá trị. Để ghi nhớ điều này người ta cũng nói rằng các trường này phải đặt khoá cấm trùng lặp. | Bài 18, mục 4 — ràng buộc khoá ngăn các bản ghi có bộ giá trị trùng lặp trên trường hoặc cặp trường xác định. |
| AUTO_INCREMENT (tự động tăng giá trị) | AUTO_INCREMENT | Để đơn giản, các trường khoá chính thường có kiểu INT và tự động tăng giá trị (AUTO_INCREMENT). | Bài 18, mục 5 — thuộc tính tự động tăng giá trị số nguyên cho trường khoá chính khi thêm bản ghi mới. |
| Kiểu dữ liệu VARCHAR (VARCHAR (255)) | VARCHAR(255) | Các trường tenNhacsi, tenCasi, tenBannhac có thể chọn là xâu kí tự có độ dài tối đa 255 kí tự (VARCHAR (255)). | Bài 18, mục 5 — kiểu dữ liệu xâu kí tự độ dài thay đổi tối đa 255 kí tự cho các trường tên. |

## Bài 19: Thực hành tạo lập cơ sở dữ liệu và các bảng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Tạo lập CSDL mới trong HeidiSQL | Creating a new database in HeidiSQL | Nháy nút phải chuột ở vùng danh sách các CSDL đã có, chọn thẻ Tạo mới, chọn Cơ sở dữ liệu. Nhập mymusic, chọn OK. | [mô tả] Bài 19, mục 1 (Hình 19.1) — thao tác khởi tạo cơ sở dữ liệu mới trên giao diện HeidiSQL. |
| utf8mb4 (Unicode 4 byte) | utf8mb4 (4-byte UTF-8 Unicode encoding) | Bộ mã kí tự mặc định là Unicode 4 byte: utf8mb4, đối chiếu so sánh xâu theo utf8mb4_general_ci. | Bài 19, mục 1 — bộ mã kí tự Unicode 4 byte mặc định khi tạo CSDL mới trong MySQL/HeidiSQL. |
| utf8mb4_general_ci | utf8mb4_general_ci collation | Bộ mã kí tự mặc định là Unicode 4 byte: utf8mb4, đối chiếu so sánh xâu theo utf8mb4_general_ci. | Bài 19, mục 1 — quy tắc đối chiếu và so sánh xâu kí tự mặc định đi kèm bộ mã utf8mb4. |
| Khai báo tạo lập bảng và các trường dữ liệu | Declaring a new table and fields | Nháy nút phải chuột ở vùng danh sách các CSDL đã có, chọn thẻ Tạo mới, chọn Bảng. Nhập tên: nhacsi, chọn Thêm mới để thêm trường. Một trường với tên mặc định Column1 sẽ xuất hiện phía dưới. | [mô tả] Bài 19, mục 2.a (Hình 19.2–19.5) — thao tác tạo bảng mới và thêm các cột trường dữ liệu trong HeidiSQL. |
| Allow NULL (not NULL) | Allow NULL | Nhập Tên: idNhacsi, chọn kiểu dữ liệu INT, bỏ đánh dấu ô Allow NULL. | Bài 19, mục 2.a (Hình 19.3) — tuỳ chọn cho phép hoặc không cho phép trường nhận giá trị rỗng NULL. |
| Khai báo khoá chính trong HeidiSQL | Declaring a primary key in HeidiSQL | Nháy nút phải chuột vào dòng khai báo idNhacsi và chọn Create new index → PRIMARY. | [mô tả] Bài 19, mục 2.b (Hình 19.6) — thao tác ấn định trường làm khoá chính của bảng trên HeidiSQL. |
| Chỉnh sửa khoá chính đã khai báo nhầm | Modifying a misconfigured primary key | Để sửa khoá chính đã khai báo nhầm này, hãy nháy đúp chuột vào ô tenNhacsi ở dưới ô PRIMARY KEY ở phần trên và chọn lại idNhacsi (Hình 19.8). | [mô tả] Bài 19, mục 2.b (Hình 19.7–19.9) — thao tác đổi lại trường khoá chính trong thẻ Indexes của HeidiSQL. |

## Bài 20: Thực hành tạo lập các bảng có khoá ngoài

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Giá trị mặc định của trường khoá ngoài | Default value of a foreign key field | Các trường là khoá ngoài của bảng là các trường tham chiếu đến một trường khoá chính (k) của một bảng khác vì vậy cần được khai báo giá trị mặc định phù hợp với giá trị tương ứng của k. | [mô tả] Bài 20, mục 2 (Hình 20.4) — nguyên tắc chọn kiểu dữ liệu và giá trị mặc định cho trường sẽ làm khoá ngoài. |
| Khai báo khoá cấm trùng lặp trong HeidiSQL | Declaring a unique key in HeidiSQL | Cặp (tenBannhac, idNhacsi) không được trùng lặp giá trị nên phải khai báo khoá cấm trùng lặp. Đánh dấu hai trường này, nháy nút phải chuột vào vùng đánh dấu và chọn Create new index, chọn UNIQUE. | [mô tả] Bài 20, mục 3.b (Hình 20.6) — thao tác tạo chỉ mục UNIQUE cho cặp trường không được trùng lặp giá trị. |
| Thẻ Foreign Key (Foreign Key) | Foreign Key tab | Để khai báo khoá ngoài idNhacsi, chọn thẻ Foreign Key. | Bài 20, mục 3.c (Hình 20.7) — thẻ chức năng khai báo ràng buộc khoá ngoài cho bảng trong HeidiSQL. |
| Khai báo tham chiếu khoá ngoài trong HeidiSQL | Declaring foreign key references in HeidiSQL | Nháy chuột vào ô dưới dòng Columns và chọn trường khoá ngoài là idNhacsi rồi chọn OK. Nháy chuột vào ô phía dưới Reference table để chọn bảng tham chiếu là nhacsi và chọn OK. | [mô tả] Bài 20, mục 3.c (Hình 20.8–20.10) — các bước chọn trường khoá ngoài, bảng tham chiếu và trường tham chiếu. |
| Reference table (bảng tham chiếu) | Reference table | Nháy chuột vào ô phía dưới Reference table để chọn bảng tham chiếu là nhacsi và chọn OK. | Bài 20, mục 3.c (Hình 20.9) — thuộc tính chỉ định bảng đích chứa khoá chính được khoá ngoài tham chiếu tới. |

## Bài 21: Thực hành cập nhật và truy xuất dữ liệu các bảng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Thêm mới hàng dữ liệu trong HeidiSQL | Inserting a new row in HeidiSQL | Để thêm vào một hàng dữ liệu mới có thể nhấn phím Insert hoặc chọn biểu tượng + hay nháy nút phải chuột lên vùng dữ liệu của bảng và chọn Chèn hàng. Một hàng dữ liệu rỗng sẽ xuất hiện. Tiếp theo nháy đúp chuột vào từng ô trên hàng đó để nhập dữ liệu tương ứng cho từng trường. | [mô tả] Bài 21, mục 1 (Hình 21.1–21.3) — thao tác thêm bản ghi mới vào bảng dữ liệu trên thẻ Dữ liệu. |
| Chèn hàng | Insert row | Nháy nút phải chuột lên vùng dữ liệu của bảng và chọn Chèn hàng. Một hàng dữ liệu rỗng sẽ xuất hiện. Tiếp theo nháy đúp chuột vào từng ô trên hàng đó để nhập dữ liệu tương ứng cho từng trường. | Bài 21, mục 1 — lệnh trong bảng chọn ngữ cảnh dùng để thêm một dòng bản ghi mới vào bảng. |
| Chỉnh sửa dữ liệu bảng trong HeidiSQL | Editing table data in HeidiSQL | Em có thể nháy đúp chuột vào ô dữ liệu cần sửa và nhập lại. | [mô tả] Bài 21, mục 2 (Hình 21.4, Hình 21.5) — thao tác sửa trực tiếp giá trị ô dữ liệu bị sai sót trên lưới dữ liệu. |
| Xoá dòng dữ liệu trong HeidiSQL | Deleting data rows in HeidiSQL | Để xoá các dòng dữ liệu trong bảng nhacsi, hãy đánh dấu những dòng muốn chọn: giữ phím Shift và nháy chuột để chọn những dòng liền nhau hoặc nhấn giữ phím Ctrl và nháy chuột để chọn những dòng tách rời nhau. Nhấn tổ hợp phím Ctrl+Delete trên bàn phím hoặc chọn biểu tượng x để xoá. Phần mềm sẽ có lời nhắc yêu cầu khẳng định muốn xoá. | [mô tả] Bài 21, mục 3 (Hình 21.6, Hình 21.7) — thao tác chọn và xoá một hoặc nhiều dòng dữ liệu trong bảng. |
| Sắp xếp kết quả truy xuất trong HeidiSQL | Sorting query results in HeidiSQL | Nhìn trong danh sách dữ liệu kết xuất, có thể thấy bình thường dữ liệu được kết xuất theo thứ tự tăng dần của trường khoá chính idNhacsi. Nếu muốn kết xuất theo thứ tự giảm dần của idNhacsi, hãy nháy chuột vào ô idNhacsi. Hình tam giác màu đen sẽ xuất hiện và dữ liệu được kết xuất theo thứ tự giảm dần của idNhacsi. | [mô tả] Bài 21, mục 4.b (Hình 21.9) — thao tác sắp xếp tăng dần hoặc giảm dần theo cột trên thẻ Dữ liệu. |
| Bộ lọc nhanh (Quick Filter) | Quick Filter | Để lấy ra danh sách dữ liệu thoả mãn một yêu cầu nào đó có thể thực hiện các thao tác tạo bộ lọc: Nháy nút phải chuột vào vùng dữ liệu tenNhacsi, chọn Quick Filter, rồi chẳng hạn chọn LIKE “%...”. Nhập vào kí tự P. | Bài 21, mục 4.c (Hình 21.10–21.13) — công cụ thiết lập nhanh biểu thức lọc dữ liệu theo cột trên HeidiSQL. |
| Cấu trúc câu truy vấn SELECT một bảng | Single-table SELECT query syntax | Ngoài việc sử dụng các thao tác qua giao diện trực quan như đã hướng dẫn ở trên, cũng có thể nhập câu truy vấn SQL để truy xuất dữ liệu một cách linh hoạt hơn. Lấy ra tất cả các dòng dữ liệu, mỗi dòng là giá trị của các trường trong danh_sách_các_trường từ bảng tên_bảng ở đó các giá trị thoả mãn biểu_thức_điều_kiện, kết quả truy vấn được sắp xếp theo thứ tự tên_trường_1 ASC hoặc DESC, tên_trường_2 ASC hoặc DESC. | [mô tả] Bài 21, mục 5 (Hình 21.14) — cú pháp và ý nghĩa câu truy vấn SQL SELECT ... FROM ... WHERE ... ORDER BY trên một bảng. |
| ASC (Ascending) | ASC (Ascending) | Nghĩa là ASC hoặc DESC. ASC là viết tắt của Ascending – tăng dần, DESC là viết tắt của Descending – giảm dần. | Bài 21, mục 5 — từ khoá chỉ định thứ tự sắp xếp tăng dần trong mệnh đề ORDER BY của SQL. |
| DESC (Descending) | DESC (Descending) | Nghĩa là ASC hoặc DESC. ASC là viết tắt của Ascending – tăng dần, DESC là viết tắt của Descending – giảm dần. | Bài 21, mục 5 — từ khoá chỉ định thứ tự sắp xếp giảm dần trong mệnh đề ORDER BY của SQL. |

## Bài 22: Thực hành cập nhật bảng dữ liệu có tham chiếu

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Nhập dữ liệu cho trường khoá ngoài | Entering data for a foreign key field | Trường idNhacsi là trường khoá ngoài, đã được khai báo tham chiếu đến trường idNhacsi của bảng nhacsi, vì vậy để đảm bảo tính nhất quán, giá trị hợp lệ chỉ có thể lấy từ các giá trị của idNhacsi có trong bảng nhacsi. Nháy đúp chuột vào ô nhập trường idNhacsi và chọn tên nhạc sĩ trong hộp danh sách. | [mô tả] Bài 22, Nhiệm vụ 1.a (Hình 22.3) — cách chọn giá trị hợp lệ từ hộp danh sách tham chiếu khi nhập trường khoá ngoài. |
| Kiểm soát toàn vẹn tham chiếu khi xoá dữ liệu | Referential integrity enforcement on delete | Chú ý rằng bây giờ bảng bannhac đã có dữ liệu với trường idNhacsi tham chiếu đến trường idNhacsi của bảng nhacsi. Do vậy, ta sẽ không thể tuỳ tiện xoá các dòng của bảng nhacsi. MySQL sẽ kiểm tra và ngăn chặn việc xoá các dòng trong bảng nhacsi mà giá trị trường idNhacsi đã có trong trường idNhacsi của bảng bannhac. | [mô tả] Bài 22, Nhiệm vụ 1.d (Hình 22.5, Hình 22.6) — cơ chế ngăn chặn xoá bản ghi đang được khoá ngoài của bảng khác tham chiếu tới. |
| Giới hạn kiểm soát lỗi theo lôgic của hệ QTCSDL | Logical error checking limitations of a DBMS | Hệ QTCSDL chỉ có thể ngăn chặn được các lỗi theo lôgic đã được khai báo (ví dụ lôgic tham chiếu khoá ngoài). Nó không thể ngăn chặn được các lỗi không liên quan đến lôgic nào. Vì vậy người làm việc với CSDL luôn phải có sự cẩn thận, mẫn cán trong công việc của mình. | [mô tả] Bài 22, Nhiệm vụ 1.d (Lưu ý) — phân biệt lỗi ràng buộc lôgic với lỗi nhập sai nội dung thực tế. |
| Phím radio | Radio button | Muốn sửa một bản nhạc nào đó, nháy chuột vào phím radio trên dòng đó, thông tin của bản nhạc sẽ được hiển thị ở phần phía trên của giao diện để người dùng sửa chữa, thay đổi,... Nháy chuột chọn Nhập để lưu lại kết quả thay đổi. | Bài 22, Nhiệm vụ 2 (Hình 22.7) — nút chọn một dòng bản ghi để hiển thị và chỉnh sửa trên giao diện ứng dụng web. |
| Hộp kiểm (checkbox) | Checkbox | Muốn xoá một hay nhiều bản nhạc nào đó trong danh sách đã có: nháy chuột vào các checkbox ở đầu các dòng tương ứng và chọn Xoá. | Bài 22, Nhiệm vụ 2 (Hình 22.7) — ô đánh dấu cho phép chọn một hoặc nhiều dòng bản ghi để xoá trên giao diện ứng dụng. |
| Giao diện ứng dụng quản lí dữ liệu chuyên biệt | Specialized data management application interface | Ứng dụng Quản lí dữ liệu âm nhạc nói trên là một ứng dụng được thiết kế chuyên biệt cho bài toán quản lí dữ liệu âm nhạc, giao diện được thiết kế hướng vào những nghiệp vụ mà người quản lí thường phải làm hằng ngày (không phải là giao diện hướng vào từng bảng dữ liệu). Tất cả các chức năng nhập mới, sửa chữa, xoá, tìm kiếm được tích hợp vào một giao diện. | [mô tả] Bài 22, Nhiệm vụ 2 — đặc điểm giao diện hướng nghiệp vụ của phần mềm ứng dụng CSDL so với phần mềm quản trị CSDL. |

## Bài 23: Thực hành truy xuất dữ liệu qua liên kết các bảng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Truy vấn hai bảng qua liên kết INNER JOIN | Querying two tables via INNER JOIN | Để truy vấn hai bảng qua liên kết khoá, câu truy vấn SQL với mệnh đề JOIN có cấu trúc như sau. | [mô tả] Bài 23, Nhiệm vụ 1 (Hình 23.1) — cách kết hợp dữ liệu từ hai bảng có quan hệ khoá ngoài bằng mệnh đề INNER JOIN ... ON. |
| Mệnh đề JOIN (INNER JOIN ... ON) | JOIN clause (INNER JOIN ... ON) | Để truy vấn hai bảng qua liên kết khoá, câu truy vấn SQL với mệnh đề JOIN có cấu trúc như sau. | Bài 23, Nhiệm vụ 1 và Nhiệm vụ 2 — mệnh đề trong câu lệnh SELECT dùng để ghép nối các bảng theo điều kiện bằng nhau giữa khoá ngoài và khoá chính. |
| Đổi tên trường trùng tên khi truy vấn liên kết | Aliasing duplicate field names in join queries | Nếu muốn ở dữ liệu kết xuất có cả trường idNhacsi của bảng nhacsi nhằm có thể đối chiếu một cách tường minh cũng không khó, chỉ cần đổi tên hai trường (cùng tên) ở hai bảng để phân biệt. | [mô tả] Bài 23, Nhiệm vụ 1 (Hình 23.2) — sử dụng từ khoá as để đặt bí danh phân biệt các trường trùng tên giữa hai bảng. |
| Tô màu cú pháp (syntax coloring) | Syntax coloring / Syntax highlighting | Dùng màu sắc để trợ giúp quan sát cú pháp của câu truy vấn (syntax coloring). | Bài 23, Nhiệm vụ 1 (Lưu ý) — tính năng hiển thị màu sắc phân biệt từ khoá, tên bảng, tên trường khi soạn thảo câu truy vấn SQL trên HeidiSQL. |
| Truy vấn nhiều hơn hai bảng qua liên kết khoá ngoài | Multi-table join query via foreign keys | Để truy vấn được nhiều hơn hai bảng theo liên kết khoá ngoài, hãy lặp lại mệnh đề JOIN trong câu truy vấn SQL theo cấu trúc như sau. | [mô tả] Bài 23, Nhiệm vụ 2 — mở rộng mệnh đề INNER JOIN lặp lại để liên kết từ ba bảng dữ liệu trở lên. |

## Bài 24: Thực hành sao lưu dữ liệu

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Xuất cơ sở dữ liệu dưới dạng SQL (sao lưu CSDL) | Export database as SQL (database backup) | Nháy chuột chọn thẻ Các công cụ, chọn Xuất cơ sở dữ liệu dưới dạng SQL. | Bài 24, Nhiệm vụ 1 (Hình 24.1) — công cụ xuất cấu trúc và dữ liệu của CSDL ra tệp truy vấn SQL để sao lưu dự phòng. |
| Tuỳ chọn Drop khi sao lưu (Drop) | Drop option on SQL export | Nháy chuột để đánh dấu vào CSDL mymusic ở phía trái và đánh dấu vào các ô Drop, có nghĩa là khi phục hồi CSDL thì xoá đối tượng cũ (nếu có) trước khi tạo đối tượng mới (Create). | Bài 24, Nhiệm vụ 1 (Hình 24.2) — tuỳ chọn chèn lệnh xoá CSDL/bảng cũ trước lệnh khởi tạo mới trong tệp sao lưu SQL. |
| Tuỳ chọn Delete + insert (Delete + insert) | Delete + insert option | Ở dòng Data chọn Delete + insert để khi phục hồi thì xoá dữ liệu cũ đi (nếu có) trước khi chèn vào dữ liệu đã sao lưu. | Bài 24, Nhiệm vụ 1 (Hình 24.2) — tuỳ chọn xoá dữ liệu hiện có trong bảng trước khi chèn lại bản ghi từ tệp sao lưu. |
| Single.sql file (tệp sao lưu .sql) | Single .sql file | Tiếp theo, chọn kiểu output là 1 tệp các câu truy vấn SQL: Single.sql file. Nhập vào tên tệp sao lưu, ví dụ là C:\Temp\_mymusic.sql. | Bài 24, Nhiệm vụ 1 (Hình 24.2) — định dạng xuất toàn bộ kết quả sao lưu thành một tệp kịch bản `.sql` duy nhất. |
| Xuất tệp sao lưu SQL trong HeidiSQL | Exporting an SQL backup file in HeidiSQL | Tiếp theo, chọn kiểu output là 1 tệp các câu truy vấn SQL: Single.sql file. Nhập vào tên tệp sao lưu, ví dụ là C:\Temp\_mymusic.sql. | [mô tả] Bài 24, Nhiệm vụ 1 — bước chọn định dạng đầu ra, đặt đường dẫn tệp `.sql` và nhấn Export để hoàn tất sao lưu. |
| Sao lưu một phần CSDL | Partial database backup | Cũng có thể thực hiện sao lưu một phần CSDL (một số bảng), bằng cách chỉ chọn những bảng muốn sao lưu. | [mô tả] Bài 24, Nhiệm vụ 1 (Hình 24.2) — cách sao lưu chọn lọc một số bảng thay vì toàn bộ CSDL trên HeidiSQL. |
| Phục hồi CSDL (phục hồi; restore) | Database restore (recovery) | Sau đây là một ví dụ phục hồi mymusic trên một máy mới, chưa có CSDL mymusic. Cũng có thể xoá CSDL mymusic đang có đi để thực hành khôi phục CSDL mymusic từ tệp sao lưu _mymusic.sql. | Bài 24, Nhiệm vụ 2 (Hình 24.3–24.7) — quá trình khôi phục lại cấu trúc và dữ liệu của CSDL từ tệp sao lưu dự phòng. |
| Khôi phục CSDL từ tệp sao lưu SQL | Restoring a database from an SQL backup file | Sau đây là một ví dụ phục hồi mymusic trên một máy mới, chưa có CSDL mymusic. Cũng có thể xoá CSDL mymusic đang có đi để thực hành khôi phục CSDL mymusic từ tệp sao lưu _mymusic.sql. | [mô tả] Bài 24, Nhiệm vụ 2 — tình huống thực hành phục hồi CSDL trên máy mới hoặc sau khi CSDL cũ bị xoá/sự cố. |
| Load SQL file... (tải tệp SQL sao lưu) | Load SQL file... | Nháy chuột chọn thẻ Tập tin, chọn Load SQL file... (hoặc nhấn Ctrl+O). | Bài 24, Nhiệm vụ 2 (Hình 24.4, Hình 24.5) — chức năng nạp nội dung tệp kịch bản `.sql` đã sao lưu vào cửa sổ truy vấn của HeidiSQL. |
| Thực thi truy vấn phục hồi và làm tươi danh sách CSDL | Executing restore script and refreshing database list | Nháy chuột chọn ▶ để thực hiện truy vấn. Sau đó nhấn F5 để làm tươi lại danh sách CSDL. Khi đó CSDL mymusic đã được khởi tạo với đầy đủ các bảng như Hình 24.6, Hình 24.7. | [mô tả] Bài 24, Nhiệm vụ 2 (Hình 24.6, Hình 24.7) — bước chạy tệp truy vấn sao lưu và nhấn F5 cập nhật lại cây danh sách CSDL sau phục hồi. |

## Đã xét, không tạo mục

- Hoạt động 1: Tìm hiểu lợi ích của quản trị CSDL trên máy tính — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 17
- Câu hỏi — tiêu đề, không phải thuật ngữ: nhãn hộp câu hỏi củng cố trong Bài 17–18
- Hoạt động 2: Tìm hiểu và lựa chọn hệ QTCSDL — tiêu đề, không phải thuật ngữ: tên hoạt động trong Bài 17
- Bảng 18.1. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng ví dụ bản thu âm trong Bài 18
- Bảng 18.2. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng casi trong Bài 18
- Bảng 18.3. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng banthuam sau khi thay idCasi trong Bài 18
- Bảng 18.4. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng bannhac trong Bài 18
- Bảng 18.5. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng banthuam sau khi dùng idBannhac trong Bài 18
- Bảng 18.6. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng nhacsi trong Bài 18
- Bảng 18.7. — tiêu đề, không phải thuật ngữ: nhãn đánh số bảng bannhac sau khi dùng idNhacsi trong Bài 18

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bảng giải thích thuật ngữ trang 151 (PDF 153) — Thuật ngữ: Không có mục thuộc Chủ đề 6 — Đã đối chiếu toàn bộ Bảng giải thích thuật ngữ cuối sách (chỉ có các mục ở trang 5, 17, 69, 73, 133; không có mục nào thuộc trang 81–115 của Chủ đề 6) → Xác nhận không có mục thuật ngữ cuối sách thuộc Chủ đề 6 (2026-11-21)
2. [đóng] Bài 18 trang 87–89 (PDF 89–91) và Bài 22 trang 105 (PDF 107) — Thuật ngữ: idNhacsi, AUTO_INCREMENT — SGK in "Đỗ Nhuân" ở một số dòng bảng ví dụ và viết "Trường idNhacsi có kiểu INT, AUTO_INCREMENT" khi nhập bảng bannhac ở Bài 22 (thực chất khoá chính tự tăng của bảng bannhac là idBannhac) → Giữ nguyên văn ở Tầng 1 theo đúng bản in SGK và giải thích chuẩn xác trong ngữ cảnh từ điển Tầng 2 (2026-11-21)
