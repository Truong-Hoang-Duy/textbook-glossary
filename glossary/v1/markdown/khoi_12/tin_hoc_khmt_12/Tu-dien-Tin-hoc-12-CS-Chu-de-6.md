---
name: tu-dien-tin-hoc-12-cs-chu-de-6
description: "Từ điển thuật ngữ Tin học 12 – Định hướng Khoa học máy tính (Kết nối tri thức với cuộc sống) — Chủ đề 6. Mạng máy tính và Internet (Bài 22–24)"
loai_hoc_lieu: tu_dien_thuat_ngu
mon: "Tin học – Định hướng Khoa học máy tính"
lop: 12
chuong: "Chủ đề 6. Mạng máy tính và Internet"
bai_so: [22, 23, 24]
nguon: "SGK Tin học 12 – Định hướng Khoa học máy tính (Kết nối tri thức với cuộc sống)"
ngay_tao: "2026-11-02"
ngay_cap_nhat: "2026-11-02"
trang_thai: verified
---

# TỪ ĐIỂN THUẬT NGỮ — CHỦ ĐỀ 6. MẠNG MÁY TÍNH VÀ INTERNET

## Quy ước sử dụng

- **Nguồn chuẩn:** Chỉ trích xuất và tổng hợp từ văn bản Tầng 1 của Chủ đề 6 (Bài 22–24, trang PDF 120–135).
- **Phân loại mục từ:**
  - *Thuật ngữ có định nghĩa trực tiếp:* Giải nghĩa bám sát nguyên văn câu định nghĩa trong sách.
  - *Thuật ngữ mô tả (`[mô tả]`):* Sách không phát biểu câu định nghĩa đóng khung nhưng trình bày qua đoạn mô tả thông số kĩ thuật, bảng chuẩn truyền thông, ưu điểm hoặc lợi ích; cột Bối cảnh bắt đầu bằng `[mô tả] `.
  - *Thuật ngữ ngoài nguồn (`Ngoài nguồn`):* Thuật ngữ được nhắc tên trong phần mở rộng, vận dụng nhưng chưa định nghĩa chi tiết trong bài.

