#!/usr/bin/env python3
"""Đối chiếu definition/term với text trang PDF nguồn. Không ghi gì vào file dữ liệu.

    python glossary/scripts/check_sources.py <unit> [--threshold 0.65] [--lesson TEXT]
        [--id ID ...] [--no-accent] [--no-ocr] [--verbose]

Với mỗi nguồn: lấy text các trang pdf_page-1, pdf_page, pdf_page+1 (text layer; nếu PDF dạng ảnh
thì OCR tiếng Việt bằng tesseract và cache vào glossary/<unit>/.ocr/).
Chuẩn hóa: chữ thường, NFC, bỏ LaTeX ($...$) và dấu câu, tách từ, bỏ từ 1 ký tự.
Mặc định so khớp CÓ DẤU tiếng Việt; --no-accent để so khớp không dấu.

Độ đo chính: tỉ lệ cặp từ liên tiếp (bigram, chỉ trong đoạn chữ giữa các công thức $...$)
của definition có trong 3 trang. Tỉ lệ từ đơn
(unigram) chỉ in để tham khảo. Thí điểm Bài 1–2 (Toán 10): dữ liệu đúng có bigram ≥ 0.70,
dữ liệu sai trang/bịa phần lớn < 0.5 → ngưỡng mặc định 0.65.
- Nguồn định nghĩa (sách ưu tiên cao nhất trong sources): gắn cờ nếu bigram < ngưỡng.
- Mọi nguồn: term/aliases phải xuất hiện (so cả chuỗi từ liên tiếp lẫn bản bỏ khoảng trắng,
  để chịu được lỗi OCR dính chữ; dự phòng so không dấu vì OCR hay sai dấu). Với type cong_thuc/quy_tac/ky_hieu/tinh_chat (tên thường do người trích đặt),
  không thấy term chỉ là CẢNH BÁO, không gắn cờ.
Script chỉ phát hiện định nghĩa bịa hoặc sai trang; sai sót nhỏ trong công thức cần kiểm tra mẫu.

Yêu cầu cần đạt (mảng lessons; bỏ qua khi lọc --id): gộp mọi objectives, so bigram với 3 trang quanh
nguồn chính, gắn cờ nếu < ngưỡng. key_terms không thấy trong trang chỉ là CẢNH BÁO.
"""
import argparse
import sys
import unicodedata

from _common import (BOOK_PRIORITY, LATEX_INLINE_RE, PageReader, load_unit, parse_unit, setup_stdout,
                     tokens)

SOFT_TERM_TYPES = {"cong_thuc", "quy_tac", "ky_hieu", "tinh_chat"}
PAGE_SEP = "|"


def contains_seq(hay, needle):
    n = len(needle)
    if n == 0:
        return False
    return any(hay[i:i + n] == needle for i in range(len(hay) - n + 1))


def bigrams(toks):
    return [b for b in zip(toks, toks[1:]) if PAGE_SEP not in b]


