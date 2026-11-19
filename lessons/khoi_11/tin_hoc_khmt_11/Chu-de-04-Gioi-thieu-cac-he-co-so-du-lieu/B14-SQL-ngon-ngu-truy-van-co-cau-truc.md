---
unit: tin_hoc_khmt_11
lesson_id: b14
toc_path:
  - "Chủ đề 4. Giới thiệu các hệ cơ sở dữ liệu"
  - "Bài 14. SQL - ngôn ngữ truy vấn có cấu trúc"
source_file: "SGK TIN HOC 11 CS - KNTT.pdf"
pdf_pages: [70, 73]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:70 -->

# BÀI 14: SQL - NGÔN NGỮ TRUY VẤN CÓ CẤU TRÚC

## 🎯 Sau bài học này em sẽ:

- Hiểu được ở mức nguyên lí: CSDL và các bảng được tạo lập, được thêm mới, cập nhật và truy xuất dữ liệu qua SQL.

## 🔴 Khởi động

> Ở bài trước các em đã biết hệ QTCSDL với vai trò là một bộ phần mềm hỗ trợ khởi tạo, cập nhật, truy xuất CSDL để người dùng có thể cập nhật, truy xuất CSDL. Ngày nay người ta thực hiện công việc đó chủ yếu thông qua ngôn ngữ truy vấn có cấu trúc SQL. Sự khác biệt của việc sử dụng SQL so với việc truy xuất dữ liệu bằng ngôn ngữ lập trình là gì?

## 1. LỢI ÍCH CỦA NGÔN NGỮ TRUY VẤN

> **Hoạt động 1: Thảo luận về hai cách truy xuất dữ liệu**
>
> Để lấy danh sách các bản nhạc do nhạc sĩ Văn Cao (mã định danh Aid = 1), sáng tác trong bảng dữ liệu Bản nhạc, ta có thể thực hiện theo một trong hai cách sau:
>
> – Dùng một ngôn ngữ lập trình, viết chương trình mở tệp chứa bảng dữ liệu Bản nhạc, rồi lần lượt lấy ra từng nhóm dữ liệu liên quan đến từng bản nhạc, sau đó tách phần Aid để kiểm tra, nếu Aid = 1 thì đưa ra tên bản nhạc (TenBN).
>
> – Dùng ngôn ngữ truy vấn, viết “CHỌN TenBN TỪ Bản nhạc VỚI Aid = 1” rồi gửi cho hệ QTCSDL thực hiện.
>
> Sự khác biệt cơ bản trong cách truy vấn nhờ ngôn ngữ truy vấn so với lập trình trực tiếp theo em là gì?

Với cách thực hiện thứ nhất trong Hoạt động 1, người dùng phải biết rõ cấu trúc tệp dữ liệu, từ đó lập trình lấy ra đoạn dữ liệu liên quan tới từng bản nhạc để xử lí. Việc làm này rất mất công sức, lại dễ nhầm lẫn. Đây là kiểu lập trình “theo thủ tục” vì phải biết rõ thủ tục truy cập dữ liệu để xây dựng thuật toán. Hơn thế nữa, ở một bài toán khác có nội dung tương tự, ví dụ lập danh sách các học sinh có điểm trung bình môn Toán trên 8 lại phải viết lại chương trình với một thủ tục tương tự.

Với cách thực hiện thứ hai trong Hoạt động 1, người dùng chỉ cần viết ra yêu cầu dưới dạng một **câu truy vấn** – muốn làm gì, chứ không phải nghĩ cách để thực hiện yêu cầu ấy. Mọi việc còn lại sẽ do hệ QTCSDL giải quyết: tiếp nhận yêu cầu ở dạng xâu truy vấn rồi lấy ra kết quả theo đúng yêu cầu.

**Ngôn ngữ truy vấn** định chuẩn cho việc định nghĩa, cập nhật, truy xuất và điều khiển dữ liệu từ các CSDL quan hệ là **SQL** (Structured Query Language) được xây dựng từ những năm 1970. SQL đã trở thành ngôn ngữ truy vấn tiêu chuẩn mà hầu hết các hệ QTCSDL đều sử dụng. Điều đó có nghĩa là chúng ta có thể dùng SQL để thao tác trên hầu hết các hệ QTCSDL phổ biến như Oracle, SQL server, MySQL, PostGreSQL,... SQL có ba thành phần là **DDL** (Data Definition Language – **ngôn ngữ định nghĩa dữ liệu**), **DML** (Data Manipulation Language – **ngôn ngữ thao tác dữ liệu**) và **DCL** (Data Control Language – **ngôn ngữ kiểm soát dữ liệu**).

