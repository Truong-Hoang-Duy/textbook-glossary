---
loai_hoc_lieu: trac-nghiem-de-cuong
mon: Hoá học
lop: 12
chu_de: "Bao phủ 8 chương môn Hoá học 12 (Bối cảnh KHÔNG CÓ từ điển)"
so_cau: 40
nguon: "Mô hình tạo sinh tự do không nạp dataset/hoa_12.json"
file_dap_an: "report/evaluation_report_hoa_12.md"
ngay_tao: 2026-10-29
trang_thai: draft
---

# BỘ CÂU HỎI TRẮC NGHIỆM HOÁ HỌC 12 — BỐI CẢNH KHÔNG CÓ TỪ ĐIỂN (40 CÂU)

> **Ghi chú đối chứng:** Bộ câu hỏi đối chứng được tạo sinh tự do bằng mô hình ngôn ngữ lớn khi **không được cung cấp bộ từ điển `hoa_12.json`**.
> 
> **Các biểu hiện nhược điểm điển hình được ghi nhận:**
> 1. **Dông dài, thừa thãi:** Câu dẫn (stem) chứa nhiều thông tin kể lể ngoài lề về đời sống, lịch sử hoặc kinh tế không liên quan đến trọng tâm hoá học.
> 2. **Lẫn lộn danh pháp cũ và mới:** Thường xuyên pha trộn danh pháp phiên âm cũ (este, axit cacboxylic, anilin, glucozơ, glixerol, natri hiđroxit) với danh pháp hiện hành IUPAC.
> 3. **Công thức thiếu chuẩn hoá:** Công thức hoá học viết dạng văn bản thuần tuý không có định dạng LaTeX `\ce{...}`, thiếu chỉ số dưới/trên hoặc điện tích ion.
> 4. **Phương án bất cân xứng:** Các phương án có độ dài chênh lệch lớn, phương án đúng thường dài dòng mang tính giải thích lộ liễu.

---

## Chương 1: Ester – Lipid

### Câu 1: Hợp chất hữu cơ chứa nhóm chức — Phản ứng tạo thành este
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong hoá học hữu cơ phần dẫn xuất của hydrocarbon, các hợp chất hữu cơ có chứa liên kết đặc trưng giữa gốc hydrocarbon và nhóm chức oxygen đóng vai trò rất quan trọng trong đời sống cũng như công nghiệp sản xuất hương liệu. Khi chúng ta tiến hành thay thế nhóm hiđroxyl (-OH) trong phân tử axit cacboxylic bằng một nhóm alkoxyl dạng -OR' với R' là gốc hydrocarbon thì nhóm hợp chất thu được mang tên gọi là gì?

A. Hợp chất ete hữu cơ thông thường R-O-R'.
[B.] Este (hoặc ester theo danh pháp mới).
C. Ancol đa chức có mạch carbon phân nhánh.
D. Andehit no đơn chức mạch hở.

**Dẫn giải lan man:** Khi cho axit tác dụng với ancol sẽ xảy ra phản ứng este hoá tạo thành este và nước, trong đó nhóm OH của axit tách ra cùng H của ancol tạo ra este có mùi thơm đặc trưng...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn dài 67 từ, kể lể lan man về ứng dụng hương liệu không liên quan đến trọng tâm câu hỏi.
- Dùng danh pháp cũ không nhất quán: 'axit cacboxylic', 'hiđroxyl', 'este', 'ancol', 'andehit' thay vì chuẩn mới SGK KNTT (carboxylic acid, ester, alcohol, aldehyde).
- Phương án độ dài không cân đối (A dài 9 từ, B dài 8 từ, C dài 8 từ, D dài 6 từ).

*Thống kê số từ:* Đề bài: 82 từ | Các phương án: 33 từ | Lời giải & Phân tích: 108 từ | **Tổng: 223 từ**

---

### Câu 2: Lipid và este phức tạp — Cấu tạo phân tử chất béo
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Chất béo hay còn gọi là dầu mỡ động thực vật là nguồn cung cấp năng lượng vô cùng quan trọng đối với cơ thể sống của con người và động vật. Về mặt bản chất hoá học cấu tạo phân tử, các nhà khoa học đã chứng minh chất béo chính là este ba chức được tạo thành từ phản ứng giữa ancol ba chức glixerol với loại axit hữu cơ nào?

A. Axit vô cơ mạnh như axit clohiđric hoặc axit nitric.
[B.] Các axit béo có mạch cacbon dài không phân nhánh.
C. Bất kì axit cacboxylic no hay không no đơn chức nào.
D. Axit hữu cơ hai chức dicarboxylic.

**Dẫn giải lan man:** Chất béo là trieste của glixerol với các axit monocacboxylic có số chẵn nguyên tử cacbon (thường từ 12C đến 24C) không phân nhánh gọi chung là triglixerit...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn dông dài 63 từ giải thích chức năng dinh dưỡng không cần thiết.
- Dùng danh pháp cũ: 'glixerol', 'ancol', 'axit monocacboxylic' thay vì glycerol, carboxylic acid.
- Phương án A đưa ra axit vô cơ là nhiễu phi lí, độ dài phương án chênh lệch lớn.

*Thống kê số từ:* Đề bài: 73 từ | Các phương án: 41 từ | Lời giải & Phân tích: 75 từ | **Tổng: 189 từ**

---

### Câu 3: Xà phòng và phản ứng thuỷ phân chất béo kiềm hoá
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Trong thực tế đời sống và sản xuất công nghiệp xà phòng, người ta thường tiến hành nấu dầu mỡ động thực vật với dung dịch kiềm xút nóng để thu được xà phòng bánh và sản phẩm phụ glixerol. Giả sử tiến hành đun một mẫu chất béo no chứa gốc axit panmitic là tripanmitin với dung dịch natri hiđroxit dư thì muối natri của axit béo thu được có công thức hoá học là gì?

A. Muối natri stearat có công thức C17H35COONa.
[B.] Muối natri panmitat có công thức C15H31COONa.
C. Muối natri oleat có công thức C17H33COONa.
D. Muối natri linoleat có công thức C17H31COONa.

**Dẫn giải lan man:** Tripanmitin là chất béo no có công thức (C15H31COO)3C3H5, khi phản ứng xà phòng hoá sẽ cắt đứt liên kết este tạo thành 3 phân tử xà phòng C15H31COONa và 1 glixerol...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ với nhiều thông tin ngoài lề (nấu dầu mỡ, sản xuất xà phòng bánh).
- Công thức hoá học không định dạng LaTeX, dùng tên cũ 'tripanmitin', 'natri panmitat', 'natri hiđroxit'.
- Phương án lặp lại cụm từ dài 'Muối natri ... có công thức'.

*Thống kê số từ:* Đề bài: 77 từ | Các phương án: 32 từ | Lời giải & Phân tích: 79 từ | **Tổng: 188 từ**

---

### Câu 4: Thành phần dinh dưỡng — Khái niệm acid béo omega
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Hiện nay trên các phương tiện truyền thông và các sản phẩm sữa dinh dưỡng, dầu cá cao cấp thường quảng cáo rất nhiều về thành phần axit béo omega-3 và omega-6 có lợi cho sức khoẻ tim mạch và trí não. Theo quy ước chuẩn trong hoá sinh và hoá học lập thể, tên gọi omega-3 bắt nguồn từ việc liên kết đôi carbon-carbon đầu tiên xuất hiện ở vị trí nào trong chuỗi hydrocacbon?

[A.] Vị trí carbon thứ 3 tính từ đầu nhóm metyl cuối mạch.
B. Vị trí carbon thứ 3 tính từ nguyên tử carbon của nhóm chức axit.
C. Vị trí carbon thứ 6 tính từ nhóm metyl của chuỗi.
D. Vị trí carbon thứ 9 trong khung phân tử mạch hở.

**Dẫn giải lan man:** Theo danh pháp quốc tế, chữ cái Hy Lạp omega chỉ carbon cuối cùng của mạch. Omega-3 là liên kết đôi đầu tiên ở vị trí C số 3 tính từ nguyên tử carbon này...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ với ngữ cảnh quảng cáo thương mại không phục vụ mục tiêu đánh giá hoá học cốt lõi.
- Dùng chữ 'metyl', 'axit' thay vì methyl, carboxylic acid.
- Độ dài các phương án rất chênh lệch (A dài 11 từ, D dài 9 từ).

