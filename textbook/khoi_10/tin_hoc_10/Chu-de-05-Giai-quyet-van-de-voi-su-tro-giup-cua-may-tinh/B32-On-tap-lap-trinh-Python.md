---
unit: tin_hoc_10
lesson_id: b32
toc_path:
  - "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính"
  - "Bài 32. Ôn tập lập trình Python"
source_file: "SGK Tin hoc 10.pdf"
pdf_pages: [154, 156]
lesson_type: on_tap
status: verified
---

<!-- pdf:154 -->

# BÀI 32: ÔN TẬP LẬP TRÌNH PYTHON

## 🎯 Sau bài học này em sẽ:

- Thực hành ôn tập lập trình Python.
- Thực hành lập trình giải bài toán có tính liên môn.

## Nhiệm vụ 1. Viết chương trình nhập họ tên đầy đủ từ bàn phím, ví dụ "Nguyễn Thị Mai Hương", sau đó tách riêng phần tên, họ, đệm và in ra màn hình.

**Hướng dẫn.** Trong Bài 25 chúng ta sẽ biết cách tách phần họ đệm và tên từ một xâu họ và tên. Bài này yêu cầu thêm tách phần đệm, tức là phần nằm giữa tên và họ ra bằng cách sử dụng lệnh `join()`. Xâu kí tự ban đầu được tách thành một danh sách dùng hàm `split()`. Sau khi lấy phần họ và tên, phần đệm sẽ lấy ra theo lệnh sau:

```python
dem = " ".join(slist[1:n-1])
```

Trong đó `slist` là danh sách được tách ra từ xâu ban đầu, `n` là độ dài của xâu `slist`.

Nhập, chạy thử và kiểm tra chương trình sau:

```python
hoten = input("Nhập họ tên đầy đủ của em: ")
slist = hoten.split()
n = len(slist)
ho = slist[0]
ten = slist[n-1]
dem = " ".join(slist[1:n-1])
print("Tên của em là",ten)
print("Họ của em là",ho)
if n > 2:
    print("Đệm của em là",dem)
```

## Nhiệm vụ 2. Trọng lượng của em trên các hành tinh khác.

Chương trình yêu cầu nhập trọng lượng của em (tính theo đơn vị N – Newton) trên Trái Đất và tính trọng lượng của em trên một hành tinh khác (ví dụ Mặt Trăng, Hoả tinh, Kim tinh, Thổ tinh, Mộc tinh, Mặt Trời).

**Hướng dẫn.** Trọng lượng đo lực hút của Trái Đất (hay hành tinh) lên vật thể. Trọng lượng có đơn vị đo N (Newton). Khối lượng vật thể tính bằng kg và giá trị này không thay đổi. Chúng ta có công thức:

$$P = m \times g \quad (1)$$
<!-- ocr-ok: đã đối chiếu ảnh trang 154, công thức toán học (1) được chuyển sang LaTeX -->

<!-- pdf:155 -->

Trong đó $P$ là trọng lượng tính bằng N, $m$ là khối lượng tính bằng kg, $g$ là gia tốc trọng trường của Trái Đất (hay hành tinh), tính theo $\text{m/s}^2$. Trên Trái Đất, $g = 9.8\text{ m/s}^2$. Trên mỗi hành tinh các giá trị $g$ sẽ khác nhau. Danh sách các hành tinh được lưu trong biến `planet`, các trọng lực tương ứng lưu trong danh sách `gravities`.

Biết trọng lượng của một người trên Trái Đất (ví dụ $P_0$) thì sẽ dễ dàng tính được trọng lượng của người này trên một hành tinh khác nếu biết giá trị $g$ của hành tinh đó. Gọi $P$ là trọng lượng cần tìm, khi đó ta có công thức sau, suy trực tiếp từ công thức (1).

$$m = P_0 / 9.8 = P / g, \text{ vậy suy ra } P = P_0 \times g / 9.8. \quad (2)$$
<!-- ocr-ok: đã đối chiếu ảnh trang 155, công thức toán học (2) được chuyển sang LaTeX -->

Em hãy nhập chương trình sau và kiểm tra tính đúng đắn của chương trình.

**weight.py**