<!-- pdf:71 -->

Chúng ta sẽ sử dụng SQL để minh hoạ cách thức quản trị CSDL.

## 2. KHỞI TẠO CSDL

<!-- term: Khởi tạo CSDL bằng DDL -->
Thành phần DDL của SQL cung cấp các câu truy vấn khởi tạo CSDL, khởi tạo bảng, thiết lập các khoá, tóm tắt trong các bảng sau.

**Bảng 14.1.** *Các câu truy vấn CSDL*

| Câu truy vấn DDL | Ý nghĩa |
| :--- | :--- |
| `CREATE DATABASE` | Khởi tạo CSDL |
| `CREATE TABLE` | Khởi tạo bảng |
| `ALTER TABLE` | Thay đổi định nghĩa bảng |
| `PRIMARY KEY` | Khai báo khoá chính |
| `FOREIGN KEY... REFERENCES...` | Khai báo khoá ngoài |

<!-- term: Các kiểu dữ liệu trong SQL -->
Các kiểu dữ liệu được sử dụng cho các thuộc tính của các bảng trong SQL.

**Bảng 14.2.** *Kiểu dữ liệu*

| Kiểu dữ liệu | Ý nghĩa |
| :--- | :--- |
| `CHAR (n)` hay `CHARACTER (n)` | Xâu kí tự có độ dài cố định n kí tự, nếu xâu có ít hơn n kí tự, các kí tự trống được thêm vào phía bên phải |
| `VARCHAR (n)` | Xâu kí tự có độ dài thay đổi, không vượt quá n kí tự |
| `BOOLEAN` | Kiểu lôgic có giá trị Đúng (1) hay Sai (0) |
| `INT` hay `INTEGER` | Số nguyên |
| `REAL` | Số thực dấu phẩy động |
| `DATE` | Ngày tháng, dạng `'YYYY-MM-DD'` |
| `TIME` | Thời gian, dạng `'HH:MM:SS'` |

Ví dụ: Khởi tạo CSDL âm nhạc, đặt tên là music và khởi tạo các bảng Nhạc sĩ, Bản nhạc có tên tương ứng là nhacsi và bannhac.

```sql
CREATE DATABASE music; -- Khởi tạo CSDL music

CREATE TABLE bannhac ( -- Khởi tạo bảng bannhac
    Mid CHAR(4),
    Aid INT,
    TenBN VARCHAR (128)
);
ALTER TABLE bannhac ADD PRIMARY KEY (Mid); -- Thêm khoá chính Mid cho bảng bannhac

CREATE TABLE nhacsi ( -- Khởi tạo bảng nhacsi
    Aid INT,
    TenNS VARCHAR (64)
); -- Các dấu chấm phẩy ";" được dùng để kết thúc câu truy vấn
```

<!-- pdf:72 -->

> ❓ **Câu hỏi**
>
> 1. Hãy viết câu truy vấn tạo bảng Ca sĩ như đã mô tả trong Bài 11 với tên bảng là casi.
> 2. Hãy viết câu truy vấn thêm khoá chính Sid cho bảng casi.

## 3. CẬP NHẬT VÀ TRUY XUẤT DỮ LIỆU

<!-- term: Cập nhật và truy xuất dữ liệu bằng DML -->
Thành phần DML của SQL cung cấp các câu truy vấn cập nhật và truy xuất dữ liệu. Sau đây là một vài câu truy xuất dữ liệu để minh hoạ.

**Bảng 14.3.** *Câu truy xuất dữ liệu*

| Câu truy xuất dữ liệu | Ý nghĩa |
| :--- | :--- |
| `SELECT <dữ liệu cần lấy>`<br>`FROM <tên bảng>` | `<dữ liệu cần lấy>` có thể là danh sách các trường hay hàm nào đó với các biến là trường trong bảng |
| `WHERE <điều kiện chọn>` | Chỉ định chọn chỉ các dòng thoả mãn điều kiện xác định |
| `ORDER BY <tên trường>` | Sắp xếp các dòng kết quả theo thứ tự chỉ định |
| `INNER JOIN` | Liên kết các bảng theo điều kiện |

Một số câu truy vấn cập nhật dữ liệu cho trong Bảng 14.4.

**Bảng 14.4.** *Các câu truy vấn cập nhật dữ liệu*

