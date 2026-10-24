# BỘ THUẬT NGỮ TOÁN 12 — KẾT NỐI TRI THỨC VỚI CUỘC SỐNG

## 1. Giới thiệu chung

Bộ thuật ngữ `toan_12` được xây dựng nhằm hệ thống hoá toàn diện, chuẩn xác và chuẩn mực các định nghĩa, định lí, tính chất, quy tắc và công thức toán học thuộc chương trình **Toán lớp 12 — Bộ sách Kết nối tri thức với cuộc sống** (Chương trình Giáo dục phổ thông 2018).

- **Môn học:** Toán học
- **Khối lớp:** 12
- **Mã bộ:** `toan_12`
- **Bộ sách:** Kết nối tri thức với cuộc sống (Nhà xuất bản Giáo dục Việt Nam)
- **Tài liệu nguồn trích xuất:**
  1. `SGK TOAN 12 TAP 1 - KNTT.pdf` (104 trang, Chương I – Chương III, Bài 1 – Bài 10).
  2. `SGK TOAN 12 TAP 2 - KNTT.pdf` (99 trang, Chương IV – Chương VI, Bài 11 – Bài 19).
  3. `SGV TOAN 12 - KNTT.pdf` (246 trang, tài liệu đối chiếu sư phạm, yêu cầu cần đạt và sai lầm thường gặp).
  4. `SCD Toan 12.pdf` (75 trang, dạng ảnh; bổ sung 2026-10-24): Chuyên đề 1 (Bài 1–2: biến ngẫu nhiên rời rạc, phân bố nhị thức), Chuyên đề 2 (Bài 3–4: quy hoạch tuyến tính, bài toán tối ưu bằng đạo hàm), Chuyên đề 3 (Bài 5–7: tiền tệ, lãi suất, tín dụng, đầu tư), `level: chuyen_de`. Thêm 64 thuật ngữ (SCD) và 7 mục `lessons` có `key_terms`; 3 mục SGK (`chi-phi-bien`, `doanh-thu-bien`, `loi-nhuan-bien`) được gộp thêm nguồn SCD PDF 42.
  5. Không có SGV Chuyên đề Toán 12: tệp `SGV CD Toán 12.pdf` từng có trong thư mục là bản trùng của `SGV TOAN 12 - KNTT.pdf` và đã bị người dùng xoá (2026-10-24). Phần chuyên đề (SCD) vì vậy lấy `lessons` từ khung "Kiến thức, kĩ năng" của chính `SCD Toan 12.pdf`.
- **Quy ước trang trích dẫn:**
  - SGK Tập 1, SGK Tập 2: `pdf_page = printed_page + 2`.
  - SGV Toán 12: `pdf_page = printed_page + 1`.
  - SCD Toán 12: `pdf_page = printed_page + 1` (đã đọc chân trang). Bảng tra cứu từ ngữ: PDF 72 (in 71); Bảng giải thích thuật ngữ: PDF 73 (in 72).

---

## 2. Thống kê số lượng thuật ngữ

- **Tổng số thuật ngữ:** **155** (SGK 91 + SCD 64; cập nhật 2026-10-24)
- **Dung lượng tệp dữ liệu:** khoảng **165 KB**
- **Phân bố theo phân loại học thuật (`type`):** (cả hai cấp độ)
  - Định nghĩa (`dinh_nghia`): **74** mục (SGK 40, SCD 34)
  - Công thức (`cong_thuc`): **48** mục (SGK 31, SCD 17)
  - Tính chất (`tinh_chat`): **20** mục (SGK 12, SCD 8)
  - Quy tắc (`quy_tac`): **10** mục (SGK 6, SCD 4)
  - Định lí (`dinh_ly`): **3** mục (SGK 2, SCD 1)
- **Cấp độ (`level`):** `co_ban` 91 mục (SGK), `chuyen_de` 64 mục (SCD). Có 3 mục SGK (`chi-phi-bien`, `doanh-thu-bien`, `loi-nhuan-bien`) được thêm nguồn SCD (PDF 42), vẫn giữ `level: co_ban`.
- **Liên kết thuật ngữ (`related_terms`):** 76/91 mục (83.5%) có liên kết mạng lưới khái niệm hai chiều trong khối 12 và liên thông với các nền tảng Toán 10, Toán 11.

---

## 3. Cấu trúc phân loại theo chương

