---
name: tu-dien-toan-11-chuong-5
description: Từ điển thuật ngữ Toán 11 Chương V — Giới hạn. Hàm số liên tục (bộ Kết nối tri thức với cuộc sống).
loai_hoc_lieu: tu_dien_thuat_ngu
mon: Toán
lop: 11
chuong: "Chương V. Giới hạn. Hàm số liên tục"
bai_so: "Bài 15 – Bài 17"
nguon: "SGK Toán 11 Tập 1 – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)"
ngay_tao: "2026-11-06"
ngay_cap_nhat: "2026-11-06"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ TOÁN 11 — CHƯƠNG V: GIỚI HẠN. HÀM SỐ LIÊN TỤC

## Quy ước sử dụng

- **Phạm vi:** Chương V (Bài 15 đến Bài 17, Bài tập cuối chương V và 2 bài Hoạt động thực hành trải nghiệm cuối Tập 1), SGK Toán 11 Tập 1 (bộ Kết nối tri thức với cuộc sống), tích hợp 4 mục tương ứng trong Bảng giải thích thuật ngữ cuối Tập 1 (trang in 131, PDF 132).
- **Cấu trúc bảng 4 cột:** `Thuật ngữ` | `Tiếng Anh` | `Giải nghĩa` | `Bối cảnh sử dụng`.
- **Phân loại nguồn:**
  - *Định nghĩa trực tiếp trong nguồn:* bám sát nguyên văn khung kiến thức trọng tâm, chú ý định nghĩa hoặc bảng giải thích thuật ngữ cuối sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* tổng hợp từ đoạn văn/nhận xét/quy tắc gắn nhãn `<!-- term: ... -->` ở bài học Tầng 1.

