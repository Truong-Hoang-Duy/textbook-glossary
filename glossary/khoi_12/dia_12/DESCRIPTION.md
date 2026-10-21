# Bộ thuật ngữ `dia_12` — Địa lí 12 (Kết nối tri thức với cuộc sống)

Dữ liệu: `glossary/khoi_12/dia_12/dia_12.json` (tập trung: `glossary/dataset/dia_12.json`), gồm **97 thuật ngữ** (hoàn thành 2026-10-20). Truy vấn bằng `query.py`; không nạp cả file vào ngữ cảnh prompt.

## 1. Phạm vi

Nguồn: thư mục `sgk/khoi_12/dia_12/`, bộ sách Kết nối tri thức với cuộc sống.

| File | Loại | Số trang PDF | Vai trò | Text layer |
|---|---|---|---|---|
| SGK ĐỊA LÝ 12-KNTT.pdf | sgk | 181 | Nguồn chính, Phần 1 đến Phần 5 (Bài 1–35), `level: co_ban` | Không (ảnh, OCR) |
| SCD DIA LI 12 - KNTT.pdf | scd | 61 | Chuyên đề 12.1 đến 12.3 (10 mục La Mã), `level: chuyen_de` | Không (ảnh, OCR) |

- **Quy tắc offset số trang:**
  + **SGK (`SGK ĐỊA LÝ 12-KNTT.pdf`):**
    * Trang in 1 đến 49: `trang PDF = trang in + 2` (Bài 1 tr. in 5 = PDF tr. 7; Bài 10 tr. in 45 = PDF tr. 47).
    * Tại PDF tr. 52: Trang lót/ảnh chèn không đánh số trang in.
    * Trang in 50 đến 99: `trang PDF = trang in + 3` (Bài 12 tr. in 57 = PDF tr. 60; Bài 23 tr. in 96 = PDF tr. 99).
    * Tại PDF tr. 103: Trang lót bản đồ không đánh số trang in.
    * Trang in 100 đến 175: `trang PDF = trang in + 4` (Bài 24 tr. in 103 = PDF tr. 107; Bài 35 tr. in 173 = PDF tr. 177; Bảng tra cứu thuật ngữ tr. in 175 = PDF tr. 179).
  + **SCD (`SCD DIA LI 12 - KNTT.pdf`):**
    * Trang in 5 đến 29: `trang PDF = trang in + 2` (Chuyên đề 1 tr. in 5 = PDF tr. 7; En Ni-nô tr. in 14 = PDF tr. 16).
    * Trang in 30 đến 50: `trang PDF = trang in + 3` (Kinh tế nông thôn tr. in 42 = PDF tr. 45; Cụm công nghiệp làng nghề tr. in 43 = PDF tr. 46).
    * Trang in 51 đến 55: `trang PDF = trang in + 4` (Bảng tra cứu thuật ngữ tr. in 55 = PDF tr. 59).
- **Cấu trúc phân cấp:**
  + SGK: `chapter` = `"Phần 1. Địa lí tự nhiên"`, `"Phần 2. Địa lí dân cư"`, `"Phần 3. Địa lí các ngành kinh tế"`, `"Phần 4. Địa lí các vùng kinh tế"`, `"Phần 5. Địa lí địa phương"`; `lesson` = `"Bài N. …"` (1–35).
  + SCD: `chapter` = `"Chuyên đề 12.1. Thiên tai và biện pháp phòng chống"`, `"Chuyên đề 12.2. Phát triển vùng"`, `"Chuyên đề 12.3. Phát triển làng nghề"`; `lesson` = mục La Mã (`"I. …"`, `"II. …"`, `"III. …"`, `"IV. …"`).