| STT | Tên chương | Sách nguồn | Số lượng bài | Số lượng thuật ngữ |
| :---: | :--- | :--- | :---: | :---: |
| 1 | **Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số** | SGK Tập 1 | 5 bài (Bài 1–5) | 25 |
| 2 | **Chương II. Vectơ và hệ trục toạ độ trong không gian** | SGK Tập 1 | 3 bài (Bài 6–8) | 18 |
| 3 | **Chương III. Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm** | SGK Tập 1 | 2 bài (Bài 9–10) | 10 |
| 4 | **Chương IV. Nguyên hàm và tích phân** | SGK Tập 2 | 3 bài (Bài 11–13) | 14 |
| 5 | **Chương V. Phương pháp toạ độ trong không gian** | SGK Tập 2 | 4 bài (Bài 14–17) | 16 |
| 6 | **Chương VI. Xác suất có điều kiện** | SGK Tập 2 | 2 bài (Bài 18–19) | 8 |
| | **Tổng SGK** | | **19 bài** | **91** |
| 7 | **Chuyên đề 1. Biến ngẫu nhiên rời rạc. Các số đặc trưng của biến ngẫu nhiên rời rạc** | SCD | 2 bài (Bài 1–2) | 12 |
| 8 | **Chuyên đề 2. Ứng dụng toán học để giải quyết một số bài toán tối ưu** | SCD | 2 bài (Bài 3–4) | 17 |
| 9 | **Chuyên đề 3. Ứng dụng toán học trong một số vấn đề liên quan đến tài chính** | SCD | 3 bài (Bài 5–7) | 35 |
| | **Tổng SCD** | | **7 bài** | **64** |
| | **TỔNG CỘNG** | | **26 bài** | **155** |

Ghi chú: SCD cũng đánh số `Bài 1`–`Bài 7` nên lọc theo bài phải kèm `--level chuyen_de` hoặc `--chapter "Chuyên đề"`. Số mục theo bài SCD: Bài 1: 6; Bài 2: 6; Bài 3: 10; Bài 4: 7; Bài 5: 18; Bài 6: 8; Bài 7: 9. Các số liệu này gồm cả mục chỉ có tên do người trích đặt (đánh dấu trong `notes`).

---

## 4. Yêu cầu cần đạt chuẩn bộ môn (Toán 12)

**Nguồn chuẩn:** khung "Kiến thức, kĩ năng" và cột "Thuật ngữ" đầu mỗi bài của SGK/SCD, đã nhập vào mảng `lessons` (26 mục: 19 SGK + 7 SCD); xem `python glossary/scripts/query.py toan_12 --lessons`. Phần tóm tắt theo chương dưới đây chỉ để tham khảo nhanh, khi ra đề phải đối chiếu `lessons`.

1. **Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số:**
   - Nhận biết tính đồng biến, nghịch biến của hàm số trên một khoảng dựa vào dấu của đạo hàm cấp một.
   - Hiểu rõ khái niệm cực trị (cực đại, cực tiểu), điểm cực trị của hàm số và điểm cực trị của đồ thị hàm số; vận dụng điều kiện cần và điều kiện đủ để tìm cực trị.
   - Tìm giá trị lớn nhất (GTLN) và giá trị nhỏ nhất (GTNN) của hàm số trên một tập hợp số, đặc biệt là trên đoạn $[a; b]$.
   - Hiểu và xác định đường tiệm cận đứng, tiệm cận ngang và tiệm cận xiên của đồ thị hàm số bằng giới hạn.
   - Thực hiện thành thạo sơ đồ khảo sát sự biến thiên và vẽ đồ thị của 3 dạng hàm số cơ bản: hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ ($a \ne 0$), hàm số phân thức hữu tỉ bậc nhất/bậc nhất $y = \frac{ax+b}{cx+d}$ ($c \ne 0, ad - bc \ne 0$) và bậc hai/bậc nhất $y = \frac{ax^2+bx+c}{px+q}$ ($a \ne 0, p \ne 0$).
   - Vận dụng đạo hàm và khảo sát hàm số để giải quyết các bài toán tối ưu hoá thực tế trong kinh tế, kĩ thuật và đời sống.

2. **Vectơ và Hệ trục toạ độ trong không gian:**
   - Mở rộng các khái niệm và phép toán vectơ từ mặt phẳng lên không gian (tổng, hiệu, tích vectơ với một số, tích vô hướng).
   - Nắm vững quy tắc hình hộp để tính tổng ba vectơ xuất phát từ một đỉnh.
   - Xác định góc giữa hai vectơ trong không gian; hiểu điều kiện đồng phẳng của ba vectơ.
   - Thiết lập hệ toạ độ $Oxyz$ trong không gian; tìm toạ độ của điểm và toạ độ của vectơ; áp dụng biểu thức toạ độ của các phép toán vectơ, tính độ dài vectơ, khoảng cách giữa hai điểm và tích vô hướng.

