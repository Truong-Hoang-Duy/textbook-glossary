# DANH SÁCH SÁCH CÒN THIẾU — theo dõi bổ sung & xử lý

> Dùng chung cho Claude và Gemini (mọi agent làm việc trong dự án này). Trả lời người dùng bằng **tiếng Việt**.
> Lập ngày 2026-10-24 bằng cách đối chiếu `sgk/` với `glossary/*/*/progress.json`.
> Quy tắc gốc vẫn là `README.md` (Mục 5: chỉ dùng sách bộ **Kết nối tri thức với cuộc sống**, NXB Giáo dục Việt Nam).
> **Không tự tải sách.** Người dùng tự đặt file vào đúng thư mục `sgk/khoi_<lop>/<unit>/`.
> **Không tự commit/push** (CLAUDE.md).

---

## 1. Kí hiệu trạng thái

| Ô | Nghĩa | Ai đổi |
|---|---|---|
| `[ ]` | Còn thiếu, chờ người dùng bổ sung | — |
| `[~]` | Người dùng đã đặt file và xác nhận, **chưa xử lý xong** | Agent, khi người dùng báo "đã bổ sung <ID>" |
| `[x]` | Đã xử lý xong và kiểm tra (ghi ngày + kết quả ngắn sau dấu `→`) | Agent, sau khi các bước ở Mục 3 đều đạt |
| `[-]` | Người dùng xác nhận **không có / không cần** (ghi lí do) | Agent, khi người dùng xác nhận |

Một số dòng có nhiều ô (các sách của cùng một bộ); đếm theo ô, không theo dòng:
`grep -o "\[ \] \*\*" MISSING_BOOKS.md | wc -l` (còn thiếu), `grep -o "\[~\] \*\*" MISSING_BOOKS.md | wc -l` (đang xử lý), `grep -o "\[x\] \*\*" MISSING_BOOKS.md | wc -l` (đã xong).

## 2. Quy tắc làm việc

1. **Làm theo thứ tự giai đoạn** (A → B → C → D → E). Xong hết mục `[~]` của một giai đoạn rồi mới mở việc của giai đoạn sau.
   Mục `[ ]` đang chờ sách **không chặn** việc xử lý sách đã có ở giai đoạn sau, nhưng cuối mỗi phiên phải báo còn bao nhiêu mục `[ ]` ở giai đoạn hiện tại.
2. Trong một giai đoạn, xử lý và đánh dấu **từng mục một** (`[~]` → `[x]`), không gom đánh dấu cuối phiên.
3. Chỉ làm **một bộ (unit) mỗi phiên** (README Mục 3). Nếu người dùng bổ sung nhiều bộ cùng lúc thì ghi `[~]` hết, làm lần lượt theo thứ tự trong file.
4. Tên file đúng quy ước tiền tố (README Mục 5): `SGK …`, `SCD …`, `SBT …`, `SGV …`, `SGV CD …`, `Tài liệu bồi dưỡng GV …`. Tên tôi đề xuất bên dưới chỉ là gợi ý; tiền tố mới là bắt buộc.
5. Nhóm sách "SCD / SGV CD / SBT" tuỳ môn: nếu NXB không phát hành bản đó thì người dùng xác nhận và đánh `[-]`, không coi là thiếu.

## 3. Quy trình khi một sách được bổ sung (mỗi mục `[~]`)

1. Kiểm tra file nằm đúng `sgk/khoi_<lop>/<unit>/`, tên đúng tiền tố, mở được, đủ trang, có/không có text layer (sách ảnh thì đọc bằng ảnh, OCR chỉ tham khảo).
2. Đăng kí vào `glossary/khoi_<lop>/<unit>/progress.json` → `books` (SGV/SGV CD điền chương/bài giống SGK/SCD tương ứng, `pdf_pages` lấy từ mục lục SGV, ban đầu `status: pending`). Ghi bằng script qua `write_json_atomic`, không sửa tay `<unit>.json`.
3. Xử lý theo loại sách:
   - **SGV / SGV CD**: trích Mục 4 (yêu cầu cần đạt) và Mục 5 (sai lầm thường gặp, kèm file + trang PDF) vào `DESCRIPTION.md`; thêm nguồn `gv` cho thuật ngữ đã có (`add_terms.py --update`); với môn lấy `lessons` từ SGV (Vật lí, Địa lí, Âm nhạc, Tiếng Anh) thì nhập `add_lessons.py`.
   - **SCD**: trích thuật ngữ `level: chuyen_de` + `lessons` (README Mục 4b).
   - **SBT**: chỉ bổ sung khái niệm SGK chưa có, không trích đề bài.
   - **Tài liệu bồi dưỡng GV / Slide tập huấn**: đọc để bổ sung `DESCRIPTION.md`, không tạo thuật ngữ mới.
   - **Bộ mới**: chạy đủ quy trình 5 giai đoạn theo CLAUDE.md ("Bắt đầu làm bộ <unit>").
