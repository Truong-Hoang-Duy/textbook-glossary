# BÀN GIAO — Trích "Yêu cầu cần đạt" (YCCĐ) vào `lessons` cho các bộ glossary

> Dán toàn bộ file này vào phiên mới, hoặc bảo agent: "Đọc `HANDOFF_YCCD.md` rồi làm tiếp".
> Cập nhật lần cuối: 2026-10-23. Gốc dự án là `d:\Project\book`. Trả lời người dùng bằng **tiếng Việt**.
> README.md và CLAUDE.md vẫn là quy tắc gốc và được nạp tự động. File này chỉ bổ sung ngữ cảnh của đợt công việc đang dở.

---

## 1. Việc đang làm

Người dùng muốn **bổ sung khung "Yêu cầu cần đạt" ở đầu mỗi bài SGK/SCD** vào dữ liệu glossary. Mục đích là để agent sinh câu hỏi bám đúng mục tiêu từng bài.

Các quyết định người dùng đã chốt (không hỏi lại):

1. **Phương án ①**: thêm mảng `lessons` trực tiếp vào `<unit>.json`, nằm cạnh `terms`, kèm `meta.lesson_count`.
   - Schema, script và chuyển đổi dữ liệu cho cả 27 bộ **đã làm xong**.
2. **Nhóm C** (Vật lí, Địa lí, Âm nhạc, Tiếng Anh) không có khung trong SGK, nên lấy YCCĐ từ **SGV KNTT** với `book_type: "gv"`.
   - `dia_12` đã có `sgk/khoi_12/dia_12/SGV Dia li 12 KNTT.pdf` do người dùng đặt vào. Cần **thêm file này vào `progress.json` của `dia_12`** trước khi trích (nếu chưa có).
3. **Toán**: cột "THUẬT NGỮ" ở đầu bài đưa vào `key_terms`. Môn khác để `key_terms: []`.
4. **Tiếng Anh**: ghi **theo Unit**, mỗi Unit một mục với `lesson: null`.
5. **Thứ tự làm**: nhóm A (Ngữ văn → Sinh → Hoá → Lịch sử → Công nghệ → Tin) → nhóm Toán → nhóm C (Vật lí 10/11, Địa lí 10/11/12, Âm nhạc 10, Tiếng Anh 10).
6. **Nguồn**: chỉ dùng sách KNTT (NXB GDVN), không dùng Chương trình GDPT 2018 hay tài liệu trên mạng (README Mục 5). Không tự tải sách; thiếu sách thì báo người dùng.
7. **Git**: **không tự commit/push**. Commit message viết tiếng Anh theo Conventional Commits, **không** thêm dòng "Co-Authored-By"/AI.
8. Người dùng thường chỉ nói "tiếp tục" hoặc "tiếp theo", nghĩa là làm bộ kế tiếp theo thứ tự trên.

---

## 2. Trạng thái (2026-10-23)

### Đã xong — 19 bộ, 616 mục `lessons` (đã đếm lại từ dữ liệu ngày 2026-10-23), đều qua `validate` và `check_sources` (YCCĐ 100%)

Tách theo sách: SGK 431 mục, SCD 185 mục (431 + 185 = 616). Ví dụ đối chiếu nhanh: `python glossary/scripts/query.py <unit> --lessons --count`.

| Bộ | lessons | label (tên khung trong sách) | Ghi chú quan trọng |
|---|---|---|---|
| ngu_van_10 | 16 | Yêu cầu cần đạt / Yêu cầu | SCD: 3 mục cấp chuyên đề `lesson: null` + 2 khung "Yêu cầu" của Phần |
| van_11 | 17 | như trên | SCD 3 `null` + 3 Phần |
| ngu_van_12 | 11 | Yêu cầu cần đạt | Đã sửa `printed_page` 51 nguồn thuật ngữ (lệch +2…+4) |
| sinh_10 | 38 | Yêu cầu cần đạt | Bài thực hành giữ câu dẫn "Sau khi học xong…" làm ý đầu |
| sinh_11 | 40 | Yêu cầu cần đạt | Bài 3 thật ở PDF 23 |
| sinh_12 | 45 | Yêu cầu cần đạt | 9 bài `pdf_pages` trong progress lệch (có notes); SCD lệch +2/+3/+4 |
| hoa_10 | 28 | Mục tiêu | Bài "Ôn tập chương" không có khung → bỏ qua |
| hoa_11 | 28 | Mục tiêu | như trên |
| hoa_12 | 31 | Mục tiêu | SCD Bài 1 thật ở PDF 8; lệch +2 |
| lich_su_10 | 17 | Học xong bài này, em sẽ | SCD: khung "Học xong chuyên đề này, em sẽ" → 3 mục `null` |
| lich_su_11 | 16 | như trên | 9 bài SGK trang thật = progress − 1 |
| lich_su_12 | 20 | như trên | SCD ở PDF 8/25/39; lệch +2 |
| cong_nghe_cong_nghiep_10 | 30 | Sau khi học xong bài này, em sẽ | Bài dự án: "Sau khi hoàn thành dự án, em sẽ / các em có thể" |
| cong_nghe_nong_nghiep_10 | 43 | như trên | SCD thực tế lệch +1 (README ghi 0 — xem Mục 5) |
| tin_hoc_10 | 63 | Sau bài này em sẽ / Học xong bài này em sẽ / Sau bài học này em sẽ | SCD ICT đánh lại Bài 1 mỗi chuyên đề |
| tin_cs_11 | 47 | Sau bài học này em sẽ / SCD: Sau bài này em sẽ | 3 bài trang lệch (15→74, 18→87, 30→138) |
| tin_ict_11 | 46 | Sau bài học này em sẽ | SGK Bài 1–16 trùng hệt tin_cs_11 |
| toan_10 | 35 | Kiến thức, kĩ năng | Có `key_terms` |
| toan_11 | 45 | Kiến thức, kĩ năng | Bài 4→PDF 32, Bài 10→PDF 71; SCD Bài 12 `key_terms: []` |