3. **Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm:**
   - Hiểu ý nghĩa và tính được khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu ghép nhóm.
   - Tính phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm; sử dụng các số đặc trưng này để đánh giá, so sánh độ phân tán và độ đồng đều của dữ liệu.

4. **Nguyên hàm và Tích phân:**
   - Hiểu khái niệm nguyên hàm của một hàm số, các tính chất cơ bản của nguyên hàm và bảng nguyên hàm của các hàm số sơ cấp thường gặp.
   - Nắm vững định nghĩa tích phân (công thức Newton-Leibniz: $\int_a^b f(x)dx = F(b) - F(a)$), ý nghĩa hình học (diện tích hình thang cong) và các tính chất cơ bản của tích phân.
   - Vận dụng tích phân để tính diện tích hình phẳng giới hạn bởi đồ thị hàm số và trục hoành, hoặc giữa hai đồ thị hàm số; tính thể tích vật thể và thể tích khối tròn xoay.

5. **Phương pháp toạ độ trong không gian:**
   - Nắm vững khái niệm vectơ pháp tuyến, cặp vectơ chỉ phương của mặt phẳng; lập phương trình tổng quát của mặt phẳng $Ax + By + Cz + D = 0$.
   - Hiểu khái niệm vectơ chỉ phương của đường thẳng; lập phương trình tham số và phương trình chính tắc của đường thẳng trong không gian.
   - Tính góc giữa hai đường thẳng, góc giữa đường thẳng và mặt phẳng, góc giữa hai mặt phẳng.
   - Lập phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$: $(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$ và nhận dạng phương trình tổng quát của mặt cầu.

6. **Xác suất có điều kiện:**
   - Hiểu định nghĩa xác suất có điều kiện $P(A|B) = \frac{P(AB)}{P(B)}$ và ý nghĩa thực tế; tính xác suất có điều kiện bằng công thức, sơ đồ hình cây và bảng dữ liệu thống kê $2 \times 2$.
   - Nắm vững công thức nhân xác suất $P(AB) = P(B)P(A|B) = P(A)P(B|A)$.
   - Vận dụng công thức xác suất toàn phần và công thức Bayes để tính xác suất và cập nhật xác suất tiên nghiệm thành hậu nghiệm trong thực tế y học, kĩ thuật và dự báo.

7. **Chuyên đề học tập (SCD Toán 12, `lessons` có `level: chuyen_de`):**
   - *Chuyên đề 1 (Bài 1–2):* nhận biết biến ngẫu nhiên rời rạc; lập bảng phân bố xác suất; tính kì vọng, phương sai, độ lệch chuẩn và giải thích ý nghĩa; nhận biết phép thử lặp, công thức Bernoulli; nhận biết và vận dụng phân bố nhị thức.
   - *Chuyên đề 2 (Bài 3–4):* vận dụng hệ bất phương trình bậc nhất hai ẩn để giải bài toán quy hoạch tuyến tính; vận dụng đạo hàm và khảo sát hàm số để giải bài toán tối ưu trong thực tiễn và kinh tế.
   - *Chuyên đề 3 (Bài 5–7):* nhận biết vấn đề về tiền tệ, lãi suất; tính lãi đơn, lãi kép, lãi suất thực có tính lạm phát; tính toán về thẻ tín dụng, vay trả góp; đầu tư, niên kim, lập kế hoạch tài chính cá nhân.

---

## 5. Những sai lầm thường gặp của học sinh (Trích từ SGV Toán 12)

Dưới đây là các nhóm sai lầm phổ biến được đúc kết từ hướng dẫn sư phạm trong `SGV TOAN 12 - KNTT.pdf` (cho phần SGK). **Phần chuyên đề (SCD) chưa có mục này** vì thư mục không có SGV Chuyên đề Toán 12.

1. **Nhầm lẫn giữa điểm cực trị của hàm số, giá trị cực trị của hàm số và điểm cực trị của đồ thị hàm số:**
   - *Biểu hiện:* Học sinh hay trả lời "cực đại của hàm số là $(x_0; y_0)$" (lẫn lộn với điểm cực trị của đồ thị), hoặc coi $y_0$ là điểm cực trị thay vì $x_0$.
2. **Ngộ nhận rằng đạo hàm bằng 0 tại đâu thì hàm số đạt cực trị tại đó:**
   - *Biểu hiện:* Kết luận hàm số đạt cực trị tại $x_0$ ngay khi $f'(x_0) = 0$ mà quên kiểm tra đạo hàm có đổi dấu khi qua $x_0$ hay không (ví dụ hàm $y = x^3$ có $y'(0) = 0$ nhưng không đạt cực trị tại $x = 0$).