## Bài 15: Giới hạn của dãy số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Dãy số có giới hạn là $0$ (có giới hạn là $0$) | $\lim_{n \to +\infty} u_n = 0$ | Ta nói dãy số $(u_n)$ có giới hạn là $0$ khi $n$ dần tới dương vô cực, nếu $\lvert u_n \rvert$ có thể nhỏ hơn một số dương bé tuỳ ý, kể từ một số hạng nào đó trở đi, kí hiệu $\lim_{n \to +\infty} u_n = 0$ hay $u_n \to 0$ khi $n \to +\infty$. | Mục 1, khái niệm dãy số có giới hạn là $0$ (trang 105, PDF 106). |
| Một số giới hạn cơ bản bằng 0 | — | Từ định nghĩa dãy số có giới hạn $0$, ta có các kết quả sau: $\lim_{n \to +\infty} \dfrac{1}{n^k} = 0$ với $k$ là một số nguyên dương; $\lim_{n \to +\infty} q^n = 0$ nếu $\lvert q \rvert < 1$; nếu $\lvert u_n \rvert \le v_n$ với mọi $n \ge 1$ và $\lim_{n \to +\infty} v_n = 0$ thì $\lim_{n \to +\infty} u_n = 0$. | [mô tả] Mục 1, chú ý các giới hạn cơ bản bằng $0$ (trang 105, PDF 106). |
| Dãy số có giới hạn hữu hạn (có giới hạn là số thực $a$) | $\lim_{n \to +\infty} u_n = a$ | Ta nói dãy số $(u_n)$ có giới hạn là số thực $a$ khi $n$ dần tới dương vô cực nếu $\lim_{n \to +\infty} (u_n - a) = 0$, kí hiệu $\lim_{n \to +\infty} u_n = a$ hay $u_n \to a$ khi $n \to +\infty$. | Mục 1, khái niệm dãy số có giới hạn hữu hạn (trang 105, PDF 106). |
| Định lí về giới hạn hữu hạn của dãy số | — | Tổng quát, ta có các quy tắc tính giới hạn sau đây: a) Nếu $\lim_{n \to +\infty} u_n = a$ và $\lim_{n \to +\infty} v_n = b$ thì $\lim_{n \to +\infty} (u_n + v_n) = a + b$; $\lim_{n \to +\infty} (u_n - v_n) = a - b$; $\lim_{n \to +\infty} (u_n \cdot v_n) = a \cdot b$; $\lim_{n \to +\infty} \dfrac{u_n}{v_n} = \dfrac{a}{b}$ (nếu $b \ne 0$). b) Nếu $u_n \ge 0$ với mọi $n$ và $\lim_{n \to +\infty} u_n = a$ thì $a \ge 0$ và $\lim_{n \to +\infty} \sqrt{u_n} = \sqrt{a}$. | [mô tả] Mục 2, các phép toán giới hạn hữu hạn của dãy số (trang 106, PDF 107). |
| Cấp số nhân lùi vô hạn | $\lvert q \rvert < 1$ | Cấp số nhân vô hạn $(u_n)$ có công bội $q$ với $\lvert q \rvert < 1$ được gọi là cấp số nhân lùi vô hạn. | Mục 3 (trang 107, PDF 108) và Bảng giải thích thuật ngữ (trang 131, PDF 132). |
| Tổng của cấp số nhân lùi vô hạn | $S = \dfrac{u_1}{1 - q}$ | Giới hạn $\lim_{n \to +\infty} S_n = \dfrac{u_1}{1 - q}$ được gọi là tổng của cấp số nhân lùi vô hạn $(u_n)$, và kí hiệu là $S = u_1 + u_2 + \dots + u_n + \dots$ | Mục 3, công thức tính tổng của cấp số nhân lùi vô hạn (trang 107, PDF 108). |
| Dãy số có giới hạn dương vô cực (có giới hạn $+\infty$) | $\lim_{n \to +\infty} u_n = +\infty$ | Dãy số $(u_n)$ được gọi là có giới hạn $+\infty$ khi $n \to +\infty$ nếu $u_n$ có thể lớn hơn một số dương bất kì, kể từ một số hạng nào đó trở đi, kí hiệu $\lim_{n \to +\infty} u_n = +\infty$ hay $u_n \to +\infty$ khi $n \to +\infty$. | Mục 4, định nghĩa giới hạn vô cực của dãy số (trang 108, PDF 109). |
| Dãy số có giới hạn âm vô cực (có giới hạn $-\infty$) | $\lim_{n \to +\infty} u_n = -\infty$ | Dãy số $(u_n)$ được gọi là có giới hạn $-\infty$ khi $n \to +\infty$ nếu $\lim_{n \to +\infty} (-u_n) = +\infty$, kí hiệu $\lim_{n \to +\infty} u_n = -\infty$ hay $u_n \to -\infty$ khi $n \to +\infty$. | Mục 4, định nghĩa giới hạn vô cực của dãy số (trang 108, PDF 109). |
| Quy tắc tính giới hạn vô cực của dãy số | — | Liên quan đến giới hạn vô cực của dãy số, ta có một số quy tắc sau đây: Nếu $\lim_{n \to +\infty} u_n = a$ và $\lim_{n \to +\infty} v_n = +\infty$ (hoặc $\lim_{n \to +\infty} v_n = -\infty$) thì $\lim_{n \to +\infty} \dfrac{u_n}{v_n} = 0$. Nếu $\lim_{n \to +\infty} u_n = a > 0$, $\lim_{n \to +\infty} v_n = 0$ và $v_n > 0$ với mọi $n$ thì $\lim_{n \to +\infty} \dfrac{u_n}{v_n} = +\infty$. Nếu $\lim_{n \to +\infty} u_n = +\infty$ và $\lim_{n \to +\infty} v_n = a > 0$ thì $\lim_{n \to +\infty} u_nv_n = +\infty$. | [mô tả] Mục 4, quy tắc tìm giới hạn vô cực của dãy số (trang 109, PDF 110). |
| Tỉ lệ vàng | golden ratio ($r = \dfrac{1 + \sqrt{5}}{2}$) | Đây chính là tỉ lệ vàng (golden ratio) được sử dụng trong kiến trúc, hội hoạ, tôn giáo, ... Dãy Fibonacci và tỉ lệ vàng cũng xuất hiện nhiều trong thế giới tự nhiên. | Mục Em có biết?, liên hệ giữa giới hạn dãy tỉ số Fibonacci và tỉ lệ vàng (trang 110, PDF 111). |
| Dãy logistic | $p_{n+1} = kp_n(1 - p_n)$ | Trong sinh thái học, người ta sử dụng dãy $(p_n)$ cho bởi công thức truy hồi $p_{n+1} = kp_n(1 - p_n)$ để mô phỏng hệ sinh thái của một loài (động vật hoặc thực vật), trong đó $p_n$ là tỉ lệ giữa số lượng cá thể theo thời gian và sức chứa của môi trường, $k$ là hệ số phụ thuộc đặc điểm của loài và điều kiện môi trường. Dãy số này được gọi là dãy logistic, do nhà sinh học Robert May đưa ra năm 1976. | Mục Em có biết?, ứng dụng giới hạn dãy số trong sinh thái học (trang 110, PDF 111). |

