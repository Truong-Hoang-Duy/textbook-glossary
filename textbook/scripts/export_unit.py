"""Cổng 3 (spec mục 6, 7): xuất textbook/dataset/<unit>.json từ progress.json, Tầng 1 và Tầng 2.

    python textbook/scripts/export_unit.py <unit> [--date YYYY-MM-DD] [--check]

Dừng và báo lỗi, không đoán, khi: thuật ngữ in_source không có chỗ in đậm ở Tầng 1, id trùng,
hoặc JSON không hợp lệ theo textbook/schema/unit.schema.json. --check: chỉ kiểm tra, không ghi file.
"""

import argparse
import datetime
import re
import sys

from _common import (TEXTBOOK_DIR, display_title, iter_nodes, load_json, load_profile, load_progress, parse_unit,
                     schema_errors, section_matchers, setup_stdout, slugify, unit_dir, write_json)
from check_dict import BOLD_RE, DESC, NOTE_RE, OUT_RE, TERM_RE, norm, parse_rows, split_term
from check_lesson import PAGE_RE, lesson_paths, split_frontmatter

SERIES = "Kết nối tri thức với cuộc sống"
PUBLISHER = "NXB Giáo dục Việt Nam"


def walk_body(body, matchers):
    """Duyệt từng dòng thân bài, kèm (trang PDF, mục) tại dòng đó. Cấp mục lấy từ hồ sơ môn.

    Heading ## / ### không khớp cấp mục nào (hộp emoji, heading thêm của hồ sơ) là "hộp":
    trong hộp section = None; gặp heading cấp mục kế tiếp thì tiếp tục mục cũ.
    """
    page, nums, box = None, [None] * len(matchers), False
    for line in body.splitlines():
        s = line.strip()
        m = PAGE_RE.match(s)
        if m:
            page = int(m.group(1))
            continue
        hit = None
        for i, (prefix, rx) in enumerate(matchers):
            if s.startswith(prefix):
                mm = rx.match(s[len(prefix):])
                if mm:
                    hit = (i, mm.group(1))
                    break
        if hit:
            i, num = hit
            nums[i:] = [num] + [None] * (len(matchers) - i - 1)
            if matchers[i][0] != "**":
                box = False
        elif s.startswith(("## ", "### ", "#### ")):
            box = True
        parts = []
        for n in nums:
            if n is None:
                break
            parts.append(n)
        section = None if box or not parts else ".".join(parts)
        yield line, page, section