Mỗi bộ đã xong có khối `"yccd": {"status": "done", "lesson_count": N, "note": "..."}` trong `progress.json` và đã nối ghi chú vào `last_session_note`.

### Còn lại — làm theo thứ tự

1. **toan_12** (nhóm Toán, cuối): SGK Tập 1, Tập 2; không có SCD. README ghi SGK trang PDF = trang in + 2 → **kiểm tra lại bằng chân trang**. Cách làm giống toan_11.
2. **Nhóm C, lấy từ SGV** (`book_type: "gv"`, `label` theo SGV, thường là "I. Mục tiêu"/"Yêu cầu cần đạt"…):
   - vat_ly_10: `SGV VAT LI 10.pdf` (SGK), `SGV CD VAT LI 10.pdf` (SCD)
   - vat_ly_11: `SGV Vat li 11 KNTT.pdf`
   - dia_10: `SGV DIA LI 10.pdf`, `SGV CD DIA LI 10.pdf`
   - dia_11: `SGV Dia li 11 KNTT.pdf`
   - dia_12: `SGV Dia li 12 KNTT.pdf` (198 trang, trang đầu không có text layer → sách dạng ảnh, phải đọc bằng ảnh).
     **Hiện `progress.json` của dia_12 CHƯA có file này** (đã xác nhận: `books` chỉ có SGK và SCD), nên `validate.py dia_12` đang báo 1 lỗi "thiếu sách". Việc đầu tiên khi làm dia_12 là thêm mục SGV vào `books`, theo đúng mẫu của `dia_11`:
     `"SGV Dia li 12 KNTT.pdf": {"status": "pending", "glossary_pdf_pages": [], "chapters": { <chương/bài giống SGK: {"lessons": {"Bài N. …": {"status": "pending", "pdf_pages": [đầu, cuối], "terms_added": 0}}}> }}`
     (README Mục 5: SGV điền chương/bài giống SGK; trang `pdf_pages` của SGV phải lấy từ mục lục SGV; sửa `progress.json` bằng script ghi qua `write_json_atomic`, không sửa tay file `<unit>.json`).
   - am_nhac_10: `SGV AM NHAC 10.pdf`, `SGV CD AM NHAC 10.pdf`
   - tieng_anh_10: `SGV TIENG ANH 10 Global Success.pdf`. Ghi theo **Unit**, `lesson: null`. OCR dùng `eng+vie`.

   Lưu ý cho nhóm C:
   - `level` phải khớp tên file: `SGV …` → `co_ban`, `SGV CD …` → `chuyen_de` (validate kiểm tra).
   - `chapter`/`lesson` là chuỗi bài của SGK/SCD trong `progress.json`, vì SGV đi theo bài.
   - Trang SGV thường lệch khác SGK; đọc chân trang. DESCRIPTION.md Mục 4 của các bộ này có thể đã ghi số trang SGV, dùng để định vị nhanh.

---

## 3. Schema `lessons` (đã có trong `glossary/schema.json`, README Mục 4b)

```json
{"chapter": "<đúng chuỗi progress.json>", "lesson": "<đúng chuỗi> | null", "level": "co_ban|chuyen_de",
 "label": "<tên khung đúng như sách>", "objectives": ["<ý nguyên văn>", "..."],
 "key_terms": ["<chỉ Toán: cột THUẬT NGỮ>"],
 "sources": [{"book_type": "sgk|scd|gv", "file": "<tên PDF>", "pdf_page": N, "printed_page": N}],
 "notes": null}
```