4. Chạy `python glossary/scripts/validate.py <unit>` (0 lỗi) và `python glossary/scripts/check_sources.py <unit>`.
5. Cập nhật `progress.json` (`status`, `last_session_note`), dòng của bộ trong bảng Mục 9 `README.md` nếu số mục/nguồn thay đổi.
6. Đổi ô tương ứng ở file này thành `[x]`, ghi ngày và kết quả: `→ 2026-MM-DD: <số mục thêm/sửa>, validate 0 lỗi`.

---

## GIAI ĐOẠN A — SGV / SGV CD còn thiếu của các bộ đã có (ưu tiên cao nhất)

README Mục 5 ghi SGV là sách **bắt buộc đọc**. Các bộ dưới đây đã xong phần SGK/SCD nhưng thiếu sách giáo viên tương ứng.

### A.1 Lớp 10

- [ ] **A01** · `toan_10` · **SGV Toán 10** (hiện chỉ có `SGV CD TOAN 10.pdf`; nếu bản in tách tập thì đặt `SGV TOAN 10 TAP 1.pdf`, `SGV TOAN 10 TAP 2.pdf`) → `sgk/khoi_10/toan_10/`
- [ ] **A02** · `sinh_10` · **SGV CD Sinh học 10** (hiện có SCD nhưng chưa có SGV CD) → `sgk/khoi_10/sinh_10/SGV CD SINH HOC 10.pdf`

### A.2 Lớp 11

- [ ] **A03** · `hoa_11` · **SGV CD Hoá học 11** → `sgk/khoi_11/hoa_11/SGV CD HOA HOC 11.pdf`
- [ ] **A04** · `lich_su_11` · **SGV CD Lịch sử 11** → `sgk/khoi_11/lich_su_11/SGV CD LICH SU 11.pdf`
- [ ] **A05** · `sinh_11` · **SGV CD Sinh học 11** → `sgk/khoi_11/sinh_11/SGV CD SINH HOC 11.pdf`
- [ ] **A06** · `tin_cs_11` · **SGV CD Tin học 11 – Khoa học máy tính** → `sgk/khoi_11/tin_cs_11/SGV CD TIN HOC 11 CS.pdf`
- [ ] **A07** · `tin_ict_11` · **SGV CD Tin học 11 – Tin học ứng dụng (ICT)** → `sgk/khoi_11/tin_ict_11/SGV CD TIN HOC 11 ICT.pdf`
- [ ] **A08** · `toan_11` · **SGV CD Toán 11** → `sgk/khoi_11/toan_11/SGV CD TOAN 11.pdf`
- [ ] **A09** · `van_11` · **SGV CD Ngữ văn 11** → `sgk/khoi_11/van_11/SGV CD NGU VAN 11.pdf`

### A.3 Lớp 12

- [ ] **A10** · `hoa_12` · **SGV Hoá học 12** → `sgk/khoi_12/hoa_12/SGV Hoa hoc 12 KNTT.pdf` (kèm F01)
- [ ] **A11** · `hoa_12` · **SGV CD Hoá học 12** → `sgk/khoi_12/hoa_12/SGV CD HOA HOC 12.pdf`
- [ ] **A12** · `lich_su_12` · **SGV Lịch sử 12** → `sgk/khoi_12/lich_su_12/SGV Lich su 12 KNTT.pdf`
- [ ] **A13** · `lich_su_12` · **SGV CD Lịch sử 12** → `sgk/khoi_12/lich_su_12/SGV CD LICH SU 12.pdf`
- [ ] **A14** · `ngu_van_12` · **SGV CD Ngữ văn 12** (đã có SGV Tập 1, 2) → `sgk/khoi_12/ngu_van_12/SGV CD NGU VAN 12.pdf`
- [ ] **A15** · `sinh_12` · **SGV Sinh học 12** → `sgk/khoi_12/sinh_12/SGV Sinh hoc 12 KNTT.pdf` (kèm F02)
- [ ] **A16** · `sinh_12` · **SGV CD Sinh học 12** → `sgk/khoi_12/sinh_12/SGV CD SINH HOC 12.pdf`
- [ ] **A17** · `toan_12` · **SGV CD Toán 12** — bản người dùng từng đặt trùng hệt SGV Toán 12 nên đã xoá (HANDOFF Mục 13). Cần xác nhận có bản riêng không; nếu không có thì đánh `[-]`.

