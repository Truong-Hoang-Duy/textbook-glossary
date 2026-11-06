---
unit: toan_11
lesson_id: hd-thtn-03
toc_path:
  - "Chương IX. Đạo hàm"
  - "Một vài mô hình toán học sử dụng hàm số mũ và hàm số lôgarit"
source_file: "SGK TOAN 11 - KNTT - TAP 2.pdf"
pdf_pages: [100, 102]
lesson_type: thuc_hanh
status: verified
---

<!-- pdf:100 -->

<!-- Phần giới thiệu Hoạt động thực hành trải nghiệm (in chung đầu trang PDF 100): HOẠT ĐỘNG THỰC HÀNH TRẢI NGHIỆM -->

Phần này đưa em tới những hoạt động trải nghiệm đối với hàm số mũ, hàm số lôgarit và nhiều khái niệm, tính chất và kết quả của hình học không gian.

# MỘT VÀI MÔ HÌNH TOÁN HỌC SỬ DỤNG HÀM SỐ MŨ VÀ HÀM SỐ LÔGARIT

## 1. MÔ HÌNH TĂNG TRƯỞNG HOẶC SUY THOÁI CẤP MŨ

<!-- term: Luật hàm số mũ -->
Người ta thấy rằng nhiều hiện tượng tự nhiên tuân theo quy luật một đại lượng $A$ biến thiên theo thời gian $t$ theo hàm số mũ sau:

$A(t) = A_0 e^{kt}.$

Ở đây $A_0$ là lượng ban đầu (ứng với $t = 0$) và $k \ne 0$ là một hằng số. Khi đó đại lượng $A$ được gọi là tuân theo **luật hàm số mũ** (tăng trưởng nếu $k > 0$, suy thoái nếu $k < 0$).

**Vận dụng 1:** (Ước tính dân số)

Năm 2020, dân số thế giới khoảng $7\,795$ triệu người và tỉ lệ tăng dân số là $1,05\%$ mỗi năm (theo *danso.org*). Nếu tỉ lệ tăng dân số này giữ nguyên, hãy ước tính dân số thế giới vào năm 2050 (làm tròn kết quả đến hàng triệu).

<!-- term: Chu kì bán rã -->
Các chất phóng xạ đều có **chu kì bán rã** riêng, là thời gian cần thiết để một nửa số chất phóng xạ bị phân rã. Trong **phương pháp xác định niên đại bằng carbon**, người ta sử dụng thực tế là tất cả các sinh vật sống đều chứa hai loại carbon: carbon-12 (một loại carbon ổn định) và carbon-14 (một loại carbon phóng xạ với chu kì bán rã $5\,730$ năm). Khi một sinh vật đang sống, tỉ lệ giữa carbon-12 và carbon-14 là không đổi. Nhưng khi một sinh vật chết đi, lượng carbon-12 ban đầu không thay đổi nhưng lượng carbon-14 bắt đầu giảm. Sự thay đổi lượng carbon-14 này so với lượng carbon-12 hiện tại giúp chúng ta có thể tính được thời điểm sinh vật chết.

**Vận dụng 2:** (Ước tính thời đại của các công cụ cổ đại)

Dấu vết của gỗ bị đốt cháy cùng với các công cụ đá cổ đại trong một cuộc khai quật khảo cổ học được phát hiện có chứa khoảng $1,67\%$ lượng carbon-14 ban đầu. Biết chu kì bán rã của carbon-14 là $5\,730$ năm (theo *britannica.com*), hãy ước tính khoảng thời gian cây bị chặt và đốt.

<!-- pdf:101 -->

## 2. THANG ĐO LÔGARIT

<!-- term: Thang đo lôgarit -->
Khi một đại lượng vật lí thay đổi trong một phạm vi rất lớn, để thuận tiện người ta thường lấy lôgarit thập phân của nó để có một bộ số dễ quản lí hơn. Chúng ta sẽ xét ba tình huống như vậy: *thang đo pH* đo độ acid; *thang độ Richter* đo cường độ của các trận động đất và *thang đo decibel* đo độ lớn của âm thanh.

**a) Thang đo pH**

<!-- term: Thang đo pH -->
Trước đây các nhà hoá học thường đo tính acid của một dung dịch bằng cách đo nồng độ ion hydrogen của nó. Vào năm 1909, nhà hoá học người Đan Mạch Søren Peter Lauritz Sørensen đề xuất một phương pháp thuận tiện hơn, ông định nghĩa

$\text{pH} = -\log[\text{H}^+],$

trong đó $[\text{H}^+]$ là nồng độ của các ion hydrogen được đo bằng mol/lít ($\text{M}$). Ông làm điều này để tránh những số rất nhỏ và số mũ âm. Ví dụ, nếu $[\text{H}^+] = 10^{-4}\text{ M}$ thì $\text{pH} = -\log[10^{-4}] = 4$.

Dung dịch có độ $\text{pH} = 7$ được xác định là *trung tính*, dung dịch có độ $\text{pH} < 7$ có tính *acid* và dung dịch có độ $\text{pH} > 7$ là dung dịch *base*. Nhận thấy rằng khi pH tăng $1$ đơn vị thì $[\text{H}^+]$ giảm đi $10$ lần.

