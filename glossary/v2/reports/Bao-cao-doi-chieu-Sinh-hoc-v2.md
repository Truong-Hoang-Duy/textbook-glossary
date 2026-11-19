# Báo cáo Đối chiếu & Kiểm chứng Từ điển Sinh học Ver 2 (Pha 2)

> **Chuẩn áp dụng:** `SPEC-GLOSSARY-V2` v1.0 ([specs/2026-11-11-glossary-v2-spec.md](../../specs/2026-11-11-glossary-v2-spec.md)) — Mục 6
> **Bản tạo mới (Pha 1 độc lập):** `textbook/glossary_v2/markdown/Tu-dien-*.md` & `dataset/glossary_master.json`
> **Bản mẫu đối chứng của thầy:** `report/research/Tu-dien.md` (583 mục Sinh học + 20 mục Toán học)

---

## 1. Tổng quan quy mô và chất lượng kỹ thuật

| Chỉ số | Bản mẫu `report/research/Tu-dien.md` | Bản Ver 2 tạo mới (`textbook/glossary_v2/`) | Nhận xét |
|---|---:|---:|---|
| **Tổng số mục từ (kể cả liên môn)** | 603 | **5899** | Tăng **+5296 mục** nhờ phủ trọn 100% cả 3 khối 10–11–12 |
| — Mục gốc `Sinh học` (`Tu-dien-Sinh-hoc.md`) | 583 | **1011** | Đủ Sinh 10 (B1–26), Sinh 11 (B1–29), Sinh 12 (B1–35) |
| — Mục gốc `Hóa học` / `Vật lí` / `Toán học` trích từ SGK Sinh | 0 (20 mục Toán rời) | **4888** | Tự động kéo vào `by_subject/sinh_hoc.json` (5899 mục) |
| **Phạm vi bài học SGK Sinh học** | Sinh 10 (B1–13), Sinh 11 (B1–8), Sinh 12 (B1–18) | **Trọn bộ 90/90 bài học + 3 bảng tra cứu cuối sách** | Bổ sung mới **560 mục** thuộc nửa sau Sinh 10, 11, 12 |
| **Tỉ lệ mục có số trang in thực tế (`tr. <số>`)** | 0% (579/579 ghi `tr. chưa rõ`, 24 thiếu `Nguồn`) | **100% (5899/5899 mục)** | Truy vết chính xác `printed_page` từ mốc `<!-- pdf:N -->` Tầng 1 |
| **Mục đa bối cảnh / gộp liên cấp** | 24 | **4755** | Hợp nhất sạch giữa các bài và các khối lớp 10–11–12 |
| **Mục có `Giải thích khác (SGK ...)`** | 22 | **317** | Giữ nguyên sắc thái định nghĩa riêng giữa các khối lớp |
| **Lỗi định dạng / thứ tự A–Z / xung đột chưa xử lý** | 4 cặp tách đôi + 24 mục thiếu `Nguồn` | **0 lỗi, 0 cảnh báo** (`check_glossary_v2.py`) | Đạt 100% schema `glossary_v2.schema.json` |

---

## 2. Kết quả đối chiếu độ phủ trên 583 mục Sinh học của bản mẫu

| Nhóm phân loại đối chiếu | Số lượng | Tỉ lệ /583 | Ý nghĩa kiểm chứng |
|---|---:|---:|---|
| **1. Khớp trực tiếp hoặc tương đương cấu trúc trong Ver 2 mới** | **496** | **85.1%** | Gồm 418 khớp y hệt khóa EN + 14 khớp gốc EN + 40 khớp qua Tiếng Việt + 24 gộp/tách cấu trúc |
| **2. Loại có chủ ý theo chuẩn SGK (đã giải trình ở cổng độ phủ)** | **64** | **11.0%** | Chỉ xuất hiện trong ví dụ/bài tập (Down, Turner, Klinefelter, ABO, CRISPR-Cas9...), tiêu đề bài/mục hoặc chỉ nhắc tên không định nghĩa |
| **3. Mục ngoài SGK / giáo viên bổ sung / nháp không nguồn** | **10** | **1.7%** | `helicase`, `primase`, `allolactose`, `criss-cross inheritance`, `holandric inheritance`, `2,4-D herbicide`, mục mẫu `DNA`/`Auxin`/`Gel electrophoresis` |
| **4. Chênh lệch khác (hoá chất/thao tác lẻ trong bài thực hành)** | **13** | **2.2%** | Hóa chất/vật tư phụ trong bài thực hành hoặc chi tiết nhỏ không in đậm định nghĩa ở Tầng 1 |
| **Tổng cộng đã đối soát** | **583** | **100.0%** | **100% mục trong file mẫu được giải trình minh bạch** |