### A.4 Kiểm tra file đã có (không cần sách mới)

- [ ] **A18** · `tin_cs_11` + `tin_ict_11` · File dùng chung `SGV Tin hoc 11 KNTT.pdf` (218 trang, sách ảnh) đang đăng kí cho cả hai bộ với cùng một khoảng bài `[18, 167]`. Xác nhận bằng ảnh rằng file chứa **cả hai** định hướng (CS và ICT). Nếu chỉ chứa một thì tách thành mục thiếu mới.

---

## GIAI ĐOẠN B — Bộ đã có SGK nhưng chưa dựng bộ (thiếu sách giáo viên để dựng đủ)

Ba môn dưới đây đã có SGK trong `sgk/khoi_10/` nhưng **chưa có thư mục `glossary/`**. Theo README Mục 5, thiếu SGV thì phần đó giữ `status: pending`; có thể dựng khung và trích SGK trước, bổ sung SGV sau.

- [ ] **B01** · `gd_ktpl_10` · **SGV Giáo dục KT&PL 10** → `sgk/khoi_10/gd_ktpl_10/SGV GD KTPL 10.pdf` *(SGK đã có: `SGK GD KTPL 10.pdf`, 158 trang)*
- [ ] **B02** · `gd_ktpl_10` · **SCD Giáo dục KT&PL 10** (nếu có) → `SCD GD KTPL 10.pdf`
- [ ] **B03** · `gd_ktpl_10` · **SGV CD Giáo dục KT&PL 10** (nếu có) → `SGV CD GD KTPL 10.pdf`
- [ ] **B04** · `gd_qpan_10` · **SGV Giáo dục QP&AN 10** → `sgk/khoi_10/gd_qpan_10/SGV GD QPAN 10.pdf` *(SGK đã có, 86 trang)*
- [ ] **B05** · `hd_tnhn_10` · **SGV Hoạt động TN, HN 10** → `sgk/khoi_10/hd_tnhn_10/SGV HD TNHN 10.pdf` *(SGK đã có, 78 trang)*
- [ ] **B06** · `gd_ktpl_10` / `gd_qpan_10` / `hd_tnhn_10` · **Dựng khung bộ** (Giai đoạn 1 của CLAUDE.md) — làm sau khi người dùng chốt có làm ba bộ này. Ghi vào đây quyết định: ____________

---

## GIAI ĐOẠN C — Môn / bộ chưa có gì trong `sgk/` (cần SGK trở lên)

Tên bộ gợi ý theo quy ước `{mon}_{lop}`; người dùng chốt tên cuối. Tên và số sách của từng bộ cần đối chiếu với nguồn hợp lệ khi bổ sung. Mỗi bộ cần tối thiểu **SGK** và **SGV**; SCD / SGV CD chỉ khi môn có chuyên đề học tập.

### C.1 Lớp 11

**`tieng_anh_11`** (Global Success; không có chuyên đề) → `sgk/khoi_11/tieng_anh_11/`
- [ ] **C01** · SGK Tiếng Anh 11 · [ ] **C02** · SGV Tiếng Anh 11

**`cong_nghe_co_khi_11`** (Công nghệ 11 – Công nghệ cơ khí) → `sgk/khoi_11/cong_nghe_co_khi_11/`
- [ ] **C03** · SGK · [ ] **C04** · SCD · [ ] **C05** · SGV · [ ] **C06** · SGV CD

