"""Dựng từ điển thuật ngữ dạng bảng Markdown (query.py --format dict).

Module độc lập, chỉ dùng thư viện chuẩn: review-station nhận một bản sao qua sync_data.py, nên không
import _common. Đầu vào là dữ liệu đã lọc; hàm render() không đọc file.
"""
import datetime
import json
import re
import unicodedata

TYPE_NAMES = {
    "dinh_nghia": "Định nghĩa", "dinh_ly": "Định lí", "tinh_chat": "Tính chất",
    "cong_thuc": "Công thức", "ky_hieu": "Kí hiệu", "quy_tac": "Quy tắc",
}
BOOK_NAMES = {"sgk": "SGK", "scd": "SCD", "gv": "SGV", "sbt": "SBT"}
ABBR_RE = re.compile(r"[A-ZĐ][A-Za-zĐđ\-]{1,7}")


def norm(s):
    return unicodedata.normalize("NFC", s or "").casefold()


def cell(s):
    """Nội dung một ô bảng Markdown: thoát '|', xuống dòng thành <br>."""
    return (s or "").replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def short_src(s):
    out = f"{BOOK_NAMES.get(s['book_type'], s['book_type'])} tr.PDF {s['pdf_page']}"
    return out + (f" (in {s['printed_page']})" if s.get("printed_page") else "")


def abbreviations(terms):
    """{viết tắt: [term]} lấy từ aliases: một từ ngắn viết hoa, không chữ số, không nằm sẵn trong term;
    có ≥ 2 chữ hoa, hoặc ≤ 3 kí tự và được sách ghi trong ngoặc, vd "(Ori)"."""
    out = {}
    for t in terms:
        for al in t["aliases"]:
            if not ABBR_RE.fullmatch(al) or al in t["term"]:
                continue
            if sum(c.isupper() for c in al) < 2 and (len(al) > 3 or f"({al})" not in t["term"] + t["definition"]):
                continue
            if t["term"] not in out.setdefault(al, []):
                out[al].append(t["term"])
    return dict(sorted(out.items(), key=lambda kv: norm(kv[0])))