## Bài 16: Giới hạn của hàm số

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Giới hạn hữu hạn của hàm số tại một điểm (giới hạn) | $\lim_{x \to x_0} f(x) = L$ | Giả sử $(a; b)$ là một khoảng chứa điểm $x_0$ và hàm số $y = f(x)$ xác định trên khoảng $(a; b)$, có thể trừ điểm $x_0$. Ta nói hàm số $f(x)$ có giới hạn là số $L$ khi $x$ dần tới $x_0$ nếu với dãy số $(x_n)$ bất kì, $x_n \in (a; b), x_n \ne x_0$ và $x_n \to x_0$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0} f(x) = L$ hay $f(x) \to L$ khi $x \to x_0$. | Mục 1, định nghĩa giới hạn hữu hạn của hàm số tại một điểm (trang 111, PDF 112). |
| Quy tắc tính giới hạn của hàm số tại một điểm | — | Tương tự đối với dãy số, ta có các quy tắc tính giới hạn của hàm số tại một điểm như sau: a) Nếu $\lim_{x \to x_0} f(x) = L$ và $\lim_{x \to x_0} g(x) = M$ thì $\lim_{x \to x_0} [f(x) + g(x)] = L + M$; $\lim_{x \to x_0} [f(x) - g(x)] = L - M$; $\lim_{x \to x_0} [f(x) \cdot g(x)] = L \cdot M$; $\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = \dfrac{L}{M}$, nếu $M \ne 0$. b) Nếu $f(x) \ge 0$ với mọi $x \in (a; b) \setminus \{x_0\}$ và $\lim_{x \to x_0} f(x) = L$ thì $L \ge 0$ và $\lim_{x \to x_0} \sqrt{f(x)} = \sqrt{L}$. | [mô tả] Mục 1, các phép toán giới hạn hữu hạn của hàm số tại một điểm (trang 112, PDF 113). |
| Giới hạn một bên của hàm số tại một điểm | $\lim_{x \to x_0^+} f(x), \lim_{x \to x_0^-} f(x)$ | Giới hạn bên phải hoặc giới hạn bên trái của hàm số tại một điểm. | Mục 1 (trang 113, PDF 114) và Bảng giải thích thuật ngữ (trang 131, PDF 132). |
| Giới hạn bên phải | $\lim_{x \to x_0^+} f(x) = L$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(x_0; b)$. Ta nói số $L$ là giới hạn bên phải của $f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì thoả mãn $x_0 < x_n < b$ và $x_n \to x_0$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^+} f(x) = L$. | Mục 1, định nghĩa giới hạn bên phải của hàm số tại một điểm (trang 113, PDF 114). |
| Giới hạn bên trái | $\lim_{x \to x_0^-} f(x) = L$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(a; x_0)$. Ta nói số $L$ là giới hạn bên trái của $f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì thoả mãn $a < x_n < x_0$ và $x_n \to x_0$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^-} f(x) = L$. | Mục 1, định nghĩa giới hạn bên trái của hàm số tại một điểm (trang 113, PDF 114). |
| Giới hạn hữu hạn của hàm số khi $x \to +\infty$ (có giới hạn là số $L$ khi $x \to +\infty$) | $\lim_{x \to +\infty} f(x) = L$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(a; +\infty)$. Ta nói hàm số $f(x)$ có giới hạn là số $L$ khi $x \to +\infty$ nếu với dãy số $(x_n)$ bất kì, $x_n > a$ và $x_n \to +\infty$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to +\infty} f(x) = L$ hay $f(x) \to L$ khi $x \to +\infty$. | Mục 2, định nghĩa giới hạn hữu hạn của hàm số tại dương vô cực (trang 114, PDF 115). |
| Giới hạn hữu hạn của hàm số khi $x \to -\infty$ (có giới hạn là số $L$ khi $x \to -\infty$) | $\lim_{x \to -\infty} f(x) = L$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(-\infty; b)$. Ta nói hàm số $f(x)$ có giới hạn là số $L$ khi $x \to -\infty$ nếu với dãy số $(x_n)$ bất kì, $x_n < b$ và $x_n \to -\infty$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to -\infty} f(x) = L$ hay $f(x) \to L$ khi $x \to -\infty$. | Mục 2, định nghĩa giới hạn hữu hạn của hàm số tại âm vô cực (trang 114, PDF 115). |
| Quy tắc tính giới hạn hữu hạn của hàm số tại vô cực | — | Các quy tắc tính giới hạn hữu hạn tại một điểm cũng đúng cho giới hạn hữu hạn tại vô cực. Với $c$ là hằng số, ta có: $\lim_{x \to +\infty} c = c$, $\lim_{x \to -\infty} c = c$. Với $k$ là một số nguyên dương, ta có: $\lim_{x \to +\infty} \dfrac{1}{x^k} = 0$, $\lim_{x \to -\infty} \dfrac{1}{x^k} = 0$. | [mô tả] Mục 2, các giới hạn cơ bản và quy tắc tính giới hạn tại vô cực (trang 114, PDF 115). |
| Giới hạn dương vô cực của hàm số tại một điểm (có giới hạn $+\infty$ khi $x \to x_0$) | $\lim_{x \to x_0} f(x) = +\infty$ | Giả sử khoảng $(a; b)$ chứa $x_0$ và hàm số $y = f(x)$ xác định trên $(a; b) \setminus \{x_0\}$. Ta nói hàm số $f(x)$ có giới hạn $+\infty$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì, $x_n \in (a; b) \setminus \{x_0\}, x_n \to x_0$, ta có $f(x_n) \to +\infty$, kí hiệu $\lim_{x \to x_0} f(x) = +\infty$. | Mục 3a, định nghĩa giới hạn vô cực của hàm số tại một điểm (trang 115, PDF 116). |
| Giới hạn âm vô cực của hàm số tại một điểm (có giới hạn $-\infty$ khi $x \to x_0$) | $\lim_{x \to x_0} f(x) = -\infty$ | Ta nói hàm số $f(x)$ có giới hạn $-\infty$ khi $x \to x_0$, kí hiệu $\lim_{x \to x_0} f(x) = -\infty$, nếu $\lim_{x \to x_0} [-f(x)] = +\infty$. | Mục 3a, định nghĩa giới hạn vô cực của hàm số tại một điểm (trang 115, PDF 116). |
| Giới hạn vô cực một bên phải (có giới hạn $+\infty$ khi $x \to x_0$ về bên phải) | $\lim_{x \to x_0^+} f(x) = +\infty$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(x_0; b)$. Ta nói hàm số $f(x)$ có giới hạn $+\infty$ khi $x \to x_0$ về bên phải nếu với dãy số $(x_n)$ bất kì thoả mãn $x_0 < x_n < b, x_n \to x_0$, ta có $f(x_n) \to +\infty$, kí hiệu $\lim_{x \to x_0^+} f(x) = +\infty$. | Mục 3a, định nghĩa giới hạn vô cực một bên (trang 116, PDF 117). |
| Giới hạn vô cực một bên trái (có giới hạn $+\infty$ khi $x \to x_0$ về bên trái) | $\lim_{x \to x_0^-} f(x) = +\infty$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(a; x_0)$. Ta nói hàm số $f(x)$ có giới hạn $+\infty$ khi $x \to x_0$ về bên trái nếu với dãy số $(x_n)$ bất kì thoả mãn $a < x_n < x_0, x_n \to x_0$, ta có $f(x_n) \to +\infty$, kí hiệu $\lim_{x \to x_0^-} f(x) = +\infty$. | Mục 3a, định nghĩa giới hạn vô cực một bên (trang 116, PDF 117). |
| Quy tắc tìm giới hạn của tích và thương khi có giới hạn vô cực | — | Ta có một số quy tắc tính giới hạn của tích và thương hai hàm số khi một trong hai hàm số đó có giới hạn vô cực. | [mô tả] Mục 3b, quy tắc tìm giới hạn vô cực của tích $f(x)g(x)$ và thương $\dfrac{f(x)}{g(x)}$ (trang 117, PDF 118). |