def norm(s):
    return unicodedata.normalize("NFC", s or "").casefold()


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("unit")
    ap.add_argument("--threshold", type=float, default=0.65, help="ngưỡng tỉ lệ bigram (mặc định 0.65)")
    ap.add_argument("--lesson")
    ap.add_argument("--id", nargs="+")
    ap.add_argument("--no-accent", action="store_true", help="so khớp không dấu")
    ap.add_argument("--no-ocr", action="store_true", help="chỉ dùng text layer và cache OCR sẵn có")
    ap.add_argument("--verbose", action="store_true", help="in tỉ lệ của mọi mục")
    a = ap.parse_args()
    if not parse_unit(a.unit):
        sys.exit(f"LỖI: tên bộ không hợp lệ: {a.unit}")

    keep = not a.no_accent
    reader = PageReader(a.unit, allow_ocr=not a.no_ocr)
    data = load_unit(a.unit)
    terms = data["terms"]
    lessons = data.get("lessons") or []
    if a.lesson:
        terms = [t for t in terms if norm(a.lesson) in norm(t["lesson"])]
        lessons = [e for e in lessons if norm(a.lesson) in norm(e["lesson"] or e["chapter"])]
    if a.id:
        terms = [t for t in terms if t["id"] in a.id]
        lessons = []

    page_cache = {}

    def page_tokens(file, page):
        key = (file, page)
        if key not in page_cache:
            text, how = reader.text(file, page)
            page_cache[key] = (None, how) if text is None else (
                (tokens(text, keep, False), tokens(text, False, False)), how)
        return page_cache[key]

    def window(s):
        """Token 3 trang quanh nguồn (có dấu theo tuỳ chọn, và bản không dấu); None nếu không đọc được trang chính."""
        main_toks, how = page_tokens(s["file"], s["pdf_page"])
        if main_toks is None:
            return None, None, how
        hay, hay_plain = [], []
        for p in (s["pdf_page"] - 1, s["pdf_page"], s["pdf_page"] + 1):
            if p < 1:
                continue
            toks, _ = page_tokens(s["file"], p)
            if toks:
                hay += toks[0] + [PAGE_SEP]
                hay_plain += toks[1] + [PAGE_SEP]
        return hay, hay_plain, how

    def found(name, h, acc):
        nt = tokens(name, acc)
        return bool(nt) and (contains_seq(h, nt) or "".join(nt) in "".join(h))

    def by_priority(sources):
        return sorted(enumerate(sources), key=lambda x: (BOOK_PRIORITY[x[1]["book_type"]], x[0]))

    passed, flagged, unverifiable, warned, rows = [], [], [], [], []
    for t in terms:
        srcs = by_priority(t["sources"])
        reasons, unver, warns, details = [], [], [], []
        for rank, (_, s) in enumerate(srcs):
            label = f"{s['file']} tr.{s['pdf_page']}"
            hay, hay_plain, how = window(s)
            if hay is None:
                unver.append(f"{label}: {how}")
                continue

            names = [t["term"], *t["aliases"]]
            # Tên thuật ngữ: so có dấu, dự phòng không dấu (OCR hay sai dấu: "bắt"/"bất", "ân"/"ẩn").
            term_found = any(found(n, hay, keep) or found(n, hay_plain, False) for n in names)

            def_toks = tokens(t["definition"], keep)
            uni = sum(w in set(hay) for w in def_toks) / len(def_toks) if def_toks else None
            # Bigram chỉ trong từng đoạn chữ giữa các công thức $...$ (không ghép từ vắt qua công thức).
            def_bi = [b for seg in LATEX_INLINE_RE.split(t["definition"]) for b in bigrams(tokens(seg, keep))]
            hay_bi = set(bigrams(hay))
            bi = sum(b in hay_bi for b in def_bi) / len(def_bi) if def_bi else None
            score = bi if bi is not None else uni  # definition 1 từ: dùng unigram
            r_txt = ("—" if bi is None else f"bigram {bi:.2f}") + ("" if uni is None else f", từ đơn {uni:.2f}")
            details.append(f"{label} [{how}] {r_txt}, term {'có' if term_found else 'KHÔNG'}")

            if rank == 0 and score is not None and score < a.threshold:
                reasons.append(f"{label}: {r_txt} < {a.threshold}")
            if not term_found:
                msg = f"{label}: không thấy term/aliases trong 3 trang"
                (warns if t["type"] in SOFT_TERM_TYPES else reasons).append(msg)
        if reasons:
            flagged.append((t, reasons, details))
        elif unver:
            unverifiable.append((t, unver))
        else:
            passed.append(t)
        if warns and not reasons:
            warned.append((t, warns, details))
        rows.append((t, details))

    mode = "có dấu" if keep else "không dấu"
    print(f"== check_sources {a.unit} (ngưỡng bigram {a.threshold}, so khớp {mode})")
    print(f"Tổng: {len(terms)} | Đạt: {len(passed)} | Gắn cờ: {len(flagged)} | "
          f"Không kiểm tra được: {len(unverifiable)} | Cảnh báo (trong số đạt): {len(warned)}")

    if a.verbose:
        print("\n-- Chi tiết mọi mục:")
        for t, details in rows:
            print(f"  {t['id']}: " + " | ".join(details))
    if flagged:
        print("\n-- GẮN CỜ:")
        for t, reasons, details in flagged:
            print(f"  {t['id']} ({t['term']})")
            for r in reasons:
                print(f"     lý do: {r}")
            for d in details:
                print(f"     nguồn: {d}")
    if unverifiable:
        print("\n-- KHÔNG KIỂM TRA ĐƯỢC:")
        for t, why in unverifiable:
            print(f"  {t['id']}: " + "; ".join(why))
    if warned:
        print("\n-- CẢNH BÁO (tên cong_thuc/quy_tac/ky_hieu/tinh_chat không có nguyên văn trong trang):")
        for t, warns, details in warned:
            print(f"  {t['id']} ({t['term']}): " + " | ".join(details))
    noted = [t for t in terms if t.get("notes")]
    print(f"\n-- Mục có notes ({len(noted)}):")
    for t in noted:
        print(f"  {t['id']}: {t['notes']}")

    if not lessons:
        return
    l_pass, l_flag, l_unver, l_warn = 0, [], [], []
    for e in lessons:
        lab = f"{e['chapter']} › {e['lesson'] or '(cả chương)'} [{e['level']}]"
        _, s = by_priority(e["sources"])[0]
        src_lab = f"{s['file']} tr.{s['pdf_page']}"
        hay, hay_plain, how = window(s)
        if hay is None:
            l_unver.append(f"{lab}: {src_lab}: {how}")
            continue
        obj_bi = [b for o in e["objectives"] for seg in LATEX_INLINE_RE.split(o) for b in bigrams(tokens(seg, keep))]
        hay_bi = set(bigrams(hay))
        bi = sum(b in hay_bi for b in obj_bi) / len(obj_bi) if obj_bi else 0.0
        missing = [k for k in e["key_terms"] if not (found(k, hay, keep) or found(k, hay_plain, False))]
        if bi < a.threshold:
            l_flag.append(f"{lab}: {src_lab} bigram {bi:.2f} < {a.threshold}")
        else:
            l_pass += 1
        if missing:
            l_warn.append(f"{lab}: key_terms không thấy trong 3 trang: {missing}")
        if a.verbose:
            print(f"  {lab}: {src_lab} [{how}] bigram {bi:.2f}")

    print(f"\n== Yêu cầu cần đạt: {len(lessons)} mục | Đạt: {l_pass} | Gắn cờ: {len(l_flag)} | "
          f"Không kiểm tra được: {len(l_unver)} | Cảnh báo key_terms: {len(l_warn)}")
    for title, items in (("GẮN CỜ", l_flag), ("KHÔNG KIỂM TRA ĐƯỢC", l_unver), ("CẢNH BÁO", l_warn)):
        if items:
            print(f"\n-- YCCĐ {title}:")
            for m in items:
                print(f"  {m}")


if __name__ == "__main__":
    main()