def lesson_extras(node, path, offset, unit, matchers):
    """objectives, key_terms, figures, vị trí in đậm và vị trí nhãn mô tả của một bài Tầng 1."""
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    objectives, key_terms, bolds, tags = None, [], {}, {}
    block, label, block_page = None, None, None
    for line, page, section in walk_body(body, matchers):
        s = line.strip()
        if s.startswith("## "):
            if s.startswith("## 🎯 "):
                block, label, block_page = "obj", s[5:].strip(), page
                objectives = {"label": label, "items": [], "pdf_page": page}
            elif re.match(r"## I\. YÊU CẦU CẦN ĐẠT$", s) and objectives is None:
                block = "obj"
                objectives = {"label": "Yêu cầu cần đạt", "items": [], "pdf_page": page}
            elif s.startswith("## 🔤"):
                block = "key"
            else:
                block = None
            continue
        if block == "obj" and s and not s.startswith("<!--"):
            objectives["items"].append(re.sub(r"^- ", "", s))
        elif block == "key" and s.startswith("- "):
            key_terms.append(s[2:])
        loc = {"lesson_id": node["id"], "section": section, "pdf_page": page, "printed_page": page - offset if page else None}
        for name in TERM_RE.findall(s):
            tags.setdefault(norm(name), loc)
        para_bolds = BOLD_RE.findall(s)
        heading = re.fullmatch(r"\*\*[a-z]\)\s*([^*]+)\*\*", s)
        for b in ([heading.group(1)] if heading else para_bolds):
            bolds.setdefault(norm(b.strip().rstrip(":")), loc)
    if objectives is not None and not objectives["items"]:
        objectives = None

    figures = []
    fig_file = path.parent / "figures.json"
    specs = load_json(fig_file) if fig_file.exists() else {}
    subject, grade = parse_unit(unit)
    table = body.split("## 📷", 1)[1] if "## 📷" in body else ""
    captions = {c[0]: c[3] for c in parse_rows(table.splitlines()) if len(c) == 4}
    for fid, spec in specs.items():
        if fid.startswith(f"H{grade}-{subject}-{node['id']}-"):
            figures.append({"id": fid, "file": f"img/{fid}.png",
                            "caption": captions.get(fid, "").replace("\\*", "*") or fid,
                            "pdf_page": spec["pdf_page"]})
    return objectives, key_terms, figures, bolds, tags


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    progress = load_progress(a.unit)
    profile = load_profile(a.unit)
    matchers = section_matchers(profile)
    col_keys = profile["dictionary_columns"]["keys"]
    base = unit_dir(a.unit)
    offsets = {f["file"]: f["printed_offset"] for f in progress["files"]}
    paths = lesson_paths(a.unit, progress["toc"])
    errors, bold_loc, tag_loc = [], {}, {}

    def build(node, parents):
        out = {k: node[k] for k in ("id", "role", "kind", "label", "number", "title")}
        if node["role"] == "group":
            out["children"] = [build(c, parents + (node,)) for c in node["children"]]
            return out
        offset = node.get("printed_offset", offsets[node["source_file"]])
        rel = "/".join([p["dir"] for p in parents] + [node["file"]]) if node.get("file") else None
        if node["role"] == "lesson":
            out["lesson_type"] = node["lesson_type"]
        out.update({"file": rel, "source_file": node["source_file"], "pdf_pages": node["pdf_pages"],
                    "printed_pages": [p - offset for p in node["pdf_pages"]], "status": node["status"]})
        if node["role"] == "lesson":
            objectives, key_terms, figures = None, [], []
            path = paths.get(node["id"], (None, None, None))[1]
            if path is not None and path.exists():
                objectives, key_terms, figures, bolds, tags = lesson_extras(node, path, offset, a.unit, matchers)
                for k, v in tags.items():
                    tag_loc.setdefault(k, v)
                figures = [dict(f, file="/".join([p["dir"] for p in parents] + [f["file"]])) for f in figures]
                for k, v in bolds.items():
                    bold_loc.setdefault(k, v)
            out.update({"objectives": objectives, "key_terms": key_terms, "figures": figures})
        elif node["role"] == "back_matter" and node.get("file"):
            # bảng thuật ngữ cuối sách: nguồn định nghĩa dự phòng (spec 5.7)
            path = paths.get(node["id"], (None, None, None))[1]
            if path is not None and path.exists():
                _, _, _, bolds, tags = lesson_extras(node, path, offset, a.unit, matchers)
                for k, v in bolds.items():
                    bold_loc.setdefault(k, v)
                for k, v in tags.items():
                    tag_loc.setdefault(k, v)
        return out

    toc = [build(n, ()) for n in progress["toc"]]
    nodes = {n["id"]: n for n, _ in iter_nodes(progress["toc"])}
    by_title = {}
    for n in nodes.values():
        if n["role"] == "lesson" and n.get("label"):
            by_title[f"{n['label']}: {n['title']}"] = n["id"]
            by_title[n["label"]] = n["id"]

    dictionaries, terms, notes = [], [], []
    term_group = {}  # id(rec) -> id nhóm của từ điển, dùng làm hậu tố khi id trùng mà không có location
    prefix = a.unit.replace("_", "-")
    for dpath in sorted(base.glob("Tu-dien-*.md")):
        fm, body = split_frontmatter(dpath.read_text(encoding="utf-8"))
        group = next(n for n in nodes.values() if n["role"] == "group" and display_title(n) == fm["chuong"])
        title = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), fm["name"])
        sections, cur = {}, None
        for line in body.splitlines():
            if line.startswith("## "):
                cur = line[3:].strip()
                sections[cur] = []
            elif cur:
                sections[cur].append(line)
        dictionaries.append({
            "file": dpath.name, "name": fm["name"], "title": title, "group_id": group["id"],
            "lesson_ids": [c["id"] for c in group["children"] if c["role"] == "lesson"],
            "conventions": [l.strip()[2:] for l in sections.get("Quy ước sử dụng", []) if l.strip().startswith("- ")],
            "status": fm["trang_thai"], "created": str(fm["ngay_tao"]), "updated": str(fm["ngay_cap_nhat"])})

        dict_terms = []
        for name, lines in sections.items():
            if name in ("Quy ước sử dụng", "Đã xét, không tạo mục", "Ghi chú nguồn cần kiểm tra"):
                continue
            for cells in parse_rows([l for l in lines if l.startswith("|")][1:]):
                term, aliases = split_term(cells[0])
                meaning = cells[2]
                out = OUT_RE.match(meaning)
                desc = cells[3].startswith(DESC)
                rec = {"id": f"{prefix}-{slugify(term, 80).lower()}", "term": term, "aliases": aliases,
                       "english": None, "notation": None, "meaning": None if out else meaning,
                       "usage_context": (cells[3][len(DESC):] if desc else cells[3]) or None,
                       "scope": "shared" if name == "Thuật ngữ dùng chung" else "lesson",
                       "source_status": "out_of_source" if out else "described" if desc else "in_source",
                       "reference": None, "location": None, "dictionary": dpath.name, "note_ids": []}
                rec[col_keys[1]] = cells[1] or None
                if out:
                    ref = out.group(2).strip()
                    rec["reference"] = None if ref == "chưa xác định" else ref
                else:
                    where = tag_loc if desc else bold_loc
                    loc = next((where[k] for k in [norm(term)] + [norm(x) for x in aliases] if k in where), None)
                    if loc is None:
                        errors.append(f"{dpath.name}: '{term}' không có " + ("nhãn mô tả" if desc else "chỗ in đậm") + " ở Tầng 1")
                    rec["location"] = loc
                dict_terms.append(rec)
                term_group[id(rec)] = group["id"]
        terms += dict_terms

        for line in sections.get("Ghi chú nguồn cần kiểm tra", []):
            s = line.strip()
            m = NOTE_RE.match(s)
            if not m:
                continue
            number = int(s.split(".", 1)[0])
            where, term_name, rest = m.group(2), m.group(3), m.group(4)
            issue, _, resolution = rest.partition(" → ")
            resolved_on = None
            if resolution:
                d = re.search(r" \((\d{4}-\d{2}-\d{2})\)$", resolution)
                resolved_on = d.group(1) if d else None
                resolution = resolution[:d.start()] if d else resolution
            lm = re.match(r"(Bài \d+)", where)
            sm = re.search(r"mục ([IVX]+(?:\.\d+(?:\.[a-z])?)?)", where)
            pm = re.search(r"pdf:(\d+)", where)
            tids = [t["id"] for t in dict_terms if term_name.strip() not in ("—", "") and
                    norm(t["term"]) == norm(split_term(term_name)[0])]
            note_id = f"{fm['name']}#{number}"
            status = "open" if m.group(1) == "mở" else "closed"
            notes.append({"id": note_id, "dictionary": dpath.name, "number": number, "status": status,
                          "lesson_id": by_title.get(lm.group(1)) if lm else None,
                          "section": sm.group(1) if sm else None, "pdf_page": int(pm.group(1)) if pm else None,
                          "term_ids": tids, "issue": issue.strip(),
                          "resolution": resolution.strip() or None, "resolved_on": resolved_on})
            if status == "open":
                for t in dict_terms:
                    if t["id"] in tids:
                        t["note_ids"].append(note_id)

    seen = {}
    for t in terms:
        if t["id"] in seen:
            lid = (t["location"] or {}).get("lesson_id") or term_group.get(id(t)) or "chung"
            t["id"] = f"{t['id']}-{lid}"
        if t["id"] in seen:
            errors.append(f"id trùng: {t['id']}")
        seen[t["id"]] = t

    subject, grade = parse_unit(a.unit)
    data = {
        "meta": {"schema_version": "2.3", "unit": a.unit, "subject": subject, "profile": profile["profile"],
                 "subject_name": progress["subject_name"], "grade": grade, "generated_at": a.date,
                 "counts": {"lessons": sum(1 for n in nodes.values() if n["role"] == "lesson"),
                            "terms": len(terms),
                            "terms_described": sum(t["source_status"] == "described" for t in terms),
                            "terms_out_of_source": sum(t["source_status"] == "out_of_source" for t in terms),
                            "open_notes": sum(n["status"] == "open" for n in notes)}},
        "source": {"book_type": "sgk", "series": SERIES, "publisher": PUBLISHER, "files": progress["files"]},
        "toc": toc, "dictionaries": dictionaries, "terms": terms, "source_notes": notes,
    }
    errors += schema_errors(data, "unit")
    if errors:
        print("Cổng 3 KHÔNG ĐẠT:\n  " + "\n  ".join(errors))
        sys.exit(1)
    out = TEXTBOOK_DIR / "dataset" / f"{a.unit}.json"
    c = data["meta"]["counts"]
    if not a.check:
        write_json(out, data)
    print(f"Cổng 3 ĐẠT: {c['terms']} thuật ngữ ({c['terms_described']} mô tả, {c['terms_out_of_source']} Ngoài nguồn), "
          f"{len(dictionaries)} từ điển, {len(notes)} ghi chú ({c['open_notes']} mở), {c['lessons']} bài"
          + ("" if a.check else f" → {out.relative_to(TEXTBOOK_DIR.parent)}"))


if __name__ == "__main__":
    main()