- Khoá duy nhất là `(level, chapter, lesson)`. Thứ tự key trong object phải giữ đúng như trên.
- `lesson: null` dùng khi khung áp dụng cho cả chương/chuyên đề.
- `notes` ghi khi trang đầu bài thật khác `pdf_pages[0]` trong progress, hoặc khi đã gộp gạch con: `"Trang đầu bài là PDF X (pdf_pages trong progress.json bắt đầu ở PDF Y)."`

Lệnh (chạy từ `d:\Project\book`):

```
python glossary/scripts/add_lessons.py <unit> <lo.json> [--update]
python glossary/scripts/validate.py <unit>
python glossary/scripts/check_sources.py <unit>          # cuối output có "== Yêu cầu cần đạt: ..."
python glossary/scripts/query.py <unit> --lessons --format text
```

File lô (`lo_yccd_<unit>.json`) để ở scratchpad, **không** để trong `glossary/`.

---

## 4. Quy trình đã dùng cho mỗi bộ (lặp lại y hệt)

1. Liệt kê bài: đọc `progress.json`, lấy `pdf_pages[0]` của mỗi bài SGK/SCD (hoặc SGV cho nhóm C).
2. Dựng **ảnh thu nhỏ cả trang** (`fullsheet.py`, 3 trang/ảnh, 62 dpi) để thấy khung nằm ở đâu và phát hiện trang lệch:
   - Bài mở chương: khung thường ở **nửa dưới trang tên chương**.
   - Nếu trang `pdf_pages[0]` không phải đầu bài, dựng ảnh thu nhỏ các trang lân cận (±1…5) để tìm trang thật.
3. **Cắt vùng khung ở 115 dpi** (`cropbox.py file:page:top:bot`) để đọc chữ, và **chép nguyên văn từ ảnh** (ảnh là chuẩn; OCR chỉ để tham khảo).
   - Sửa các lỗi dấu OCR hay gặp: lối/lỗi, kẻ/kể, chỉ tiết/chi tiết…
   - Công thức/kí hiệu viết LaTeX (`$\pi$`, `$y = \sin x$`, `$K_C$`, `$SO_4^{2-}$`).
4. **`printed_page`**: đọc số in ở chân trang, không giả định. Phần lớn các bộ lệch +1; lớp 12 thường +2.
5. **Ghi kết quả ra file ngay sau mỗi 3–4 ảnh** (`obj.py` dạng dict `(file, page) -> (key_terms, objectives)`), vì ảnh có thể bị xoá khỏi ngữ cảnh.
6. Dựng lô bằng `mk_toan2.py` (hoặc biến thể), rồi chạy `add_lessons.py`, `validate.py`, `check_sources.py`.
   - Cảnh báo `key_terms` do OCR cột hẹp: xác nhận lại trên ảnh rồi bỏ qua.
   - YCCĐ phải đạt 100%.
7. Ghi tiến độ bằng `prog_note.py <root> <unit> <count> "<note>"`.
8. Báo cáo ngắn cho người dùng: bảng SGK/SCD, ghi chú trang lệch, kết quả kiểm tra, "Chưa commit gì", bộ tiếp theo.

### Script hỗ trợ (dán vào scratchpad của phiên mới; đường dẫn PDF tương đối từ gốc dự án)

`fullsheet.py`: ảnh thu nhỏ cả trang đầu mỗi bài
```python
"""python fullsheet.py unit grade outdir  -> outdir/fNN.png (3 trang/ảnh)"""
import json, sys, pymupdf
from pathlib import Path
from PIL import Image, ImageDraw
unit, grade, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]); out.mkdir(exist_ok=True, parents=True)
prog = json.load(open(f"glossary/khoi_{grade}/{unit}/progress.json", encoding="utf-8"))
items = [(f, i["pdf_pages"][0]) for f, b in prog["books"].items() if f.startswith(("SGK", "SCD"))
         for c in b["chapters"].values() for i in c["lessons"].values()]
docs = {}; k = 0
for s in range(0, len(items), 3):
    ims = []
    for f, p in items[s:s + 3]:
        d = docs.setdefault(f, pymupdf.open(f"sgk/khoi_{grade}/{unit}/{f}"))
        x = d[p - 1].get_pixmap(dpi=62); im = Image.frombytes("RGB", (x.width, x.height), x.samples)
        ImageDraw.Draw(im).text((4, 4), f"{f[:3]} p{p}", fill="red"); ims.append(im)
    o = Image.new("RGB", (sum(i.width for i in ims), max(i.height for i in ims)), "white"); xx = 0
    for i in ims: o.paste(i, (xx, 0)); xx += i.width
    o.save(out / f"f{k:02d}.png"); print(k, items[s:s + 3]); k += 1
```
(Với nhóm C, đổi bộ lọc `startswith(("SGK","SCD"))` thành tên file SGV và lấy trang từ sách SGV tương ứng.)