## Bài 22: Tìm hiểu thiết bị mạng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Server (máy chủ) | Server | Hệ thống phần cứng và phần mềm cung cấp các dịch vụ qua mạng theo yêu cầu của máy tính khác (máy khách). | Mục 1 Bài 22, định nghĩa khái niệm server và vai trò trong mạng máy tính (trang PDF 120–121). |
| Máy khách (client) | Client | Máy tính yêu cầu và được cung cấp dịch vụ từ máy chủ (server) qua mạng. | Mục 1 Bài 22, phân biệt vai trò máy khách và máy chủ trong mạng máy tính (trang PDF 120). |
| File server | File server | Máy chủ cung cấp dịch vụ lưu trữ tệp. | Mục 1 Bài 22, ví dụ về các loại server trong mạng máy tính (trang PDF 120). |
| Database server | Database server | Máy chủ quản trị cơ sở dữ liệu, cho phép các máy khách yêu cầu truy vấn dữ liệu trên đó. | Mục 1 Bài 22, ví dụ về các loại server trong mạng máy tính (trang PDF 120). |
| Web server | Web server | Hệ thống máy tính chạy phần mềm dịch vụ web, cung cấp các nội dung của website theo yêu cầu từ máy khách, máy khách nhận và hiển thị trang web đó. | Mục 1 Bài 22, ví dụ về các loại server trong mạng máy tính (trang PDF 120). |
| Máy chủ xác thực (authentication server) | Authentication server | Máy chủ cung cấp dịch vụ mạng có chức năng thẩm định quyền hạn của người dùng khi đăng nhập vào một mạng. | Mục 1 Bài 22, ví dụ về máy chủ cung cấp dịch vụ quản trị mạng (trang PDF 121). |
| Máy chủ tên miền (Domain Name Server - DNS) | Domain Name Server (DNS) | Máy chủ cung cấp dịch vụ mạng cho phép xác định địa chỉ IP từ tên miền, giúp người dùng không phải nhớ địa chỉ dạng các chữ số. | Mục 1 Bài 22, ví dụ về máy chủ cung cấp dịch vụ quản trị mạng (trang PDF 121). |
| Miền xung đột (collision domain) | Collision domain | Một phần của mạng gồm một nhóm máy tính được kết nối với nhau mà khi nhiều máy tính gửi tín hiệu đồng thời lên mạng sẽ gây ra xung đột tín hiệu. | Mục 2a Bài 22, giải thích cơ sở lựa chọn switch thay cho hub khi thiết kế mạng (trang PDF 122). |
| Hub | Hub | Bộ chia tín hiệu, cho tín hiệu lan toả từ một cổng ra tất cả các cổng khác; các máy tính nối vào cùng một hub sẽ thuộc về cùng một miền xung đột. | Mục 2a Bài 22, so sánh cơ chế truyền tín hiệu của hub và switch (trang PDF 122). |
| Switch | Switch | Thiết bị kết nối chỉ thiết lập kết nối tạm thời cổng của hai máy tính trong thời gian truyền nên các máy tính nối vào các cổng khác nhau của switch sẽ thuộc về các miền xung đột khác nhau, giúp chia nhỏ các miền xung đột. | Mục 2a Bài 22, phân tích ưu điểm của switch đối với mạng nhiều máy tính (trang PDF 122). |
| Cổng Gigabit | Gigabit port | Cổng Gigabit được hiểu là cổng có thể truyền với tốc độ từ một Gigabit/s trở lên (trong các mức tốc độ truyền dữ liệu qua các cổng 100 Megabit/s, 1 Gigabit/s hay 10 Gigabit/s). | Mục 2a Bài 22, giải thích thông số tốc độ truyền dữ liệu qua các cổng (trang PDF 122). |
| Thông số kĩ thuật của hub và switch | — | Các tính năng quan trọng thường được ghi trên thiết bị gồm: là hub hay switch; số cổng (nhiều cổng thì có thể kết nối được với nhiều thiết bị); tốc độ truyền dữ liệu qua các cổng (100 Megabit/s, 1 Gigabit/s hay 10 Gigabit/s). | [mô tả] Mục 2a Bài 22, nêu các tính năng kĩ thuật cần lưu ý của hub và switch (trang PDF 122). |
| Router | Router | Có thể nhận diện router qua đặc trưng có cổng WAN để kết nối ra ngoài mạng cục bộ; các router dùng trong gia đình thường chỉ có một cổng WAN và được ghi rõ "WAN" hoặc "Internet", còn các router của các mạng lớn có thể có nhiều cổng WAN. | Mục 2b Bài 22, nhận diện và tìm hiểu tính năng của router (trang PDF 122). |
| Cổng WAN | WAN port | Cổng trên router để kết nối ra ngoài mạng cục bộ; các router dùng trong gia đình thường chỉ có một cổng WAN (có màu khác với cổng LAN, còn gọi là cổng Ethernet) và được ghi rõ "WAN" hoặc "Internet", các router của các mạng lớn có thể có nhiều cổng WAN. | Mục 2b Bài 22, đặc trưng nhận diện và thông số kĩ thuật của router (trang PDF 122). |
| Cổng LAN (cổng Ethernet) | LAN port / Ethernet port | Cổng trên router có màu khác với cổng WAN (còn gọi là cổng Ethernet); các router dùng trong gia đình thường chỉ có một cổng WAN có màu khác với cổng LAN. | Mục 2b Bài 22, phân biệt cổng LAN và cổng WAN trên router (trang PDF 122). |
| Thông số kĩ thuật của router | — | Gồm: số cổng kết nối (cần phân biệt cổng WAN và cổng LAN, khi có nhiều cổng WAN router mới có thể định tuyến thực sự và có khả năng thiết lập kết nối dự phòng); tốc độ truyền dữ liệu qua các cổng; số lượng truy cập đồng thời; một số tính năng khác được đảm bảo bởi phần mềm tích hợp trên router. | [mô tả] Mục 2b Bài 22, liệt kê các thông số kĩ thuật quan trọng của router (trang PDF 122). |
| Bộ lặp (repeater) | Repeater | Thiết bị dùng để sửa lại tín hiệu khi truyền xa hơn 100 m trên cáp xoắn làm tín hiệu bị yếu đi, bị biến dạng hay bị nhiễu; repeater nhận tín hiệu ở một đầu, chỉnh sửa rồi phát lại tín hiệu tốt về đầu bên kia. | Mục 2c Bài 22, trình bày vai trò của repeater khi sử dụng cáp xoắn vượt quá khoảng cách hiệu quả 100 m (trang PDF 123). |
| Repeater Wi-Fi | Wi-Fi repeater | Thiết bị tiếp nhận tín hiệu qua Wi-Fi và phát lại qua Wi-Fi hoặc theo cáp mạng cắm vào cổng RJ45. | Mục 2c Bài 22, giới thiệu loại repeater phổ biến hiện nay (trang PDF 123). |
| Bộ thu phát Wi-Fi (điểm truy cập không dây) | Wireless Access Point (WAP) | Thiết bị cho phép các thiết bị kết nối không dây vào mạng cục bộ hay Internet, có thể được tích hợp với router hoặc độc lập. | Mục 2d Bài 22 (trang PDF 123) và Mục 2c Bài 23 (trang PDF 128). |
| Thông số kĩ thuật của bộ thu phát Wi-Fi | — | Gồm: băng tần hỗ trợ (tần số làm việc) thường tính theo GigaHz; băng thông - tốc độ truyền tính theo Megabit/s hoặc Gigabit/s phụ thuộc vào giao thức hỗ trợ; khoảng cách hiệu quả (độ phủ) phụ thuộc vào công suất phát; số lượng người dùng có thể truy cập đồng thời; môi trường làm việc là trong nhà (indoor) hay ngoài trời (outdoor). | [mô tả] Mục 2d Bài 22, liệt kê các thông số kĩ thuật quan trọng của bộ thu phát Wi-Fi (trang PDF 123). |

