# QUY TRÌNH TIẾP NHẬN VÀ XỬ LÝ SỐ HOÁ SÁCH GIÁO KHOA

## I. MỤC TIÊU VÀ NGUYÊN TẮC CỐT LÕI

### 1. Mục tiêu của quy trình
- **Số hoá toàn vẹn và trung thực:** Chuyển hoá tài liệu sách giáo khoa nguyên bản dạng bản quét thành kho học liệu số có cấu trúc chuẩn mực, giữ trọn vẹn mạch sư phạm, văn phong và độ chính xác của sách giáo khoa chính thống.
- **Xây dựng từ điển tri thức chuyên ngành:** Trích xuất và hệ thống hoá các định nghĩa, khái niệm, tính chất và công thức thành hệ thống từ điển thuật ngữ chuẩn hoá, đóng vai trò làm điểm tựa khoa học để các chuyên gia giáo dục hoặc hệ thống thông minh tạo sinh câu hỏi, bài tập và học liệu giảng dạy.
- **Tạo lập cơ sở dữ liệu số chuẩn hoá:** Đóng gói toàn bộ bài học, cây mục lục, hình ảnh trích xuất và từ điển thành các bộ dữ liệu số đồng nhất, sẵn sàng kết nối vào các hệ thống quản lí học tập, ngân hàng đề thi hoặc ứng dụng ôn luyện thông minh.

### 2. Nguyên tắc chống sai lệch và chống bịa đặt (Chất lượng là sống còn)
- **Ảnh trang sách là chuẩn mực chân lý:** Mọi văn bản số hoá đều bắt buộc phải đối chiếu trực tiếp từng câu chữ, dấu chấm câu và vị trí trên ảnh trang in thực tế của sách giáo khoa gốc. Công nghệ nhận dạng ký tự quang học chỉ đóng vai trò hỗ trợ đối soát nhanh, tuyệt đối không được dùng để thay thế mắt người đối chiếu trực tiếp với trang sách.
- **Bảo toàn nguyên văn, không tự ý sửa đổi:** Nội dung bài học phải được ghi lại chính xác đến từng từ ngữ, không tự ý sửa lỗi chính tả của sách (nếu có lỗi in thì ghi chú riêng), không diễn giải lại theo ý hiểu cá nhân, không thêm bớt nội dung ngoài chương trình.
- **Tôn trọng phạm vi nguồn:** Chỉ ghi nhận là định nghĩa khi sách giáo khoa nêu rõ ràng bằng các câu khẳng định định nghĩa. Trường hợp sách chỉ dùng từ ngữ trong bài hoặc mô tả gián tiếp đặc điểm mà không định nghĩa trực tiếp, thuật ngữ đó phải được phân loại rõ ràng là dạng mô tả hoặc ngoài nguồn, tránh việc tự ý gán ghép định nghĩa từ các tài liệu khác bên ngoài.
- **Xử lý tuần tự có thứ bậc:** Dữ liệu được kiến tạo theo từng tầng kế thừa nhau. Khi phát hiện sai sót ở tầng dữ liệu phía sau (như từ điển hay gói dữ liệu xuất), người thực hiện bắt buộc phải quay lại sửa tận gốc ở tầng bài học nguyên văn, sau đó mới cập nhật lại các bước tiếp theo nhằm đảm bảo tính nhất quán tuyệt đối.

---

## II. TỔNG QUAN CÁC GIAI ĐOẠN TRONG QUY TRÌNH

Toàn bộ quy trình tiếp nhận và xử lý sách giáo khoa được tổ chức thành bốn giai đoạn nối tiếp nhau một cách chặt chẽ và khoa học:

1. **Giai đoạn 1: Khảo sát ban đầu và Dựng khung dữ liệu** (Tiếp nhận tài liệu, khảo sát đặc thù môn học, lập cây mục lục và tính toán độ lệch trang).
2. **Giai đoạn 2: Số hoá bài học nguyên văn và Xử lý hình ảnh - Tầng 1** (Nhập liệu trung thực bài học, phân cấp đề mục, đánh dấu thuật ngữ, cắt chuẩn hình ảnh và kiểm tra chất lượng bài học).
3. **Giai đoạn 3: Biên soạn Từ điển thuật ngữ chuẩn hoá - Tầng 2** (Hệ thống hoá thuật ngữ, phân loại theo nhóm định nghĩa và mô tả, đối chiếu bảng tra cứu cuối sách, kiểm tra độ phủ toàn diện).
4. **Giai đoạn 4: Đóng gói dữ liệu số và Kiểm toán nghiệm thu** (Xuất gói dữ liệu chuẩn hoá, kiểm toán mẫu độc lập đối chiếu từng ký tự với trang sách in gốc, lập biên bản nghiệm thu và bàn giao).