3. **Nhầm lẫn giữa giá trị cực đại và giá trị lớn nhất:**
   - *Biểu hiện:* Cho rằng giá trị cực đại luôn là giá trị lớn nhất của hàm số trên toàn bộ tập xác định. Thực tế cực trị chỉ mang tính địa phương (trong một lân cận của điểm đó).
4. **Quên kiểm tra điều kiện nghiệm mẫu số khi tìm tiệm cận đứng:**
   - *Biểu hiện:* Với hàm phân thức $y = \frac{P(x)}{Q(x)}$, học sinh vội vàng kết luận mọi nghiệm của mẫu $Q(x) = 0$ đều là tiệm cận đứng mà không kiểm tra xem nghiệm đó có triệt tiêu với tử $P(x)$ hay không (điều kiện $\lim_{x \to x_0} f(x) = \pm\infty$).
5. **Sai lầm trong xác định tiệm cận ngang khi hàm số chứa căn thức:**
   - *Biểu hiện:* Khi đưa $x$ ra ngoài dấu căn bậc hai ở mẫu hoặc tử khi $x \to -\infty$, học sinh quên đổi dấu $\sqrt{x^2} = |x| = -x$, dẫn đến tính sai dấu của giới hạn và bỏ sót một tiệm cận ngang.
6. **Nhầm lẫn quy tắc hình bình hành với quy tắc hình hộp:**
   - *Biểu hiện:* Trong không gian, học sinh cộng ba vectơ $\vec{AB} + \vec{AD} + \vec{AA'}$ thành vectơ đường chéo mặt phẳng thay vì đường chéo hình hộp $\vec{AC'}$.
7. **Bỏ quên dấu giá trị tuyệt đối khi tính diện tích hình phẳng:**
   - *Biểu hiện:* Viết $S = \int_a^b (f(x) - g(x))dx$ thay vì $\int_a^b |f(x) - g(x)|dx$, dẫn đến kết quả diện tích mang giá trị âm khi đồ thị đổi chỗ trên đoạn $[a; b]$.
8. **Nhầm lẫn giữa phương sai mẫu số liệu ghép nhóm và phương sai mẫu số liệu gốc:**
   - *Biểu hiện:* Học sinh quên thay các khoảng bằng giá trị đại diện $c_i = \frac{a_i + a_{i+1}}{2}$ khi tính tổng bình phương độ lệch và chia cho cỡ mẫu.
9. **Nhầm lẫn giữa vectơ chỉ phương và vectơ pháp tuyến trong không gian:**
   - *Biểu hiện:* Khi viết phương trình đường thẳng vuông góc với mặt phẳng $(P)$, học sinh không nhận ra vectơ pháp tuyến $\vec{n}_P$ của mặt phẳng chính là vectơ chỉ phương $\vec{u}_d$ của đường thẳng.
10. **Lẫn lộn thứ tự điều kiện trong xác suất có điều kiện:**
    - *Biểu hiện:* Tính $P(B|A)$ thay vì $P(A|B)$ khi đọc bài toán ngôn ngữ đời thường (ví dụ: "biết người đó bị bệnh, tính xác suất xét nghiệm dương tính" bị nhầm thành "biết xét nghiệm dương tính, tính xác suất người đó bị bệnh").

---

## 6. Quy trình kiểm tra chất lượng

Bộ thuật ngữ `toan_12` đã trải qua quy trình kiểm thử 3 lớp nghiêm ngặt theo quy định:

1. **Kiểm tra cấu trúc và lược đồ (`validate.py`):**
   - Lệnh: `python glossary/scripts/validate.py toan_12`
   - Kết quả (2026-10-20, phần SGK): **OK (91 thuật ngữ, 82.6 KB) — 0 lỗi**. Cập nhật 2026-10-24 sau khi thêm SCD: **OK (155 thuật ngữ, 26 bài YCCĐ) — 0 lỗi**.
   - Toàn bộ các trường dữ liệu bắt buộc (`id`, `term`, `aliases`, `type`, `definition`, `notation`, `chapter`, `lesson`, `level`, `related_terms`, `sources`) đạt chuẩn tuyệt đối; các liên kết `related_terms` đều hợp lệ và tương thích hai chiều.

