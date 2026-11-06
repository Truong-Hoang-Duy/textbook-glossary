---
unit: tin_hoc_khmt_11
lesson_id: b22
toc_path:
  - "Chủ đề 6. Kĩ thuật lập trình"
  - "Bài 22. Thực hành bài toán sắp xếp"
source_file: "SGK TIN HOC 11 CS - KNTT.pdf"
pdf_pages: [105, 106]
lesson_type: thuc_hanh
status: verified
---

<!-- pdf:105 -->

# BÀI 22: THỰC HÀNH BÀI TOÁN SẮP XẾP

## 🎯 Sau bài học này em sẽ:

- Áp dụng được thuật toán sắp xếp trong một vài bài toán cụ thể.

## 🔴 Khởi động

> Trong Bài 21, em đã được học cách triển khai thuật toán sắp xếp để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần. Nếu cần sắp xếp theo thứ tự ngược lại thì câu lệnh so sánh tương ứng trong vòng lặp sẽ cần thay đổi như thế nào?

## Nhiệm vụ 1. Sắp xếp số lượng các mặt hàng trong kho theo thứ tự tăng dần

Cho danh sách số lượng mỗi mặt hàng trong kho của một cửa hàng. Người quản lí kho cần xem các mặt hàng theo thứ tự số lượng tăng dần. Em hãy viết chương trình sắp xếp các mặt hàng trong kho theo thứ tự số lượng tăng dần, sử dụng thuật toán sắp xếp chèn, sau đó in ra màn hình dãy số vừa sắp xếp. Danh sách số lượng các mặt hàng được đọc từ tệp văn bản `kho.inp`, mỗi dòng bao gồm số lượng một mặt hàng.

```text
kho.inp
5
3
10
4
8
2
```

**Hướng dẫn:**

*Phân tích:*

<!-- term: Sắp xếp danh sách tăng dần bằng thuật toán sắp xếp chèn -->
Chúng ta có thể sử dụng thuật toán sắp xếp chèn đã học ở bài học trước để sắp xếp các phần tử trong danh sách số lượng mặt hàng theo thứ tự tăng dần. Bài toán này bao gồm các bước sau: Đầu tiên, chúng ta đọc số lượng các mặt hàng trong kho từ tệp văn bản; Sau đó sử dụng thuật toán sắp xếp chèn để sắp xếp số lượng các mặt hàng; Cuối cùng là in số lượng các mặt hàng đã sắp xếp ra màn hình.

**quanlykho.py**

```python
def InsertionSort(A):
    n = len(A)
    for i in range(1,n):
        value = A[i]
        j = i-1
        while j >= 0 and A[j] > value:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = value
input_file = open("kho.inp", encoding="utf8")
soluong_ds = []
for line in input_file.readlines():
    soluong_ds.append(int(line))  # Đọc số lượng các mặt hàng trong tệp và đưa vào danh sách soluong_ds
InsertionSort(soluong_ds)
print('Số lượng các mặt hàng trong kho theo thứ tự tăng dần là:')
for i in range(len(soluong_ds)):
    print(soluong_ds[i])
```

<!-- pdf:106 -->

## Nhiệm vụ 2. Sắp xếp điểm trung bình theo thứ tự giảm dần

Cho danh sách điểm trung bình môn Tin học của các học sinh. Em hãy sử dụng thuật toán sắp xếp chọn để sắp xếp danh sách này theo thứ tự điểm trung bình giảm dần, sau đó in danh sách đã sắp xếp ra màn hình. Danh sách điểm trung bình được đọc từ tệp văn bản `diem.inp`, mỗi dòng bao gồm điểm trung bình của một học sinh.

```text
diem.inp
7.8
5.6
8.9
7.4
9.5
8.4
9.1
```

**Hướng dẫn:**

*Phân tích:*

<!-- term: Sắp xếp danh sách giảm dần bằng thuật toán sắp xếp chọn -->
Chúng ta có thể sử dụng thuật toán sắp xếp chọn đã học ở bài học trước để sắp xếp danh sách điểm số. Chú ý đề bài yêu cầu sắp xếp danh sách theo thứ tự điểm trung bình giảm dần. Do đó ở mỗi vòng lặp của thuật toán sắp xếp chọn, chúng ta phải tìm kiếm phần tử có giá trị cao nhất, thay vì tìm phần tử có giá trị bé nhất. Bài toán này bao gồm các bước sau: Đầu tiên, chúng ta đọc điểm trung bình từ tệp văn bản `diem.inp`; Sau đó sử dụng thuật toán sắp xếp chọn đã học ở bài trước để sắp xếp điểm trung bình theo thứ tự giảm dần; Cuối cùng là in danh sách điểm trung bình đã sắp xếp ra màn hình.

**sapxepdiem.py**

```python
def SelectionSort(A):
    n = len(A)
    for i in range(n-1):
        iMax = i
        for j in range(i+1,n):
            if A[j] > A[iMax]:
                iMax = j
        A[i],A[iMax] = A[iMax],A[i]
input_file = open("diem.inp", encoding="utf8")
diem_ds = []
for line in input_file.readlines():
    diem_ds.append(float(line))
SelectionSort(diem_ds)
print('Danh sách điểm theo thứ tự giảm dần là:')
for i in range(len(diem_ds)):
    print(diem_ds [i])
```

## ✏️ Luyện tập

1. Sử dụng thuật toán sắp xếp chọn viết lại chương trình trong Nhiệm vụ 1.
2. Sử dụng thuật toán sắp xếp nổi bọt viết lại chương trình trong Nhiệm vụ 2.

## 🚀 Vận dụng

Một người đi mua hàng với danh sách các mặt hàng cần mua, đơn giá từng mặt hàng và số lượng hàng cần mua được lưu trong tệp văn bản `muahang.inp`.

Hãy sử dụng thuật toán nổi bọt để sắp xếp các mặt hàng theo thứ tự thành tiền của các mặt hàng tăng dần rồi in ra tên các mặt hàng và thành tiền tương ứng.