---

## III. NỘI DUNG CHI TIẾT TỪNG BƯỚC THỰC HIỆN

### GIAI ĐOẠN 1: KHẢO SÁT BAN ĐẦU VÀ DỰNG KHUNG DỮ LIỆU

#### Bước 1: Tiếp nhận và thẩm định nguồn sách giáo khoa
- Tiếp nhận bản quét sách giáo khoa chính thống thuộc chương trình mới. Kiểm tra tính toàn vẹn của tệp tài liệu: độ phân giải hình ảnh, các trang bìa, lời nói đầu, mục lục, nội dung các bài và các bảng tra cứu phụ lục ở cuối sách.
- Ghi nhận đầy đủ thông tin xuất bản: tên sách, bộ sách, môn học, khối lớp, nhà xuất bản và năm phát hành.

#### Bước 2: Khảo sát cấu trúc sư phạm và đặc thù môn học
- Đọc kỹ từ một đến hai bài học đầu tiên của cuốn sách để xác lập quy chuẩn biên soạn riêng cho môn đó:
  - *Môn Khoa học tự nhiên (Sinh học, Hoá học, Vật lí):* Khảo sát cách trình bày công thức hoá học, phương trình phản ứng, bảng số liệu, ký hiệu viết tắt và quy chuẩn gọi tên danh pháp quốc tế hiện hành.
  - *Môn Khoa học xã hội (Lịch sử, Địa lí):* Khảo sát cách trình bày các sự kiện, mốc thời gian, tên riêng nhân vật lịch sử, địa danh nước ngoài có gạch nối phiên âm, hệ thống lược đồ, biểu đồ và bản đồ chuyên đề.
  - *Môn Ngữ văn:* Khảo sát các thể loại văn bản, phần Tri thức ngữ văn mở đầu, các văn bản đọc hiểu, phần Thực hành tiếng Việt, phần hướng dẫn Viết và Nói – nghe, cùng các chú thích giải nghĩa từ ngữ ở chân trang.
  - *Môn Tiếng Anh:* Khảo sát hệ thống chủ điểm bài học, các kỹ năng ngôn ngữ và phần bảng chú giải từ vựng ở cuối sách kèm phiên âm và nghĩa tiếng Việt.
- Lập biên bản khảo sát ghi nhận rõ các quy ước trình bày và giải quyết các câu hỏi tồn đọng trước khi triển khai hàng loạt.

#### Bước 3: Thiết lập cây mục lục định danh và bản đồ số trang
- Dựa vào trang mục lục in và trang mở đầu từng bài trong ảnh để dựng cây cấu trúc hoàn chỉnh của cuốn sách từ các đơn vị lớn (Phần, Chương, Chủ đề hoặc Tập) đến từng bài học cụ thể.
- Tính toán và xác định mối quan hệ giữa số thứ tự trang trong bản quét điện tử và số trang in thực tế của sách giáo khoa:
  - Thông thường số trang điện tử sẽ lệch hơn số trang in một số trang nhất định do các trang bìa phụ ở đầu sách.
  - Rà soát cẩn thận để phát hiện những trang chèn ngoài lề (nếu có trong bản quét) để thiết lập công thức bù trừ số trang chính xác cho từng bài, đảm bảo người tra cứu luôn tìm đúng trang sách in gốc.
- Gán mã định danh duy nhất cho từng đơn vị bài học để theo dõi tiến độ một cách khoa học.

#### Bước 4: Tạo dữ liệu nhận dạng sơ bộ làm đối sánh
- Thực hiện quét nhận dạng chữ tự động toàn bộ các trang sách nhằm tạo ra kho văn bản thô. Kho văn bản này không dùng để xuất bản mà đóng vai trò làm thước đo kiểm tra đối chiếu chéo tự động với văn bản do con người số hoá ở giai đoạn sau.

