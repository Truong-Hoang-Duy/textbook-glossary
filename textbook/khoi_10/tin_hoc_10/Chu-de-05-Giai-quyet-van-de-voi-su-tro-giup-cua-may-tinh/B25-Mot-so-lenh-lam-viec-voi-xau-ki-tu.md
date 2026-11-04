---
unit: tin_hoc_10
lesson_id: b25
toc_path:
  - "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính"
  - "Bài 25. Một số lệnh làm việc với xâu kí tự"
source_file: "SGK Tin hoc 10.pdf"
pdf_pages: [124, 127]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:124 -->

# BÀI 25: MỘT SỐ LỆNH LÀM VIỆC VỚI XÂU KÍ TỰ

## 🎯 Sau bài học này em sẽ:

- Biết và thực hiện được một số lệnh thường dùng với xâu kí tự.

## 🔴 Khởi động

> Bài toán tìm kiếm xâu con trong một xâu là một trong những bài toán tin học được ứng dụng nhiều trong thực tế. Công cụ tìm kiếm thông tin trên Internet hay lệnh tìm kiếm trong soạn thảo văn bản được xây dựng trên cơ sở bài toán tìm xâu con.
>
> Cho xâu `c = "Trường Sơn"` và xâu `m = "Bước chân trên dải Trường Sơn"`. Em hãy cho biết xâu `c` có là xâu con của xâu `m` không. Nếu có thì tìm vị trí của xâu `c` trong xâu `m`.

## 1. XÂU CON VÀ LỆNH TÌM VỊ TRÍ XÂU CON

> **Hoạt động 1: Một số lệnh tìm kiếm xâu con trong xâu kí tự**
>
> Quan sát các ví dụ sau để tìm hiểu cách kiểm tra xâu con và tìm kiếm vị trí xâu con trong xâu kí tự.

**Ví dụ 1.** Dùng toán tử `in` để kiểm tra một xâu có là xâu con của xâu khác không.

```python
>>> "abc" in "123abc"
True
>>> "010" in "1101"
False
```

Biểu thức kiểm tra `<xâu 1>` nằm trong `<xâu 2>` là:

```python
<xâu 1> in <xâu 2>
```

Nếu đúng thì trả lại giá trị `True`, nếu sai trả lại giá trị `False`.

**Ví dụ 2.** Lệnh **`find()`** tìm vị trí xuất hiện của một xâu trong xâu khác.

```python
>>> s = "ab bc cd 123 456 00"
>>> s.find("b")
1     # Vị trí xuất hiện đầu tiên của "b" trong xâu s là chỉ số 1.
>>> s.find("12")
9     # Vị trí tìm thấy đầu tiên của "12" trong xâu s là chỉ số 9.
>>> s.find("AB")
-1    # Không tìm thấy xâu "AB" trong xâu s nên trả về -1.
```

<!-- pdf:125 -->

Tương tự danh sách, Python cũng có một số lệnh đặc biệt dành riêng cho xâu kí tự (phương thức). Cách thực hiện phương thức là:

```python
<xâu>.<phương thức>
```

Cú pháp đơn của lệnh `find()`:

```python
<xâu mẹ>.find(<xâu con>)
```

Lệnh sẽ tìm vị trí đầu tiên của xâu con trong xâu mẹ và trả về vị trí đó. Nếu không tìm thấy thì trả về `-1`.

Cú pháp đầy đủ của lệnh `find()`:

```python
<xâu mẹ>.find(<xâu con>,start)
```

Lệnh sẽ tìm vị trí xâu con bắt đầu từ vị trí `start`.

**Ví dụ 3**

```python
>>> sub = "Đà Nẵng"
>>> s = "Hà Nội - Đà Nẵng - Hồ Chí Minh"
>>> s.find(sub)
9
>>> s.find(sub,10)
-1
```

<!-- term: Phương thức find() -->
> Để tìm một xâu trong một xâu khác có thể dùng toán tử `in` hoặc lệnh **`find()`**. Lệnh `find()` trả về vị trí của xâu con trong xâu mẹ.

> ❓ **Câu hỏi**
>
> 1. Biểu thức lôgic sau là đúng hay sai?
>
> ```python
> >>> "010" in "001100"
> ```
>
> 2. Lệnh sau trả lại giá trị gì?
>
> ```python
> >>> "ababababab".find("ab",4)
> ```

## 2. MỘT SỐ LỆNH THƯỜNG DÙNG VỚI XÂU KÍ TỰ

> **Hoạt động 2: Một số lệnh thường dùng với xâu kí tự**
>
> Quan sát các ví dụ sau để biết cách sử dụng một số lệnh thường dùng với xâu kí tự như: `split()`, `join()`.

**Ví dụ 1.** Lệnh **`split()`** tách một xâu thành danh sách các từ.

```python
>>> s = "Tiên học lễ hậu học văn"
>>> s.split()        # Tách xâu dùng dấu cách để phân biệt tách.
['Tiên', 'học', 'lễ', 'hậu', 'học', 'văn']
>>> st = "0,1,2,3,4,5,6,10"
>>> st.split(",")    # Tách xâu dùng dấu "," để phân biệt tách.
['0', '1', '2', '3', '4', '5', '6', '10']
```