`cropbox.py`: cắt vùng khung để đọc chữ
```python
"""python cropbox.py <out.png> <file>:<page>:<top>:<bot> ...  (tỉ lệ chiều cao trang, 115 dpi)"""
import sys, pymupdf
from PIL import Image, ImageDraw
ims = []
for spec in sys.argv[2:]:
    f, p, a, b = spec.rsplit(":", 3); p = int(p); d = pymupdf.open(f); r = d[p - 1].rect
    x = d[p - 1].get_pixmap(dpi=115, clip=pymupdf.Rect(r.width * 0.05, r.height * float(a), r.width * 0.97, r.height * float(b)))
    im = Image.frombytes("RGB", (x.width, x.height), x.samples); ImageDraw.Draw(im).text((4, 4), f"p{p}", fill="red"); ims.append(im)
o = Image.new("RGB", (max(i.width for i in ims), sum(i.height for i in ims) + 6 * len(ims)), "red"); y = 0
for i in ims: o.paste(i, (0, y)); y += i.height + 6
o.save(sys.argv[1])
```
Để đọc số trang in: cắt `0.94:1.0` của trang (chân trang).

`obj.py` (mẫu cho từng bộ; ghi dần):
```python
L = "Kiến thức, kĩ năng"
T1, T2 = "SGK TOAN 12 TAP 1 - KNTT.pdf", "SGK TOAN 12 TAP 2 - KNTT.pdf"
O = {
 (T1, 7): (["<thuật ngữ 1>", "..."], ["<ý 1 nguyên văn>", "..."]),
}
# Ghi tiếp bằng: O.update({...}) ở cuối file
```

`mk_toan2.py`: dựng lô từ `obj.py` + `progress.json`
```python
"""python mk_toan2.py <out.json> <dir chứa obj.py> <unit> <grade> '{"SGK":1,"SCD":1}' ['{"<file>:<p0>": p_thật}']"""
import json, sys
sys.path.insert(0, sys.argv[2]); from obj import O, L
unit, grade = sys.argv[3], sys.argv[4]
OFF = json.loads(sys.argv[5]); REAL = json.loads(sys.argv[6]) if len(sys.argv) > 6 else {}
prog = json.load(open(f"glossary/khoi_{grade}/{unit}/progress.json", encoding="utf-8"))
batch = []
for f, b in prog["books"].items():
    t = f[:3]
    if t not in ("SGK", "SCD"): continue
    for ch, c in (b.get("chapters") or {}).items():
        for le, info in c["lessons"].items():
            p0 = info["pdf_pages"][0]; p = REAL.get(f"{f}:{p0}", p0)
            kt, obj = O.pop((f, p))
            batch.append({"chapter": ch, "lesson": le, "level": "co_ban" if t == "SGK" else "chuyen_de", "label": L,
                          "objectives": obj, "key_terms": kt,
                          "sources": [{"book_type": t.lower(), "file": f, "pdf_page": p, "printed_page": p - OFF[t]}],
                          "notes": None if p == p0 else f"Trang đầu bài là PDF {p} (pdf_pages trong progress.json bắt đầu ở PDF {p0})."})
assert not O, O.keys()
json.dump(batch, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(len(batch))
```
- Cho nhóm C: đặt `book_type: "gv"`, `file` = tên SGV, `level` theo tên SGV, `key_terms: []`. Nếu độ lệch trang không đều thì truyền `printed_page` theo dict.
- Cho Tiếng Anh: một mục mỗi `chapter` (`Unit N. …`) với `lesson: null`.

`prog_note.py`: ghi tiến độ vào progress.json
```python
"""python prog_note.py <book_root> <unit> <lesson_count> "<note>" """
import sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]) / "glossary" / "scripts"))
from _common import load_json, progress_path, setup_stdout, write_json_atomic
setup_stdout()
unit, count, note = sys.argv[2], int(sys.argv[3]), sys.argv[4]
p = progress_path(unit); prog = load_json(p)
prog["yccd"] = {"status": "done", "lesson_count": count, "note": note}
prog["last_session_note"] = (prog.get("last_session_note") + " | " if prog.get("last_session_note") else "") + note
write_json_atomic(p, prog); print("ok", unit)
```

Mẹo môi trường (Windows + Git Bash):
- Đặt `export PYTHONIOENCODING=utf-8` trước lệnh in tiếng Việt.
- Heredoc chứa dấu `'` trong chuỗi tiếng Việt có thể làm hỏng lệnh bash. Khi đó dùng công cụ Write để tạo file `.py`.
- Tesseract nằm ở `C:\Program Files\Tesseract-OCR\tesseract.exe`, tessdata ở `glossary/tessdata` (`vie`, `eng`).

---

## 5. Việc treo cần người dùng quyết định (chưa làm)