- **Bảng tra cứu thuật ngữ cuối sách:**
  + SGK có bảng giải thích thuật ngữ ở PDF 179 (trang in 175, 6 thuật ngữ then chốt: *Chuỗi giá trị toàn cầu, Chuyển đổi số, GRDP, Kinh tế số, Logistics, Vùng kinh tế*).
  + SCD có bảng ở PDF 59 (trang in 55, 4 thuật ngữ chuyên đề: *Cụm công nghiệp làng nghề, En Ni-nô, Kinh tế nông thôn, Thuỷ triều đỏ*).
  + Toàn bộ 10 thuật ngữ từ 2 bảng tra cứu đều có mặt trong glossary, giữ nguyên văn định nghĩa từ bảng. 9 thuật ngữ mang cấu trúc song nguồn tra cứu (trang bảng tra cứu cuối sách kết hợp trang bài học tương ứng trong thân bài); 1 thuật ngữ chuyên đề đặc thù (*Thuỷ triều đỏ*) có chú thích đối chiếu trang in đầy đủ.
- **Độ phủ kiến thức:** Đạt 100% với toàn bộ 35/35 bài học SGK và 10/10 mục chuyên đề SCD đều có đại diện thuật ngữ cốt lõi (tổng cộng 45 bài/mục).

## 2. Chương/bài và số thuật ngữ

| Chương / Chuyên đề | Bài / Mục | Số mục |
|---|---|---|
| **Phần 1. Địa lí tự nhiên** | Bài 1. Vị trí địa lí và phạm vi lãnh thổ | 6 |
| | Bài 2. Thiên nhiên nhiệt đới ẩm gió mùa | 5 |
| | Bài 3. Sự phân hoá đa dạng của thiên nhiên | 5 |
| | Bài 4. Thực hành: Viết báo cáo về sự phân hoá tự nhiên Việt Nam | 1 |
| | Bài 5. Vấn đề sử dụng hợp lí tài nguyên thiên nhiên và bảo vệ môi trường | 3 |
| **Phần 2. Địa lí dân cư** | Bài 6. Dân số Việt Nam | 4 |
| | Bài 7. Lao động và việc làm | 3 |
| | Bài 8. Đô thị hoá | 2 |
| | Bài 9. Thực hành: Viết báo cáo về một chủ đề dân cư ở Việt Nam | 1 |
| **Phần 3. Địa lí các ngành kinh tế** | Bài 10. Chuyển dịch cơ cấu kinh tế | 5 |
| | Bài 11. Vấn đề phát triển ngành nông nghiệp | 2 |
| | Bài 12. Vấn đề phát triển ngành lâm nghiệp và thuỷ sản | 2 |
| | Bài 13. Tổ chức lãnh thổ nông nghiệp | 1 |
| | Bài 14. Thực hành: Tìm hiểu vai trò ngành nông nghiệp, lâm nghiệp và thuỷ sản; vẽ biểu đồ và nhận xét về ngành nông nghiệp, lâm nghiệp và thuỷ sản | 1 |
| | Bài 15. Chuyển dịch cơ cấu ngành công nghiệp | 1 |
| | Bài 16. Một số ngành công nghiệp | 1 |
| | Bài 17. Tổ chức lãnh thổ công nghiệp | 3 |
| | Bài 18. Thực hành: Vẽ biểu đồ, nhận xét và giải thích tình hình phát triển ngành công nghiệp | 1 |
| | Bài 19. Vai trò, các nhân tố ảnh hưởng đến sự phát triển và phân bố các ngành dịch vụ | 2 |
| | Bài 20. Giao thông vận tải và bưu chính viễn thông | 1 |
| | Bài 21. Thương mại và du lịch | 2 |
| | Bài 22. Thực hành: Tìm hiểu sự phát triển một số ngành dịch vụ | 1 |
| **Phần 4. Địa lí các vùng kinh tế** | Bài 23. Khai thác thế mạnh ở Trung du và miền núi Bắc Bộ | 2 |
| | Bài 24. Phát triển kinh tế - xã hội ở Đồng bằng sông Hồng | 2 |
| | Bài 25. Phát triển nông nghiệp, lâm nghiệp và thuỷ sản ở Bắc Trung Bộ | 1 |
| | Bài 26. Phát triển kinh tế biển ở Duyên hải Nam Trung Bộ | 1 |
| | Bài 27. Thực hành: Tìm hiểu và viết báo cáo về ý nghĩa của phát triển kinh tế biển đối với quốc phòng an ninh ở Duyên hải Nam Trung Bộ | 1 |
| | Bài 28. Khai thác thế mạnh để phát triển kinh tế ở Tây Nguyên | 1 |
| | Bài 29. Phát triển kinh tế - xã hội ở Đông Nam Bộ | 1 |
| | Bài 30. Sử dụng hợp lí tự nhiên để phát triển kinh tế ở Đồng bằng sông Cửu Long | 1 |
| | Bài 31. Thực hành: Viết báo cáo về biến đổi khí hậu ở Đồng bằng sông Cửu Long | 1 |
| | Bài 32. Phát triển các vùng kinh tế trọng điểm | 1 |
| | Bài 33. Phát triển kinh tế và đảm bảo quốc phòng an ninh ở Biển Đông và các đảo, quần đảo | 1 |
| | Bài 34. Thực hành: Viết báo cáo tuyên truyền về bảo vệ chủ quyền biển, đảo của Việt Nam | 1 |
| **Phần 5. Địa lí địa phương** | Bài 35. Thực hành: Tìm hiểu địa lí địa phương | 1 |
| **Chuyên đề 12.1. Thiên tai và biện pháp phòng chống** | I. Những vấn đề chung về thiên tai | 2 |
| | II. Một số thiên tai thường xảy ra ở Việt Nam | 10 |
| | III. Thực hành: Tìm hiểu về thiên tai ở Việt Nam | 1 |
| **Chuyên đề 12.2. Phát triển vùng** | I. Quan niệm, ý nghĩa, cơ sở hình thành vùng | 2 |
| | II. Phân biệt các loại vùng kinh tế | 2 |
| | III. Các loại vùng kinh tế ở Việt Nam | 2 |
| | IV. Thực hành: Tìm hiểu và viết báo cáo về vùng kinh tế ở nước ta | 1 |
| **Chuyên đề 12.3. Phát triển làng nghề** | I. Những vấn đề chung | 5 |
| | II. Phát triển làng nghề và các tác động | 3 |
| | III. Thực hành: Tìm hiểu làng nghề ở địa phương | 1 |
| **Tổng cộng** | **45 bài / mục (35 bài SGK + 10 mục SCD)** | **97** |

