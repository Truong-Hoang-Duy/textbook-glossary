---
unit: tin_hoc_10
lesson_id: b24
toc_path:
  - "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính"
  - "Bài 24. Xâu kí tự"
source_file: "SGK Tin hoc 10.pdf"
pdf_pages: [120, 123]
lesson_type: ly_thuyet
status: verified
---

<!-- pdf:120 -->

# BÀI 24: XÂU KÍ TỰ

## 🎯 Sau bài học này em sẽ:

- Hiểu được xâu kí tự là kiểu dữ liệu cơ bản của Python.
- Biết và thực hiện được lệnh `for` để xử lí xâu kí tự.

## 🔴 Khởi động

> Em đã biết dữ liệu xâu kí tự (gọi tắt là xâu) từ Bài 16 và chúng ta có thể tạo các biến kiểu xâu kí tự theo nhiều cách như sau:

```python
>>> s = "Thời khoá biểu"
>>> xau = 'Hoa học trò'
>>> Cau_tho = """ Mình về mình có nhớ ta
Mười lăm năm ấy thiết tha mặn nồng"""
```

> Liệu có lệnh nào trích ra từng kí tự của một xâu kí tự? Đếm số kí tự của một xâu?

## 1. XÂU LÀ MỘT DÃY CÁC KÍ TỰ

> **Hoạt động 1: Tìm hiểu cấu trúc của xâu kí tự**
>
> Quan sát các ví dụ sau để biết cấu trúc xâu kí tự, so sánh với danh sách để biết sự khác nhau giữa xâu (`string`) và danh sách (`list`).

**Ví dụ 1.** Xâu kí tự và cách truy cập đến từng kí tự của xâu.

```python
>>> s = "Thời khoá biểu"
>>> len(s)    # Lệnh len() sẽ tính độ dài của xâu hay số lượng các kí tự có trong xâu.
14
>>> s[0]      # Có thể truy cập từng kí tự của xâu thông qua chỉ số. Chỉ số bắt đầu từ 0.
'T'
>>> s[10]
'b'
```

Một **xâu kí tự** được hiểu là một dãy các kí tự. Tương tự danh sách, ta có thể truy cập từng kí tự của xâu thông qua chỉ số, chỉ số bắt đầu từ 0.

**Ví dụ 2.** Quan sát các lệnh sau để thấy sự khác nhau giữa xâu và danh sách.

```python
>>> d = ["a","b","c"]
>>> d[0] = "A"
>>> s = "abc"
>>> s[0] = "A"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[0] = "A"
TypeError: 'str' object does not support item assignment
```

<!-- pdf:121 -->

Python không cho phép thay đổi từng kí tự của một xâu. Điều này khác với danh sách.

Python không có kiểu dữ liệu kí tự. **Kí tự** chính là xâu có độ dài 1. **Xâu rỗng** được định nghĩa như sau:

```python
empty = ""
```

<!-- term: Xâu kí tự -->
> **Xâu kí tự** trong Python là dãy các kí tự Unicode. Xâu có thể được coi là danh sách các kí tự nhưng không thay đổi từng kí tự của xâu. Truy cập từng kí tự của xâu qua chỉ số, chỉ số từ 0 đến độ dài `len() - 1`.

> ❓ **Câu hỏi**
>
> 1. Các xâu kí tự sau có hợp lệ không?
>    a) `"123&*()-+ABC"`
>    b) `"1010110&0101001"`
>    c) `"Tây Nguyên"`
>    d) `11111111 = 256`
> 2. Mỗi xâu hợp lệ ở Câu 1 có độ dài bằng bao nhiêu?

## 2. LỆNH DUYỆT KÍ TỰ CỦA XÂU

> **Hoạt động 2: Tìm hiểu lệnh duyệt từng kí tự của xâu**
>
> Quan sát các lệnh sau để biết cách duyệt từng kí tự của xâu kí tự bằng lệnh `for`. Có hai cách duyệt, theo chỉ số và theo phần tử của xâu kí tự.

```python
>>> s = "Thời khoá biểu"
>>> for i in range(len(s)):    # Duyệt theo chỉ số với lệnh range().
        print(s[i],end = " ")

T h ờ i   k h o á   b i ể u 
>>> for ch in s:               # Duyệt theo kí tự của xâu kí tự.
        print(ch, end = " ")

T h ờ i   k h o á   b i ể u 
```