1. **sinh_12**: 9 bài có `pdf_pages` trong `progress.json` lệch so với trang đầu bài thật (SGK Bài 6, 9, 11, 17, 22, 25, 33, 35; SCD Bài 10). Đã đề xuất sửa progress; người dùng **chưa trả lời**.
2. **cong_nghe_nong_nghiep_10**: README Mục 9 ghi "SCD trang PDF = trang in", nhưng chân trang cho thấy +1 (54 nguồn SCD của terms cũng +1). 8 nguồn ở SCD PDF 72 ghi lệch 0, chưa xem ảnh. Đã đề xuất sửa README và kiểm tra 8 nguồn đó; **chưa trả lời**.
3. Các bộ khác cũng có `pdf_pages` lệch nhẹ (lich_su_11, tin_cs_11, toan_11, hoa_12, sinh_11): đã ghi `notes` trong `lessons`, **chưa sửa progress.json**.
4. (Đã xử lý 2026-10-23) `tieng_anh_12` đã làm xong 284 mục; `lessons` còn rỗng vì chưa có SGV Tiếng Anh 12 trong `sgk/khoi_12/tieng_anh_12/` — cần người dùng bổ sung. `dia_12` đã khai báo SGV trong `progress.json` (status pending). `validate.py` không tham số hiện 0 lỗi.
5. **Chưa commit gì** cho toàn bộ đợt này: schema, scripts, 27 file chuyển đổi, 22 bộ lessons, README/CLAUDE.md. Khi người dùng yêu cầu commit, đề xuất chia nhỏ, ví dụ:
   - `feat(schema): add lessons (learning objectives) to unit data`
   - `feat(glossary): add learning objectives for <group>`
   - `fix(ngu_van_12): correct printed_page of 51 term sources`

---

## 6. Những thay đổi hạ tầng đã làm trong đợt này (để không làm lại)

- `glossary/schema.json`: thêm `$defs/lesson`, `lessons` (bắt buộc), `meta.lesson_count`.
- `glossary/scripts/_common.py`: thêm `is_unit_data`, `dumps_unit` ghi cả `lessons` (mỗi mục một dòng), `progress_order`, `lesson_key`, `lesson_label`, `source_errors` (tách ra từ `term_errors`) và `lesson_errors`.
  - Đã sửa lỗi cũ: trước đây file có thêm key thì mất đồng bộ sang `dataset/`.
- `glossary/scripts/add_lessons.py` (mới), `validate.py` (kiểm tra lessons, lesson_count, cảnh báo dataset lệch), `check_sources.py` (đối chiếu bigram objectives, cảnh báo key_terms), `query.py --lessons`.
  - Người dùng sau đó tự thêm `query.py --format dict`, `dict_md.py`, `serve.py`; README đã ghi.
- README: Mục 4b (schema lessons), Mục 5 (chỉ dùng sách KNTT, không tự tải), Mục 7, Mục 10. CLAUDE.md: bước trích YCCĐ ở Giai đoạn 2–3 và quy tắc nguồn KNTT.
- `review-station/` (repo git riêng): người dùng đã tự cập nhật để hiển thị `lessons` và có `sync_data.py`. Sau khi thêm lessons cho bộ nào thì có thể chạy `python sync_data.py <unit>` trong `review-station/`. Không bắt buộc, không tự làm nếu không được yêu cầu.

---

## 7. Lệnh khởi động nhanh cho phiên mới

```
cd d:\Project\book
python glossary/scripts/validate.py toan_12
python -c "import json;p=json.load(open('glossary/khoi_12/toan_12/progress.json',encoding='utf-8'));[print(f,i['pdf_pages'][0],l) for f,b in p['books'].items() if f.startswith('SGK') for c in b['chapters'].values() for l,i in c['lessons'].items()]"
```
Sau đó: tạo scratchpad (`t12/`), dán `fullsheet.py`, `cropbox.py`, `mk_toan2.py`, `prog_note.py`, rồi làm theo Mục 4.

---

## 8. Bảng độ lệch trang (trang PDF − trang in) đã xác nhận bằng chân trang

Dùng để đoán `printed_page`, nhưng **vẫn phải xác nhận lại bằng ảnh chân trang** của từng trang (lớp 12 và vài sách lệch không đều).

| Bộ | SGK | SCD |
|---|---|---|
| ngu_van_10, van_11 | +1 | +1 |
| ngu_van_12 | +2…+4 (tăng dần) | không có SCD |
| sinh_10, sinh_11 | +1 | +1 |
| sinh_12 | +2 | +2 (Bài 1–4), +3 (Bài 5–8), +4 (Bài 9–10) |
| hoa_10, hoa_11 | +1 | +1 |
| hoa_12 | +2 | +2 |
| lich_su_10, lich_su_11 | +1 | +1 |
| lich_su_12 | +2 | +2 |
| cong_nghe_*_10 | +1 | +1 |
| tin_hoc_10, tin_cs_11, tin_ict_11 | +1 | +1 |
| toan_10, toan_11 | +1 | +1 |
| toan_12 | README ghi +2 (chưa kiểm chứng) | không có SCD |
| Chưa làm (README ghi) | vat_ly_10 +1; vat_ly_11 SGK +2, SCD/SGV +1; dia_10 +1; dia_11 SGK/SCD +2, SGV +1; dia_12 +2…+4; am_nhac_10 +1; tieng_anh_10 +1 | |