*Thống kê số từ:* Đề bài: 76 từ | Các phương án: 52 từ | Lời giải & Phân tích: 82 từ | **Tổng: 210 từ**

---

### Câu 5: Chất tẩy rửa nhân tạo và ứng dụng trong giặt giũ gia đình
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Ngày nay bột giặt và nước giặt tổng hợp đã trở thành vật dụng thiết yếu trong mọi gia đình thay thế cho các loại xà phòng truyền thống sản xuất từ mỡ lợn hay dầu cọ. Nguyên nhân kỹ thuật hoá học chủ yếu nào giải thích tại sao chất giặt rửa tổng hợp lại giặt tẩy tốt hơn hẳn xà phòng bánh thông thường trong điều kiện nguồn nước máy sinh hoạt chưa qua xử lí làm mềm?

[A.] Do muối của chất giặt rửa tổng hợp không tạo kết tủa với các ion canxi và magie trong nước cứng.
B. Do chất giặt rửa tổng hợp có nguồn gốc từ dầu mỏ nên có khả năng hoà tan dầu mỡ mạnh hơn gấp mười lần.
C. Do chất giặt rửa tổng hợp dễ dàng bị vi sinh vật phân huỷ trong tự nhiên hơn xà phòng.
D. Do giá thành sản xuất chất giặt rửa tổng hợp rẻ hơn xà phòng bánh rất nhiều.

**Dẫn giải lan man:** Xà phòng truyền thống chứa muối natri của axit béo bị kết tủa bởi ion Ca2+ và Mg2+ tạo cặn bẩn, còn chất giặt rửa tổng hợp là alkyl sulfonate không tạo kết tủa...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ dài dòng, kể lể về gia đình, nước máy sinh hoạt.
- Các phương án quá dài dòng (trung bình 20 từ/phương án), nhiều phương án giải thích cảm tính phi khoa học (phương án B và D).
- Viết tên kim loại dạng cũ 'canxi và magie'.

*Thống kê số từ:* Đề bài: 80 từ | Các phương án: 87 từ | Lời giải & Phân tích: 84 từ | **Tổng: 251 từ**

---

## Chương 2: Carbohydrate

### Câu 6: Đại cương hoá học carbohydrate — Phân loại các chất đường bột
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Hợp chất carbohydrate hay còn gọi là gluxit, saccarit là nhóm hợp chất hữu cơ tạp chức phổ biến nhất trong giới thực vật và đóng vai trò nền tảng cung cấp lương thực thực phẩm. Dựa vào phản ứng thuỷ phân, người ta chia cacbohiđrat thành monosaccarit, đisaccarit và polisaccarit. Trong các chất sau đây, chất nào là đisaccarit?

[A.] Đường saccarozơ (đường mía).
B. Đường nho glucozơ.
C. Đường hoa quả fructozơ.
D. Xenlulozơ có trong bông nõn.

**Dẫn giải lan man:** Saccarozơ có công thức phân tử C12H22O11 khi thuỷ phân tạo ra một glucozơ và một fructozơ nên là đisaccarit...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 58 từ, liệt kê quá nhiều tên gọi phụ (gluxit, saccarit) làm loãng câu hỏi.
- Dùng danh pháp cũ thuần Việt phiên âm (glucozơ, fructozơ, saccarozơ, xenlulozơ).
- Phương án đính kèm mở ngoặc giải thích không đồng nhất (đường mía, đường nho...).

*Thống kê số từ:* Đề bài: 60 từ | Các phương án: 20 từ | Lời giải & Phân tích: 64 từ | **Tổng: 144 từ**

---

### Câu 7: Cấu tạo phân tử monosaccharide — Đồng phân glucose và fructose
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Glucose là chất dinh dưỡng quan trọng dùng làm thuốc tăng lực trong y tế. Các nghiên cứu hoá học thực nghiệm chứng minh rằng ở trạng thái dung dịch cân bằng, ngoài các dạng mạch vòng thì glucose tồn tại một lượng nhỏ dạng mạch hở. Cấu trúc mạch hở này có đặc điểm về các nhóm chức hoá học như thế nào?

[A.] Phân tử gồm một nhóm andehit ở đầu mạch và 5 nhóm hiđroxyl liền kề.
B. Phân tử gồm một nhóm xeton ở vị trí C2 và 5 nhóm hiđroxyl phân bố đều.
C. Phân tử có chứa hai nhóm chức andehit đối xứng nhau ở hai đầu mạch cacbon.
D. Phân tử chỉ có các nhóm chức ancol đơn thuần không có nhóm chức cacbonyl.

**Dẫn giải lan man:** Dạng mạch hở của glucozơ có công thức cấu tạo thu gọn là CH2OH[CHOH]4CHO có 5 nhóm OH kề nhau và 1 nhóm CHO...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 54 từ, nhắc đến thuốc tăng lực y tế không liên quan đến cấu trúc nhóm chức.
- Dùng danh pháp cũ: 'andehit', 'xeton', 'hiđroxyl', 'ancol'.
- Độ dài các phương án rất dài (14-16 từ/phương án).

*Thống kê số từ:* Đề bài: 64 từ | Các phương án: 67 từ | Lời giải & Phân tích: 61 từ | **Tổng: 192 từ**

---

### Câu 8: Hoá học disaccharide — Cấu trúc liên kết glycoside đường mía
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Saccarozơ là loại đường phổ biến nhất trong đời sống, được sản xuất chủ yếu từ mía đường hoặc củ cải đường. Về mặt hoá học lập thể, phân tử saccarozơ được hình thành do sự kết hợp giữa một gốc alpha-glucozơ và một gốc beta-fructozơ thông qua cầu nối nguyên tử oxy gọi là liên kết gì?

[A.] Liên kết alpha-1,2-glicozit qua nguyên tử oxi.
B. Liên kết alpha-1,4-glicozit tương tự như trong maltose.
C. Liên kết beta-1,4-glicozit tương tự như trong xenlulozơ.
D. Liên kết photphodiester giữa hai gốc đường.

**Dẫn giải lan man:** Saccarozơ không có nhóm OH hemiaxetal tự do do liên kết glycoside tạo thành giữa C1 của alpha-glucozơ và C2 của beta-fructozơ...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 54 từ, thông tin củ cải đường và mía đường thừa thãi.
- Dùng chính tả cũ 'alpha-glucozơ', 'glicozit' thay vì $\alpha$-glucose, glycoside.
- Phương án D đưa liên kết photphodiester của acid nucleic vào câu hỏi carbohydrate là nhiễu không tương xứng.

*Thống kê số từ:* Đề bài: 58 từ | Các phương án: 34 từ | Lời giải & Phân tích: 65 từ | **Tổng: 157 từ**

---

### Câu 9: Cấu trúc polymer thiên nhiên — Hai thành phần của tinh bột
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Tinh bột trong các loại hạt ngũ cốc như gạo, ngô, khoai, sắn tồn tại dưới hai dạng thành phần cấu trúc khác biệt nhau về tính chất vật lí và khả năng hồ hoá là amilozơ và amilopectin. Điểm khác biệt mấu chốt về mặt cấu trúc hoá học phân tử giữa thành phần amilopectin so với amilozơ là gì?

[A.] Amilopectin có cấu trúc phân nhánh chứa thêm liên kết alpha-1,6-glicozit ở các điểm nhánh.
B. Amilopectin chỉ có cấu trúc mạch thẳng dài không phân nhánh xoắn hình lò xo.
C. Amilopectin được cấu tạo hoàn toàn từ các mắt xích beta-glucozơ liên kết với nhau.
D. Amilozơ tan tốt trong nước nóng còn amilopectin thì hoàn toàn không tan trong nước.

**Dẫn giải lan man:** Amilozơ chiếm khoảng 20-30% khối lượng tinh bột, có mạch không phân nhánh; amilopectin chiếm 70-80%, có cấu tạo phân nhánh...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 56 từ, liệt kê gạo, ngô, khoai, sắn không phục vụ bản chất hoá học.
- Dùng chính tả cũ 'amilozơ', 'amilopectin', 'alpha-1,6-glicozit'.
- Phương án D lẫn lộn giữa tính chất vật lí với đặc điểm cấu tạo phân tử được hỏi.

*Thống kê số từ:* Đề bài: 61 từ | Các phương án: 64 từ | Lời giải & Phân tích: 64 từ | **Tổng: 189 từ**