---

### GIAI ĐOẠN 2: SỐ HOÁ BÀI HỌC NGUYÊN VĂN VÀ XỬ LÝ HÌNH ẢNH (TẦNG 1)

#### Bước 1: Số hoá nội dung bài học từng trang
- Người biên soạn đọc trực tiếp từng ảnh trang sách và số hoá lại toàn bộ văn bản một cách trung thực nhất.
- Đặt các mốc định vị trang rõ ràng tương ứng với từng trang sách in, giúp việc tra cứu ngược lại bản gốc luôn thuận tiện và minh bạch.
- Thiết lập hệ thống đề mục theo đúng thứ tự phân cấp sư phạm của sách: tiêu đề bài học, các phần lớn, các mục đánh số La Mã hoặc số Ả Rập, và các tiểu mục chữ cái.
- Chuyển hoá khéo léo các khung hộp chức năng (như khung mục tiêu bài học, câu hỏi mở đầu, hoạt động nghiên cứu, hoạt động thí nghiệm, góc kiến thức mở rộng, bài tập luyện tập và vận dụng) thành các khối trích dẫn trực quan, có biểu tượng nhận diện rõ ràng mà không làm đứt đoạn dòng chảy kiến thức của bài học.

#### Bước 2: Đánh dấu và nhận diện thuật ngữ trọng tâm
- Khi gặp câu văn chứa định nghĩa chính thức của sách, thuật ngữ được đánh dấu nổi bật bằng định dạng in đậm đặc biệt để hệ thống nhận diện đây là thuật ngữ có định nghĩa nguồn.
- Đối với những thuật ngữ quan trọng mà sách giới thiệu, phân tích chi tiết nhưng không diễn đạt dưới dạng một câu định nghĩa cứng nhắc, đoạn văn mô tả đó được gắn nhãn định danh để chuẩn bị trích xuất vào từ điển ở bước sau.
- Với các môn có công thức (Toán học, Vật lí, Hoá học), công thức được định dạng chuẩn mực theo quy chuẩn biểu diễn khoa học để hiển thị sắc nét và chính xác từng chỉ số trên, chỉ số dưới và ký hiệu toán học.

#### Bước 3: Trích xuất và chuẩn hoá hình ảnh, sơ đồ, bản đồ
- Xác định toạ độ hình chữ nhật bao quanh từng hình vẽ, ảnh chụp thực tế, biểu đồ, sơ đồ hoặc bản đồ trên trang sách.
- Trích xuất hình ảnh ở độ phân giải cao, đảm bảo bao trọn vẹn cả tiêu đề của hình, nội dung minh hoạ trực quan và khối chú giải hoặc chú thích ở phía dưới.
- Kiểm tra nghiêm ngặt mép viền hình ảnh: hình cắt ra phải sạch sẽ, không bị dính nét mực của dòng chữ văn bản liền kề, không bị cắt phạm vào nội dung và không để lại khoảng trống thừa thãi. Trường hợp hình vẽ có nét vẽ đặc thù nằm sát dòng chữ thì phải được ghi chú và kiểm soát chặt chẽ.

#### Bước 4: Kiểm tra và thông qua chất lượng bài học
- Thực hiện so sánh văn bản số hoá với kho văn bản nhận dạng quang học thô để rà soát tự động các lỗi chính tả, từ ngữ bị gõ thiếu, sót dòng hoặc nhầm lẫn ký tự.
- Kiểm tra tính liên tục của hệ thống mốc trang, đảm bảo không có trang nào bị bỏ quên.
- Chỉ khi bài học đạt độ sạch tuyệt đối, không còn bất kỳ lỗi sai sót hay cảnh báo nào thì mới được xác nhận hoàn thành Tầng 1 và chuyển tiếp sang Tầng 2.

---

### GIAI ĐOẠN 3: BIÊN SOẠN TỪ ĐIỂN THUẬT NGỮ CHUẨN HOÁ (TẦNG 2)