- Cách thứ nhất, biến `i` lần lượt chạy theo chỉ số của xâu kí tự `s`, từ 0 đến `len(s) - 1`. Kí tự tại chỉ số `i` là `s[i]`.
- Cách thứ hai duyệt theo từng kí tự của xâu `s`. Biến `ch` sẽ được gán lần lượt các kí tự của xâu `s` từ đầu đến cuối.

*Chú ý:* Từ khoá **`in`**, tuỳ trường hợp cụ thể, hoặc là toán tử lôgic dùng để kiểm tra một giá trị có mặt hay không trong một vùng giá trị/danh sách/xâu, hoặc để chọn lần lượt từng phần tử trong một vùng giá trị/danh sách/xâu.

```python
>>> "a" in "abcd"
True
>>> "abc" in "abcd"
True
```

<!-- pdf:122 -->

<!-- term: Xâu con -->
> Có thể duyệt các kí tự của xâu bằng lệnh `for` tương tự như với danh sách.
> `s1 in s2` trả lại giá trị `True` nếu `s1` là **xâu con** của `s2`.

> ❓ **Câu hỏi**
>
> 1. Sau khi thực hiện các lệnh sau, biến `skq` sẽ có giá trị bao nhiêu?

```python
>>> s = "81723"
>>> skq = ""
>>> for ch in s:
        if int(ch) % 2 != 0:
            skq = skq + ch
```

> 2. Cho `s1 = "abc"`, `s2 = "ababcabca"`. Các biểu thức lôgic sau cho kết quả là đúng hay sai?
>    a) `s1 in s2`
>    b) `s1 + s1 in s2`
>    c) `"abcabca" in s2`
>    d) `"abc123" in s2`

## THỰC HÀNH

**Các lệnh cơ bản làm việc với xâu kí tự**

### Nhiệm vụ 1. Viết chương trình nhập số tự nhiên `n` là số học sinh, sau đó nhập họ và tên học sinh. Lưu họ và tên học sinh vào một danh sách. In danh sách ra màn hình, mỗi họ tên trên một dòng.

**Hướng dẫn.** Chương trình có thể như sau:

```python
n = int(input("Nhập số học sinh trong lớp: "))
ds_lop = []
for i in range(n):
    hoten = input("Nhập họ tên học sinh thứ " + str(i+1)+": ")
    ds_lop.append(hoten)
print("Danh sách lớp học:")
for i in range(n):
    print(ds_lop[i])
```

### Nhiệm vụ 2. Nhập một xâu kí tự `S` từ bàn phím rồi kiểm tra xem xâu `S` có chứa xâu con `"10"` không.

**Hướng dẫn.** Cách 1. Nếu xâu `S` chứa xâu con `"10"` thì sẽ có chỉ số `k` mà `S[k] = "1"` và `S[k+1] = "0"`. Cách 2. Dùng toán tử `in` để kiểm tra xâu `"10"` có là xâu con của `S`.

Cách 1: Duyệt kí tự của xâu theo chỉ số.

```python
S = input("Nhập xâu kí tự bất kì: ")
kq = False
```

<!-- pdf:123 -->

```python
for i in range(len(S)-1):
    if S[i] == "1" and S[i+1] == "0":
        kq = True
        break
if kq:
    print("Xâu gốc có chứa xâu '10'")
else:
    print("Xâu gốc không chứa xâu '10'")
```

Cách 2: Sử dụng toán tử `in`.

```python
S = input("Nhập xâu kí tự bất kì: ")
s10 = "10"
if s10 in S:
    print("Xâu gốc có chứa xâu '10'")
else:
    print("Xâu gốc không chứa xâu '10'")
```

## ✏️ Luyện tập

1. Cho xâu `S`, viết đoạn lệnh trích ra xâu con của `S` bao gồm ba kí tự đầu tiên của `S`.
2. Viết chương trình kiểm tra xâu `S` có chứa chữ số không. Thông báo `"S có chứa chữ số"` hoặc `"S không chứa chữ số nào"`.

## 🚀 Vận dụng

1. Cho hai xâu $s_1$, $s_2$. Viết đoạn chương trình chèn xâu $s_1$ vào giữa $s_2$, tại vị trí `len(s2)//2`. In kết quả ra màn hình.
2. Viết chương trình nhập số học sinh và họ tên học sinh. Sau đó đếm xem trong danh sách có bao nhiêu bạn tên là "Hương".
   *Gợi ý:* Sử dụng toán tử `in` để kiểm tra một xâu có là xâu con của một xâu khác.

## 📷 Danh sách hình trong bài

*(Không có hình minh hoạ)*