---

### Câu 10: Hợp chất đại phân tử cellulose — Cấu tạo nhóm chức và ứng dụng
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Cellulose hay xenlulozơ là thành phần chính cấu tạo nên màng tế bào thực vật, tạo nên bộ khung vững chắc cho thân cây gỗ. Khi tham gia phản ứng với axit nitric có xúc tác axit sunfuric đặc để sản xuất thuốc súng không khói xenlulozơ trinitrat, mỗi mắt xích glucozơ trong đại phân tử xenlulozơ tham gia phản ứng bằng bao nhiêu nhóm hiđroxyl (-OH) còn tự do?

[A.] 3 nhóm hiđroxyl tự do.
B. 2 nhóm hiđroxyl tự do.
C. 4 nhóm hiđroxyl tự do.
D. 5 nhóm hiđroxyl tự do.

**Dẫn giải lan man:** Công thức cấu tạo của xenlulozơ được viết dưới dạng [C6H7O2(OH)3]n, mỗi gốc C6H10O5 có 3 nhóm OH nên phản ứng tối đa với 3 phân tử HNO3...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 64 từ, lồng ghép phản ứng thuốc súng không khói khiến học sinh bị phân tán khỏi câu hỏi chính.
- Trộn lẫn thuật ngữ 'cellulose' và 'xenlulozơ', 'axit nitric', 'hiđroxyl'.
- Phương án lặp thừa từ 'nhóm hiđroxyl tự do'.

*Thống kê số từ:* Đề bài: 70 từ | Các phương án: 24 từ | Lời giải & Phân tích: 69 từ | **Tổng: 163 từ**

---

## Chương 3: Hợp chất chứa nitrogen

### Câu 11: Hợp chất hữu cơ chứa nitơ — Bậc của phân tử amin
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Khi thay thế một hay nhiều nguyên tử hiđro trong phân tử amoniac NH3 bằng các gốc hiđrocacbon ta thu được hợp chất amin. Khác với quy tắc tính bậc của ancol dựa vào nguyên tử cacbon liên kết với nhóm OH, bậc của amin được định nghĩa theo một quy tắc riêng biệt. Trong các công thức cấu tạo dưới đây, chất nào thuộc loại amin bậc hai?

[A.] Đimetylamin CH3-NH-CH3.
B. Etylamin CH3-CH2-NH2.
C. Trimetylamin (CH3)3N.
D. Isopropylamin CH3-CH(NH2)-CH3.

**Dẫn giải lan man:** Bậc của amin bằng số nguyên tử H trong phân tử NH3 bị thay thế bởi gốc hidrocacbon. CH3-NH-CH3 có 2 gốc CH3 gắn vào N nên là amin bậc 2...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ dài dòng giải thích sự khác nhau giữa bậc ancol và bậc amin.
- Dùng danh pháp cũ: 'amin', 'đimetylamin', 'etylamin', 'hiđrocacbon'.
- Công thức hoá học không viết chuẩn mhchem LaTeX.

*Thống kê số từ:* Đề bài: 69 từ | Các phương án: 12 từ | Lời giải & Phân tích: 65 từ | **Tổng: 146 từ**

---

### Câu 12: Phản ứng thế vào nhân thơm của amin thơm bậc một anilin
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Anilin (C6H5NH2) là một amin thơm tiêu biểu có nhiều ứng dụng trong công nghiệp tổng hợp phẩm nhuộm azo và dược phẩm. Do ảnh hưởng của đôi electron chưa liên kết trên nguyên tử nitơ đến mật độ electron của nhân thơm benzen, anilin phản ứng rất nhạy với dung dịch brom ở điều kiện thường. Hiện tượng quan sát được trong thí nghiệm này là gì?

[A.] Nước brom bị mất màu và đồng thời xuất hiện kết tủa trắng 2,4,6-tribromanilin.
B. Xuất hiện kết tủa màu vàng tươi tương tự như phản ứng của phenol với axit nitric đặc.
C. Dung dịch brom chuyển sang màu xanh tím đặc trưng của phức chất hữu cơ.
D. Không có hiện tượng gì xảy ra vì tính bazơ của anilin quá yếu không tác dụng được.

**Dẫn giải lan man:** Nhóm NH2 đẩy electron làm tăng mật độ electron ở các vị trí ortho và para làm anilin dễ tham gia phản ứng thế brom tạo kết tủa trắng...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 66 từ kể lể về phẩm nhuộm azo và dược phẩm.
- Dùng chữ 'anilin', 'brom', 'benzen', 'tribromanilin'.
- Phương án A quá dài (15 từ), các phương án khác dài dòng mang tính giải thích lan man.

*Thống kê số từ:* Đề bài: 68 từ | Các phương án: 69 từ | Lời giải & Phân tích: 67 từ | **Tổng: 204 từ**

---

### Câu 13: Hợp chất hữu cơ tạp chức amino axit — Cấu trúc ion lưỡng cực
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Amino axit là hợp chất hữu cơ tạp chức mà phân tử chứa đồng thời nhóm chức amino (-NH2) có tính bazơ và nhóm chức cacboxyl (-COOH) có tính axit. Do có sự tương tác tĩnh điện nội phân tử chuyển proton H+ từ nhóm cacboxyl sang nhóm amino, trạng thái tồn tại chủ yếu của amino axit trong dung dịch nước ở điều kiện pH sinh lí là gì?

[A.] Tồn tại chủ yếu dưới dạng ion lưỡng cực vừa mang điện tích dương vừa mang điện tích âm.
B. Tồn tại dưới dạng cation dương di chuyển về phía cực âm khi đặt vào điện trường.
C. Tồn tại dưới dạng anion tích điện âm di chuyển về phía cực dương của bình điện phân.
D. Tồn tại dạng phân tử trung hoà chưa điện li có công thức H2N-R-COOH.

**Dẫn giải lan man:** Do phản ứng trao đổi proton nội phân tử H2N-R-COOH biến thành ion lưỡng cực H3N+-R-COO- làm amino axit có nhiệt độ nóng chảy cao và tan tốt trong nước...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ, giảng giải lại lý thuyết tương tác proton nội phân tử trong đề bài.
- Các phương án quá dài dòng, lặp lại 'Tồn tại dưới dạng...' trung bình 16 từ/phương án.
- Dùng chữ 'amino axit', 'cacboxyl', 'bazơ'.

*Thống kê số từ:* Đề bài: 70 từ | Các phương án: 72 từ | Lời giải & Phân tích: 71 từ | **Tổng: 213 từ**

---

### Câu 14: Hợp chất peptit và protein — Số lượng liên kết peptit trong phân tử
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Peptit là những hợp chất chứa từ 2 đến 50 gốc alpha-amino axit liên kết với nhau bởi các liên kết peptit -CO-NH-. Khái niệm dipeptit, tripeptit, tetrapeptit được gọi dựa theo số lượng gốc amino axit tạo nên mạch peptit đó. Hỏi trong một phân tử tripeptit mạch hở bất kì thì có chứa bao nhiêu liên kết peptit?

[A.] Có đúng 2 liên kết peptit.
B. Có 3 liên kết peptit bằng số gốc.
C. Có 1 liên kết peptit duy nhất.
D. Có 4 liên kết peptit trong mạch.

**Dẫn giải lan man:** Số liên kết peptit luôn bằng số gốc amino axit trừ đi 1. Do đó tripeptit gồm 3 gốc thì có 3 - 1 = 2 liên kết peptit...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 54 từ, định nghĩa lại peptit và dipeptit không cần thiết.
- Phương án lặp từ 'Có ... liên kết peptit'.
- Dùng danh pháp cũ 'peptit', 'amino axit'.

*Thống kê số từ:* Đề bài: 60 từ | Các phương án: 32 từ | Lời giải & Phân tích: 58 từ | **Tổng: 150 từ**

---

### Câu 15: Phản ứng màu đặc trưng của peptit và protein — Thử nghiệm biure
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong phòng thí nghiệm hoá học hữu cơ, phản ứng màu biure là một phản ứng rất đặc trưng dùng để nhận biết các hợp chất có chứa liên kết peptit khi cho tác dụng với kết tủa đồng(II) hiđroxit Cu(OH)2 trong môi trường kiềm tạo phức màu tím. Trong số các chất hữu cơ sau đây, chất nào không có khả năng tham gia phản ứng màu biure?