#### Bước 1: Thu thập và phân loại nguồn thuật ngữ
- Tập hợp toàn bộ các thuật ngữ đã được làm nổi bật hoặc gắn nhãn mô tả từ các bài học Tầng 1 đã được nghiệm thu.
- Khai thác triệt để Bảng tra cứu thuật ngữ, Bảng giải thích khái niệm hoặc Bảng thuật ngữ chuyên ngành ở cuối cuốn sách giáo khoa (nếu có) để làm căn cứ quy chiếu chuẩn mực.
- Phân loại rõ ràng từng mục thuật ngữ vào ba nhóm chức năng:
  - *Nhóm thuật ngữ có định nghĩa trong nguồn:* Trích dẫn nguyên văn câu định nghĩa chuẩn mực từ bài học hoặc từ bảng giải thích cuối sách.
  - *Nhóm thuật ngữ có mô tả trong bài:* Chắt lọc và kết hợp các câu mô tả bản chất từ bài học thành lời giải nghĩa sáng rõ, súc tích và trung thực, có gắn dấu nhận diện là dạng mô tả.
  - *Nhóm thuật ngữ ngoài nguồn:* Thuật ngữ chuyên môn có xuất hiện trong bài hoặc chương nhưng sách giáo khoa không định nghĩa cụ thể. Nhóm này được ghi nhận kèm ngữ cảnh ứng dụng thực tế để người dạy và người học hiểu đúng phạm vi chương trình, đồng thời không dùng nhóm này làm đáp án định nghĩa cứng trong các câu hỏi thi cử.

#### Bước 2: Xây dựng bảng từ điển theo từng chương hoặc chủ đề
- Mỗi cụm bài học hoặc chương được biên soạn thành một tệp từ điển riêng biệt nhằm phục vụ giảng dạy linh hoạt theo tiến trình học tập.
- Bảng từ điển được tổ chức quy củ gồm các thông tin thiết yếu:
  - Tên thuật ngữ tiếng Việt chuẩn mực.
  - Tên tiếng Anh tương ứng (đối chiếu theo bảng đối chiếu chuẩn hoặc thuật ngữ quốc tế), hoặc công thức hoá học, phiên âm ngữ âm tuỳ theo môn học.
  - Lời giải thích, định nghĩa hoặc mô tả chính xác.
  - Bối cảnh sử dụng, chỉ rõ vị trí xuất hiện cụ thể (thuộc bài học nào, mục số mấy, trang in bao nhiêu trong sách giáo khoa).
- Lập danh mục giải trình các trường hợp đã được xem xét kỹ lưỡng trong bài học nhưng không tạo thành mục thuật ngữ riêng (ví dụ: các từ ngữ đời thường, tên địa danh thuần tuý hoặc các khái niệm đã học ở lớp dưới) kèm lý do rõ ràng, đảm bảo tính chặt chẽ và không bỏ sót bất kỳ ứng viên tri thức nào.

#### Bước 3: Kiểm soát độ phủ tri thức toàn diện
- Tiến hành rà soát đối chiếu hai chiều: Mọi từ ngữ được làm nổi bật trong bài học Tầng 1 đều phải xuất hiện tương ứng trong bảng từ điển hoặc đã được giải trình thỏa đáng trong danh mục từ đã xem xét.
- Đảm bảo lời giải thích trong từ điển ăn khớp tuyệt đối với câu văn gốc của bài học, không để xảy ra hiện tượng "râu ông nọ cắm cằm bà kia".

---

### GIAI ĐOẠN 4: ĐÓNG GÓI DỮ LIỆU SỐ VÀ KIỂM TOÁN NGHIỆM THU

#### Bước 1: Đóng gói dữ liệu số có cấu trúc tự động
- Khi toàn bộ bài học và các tệp từ điển của cuốn sách đã vượt qua các vòng kiểm tra nội bộ, hệ thống tự động tổng hợp toàn bộ tri thức thành một tệp dữ liệu số hoá hoàn chỉnh.
- Gói dữ liệu này bao hàm trọn vẹn: thông tin hành chính của môn học và khối lớp, cây phả hệ mục lục bài học, các mục tiêu cần đạt, đường dẫn hình ảnh chất lượng cao, cùng toàn bộ kho từ điển thuật ngữ với toạ độ định vị chính xác đến từng trang sách.
- Toàn bộ gói dữ liệu được tự động kiểm tra cú pháp và cấu trúc, đảm bảo không có sự trùng lặp mã định danh, không có liên kết đứt gãy và sẵn sàng tích hợp với các hệ thống phần mềm khác.

