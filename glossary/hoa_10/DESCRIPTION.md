# Bộ thuật ngữ `hoa_10` — Hoá học 10 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/hoa_10/hoa_10.json`, gồm **194 thuật ngữ** (cập nhật 2026-10-15). Truy vấn bằng `query.py`; không nạp cả file.

## 1. Phạm vi

Nguồn: thư mục `hoa_10/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK Hoa hoc 10.pdf | sgk | 122 | Nguồn chính, Mở đầu + Chương 1–7 (23 bài), `level: co_ban` | Không (ảnh, OCR) |
| SCD Hoa hoc 10.pdf | scd | 78 | Chuyên đề 1–3 (11 bài), `level: chuyen_de` | Không (ảnh, OCR) |
| SGV HOA HOC 10.pdf | gv | 154 | Mục tiêu từng bài, thông tin bổ sung, lưu ý giảng dạy (mục 4–5); nguồn `gv` cho 22 thuật ngữ | Không (ảnh, OCR) |
| SGV CD HOA HOC 10.pdf | gv | 98 | Mục tiêu từng bài chuyên đề, lưu ý (mục 4–5); nguồn `gv` cho 4 thuật ngữ | Không (ảnh, OCR) |
| SBT HOA HOC 10.pdf | sbt | 130 | Chỉ gồm câu hỏi, bài tập (PDF 5–75) và đáp án (PDF 76–128); **không có khái niệm mới** → 0 mục | Không (ảnh, OCR) |
| Tài liệu bồi dưỡng GV môn Hóa học 10.pdf | gv | 57 | So sánh CT 2006 – 2018, thời lượng, cấu trúc SGK, chuyên đề (mục 4) | Có (đọc trực tiếp) |

- Ở năm sách dạng ảnh: **trang PDF = trang in + 1**. Tài liệu bồi dưỡng GV: trang PDF = trang in.
- SGK có phần **Mở đầu** (PDF 7–12) không đánh số bài: `chapter` = `lesson` = `Mở đầu`.
- SGK (trang in 119, PDF 120) có bảng "Giải thích một số thuật ngữ dùng trong sách" (15 mục). Cả 15 đều có trong glossary; 14 mục mang nguồn trang bảng. `tinh-the`, `pho-khoi-luong` và `nhiet-luong-ke` dùng câu định nghĩa của bảng. `lien-ket-cho-nhan` chỉ giữ nguồn thân bài vì OCR trang bảng đọc sai tên (`check_sources` không khớp được); nội dung bảng và thân bài trùng nhau.
- SCD (trang in 75, PDF 76) có bảng thuật ngữ (9 mục), đều có trong glossary; 8 mục mang nguồn PDF 76. `phong-xa` và `trang-thai-can-bang` lấy định nghĩa từ bảng vì thân bài không phát biểu tường minh. OCR mặc định trang bảng của SGK và SCD kém, nên cache `.ocr/` của hai trang này được nối thêm bản OCR 400 dpi (psm 4).
- Các bài **Ôn tập** (Bài 4, 9, 14, 16, 18, 20, 23) chỉ hệ thống hoá và luyện tập → 0 mục. Chuyên đề 3 (Bài 9, 10) là hướng dẫn thao tác phần mềm → 0 mục; Bài 11 chỉ lấy 4 khái niệm nền của hoá học tính toán.
- Nhiều mục `tinh_chat` lấy nguyên các bảng số liệu trong SGK (Bảng 1.1 hạt cơ bản, Bảng 7.2 tính acid – base, Bảng 12.1 hiệu độ âm điện, Bảng 21.2–21.3 halogen, Bảng 22.2 nhiệt độ sôi HX), đã đối chiếu ảnh.
- SGK và SCD đều đánh số "Bài 1, 2, …". Khi lọc, kết hợp `--level` hoặc `--chapter`. Ví dụ: `--lesson "Bài 1." --level co_ban` là "Thành phần của nguyên tử"; `--lesson "Bài 1." --level chuyen_de` là "Liên kết hoá học" (Chuyên đề).

## 2. Chương/bài và số thuật ngữ

Bài không liệt kê (các bài Ôn tập, Chuyên đề Bài 9–10) có 0 mục. SBT không bổ sung mục nào.

| Chương / Chuyên đề | Bài | Số mục |
|---|---|---|
| Mở đầu | Mở đầu | 4 |
| Chương 1. Cấu tạo nguyên tử | Bài 1. Thành phần của nguyên tử | 9 |
|  | Bài 2. Nguyên tố hoá học | 8 |
|  | Bài 3. Cấu trúc lớp vỏ electron nguyên tử | 13 |
| Chương 2. Bảng tuần hoàn các nguyên tố hoá học và định luật tuần hoàn | Bài 5. Cấu tạo của bảng tuần hoàn các nguyên tố hoá học | 8 |
|  | Bài 6. Xu hướng biến đổi một số tính chất của nguyên tử các nguyên tố trong một chu kì và trong một nhóm | 9 |
|  | Bài 7. Xu hướng biến đổi thành phần và một số tính chất của hợp chất trong một chu kì | 2 |
|  | Bài 8. Định luật tuần hoàn. Ý nghĩa của bảng tuần hoàn các nguyên tố hoá học | 2 |
| Chương 3. Liên kết hoá học | Bài 10. Quy tắc octet | 3 |
|  | Bài 11. Liên kết ion | 8 |
|  | Bài 12. Liên kết cộng hoá trị | 11 |
|  | Bài 13. Liên kết hydrogen và tương tác van der Waals | 6 |
| Chương 4. Phản ứng oxi hoá – khử | Bài 15. Phản ứng oxi hoá – khử | 9 |
| Chương 5. Năng lượng hoá học | Bài 17. Biến thiên enthalpy trong các phản ứng hoá học | 12 |
| Chương 6. Tốc độ phản ứng | Bài 19. Tốc độ phản ứng | 13 |
| Chương 7. Nguyên tố nhóm halogen | Bài 21. Nhóm halogen | 11 |
|  | Bài 22. Hydrogen halide. Muối halide | 5 |
| Chuyên đề 1. Cơ sở hoá học | Bài 1. Liên kết hoá học | 10 |
|  | Bài 2. Phản ứng hạt nhân | 14 |
|  | Bài 3. Năng lượng hoạt hoá của phản ứng hoá học | 3 |
|  | Bài 4. Entropy và biến thiên năng lượng tự do Gibbs | 5 |
| Chuyên đề 2. Hoá học trong việc phòng chống cháy, nổ | Bài 5. Sơ lược về phản ứng cháy, nổ | 8 |
|  | Bài 6. Điểm chớp cháy. Nhiệt độ ngọn lửa. Nhiệt độ tự bốc cháy | 4 |
|  | Bài 7. Hoá học về phản ứng cháy, nổ | 4 |
|  | Bài 8. Phòng chống cháy, nổ | 9 |
| Chuyên đề 3. Thực hành hoá học và công nghệ thông tin | Bài 11. Thực hành tính tham số cấu trúc và năng lượng | 4 |

Một khái niệm có ở cả SGK và SCD được **gộp vào mục SGK** và thêm nguồn `scd` (4 mục: `cong-thuc-lewis`, `nang-luong-hoat-hoa`, `chat-xuc-tac`, `phan-ung-chay`). Định nghĩa giữ theo SGK. Phần mở rộng ở SCD được tách thành mục riêng `chuyen_de`, ví dụ `phuong-trinh-arrhenius`, `dac-diem-chat-xuc-tac`, `dac-diem-phan-ung-chay`.

## 3. Thống kê theo `type`, `level`, nguồn

| type | Số mục |
|---|---|
| dinh_nghia | 111 |
| tinh_chat | 45 |
| quy_tac | 18 |
| cong_thuc | 10 |
| ky_hieu | 7 |
| dinh_ly | 3 |

- Theo `level`: `co_ban` 133, `chuyen_de` 61.
- Theo nguồn định nghĩa: SGK 133, SCD 61, SBT 0. 26 mục mang thêm nguồn `gv` (22 từ SGV, 4 từ SGV CD); định nghĩa vẫn giữ theo SGK/SCD.
- 58 mục có `notation` (LaTeX). Kí hiệu theo SGK: biến thiên enthalpy $\Delta_r H$, chuẩn $\Delta_r H^o_{298}$; nhiệt tạo thành $\Delta_f H^o_{298}$; năng lượng liên kết $E_b$; năng lượng hoạt hoá $E_a$; độ âm điện $\chi$; nguyên tử khối trung bình $\overline{A}$; kí hiệu nguyên tử $^A_ZX$.
- `dinh_ly` (3): định luật tuần hoàn, định luật Hess, định luật bảo toàn số khối và điện tích trong phản ứng hạt nhân.
- `cong_thuc` chính: $\overline{A}$; $n^2$ AO; $\Delta_r H^o_{298}$ theo nhiệt tạo thành và theo năng lượng liên kết; $v_{tb}$; $v = k \cdot C^2_{NO} \cdot C_{O_2}$; hệ số Van't Hoff $\gamma$; phương trình Arrhenius; $\Delta_r S^o_{298}$; $\Delta_r G^o_T = \Delta_r H^o_T - T\Delta_r S^o_T$.
- 0 mục có `notes`.

## 4. Yêu cầu cần đạt theo chương

Nguồn: `SGV HOA HOC 10.pdf`, phần "I. Mục tiêu" đầu mỗi bài (số trang PDF trong ngoặc). Số tiết lấy theo bảng "Phân phối chương trình Hoá học lớp 10" (SGV PDF 13; gồm 1 tiết kiểm tra đánh giá mỗi chương). Trích rút gọn.

- **Mở đầu** (3 tiết; SGV tr.14): Nêu đối tượng nghiên cứu của hoá học. Trình bày phương pháp học tập và nghiên cứu hoá học. Nêu vai trò của hoá học đối với đời sống, sản xuất.
- **Chương 1. Cấu tạo nguyên tử** (12 tiết; SGV tr.20–48): Trình bày thành phần nguyên tử (hạt nhân gồm p, n; vỏ gồm e; điện tích, khối lượng từng hạt); so sánh khối lượng electron với proton, neutron và kích thước hạt nhân với nguyên tử. Khái niệm nguyên tố hoá học, số hiệu nguyên tử, kí hiệu nguyên tử, đồng vị, nguyên tử khối; tính nguyên tử khối trung bình theo phổ khối lượng. So sánh mô hình Rutherford – Bohr với mô hình hiện đại; khái niệm AO, hình dạng AO s, p; lớp, phân lớp; viết cấu hình electron (theo lớp, phân lớp, ô orbital) của **20 nguyên tố đầu**; dự đoán kim loại/phi kim từ lớp ngoài cùng.
- **Chương 2. Bảng tuần hoàn và định luật tuần hoàn** (10 tiết; SGV tr.49–75): Lịch sử phát minh; cấu tạo bảng (ô, chu kì, nhóm); nguyên tắc sắp xếp theo cấu hình electron; phân loại nguyên tố s, p, d, f và kim loại, phi kim, khí hiếm. Giải thích xu hướng biến đổi bán kính nguyên tử, độ âm điện, tính kim loại – phi kim trong chu kì và **nhóm A**. Nhận xét xu hướng biến đổi thành phần, tính acid – base của oxide và hydroxide theo chu kì. Phát biểu định luật tuần hoàn; ý nghĩa của bảng tuần hoàn (vị trí ⇄ tính chất).
- **Chương 3. Liên kết hoá học** (12 tiết; SGV tr.76–109): Vận dụng quy tắc octet cho nguyên tố nhóm A. Khái niệm và sự hình thành liên kết ion; cấu tạo tinh thể NaCl; vì sao hợp chất ion thường ở thể rắn. Liên kết cộng hoá trị (đơn, đôi, ba); viết công thức Lewis chất đơn giản; liên kết cho – nhận; phân biệt liên kết cộng hoá trị không phân cực, phân cực, ion theo độ âm điện; liên kết σ, π qua xen phủ AO; năng lượng liên kết. Liên kết hydrogen (với N, O, F) và ảnh hưởng tới tính chất vật lí của nước; tương tác van der Waals và ảnh hưởng tới nhiệt độ nóng chảy, nhiệt độ sôi.
- **Chương 4. Phản ứng oxi hoá – khử** (5 tiết; SGV tr.110–118): Khái niệm và cách xác định số oxi hoá; khái niệm, ý nghĩa phản ứng oxi hoá – khử; lập phương trình bằng **phương pháp thăng bằng electron**; một số phản ứng oxi hoá – khử quan trọng trong đời sống.
- **Chương 5. Năng lượng hoá học** (9 tiết; SGV tr.119–124): Khái niệm phản ứng toả nhiệt, thu nhiệt; điều kiện chuẩn; nhiệt tạo thành; biến thiên enthalpy (nhiệt phản ứng). Ý nghĩa dấu và giá trị $\Delta_r H^o_{298}$. Tính $\Delta_r H^o_{298}$ theo năng lượng liên kết và theo nhiệt tạo thành.
- **Chương 6. Tốc độ phản ứng** (8 tiết; SGV tr.125–136): Khái niệm tốc độ phản ứng, cách tính tốc độ trung bình. Biểu thức tốc độ theo hằng số tốc độ và nồng độ (định luật tác dụng khối lượng — **chỉ đúng cho phản ứng đơn giản, không tuỳ ý áp dụng cho mọi phản ứng**); ý nghĩa hằng số tốc độ. Thí nghiệm và giải thích các yếu tố ảnh hưởng (nồng độ, nhiệt độ, áp suất, diện tích bề mặt, chất xúc tác); ý nghĩa hệ số nhiệt độ Van't Hoff.
- **Chương 7. Nguyên tố nhóm halogen** (11 tiết; SGV tr.137–152): Trạng thái tự nhiên; trạng thái, màu sắc, biến đổi nhiệt độ nóng chảy, nhiệt độ sôi của đơn chất (giải thích bằng tương tác van der Waals). Xu hướng nhận 1 electron hoặc dùng chung electron; xu hướng phản ứng với hydrogen; phản ứng tự oxi hoá – khử của chlorine; thí nghiệm so sánh tính oxi hoá. Biến đổi nhiệt độ sôi HX (bất thường của HF), tính acid của dãy hydrohalic acid; phân biệt ion halide bằng $AgNO_3$; tính khử của ion halide với $H_2SO_4$ đặc; ứng dụng một số hydrogen halide.

**Chuyên đề** (nguồn: `SGV CD HOA HOC 10.pdf`, cấu trúc sách PDF 9 và mục tiêu từng bài):
- **Chuyên đề 1. Cơ sở hoá học** (15 tiết; SGV CD tr.11–50): Viết công thức Lewis; dùng mô hình VSEPR dự đoán dạng hình học phân tử đơn giản; khái niệm lai hoá AO (sp, sp², sp³) và vận dụng. Sơ lược phóng xạ tự nhiên, nhân tạo, phản ứng hạt nhân; vận dụng định luật bảo toàn số khối và điện tích; ứng dụng (y tế, năng lượng, xác định niên đại). Khái niệm năng lượng hoạt hoá; ảnh hưởng của $E_a$ và nhiệt độ qua phương trình Arrhenius; vai trò chất xúc tác. Khái niệm entropy; ý nghĩa dấu và trị số $\Delta_r G^o$; tính $\Delta_r G^o$ từ bảng $\Delta_f H^o$ và $S^o$.
- **Chuyên đề 2. Hoá học trong việc phòng chống cháy, nổ** (10 tiết; SGV CD tr.51–78): Khái niệm, đặc điểm phản ứng cháy; điều kiện cần và đủ; phản ứng nổ (vật lí, hoá học), nổ bụi; sản phẩm độc hại. Điểm chớp cháy, nhiệt độ ngọn lửa, nhiệt độ tự bốc cháy; phân biệt chất lỏng dễ cháy và có thể gây cháy. Tính $\Delta_r H^o_{298}$ phản ứng cháy, nổ; ảnh hưởng của nồng độ oxygen tới tốc độ cháy và "phản ứng hô hấp". Nhận biết nguy cơ, phòng cháy; nguyên tắc chữa cháy; vì sao không dùng nước, $CO_2$, cát, bọt cho đám cháy kim loại kiềm, kiềm thổ, nhôm.
- **Chuyên đề 3. Thực hành hoá học và công nghệ thông tin** (10 tiết, **chọn 2 trong 3 bài**; SGV CD tr.79–97): vẽ cấu trúc phân tử (ChemSketch), thí nghiệm ảo (Yenka), tính tham số cấu trúc và năng lượng bằng phương pháp bán kinh nghiệm (MOPAC, AM1).

**Giới hạn và trọng tâm.** Agent sinh câu hỏi lưu ý:
- So với CT 2006: **lược bỏ nhóm oxygen – sulfur**, chuyển **cân bằng hoá học** sang lớp 11; bổ sung chương "Năng lượng hoá học", chủ yếu tính enthalpy bằng công thức với bảng số liệu cho sẵn (Tài liệu bồi dưỡng GV tr.4). Không ra câu hỏi về hằng số cân bằng, nguyên lí Le Chatelier ở lớp 10.
- Thời lượng: SGK 70 tiết (7 tiết kiểm tra); chuyên đề 35 tiết, nên dạy sau 3 chương đầu (Tài liệu bồi dưỡng GV tr.5–6).
- Cấu hình electron chỉ yêu cầu với **20 nguyên tố đầu**; số phân lớp và số AO theo $n^2$ chỉ xét $n \le 4$ (SGK PDF 24).
- Xu hướng biến đổi tính chất chỉ xét trong chu kì và **nhóm A** (mục tiêu Bài 6, SGK PDF 35).
- Tốc độ phản ứng: HS chỉ cần biết cách tính **tốc độ trung bình**; tốc độ tức thời chỉ nêu để so sánh, GV không cần đi sâu (SGV tr.129). Biểu thức tốc độ theo nồng độ với số mũ là hệ số tỉ lượng chỉ đúng cho phản ứng đơn giản (SGV tr.125, 131). Chương trình chủ yếu đo tốc độ qua thể tích khí thoát ra (SGV tr.126).
- Sơ đồ tạo ion viết **không kèm trạng thái** ($Na \rightarrow Na^+ + e$) dù quá trình thực xảy ra ở thể khí (SGV tr.82).

## 5. Sai lầm thường gặp của học sinh

SGV và SGV CD bộ này **không có mục "sai lầm thường gặp" riêng**. Bảng dưới tổng hợp các đoạn "GV lưu ý HS", "Chú ý", "Cần chú ý phân biệt" chỉ ra điểm HS dễ hiểu sai (cột Nguồn: trang PDF của `SGV HOA HOC 10.pdf`, hoặc `SGV CD` cho `SGV CD HOA HOC 10.pdf`).

| Chủ đề | Sai lầm / điểm dễ nhầm | Nguồn |
|---|---|---|
| Nguyên tử khối (Bài 2) | Nguyên tử khối chỉ **xấp xỉ** số khối, không bằng chính xác (trừ carbon-12). Nguyên tử khối trung bình không nguyên (ví dụ Cr 51,996) vì là trung bình theo tỉ lệ đồng vị, **không phải do làm tròn**. Khối lượng nguyên tử tương đối không có đơn vị. | SGV tr.22, 32, 36 |
| Lớp, phân lớp (Bài 3) | Electron trong cùng **lớp** có năng lượng **gần bằng nhau**; electron cùng **phân lớp** mới **bằng nhau**. Số phân lớp bằng n. | SGV tr.45 |
| Ion, liên kết ion (Bài 11) | Không vẽ sự tạo ion bằng nhiều vòng tròn đồng tâm (mô hình hành tinh) vì mâu thuẫn với mô hình orbital hiện đại. Cấu hình ion giống khí hiếm gần nhất. | SGV tr.82, 85 |
| Phân cực (Bài 12) | Nhầm **phân cực của liên kết** với **phân cực của phân tử**. $CO_2$ có liên kết C=O phân cực nhưng phân tử thẳng nên không phân cực; $H_2O$ có góc 104,5° nên phân cực. | SGV tr.94; SGK PDF 60 |
| Năng lượng liên kết (Bài 12) | $E_b$ mang dấu "+" là năng lượng **cần cung cấp** để phá liên kết; đổi dấu là năng lượng toả ra khi hình thành liên kết. | SGV tr.97 |
| Lực giữa phân tử (Bài 13, 21) | Liên kết hydrogen, tương tác van der Waals đều có bản chất tĩnh điện nhưng **không hình thành liên kết hoá học** mới. | SGV tr.142 |
| Biến thiên enthalpy (Bài 17) | Dấu: $\Delta_r H < 0$ là **toả** nhiệt, $\Delta_r H > 0$ là **thu** nhiệt (ngược với cảm nhận "giá trị âm = mất"). Đồng nhất biến thiên enthalpy với nhiệt phản ứng **ở áp suất không đổi**. | SGV tr.119–121 |
| Tốc độ phản ứng (Bài 19) | Áp dụng $v = k \cdot C^a_A \cdot C^b_B$ với số mũ = hệ số cho **mọi** phản ứng là sai; chỉ đúng với phản ứng đơn giản. Thêm dấu "−" khi tính theo chất đầu. | SGV tr.125, 131 |
| Chất xúc tác (Bài 19; CĐ Bài 3) | Xúc tác chỉ làm **tăng tốc độ**, không gây ra phản ứng và không làm thay đổi chiều phản ứng; chất làm chậm phản ứng là **chất ức chế**. | SGV tr.133; SCD PDF 22 |
| Số oxi hoá (Bài 15) | Số oxi hoá là hoá trị **hình thức**, không phụ thuộc liên kết ion hay cộng hoá trị. Ngoại lệ: H là −1 trong hydride kim loại (NaH); O là −1 trong $H_2O_2$, +2 trong $OF_2$. | SGV tr.111 |
| Halogen (Bài 21) | Fluorine **chỉ có số oxi hoá −1**; các halogen khác có thể +1, +3, +5, +7 khi liên kết với nguyên tố có độ âm điện lớn hơn. | SGV tr.138; SGK PDF 107 |
| Mô hình VSEPR (CĐ Bài 1) | Phải viết $AX_nE_m$ để phân biệt với công thức hoá học $AX_n$; tổng $m + n$ quyết định dạng hình học. | SGV CD tr.20 |
| Cháy, nổ (CĐ Bài 5–6) | Nhầm phản ứng cháy với phản ứng nổ (khác ở tốc độ rất nhanh và tăng thể tích đột ngột). Nhầm **điểm chớp cháy** với **điểm sôi** (ethanol: chớp cháy 13 °C, sôi 78 °C). | SGV CD tr.54, 60 |

## 6. Hạn chế đã biết và kết quả kiểm tra chất lượng

**Hạn chế đã biết:**
- Năm sách nguồn là PDF dạng ảnh. Định nghĩa được đọc từ OCR (tesseract `vie`, 300 dpi, cache ở `.ocr/`) và đối chiếu ảnh trang (100–110 dpi) với mọi trang có bảng, công thức, kí hiệu. Tài liệu bồi dưỡng GV có text layer tốt, đọc trực tiếp.
- OCR không đọc được công thức. Phần LaTeX trong `definition` và toàn bộ `notation` **không được kiểm tra tự động**; phần này dựa vào đối chiếu ảnh khi trích và kiểm tra mẫu.
- Bổ sung cache OCR: PDF 95 SGK (hộp "Em có biết" về tốc độ tức thời bị bỏ sót, OCR riêng vùng cắt) và trang bảng thuật ngữ SGK PDF 120, SCD PDF 76 (nối thêm OCR 400 dpi). Nếu xoá `.ocr/`, `check_sources.py` sẽ OCR lại theo mặc định và có thể gắn cờ `toc-do-tuc-thoi`, `phong-xa`.
- Tên các mục `tinh_chat`, `quy_tac`, `cong_thuc` thường do người trích đặt. Lần chạy gần nhất có 24 cảnh báo tên; nội dung các mục này vẫn đạt (bigram ≥ 0.69 ở nguồn định nghĩa).
- Nguồn `gv` (26 mục) chỉ kiểm tra sự có mặt của tên thuật ngữ. Đã thêm alias theo cách gọi của SGV: `ion đơn nguyên tố`, `tốc độ phản ứng tức thời`, `công thức VSEPR`.

**Kiểm tra tự động** (2026-10-15, ngưỡng bigram 0.65, so khớp có dấu):

| Hạng mục | Kết quả |
|---|---|
| `validate.py hoa_10` | 0 lỗi; 194 thuật ngữ |
| `check_sources.py hoa_10` | 194 đạt, 0 gắn cờ, 0 không kiểm tra được, 24 cảnh báo về tên |
| Mục bị gắn cờ trong quá trình trích (đã xử lý) | 11 lượt: 4 do trang bảng thuật ngữ OCR kém hoặc đứng đầu `sources` (đổi thứ tự nguồn: `lien-ket-cong-hoa-tri`, `nhiet-luong-ke`; bỏ nguồn trang bảng: `lien-ket-cho-nhan`; bổ sung OCR 400 dpi: `phong-xa`); 1 do OCR bỏ sót hộp bên lề (`toc-do-tuc-thoi`, OCR vùng cắt); 2 do nguồn phụ ở trang xa (bỏ nguồn tóm tắt PDF 19 của `dinh-luat-bao-toan-trong-phan-ung-hat-nhan`; tách `tinh-oxi-hoa-cua-halogen` thành 2 mục); 1 do tên không có nguyên văn (đổi tên thành "Ion đa nguyên tử"); 1 do bảng dạng ảnh (`duong-luong-no`: chuyển bảng sang `notation`, đã đối chiếu ảnh); 2 do SGV dùng tên khác (thêm alias). Không mục nào sai nội dung. |

**Kiểm tra mẫu** (Giai đoạn 4, 2026-10-15, cùng phiên trích xuất):

| Hạng mục | Kết quả |
|---|---|
| Số mục kiểm tra | 30/194 (15%): 20 ngẫu nhiên + 10 mục `cong_thuc`/`dinh_ly`/có `notation` |
| Cách chọn | `query.py hoa_10 --audit` (seed 2026), danh sách ở `sample_audit.md` |
| Đối chiếu ảnh | 22 trang ảnh được mở lại (SGK PDF 7, 18, 19, 23, 51, 53, 57, 58, 67, 83, 96, 100, 114, 117; SCD PDF 11, 12, 17, 20, 22, 30, 50, 68). Các trang còn lại của mẫu (SGK PDF 16, 20, 24, 25, 85, 98, 108–110, 113, 116; SCD PDF 15, 16, 21, 27, 33, 76) đã đối chiếu ảnh khi trích. |
| Số mục sai | 0 (0%, dưới ngưỡng 5%) |
| Kiểm tra độc lập | Đã hoàn thành (người dùng đã kiểm tra độc lập file mẫu 30 mục ở phiên riêng, đạt yêu cầu; đã xoá file mẫu). |

## 7. Liên hệ với các lớp khác

Phần này điền khi làm Hoá học 11 và 12. Các khái niệm dự kiến được mở rộng ở lớp sau:
- Phản ứng thuận nghịch, trạng thái cân bằng (Bài 21; Chuyên đề Bài 4) → cân bằng hoá học (lớp 11).
- Lai hoá orbital, liên kết σ/π (Bài 12; Chuyên đề Bài 1) → cấu tạo hợp chất hữu cơ (lớp 11).
- Phản ứng oxi hoá – khử, số oxi hoá (Bài 15) → pin điện, điện phân (lớp 12).
- Xăng, gas, nhiên liệu (Chuyên đề Bài 7) → hydrocarbon (lớp 11).
- Liên quan liên môn: phóng xạ, phản ứng hạt nhân (Chuyên đề Bài 2) ↔ Vật lí 12; nhiệt độ, năng lượng ↔ `vat_ly_10` Chương IV.