[A.] Đipeptit Gly-Ala mạch hở.
B. Tripeptit Gly-Ala-Val mạch hở.
C. Dung dịch lòng trắng trứng (chứa protein albumin).
D. Hợp chất tripeptit Gly-Gly-Gly.

**Dẫn giải lan man:** Điều kiện để có phản ứng màu biure là phân tử peptit phải có từ 2 liên kết peptit trở lên. Đipeptit chỉ có 1 liên kết peptit nên không tạo được phức chất màu tím...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ mô tả chi tiết phản ứng và màu tím của phức chất ngay trong đề.
- Dùng chữ 'biure', 'đipeptit', 'hiđroxit'.
- Phương án A và B thêm chữ 'mạch hở' dông dài không cần thiết.

*Thống kê số từ:* Đề bài: 69 từ | Các phương án: 24 từ | Lời giải & Phân tích: 74 từ | **Tổng: 167 từ**

---

## Chương 4: Polymer

### Câu 16: Đại cương về hợp chất cao phân tử — Đơn vị cấu tạo nên polymer
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Hợp chất polymer hay còn gọi là hợp chất cao phân tử đóng vai trò là vật liệu nền tảng cho ngành công nghiệp chất dẻo, tơ sợi và cao su hiện đại. Về mặt bản chất cấu trúc vi mô, các phân tử polymer khổng lồ được tạo thành từ vô số các đơn vị nhỏ có cấu tạo hoá học giống nhau lặp đi lặp lại nhiều lần. Trong hoá học polymer, các đơn vị cấu trúc nhỏ lặp lại này được gọi tên chính xác là gì?

[A.] Mắt xích của phân tử polime.
B. Monome ban đầu tham gia phản ứng trùng hợp.
C. Các phân tử oligome mạch ngắn.
D. Nhóm định chức của polime.

**Dẫn giải lan man:** Mắt xích là phần lặp lại trong mạch polime, ví dụ polietilen có mắt xích là -CH2-CH2- còn monome là CH2=CH2...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ với những từ ngữ cảm thán 'vô số', 'khổng lồ'.
- Dùng chữ 'polime', 'monome', 'oligome'.
- Phương án độ dài không cân đối (A dài 7 từ, B dài 8 từ, C dài 6 từ, D dài 6 từ).

*Thống kê số từ:* Đề bài: 90 từ | Các phương án: 30 từ | Lời giải & Phân tích: 63 từ | **Tổng: 183 từ**

---

### Câu 17: Phương pháp điều chế polymer — Phản ứng trùng hợp tạo cao phân tử
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Để sản xuất các loại nhựa nhiệt dẻo phổ biến như PE, PP hay PVC, người ta tiến hành quá trình kết hợp liên tiếp nhiều phân tử nhỏ giống nhau hoặc tương tự nhau thành phân tử rất lớn thông qua phản ứng hoá học gọi là phản ứng trùng hợp. Để một monome có thể tham gia được phản ứng trùng hợp thì cấu tạo phân tử của nó cần thoả mãn điều kiện tiên quyết nào trong số các chất dưới đây?

[A.] Vinyl clorua CH2=CH-Cl có chứa liên kết đôi C=C kém bền.
B. Etyl clorua CH3-CH2-Cl là dẫn xuất halogen no.
C. Axit hiđroxiaxetic chứa hai nhóm chức khác loại.
D. Axit aminoaxetic (glyxin) tham gia trùng ngưng.

**Dẫn giải lan man:** Điều kiện monome trùng hợp là có liên kết bội hoặc vòng kém bền có thể mở vòng. CH2=CH-Cl có liên kết đôi nên trùng hợp tạo poli(vinyl clorua)...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ, giảng giải lại lý thuyết điều chế nhựa PE, PP trong đề bài.
- Công thức không viết LaTeX, dùng tên cũ 'vinyl clorua', 'etyl clorua', 'axit aminoaxetic'.
- Phương án A quá dài (11 từ), mang tính gợi ý đáp án ngay trong phương án.

*Thống kê số từ:* Đề bài: 85 từ | Các phương án: 38 từ | Lời giải & Phân tích: 77 từ | **Tổng: 200 từ**

---

### Câu 18: Vật liệu polime và ứng dụng — Phân loại chất dẻo, tơ và cao su
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Các vật liệu polime đóng vai trò cách mạng hoá đời sống loài người thế kỉ 20 được chia thành các nhóm chính bao gồm chất dẻo, tơ sợi, cao su và keo dán dựa trên cơ sở tính chất cơ lí đặc trưng của từng loại. Thuật ngữ 'chất dẻo' trong hoá học vật liệu được định nghĩa chính xác dựa trên thuộc tính cơ học nổi bật nào của polime thành phần?

[A.] Có tính dẻo tức là bị biến dạng dưới tác dụng của nhiệt độ và áp suất rồi giữ nguyên biến dạng đó.
B. Có tính đàn hồi vượt trội tức là biến dạng khi có lực rồi tự động co trở lại trạng thái ban đầu.
C. Có độ bền cơ học cao và khả năng dễ dàng kéo thành các sợi nhỏ mảnh bền chắc.
D. Hoàn toàn không bị biến dạng dưới bất kì tác dụng lực cơ học bên ngoài nào.

**Dẫn giải lan man:** Chất dẻo là những vật liệu polime có tính dẻo. Cần phân biệt tính dẻo với tính đàn hồi của cao su...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ, kể lể về 'cách mạng hoá đời sống loài người'.
- Các phương án quá dài dòng (trung bình 20 từ/phương án), diễn giải lan man.
- Dùng chính tả cũ 'polime'.

*Thống kê số từ:* Đề bài: 74 từ | Các phương án: 86 từ | Lời giải & Phân tích: 56 từ | **Tổng: 216 từ**

---

### Câu 19: Vật liệu dệt may — Phân loại tơ tự nhiên, nhân tạo và tổng hợp
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Trong ngành công nghiệp dệt may hiện đại, các loại tơ sợi được phân chia theo nguồn gốc xuất xứ thành ba nhóm: tơ thiên nhiên, tơ tổng hợp và tơ bán tổng hợp (tơ nhân tạo có nguồn gốc chế biến từ xenlulozơ). Trong số các loại tơ sợi thông dụng dưới đây, loại tơ nào thuộc phân nhóm tơ bán tổng hợp?

[A.] Tơ visco sản xuất từ gỗ và bông.
B. Tơ tằm lấy từ kén tằm dâu.
C. Tơ nilon-6,6 tổng hợp từ hexametylendiamin.
D. Tơ olon (nitron) trùng hợp từ vinyl xianua.

**Dẫn giải lan man:** Tơ visco và tơ axetat là tơ nhân tạo vì dùng polime thiên nhiên xenlulozơ chế biến bằng phương pháp hoá học...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 55 từ, đưa định nghĩa tơ bán tổng hợp vào ngay trong đề bài làm giảm tính đánh giá.
- Dùng chữ 'xenlulozơ', 'visco', 'nilon-6,6', 'vinyl xianua'.
- Phương án đính kèm đuôi giải thích không đồng nhất.

*Thống kê số từ:* Đề bài: 64 từ | Các phương án: 33 từ | Lời giải & Phân tích: 60 từ | **Tổng: 157 từ**

---

### Câu 20: Hoá học các hợp chất đàn hồi — Cấu tạo cao su thiên nhiên
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Cây cao su Hevea brasiliensis mọc nhiều ở vùng Đông Nam Bộ và Tây Nguyên của nước ta cung cấp mủ cao su thiên nhiên có giá trị xuất khẩu kinh tế rất cao. Nghiên cứu thành phần cấu tạo hoá học của cao su tự nhiên cho thấy nó là một polime thiên nhiên mạch thẳng có cấu hình cis. Đơn vị monome cơ sở cấu thành nên đại phân tử cao su tự nhiên này là gì?

[A.] Isopren (2-metylbuta-1,3-đien).
B. Butađien-1,3 dùng để sản xuất cao su buna.
C. Cloropren dùng làm cao su nhân tạo chịu dầu.
D. Stiren dùng sản xuất nhựa polistiren.