#### Bước 2: Kiểm toán mẫu độc lập trực tiếp với sách in (Cửa nghiệm thu cuối cùng)
- Đây là bước chốt chặn quan trọng nhất quyết định chất lượng đầu ra của sản phẩm số hoá:
  - Một hội đồng thẩm định độc lập tiến hành rút ngẫu nhiên có kiểm soát một tập hợp mẫu từ 20 đến 30 mục tri thức (bao gồm các định nghĩa trọng tâm, các thuật ngữ có công thức phức tạp, các thuật ngữ mô tả và các hình ảnh minh hoạ), phân bổ đều khắp các chương của cuốn sách.
  - Từng mục trong mẫu kiểm toán được đặt cạnh ảnh chụp trang sách in gốc để đối chiếu tỉ mỉ:
    + Kiểm tra từng ký tự, từng từ ngữ trong lời giải thích xem có đúng từng dấu phẩy, dấu chấm của sách in hay không.
    + Kiểm tra số trang in thực tế và số trang bản quét xem có chuẩn xác tuyệt đối không.
    + Kiểm tra hình ảnh xem có sắc nét, đúng chú thích và sạch mép biên hay không.
  - **Tiêu chuẩn nghiệm thu:** Tỉ lệ sai sót tối đa cho phép phải nhỏ hơn hoặc bằng 5%, với mục tiêu hướng tới là **0% lỗi** (hoàn toàn không có sai sót).
  - Nếu phát hiện bất kỳ điểm sai lệch nào, dù là lỗi chính tả nhỏ, toàn bộ bài học và từ điển liên quan phải được sửa đổi ngay tại nguồn, sau đó chạy lại quy trình đóng gói và tiến hành kiểm toán mẫu lại từ đầu.

#### Bước 3: Lập biên bản kiểm toán và lưu trữ phiên bản
- Ghi nhận đầy đủ kết quả kiểm toán (ngày thực hiện, phạm vi kiểm tra, số lượng mẫu, tỉ lệ lỗi thực tế và người thẩm định) vào nhật ký tiến độ của cuốn sách.
- Chuyển đổi trạng thái chính thức của toàn bộ các bài học sang trạng thái "Đã kiểm định chất lượng".
- Cập nhật thông tin hoàn thành vào bảng tổng quan toàn dự án, lưu trữ an toàn các phiên bản mã nguồn và tài sản số hoá lên hệ thống kho lưu trữ đám mây, sẵn sàng đưa vào khai thác sử dụng thực tế.

---

## IV. GIÁ TRỊ VÀ ỨNG DỤNG CỦA KHO HỌC LIỆU SAU XỬ LÝ

Sản phẩm đầu ra của quy trình số hoá mang lại những giá trị ứng dụng to lớn và lâu dài trong chuyển đổi số giáo dục:

1. **Chuẩn hoá kho tri thức giáo dục:** Tạo nên nguồn dữ liệu số sạch, trung thực tuyệt đối với sách giáo khoa chính thống, xoá bỏ hoàn toàn nguy cơ học sinh và giáo viên tiếp cận phải các tài liệu trôi nổi, sai lệch trên internet.
2. **Nền tảng vàng cho tự động hoá khảo thí:** Kho từ điển thuật ngữ định vị chính xác là điều kiện tiên quyết để xây dựng các ngân hàng câu hỏi trắc nghiệm và đề thi tự động. Câu hỏi sinh ra từ nguồn tri thức này luôn có độ súc tích cao, câu dẫn rõ ràng, phương án trả lời chuẩn xác và định vị được chính xác vị trí bài học để giải thích đáp án cho học sinh.
3. **Tra cứu và hỗ trợ giảng dạy tức thì:** Cho phép giáo viên và học sinh tra cứu tức thì ý nghĩa của bất kỳ thuật ngữ, ký hiệu hoặc công thức nào trong bài học chỉ qua một lần chạm hoặc nhấp chuột, kèm theo hình ảnh minh hoạ trực quan.
4. **Phục vụ phân tích và liên thông kiến thức:** Hệ thống dữ liệu có cấu trúc giúp các nhà nghiên cứu và quản lí giáo dục dễ dàng phân tích ma trận kiến thức, đối sánh nội dung giữa các môn học và phát triển các mô hình học tập cá nhân hoá tiên tiến.