| Câu truy vấn cập nhật dữ liệu | Ý nghĩa |
| :--- | :--- |
| `INSERT INTO <tên bảng>`<br>`VALUES <danh sách giá trị>` | Thêm dữ liệu vào bảng `<tên bảng>` với giá trị lấy từ `<danh sách giá trị>` |
| `DELETE FROM <tên bảng>`<br>`WHERE <điều kiện>` | Xoá các dòng trong bảng `<tên bảng>` thoả mãn `<điều kiện>` |
| `UPDATE <tên bảng>`<br>`SET <tên trường> = <giá trị>` | Cập nhật `<giá trị>` cho trường có tên là `<tên trường>` trong bảng `<tên bảng>` |

Ví dụ:

```sql
-- Chọn ra từ bảng bannhac các dòng có Aid = 1, ở mỗi dòng chỉ lấy giá trị các cột Mid và TenBN.
-- Sắp xếp các dòng kết quả theo thứ tự TenBN.
SELECT Mid, TenBN
FROM bannhac
WHERE Aid=1
ORDER by TenBN;

-- Chọn lấy tất cả các dòng từ bảng bannhac, liên kết với bảng nhacsi theo khoá Aid,
-- ở mỗi dòng lấy cột TenBN ở bảng bannhac và cột TenNS ở bảng nhacsi.
SELECT bannhac.TenBN, nhacsi.TenNS
FROM bannhac INNER JOIN nhacsi
ON bannhac.Aid = nhacsi.Aid;

-- Thêm vào bảng nhacsi hai dòng mới.
INSERT INTO nhacsi VALUES
(5, 'Phú Quang'),
(6, 'Phan Huỳnh Điểu');

-- Xoá dòng có Mid = '0005' trong bảng bannhac.
DELETE FROM bannhac
WHERE Mid = '0005';

-- Thay đổi giá trị cột TenNS thành 'Hoàng Hiệp' ở dòng có cột Aid = 6 trong bảng nhacsi.
UPDATE nhacsi
SET TenNS = 'Hoàng Hiệp'
WHERE Aid = 6;
```

<!-- pdf:73 -->

Giả sử đã có bảng diemtoan_11A, trong đó có cột tb ghi điểm trung bình môn Toán của tất cả các học sinh lớp 11A. Khi đó câu truy vấn sau lấy ra điểm trung bình cộng môn Toán của tất cả các học sinh lớp 11A.

```sql
SELECT AVG(tb) FROM diemtoan_11A;
```

> ❓ **Câu hỏi**
>
> 1. Hãy viết câu truy vấn lấy tất cả các dòng của bảng nhacsi.
> 2. Hãy viết câu truy vấn thêm các dòng cho bảng casi với các giá trị là ('TK', 'Nguyễn Trung Kiên'), ('QD', 'Quý Dương'), ('YM', 'Y Moan').

## 4. KIỂM SOÁT QUYỀN TRUY CẬP

<!-- term: Kiểm soát quyền truy cập bằng DCL -->
Thành phần DCL của SQL cung cấp các câu truy vấn kiểm soát quyền người dùng đối với CSDL, tóm tắt trong Bảng 14.5.

**Bảng 14.5.** *Câu truy vấn kiểm soát quyền người dùng*

| Mẫu câu truy vấn | Ý nghĩa |
| :--- | :--- |
| `GRANT` | Cấp quyền cho người dùng |
| `REVOKE` | Thu hồi quyền đối với người dùng |

Ví dụ:

```sql
-- Cấp quyền dùng truy vấn SELECT đối với tất cả các bảng trong CSDL music cho người dùng guest.
GRANT select
ON music.*
TO guest ;

-- Thu hồi quyền CREATE và ALTER cho bảng bannhac trong CSDL music đối với người dùng mod.
REVOKE create, alter
ON music.bannhac
FROM mod ;
```

> ❓ **Câu hỏi**
>
> 1. Hãy viết câu truy vấn cấp quyền `UPDATE` đối với tất cả các bảng trong CSDL music cho người dùng mod.
> 2. Hãy viết câu truy vấn thu hồi quyền `DELETE` đối bảng nhacsi trong CSDL music cho người dùng mod.

## ✏️ Luyện tập

1. Hãy viết câu truy vấn tạo bảng Bản thu âm (banthuam) như đã mô tả trong Bài 13.
2. Viết câu truy vấn tạo khoá ngoài Mid và Sid cho bảng banthuam.
3. Viết câu truy vấn lấy ra tất cả các dòng trong liên kết bảng banthuam với bảng bannhac, mỗi dòng lấy các cột: Mid, Sid của bảng banthuam và cột TenBN của bảng bannhac.

## 🚀 Vận dụng

Viết câu truy vấn lấy ra tất cả các dòng trong liên kết bảng banthuam với bảng bannhac và bảng casi, mỗi dòng lấy các cột: Mid, Sid của bảng banthuam, cột TenBN của bảng bannhac và TenCS của bảng casi.