```python
def string(w):
    s = ""
    for i in range(len(w)):
        s = s+str(i+1)+". "+w[i] + " "
    return s
planet = ["Mặt Trăng","Hoả tinh","Kim tinh","Mộc tinh","Thổ tinh", "Mặt Trời"]
gravities = [1.62, 3.711, 8.83, 24.79, 10.44, 274.0]
P_earth = float(input("Nhập trọng lượng của em, tính theo N: "))
k = int(input("Nhập số thứ tự hành tinh\n"+string(planet)+": "))
Grp = gravities[k-1]
P = round(P_earth*Grp/9.8,3)
print("Trọng lượng của em trên",planet[k-1],"là:",P,"N")
```

## Nhiệm vụ 3. Kiểm tra tính hợp lệ của ba tham số ngày, tháng, năm.

Chương trình sẽ yêu cầu nhập ba số tự nhiên: ngày, tháng, năm từ bàn phím theo khuôn dạng, ví dụ nhập `08-02-2021`. Chương trình sẽ thông báo bộ dữ liệu đã nhập là hợp lệ hay không hợp lệ.

**Hướng dẫn.** Bộ dữ liệu chính cần nhập sẽ đặt tên là **day**, **month**, **year**. Nhiệm vụ của bài toán là nhập bộ dữ liệu này và kiểm tra tính hợp lệ theo các yêu cầu về lịch của ngày, tháng, năm.

Điểm đặc biệt nhất cần chú ý là kiểm tra năm **year** có phải là nhuận không, nếu là nhuận thì tháng 2 phải có 29 ngày so với các năm không nhuận tháng 2 có 28 ngày. Chúng ta sử dụng biến danh sách số **thang** để lưu số ngày của các tháng trong năm. Sau mỗi lần nhập ba số **day**, **month**, **year** cần kiểm tra năm nhuận để cập nhật tháng 2. Khi đó, chương trình kiểm tra có thể viết đơn giản như sau:

<!-- pdf:156 -->

**date.py**

```python
thang = [31,28,31,30,31,30,31,31,30,31,30,31]
def nhuan(year):
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)
date = input("Nhập thời gian theo dạng ngày - tháng - năm: ")
tg = date.split("-")
day,month,year = int(tg[0]),int(tg[1]),int(tg[2])
if nhuan(year):
    thang[1] = 29
else:
    thang[1] = 28
if year > 0 and 1 <= month <= 12 and 1<= day <= thang[month-1]:
    print(day,"-",month,"-",year, "là hợp lệ")
else:
    print("Bộ dữ liệu đã nhập không hợp lệ")
```

## ✏️ Luyện tập

Viết chương trình nhập số `n`, sau đó nhập danh sách tên học sinh với họ, đệm, tên. Sắp xếp tên học sinh trong lớp theo bảng chữ cái. Đưa kết quả ra màn hình.

## 🚀 Vận dụng

1. Trong các phần mềm bảng tính điện tử, dữ liệu ngày tháng được coi là số ngày tính từ ngày 1-1-1990. Viết chương trình:
   - Nhập số tự nhiên `n` từ bàn phím và tính xem số đó ứng với ngày, tháng, năm nào.
   - Nhập thời gian theo khuôn dạng ngày - tháng - năm (ví dụ `8-10-2021`), tính số ngày ứng với ngày này theo phần mềm bảng tính điện tử.
2. Mở rộng bài tập trong phần luyện tập như sau:
   - Việc sắp xếp thứ tự phải ưu tiên tính theo tên trước, rồi đến họ, rồi đến đệm.
   - Sắp xếp theo thứ tự của bảng chữ cái tiếng Việt.

   *Chú ý:* Bảng chữ cái tiếng Việt (bao gồm cả dấu thanh) được sắp xếp theo thứ tự sau: AÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬBCDĐEÈÉẺẼẸÊỀẾỂỄỆGHIÌÍỈĨỊJKLMNOÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢPQRSTUÙÚỦŨỤƯỪỨỬỮỰVXYỲÝỶỸỴ.

3. Nếu $n$ là hợp số thì dễ thấy $n$ phải có ước số nguyên tố nhỏ hơn hoặc bằng $\sqrt{n}$. Viết chương trình tối ưu hoá hơn nhiệm vụ 1, bài 31, theo cách sau: để tìm ước số nguyên tố nhỏ nhất chỉ cần tìm trong các số $2, 3, \dots, \sqrt{n}$. Nếu trong dãy trên không tìm thấy ước của $n$ thì kết luận ngay $n$ là nguyên tố.

## 📷 Danh sách hình trong bài

*(Không có hình minh hoạ)*