## Bài 23: Đường truyền mạng và ứng dụng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Đường truyền (kênh truyền) | Transmission medium / Channel | Một thành phần của mạng máy tính dùng để kết nối các máy tính với nhau theo những giao thức nhất định. | Hộp Khởi động Bài 23, giới thiệu vai trò của đường truyền mạng (trang PDF 125). |
| Đường truyền có dây | Wired transmission medium | Đường truyền gồm cáp đồng truyền dẫn tín hiệu điện và cáp quang truyền dẫn tín hiệu ánh sáng; tuỳ theo giao thức truyền thông và loại cáp mà tốc độ truyền, khoảng cách truyền hiệu quả cũng như chi phí sẽ khác nhau. | Hộp kiến thức trọng tâm Mục 1 Bài 23 (trang PDF 127). |
| Cáp đồng trục (Coaxial) | Coaxial cable | Loại cáp đồng truyền tín hiệu điện được dùng phổ biến vào trước những năm 2000. | Mục 1 Bài 23, giới thiệu các loại cáp đồng truyền tín hiệu (trang PDF 125–126). |
| Cáp xoắn (Twisted Pair, cáp đôi dây xoắn) | Twisted Pair cable | Loại cáp đồng truyền tín hiệu điện gọi tắt của cáp đôi dây xoắn (Twisted Pair), phổ biến nhất hiện nay. | Mục 1 và Mục 1a Bài 23, trình bày cấu tạo và đặc điểm của cáp xoắn (trang PDF 125). |
| Category (CAT) | Category (CAT) | Phân loại chất lượng cáp xoắn (ví dụ CAT.4, CAT.5, CAT.6) theo các chuẩn truyền dữ liệu với các thông số về băng thông và khoảng cách truyền hiệu quả. | Mục 1a Bài 23, phân loại cáp xoắn theo hiệu suất truyền dữ liệu (trang PDF 125). |
| Các chuẩn truyền thông trong mạng Ethernet | — | Các tiêu chuẩn truyền thông trong mạng Ethernet quy định loại cáp, tốc độ (đo bằng Mb/s hay Gb/s) và khoảng cách truyền hiệu quả, gồm: 10BASE5 (Đồng trục, 10 Mb/s, 500 m, Thick Ethernet), 10BASE2 (Đồng trục, 10 Mb/s, 185 m, Thin Ethernet), 10BASE-T (UTP, 10 Mb/s, 100 m, Ethernet Twist Pair), 100BASE-TX (UTP, 100 Mb/s, 250 m, Fast Ethernet), 100BASE-FX (Cáp quang, 100 Mb/s, 2000 m), 1000Base-SX (Cáp quang đa mode, cỡ Gb/s, 550 m, Gigabit Ethernet), 1000BASE-LX (Cáp quang đơn hoặc đa mode, cỡ Gb/s, 550 m cáp đa mode / 5000 m cáp đơn mode), 1000Base-CX (Cáp xoắn bọc kim STP, 1-10 Gb/s, 25 m), 1000Base-T (Cáp xoắn CAT 6, 1-10 Gb/s, 100 m). | [mô tả] Bảng 23.1 Mục 1a Bài 23, tổng hợp các chuẩn truyền thông Ethernet (trang PDF 126). |
| Cáp quang | Fiber optic cable | Phương tiện truyền dẫn tín hiệu ánh sáng là một ống sợi thuỷ tinh hay nhựa có đường kính rất nhỏ, mặt trong phản xạ toàn phần, giúp tia sáng phản xạ trong lòng ống và đi được thông suốt ngay cả khi cáp bị uốn cong. | Mục 1b Bài 23, trình bày cấu tạo và nguyên lí truyền ánh sáng của cáp quang (trang PDF 126). |
| Cáp đa mode (multimode) | Multimode fiber | Một trong hai loại cáp quang bên cạnh cáp quang đơn mode (single mode – có đường kính rất nhỏ, truyền xa hơn). | Mục 1b Bài 23, phân loại cáp quang (trang PDF 126). |
| Cáp quang đơn mode (single mode) | Single-mode fiber | Một trong hai loại cáp quang (bên cạnh cáp đa mode), có đường kính rất nhỏ, truyền xa hơn. | Mục 1b Bài 23, phân loại cáp quang (trang PDF 126). |
| Ưu điểm của cáp quang | — | Tín hiệu truyền dẫn ổn định, không bị ảnh hưởng bởi nhiễu điện từ và các điều kiện ngoại cảnh khác; ít suy hao hơn tín hiệu trong cáp điện nên truyền xa hơn; băng thông lớn gấp hàng trăm lần so với ADSL; gọn nhẹ, tiêu thụ năng lượng rất thấp và chi phí rẻ hơn so với cáp đồng; bảo mật vì khó lấy tín hiệu trên đường truyền. | [mô tả] Mục 1b Bài 23, liệt kê các ưu điểm nổi bật của cáp quang (trang PDF 126). |
| Dàn đĩa mạng (Network Attached Storage - NAS) | Network Attached Storage (NAS) | Các dàn đĩa mạng (Network Attached Storage - NAS) được kết nối trực tiếp với các máy chủ bằng cáp quang để đảm bảo băng thông cao và ổn định. | Mục 1b Bài 23, nêu trường hợp ứng dụng cáp quang trong mạng cục bộ (trang PDF 127). |
| Truyền không dây | Wireless transmission | Mã hoá dữ liệu trên sóng vô tuyến điện tần số cao; một số loại hình mạng không dây thông dụng gồm: mạng vệ tinh, mạng thông tin di động toàn cầu GSM, mạng Wi-Fi, mạng sử dụng bluetooth, mạng sử dụng kết nối trường gần NFC. | Mục 2 Bài 23, giới thiệu nguyên lí và đặc điểm của đường truyền không dây (trang PDF 127). |
| Mạng vệ tinh | Satellite network | Loại hình mạng không dây trong đó các vệ tinh có những bộ thu phát tín hiệu và các phương tiện dưới mặt đất sử dụng anten vệ tinh hoặc cảm biến để thu tín hiệu vệ tinh, có ưu điểm là vùng phủ sóng rất rộng. | Mục 2a Bài 23, trình bày nguyên lí và ưu điểm của mạng vệ tinh (trang PDF 127). |
| Hệ thống định vị toàn cầu | Global Positioning System | Hệ thống gồm các vệ tinh liên tục phát sóng xuống mặt đất giúp các thiết bị định vị xử lí để xác định toạ độ, phục vụ tìm đường và dẫn đường tự động cho phương tiện tự lái. | Mục 2a Bài 23, ứng dụng của mạng vệ tinh trong định vị và dẫn đường (trang PDF 128). |
| Starlink | Starlink | Dự án dùng hàng nghìn vệ tinh quỹ đạo thấp kết nối Internet qua các trạm thu phát trên mặt đất, mang lại cơ hội sử dụng Internet cho những nơi chưa có điều kiện thi công cáp như ở sa mạc, rừng sâu, đỉnh núi cao với chi phí thấp. | Mục 2a Bài 23, ứng dụng vệ tinh để kết nối Internet (trang PDF 128). |
| Mạng thông tin di động toàn cầu (Global System for Mobile Communications - GSM) | Global System for Mobile Communications (GSM) | Mạng thông tin di động có nhiều trạm thu phát (BTS), trong đó các thiết bị di động tìm kiếm và kết nối với trạm thu phát sóng gần nhất để kết nối vào mạng và chuyển dữ liệu giữa các thiết bị đầu cuối. | Mục 2b Bài 23, trình bày nguyên lí hoạt động và vai trò của mạng thông tin di động toàn cầu (trang PDF 128). |
| Trạm thu phát (Base Transceiver Station – BTS) | Base Transceiver Station (BTS) | Trạm thu phát sóng trong mạng thông tin di động toàn cầu GSM, làm nhiệm vụ kết nối với các thiết bị di động gần nhất và chuyển tiếp tín hiệu cho nhau để chuyển dữ liệu giữa các thiết bị đầu cuối. | Mục 2b Bài 23, cấu trúc của mạng GSM (trang PDF 128). |
| Mạng 2G | 2G network | Thế hệ thứ hai của mạng GSM, mới chỉ cung cấp được dịch vụ nghe gọi và tin nhắn ngắn SMS. | Mục 2b Bài 23, lịch sử phát triển các thế hệ mạng GSM (trang PDF 128). |
| Mạng thế hệ thứ ba (3G) | 3G network | Thế hệ thứ ba của mạng GSM, có thể truyền dữ liệu số nói chung, cho phép gửi thư điện tử, truy cập Internet, sử dụng dịch vụ định vị toàn cầu, truyền nhận dữ liệu âm thanh, hình ảnh chất lượng cao với tốc độ trao đổi dữ liệu đạt tới 40 Mb/s. | Mục 2b Bài 23, lịch sử phát triển các thế hệ mạng GSM (trang PDF 128). |
| Mạng thế hệ thứ tư (4G) | 4G network | Thế hệ thứ tư của mạng di động, có thể truyền tải dữ liệu với tốc độ tối đa tới 1,5 Gb/s. | Mục 2b Bài 23, lịch sử phát triển các thế hệ mạng GSM (trang PDF 128). |
| Mạng 5G | 5G network | Thế hệ mạng di động có thể đạt tốc độ tới 10 Gb/s, độ trễ rất thấp, hỗ trợ số lượng thiết bị kết nối lớn hơn rất nhiều so với mạng 4G nên rất phù hợp với các ứng dụng IoT. | Mục 2b Bài 23, lịch sử phát triển các thế hệ mạng GSM (trang PDF 128). |
| Họ giao thức IEEE 802.11 | IEEE 802.11 family | Họ giao thức của sóng Wi-Fi phổ biến dùng tần số cao như 2.4 GHz, 5 GHz và 60 GHz giúp chuyển tải dữ liệu nhanh, có nhiều chuẩn sử dụng tần số khác nhau với tốc độ truyền dữ liệu khác nhau (như chuẩn 802.11b có tốc độ 11 Mb/s, chuẩn 802/11a và 802.11g có tốc độ 54 Mb/s, chuẩn 802.11n có tốc độ 450 Mb/s). | Mục 2c Bài 23, các chuẩn Wi-Fi thông dụng (trang PDF 128–129). |
| Bluetooth | Bluetooth | Loại hình mạng không dây có tốc độ khoảng 1 Mb/s trong một phạm vi bán kính khoảng 10 m, thường chỉ kết nối hai thiết bị với nhau, rất thích hợp để kết nối các thiết bị cá nhân và đồ gia dụng. | Mục 2d Bài 23, trình bày đặc điểm và phạm vi ứng dụng của Bluetooth (trang PDF 129). |
| Ứng dụng của kết nối Bluetooth | — | Kết nối máy tính hay điện thoại di động với loa hay tai nghe không dây; truyền dữ liệu giữa các máy tính cá nhân hay điện thoại di động; kết nối không dây máy tính với thiết bị ngoại vi như chuột, bàn phím và máy in; thay thế các giao tiếp nối tiếp dùng dây cáp truyền thống giữa các thiết bị đo, thiết bị định vị dùng GPS, thiết bị y tế, máy quét mã vạch. | [mô tả] Mục 2d Bài 23, liệt kê các ví dụ sử dụng kết nối Bluetooth (trang PDF 129). |
| NFC (Near Field Communications) | Near Field Communications (NFC) | Công nghệ giao tiếp không dây trong khoảng cách ngắn (dưới 4 cm). | Mục Vận dụng Bài 23, giới thiệu công nghệ giao tiếp trường gần NFC (trang PDF 129). |

