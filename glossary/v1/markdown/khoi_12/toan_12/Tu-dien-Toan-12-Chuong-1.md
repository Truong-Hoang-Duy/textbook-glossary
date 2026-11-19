---
name: tu-dien-toan-12-chuong-1
description: Từ điển thuật ngữ Toán 12 Chương I — Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 12
chuong: "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số"
bai_so: "Bài 1 – Bài 5"
nguon: "SGK Toán 12 Tập 1 – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: "2026-11-02"
ngay_cap_nhat: "2026-11-02"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 12 — CHƯƠNG I: ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ

## Quy ước sử dụng

- **Phạm vi:** Chương I (Bài 1 đến Bài 5 và Bài tập cuối chương I), Tập 1, SGK Toán 12 (bộ Kết nối tri thức với cuộc sống), tích hợp các mục tương ứng trong Bảng giải thích thuật ngữ cuối Tập 1 (trang in 100, PDF 102).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Kí hiệu / Công thức` | `Định nghĩa / Giải nghĩa` | `Bối cảnh trong bài`.
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm, chú ý định nghĩa hoặc bảng giải thích thuật ngữ cuối sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp từ đoạn văn/định lí/quy tắc gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.
  - *Ngoài nguồn:* các khái niệm nền tảng từ lớp dưới được nhắc lại nhưng không định nghĩa lại trong Chương I.

## Bài 1: Tính đơn điệu và cực trị của hàm số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Đồng biến (hàm số đồng biến) | $\forall x_1, x_2 \in K, x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$ | Giả sử $K$ là một khoảng, một đoạn hoặc một nửa khoảng và $y = f(x)$ là hàm số xác định trên $K$. Hàm số $y = f(x)$ được gọi là đồng biến trên $K$ nếu $\forall x_1, x_2 \in K, x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$. | Mục 1a, định nghĩa tính đồng biến của hàm số (trang 6, PDF 8). |
| Nghịch biến (hàm số nghịch biến) | $\forall x_1, x_2 \in K, x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$ | Giả sử $K$ là một khoảng, một đoạn hoặc một nửa khoảng và $y = f(x)$ là hàm số xác định trên $K$. Hàm số $y = f(x)$ được gọi là nghịch biến trên $K$ nếu $\forall x_1, x_2 \in K, x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$. | Mục 1a, định nghĩa tính nghịch biến của hàm số (trang 6, PDF 8). |
| Tính đơn điệu (đơn điệu; khoảng đơn điệu; xét chiều biến thiên; chiều biến thiên) | — | Hàm số đồng biến hay nghịch biến trên $K$ còn được gọi chung là đơn điệu trên $K$. Việc tìm các khoảng đồng biến, nghịch biến của hàm số còn được gọi là tìm các khoảng đơn điệu (hay xét tính đơn điệu, xét chiều biến thiên) của hàm số. | Mục 1a và Mục 1b, chú ý về tính đơn điệu và chiều biến thiên (trang 6, 8, PDF 8, 10). |
| Định lí tính đơn điệu của hàm số | $f'(x) > 0 \Rightarrow f(x)$ đồng biến; $f'(x) < 0 \Rightarrow f(x)$ nghịch biến | Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $K$. Nếu $f'(x) > 0$ với mọi $x \in K$ thì hàm số $f(x)$ đồng biến trên khoảng $K$. Nếu $f'(x) < 0$ với mọi $x \in K$ thì hàm số $f(x)$ nghịch biến trên khoảng $K$. | [mô tả] Mục 1a, định lí liên hệ giữa dấu đạo hàm và tính đơn điệu (trang 7, PDF 9). |
| Bảng biến thiên | — | Bảng biến thiên của hàm số là bảng thể hiện dấu của đạo hàm và sự đồng biến, nghịch biến của hàm số trên các khoảng tương ứng. | Mục 1b, HĐ3 giới thiệu bảng biến thiên (trang 7, PDF 9). |
| Quy tắc xét tính đơn điệu | — | Các bước để xét tính đơn điệu của hàm số $y = f(x)$: 1. Tìm tập xác định của hàm số. 2. Tính đạo hàm $f'(x)$. Tìm các điểm $x_i$ mà tại đó đạo hàm bằng $0$ hoặc không tồn tại. 3. Sắp xếp các điểm $x_i$ theo thứ tự tăng dần và lập bảng biến thiên của hàm số. 4. Nêu kết luận về khoảng đồng biến, nghịch biến của hàm số. | [mô tả] Mục 1b, các bước xét tính đơn điệu bằng bảng biến thiên (trang 8, PDF 10). |
| Cực đại (điểm cực đại; giá trị cực đại) | $f_{\text{CĐ}}$ hay $y_{\text{CĐ}} = f(x_0)$ | Nếu hàm số $y = f(x)$ đạt cực đại tại $x_0$ thì $x_0$ được gọi là điểm cực đại của hàm số $f(x)$. Khi đó, $f(x_0)$ được gọi là giá trị cực đại của hàm số $f(x)$ và kí hiệu là $f_{\text{CĐ}}$ hay $y_{\text{CĐ}}$. Điểm $M_0(x_0; f(x_0))$ được gọi là điểm cực đại của đồ thị hàm số. | Mục 2a, định nghĩa và chú ý về cực đại của hàm số (trang 9, PDF 11). |
| Cực tiểu (điểm cực tiểu; giá trị cực tiểu) | $f_{\text{CT}}$ hay $y_{\text{CT}} = f(x_0)$ | Nếu hàm số $y = f(x)$ đạt cực tiểu tại $x_0$ thì $x_0$ được gọi là điểm cực tiểu của hàm số $f(x)$. Khi đó, $f(x_0)$ được gọi là giá trị cực tiểu của hàm số $f(x)$ và kí hiệu là $f_{\text{CT}}$ hay $y_{\text{CT}}$. Điểm $M_0(x_0; f(x_0))$ được gọi là điểm cực tiểu của đồ thị hàm số. | Mục 2a, định nghĩa và chú ý về cực tiểu của hàm số (trang 9, PDF 11). |
| Điểm cực trị của hàm số (điểm cực trị) | $x_0$ | Điểm cực trị của hàm số là giá trị của biến số mà tại đó hàm số đạt cực trị; các điểm cực đại và điểm cực tiểu được gọi chung là điểm cực trị. | Mục 2a (trang 9, PDF 11) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Cực trị của hàm số (cực trị; giá trị cực trị) | $f(x_0)$ | Giá trị cực đại hoặc giá trị cực tiểu của hàm số được gọi chung là giá trị cực trị (hay cực trị) của hàm số. | Mục 2a (trang 9, PDF 11) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Điểm cực trị của đồ thị hàm số (điểm cực đại của đồ thị hàm số; điểm cực tiểu của đồ thị hàm số) | $M_0(x_0; f(x_0))$ | Điểm $(x_0; f(x_0))$, trong đó $x_0$ là điểm cực trị của hàm số $f(x)$. Nếu hàm số đạt cực đại tại $x_0$ thì điểm $M_0(x_0; f(x_0))$ được gọi là điểm cực đại của đồ thị hàm số; nếu đạt cực tiểu tại $x_0$ thì $M_0(x_0; f(x_0))$ được gọi là điểm cực tiểu của đồ thị hàm số. | Mục 2a (trang 9, PDF 11) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Định lí cực trị của hàm số | — | Giả sử hàm số $y = f(x)$ liên tục trên khoảng $(a; b)$ chứa điểm $x_0$ và có đạo hàm trên các khoảng $(a; x_0)$ và $(x_0; b)$. Nếu $f'(x) < 0$ với mọi $x \in (a; x_0)$ và $f'(x) > 0$ với mọi $x \in (x_0; b)$ thì $x_0$ là một điểm cực tiểu của hàm số $f(x)$. Nếu $f'(x) > 0$ với mọi $x \in (a; x_0)$ và $f'(x) < 0$ với mọi $x \in (x_0; b)$ thì $x_0$ là một điểm cực đại của hàm số $f(x)$. | [mô tả] Mục 2b, định lí dấu đạo hàm đổi qua điểm cực trị (trang 10, PDF 12). |
| Quy tắc tìm cực trị của hàm số | — | Từ định lí trên ta có các bước tìm cực trị của hàm số $y = f(x)$ như sau: 1. Tìm tập xác định của hàm số. 2. Tính đạo hàm $f'(x)$. Tìm các điểm mà tại đó đạo hàm $f'(x)$ bằng $0$ hoặc đạo hàm không tồn tại. 3. Lập bảng biến thiên của hàm số. 4. Từ bảng biến thiên suy ra các cực trị của hàm số. | [mô tả] Mục 2b, chú ý các bước tìm cực trị của hàm số (trang 11, PDF 13). |
| Đạo hàm | $f'(x)$, $y'$ | Ngoài nguồn — chưa định nghĩa trong Chương I Toán 12. Xem: SGK Toán 11 Tập 2, Chương IX | Công cụ nền tảng dùng xuyên suốt Bài 1 để xét tính đơn điệu và tìm cực trị. |

## Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Giá trị lớn nhất của hàm số (giá trị lớn nhất) | $M = \max_{x \in D} f(x) = \max_D f(x)$ | Cho hàm số $y = f(x)$ xác định trên tập $D$. Số $M$ được gọi là giá trị lớn nhất của hàm số $y = f(x)$ trên tập $D$ nếu $f(x) \le M$ với mọi $x \in D$ và tồn tại $x_0 \in D$ sao cho $f(x_0) = M$. | Mục 1, định nghĩa giá trị lớn nhất (trang 15, PDF 17) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Giá trị nhỏ nhất của hàm số (giá trị nhỏ nhất) | $m = \min_{x \in D} f(x) = \min_D f(x)$ | Cho hàm số $y = f(x)$ xác định trên tập $D$. Số $m$ được gọi là giá trị nhỏ nhất của hàm số $y = f(x)$ trên tập $D$ nếu $f(x) \ge m$ với mọi $x \in D$ và tồn tại $x_0 \in D$ sao cho $f(x_0) = m$. | Mục 1, định nghĩa giá trị nhỏ nhất (trang 15, PDF 17) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Tìm giá trị lớn nhất, nhỏ nhất trên đoạn | $M = \max_{[a; b]} f(x)$; $m = \min_{[a; b]} f(x)$ | Giả sử $y = f(x)$ là hàm số liên tục trên $[a; b]$ và có đạo hàm trên $(a; b)$, có thể trừ ra tại một số hữu hạn điểm mà tại đó hàm số không có đạo hàm. Các bước tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x)$ trên đoạn $[a; b]$: 1. Tìm các điểm $x_1, x_2, \dots, x_n \in (a; b)$, tại đó $f'(x)$ bằng $0$ hoặc không tồn tại. 2. Tính $f(x_1), f(x_2), \dots, f(x_n), f(a)$ và $f(b)$. 3. Tìm số lớn nhất $M$ và số nhỏ nhất $m$ trong các số trên. | [mô tả] Mục 2, quy tắc tìm GTLN và GTNN của hàm số trên đoạn $[a; b]$ (trang 18, PDF 20). |
| Hàm số liên tục | — | Ngoài nguồn — chưa định nghĩa trong Chương I Toán 12. Xem: SGK Toán 11 Tập 1, Chương V | Điều kiện giả thiết để tìm giá trị lớn nhất và nhỏ nhất của hàm số trên một đoạn. |

## Bài 3: Đường tiệm cận của đồ thị hàm số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Đường tiệm cận ngang (tiệm cận ngang) | $\lim_{x \to +\infty} f(x) = y_0$ hoặc $\lim_{x \to -\infty} f(x) = y_0$ | Đường thẳng $y = y_0$ gọi là đường tiệm cận ngang (gọi tắt là tiệm cận ngang) của đồ thị hàm số $y = f(x)$ nếu $\lim_{x \to +\infty} f(x) = y_0$ hoặc $\lim_{x \to -\infty} f(x) = y_0$. | Mục 1, định nghĩa đường tiệm cận ngang (trang 20, PDF 22) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Đường tiệm cận đứng (tiệm cận đứng) | $\lim_{x \to x_0^\pm} f(x) = \pm\infty$ | Đường thẳng $x = x_0$ gọi là đường tiệm cận đứng (gọi tắt là tiệm cận đứng) của đồ thị hàm số $y = f(x)$ nếu ít nhất một trong các điều kiện sau được thoả mãn: $\lim_{x \to x_0^+} f(x) = +\infty$; $\lim_{x \to x_0^-} f(x) = -\infty$; $\lim_{x \to x_0^+} f(x) = -\infty$; $\lim_{x \to x_0^-} f(x) = +\infty$. | Mục 2, định nghĩa đường tiệm cận đứng (trang 21, PDF 23) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Đường tiệm cận xiên (tiệm cận xiên) | $\lim_{x \to \pm\infty} [f(x) - (ax + b)] = 0$ ($a \ne 0$) | Đường thẳng $y = ax + b$ ($a \ne 0$) gọi là đường tiệm cận xiên (gọi tắt là tiệm cận xiên) của đồ thị hàm số $y = f(x)$ nếu $\lim_{x \to +\infty} [f(x) - (ax + b)] = 0$ hoặc $\lim_{x \to -\infty} [f(x) - (ax + b)] = 0$. | Mục 3, định nghĩa đường tiệm cận xiên (trang 23, PDF 25) và Bảng giải thích thuật ngữ (trang 100, PDF 102). |
| Giới hạn của hàm số (tiệm cận) | $\lim_{x \to x_0} f(x)$, $\lim_{x \to \pm\infty} f(x)$ | Ngoài nguồn — chưa định nghĩa trong Chương I Toán 12. Xem: SGK Toán 11 Tập 1, Chương V | Công cụ xác định các đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm số. |

## Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Khảo sát hàm số | — | Việc tìm tập xác định, xét chiều biến thiên, tìm cực trị, tìm các giới hạn đặc biệt của hàm số đó và thể hiện các kết quả này trong bảng biến thiên. | Bảng giải thích thuật ngữ cuối Tập 1 (trang 100, PDF 102) và Mục 1 Bài 4. |
| Sơ đồ khảo sát hàm số | — | Sơ đồ khảo sát hàm số $y = f(x)$: 1. Tìm tập xác định của hàm số. 2. Khảo sát sự biến thiên của hàm số: tính đạo hàm $y'$, tìm các điểm tại đó $y'$ bằng $0$ hoặc đạo hàm không tồn tại; xét dấu $y'$ để chỉ ra các khoảng đơn điệu; tìm cực trị; tìm các giới hạn tại vô cực, giới hạn vô cực và tìm tiệm cận của đồ thị hàm số; lập bảng biến thiên. 3. Vẽ đồ thị của hàm số dựa vào bảng biến thiên. | [mô tả] Mục 1, quy trình 3 bước khảo sát và vẽ đồ thị hàm số (trang 26, PDF 28). |
| Tâm đối xứng | $x = -\frac{b}{3a}$ (hàm bậc ba); giao điểm hai tiệm cận (hàm phân thức) | Đồ thị của hàm số bậc ba $y = ax^3 + bx^2 + cx + d \ (a \ne 0)$ có tâm đối xứng là điểm có hoành độ thoả mãn $y'' = 0$, hay $x = -\frac{b}{3a}$, và không có tiệm cận. | Mục 2 và Mục 3, chú ý về tính đối xứng của đồ thị hàm bậc ba và hàm phân thức (trang 27, 29, 32, PDF 29, 31, 34). |
| Trục đối xứng | — | Đồ thị của hàm số phân thức $y = \frac{ax + b}{cx + d}$ hoặc $y = \frac{ax^2 + bx + c}{px + q}$ nhận hai đường phân giác của các góc tạo bởi hai đường tiệm cận làm các trục đối xứng. | Mục 3a và Mục 3b, chú ý về trục đối xứng của đồ thị hàm phân thức hữu tỉ (trang 29, 32, PDF 31, 34). |
| Đồ thị hàm số (đồ thị) | $(C): y = f(x)$ | Ngoài nguồn — chưa định nghĩa trong Chương I Toán 12. Xem: SGK Toán 10 Tập 1, Chương VI | Bước cuối trong sơ đồ khảo sát sự biến thiên và vẽ đồ thị của hàm số. |

## Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Tốc độ thay đổi trung bình | $\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$ | Tỉ số $\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$ được gọi là tốc độ thay đổi trung bình của $y$ đối với $x$ trên đoạn $[x_1; x_2]$. | Mục 1, tốc độ thay đổi của một đại lượng (trang 33, PDF 35). |
| Tốc độ thay đổi tức thời | $f'(x_1) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$ | Giới hạn $\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{x_2 \to x_1} \frac{f(x_2) - f(x_1)}{x_2 - x_1}$ được gọi là tốc độ thay đổi tức thời của $y$ đối với $x$ tại điểm $x = x_1$. | Mục 1, định nghĩa tốc độ thay đổi tức thời bằng đạo hàm (trang 33, PDF 35). |
| Hàm vị trí | $s = s(t)$ | Nếu $s = s(t)$ là hàm vị trí của một vật chuyển động trên một đường thẳng thì $v = s'(t)$ biểu thị vận tốc tức thời của vật (tốc độ thay đổi của độ dịch chuyển theo thời gian). | Mục 1, ứng dụng đạo hàm trong cơ học (trang 33, PDF 35). |
| Vận tốc tức thời | $v(t) = s'(t)$ | Nếu $s = s(t)$ là hàm vị trí của một vật chuyển động trên một đường thẳng thì $v = s'(t)$ biểu thị vận tốc tức thời của vật (tốc độ thay đổi của độ dịch chuyển theo thời gian). | Mục 1, ứng dụng đạo hàm trong cơ học (trang 33, PDF 35). |
| Gia tốc tức thời | $a(t) = v'(t) = s''(t)$ | Nếu $s = s(t)$ là hàm vị trí của một vật chuyển động trên một đường thẳng thì $v = s'(t)$ biểu thị vận tốc tức thời của vật. Tốc độ thay đổi tức thời của vận tốc theo thời gian là gia tốc tức thời của vật. | Mục 1, ứng dụng đạo hàm trong cơ học (trang 33, PDF 35). |
| Tốc độ phản ứng tức thời | $C'(t)$ | Nếu $C = C(t)$ là nồng độ của một chất tham gia phản ứng hoá học tại thời điểm $t$, thì $C'(t)$ là tốc độ phản ứng tức thời (tức là độ thay đổi nồng độ) của chất đó tại thời điểm $t$. | Mục 1, ứng dụng đạo hàm trong hoá học (trang 33, PDF 35). |
| Tốc độ tăng trưởng tức thời | $P'(t)$ | Nếu $P = P(t)$ là số lượng cá thể trong một quần thể động vật hoặc thực vật tại thời điểm $t$, thì $P'(t)$ biểu thị tốc độ tăng trưởng tức thời của quần thể tại thời điểm $t$. | Mục 1, ứng dụng đạo hàm trong sinh học (trang 33, PDF 35). |
| Hàm chi phí | $C = C(x)$ | Nếu $C = C(x)$ là hàm chi phí, tức là tổng chi phí khi sản xuất $x$ đơn vị hàng hoá, thì tốc độ thay đổi tức thời $C'(x)$ của chi phí đối với số lượng đơn vị hàng được sản xuất được gọi là chi phí biên. | Mục 1 và Mục 2, ứng dụng đạo hàm trong kinh tế (trang 34, 38, PDF 36, 40). |
| Chi phí biên | $C'(x)$ | Nếu $C = C(x)$ là hàm chi phí, tức là tổng chi phí khi sản xuất $x$ đơn vị hàng hoá, thì tốc độ thay đổi tức thời $C'(x)$ của chi phí đối với số lượng đơn vị hàng được sản xuất được gọi là chi phí biên. | Mục 1 và Mục 2, ứng dụng đạo hàm trong kinh tế (trang 34, 38, PDF 36, 40). |
| Bài toán tối ưu hoá | $\max Q(x)$, $\min Q(x)$ | Quy trình giải một bài toán tối ưu hoá: Bước 1. Xác định đại lượng $Q$ mà ta cần làm cho giá trị của đại lượng ấy lớn nhất hoặc nhỏ nhất và biểu diễn nó qua các đại lượng khác trong bài toán. Bước 2. Chọn một đại lượng thích hợp nào đó, kí hiệu là $x$, và biểu diễn các đại lượng khác ở Bước 1 theo $x$. Tìm tập xác định của hàm số $Q = Q(x)$. Bước 3. Tìm giá trị lớn nhất hoặc giá trị nhỏ nhất của hàm số $Q = Q(x)$ bằng các phương pháp đã biết và kết luận. | [mô tả] Mục 2, quy trình 3 bước giải bài toán tối ưu hoá thực tiễn (trang 36–37, PDF 38–39). |
| Hàm cầu (hàm giá) | $p = p(x)$ | Gọi $p(x)$ là giá bán mỗi đơn vị mà công ty có thể tính nếu bán $x$ đơn vị. Khi đó, $p$ được gọi là hàm cầu (hay hàm giá) và chúng ta mong đợi đó là một hàm giảm của $x$. | Mục 2, các hàm kinh tế trong bài toán tối ưu hoá lợi nhuận (trang 38, PDF 40). |
| Hàm doanh thu | $R(x) = x \cdot p(x)$ | Nếu $x$ đơn vị được bán và giá mỗi đơn vị là $p(x)$ thì tổng doanh thu là $R(x) = x \cdot p(x)$ và $R(x)$ được gọi là hàm doanh thu. Đạo hàm $R'(x)$ của hàm doanh thu được gọi là hàm doanh thu biên và là tốc độ thay đổi của doanh thu đối với số lượng đơn vị sản phẩm bán ra. | Mục 2, tổng doanh thu khi bán $x$ đơn vị sản phẩm (trang 38, PDF 40). |
| Hàm doanh thu biên | $R'(x)$ | Đạo hàm $R'(x)$ của hàm doanh thu được gọi là hàm doanh thu biên và là tốc độ thay đổi của doanh thu đối với số lượng đơn vị sản phẩm bán ra. | Mục 2, tốc độ thay đổi của doanh thu (trang 38, PDF 40). |
| Hàm lợi nhuận | $P(x) = R(x) - C(x)$ | Nếu $x$ đơn vị được bán, thì tổng lợi nhuận là $P(x) = R(x) - C(x)$ và $P(x)$ được gọi là hàm lợi nhuận. Hàm lợi nhuận biên là đạo hàm $P'(x)$ của hàm lợi nhuận. | Mục 2, hiệu giữa tổng doanh thu và tổng chi phí (trang 38, PDF 40). |
| Hàm lợi nhuận biên | $P'(x) = R'(x) - C'(x)$ | Nếu $x$ đơn vị được bán, thì tổng lợi nhuận là $P(x) = R(x) - C(x)$ và $P(x)$ được gọi là hàm lợi nhuận. Hàm lợi nhuận biên là đạo hàm $P'(x)$ của hàm lợi nhuận. | Mục 2, đạo hàm của hàm lợi nhuận (trang 38, PDF 40). |

## Đã xét, không tạo mục

- tốc độ truyền bệnh — chỉ có trong ví dụ, bài tập: cách gọi khác của tốc độ lây lan virus trong bài toán Vận dụng ở Bài 2

## Ghi chú nguồn cần kiểm tra

Không có ghi chú nguồn mở.