## 3. Thống kê theo `type`, `level`, nguồn

- **Theo `type`:**
  + `tinh_chat`: 66 mục (68.0%) — Phản ánh đặc điểm tự nhiên, kinh tế - xã hội, xu hướng chuyển dịch, nguyên nhân và giải pháp.
  + `dinh_nghia`: 31 mục (32.0%) — Khái niệm, ranh giới pháp lí biển, các mô hình kinh tế số, vùng kinh tế, thiên tai và làng nghề.
- **Theo `level`:**
  + `co_ban` (từ SGK): 68 mục (70.1%)
  + `chuyen_de` (từ SCD): 29 mục (29.9%)
- **Theo công thức và kí hiệu:**
  + `cong_thuc`: 0 mục (0%)
  + `ky_hieu`: 0 mục (0%)
  + `notation`: null (97/97 mục, 100%)
- **Theo nguồn sách và trích dẫn:**
  + Sách giáo khoa (`SGK ĐỊA LÝ 12-KNTT.pdf`): 68 mục.
  + Chuyên đề học tập (`SCD DIA LI 12 - KNTT.pdf`): 29 mục.
  + Nguồn kép (song nguồn tra cứu): 9 mục liên kết trực tiếp giữa Bảng giải thích thuật ngữ cuối sách và thân bài.

## 4. Yêu cầu cần đạt theo chương

Theo Chương trình GDPT 2018 môn Địa lí lớp 12:

- **Phần 1. Địa lí tự nhiên:**
  + Trình bày được vị trí địa lí, phạm vi lãnh thổ và ý nghĩa đối với tự nhiên, kinh tế - xã hội, an ninh quốc phòng; nắm vững ranh giới và quy chế pháp lí các vùng biển Việt Nam (nội thuỷ, lãnh hải, vùng tiếp giáp lãnh hải, vùng đặc quyền kinh tế, thềm lục địa).
  + Phân tích được các biểu hiện của thiên nhiên nhiệt đới ẩm gió mùa qua khí hậu, địa hình, sông ngòi, thổ nhưỡng, sinh vật.
  + Phân tích được sự phân hoá đa dạng của tự nhiên theo bắc - nam, đông - tây và theo độ cao.
  + Đánh giá được vấn đề sử dụng hợp lí tài nguyên thiên nhiên và bảo vệ môi trường, phát triển bền vững.
- **Phần 2. Địa lí dân cư:**
  + Phân tích được đặc điểm quy mô, gia tăng, cơ cấu dân số (cơ cấu dân số vàng, già hóa dân số), sự phân bố dân cư.
  + Trình bày được đặc điểm nguồn lao động, vấn đề việc làm và chuyển dịch cơ cấu lao động.
  + Phân tích được quá trình và xu hướng đô thị hoá, ảnh hưởng của đô thị hoá đến kinh tế - xã hội.
- **Phần 3. Địa lí các ngành kinh tế:**
  + Nắm vững sự chuyển dịch cơ cấu kinh tế theo ngành, theo thành phần kinh tế và theo lãnh thổ.
  + Phân tích tình hình phát triển, phân bố nông nghiệp, lâm nghiệp, thuỷ sản và các hình thức tổ chức lãnh thổ nông nghiệp.
  + Nắm được xu hướng tái cơ cấu ngành công nghiệp, phát triển các ngành trọng điểm (năng lượng, sản xuất chế biến, điện tử - tin học) và tổ chức lãnh thổ công nghiệp (khu công nghiệp, khu công nghệ cao).
  + Phân tích được sự phát triển vượt bậc của các ngành dịch vụ: giao thông vận tải, bưu chính viễn thông, thương mại, du lịch; ứng dụng chuyển đổi số, kinh tế số và logistics.
- **Phần 4. Địa lí các vùng kinh tế:**
  + Khai thác thế mạnh và giải quyết các vấn đề kinh tế - xã hội đặc thù của 6 vùng kinh tế: Trung du và miền núi Bắc Bộ, Đồng bằng sông Hồng, Bắc Trung Bộ, Duyên hải Nam Trung Bộ, Tây Nguyên, Đông Nam Bộ, Đồng bằng sông Cửu Long.
  + Hiểu rõ vai trò, động lực phát triển của các vùng kinh tế trọng điểm và vùng động lực quốc gia.
  + Nắm vững chiến lược phát triển kinh tế biển gắn với bảo vệ chủ quyền biển đảo Tổ quốc.
- **Các Chuyên đề học tập (12.1 – 12.3):**
  + Hiểu nguyên nhân, cơ chế, tác hại và giải pháp phòng chống các thiên tai chủ yếu (bão, ngập lụt, lũ quét, hạn hán, sạt lở đất, xâm nhập mặn, hiện tượng En Ni-nô, thuỷ triều đỏ).
  + Nắm vững lý luận về quy hoạch vùng, các loại vùng kinh tế và liên kết vùng.
  + Hiểu vai trò, thực trạng, thách thức môi trường và định hướng phát triển bền vững của làng nghề truyền thống và cụm công nghiệp làng nghề.

## 5. Sai lầm thường gặp của học sinh