## Bài 24: Sơ bộ về thiết kế mạng

| Thuật ngữ | Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |
| --- | --- | --- | --- |
| Thiết kế mạng | Network design | Xây dựng các giải pháp kĩ thuật cho mạng để đáp ứng được các yêu cầu ứng dụng mạng, thực hiện qua 4 bước: khảo sát và phân tích yêu cầu; thiết kế logic; thiết kế vật lí; lựa chọn hệ điều hành mạng. | Hộp kiến thức trọng tâm Bài 24 (trang PDF 135). |
| Các yếu tố cần tính tới khi thiết kế mạng | — | Mục đích xây dựng mạng (ảnh hưởng quyết định đến thiết kế) và mức độ sử dụng (liên quan đến công suất, băng thông); quy mô địa lí và nơi đặt thiết bị (ảnh hưởng đến việc lựa chọn thiết bị, đường truyền và cấu trúc mạng); kinh phí đầu tư (để điều chỉnh thiết kế hoặc đầu tư từng phần theo thứ tự ưu tiên). | [mô tả] Mở đầu Bài 24, phân tích các yếu tố ảnh hưởng đến thiết kế mạng cục bộ (trang PDF 130). |
| Hệ điều hành mạng | Network operating system | Hệ điều hành được lựa chọn ở bước 4 của việc thiết kế mạng (việc xác định các ứng dụng sẽ cài đặt trên mạng không phải là công việc thiết kế mạng, nhưng có ảnh hưởng tới việc lựa chọn mô hình mạng và tính năng của các thiết bị mạng để đáp ứng yêu cầu của các ứng dụng). | Mở đầu và Bước 4 Bài 24, lựa chọn hệ điều hành mạng cho trường học (trang PDF 130, 134). |
| Thiết kế logic | Logical design | Bước 2 của các bước thiết kế mạng: đưa ra mô hình tương tác trong mạng, cấu trúc kết nối của mạng và giao thức mạng. | Bước 2 và Hộp kiến thức trọng tâm Bài 24 (trang PDF 130, 131, 135). |
| Mô hình làm việc nhóm (workgroup) | Workgroup model | Mô hình kiểm soát mạng trong đó không có máy nào điều khiển máy tính nào, người dùng phải thiết lập tài khoản trên máy và phải đăng nhập theo máy, không đòi hỏi quản trị phức tạp. | Bước 2 Bài 24, phân tích các mô hình kiểm soát mạng trong thiết kế logic (trang PDF 131). |
| Mô hình miền (domain) | Domain model | Mô hình kiểm soát mạng trong đó tài nguyên (thư mục dữ liệu chung, phần mềm chung, quyền truy cập Internet,...) và người dùng được quản lí chung bởi một máy chủ kiểm soát miền (Domain Controller); người dùng được cấp tài khoản trên toàn bộ miền và đăng nhập vào miền từ máy nào cũng được. | Bước 2 Bài 24, phân tích các mô hình kiểm soát mạng trong thiết kế logic (trang PDF 131). |
| Máy chủ kiểm soát miền (Domain Controller) | Domain Controller | Máy chủ trong mô hình miền (domain) quản lí chung người dùng và kiểm soát các tài nguyên của mạng như thư mục dữ liệu chung, phần mềm chung, quyền truy cập Internet, cho phép ai được dùng tài nguyên nào. | Bước 2 Bài 24, giải thích cơ chế quản trị tập trung của mô hình miền (trang PDF 131). |
| Cấu trúc dạng tuyến (bus topology) | Bus topology | Cấu trúc kết nối cơ bản trong đó các thiết bị được gắn vào một đường trục mạng; hiện nay vẫn còn dùng để xây dựng các đường trục kết nối các toà nhà hay xuyên các tầng của toà nhà cao tầng. | Bước 2 Bài 24, trình bày ba cấu trúc kết nối mạng cơ bản (trang PDF 132). |
| Cấu trúc dạng vòng (ring topology) | Ring topology | Cấu trúc kết nối cơ bản trong đó các thiết bị nối trên một vòng kín, dữ liệu được chuyển theo một chiều từ thiết bị này đến thiết bị kia rồi quay lại thiết bị ban đầu. | Bước 2 Bài 24, trình bày ba cấu trúc kết nối mạng cơ bản (trang PDF 132). |
| Cấu trúc hình sao (star topology) | Star topology | Cấu trúc kết nối cơ bản trong đó các thiết bị đầu cuối được đấu chung vào một thiết bị kết nối như hub, switch hay router; dễ thi công, dễ mở rộng, rẻ tiền và tin cậy, được dùng hầu hết trong các mạng cục bộ ngày nay. | Bước 2 Bài 24, trình bày ba cấu trúc kết nối mạng cơ bản (trang PDF 132). |
| Cấu trúc hỗn hợp | Hybrid topology | Cấu trúc mạng kết hợp nhiều cấu trúc cơ bản trong thực tế, ví dụ sự kết hợp của cấu trúc tuyến làm đường trục và cấu trúc hình sao gắn các máy tính vào đường trục. | Bước 2 Bài 24, giới thiệu các cấu trúc mạng thực tế (trang PDF 132). |
| Cấu trúc phân cấp | Hierarchical topology | Một cấu trúc hỗn hợp thông dụng về bản chất là cấu trúc hình sao của các hình sao (ví dụ tạo hai tầng: tầng dưới sử dụng hình sao để kết nối các thiết bị đầu cuối của từng khu vực, tầng trên kết nối các khu vực), rất thích hợp với các mạng cục bộ có nhiều máy tính. | Bước 2 Bài 24, lựa chọn cấu trúc kết nối cho mạng trường học khoảng 100 máy tính (trang PDF 132). |
| Thiết kế vật lí | Physical design | Bước thiết kế kĩ thuật ở mức vật lí: lựa chọn chủng loại thiết bị và thông số kĩ thuật, cách kết nối thiết bị theo cấu trúc kết nối và chọn điểm đặt thiết bị, cáp nối. | Bước 3 và Hộp kiến thức trọng tâm Bài 24 (trang PDF 130, 132, 135). |
| Phân đoạn mạng (segmentation) | Network segmentation | Công việc chia mạng (khi có vài chục máy tính trở lên) thành những thành phần nhỏ gọi là các phân đoạn (segment) để dễ kiểm soát hơn, giới hạn miền xung đột và tăng cường hiệu quả truyền dữ liệu. | Bước 3 Bài 24, trình bày nguyên tắc phân đoạn mạng trong thiết kế vật lí (trang PDF 132). |
| Phân đoạn (segment) | Network segment | Mỗi thành phần nhỏ khi mạng có vài chục máy tính trở lên cần xem xét chia mạng thành những thành phần nhỏ để dễ kiểm soát hơn và tăng cường hiệu quả truyền dữ liệu. | Bước 3 Bài 24, định nghĩa thành phần của phân đoạn mạng (trang PDF 132). |
| Lợi ích của phân đoạn mạng | — | Nhiều tổ chức có dữ liệu quan trọng cần được bảo vệ tốt thường tạo một phân đoạn mạng đặt máy chủ dữ liệu tách khỏi phân đoạn khác bằng router có cài đặt hệ thống tường lửa để kiểm soát việc truy cập vào các thiết bị trong phân đoạn; một lợi ích khác của việc phân đoạn mạng là có thể cô lập một phân đoạn khi có sự cố để khắc phục mà không gây ảnh hưởng tới hoạt động ở các phân đoạn khác. | [mô tả] Bước 3 Bài 24, phân tích các mục đích và lợi ích của việc phân đoạn mạng (trang PDF 133). |
| Quy tắc 5-4-3 | 5-4-3 rule | Quy tắc cần tuân thủ khi thiết kế mạng liên kết nhiều khu vực xa nhau của mạng cục bộ với nhiều phân đoạn tiếp nối với nhau qua repeater, vì repeater không chia nhỏ vùng xung đột nhưng gây trễ tín hiệu và nếu tín hiệu đi qua quá nhiều repeater thì độ trễ có thể làm sai lệch kiểm soát trong giao thức Ethernet. | Bước 3 Bài 24, giới hạn số lượng phân đoạn và repeater để tránh độ trễ làm sai lệch kiểm soát trong giao thức Ethernet (trang PDF 134). |
| Lựa chọn băng thông khi thiết kế mạng | — | Băng thông phụ thuộc vào ứng dụng: các ứng dụng quản lí chỉ cần băng thông rất thấp; các ứng dụng dùng video (xem phim, học trực tuyến, hội nghị truyền hình, thực tế ảo) đòi hỏi từ 0,5 đến 3 Megabit/s cho một luồng video, nên với vài chục người truy cập đồng thời có thể chọn chuẩn 100Base-TX (Fast Ethernet khoảng 100 Megabit/s) hoặc băng thông Gigabit, đồng thời chọn thiết bị kết nối và cáp mạng đồng bộ. | [mô tả] Bước 3 Bài 24, hướng dẫn xác định băng thông và chuẩn truyền trong thiết kế vật lí (trang PDF 134). |
| Gateway | Gateway | Ngoài nguồn — chưa định nghĩa trong Chủ đề 6. Xem: Tài liệu cấu hình giao thức TCP/IP và định tuyến mạng | Nhắc trong mục Vận dụng Bài 24 về cấu hình kết nối Internet (trang PDF 135). |
| DHCP (Dynamic Host Control Protocol) | Dynamic Host Configuration Protocol (DHCP) | Ngoài nguồn — chưa định nghĩa trong Chủ đề 6. Xem: Tài liệu cấu hình giao thức TCP/IP (cấp địa chỉ IP động) | Nhắc trong mục Vận dụng Bài 24 về chế độ cấp địa chỉ động cho các máy trong mạng (trang PDF 135). |
| Mặt nạ mạng con (subnetwork mask) | Subnetwork mask | Ngoài nguồn — chưa định nghĩa trong Chủ đề 6. Xem: Tài liệu cấu hình giao thức TCP/IP và địa chỉ IP | Nhắc trong mục Vận dụng Bài 24 về thiết lập thông số mạng trên các máy trạm (trang PDF 135). |