Quy luật: trang mở chương (tên chương) không in số; khung YCCĐ của bài đầu chương nằm ở **nửa dưới** trang đó. Số in nằm ở chân trang (góc trái hoặc phải tuỳ trang chẵn/lẻ).

---

## 9. Bẫy đã gặp và cách xử lý (đọc trước khi làm)

1. **`progress.json` lệch trang**: nhiều bài có `pdf_pages[0]` không phải trang đầu bài (thường là trang kế tiếp, đôi khi lệch tới 5 trang). Luôn nhìn ảnh trang trước khi tin. Khi dùng trang khác, ghi `notes`.
2. **OCR bỏ sót khung**: khung nằm dưới banner chuyên đề hoặc trong nền có hoa văn hay bị OCR bỏ qua. Dựa vào ảnh thu nhỏ, không dựa vào kết quả quét OCR. Quét OCR chỉ để gợi ý.
3. **Trùng nội dung giữa các bộ**: `tin_ict_11` Bài 1–16 giống hệt `tin_cs_11`; phần chung có thể dùng lại nhưng phải xác nhận trên ảnh và trang PDF.
4. **Khung có câu dẫn + gạch con** (vd "Trình bày được …:" rồi các gạch con): chọn một cách và ghi `notes`; các bộ đã làm giữ câu dẫn làm ý đầu hoặc gộp gạch con vào một ý (có notes).
5. **Bài "Ôn tập chương/Ôn tập cuối …" ở Hoá không có khung** → không tạo mục. Ở Ngữ văn/Sinh/Lịch sử thì "Ôn tập học kì" có khung "Yêu cầu cần đạt" → có mục.
6. **Mỗi chuyên đề SCD** ở Lịch sử, Ngữ văn, Tiếng Anh chỉ có một khung ở đầu chuyên đề → dùng `lesson: null`. Ở Toán/Tin/Sinh/Hoá/Công nghệ thì khung nằm ở từng bài.
7. **SCD Tin học 10 – ICT** đánh lại "Bài 1" cho mỗi chuyên đề: khoá `(level, chapter, lesson)` vẫn duy nhất nhờ `chapter`.
8. **Không đọc cả file `<unit>.json`**; dùng `query.py`. **Không sửa `<unit>.json` bằng tay** (README Mục 3); chỉ `add_terms.py` / `add_lessons.py`. Với `progress.json` dùng script ghi qua `write_json_atomic` (đồng bộ định dạng).
9. **Git hiện thấy ~34.000 dòng xoá** ở 6 file bộ (toan_11, lich_su_11, tin_ict_11, tin_cs_11, dia_12, ngu_van_12). Đó chỉ là chuẩn hoá định dạng sang "một mục một dòng"; nội dung JSON không đổi (đã so với HEAD).
10. **Console Windows**: in tiếng Việt cần `PYTHONIOENCODING=utf-8`. Heredoc bash có dấu `'` trong tiếng Việt có thể làm hỏng lệnh → ghi file bằng công cụ Write.
11. **Ảnh bị xoá khỏi ngữ cảnh** sau một thời gian; vì vậy ghi `obj.py` ngay sau khi đọc mỗi 3–4 khung.

---

## 10. Bối cảnh các việc khác trong dự án (đã làm, để không hỏi lại)