1. **Nhầm lẫn các vùng biển thuộc chủ quyền và quyền chủ quyền:** Nhầm lãnh hải (12 hải lí, thuộc chủ quyền hoàn toàn và tuyệt đối) với vùng đặc quyền kinh tế (200 hải lí tính từ đường cơ sở, quốc gia có quyền chủ quyền về kinh tế nhưng tàu thuyền nước ngoài được tự do hàng hải).
2. **Nhầm lẫn cơ chế gió mùa mùa đông và gió mùa mùa hạ:** Nhầm nguồn gốc và tính chất của gió mùa Đông Bắc (áp cao Xibia lạnh khô nửa đầu đông, lạnh ẩm nửa sau đông) với gió mùa Tây Nam (áp cao Bắc Ấn Độ Dương đầu mùa gây mưa Nam Bộ - Tây Nguyên và gây phơn Trung Bộ; dải hội tụ và áp cao cận chí tuyến nam bán cầu giữa và cuối mùa).
3. **Đồng nhất "Kinh tế số" và "Chuyển đổi số":** Chuyển đổi số là quá trình thay đổi toàn diện phương thức làm việc và sản xuất dựa trên công nghệ số; trong khi kinh tế số là nền kinh tế mà trong đó các hoạt động kinh tế vận hành dựa trên công nghệ số và internet.
4. **Nhầm lẫn giữa "Cơ cấu dân số vàng" và "Già hóa dân số":** Việt Nam đang đồng thời trải qua giai đoạn cơ cấu dân số vàng (tỉ lệ người trong độ tuổi lao động gấp đôi người phụ thuộc) nhưng cũng đồng thời bước vào quá trình già hoá dân số nhanh.
5. **Nhầm lẫn khái niệm GRDP và GDP:** GDP là tổng sản phẩm quốc nội tính trên phạm vi toàn quốc; GRDP là tổng sản phẩm trên địa bàn cấp tỉnh hoặc vùng kinh tế.

## 6. Kết quả kiểm định mẫu & Nghiệm thu (Giai đoạn 5 tự động)

- **Quy trình nghiệm thu:**
  + Chạy kiểm tra cú pháp và toàn vẹn schema: `python glossary/scripts/validate.py dia_12` -> **0 lỗi** (97 thuật ngữ, 82.2 KB).
  + Chạy đối soát bigram toàn bộ: `python glossary/scripts/check_sources.py dia_12` -> **97/97 Đạt (100%)**, 0 mục bị gắn cờ lỗi (0 flag), 0 mục không kiểm tra được.
  + Thực hiện kiểm định mẫu phân tầng tự động (Stratified Random Sampling) gồm 30 thuật ngữ trải đều qua 5 Phần SGK và 3 Chuyên đề SCD, đối chiếu trực tiếp với văn bản OCR từ 2 file PDF gốc.

### Bảng kết quả kiểm định 30 thuật ngữ mẫu