### 2.1. Các mục ngoài SGK hoặc mục nháp trong bản mẫu (không chép sang để chống bịa nguồn SGK)

- **`2,4-D herbicide`** (*Thuốc diệt cỏ 2,4D*): không có trong SGK (`Tu-dien-Sinh-hoc-12-Chuong-2.md`)
- **`acetyl-CoA`** (*Acetyl-CoA*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK
- **`allolactose`** (*Allolactose*): không có trong SGK: sách viết "đồng phân của lactose" (`Tu-dien-Sinh-hoc-12-Chuong-1.md`)
- **`criss-cross inheritance`** (*Di truyền chéo*): không có trong SGK (`Tu-dien-Sinh-hoc-12-Chuong-2.md`)
- **`Gel electrophoresis (DNA)`** (*Điện di DNA (điện di trên gel)*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK
- **`helicase`** (*Helicase*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK
- **`holandric inheritance`** (*Di truyền thẳng*): không có trong SGK (`Tu-dien-Sinh-hoc-12-Chuong-2.md`)
- **`lactose intolerance`** (*Không dung nạp lactose*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK
- **`P, F1, F2`** (*P, F₁, F₂*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK
- **`primase`** (*Primase*): Mục hạt giống không gắn nguồn SGK hoặc do giáo viên bổ sung ngoài SGK

### 2.2. Các cặp bị tách đôi trong bản mẫu đã được hợp nhất sạch ở Ver 2 mới

| Trong `report/research/Tu-dien.md` (bị tách 2 mục) | Trong `Tu-dien-Sinh-hoc.md` mới (hợp nhất chuẩn Quy tắc 2) |
|---|---|
| `DNA` (*ADN*) + `DNA (deoxyribonucleic acid)` (*DNA*) | Hợp nhất thành 1 mục **`DNA`** duy nhất theo danh pháp GDPT 2018, đầy đủ nguồn trang in |
| `genetically modified organism` (Sinh 10) + `genetically modified organism (GMO)` (Sinh 12) | Hợp nhất thành 1 mục **`genetically modified organism (GMO)`**, gộp đủ bối cảnh Sinh 10 Bài 1 và Sinh 12 Bài 5 |
| `macroelement` (Sinh 10) + `macronutrient` (Sinh 11) — cùng là *Nguyên tố đa lượng* | Hợp nhất thành 1 mục **`macronutrient`** kèm `Giải thích khác (SGK Sinh học 11)` và đa bối cảnh |
| `trace element` (Sinh 10) + `micronutrient` (Sinh 11) — cùng là *Nguyên tố vi lượng* | Hợp nhất thành 1 mục **`trace element`** kèm `Giải thích khác (SGK Sinh học 11)` và đa bối cảnh |

### 2.3. Một số cặp cùng khái niệm nhưng chọn khóa Tiếng Anh khác nhau (Tiêu chí 2)

| Thuật ngữ Tiếng Việt | Khóa EN bản mẫu | Khóa EN bản Ver 2 mới | Ghi chú |
|---|---|---|---|
| Chất hoạt hoá | `activator` | `enzyme activator` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Tương tác cộng gộp | `additive interaction` | `additive gene interaction` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| ADP | `adenosine diphosphate` | `ADP` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| AMP | `adenosine monophosphate` | `AMP` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| ATP | `adenosine triphosphate` | `ATP` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Đột biến thay thế cặp nucleotide | `base-pair substitution` | `substitution mutation` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Chuyển hoá năng lượng (trong tế bào) | `cellular energy transformation` | `energy transformation` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| cDNA | `complementary DNA` | `cDNA` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Chu trình C₃ (Calvin) | `C₃ cycle (Calvin cycle)` | `Calvin cycle` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Điều hoà biểu hiện gene | `gene expression regulation` | `gene regulation` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Quần thể đa dạng di truyền (đa hình di truyền) | `genetic diversity (polymorphism)` | `genetically diverse population` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Cân bằng di truyền | `genetic equilibrium` | `Hardy–Weinberg equilibrium` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Chất ức chế | `inhibitor` | `enzyme inhibitor` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Nitrogen vô cơ hấp thụ được | `inorganic nitrogen` | `absorbable inorganic nitrogen` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Protein xuyên màng | `integral protein` | `transmembrane protein` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Đèn LED trồng cây | `LED plant lighting` | `LED grow light` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Thành phần ánh sáng | `light quality` | `spectral composition of light` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Nguyên tố đa lượng | `macroelement` | `macronutrient` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| mRNA | `messenger RNA` | `mRNA` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Nguyên tố vi lượng | `micronutrient` | `trace element` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Thoi phân bào | `mitotic spindle` | `spindle apparatus` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| NADH, FADH₂ | `NADH, FADH₂` | `NADH and FADH₂` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Nhân tế bào | `nucleus` | `cell nucleus` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Thuyết operon | `operon model` | `operon theory` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |
| Nhiệt độ tối ưu (nảy mầm) | `optimum temperature for germination` | `optimum temperature` | Cùng khái niệm, đồng bộ tên gọi chuẩn quốc tế |

---

## 3. Đối chiếu trực tiếp chất lượng cô đọng & tổng hợp đa đoạn (Tiêu chí 3 & 4)

### `biuret test` — *Phép thử Biuret* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Nhận biết protein: liên kết peptide tạo phức chất màu tím với Cu²⁺ trong môi trường kiềm. *(Nguồn: SGK Sinh học 10, Bài 6: Thực hành nhận biết một số phân tử sinh học, Mục III.3, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** A biochemical test for detecting proteins based on the reaction in an alkaline medium between compounds containing two or more peptide bonds and CuSO₄ solution, in which peptide nitrogen atoms coordinate with Cu²⁺ ions to form a violet-blue, purple, or reddish-violet complex depending on the number of peptide bonds.
- **Bản Ver 2 tạo mới (VI):** Phép thử hoá sinh dùng để nhận biết protein dựa trên phản ứng trong môi trường kiềm giữa các hợp chất chứa từ hai liên kết peptide trở lên với dung dịch CuSO₄, trong đó các nguyên tử nitrogen của liên kết peptide phối trí với ion Cu²⁺ tạo thành phức chất màu xanh tím, tím hoặc tím đỏ tuỳ theo số lượng liên kết peptide.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Chương 01, B6 (Mục III.3.a), tr. 42`

### `systems biology` — *Sinh học hệ thống* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Ngành kết hợp sinh học với hoá học, tin học, toán, vật lí; dùng mô hình máy tính để dự đoán tương tác giữa các protein. *(Nguồn: SGK Sinh học 10, Bài 1: Giới thiệu khái quát môn Sinh học, Mục I.5, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** An interdisciplinary scientific field combining biology with chemistry, informatics, mathematics, and physics—supported by bioinformatics—to study complex interactions within biological systems. It uses specialized software and computer models to describe and predict molecular interactions, such as among cellular proteins and pathological effects of protein mutations, accelerating drug testing and production.
- **Bản Ver 2 tạo mới (VI):** Ngành khoa học liên ngành kết hợp sinh học với hoá học, tin học, toán học và vật lí trên nền tảng hỗ trợ của tin sinh học để nghiên cứu sự tương tác phức tạp trong hệ thống sống. Ngành này sử dụng phần mềm chuyên dụng và mô hình máy tính để mô tả, dự đoán tương tác giữa các phân tử như protein trong tế bào cũng như hậu quả bệnh lí khi protein đột biến, giúp đẩy nhanh việc thử nghiệm và sản xuất thuốc chữa bệnh.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Phần Mở đầu, B1 (Mục I.5), tr. 6; SGK Sinh học 10 KNTT, Phần Mở đầu, B2 (Mục IV), tr. 16`

### `targeted drug` — *Thuốc hướng đích* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Thuốc tác động đến protein riêng biệt gây bệnh, ví dụ trong điều trị ung thư. *(Nguồn: SGK Sinh học 10, Bài 1: Giới thiệu khái quát môn Sinh học, Mục II.1, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** A specific class of medication designed to directly target and inhibit particular disease-causing proteins to treat severe illnesses such as cancer. At the nanoscale, these drugs can autonomously locate target cells and specifically interact with molecules inside diseased cells, significantly reducing undesirable side effects.
- **Bản Ver 2 tạo mới (VI):** Loại thuốc đặc hiệu tác động trực tiếp và ức chế các protein gây bệnh riêng biệt để điều trị những bệnh hiểm nghèo như ung thư. Ở cấp độ nano, thuốc có khả năng tự tìm đến tế bào đích và tương tác đặc hiệu với các phân tử trong tế bào bị bệnh, giúp giảm đáng kể các tác động không mong muốn.
- **Giải thích khác (SGK Sinh học 11):** Thuốc được điều chế nhờ các kĩ thuật tiên tiến như công nghệ nano, có khả năng tự tìm đến đúng các tế bào bị bệnh ở cấp độ nano nhằm phát hiện, điều trị bệnh và nâng cao sức khoẻ con người.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Phần Mở đầu, B1 (Mục I.5), tr. 6; SGK Sinh học 10 KNTT, Phần Mở đầu, B1 (Mục II.1), tr. 7; SGK Sinh học 11 KNTT, Chương 05, B29 (Mục I), tr. 185`

### `ribosome` — *Ribosome* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Bào quan không màng, gồm rRNA và protein, hai tiểu đơn vị lớn và nhỏ; nơi tổng hợp protein. *(Nguồn: SGK Sinh học 10, Bài 8: Tế bào nhân thực, mục II.2, tr. chưa rõ; SGK Sinh học 12, Bài 2: Gene, hệ gene và quá trình truyền đạt thông tin di truyền, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** A spherical, non-membrane-bound organelle (about 150 Å in diameter) composed of rRNA (about 80%–90%) and proteins arranged into a large subunit and a small subunit. It serves as the site of protein synthesis in both prokaryotic and eukaryotic cells (free in the cytosol, bound to the rough endoplasmic reticulum, and inside mitochondria and chloroplasts).
- **Bản Ver 2 tạo mới (VI):** Bào quan không có màng bao bọc, dạng hình cầu (đường kính khoảng 150 Å), cấu tạo từ rRNA (khoảng 80%–90%) và protein tạo nên hai tiểu đơn vị lớn và nhỏ. Đây là bộ máy tổng hợp protein có ở cả tế bào nhân sơ và tế bào nhân thực (trong bào tương, trên màng lưới nội chất hạt, trong ti thể và lục lạp).
- **Giải thích khác (SGK Sinh học 12):** Phức hệ cấu tạo từ rRNA và protein, gồm một tiểu phần nhỏ và một tiểu phần lớn nằm tách rời nhau khi chưa hoạt động và liên kết lại trên mRNA khi dịch mã. Bào quan này mang các vị trí A, P, E để di chuyển trên mRNA theo chiều 5'→3' và lắp ráp các amino acid thành chuỗi polypeptide.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Chương 02, B7 (Mục II.3), tr. 46; SGK Sinh học 10 KNTT, Chương 02, B8 (Mục II.2), tr. 49; SGK Sinh học 10 KNTT, Chương 02, B8 (Mục II.3), tr. 50; SGK Sinh học 10 KNTT, Chương 02, B8 (Mục II.14), tr. 59; SGK Sinh học 12 KNTT, Chương 01, B2 (Mục III.2.b), tr. 12; SGK Sinh học 12 KNTT, Chương 01, B2 (Mục III.2.c), tr. 13; SGK Sinh học 12 KNTT, Chương 01, B2 (Mục III.4.b), tr. 15`

### `thylakoid` — *Thylakoid* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Hệ thống túi dẹp trong lục lạp, chứa diệp lục và enzyme quang hợp. *(Nguồn: SGK Sinh học 10, Bài 8: Tế bào nhân thực, mục II.9, tr. chưa rõ; SGK Sinh học 11, Bài 4: Quang hợp ở thực vật, Mục I.3.b, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** A flattened, membrane-bound sac inside the chloroplast that stacks and interconnects to form grana. The thylakoid membrane contains chlorophyll along with enzymes and proteins involved in photosynthesis.
- **Bản Ver 2 tạo mới (VI):** Cấu trúc màng dạng túi dẹp nằm bên trong lục lạp, xếp chồng và nối thông với nhau tạo thành các granum. Trên bề mặt màng thylakoid có chứa chất diệp lục cùng các enzyme và protein tham gia quá trình quang hợp.
- **Giải thích khác (SGK Sinh học 11):** Cấu trúc màng bên trong lục lạp nơi phân bố hệ sắc tố quang hợp và diễn ra pha sáng của quá trình quang hợp ở tất cả các nhóm thực vật (C₃, C₄ và CAM).
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Chương 02, B8 (Mục II.9), tr. 53; SGK Sinh học 11 KNTT, Chương 01, B4 (Mục I.3.b), tr. 27; SGK Sinh học 11 KNTT, Chương 01, B4 (Mục II), tr. 28`

### `carotenoid` — *Carotenoid* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Sắc tố màu vàng cam của thực vật, có bản chất lipid; chuyển hoá thành vitamin A. *(Nguồn: SGK Sinh học 10, Bài 5: Các phân tử sinh học, Mục II.2.d, tr. chưa rõ; SGK Sinh học 11, Bài 4: Quang hợp ở thực vật, Mục I.3.a, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** A group of yellow-orange plant pigments of lipid nature; when ingested by humans and animals, they are metabolized into vitamin A and subsequently converted into retinal pigments essential for vision.
- **Bản Ver 2 tạo mới (VI):** Nhóm sắc tố màu vàng cam ở thực vật có bản chất là lipid; khi đi vào cơ thể người và động vật qua thức ăn, chất này được chuyển hoá thành vitamin A rồi thành sắc tố võng mạc cần thiết cho thị giác.
- **Giải thích khác (SGK Sinh học 11):** Nhóm sắc tố quang hợp phụ tạo nên màu vàng, đỏ, cam của lá, hoa, củ, quả ở thực vật; gồm hai loại là xanthophyll (có oxygen) và carotene (không có oxygen), tham gia hấp thụ và truyền năng lượng ánh sáng cho diệp lục a.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Chương 01, B5 (Mục II.2.d), tr. 33; SGK Sinh học 11 KNTT, Chương 01, B4 (Mục I.3.a), tr. 27; SGK Sinh học 11 KNTT, Chương 01, B4 (Mục I.3.b), tr. 27; SGK Sinh học 11 KNTT, Chương 01, B4 (Mục IV.2), tr. 34`

### `allele` — *Allele* (`Tu-dien-Sinh-hoc.md`)
- **Bản mẫu của thầy (VI):** Là các trạng thái khác nhau của cùng một gene. Các allele thường nằm trên cùng locus của một cặp NST tương đồng *(Nguồn: SGK Sinh học 12, Thuật ngữ dùng chung, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** Alternative forms of the same gene occupying a specific locus on homologous chromosomes, typically differing by one or a few nucleotide pairs. A gene may have two or more alleles that interact to determine an organism's traits.
- **Bản Ver 2 tạo mới (VI):** Các trạng thái biểu hiện khác nhau của cùng một gene nằm tại một locus xác định trên cặp nhiễm sắc thể tương đồng, thường khác nhau ở một hoặc một số cặp nucleotide. Một gene có thể có hai hay nhiều allele tương tác với nhau để quy định tính trạng của sinh vật.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 12 KNTT, Chương 02, B7 (Mục II.1), tr. 38; SGK Sinh học 12 KNTT, Chương 02, B8 (Mục II.1), tr. 42; SGK Sinh học 12 KNTT, Chương 02, B9 (Mục Mở đầu), tr. 46; SGK Sinh học 12 KNTT, Bảng giải thích thuật ngữ, tr. 194`

### `activation energy` — *Năng lượng hoạt hoá* (`Tu-dien-Hoa-hoc.md`)
- **Bản mẫu của thầy (VI):** Năng lượng cần để phản ứng hoá học xảy ra; enzyme làm giảm mức này. *(Nguồn: SGK Sinh học 10, Bài 13: Khái quát về chuyển hoá vật chất và năng lượng, Mục II.2, tr. chưa rõ)*
- **Bản Ver 2 tạo mới (EN):** The initial amount of energy required to activate reactant molecules so that a chemical reaction can occur. In living cells, enzymes lower this activation energy barrier, enabling biochemical reactions to proceed rapidly under normal physiological temperature and pressure.
- **Bản Ver 2 tạo mới (VI):** Lượng năng lượng cần cung cấp ban đầu để hoạt hoá các chất tham gia nhằm khởi phát một phản ứng hoá học. Trong tế bào sống, enzyme làm giảm mức năng lượng hoạt hoá này xuống thấp, giúp các phản ứng sinh hoá diễn ra nhanh chóng ở điều kiện nhiệt độ, áp suất và độ pH sinh lí bình thường.
- **Giải thích khác (SGK Hóa học 10):** Năng lượng tối thiểu mà các hạt chất phản ứng (nguyên tử, phân tử hoặc ion) cần có để va chạm giữa chúng gây ra phản ứng hoá học. Khi có mặt chất xúc tác, phản ứng diễn ra qua các giai đoạn có năng lượng hoạt hoá thấp hơn, làm tăng số hạt đạt đủ năng lượng này và làm tăng tốc độ phản ứng.
- **Nguồn chuẩn hóa (có trang in thật):** `SGK Sinh học 10 KNTT, Chương 04, B13 (Mục II.2), tr. 81; SGK Sinh học 10 KNTT, Chương 04, B13 (Mục II.4), tr. 84; SGK Hóa học 10 KNTT, Chương 06, B19 (Mục II.5), tr. 99; SGK Hóa học 10 KNTT, Chương 06, B20 (Mục I), tr. 101; SGK Hóa học 10 KNTT, Bảng giải thích thuật ngữ, tr. 119`

---

## 4. Danh mục 13 mục chi tiết nhỏ / hoá chất phụ trong bản mẫu không tách mục riêng ở Ver 2

- `albumin` (*Albumin*) — SGK Sinh học 10, Bài 6: Thực hành nhận biết một số phân tử sinh học, Mục III.3, tr. chưa rõ
- `dilute NaCl solution` (*Dung dịch NaCl loãng*) — SGK Sinh học 10, Bài 11: Thực hành thí nghiệm co và phản co nguyên sinh, Mục II.2, tr. chưa rõ
- `enzyme inactivation` (*Bất hoạt enzyme*) — SGK Sinh học 10, Bài 13: Khái quát về chuyển hoá vật chất và năng lượng, Mục II.3.b, tr. chưa rõ
- `epidermis` (*Biểu bì (hành, thài lài tía)*) — SGK Sinh học 10, Bài 9: Thực hành quan sát tế bào, Mục III.2, tr. chưa rõ
- `laboratory safety` (*An toàn phòng thí nghiệm*) — SGK Sinh học 10, Bài 2: Phương pháp nghiên cứu và học tập môn Sinh học, Mục I.2.a, tr. chưa rõ
- `lignin` (*Lignin*) — SGK Sinh học 10, Bài 8: Tế bào nhân thực, mục II.12, tr. chưa rõ
- `magnification` (*Độ phóng đại*) — SGK Sinh học 10, Bài 2: Phương pháp nghiên cứu và học tập môn Sinh học, Mục II.1, tr. chưa rõ
- `metabolic regulation` (*Điều hoà chuyển hoá*) — SGK Sinh học 10, Bài 13: Khái quát về chuyển hoá vật chất và năng lượng, Mục II.4, tr. chưa rõ
- `nitric oxide` (*Oxide nitric (NO)*) — SGK Sinh học 10, Bài 12: Truyền tin tế bào, Mục I, tr. chưa rõ
- `penicillin` (*Penicillin*) — SGK Sinh học 10, Bài 7: Tế bào nhân sơ, Mục II.2, tr. chưa rõ
- `self-fertilization` (*Tự thụ tinh*) — SGK Sinh học 12, Bài 18: Di truyền học quần thể, Mục III.1, tr. chưa rõ
- `solvent` (*Dung môi*) — SGK Sinh học 10, Bài 4: Các nguyên tố hoá học và nước, Mục III.2, tr. chưa rõ
- `statistical significance` (*Ý nghĩa thống kê*) — SGK Sinh học 10, Bài 2: Phương pháp nghiên cứu và học tập môn Sinh học, Mục III.5, tr. chưa rõ