| Chất | Độ pH |
| :--- | :---: |
| Sữa magie | $10,5$ |
| Nước biển | $8,0 - 8,4$ |
| Máu người | $7,3 - 7,5$ |
| Bánh quy giòn | $7,0 - 8,5$ |
| Sữa bò | $6,4 - 6,8$ |
| Cà chua | $4,1 - 4,4$ |
| Cam | $3,0 - 4,0$ |
| Táo | $2,9 - 3,3$ |
| Pin acid | $1,0$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 101, bảng Độ pH của một số chất phổ biến -->

*(Theo britannica.com)*

**Vận dụng 3:** (Tính độ pH)
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 101 -->

Nồng độ ion hydrogen của nước chanh là $[\text{H}^+] = 5,0 \cdot 10^{-3}\text{ M}$. Hãy tính độ pH của nước chanh và cho biết nó có tính acid hay base.

**b) Thang độ Richter**

<!-- term: Thang độ Richter -->
Vào năm 1935, nhà địa chất học người Mỹ Charles Richter đã định nghĩa cường độ $M$ của một trận động đất là

$M = \log \frac{I}{S},$

trong đó $I$ là biên độ của trận động đất (được đo bằng biên độ của kết quả đo địa chấn lấy $100\text{ km}$ từ tâm động của trận động đất) và $S$ là biên độ của một trận động đất “tiêu chuẩn” (có biên độ là $1\text{ micrômét} = 10^{-6}\text{ mét}$). Cường độ của một trận động đất “tiêu chuẩn” là

$M = \log \frac{S}{S} = \log 1 = 0.$

Thang độ Richter cung cấp các con số dễ quản lí hơn để làm việc. Chẳng hạn, một trận động đất có cường độ $6$ độ Richter mạnh hơn $10$ lần so với một trận động đất có cường độ $5$ độ Richter.

| Địa điểm | Năm | Độ Richter |
| :--- | :---: | :---: |
| Chile | $1960$ | $9,5$ |
| Alaska | $1964$ | $9,2$ |
| Sumatra | $2004$ | $9,1$ |
| Alaska | $1957$ | $9,1$ |
| Kamchatka | $1952$ | $9,0$ |
| Chile | $2010$ | $8,8$ |
| Ecuador | $1906$ | $8,8$ |
| Alaska | $1965$ | $8,7$ |
| Sumatra | $2005$ | $8,7$ |
| Tibet | $1950$ | $8,6$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 101, bảng Những trận động đất lớn nhất -->

*(Theo britannica.com)*

<!-- pdf:102 -->

Ở $3$ độ Richter, động đất chỉ có ảnh hưởng trong một vùng có diện tích nhỏ; ở $4$ đến $5$ độ Richter, động đất gây ra một số thiệt hại nhỏ; ở $6$ đến $8$ độ Richter, động đất gây ra thiệt hại lớn; ở $9$ độ Richter, thiệt hại là cực kì lớn.

**Vận dụng 4:** (Tính cường độ của một trận động đất)

Trận động đất năm 1906 ở San Francisco có cường độ ước tính là $8,3$ độ Richter. Trong cùng năm đó, một trận động đất mạnh đã xảy ra ở biên giới Colombia-Ecuador với cường độ mạnh gấp $4$ lần. Hỏi trận động đất ở biên giới Colombia-Ecuador có cường độ là bao nhiêu độ Richter?

*(Theo britannica.com)*

**c) Thang đo decibel**

<!-- term: Thang đo decibel -->
Tai người nhạy cảm với nhiều cường độ âm thanh khác nhau. Chúng ta lấy cường độ tham chiếu $I_0 = 10^{-12}\text{ W/m}^2$ (woát trên mét vuông) ở tần số $1\,000\text{ hertz}$, nó đo âm thanh nhỏ nhất mà tai người có thể phát hiện được (gọi là **ngưỡng nghe**). Cảm giác tâm lí về âm lượng thay đổi theo lôgarit của cường độ (định luật Weber-Fechner), do đó **mức cường độ âm** $L$, đo bằng decibel ($\text{dB}$), được định nghĩa là $L = 10\log \frac{I}{I_0}$.

Mức cường độ âm đặc trưng cho độ to nhỏ của âm. Công thức trên cho thấy: Khi cường độ của âm tăng lên $10^2, 10^3, \dots$ lần thì cảm giác về độ to nhỏ của âm tăng lên gấp $2, 3, \dots$ lần.

*Mức cường độ âm của một số âm thanh thường nghe (ngưỡng làm đau tai là khoảng $120\text{ dB}$)*

| Nguồn âm thanh | $L\text{ (dB)}$ |
| :--- | :---: |
| Máy bay phản lực cất cánh | $140$ |
| Buổi hoà nhạc rock | $120$ |
| Tàu điện ngầm | $100$ |
| Nhiều xe cộ lưu thông | $80$ |
| Giao thông bình thường | $70$ |
| Cuộc trò chuyện bình thường | $50$ |
| Thì thầm | $30$ |
| Tiếng lá xào xạc | $10 - 20$ |
| Ngưỡng nghe | $0$ |
<!-- ocr-ok: đã đối chiếu ảnh trang PDF 102, bảng Mức cường độ âm -->

*(Theo britannica.com)*

**Vận dụng 5:** (Tính mức cường độ âm)

Cường độ của âm thanh giao thông tại một ngã tư đông đúc đo được là $2,0 \cdot 10^{-5}\text{ W/m}^2$. Tìm mức cường độ âm tính bằng decibel.