**Dẫn giải lan man:** Mủ cao su chứa 95% poliisopren có cấu hình cis. Monome cấu tạo nên cao su tự nhiên là isopren...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ với thông tin địa lí (Tây Nguyên, Đông Nam Bộ) và kinh tế xuất khẩu không phục vụ câu hỏi hoá học.
- Dùng danh pháp cũ 'isopren', '2-metylbuta-1,3-đien', 'cloropren', 'stiren'.
- Phương án kéo dài giải thích ứng dụng (A dài 3 từ, B dài 8 từ, C dài 8 từ, D dài 5 từ).

*Thống kê số từ:* Đề bài: 79 từ | Các phương án: 29 từ | Lời giải & Phân tích: 78 từ | **Tổng: 186 từ**

---

## Chương 5: Pin điện và điện phân

### Câu 21: Điện hoá học — Khái niệm cặp oxi hoá khử kim loại
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong điện hoá học và lí thuyết về phản ứng oxi hoá - khử, sự chuyển đổi giữa nguyên tử kim loại tự do và ion kim loại tương ứng trong dung dịch nước đóng vai trò quyết định chiều của phản ứng điện hoá. Quy ước quốc tế viết cặp oxi hoá - khử theo dạng dạng oxi hoá/dạng khử. Với cặp oxi hoá - khử của kim loại đồng Cu2+/Cu thì tiểu phân nào đóng vai trò là dạng oxi hoá?

[A.] Cation đồng Cu2+ mang điện tích dương.
B. Kim loại đồng Cu ở trạng thái đơn chất tự do.
C. Ion đồng hoá trị một Cu+ trong dung dịch.
D. Hợp chất kết tủa hiđroxit Cu(OH)2.

**Dẫn giải lan man:** Quy ước viết dạng oxi hoá ở trên (hoặc trước), dạng khử ở dưới (hoặc sau). Do đó Cu2+ là dạng oxi hoá, Cu là dạng khử...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ dài dòng kể lể về chuyển đổi nguyên tử và ion kim loại.
- Công thức ion không dùng LaTeX (Cu2+/Cu thay vì $\ce{Cu^{2+}/Cu}$).
- Phương án kéo dài rườm rà (A dài 7 từ, B dài 9 từ).

*Thống kê số từ:* Đề bài: 83 từ | Các phương án: 37 từ | Lời giải & Phân tích: 68 từ | **Tổng: 188 từ**

---

### Câu 22: Dãy điện hoá kim loại và dự đoán chiều phản ứng oxi hoá khử
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Biết thế điện cực chuẩn của cặp sắt E0(Fe2+/Fe) = -0,44 V và của cặp đồng E0(Cu2+/Cu) = +0,34 V đo ở điều kiện chuẩn 25 độ C, nồng độ ion 1M và áp suất 1 bar so với điện cực hiđro tiêu chuẩn. Căn cứ theo quy tắc alpha hoặc sự chênh lệch thế điện cực, phản ứng oxi hoá - khử nào dưới đây có thể tự phát sinh công và diễn ra theo chiều thuận?

[A.] Thanh kim loại sắt Fe đẩy ion đồng Cu2+ ra khỏi dung dịch theo phản ứng Fe + Cu2+ -> Fe2+ + Cu.
B. Thanh kim loại đồng Cu đẩy ion sắt Fe2+ ra khỏi dung dịch theo phản ứng Cu + Fe2+ -> Cu2+ + Fe.
C. Ion Fe2+ oxi hoá ion Cu2+ tạo thành các ion hoá trị mới.
D. Cả hai kim loại cùng bị hoà tan tạo hỗn hợp cation.

**Dẫn giải lan man:** Quy tắc alpha: chất oxi hoá của cặp có thế điện cực lớn hơn (Cu2+) sẽ tác dụng với chất khử của cặp có thế nhỏ hơn (Fe)...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ liệt kê điều kiện đo nhiệt độ, áp suất, điện cực hiđro không cần thiết cho câu hỏi trắc nghiệm.
- Công thức phương trình hoá học dài dòng, nhồi nhét chữ 'Thanh kim loại sắt Fe...' vào phương án.
- Không dùng định dạng LaTeX cho thế điện cực và phản ứng.

*Thống kê số từ:* Đề bài: 78 từ | Các phương án: 75 từ | Lời giải & Phân tích: 83 từ | **Tổng: 236 từ**

---

### Câu 23: Cấu tạo và cơ chế hoạt động của pin điện hoá Galvani
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Pin điện hoá Đanien - Gianvani (Zn - Cu) là mô hình kinh điển để tìm hiểu sự chuyển hoá trực tiếp hoá năng thành điện năng nhờ phản ứng oxi hoá - khử diễn ra ở hai bán pin cách nhau bởi cầu muối. Ở điện cực âm (anot) làm bằng thanh kẽm nhúng trong dung dịch muối kẽm sunfat, quá trình bán phản ứng điện hoá nào thực tế xảy ra?

[A.] Quá trình oxi hoá kẽm Zn -> Zn2+ + 2e giải phóng electron vào mạch ngoài.
B. Quá trình khử ion đồng Cu2+ + 2e -> Cu bám vào thanh catot.
C. Quá trình khử ion kẽm Zn2+ + 2e -> Zn nhận electron.
D. Quá trình oxi hoá thanh đồng Cu -> Cu2+ + 2e.

**Dẫn giải lan man:** Tại anot (cực âm) kẽm có tính khử mạnh hơn nhường electron, xảy ra sự oxi hoá Zn thành Zn2+...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ mô tả pin Đanien - Gianvani và cầu muối dài dòng.
- Dùng chữ 'anot', 'catot' phiên âm cũ.
- Phương án kéo dài tới 14 từ, kèm giải thích 'giải phóng electron vào mạch ngoài'.

*Thống kê số từ:* Đề bài: 73 từ | Các phương án: 57 từ | Lời giải & Phân tích: 58 từ | **Tổng: 188 từ**

---

### Câu 24: Công nghệ luyện kim — Phương pháp điện phân hợp chất nóng chảy
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong công nghiệp luyện kim hiện đại, điện phân hợp chất nóng chảy là phương pháp duy nhất có thể cung cấp lực khử cực mạnh của dòng điện một chiều để tách các kim loại có tính khử rất mạnh ra khỏi hợp chất oxide hay muối halogenua tương ứng. Nhóm kim loại nào dưới đây bắt buộc phải điều chế bằng phương pháp điện phân nóng chảy?

[A.] Các kim loại có tính khử rất mạnh gồm kim loại kiềm, kiềm thổ và nhôm (Na, Mg, Al).
B. Các kim loại hoạt động trung bình như sắt Fe, kẽm Zn, niken Ni.
C. Các kim loại hoạt động hoá học yếu như đồng Cu, bạc Ag, thuỷ ngân Hg.
D. Tất cả các kim loại tồn tại trong vỏ Trái Đất.

**Dẫn giải lan man:** Cation kim loại mạnh như Na+, Mg2+, Al3+ rất khó bị khử, trong dung dịch nước thì H2O sẽ bị khử trước. Do đó phải điện phân nóng chảy...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ dài dòng, kể lể về 'công nghệ luyện kim hiện đại'.
- Phương án quá dài (trung bình 15 từ/phương án).
- Phương án D đưa phương án phi lí làm nhiễu kém chất lượng.

*Thống kê số từ:* Đề bài: 69 từ | Các phương án: 64 từ | Lời giải & Phân tích: 66 từ | **Tổng: 199 từ**

---

### Câu 25: Hiện tượng điện phân dung dịch chất điện li trong nước
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Khi cho dòng điện một chiều đi qua bình điện phân chứa dung dịch đồng(II) sunfat CuSO4 có sử dụng hai điện cực bằng than chì (graphite) trơ không tan, các ion trong dung dịch sẽ di chuyển về các điện cực trái dấu và xảy ra các phản ứng trao đổi electron. Bán phản ứng khử điện hoá nào sẽ xảy ra trước tiên tại bề mặt cực âm (catot)?

[A.] Ion Cu2+ nhận electron bị khử thành kim loại đồng Cu bám lên điện cực: Cu2+ + 2e -> Cu.
B. Phân tử nước bị khử giải phóng khí hiđro theo phương trình: 2H2O + 2e -> H2 + 2OH-.
C. Nước bị oxi hoá ở cực catot giải phóng khí oxi và ion proton H+.
D. Ion sunfat SO4(2-) bị khử thành khí SO2.