2. **Đối soát nguồn gốc với trang sách PDF gốc (`check_sources.py`):**
   - Lệnh: `python glossary/scripts/check_sources.py toan_12 --threshold 0.65`
   - Kết quả (2026-10-20, phần SGK): **Tổng: 91 | Đạt: 91 (100%) | Gắn cờ: 0 | Không kiểm tra được: 0 | Cảnh báo: 17**.
   - Cập nhật 2026-10-24 (155 mục): **Đạt 155/155, gắn cờ 0**, 29 cảnh báo tên (mục `cong_thuc`/`quy_tac`/`tinh_chat` do người trích đặt tên). Phần YCCĐ: 26/26 đạt. Sáu mục SCD bị gắn cờ lúc đầu do tên thuật ngữ xuống dòng/OCR (`ki-vong`, `phuong-sai`, `do-lech-chuan`, `phuong-an-cuc-bien`, `tien-von`, `vay-tra-gop`) đã được chuẩn hoá `term`/`aliases` theo đúng cách sách ghi.
   - Mọi định nghĩa toán học đều được đối chiếu trực tiếp qua lớp OCR tiếng Việt với các trang sách giáo khoa nguồn (đạt tỉ lệ bigram $\ge 0.65$). 17 cảnh báo thuộc về các công thức/tính chất có tiêu đề thuật ngữ mở rộng ngữ nghĩa theo chuẩn hệ thống.

3. **Kiểm định độc lập mẫu ngẫu nhiên (`query.py --audit`):**
   - Lệnh: `python glossary/scripts/query.py toan_12 --audit`
   - File xuất: `glossary/khoi_12/toan_12/sample_audit.md` (30 mục gồm 20 mục ngẫu nhiên và 10 mục công thức/kí hiệu toán học).
   - Kết quả kiểm định đối chiếu: **Đạt 30/30 mục (100% chính xác, 0 sai sót)** về cả số trang in, số trang PDF, công thức LaTeX và nội dung định nghĩa bám sát sách giáo khoa.

---

## 7. Hướng dẫn sử dụng và mở rộng

- **Truy vấn thuật ngữ:**
  ```powershell
  python glossary/scripts/query.py toan_12 "nguyên hàm"
  python glossary/scripts/query.py toan_12 "tích phân"
  python glossary/scripts/query.py toan_12 --id toan-12-xac-suat-co-dieu-kien
  ```
- **Kiểm tra hợp lệ:**
  ```powershell
  python glossary/scripts/validate.py toan_12
  python glossary/scripts/check_sources.py toan_12
  ```

---

## 8. Kiểm định mẫu phần Chuyên đề học tập (SCD) — 2026-10-24

Phần SCD (64 mục) được kiểm định riêng, do cùng phiên trích xuất:

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 26 mục lấy mẫu ngẫu nhiên (`query.py --level chuyen_de --sample 26 --seed 2026`), gồm công thức Bernoulli, độ lệch chuẩn, các phương án, hàm lợi nhuận, lãi đơn, lãi kép, lạm phát, sức mua, phí thẻ, vay trả góp, niên kim, giá trị hiện tại,... |
| Cách đối chiếu | (1) So từng từ của `definition` với OCR của trang nguồn và hai trang kề cho cả 64 mục (chỉ 2 mục lệch do nhiễu OCR: `ti-le-lam-phat`, `lai-suat-danh-nghia`). (2) Đọc lại ảnh trang nguồn PDF 16, 62, 64 (và 50, 51 khi trích) để so công thức LaTeX: công thức Bernoulli, lãi suất và thời gian khoản đầu tư (căn bậc $N$, lôgarit cơ số $1 + r/n$), giá trị hiện tại (số mũ $-nt$). (3) Số trang in = trang PDF − 1 đối chiếu bằng chân trang |
| Số mục sai nội dung | 0 |
| Kiểm tra độc lập | Chưa làm (cùng một phiên đọc và đối chiếu) |
| Mục không kiểm thử trực tiếp | 3 mục SGK được thêm nguồn SCD PDF 42 (`chi-phi-bien`, `doanh-thu-bien`, `loi-nhuan-bien`) |

Hạn chế đã biết của phần SCD: (a) một số mục (`cac-buoc-giai-quy-hoach-tuyen-tinh`, `cac-buoc-giai-bai-toan-toi-uu`, `kenh-dau-tu-pho-bien`, `chuc-nang-cua-tien-te`, `tinh-chat-cua-tien-te`,...) có tên do người trích đặt cho một đoạn có cấu trúc rõ ràng trong sách; `definition` giữ nguyên văn đoạn đó nhưng lược các ví dụ. (b) `definition` các mục dài (chức năng thẻ tín dụng, các kênh đầu tư) là bản lược theo ý chính của từng gạch đầu dòng. Agent ra đề **không** nên dùng làm đáp án các mục có `notes`.