<!-- pdf:126 -->

Lệnh **`split()`** tách một xâu thành các từ và đưa vào một danh sách. Kí tự tách dùng để phân tách các từ mặc định là dấu cách, tuy nhiên có thể thay thế kí tự tách bằng kí tự khác.

Cú pháp của lệnh `split()`.

```python
<xâu mẹ>.split(<kí tự tách>)
```

**Ví dụ 2.** Lệnh **`join()`** nối danh sách gồm các từ thành một xâu.

```python
>>> A = ['Tiên', 'học', 'lễ', 'hậu', 'học', 'văn']
>>> " ".join(A)    # Lệnh join() này sẽ nối các phần tử của danh sách A bởi dấu cách.
'Tiên học lễ hậu học văn'
>>> B = ['0', '1', '2', '3', '4', '5', '6', '10']
>>> ",".join(B)    # Lệnh join() này sẽ nối các phần tử của danh sách B bởi dấu ",".
'0,1,2,3,4,5,6,10'
```

Lệnh **`join()`** có tác dụng ngược với lệnh `split()`, có chức năng nối các phần tử (là xâu) của một danh sách thành một xâu. Cú pháp của lệnh `join()` là:

```python
"kí tự nối".joint(<danh sách>)
```

<!-- term: Phương thức split() và join() -->
> Python có các lệnh đặc biệt để xử lí xâu là **`split()`** dùng để tách xâu thành danh sách và lệnh **`join()`** dùng để nối danh sách các xâu thành một xâu.

> ❓ **Câu hỏi**
>
> Cho xâu kí tự: `"gà,vịt,chó,lợn,ngựa,cá"`. Em hãy trình bày cách làm để xoá các dấu `","` và thay thế bằng dấu `" "` trong xâu này.

## THỰC HÀNH

**Một số bài toán liên quan đến xâu kí tự.**

### Nhiệm vụ 1. Viết chương trình nhập nhiều số nguyên từ bàn phím, các số cách nhau bởi dấu cách. Khi nhập xong thông báo số lượng các số đã nhập và in các số này thành hàng ngang.

**Hướng dẫn.** Dữ liệu nhập vào là một xâu. Dùng lệnh `split()` để tách thành danh sách. Chuyển các phần tử của danh sách này thành số và in ra màn hình.

```python
s = input("Nhập các số nguyên cách nhau bởi dấu cách: ")
sline = s.split()
n = len(sline)
nline = []
for x in sline:
    nline.append(int(x))
print("Bạn đã nhập",n,"số.")
for k in nline:
    print(k, end = " ")
```

<!-- pdf:127 -->

### Nhiệm vụ 2. Viết chương trình nhập một xâu kí tự có thể có nhiều dấu cách giữa các từ. Sau đó chỉnh sửa xâu kí tự đó sao cho giữa các từ chỉ có một dấu cách. In xâu kết quả ra màn hình.

**Hướng dẫn.** Chuyển xâu kí tự ban đầu thành danh sách các từ đơn bằng lệnh `split()`, sau đó nối các từ đơn này bằng lệnh `join()`.

```python
s = input("Nhập đoạn văn bản: \n")
sline = s.split()
skq = " ".join(sline)
print(skq)
```

### Nhiệm vụ 3. Viết chương trình nhập số tự nhiên `n`, rồi nhập họ tên của `n` học sinh. Sau đó in ra danh sách tên học sinh theo hai cột, cột 1 là tên, cột 2 là họ đệm.

**Hướng dẫn.** Họ tên ban đầu tách ra thành tên và họ đệm bằng lệnh `split()`. Các tên được đưa vào danh sách `ten`, các họ đệm được đưa vào danh sách `hodem`. Sau đó in ra danh sách theo yêu cầu.

```python
n = int(input("Nhập số học sinh trong lớp: "))
ten = []
hodem = []
for i in range(n):
    s = input("Nhập họ tên học sinh thứ "+str(i+1)+": ")
    sline = s.split()
    m = len(sline)-1
    ten.append(sline[m])
    del sline[m]
    hodem.append(" ".join(sline))
print("Danh sách học sinh:")
for i in range(n):
    print(ten[i],hodem[i])
```

## ✏️ Luyện tập

1. Viết chương trình nhập nhiều số (số nguyên hoặc số thực) từ bàn phím, các số cách nhau bởi dấu cách. Sau đó in ra màn hình tổng các số đã nhập.
2. Viết chương trình nhập họ tên đầy đủ của người dùng, sau đó in thông báo tên và họ đệm của người đó.

## 🚀 Vận dụng

1. Viết chương trình nhập hai số tự nhiên từ bàn phím, cách nhau bởi dấu cách và đưa ra kết quả là ƯCLN của hai số này.
2. Viết chương trình nhập số tự nhiên `n` rồi nhập `n` họ tên học sinh. Sau đó yêu cầu nhập một tên và thông báo số bạn có cùng tên đó trong lớp.

## 📷 Danh sách hình trong bài

*(Không có hình minh hoạ)*