**Dẫn giải lan man:** Tại catot xảy ra sự khử Cu2+ thành Cu vì thế điện cực của Cu2+/Cu (+0,34V) lớn hơn thế điện cực khử của nước (-0,41V ở pH=7)...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ dông dài, kể lể về di chuyển ion và than chì graphite.
- Các phương án quá dài dòng, lặp lại 'Ion Cu2+ nhận electron bị khử...' dài 18 từ.
- Dùng chữ 'catot', 'sunfat', 'hiđro'.

*Thống kê số từ:* Đề bài: 71 từ | Các phương án: 66 từ | Lời giải & Phân tích: 65 từ | **Tổng: 202 từ**

---

## Chương 6: Đại cương về kim loại

### Câu 26: Cấu tạo tinh thể kim loại — Bản chất liên kết kim loại
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong mạng tinh thể của các đơn chất kim loại ở thể rắn, các nguyên tử kim loại nhường electron hoá trị để trở thành các ion dương nằm ở các nút mạng tinh thể, còn các electron hoá trị thì chuyển động tự do tương đối trong toàn bộ thể tích tinh thể. Lực tương tác đóng vai trò liên kết giữ các phần tử tinh thể lại với nhau trong liên kết kim loại là gì?

[A.] Lực hút tĩnh điện giữa các electron hoá trị tự do với các ion dương kim loại ở nút mạng.
B. Lực hút tĩnh điện giữa cation kim loại với các anion phi kim tích điện âm.
C. Lực liên kết cộng hoá trị do các cặp electron dùng chung phân bố đều.
D. Lực đẩy tương hỗ giữa các ion dương kim loại cùng dấu.

**Dẫn giải lan man:** Bản chất liên kết kim loại là lực hút tĩnh điện giữa các electron tự do mang điện tích âm và các cation kim loại mang điện tích dương...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ, giải thích cấu tạo tinh thể trước khi hỏi bản chất lực liên kết.
- Phương án kéo dài từ 14 đến 17 từ mỗi phương án.
- Phương án D đưa lực đẩy vào câu hỏi về liên kết là phương án nhiễu vô lý.

*Thống kê số từ:* Đề bài: 78 từ | Các phương án: 67 từ | Lời giải & Phân tích: 77 từ | **Tổng: 222 từ**

---

### Câu 27: Tính chất vật lí chung của kim loại và nguyên nhân bản chất
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Tất cả các kim loại trong bảng tuần hoàn mặc dù có những điểm khác biệt về màu sắc, nhiệt độ nóng chảy và khối lượng riêng nhưng đều thể hiện bốn tính chất vật lí chung nổi bật là tính dẻo dễ dát mỏng, tính dẫn điện, tính dẫn nhiệt và có ánh kim lấp lánh. Yếu tố cấu trúc vi mô quyết định trực tiếp tới bốn tính chất vật lí chung này là gì?

[A.] Sự có mặt và chuyển động của các electron tự do trong toàn bộ mạng tinh thể kim loại.
B. Do cấu trúc tinh thể lập phương tâm diện của đa số kim loại.
C. Do các ion dương kim loại có kích thước bán kính tương đối nhỏ.
D. Do mật độ electron hoá trị ở lớp vỏ ngoài cùng rất thấp.

**Dẫn giải lan man:** Bốn tính chất vật lí chung của kim loại đều do các electron tự do trong mạng tinh thể gây ra. Các electron tự do truyền nhiệt, dẫn điện, phản xạ ánh sáng...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 66 từ, liệt kê dông dài các tính chất riêng và chung.
- Các phương án dài dòng, nhồi nhét thuật ngữ 'lập phương tâm diện' không cần thiết.
- Dùng cụm từ hoa mỹ không chuẩn mực khoa học.

*Thống kê số từ:* Đề bài: 77 từ | Các phương án: 64 từ | Lời giải & Phân tích: 73 từ | **Tổng: 214 từ**

---

### Câu 28: Các phương pháp điều chế kim loại — Phương pháp nhiệt luyện truyền thống
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Nhiệt luyện là một trong những phương pháp điều chế kim loại cổ xưa nhất trong lịch sử văn minh nhân loại, đóng vai trò nền tảng cho thời kì đồ đồng và đồ sắt. Nguyên tắc của phương pháp này là sử dụng các chất khử rẻ tiền, dễ kiếm trong công nghiệp để khử các ion kim loại trong oxide ở nhiệt độ cao. Chất khử thông dụng nhất được sử dụng trong lò cao luyện gang thép là:

[A.] Khí cacbon monooxit CO và than cốc C.
B. Kim loại nhôm Al dạng bột mịn trong phản ứng nhiệt nhôm.
C. Kim loại kiềm natri Na có tính khử cực mạnh.
D. Khí cacbonic CO2 từ quá trình đốt cháy nhiên liệu.

**Dẫn giải lan man:** Trong công nghiệp luyện kim, C và CO là hai chất khử chủ yếu vì có sẵn từ than cốc và có giá thành rất rẻ so với các chất khử kim loại khác...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ nói về thời kì đồ đồng, đồ sắt và văn minh nhân loại.
- Dùng chữ 'cacbon monooxit', 'cacbonic'.
- Phương án D đưa chất oxi hoá CO2 vào câu hỏi về chất khử là nhiễu phi lí.

*Thống kê số từ:* Đề bài: 81 từ | Các phương án: 44 từ | Lời giải & Phân tích: 74 từ | **Tổng: 199 từ**

---

### Câu 29: Vật liệu hợp kim kim loại — Thành phần của gang và thép
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Trong thực tế đời sống và kĩ thuật xây dựng cơ khí, kim loại nguyên chất thường có độ bền cơ học không cao nên hiếm khi được sử dụng đơn lẻ mà thường được chế tạo thành các hợp kim có tính chất ưu việt hơn. Hai loại vật liệu nền tảng nhất là gang và thép thực chất là hợp kim của kim loại sắt Fe với nguyên tố phi kim chủ đạo nào?

[A.] Phi kim cacbon C với hàm lượng khác nhau ở gang và thép.
B. Nguyên tố silic Si có trong cát và quặng tự nhiên.
C. Kim loại crom Cr tạo độ sáng bóng chống gỉ.
D. Kim loại niken Ni tăng độ bền dẻo cơ học.

**Dẫn giải lan man:** Gang là hợp kim Fe-C chứa 2-5% C; Thép là hợp kim Fe-C chứa dưới 2% C. Carbon là thành phần bắt buộc thứ hai quyết định độ cứng...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 64 từ với thông tin kĩ thuật cơ khí dông dài.
- Dùng chữ 'cacbon', 'silic', 'crom', 'niken'.
- Phương án kéo dài rườm rà (A dài 12 từ).

*Thống kê số từ:* Đề bài: 76 từ | Các phương án: 48 từ | Lời giải & Phân tích: 58 từ | **Tổng: 182 từ**

---

### Câu 30: Chống ăn mòn kim loại — Phương pháp bảo vệ điện hoá
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Vỏ tàu thuỷ đi biển làm bằng thép cacbon chịu sự ăn mòn điện hoá học rất khốc liệt của môi trường nước biển giàu muối natri clorua dẫn điện tốt. Để bảo vệ vỏ tàu khỏi bị gỉ sét thủng đáy, các kĩ sư đóng tàu thường sử dụng phương pháp bảo vệ điện hoá bằng cách gắn các tấm kim loại đóng vai trò anot hi sinh lên thân vỏ tàu. Kim loại nào sau đây thích hợp nhất?

[A.] Tấm kim loại kẽm Zn có tính khử mạnh hơn sắt.
B. Tấm kim loại đồng Cu có độ bền chống ăn mòn cao trong nước muối.
C. Tấm kim loại thiếc Sn thường dùng tráng lên bề mặt sắt tây.
D. Tấm kim loại niken Ni có khả năng tạo màng thụ động hoá.

**Dẫn giải lan man:** Kẽm có thế điện cực âm hơn sắt nên đóng vai trò là cực âm (anot) bị ăn mòn trước, bảo vệ sắt thép đóng vai trò là catot...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ, kể lể về 'kĩ sư đóng tàu', 'thủng đáy tàu'.
- Phương án kéo dài với lời giải thích đi kèm không đồng nhất.
- Dùng chữ 'natri clorua', 'anot hi sinh'.