**`cong_nghe_chan_nuoi_11`** (Công nghệ 11 – Công nghệ chăn nuôi) → `sgk/khoi_11/cong_nghe_chan_nuoi_11/`
- [ ] **C07** · SGK · [ ] **C08** · SCD · [ ] **C09** · SGV · [ ] **C10** · SGV CD

**`gd_ktpl_11`** → `sgk/khoi_11/gd_ktpl_11/`
- [ ] **C11** · SGK · [ ] **C12** · SCD · [ ] **C13** · SGV · [ ] **C14** · SGV CD

**`gd_qpan_11`** → `sgk/khoi_11/gd_qpan_11/`
- [ ] **C15** · SGK · [ ] **C16** · SGV

**`hd_tnhn_11`** → `sgk/khoi_11/hd_tnhn_11/`
- [ ] **C17** · SGK · [ ] **C18** · SGV

**`am_nhac_11`** → `sgk/khoi_11/am_nhac_11/`
- [ ] **C19** · SGK · [ ] **C20** · SCD · [ ] **C21** · SGV · [ ] **C22** · SGV CD

### C.2 Lớp 12

**`vat_ly_12`** → `sgk/khoi_12/vat_ly_12/`
- [ ] **C23** · SGK · [ ] **C24** · SCD · [ ] **C25** · SGV · [ ] **C26** · SGV CD

**`tin_cs_12`** (Tin học 12 – Khoa học máy tính) → `sgk/khoi_12/tin_cs_12/`
- [ ] **C27** · SGK · [ ] **C28** · SCD · [ ] **C29** · SGV · [ ] **C30** · SGV CD

**`tin_ict_12`** (Tin học 12 – Tin học ứng dụng) → `sgk/khoi_12/tin_ict_12/`
- [ ] **C31** · SGK · [ ] **C32** · SCD · [ ] **C33** · SGV · [ ] **C34** · SGV CD

**`cong_nghe_dien_dien_tu_12`** (Công nghệ 12 – Điện, điện tử) → `sgk/khoi_12/cong_nghe_dien_dien_tu_12/`
- [ ] **C35** · SGK · [ ] **C36** · SCD · [ ] **C37** · SGV · [ ] **C38** · SGV CD

**`cong_nghe_lam_nghiep_thuy_san_12`** (Công nghệ 12 – Lâm nghiệp, thuỷ sản) → `sgk/khoi_12/cong_nghe_lam_nghiep_thuy_san_12/`
- [ ] **C39** · SGK · [ ] **C40** · SCD · [ ] **C41** · SGV · [ ] **C42** · SGV CD

**`gd_ktpl_12`** → `sgk/khoi_12/gd_ktpl_12/`
- [ ] **C43** · SGK · [ ] **C44** · SCD · [ ] **C45** · SGV · [ ] **C46** · SGV CD

**`gd_qpan_12`** → `sgk/khoi_12/gd_qpan_12/`
- [ ] **C47** · SGK · [ ] **C48** · SGV

**`hd_tnhn_12`** → `sgk/khoi_12/hd_tnhn_12/`
- [ ] **C49** · SGK · [ ] **C50** · SGV

**`am_nhac_12`** → `sgk/khoi_12/am_nhac_12/`
- [ ] **C51** · SGK · [ ] **C52** · SCD · [ ] **C53** · SGV · [ ] **C54** · SGV CD

---

## GIAI ĐOẠN D — Sách bổ trợ tuỳ chọn (SBT, Tài liệu bồi dưỡng GV)

Giá trị thấp hơn: SBT chỉ bổ sung khái niệm SGK chưa có (không trích đề bài); Tài liệu bồi dưỡng GV chỉ bổ sung `DESCRIPTION.md`. Lớp 10 đã có đủ Tài liệu bồi dưỡng GV / Slide tập huấn cho mọi bộ (Toán, Tiếng Anh là Slide). Hiện **không bộ nào của lớp 11, 12 có SBT hoặc Tài liệu bồi dưỡng GV**. Không bắt buộc; người dùng quyết định có bổ sung không.

### D.1 SBT thiếu