- **review-station/** (repo git riêng, nằm trong `book/`): app Python chuẩn thư viện, **chỉ còn trang duyệt từ điển thuật ngữ** (đã bỏ phần ngân hàng câu hỏi và `sample_questions.json`; bỏ ảnh trang sách theo yêu cầu).
  - Chạy: `cd review-station; python review_station.py --port 8080` → `http://127.0.0.1:8080`, mật khẩu mặc định `kntt2026` (biến `REVIEW_PASSWORD`).
  - Dữ liệu đọc từ `review-station/data/glossary/{units,progress}/`; làm mới bằng `python sync_data.py <unit...>` hoặc `--check --all`.
  - Kết quả duyệt lưu SQLite `storage/reviews.db`; xuất "lô sửa" để chạy `add_terms.py --update`.
  - Người dùng đã tự bổ sung hiển thị YCCĐ (`lessons`) trong app. 4 test pytest trong `tests/`.
- **Quy tắc nguồn**: chỉ sách KNTT (NXB GDVN); thiếu sách thì báo người dùng, không tự tải từ trang chia sẻ không chính thức. (Người dùng từng yêu cầu tự tải SGV; tôi đã từ chối vì lí do bản quyền, sau đó người dùng tự đặt `SGV Dia li 12 KNTT.pdf` vào thư mục.)
- **Đo quy mô**: dataset hiện có 28 bộ (27 có dữ liệu + `tieng_anh_12` chưa có file dữ liệu), tổng 4.540 thuật ngữ ở 27 bộ.
- **Trạng thái `validate.py` (không tham số) hiện tại**: 0 lỗi (28 bộ) từ 2026-10-23 (đã xử lý `tieng_anh_12` và `dia_12`). Mọi bộ OK; có cảnh báo "file lớn hơn 300 KB" ở vài bộ, bỏ qua.


---

## 11. Cập nhật 2026-10-23 (cuối phiên): đã làm xong toàn bộ danh sách còn lại

| Bộ | lessons | Nguồn | Ghi chú |
|---|---|---|---|
| toan_12 | 19 | SGK | Bài 9 thật ở PDF 77 (notes) |
| vat_ly_10 | 44 | SGV 34 + SGV CD 10 | label 'Mục tiêu' |
| vat_ly_11 | 26 | SGV | 12 bài lệch trang (notes); SCD thiếu SGV CD |
| dia_10 | 43 | SGV 40 + SGV CD 3 (lesson null) | chỉ '1. Về kiến thức, kĩ năng' |
| dia_11 | 31 | SGV | SCD thiếu SGV CD |
| dia_12 | 30 | SGV | 5 bài SGK không có bài SGV tương ứng (25, 26, 27, 28, 32); SCD thiếu SGV CD |
| am_nhac_10 | 45 | SGV 32 + SGV CD 13 | chép Kiến thức + Năng lực |
| tieng_anh_10 | 10 | SGV | theo Unit, lesson null; Review không có khung |
| tieng_anh_12 | 0 | chưa có SGV | chờ người dùng bổ sung; bộ đã làm xong 284 terms |

Còn treo (cần người dùng): SGV CD cho vat_ly_11, dia_11, dia_12; SGV Tiếng Anh 12; 5 bài dia_12 (cần SGV đúng bản SGK); các mục ở Mục 5 (sinh_12, cong_nghe_nong_nghiep_10, pdf_pages lệch). Chưa commit gì.


---

## 12. Cập nhật 2026-10-24: đã xử lý các mục treo ở Mục 5

- **sinh_12** (9 bài trong Mục 5 + các bài kề): sửa `pdf_pages` 18 bài (SGK 16, SCD 2) theo trang đầu bài thật (đối chiếu ảnh). Quy ước: bài sau bắt đầu ở trang tiêu đề, bài trước kết thúc ở trang liền trước; trang "Sơ đồ tóm tắt kiến thức chương" tính vào bài cuối chương.
- **Cùng lỗi ở bộ khác**: sửa `pdf_pages` ở lich_su_11 (Bài 4–13), tin_cs_11 (Bài 14, 15, 17, 18, 29, 30), toan_11 (Bài 3, 4, 10), toan_12 (Bài 9), hoa_12 (SCD Bài 1), ngu_van_12 (Bài 6: [6, 39]), vat_ly_11 SGV (20 bài, dựng lại theo vị trí khung Mục tiêu). sinh_11 không lệch. Đã gỡ các `notes` "Trang đầu bài là PDF …" của 38 mục `lessons` vì không còn đúng.
- **cong_nghe_nong_nghiep_10**: chân trang cho thấy SGK, SCD và SGV đều trang PDF = trang in + 1. Sửa `printed_page` của 22 nguồn (8 nguồn SCD PDF 72 ghi 72, đúng là 71; 14 nguồn SGV ghi lệch 0) và sửa dòng README Mục 9.
- **Phát hiện thêm**: `lich-su-11-quan-dao-truong-sa` có nguồn ở PDF 80 (cuối Bài 12) nhưng gán Bài 13 → đã chuyển sang Bài 12.
- Còn lại ở lich_su_11: 8 thuật ngữ SCD/SGK có nguồn phụ nằm ngoài `pdf_pages` của bài (vd `lich-su-11-doc-quyen`, `tranh-kim-hoang`, `phat-xit`, `le-thanh-tong`); chưa mở ảnh nên chưa kết luận.
- **Sách mới người dùng bổ sung** (chưa đăng kí vào `progress.json`, `validate.py` đang báo 4 lỗi vì thiếu): `SGV CD DIA LI 11.pdf`, `SGV CD DIA LI 12.pdf`, `SGV CD VAT LI 11.pdf`, `SGK Chuyên đề học tập Vật lí 11pdf.pdf` (tên SGK nhưng có vẻ là chuyên đề, cần đổi tên hoặc xác nhận); `tieng_anh_12/` có file tải dở `Unconfirmed 693490.crdownload`.
- Chưa commit gì.

---

## 13. Cập nhật 2026-10-24 (tiếp): sách chuyên đề mới

- `vat_ly_11` (+9 lessons SCD từ `SGV CD VAT LI 11.pdf`; tệp `SGK Chuyên đề học tập Vật lí 11pdf.pdf` đã bị người dùng xoá), `dia_11` (+3), `dia_12` (+3), `tieng_anh_12` (+10 từ `SGV TIENG ANH 12 Global Success.pdf`; `lessons` tổng 10).
- `toan_12`: thêm `SCD Toan 12.pdf` → +64 thuật ngữ chuyên đề, +7 lessons (`key_terms`); gộp nguồn SCD vào 3 mục SGK (chi phí/doanh thu/lợi nhuận biên). `SGV CD Toán 12.pdf` (bản trùng SGV Toán 12) đã bị người dùng xoá 2026-10-24; không có SGV Chuyên đề Toán 12, SCD dùng `lessons` từ chính SCD.
- `ngu_van_12`: thêm `SCD van 12.pdf` → +15 thuật ngữ (Bảng giải thích PDF 86–87, trang PDF = in + 2), +12 lessons (3 chuyên đề `lesson: null` + 9 Phần); đăng kí `SGV Ngữ văn 12 - Tập 1/2` vào `progress.json` (chưa trích mục 4–5 DESCRIPTION).
- (Đã xử lý ở Mục 14.)

---

## 14. Chốt 2026-10-24 (cuối phiên)

Đã làm nốt các việc còn lại ở Mục 13:
- **Kiểm tra mẫu SCD**: toan_12 (26 mục mẫu + so từng từ OCR cho cả 64 mục + đọc lại ảnh PDF 16, 62, 64) và ngu_van_12 (18/18 mục SCD đối chiếu ảnh), 0 sai. Ghi vào DESCRIPTION (toan_12 Mục 8; ngu_van_12 Mục 6) và README.
- **ngu_van_12**: thêm 3 thuật ngữ từ 'Tri thức tổng quát' Chuyên đề 2 (chuyển thể, chuyển thể bám sát / ít bám sát tác phẩm gốc), tổng 78 mục; DESCRIPTION Mục 2–6 cập nhật (SCD, SGV Tập 1–2: phân phối tiết, lưu ý sư phạm).
- **tieng_anh_12**: Mục 5 DESCRIPTION điền từ SGV (OCR `eng` toàn bộ 282 trang), kèm trang SGV.
- **toan_12**: DESCRIPTION cập nhật số liệu 155 mục, bảng chương gồm SCD, Mục 4 (đổi dòng 'Theo Chương trình GDPT 2018' thành nguồn chuẩn là `lessons`), Mục 8 kiểm định SCD; không có SGV Chuyên đề Toán 12.
- **dia_12**: Mục 4 bỏ câu 'Theo Chương trình GDPT 2018'; Mục 5 có cảnh báo: 5 mục sai lầm viết trước khi có SGV, chưa có trang nguồn, cần đối chiếu SGV.

Việc còn mở (cần người dùng hoặc phiên sau): (SGV Chuyên đề Toán 12: không có, không cần); kiểm tra độc lập cho các bộ ghi 'chờ kiểm tra độc lập' và phần SCD mới; đối chiếu Mục 5 của dia_12 với SGV; Mục 5 của ngu_van_12 chỉ có lưu ý sư phạm (SGV không có phần sai lầm HS); các mục Mục 5 cũ (sinh_12 pdf_pages đã sửa 2026-10-24). Chưa commit gì: đề xuất chia commit: `feat(schema)`, `feat(glossary): add learning objectives`, `feat(tieng_anh_12): add unit`, `feat(scd): add toan_12 and ngu_van_12 specialised topics`, `fix(progress): correct pdf_pages`, `docs: update README and DESCRIPTION`.

### Cập nhật cuối: dia_12 Mục 5 (2026-10-24)
Đã đối chiếu 5 mục sai lầm cũ với `SGV Dia li 12 KNTT.pdf` (OCR cả 198 trang + xem ảnh PDF 35). SGV không có mục sai lầm của HS; các mục cũ không có căn cứ như đã viết (vd 'áp cao Xibia', 'dân số vàng = gấp đôi người phụ thuộc' không có trong SGV/SGK) nên đã **thay** bằng 7 điểm phân biệt/lưu ý có trang nguồn (vùng biển, gió mùa và tín phong, phân hoá đông–tây, dân số vàng và già hoá, GRDP và GDP, kinh tế số và chuyển đổi số, sơ đồ tư duy). Việc mở còn lại: kiểm tra độc lập; commit.