*Thống kê số từ:* Đề bài: 81 từ | Các phương án: 56 từ | Lời giải & Phân tích: 63 từ | **Tổng: 200 từ**

---

## Chương 7: Nguyên tố nhóm IA và nhóm IIA

### Câu 31: Hoá học kim loại nhóm IA — Phương pháp bảo quản kim loại kiềm
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Các kim loại nhóm IA như liti, natri, kali có thế điện cực chuẩn rất âm và năng lượng ion hoá thứ nhất rất nhỏ nên có tính khử mạnh nhất trong tất cả các kim loại. Ở điều kiện thường, chúng phản ứng nhanh chóng với oxi trong không khí và phản ứng mãnh liệt với nước. Do đó trong phòng thí nghiệm hoá học, người ta bắt buộc phải bảo quản natri bằng cách ngâm chìm hoàn toàn trong chất lỏng nào?

[A.] Ngâm ngập trong dầu hoả khan.
B. Ngâm trong nước cất tinh khiết cách li với không khí.
C. Ngâm trong dung dịch cồn etylic 96 độ.
D. Ngâm trong dung dịch nước xút natri hiđroxit.

**Dẫn giải lan man:** Natri có phản ứng mãnh liệt với H2O và cồn tạo khí H2 cháy nổ. Dầu hoả gồm các ankan không có phản ứng và ngăn cản tiếp xúc với không khí...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ, nhắc lại kiến thức thế điện cực và năng lượng ion hoá dông dài.
- Dùng chữ 'liti', 'natri', 'kali', 'cồn etylic', 'nước xút'.
- Phương án kéo dài rườm rà (A dài 6 từ, B dài 10 từ).

*Thống kê số từ:* Đề bài: 84 từ | Các phương án: 37 từ | Lời giải & Phân tích: 73 từ | **Tổng: 194 từ**

---

### Câu 32: Công nghiệp sản xuất soda — Quá trình hoá học Solvay
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Phương pháp Solvay là quy trình công nghệ hoá học vĩ đại phát minh vào thế kỉ 19 để sản xuất natri cacbonat (soda) từ nguồn nguyên liệu tự nhiên dồi dào là đá vôi, muối ăn, amoniac và nước. Ở giai đoạn tạo thành sản phẩm trung gian quan trọng nhất trong tháp cacbonat hoá, khi làm lạnh dung dịch thì muối nào sẽ bị kết tinh kết tủa tách ra đầu tiên nhờ có độ tan tương đối kém?

[A.] Natri hiđrocacbonat NaHCO3 có độ tan nhỏ nhất khi làm lạnh.
B. Natri cacbonat Na2CO3 tan tốt trong nước ở nhiệt độ thấp.
C. Amoni clorua NH4Cl đóng vai trò là phân bón phụ phẩm.
D. Canxi clorua CaCl2 tạo thành từ giai đoạn thu hồi khí amoniac.

**Dẫn giải lan man:** Phản ứng: NaCl + NH3 + CO2 + H2O <=> NaHCO3 + NH4Cl. Do NaHCO3 ít tan nhất nên kết tủa, sau đó nung NaHCO3 thu được Na2CO3...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ với những từ ngữ tán tụng 'quy trình công nghệ vĩ đại phát minh thế kỉ 19'.
- Dùng chữ 'natri cacbonat', 'amoniac', 'amoni clorua'.
- Phương án kéo dài từ 11 đến 12 từ.

*Thống kê số từ:* Đề bài: 81 từ | Các phương án: 49 từ | Lời giải & Phân tích: 65 từ | **Tổng: 195 từ**

---

### Câu 33: Phép thử màu ngọn lửa — Nhận biết ion kim loại kiềm thổ
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Phép thử ngọn lửa là một phương pháp phân tích định tính quang phổ phát xạ đơn giản nhưng vô cùng hiệu quả trong hoá học vô cơ để nhận dạng ion kim loại dựa trên bước sóng ánh sáng phát ra khi các electron bị kích thích rơi về trạng thái cơ bản. Khi đưa một mẫu muối của kim loại canxi sạch vào ngọn lửa không màu của đèn khí thì ngọn lửa sẽ chuyển sang màu gì?

[A.] Ngọn lửa cháy có màu đỏ cam đặc trưng của canxi.
B. Ngọn lửa có màu vàng tươi rực rỡ của natri.
C. Ngọn lửa có màu tím hoa cà của kali.
D. Ngọn lửa có màu đỏ son thẫm của stronti.

**Dẫn giải lan man:** Màu ngọn lửa của các ion kim loại: Li+ đỏ tía, Na+ vàng, K+ tím, Ca2+ đỏ cam, Sr2+ đỏ son, Ba2+ lục...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ giải thích dài dòng lý thuyết quang phổ phát xạ và bước sóng ánh sáng.
- Dùng chữ 'canxi', 'natri', 'kali', 'stronti'.
- Phương án kéo dài lặp từ 'Ngọn lửa cháy có màu...'.

*Thống kê số từ:* Đề bài: 80 từ | Các phương án: 43 từ | Lời giải & Phân tích: 59 từ | **Tổng: 182 từ**

---

### Câu 34: Phân loại nước cứng trong tự nhiên và công nghiệp
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Nước cứng tự nhiên được phân loại dựa trên thành phần hoá học của các anion gốc axit đi kèm với hai cation kim loại canxi Ca2+ và magie Mg2+. Giả sử trong một phòng thí nghiệm phân tích hoá học nước, người ta tiến hành xét nghiệm một mẫu nước khoáng và nhận thấy mẫu này chỉ chứa các cation Ca2+, Mg2+ cùng các anion Cl- và SO4(2-), không chứa ion HCO3-. Mẫu nước này có tính cứng thuộc loại nào?

[A.] Nước có tính cứng vĩnh cửu vì không thể làm mềm bằng cách đun sôi.
B. Nước có tính cứng tạm thời vì dễ dàng tạo cặn vôi khi đun nóng.
C. Nước có tính cứng toàn phần do chứa hỗn hợp nhiều muối vô cơ.
D. Nước hoàn toàn mềm không gây tác hại cho nồi hơi công nghiệp.

**Dẫn giải lan man:** Nước cứng tạm thời do muối hydrogencarbonate gây ra; nước cứng vĩnh cửu do muối chloride, sulfate gây ra; nước cứng toàn phần có cả hai loại muối...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 66 từ dài dòng giải thích bối cảnh xét nghiệm phòng thí nghiệm.
- Công thức ion viết không chuẩn LaTeX (SO4(2-) thay vì $\ce{SO4^{2-}}$).
- Phương án A quá dài (15 từ), lặp lại lời giải thích.

*Thống kê số từ:* Đề bài: 82 từ | Các phương án: 61 từ | Lời giải & Phân tích: 66 từ | **Tổng: 209 từ**

---

### Câu 35: Kĩ thuật xử lí nước cứng — Hoá chất kết tủa cation kim loại
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Nguyên tắc chung của mọi phương pháp hoá học làm mềm nước cứng là làm giảm nồng độ của hai cation Ca2+ và Mg2+ bằng cách chuyển chúng về dạng kết tủa không tan hoặc giữ chúng lại trên cột nhựa trao đổi ion. Để xử lí triệt để một nguồn nước cứng chưa rõ thành phần chứa cả tính cứng tạm thời lẫn vĩnh cửu, hoá chất công nghiệp rẻ tiền nào dưới đây là lựa chọn vạn năng tốt nhất?

[A.] Dùng muối soda natri cacbonat Na2CO3 hoặc natri photphat Na3PO4.
B. Dùng axit clohiđric HCl đậm đặc để hoà tan cặn bám.
C. Dùng muối ăn natri clorua NaCl nồng độ cao.
D. Dùng dung dịch thạch cao canxi sunfat CaSO4 bão hoà.

**Dẫn giải lan man:** Na2CO3 tạo kết tủa CaCO3 và MgCO3 tách Ca2+ và Mg2+ ra khỏi nước cứng tạm thời, vĩnh cửu và toàn phần...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 67 từ với từ ngữ quảng cáo 'lựa chọn vạn năng tốt nhất'.
- Dùng chữ 'soda natri cacbonat', 'axit clohiđric', 'canxi sunfat'.
- Công thức viết lộn xộn không chuẩn mhchem LaTeX.

*Thống kê số từ:* Đề bài: 82 từ | Các phương án: 44 từ | Lời giải & Phân tích: 55 từ | **Tổng: 181 từ**