## Bài 17: Hàm số liên tục

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Hàm số liên tục tại một điểm (liên tục tại điểm) | $\lim_{x \to x_0} f(x) = f(x_0)$ | Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa điểm $x_0$. Hàm số $f(x)$ được gọi là liên tục tại điểm $x_0$ nếu $\lim_{x \to x_0} f(x) = f(x_0)$. | Mục 1, định nghĩa hàm số liên tục tại một điểm (trang 119, PDF 120). |
| Hàm số gián đoạn tại một điểm (gián đoạn) | — | Hàm số không liên tục tại điểm đó; hàm số $f(x)$ không liên tục tại $x_0$ được gọi là gián đoạn tại điểm đó. | Mục 1 (trang 119, PDF 120) và Bảng giải thích thuật ngữ (trang 131, PDF 132). |
| Hàm dấu | $s(x)$ | Xét tính liên tục của hàm dấu $s(x) = \begin{cases} 1 & \text{nếu } x > 0 \\ 0 & \text{nếu } x = 0 \\ -1 & \text{nếu } x < 0 \end{cases}$ tại điểm $x_0 = 0$. | Mục 1, Ví dụ 2 minh hoạ hàm số gián đoạn tại điểm $x_0 = 0$ (trang 120, PDF 121). |
| Hàm số liên tục trên một khoảng (liên tục trên khoảng) | — | Hàm số $y = f(x)$ được gọi là liên tục trên khoảng $(a; b)$ nếu nó liên tục tại mọi điểm thuộc khoảng này. | Mục 2, định nghĩa hàm số liên tục trên một khoảng (trang 120, PDF 121). |
| Hàm số liên tục trên đoạn $[a; b]$ (liên tục trên đoạn) | — | Hàm số liên tục tại mọi điểm của khoảng $(a; b)$, liên tục phải tại điểm $a$ và liên tục trái tại điểm $b$; hàm số $y = f(x)$ được gọi là liên tục trên đoạn $[a; b]$ nếu nó liên tục trên khoảng $(a; b)$ và $\lim_{x \to a^+} f(x) = f(a)$, $\lim_{x \to b^-} f(x) = f(b)$. | Mục 2 (trang 120, PDF 121) và Bảng giải thích thuật ngữ (trang 131, PDF 132). |
| Tính liên tục của các hàm số sơ cấp cơ bản | — | Về tính liên tục của các hàm số sơ cấp cơ bản đã biết, ta có: Hàm số đa thức và các hàm số $y = \sin x, y = \cos x$ liên tục trên $\mathbb{R}$. Các hàm số $y = \tan x, y = \cot x, y = \sqrt{x}$ và hàm phân thức hữu tỉ (thương của hai đa thức) liên tục trên tập xác định của chúng. | [mô tả] Mục 2, tính chất liên tục của các hàm số sơ cấp cơ bản trên tập xác định (trang 121, PDF 122). |
| Tính liên tục của tổng, hiệu, tích và thương hai hàm số liên tục | — | Ta có khẳng định sau đây về tổng, hiệu, tích và thương của hai hàm số liên tục. Giả sử hai hàm số $y = f(x)$ và $y = g(x)$ liên tục tại điểm $x_0$. Khi đó: a) Các hàm số $y = f(x) + g(x)$, $y = f(x) - g(x)$ và $y = f(x)g(x)$ liên tục tại $x_0$; b) Hàm số $y = \dfrac{f(x)}{g(x)}$ liên tục tại $x_0$ nếu $g(x_0) \ne 0$. | [mô tả] Mục 3, tính chất liên tục của các phép toán trên hàm số (trang 121, PDF 122). |
| Định lí giá trị trung gian của hàm số liên tục trên đoạn | $f(a)f(b) < 0 \Rightarrow \exists c \in (a; b), f(c) = 0$ | Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a)f(b) < 0$ thì tồn tại ít nhất một điểm $c \in (a; b)$ sao cho $f(c) = 0$. | [mô tả] Mục 3, nhận xét ứng dụng chứng minh sự tồn tại nghiệm của phương trình (trang 122, PDF 123). |