## Đã xét, không tạo mục

- máy chủ — tên khác của Server (máy chủ)
- cáp đôi dây xoắn — tên khác của Cáp xoắn (Twisted Pair, cáp đôi dây xoắn)
- điểm truy cập không dây — tên khác của Bộ thu phát Wi-Fi (điểm truy cập không dây)
- bộ thu phát Wi-Fi — tên khác của Bộ thu phát Wi-Fi (điểm truy cập không dây)
- một thiết bị tách các phân đoạn — chỉ có trong ví dụ, bài tập
- bridge — chỉ có trong ví dụ, bài tập
- Hoạt động 1: Server là gì? — tiêu đề, không phải thuật ngữ
- Bước 1. Khảo sát hiện trạng và phân tích nhu cầu — tiêu đề, không phải thuật ngữ
- Bước 2. Thiết kế logic — tiêu đề, không phải thuật ngữ
- Bước 3. Thiết kế vật lí — tiêu đề, không phải thuật ngữ
- Bước 4. Chọn hệ điều hành mạng — tiêu đề, không phải thuật ngữ

## Ghi chú nguồn cần kiểm tra

1. [đóng] Bài 23 (trang PDF 127) — Thuật ngữ: Mạng vệ tinh — Chú thích hình trên trang in 125 (trang PDF 127) in là "Hình 25.5. Một anten mặt đất của Starlink" (lỗi đánh số thứ tự bài trong SGK gốc của NXB, đúng ra là Hình 23.5) → Đã giữ nguyên văn chú thích sách ở Tầng 1 theo quy tắc trung thực nguồn (2026-11-02)
2. [đóng] Bài 24 (trang PDF 132) — Thuật ngữ: Cấu trúc phân cấp — Đoạn văn trên trang in 130 (trang PDF 132) in là "cấu trúc phân cấp (Hình 24.2b)" (lỗi tham chiếu hình trong SGK gốc, thực tế là Hình 24.3b) → Đã giữ nguyên văn chữ sách ở Tầng 1 theo quy tắc trung thực nguồn (2026-11-02)