---

## Chương 8: Kim loại chuyển tiếp và phức chất

### Câu 36: Bảng tuần hoàn hoá học — Dãy nguyên tố chuyển tiếp thứ nhất
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Các nguyên tố chuyển tiếp đóng vai trò xương sống cho ngành luyện kim và chế tạo vật liệu kĩ thuật cao nhờ có cấu hình electron phân lớp d chưa bão hoà. Trong bảng tuần hoàn các nguyên tố hoá học, dãy kim loại chuyển tiếp đầu tiên thuộc chu kì 4 bắt đầu từ nguyên tố scandium (Sc, Z=21) và theo định nghĩa chuẩn mực của hoá học hiện đại kết thúc ở nguyên tố nào?

[A.] Đồng (Cu, Z=29) vì cation tạo ra còn phân lớp d chưa bão hoà.
B. Kẽm (Zn, Z=30) ở vị trí nhóm IIB cuối chu kì 4 họ d.
C. Niken (Ni, Z=28) dùng làm chất xúc tác hydro hoá.
D. Sắt (Fe, Z=26) kim loại phổ biến nhất của chu kì 4.

**Dẫn giải lan man:** Theo định nghĩa hiện đại của IUPAC và SGK mới, Zn không phải là kim loại chuyển tiếp vì phân lớp d bão hoà (3d10). Dãy chuyển tiếp 3d chỉ từ Sc đến Cu...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 64 từ dông dài về 'xương sống ngành luyện kim'.
- Phương án kéo dài rườm rà tới 14 từ, kèm lời giải thích trong phương án.
- Định dạng Z=21, Z=29 không chuẩn LaTeX.

*Thống kê số từ:* Đề bài: 78 từ | Các phương án: 54 từ | Lời giải & Phân tích: 69 từ | **Tổng: 201 từ**

---

### Câu 37: Hợp chất phức chất — Thành phần cấu tạo nguyên tử trung tâm và phối tử
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Phức chất là một lớp hợp chất hoá học đặc biệt vô cùng phong phú đóng vai trò quan trọng trong hoá học vô cơ và sinh học. Trong công thức cấu tạo của một phức chất kinh điển là ion phức hexaamminecobalt(III) có công thức [Co(NH3)6]3+, hai thành phần cốt lõi đóng vai trò nguyên tử trung tâm nhận electron và phối tử cho cặp electron chưa liên kết lần lượt là gì?

[A.] Cation trung tâm Co3+ và các phối tử phân tử NH3.
B. Nguyên tử kim loại Co tự do và phối tử ion amoni NH4+.
C. Phối tử NH3 ở trung tâm và các cation Co3+ xung quanh.
D. Phức chất trung hoà không có nguyên tử trung tâm riêng biệt.

**Dẫn giải lan man:** Nguyên tử trung tâm là cation Co3+ có obitan trống, phối tử là NH3 có cặp e tự do tạo liên kết cho - nhận...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 65 từ dài dòng, nhồi nhét tên phức chất tiếng Anh 'hexaamminecobalt(III)'.
- Công thức ion phức không viết LaTeX ([Co(NH3)6]3+ thay vì $\ce{[Co(NH3)6]^{3+}}$).
- Dùng chữ 'obitan trống'.

*Thống kê số từ:* Đề bài: 74 từ | Các phương án: 52 từ | Lời giải & Phân tích: 54 từ | **Tổng: 180 từ**

---

### Câu 38: Thuốc thử Tollens tráng bạc — Vai trò của cầu nội và cầu ngoại
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Thuốc thử Tollens là một hoá chất cực kì thông dụng trong hoá học hữu cơ dùng để nhận biết andehit và đường glucozơ thông qua phản ứng tráng gương tạo lớp bạc sáng bóng. Về bản chất hoá học, thuốc thử Tollens là dung dịch của phức chất [Ag(NH3)2]OH. Thành phần nào trong công thức phức chất này đóng vai trò quyết định tính oxi hoá đặc trưng của thuốc thử?

[A.] Cation cầu nội [Ag(NH3)2]+ nằm trong dấu ngoặc vuông.
B. Anion cầu ngoại hiđroxit OH- phân li trong dung dịch nước.
C. Các phân tử khí amoniac thoát ra khỏi dung dịch.
D. Kim loại bạc Ag ở đáy ống nghiệm sau phản ứng.

**Dẫn giải lan man:** Cầu nội nằm trong dấu ngoặc vuông quyết định tính chất hoá học của phức chất, anion OH- chỉ là ion cầu ngoại trung hoà điện tích...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ mô tả phản ứng tráng gương của aldehyde và glucose dài dòng.
- Dùng chữ 'andehit', 'glucozơ', 'hiđroxit', 'amoniac'.
- Không định dạng công thức phức chất bằng LaTeX.

*Thống kê số từ:* Đề bài: 72 từ | Các phương án: 45 từ | Lời giải & Phân tích: 58 từ | **Tổng: 175 từ**

---

### Câu 39: Phản ứng của phức chất — Quá trình thay thế phối tử trong dung dịch
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Thông hiểu

**Đề bài:** Trong dung dịch nước, các phối tử liên kết với nguyên tử trung tâm kim loại có thể bị thay thế một phần hoặc thay thế hoàn toàn bởi các phối tử khác tạo thành phức chất mới bền vững hơn. Khi cho amoniac tác dụng với ion phức tetracloroplatinat(II) theo phương trình [PtCl4]2- + NH3 -> [PtCl3(NH3)]- + Cl-, phản ứng này thuộc loại phản ứng hoá học nào?

[A.] Phản ứng thế phối tử của phức chất trong dung dịch.
B. Phản ứng oxi hoá khử làm thay đổi số oxi hoá của platin.
C. Phản ứng trung hoà axit bazơ tạo muối phức chất.
D. Phản ứng kết tủa tạo hợp chất vô cơ ít tan.

**Dẫn giải lan man:** Phối tử NH3 thay thế phối tử Cl- trong cầu nội phức chất mà số oxi hoá của Pt không đổi (+2), đây là phản ứng thế phối tử...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 62 từ dài dòng giải thích nguyên tắc phối tử mới bền hơn trong đề bài.
- Dùng tên cũ 'tetracloroplatinat(II)', 'platin', 'axit bazơ'.
- Phương trình không viết mã LaTeX $\ce{...}$ chuẩn.

*Thống kê số từ:* Đề bài: 70 từ | Các phương án: 49 từ | Lời giải & Phân tích: 62 từ | **Tổng: 181 từ**

---

### Câu 40: Ứng dụng y học của phức chất — Thuốc hoá trị cisplatin
- **Bối cảnh tạo sinh:** Không nạp từ điển `hoa_12.json`, prompt chung cho mô hình ngôn ngữ
- **Mức nhận thức dự kiến:** Nhận biết

**Đề bài:** Sự phát triển của hoá vô cơ y sinh học đã mang lại nhiều thành tựu đột phá trong việc phát minh các loại dược phẩm chữa trị các căn bệnh hiểm nghèo của con người. Hợp chất phức chất vuông phẳng cisplatin có công thức hoá học PtCl2(NH3)2 với nguyên tử trung tâm là platin đóng vai trò nổi tiếng trong y dược hiện đại với công dụng điều trị căn bệnh nào?

[A.] Thuốc hoá trị liệu chữa trị các bệnh ung thư hiểm nghèo.
B. Thuốc kháng sinh đặc trị chống nhiễm khuẩn đường ruột.
C. Thuốc hạ huyết áp và điều trị bệnh lí tim mạch.
D. Thuốc an thần hỗ trợ điều trị rối loạn tâm thần.

**Dẫn giải lan man:** Cisplatin liên kết với DNA của tế bào ung thư ngăn cản quá trình nhân đôi, được dùng làm thuốc hoá trị ung thư tinh hoàn, buồng trứng...

**Lỗi phong cách & Nguy cơ sai sót:**
- Câu dẫn 66 từ kể lể về 'thành tựu đột phá hoá vô cơ y sinh học'.
- Dùng chữ 'platin' thay vì platinum.
- Phương án kéo dài rườm rà tới 12 từ.

*Thống kê số từ:* Đề bài: 74 từ | Các phương án: 48 từ | Lời giải & Phân tích: 60 từ | **Tổng: 182 từ**

---