- [ ] **D01** · `toan_10` · **SBT Toán 10 Tập 2** (đã có Tập 1) → `SBT TOAN 10 TAP 2.pdf`
- [ ] **D02** · `dia_11` · SBT Địa lí 11
- [ ] **D03** · `hoa_11` · SBT Hoá học 11
- [ ] **D04** · `lich_su_11` · SBT Lịch sử 11
- [ ] **D05** · `sinh_11` · SBT Sinh học 11
- [ ] **D06** · `tin_cs_11` · SBT Tin học 11 (Khoa học máy tính)
- [ ] **D07** · `tin_ict_11` · SBT Tin học 11 (Tin học ứng dụng)
- [ ] **D08** · `toan_11` · SBT Toán 11 (Tập 1 và Tập 2)
- [ ] **D09** · `van_11` · SBT Ngữ văn 11 (Tập 1 và Tập 2)
- [ ] **D10** · `vat_ly_11` · SBT Vật lí 11
- [ ] **D11** · `dia_12` · SBT Địa lí 12
- [ ] **D12** · `hoa_12` · SBT Hoá học 12
- [ ] **D13** · `lich_su_12` · SBT Lịch sử 12
- [ ] **D14** · `ngu_van_12` · SBT Ngữ văn 12 (Tập 1 và Tập 2)
- [ ] **D15** · `sinh_12` · SBT Sinh học 12
- [ ] **D16** · `tieng_anh_12` · SBT Tiếng Anh 12
- [ ] **D17** · `toan_12` · SBT Toán 12 (Tập 1 và Tập 2)

### D.2 Tài liệu bồi dưỡng GV thiếu (lớp 11, 12)

- [ ] **D18** · `dia_11` · [ ] **D19** · `hoa_11` · [ ] **D20** · `lich_su_11` · [ ] **D21** · `sinh_11`
- [ ] **D22** · `tin_cs_11` + `tin_ict_11` · [ ] **D23** · `toan_11` · [ ] **D24** · `van_11` · [ ] **D25** · `vat_ly_11`
- [ ] **D26** · `dia_12` · [ ] **D27** · `hoa_12` · [ ] **D28** · `lich_su_12` · [ ] **D29** · `ngu_van_12`
- [ ] **D30** · `sinh_12` · [ ] **D31** · `tieng_anh_12` (Slide tập huấn) · [ ] **D32** · `toan_12`

Tên file: `Tài liệu bồi dưỡng GV môn <Môn> <Lớp>.pdf` (lớp 10 đã dùng đúng quy ước này).

---

## GIAI ĐOẠN E — Môn ngoài phạm vi hiện tại (chờ người dùng quyết định)

Bộ KNTT còn có Mĩ thuật và Giáo dục thể chất ở cả ba khối; dự án chưa có bộ nào. Chỉ làm khi người dùng đồng ý đưa vào phạm vi. Ghi quyết định rồi mới liệt kê sách.

- [ ] **E01** · Mĩ thuật 10/11/12 — quyết định có làm không: ____________
- [ ] **E02** · Giáo dục thể chất 10/11/12 — quyết định có làm không: ____________

---

## PHỤ LỤC F — Việc kèm theo (không cần sách mới nhưng liên quan nguồn)

Khi rà soát, thấy nhiều `DESCRIPTION.md` ghi nguồn "Chương trình GDPT 2018 / CTGDPT 2018", trái README Mục 5 (chỉ dùng sách KNTT). Chỉ tìm thấy qua `grep`, **chưa mở từng đoạn để kết luận nội dung có thật sự lấy từ chương trình hay không**.

- [ ] **F01** · `hoa_12` · Mục 4 (dòng ~102) ghi "SGK/SGV & CTGDPT 2018" nhưng bộ **chưa có SGV**. Viết lại từ SGK sau khi có A10, hoặc bỏ phần không có nguồn KNTT.
- [ ] **F02** · `sinh_12` · Mục 4 (dòng ~111) tương tự, bộ chưa có SGV. Làm cùng A15.
- [ ] **F03** · `hoa_11` (dòng ~85), `sinh_11` (~88) · Mục 4 ghi "SGV & CTGDPT 2018". Đã có SGV: rà lại, chỉ giữ nội dung có trong SGV KNTT.
- [ ] **F04** · `lich_su_11` (dòng ~74) · nhắc "Chương trình GDPT 2018 môn Lịch sử". Rà lại như F03.
- [ ] **F05** · `toan_11` (dòng ~5, ~68–70), `toan_12` (dòng ~5), `vat_ly_11` (dòng ~110) · có nhắc GDPT 2018. Rà lại như F03.