def render(unit, meta, terms, lessons, lesson_order, names, scope=""):
    """terms, lessons: các mục đã lọc. lesson_order: [(chapter, lesson)] theo progress.json
    (lesson None = vị trí đầu chương). names: {id: term} để in tên thuật ngữ liên quan. scope: mô tả bộ lọc."""
    order = {}
    for ch, le in lesson_order:
        order.setdefault((ch, None), len(order))
        order.setdefault((ch, le), len(order))

    # Nhóm theo (chapter, lesson), sắp theo progress.json; lesson None = yêu cầu cần đạt cả chương
    groups = {}
    for e in lessons:
        groups.setdefault((e["chapter"], e["lesson"]), {"lessons": [], "terms": []})["lessons"].append(e)
    for t in terms:
        groups.setdefault((t["chapter"], t["lesson"]), {"lessons": [], "terms": []})["terms"].append(t)
    keys = sorted(groups, key=lambda k: (order.get(k, order.get((k[0], None), len(order))), k[1] is not None))

    chapters = list(dict.fromkeys(k[0] for k in keys))
    files = sorted({s["file"] for t in terms for s in t["sources"]} | {s["file"] for e in lessons for s in e["sources"]})
    title = f"Từ điển thuật ngữ {meta['subject_name']} {meta['grade']}"
    if scope and len(chapters) == 1:
        title += f" — {chapters[0]}"

    def yaml_str(s):
        return json.dumps(s, ensure_ascii=False)

    lines = ["---", f"unit: {unit}", f"mon: {yaml_str(meta['subject_name'])}", f"lop: {meta['grade']}",
             "chuong:", *[f"  - {yaml_str(c)}" for c in chapters],
             "nguon:", *[f"  - {yaml_str(f)}" for f in files],
             f"bo_loc: {yaml_str(scope or 'toàn bộ')}",
             f"so_thuat_ngu: {len(terms)}", f"so_bai_yccd: {len(lessons)}",
             f"ngay_cap_nhat_du_lieu: {meta['last_updated']}", f"ngay_xuat: {datetime.date.today().isoformat()}",
             "trang_thai: kiem-tra", "---", "", f"# {title}", "",
             "Dữ liệu trích nguyên văn từ sách Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam), "
             "xuất từ glossary để kiểm tra. Cột \"Bối cảnh sử dụng\" ghi loại thuật ngữ, thuật ngữ liên quan "
             "và trang nguồn để đối chiếu.", "",
             "## Quy ước sử dụng", "",
             "- Dùng đúng tên ở cột \"Thuật ngữ\", không thay bằng từ đồng nghĩa."]
    abbr = abbreviations(terms)
    if abbr:
        lines.append("- Viết tắt: " + "; ".join(f"{k} = {' / '.join(v)}" for k, v in abbr.items())
                     + ". Lần đầu xuất hiện thì viết đầy đủ.")
    lines.append("")

    header = ["| Thuật ngữ | Tên khác / Tiếng Anh | Giải nghĩa | Bối cảnh sử dụng |", "|---|---|---|---|"]
    current = None
    for ch, le in keys:
        g = groups[(ch, le)]
        if ch != current:
            lines += [f"## {ch}", ""]
            current = ch
        if le is not None:
            lines += [f"### {le}", ""]
        for e in g["lessons"]:
            lines.append(f"**{e['label']}** ({'; '.join(short_src(s) for s in e['sources'])})")
            lines.append("")
            lines += [f"- {o}" for o in e["objectives"]]
            if e["key_terms"]:
                lines.append(f"- *Thuật ngữ:* {', '.join(e['key_terms'])}")
            if e.get("notes"):
                lines.append(f"- *Ghi chú:* {e['notes']}")
            lines.append("")
        if g["terms"]:
            lines += header
            for t in g["terms"]:
                nota = t.get("notation")
                if nota and "$" not in nota:
                    nota = f"${nota}$"
                gloss = t["definition"] + (f" Kí hiệu: {nota}." if nota else "")
                ctx = [TYPE_NAMES.get(t["type"], t["type"]) + "."]
                related = [names.get(r, r) for r in t["related_terms"]]
                if related:
                    ctx.append("Liên quan: " + ", ".join(related) + ".")
                ctx.append("Nguồn: " + "; ".join(short_src(s) for s in t["sources"]) + ".")
                lines.append(f"| {cell(t['term'])} | {cell('; '.join(t['aliases']))} | {cell(gloss)} | {cell(' '.join(ctx))} |")
            lines.append("")

    lines += ["## Ghi chú nguồn cần kiểm tra", ""]
    noted = [t for t in terms if t.get("notes")] + [e for e in lessons if e.get("notes")]
    if not noted:
        lines.append("Không có.")
    for i, x in enumerate(noted, 1):
        name = x.get("term") or f"Yêu cầu cần đạt — {x['lesson'] or x['chapter']}"
        where = x["lesson"] or x["chapter"]
        lines.append(f"{i}. **{name}** ({where}; {'; '.join(short_src(s) for s in x['sources'])}): {x['notes']}")
    return "\n".join(lines) + "\n"


def filename(unit, chapter=None, lesson=None, level=None):
    """Tên file không dấu: tu_dien_<unit>[_<bài hoặc chương>][_<level>].md"""
    parts = [f"tu_dien_{unit}"]
    scope = lesson or chapter
    if scope:
        ascii_ = unicodedata.normalize("NFD", scope.replace("đ", "d").replace("Đ", "D"))
        ascii_ = "".join(c for c in ascii_ if unicodedata.category(c) != "Mn").lower()
        parts.append(re.sub(r"[^a-z0-9]+", "_", ascii_).strip("_")[:40])
    if level:
        parts.append(level)
    return "_".join(parts) + ".md"