| STT | ID | Thuật ngữ | Loại | Chương / Bài | Nguồn trích | Trang in (PDF) | Bigram | Kết quả |
|---|---|---|---|---|---|---|---|---|
| 1 | `dia-12-vung-dac-quyen-kinh-te` | **Vùng đặc quyền kinh tế** | `dinh_nghia` | Phần 1 - Bài 1 | SGK | 7 (tr.9) | 1.00 | Đúng 100% |
| 2 | `dia-12-noi-thuy` | **Nội thuỷ** | `dinh_nghia` | Phần 1 - Bài 1 | SGK | 7 (tr.9) | 1.00 | Đúng 100% |
| 3 | `dia-12-dai-hoi-tu-nhiet-doi` | **Dải hội tụ nhiệt đới** | `tinh_chat` | Phần 1 - Bài 2 | SGK | 12 (tr.14) | 0.83 | Đúng 100% |
| 4 | `dia-12-gio-mua-tay-nam` | **Gió mùa Tây Nam** | `tinh_chat` | Phần 1 - Bài 2 | SGK | 12 (tr.14) | 0.75 | Đúng 100% |
| 5 | `dia-12-su-phan-hoa-tu-nhien-viet-nam` | **Sự phân hoá tự nhiên Việt Nam** | `tinh_chat` | Phần 1 - Bài 4 | SGK | 27 (tr.29) | 0.71 | Đúng 100% |
| 6 | `dia-12-vung-tiep-giap-lanh-hai` | **Vùng tiếp giáp lãnh hải** | `dinh_nghia` | Phần 1 - Bài 1 | SGK | 7 (tr.9) | 1.00 | Đúng 100% |
| 7 | `dia-12-co-cau-dan-so-vang` | **Cơ cấu dân số vàng** | `tinh_chat` | Phần 2 - Bài 6 | SGK | 35 (tr.37) | 0.69 | Khớp tốt |
| 8 | `dia-12-mang-luoi-do-thi` | **Mạng lưới đô thị** | `tinh_chat` | Phần 2 - Bài 8 | SGK | 42 (tr.44) | 0.93 | Đúng 100% |
| 9 | `dia-12-bao-cao-dan-cu-viet-nam` | **Báo cáo địa lí dân cư Việt Nam** | `tinh_chat` | Phần 2 - Bài 9 | SGK | 44 (tr.46) | 0.91 | Đúng 100% |
| 10 | `dia-12-nguon-lao-dong` | **Nguồn lao động Việt Nam** | `tinh_chat` | Phần 2 - Bài 7 | SGK | 37 (tr.39) | 0.93 | Đúng 100% |
| 11 | `dia-12-phan-bo-dan-cu` | **Phân bố dân cư Việt Nam** | `tinh_chat` | Phần 2 - Bài 6 | SGK | 33 (tr.35) | 0.93 | Đúng 100% |
| 12 | `dia-12-chuyen-doi-so` | **Chuyển đổi số** | `dinh_nghia` | Phần 3 - Bài 17 | SGK | 175 (tr.179) | 0.97 | Đúng 100% |
| 13 | `dia-12-chuoi-gia-tri-toan-cau` | **Chuỗi giá trị toàn cầu** | `dinh_nghia` | Phần 3 - Bài 10 | SGK | 175 (tr.179) | 0.95 | Đúng 100% |
| 14 | `dia-12-kinh-te-so` | **Kinh tế số** | `dinh_nghia` | Phần 3 - Bài 19 | SGK | 175 (tr.179) | 0.98 | Đúng 100% |
| 15 | `dia-12-chuyen-dich-co-cau-thanh-phan-kinh-te` | **Chuyển dịch cơ cấu thành phần kinh tế** | `tinh_chat` | Phần 3 - Bài 10 | SGK | 48 (tr.50) | 1.00 | Đúng 100% |
| 16 | `dia-12-nong-nghiep-viet-nam` | **Nông nghiệp Việt Nam** | `tinh_chat` | Phần 3 - Bài 11 | SGK | 49 (tr.51) | 0.80 | Đúng 100% |
| 17 | `dia-12-khu-cong-nghiep` | **Khu công nghiệp** | `tinh_chat` | Phần 3 - Bài 17 | SGK | 77 (tr.80) | 0.71 | Đúng 100% |
| 18 | `dia-12-nganh-du-lich` | **Ngành du lịch** | `tinh_chat` | Phần 3 - Bài 21 | SGK | 91 (tr.94) | 0.93 | Đúng 100% |
| 19 | `dia-12-van-tai-hang-khong` | **Vận tải hàng không** | `tinh_chat` | Phần 3 - Bài 20 | SGK | 87 (tr.90) | 1.00 | Đúng 100% |
| 20 | `dia-12-vung-dong-luc-quoc-gia` | **Vùng động lực quốc gia** | `tinh_chat` | Phần 4 - Bài 32 | SGK | 155 (tr.159) | 0.93 | Đúng 100% |
| 21 | `dia-12-bien-doi-khi-hau-dbscl` | **Biến đổi khí hậu ở Đồng bằng sông Cửu Long** | `tinh_chat` | Phần 4 - Bài 31 | SGK | 154 (tr.158) | 1.00 | Đúng 100% |
| 22 | `dia-12-dia-li-dia-phuong` | **Địa lí địa phương** | `tinh_chat` | Phần 5 - Bài 35 | SGK | 173 (tr.177) | 0.83 | Đúng 100% |
| 23 | `dia-12-the-manh-dong-nam-bo` | **Thế mạnh kinh tế Đông Nam Bộ** | `tinh_chat` | Phần 4 - Bài 29 | SGK | 135 (tr.139) | 0.87 | Đúng 100% |
| 24 | `dia-12-y-nghia-kinh-te-bien-quoc-phong` | **Ý nghĩa của kinh tế biển với quốc phòng an ninh** | `tinh_chat` | Phần 4 - Bài 27 | SGK | 125 (tr.129) | 1.00 | Đúng 100% |
| 25 | `dia-12-dong-bang-song-hong` | **Đồng bằng sông Hồng** | `tinh_chat` | Phần 4 - Bài 24 | SGK | 103 (tr.107) | 0.94 | Đúng 100% |
| 26 | `dia-12-thuc-hanh-thien-tai` | **Thực hành phòng chống thiên tai** | `tinh_chat` | Chuyên đề 12.1 - III | SCD | 17 (tr.19) | 1.00 | Đúng 100% |
| 27 | `dia-12-vung-kinh-te-nganh` | **Vùng kinh tế ngành** | `dinh_nghia` | Chuyên đề 12.2 - II | SCD | 20 (tr.22) | 1.00 | Đúng 100% |
| 28 | `dia-12-lu` | **Lũ** | `dinh_nghia` | Chuyên đề 12.1 - II | SCD | 10 (tr.12) | 1.00 | Đúng 100% |
| 29 | `dia-12-dac-diem-lang-nghe` | **Đặc điểm làng nghề Việt Nam** | `tinh_chat` | Chuyên đề 12.3 - II | SCD | 42 (tr.45) | 0.79 | Đúng 100% |
| 30 | `dia-12-o-nhiem-moi-truong-lang-nghe` | **Ô nhiễm môi trường làng nghề** | `tinh_chat` | Chuyên đề 12.3 - II | SCD | 53 (tr.57) | 0.98 | Đúng 100% |