## Thuật ngữ dùng chung

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Niên kim | — | Niên kim là một khoản tiền được trả bằng các khoản thanh toán đều đặn. Thanh toán thường được thực hiện vào cuối khoảng thời gian thanh toán. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 1 (trang 126, PDF 127). |
| Số tiền của một niên kim (số tiền của niên kim) | $A_f = R\dfrac{(1 + i)^n - 1}{i}$ | Số tiền của một niên kim là tổng của tất cả các khoản thanh toán riêng lẻ từ thời điểm thanh toán đầu tiên cho đến khi thanh toán cuối cùng được thực hiện, cùng với tất cả tiền lãi. Số tiền $A_f$ của một niên kim bao gồm $n$ khoản thanh toán đều đặn bằng nhau và bằng $R$ với lãi suất $i$ trong mỗi khoảng thời gian được cho bởi $A_f = R\dfrac{(1 + i)^n - 1}{i}$. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 1 (trang 126, PDF 127). |
| Tiền thuê định kì | $R$ | Nói chung, khoản thanh toán theo niên kim được gọi là tiền thuê định kì và kí hiệu là $R$. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 1 (trang 126, PDF 127). |
| Giá trị hiện tại | — | Đây là số tiền, cùng với tiền lãi, sẽ trị giá $100$ triệu đồng trong $5$ năm tới. Số tiền này được gọi là giá trị hiện tại. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 2 (trang 126, PDF 127). |
| Giá trị hiện tại của một niên kim | $A_p = R\dfrac{1 - (1 + i)^{-n}}{i}$ | Giá trị hiện tại của một niên kim bao gồm $n$ khoản thanh toán đều đặn bằng nhau và bằng $R$ với lãi suất $i$ trong mỗi khoảng thời gian được cho bởi $A_p = R\dfrac{1 - (1 + i)^{-n}}{i}$. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 2 (trang 127, PDF 128). |
| Trả góp | — | Trả góp là phương thức cho vay tiền mà các kì trả nợ gốc và lãi trùng nhau. Số tiền trả nợ của mỗi kì là bằng nhau theo thoả thuận và số lãi được tính dựa trên số dư nợ gốc và thời hạn thực tế của kì hạn trả nợ. Trả góp còn áp dụng trong việc cho vay tiêu dùng, mua tài sản giá trị lớn như nhà đất, ô tô, ... | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 3 (trang 127, PDF 128). |
| Mua trả góp | $R = \dfrac{iA_p}{1 - (1 + i)^{-n}}$ | Nếu một khoản vay $A_p$ phải được hoàn trả trong $n$ lần thanh toán đều đặn bằng nhau với lãi suất $i$ trong mỗi khoảng thời gian thì số tiền $R$ của mỗi khoản thanh toán là $R = \dfrac{iA_p}{1 - (1 + i)^{-n}}$. | Hoạt động thực hành trải nghiệm: Một vài áp dụng của Toán học trong tài chính, Mục 3 (trang 127, PDF 128). |
| Lực căng bề mặt | — | Nước cũng như các chất lỏng đều có lực căng bề mặt hình thành do sự tương tác giữa các phân tử của chất lỏng. Sẽ rất khó để thổi bong bóng từ nước do lực căng bề mặt của nước lớn. Tuy nhiên, nếu pha thêm xà phòng vào nước việc này sẽ được thực hiện do xà phòng làm giảm lực này của nước. Lực càng yếu bong bóng càng lớn. | [mô tả] Hoạt động thực hành trải nghiệm: Lực căng mặt ngoài của nước, Mở đầu (trang 128, PDF 129). |

## Đã xét, không tạo mục

- Nghịch lí Zeno. — chỉ có trong ví dụ, bài tập: tên bài toán mở đầu Bài 15 về Achilles đuổi rùa
- tổng — gộp vào Tổng của cấp số nhân lùi vô hạn: cụm tách tự động trước chữ của trong câu định nghĩa tổng của cấp số nhân lùi vô hạn ở Mục 3 Bài 15
- Giới hạn vô cực — tiêu đề, không phải thuật ngữ: tiêu đề mục con 3a trong Bài 16
- Một số quy tắc tính giới hạn vô cực — tiêu đề, không phải thuật ngữ: tiêu đề mục con 3b trong Bài 16

## Ghi chú nguồn cần kiểm tra

Không có ghi chú nguồn mở.