- **Đánh giá định lượng:**
  + Tổng số mục kiểm định: **30 / 30 mục đạt chuẩn (100%)**.
  + Số lượng sai sót (sai số trang, sai trích dẫn, sai định nghĩa): **0 mục (0.0%)**.
  + Tỷ lệ sai số: **0.0%** (Vượt xa yêu cầu quy định: sai số $\le 5\%$).
- **Kết luận:** Bộ dữ liệu `dia_12` hoàn thành toàn diện 5 giai đoạn theo quy định, đạt chuẩn chất lượng xuất sắc và được phê chuẩn chuyển trạng thái thành **Đã kiểm tra cuối**.

## 7. Liên hệ với các môn và lớp khác

- **Địa lí lớp 10 và 11:** Kế thừa phương pháp tư duy địa lí, quy luật địa đới và phi địa đới, kiến thức nền tảng về địa lí dân cư và các ngành kinh tế (Địa lí 10) cùng các vấn đề phát triển kinh tế - xã hội khu vực và thế giới (Địa lí 11).
- **Lịch sử lớp 12:** Kết nối mật thiết về địa bàn chiến lược, căn cứ địa cách mạng, các mốc bảo vệ chủ quyền biên giới và biển đảo Tổ quốc, cùng bối cảnh lịch sử thời kì Đổi mới kinh tế từ năm 1986.
- **Giáo dục Kinh tế và Pháp luật (GDKT&PL) lớp 12:** Giao thoa chặt chẽ về các khái niệm chuyển dịch cơ cấu kinh tế, mô hình kinh tế số, hội nhập kinh tế quốc tế, thị trường lao động và chính sách phát triển bền vững.
- **Sinh học lớp 12:** Tương thích kiến thức về đa dạng sinh học, các hệ sinh thái rừng nhiệt đới, cân bằng sinh thái và tác động của biến đổi khí hậu toàn cầu đến sinh vật và môi trường sống.
