#!/usr/bin/env python3
"""Lọc thuật ngữ mà không cần nạp cả file vào ngữ cảnh.

    python glossary/scripts/query.py <unit|mon> [--lesson TEXT] [--chapter TEXT] [--type TYPE]
        [--level LEVEL] [--q TEXT] [--id ID ...] [--has-notes] [--fields a,b,c|all]
        [--sample N [--seed S]] [--count]

<unit> (vd toan_10): chỉ tìm trong bộ đó. <mon> (vd toan): mọi bộ có meta.subject trùng.
Lọc là tìm chuỗi con, không phân biệt hoa thường. --q tìm trong term, aliases, definition, notation.
Mặc định in các trường: id, term, definition, notation, sources.

--lessons: in "Yêu cầu cần đạt" (mảng lessons) thay cho thuật ngữ; dùng được kèm --chapter, --lesson,
--level, --q (tìm trong objectives, key_terms), --has-notes, --count, --format, --out.

--format dict: xuất từ điển thuật ngữ dạng bảng Markdown để kiểm tra (chỉ một bộ): frontmatter, quy ước
(viết tắt suy từ aliases), mỗi bài gồm yêu cầu cần đạt + bảng Thuật ngữ | Tên khác / Tiếng Anh |
Giải nghĩa | Bối cảnh sử dụng, cuối file là các mục có notes. Bộ lọc --chapter/--lesson/--level áp dụng
cho cả thuật ngữ và yêu cầu cần đạt.
"""
import argparse
import json
import random
import sys
import unicodedata
from pathlib import Path

import dict_md
from _common import load_unit, progress_order, resolve_target, setup_stdout, unit_dir, units_of_subject

DEFAULT_FIELDS = ["id", "term", "definition", "notation", "sources"]


def norm(s):
    return unicodedata.normalize("NFC", s or "").casefold()


def contains(hay, needle):
    return norm(needle) in norm(hay)


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="tên bộ (toan_10) hoặc tên môn (toan)")
    ap.add_argument("--lesson")
    ap.add_argument("--chapter")
    ap.add_argument("--type")
    ap.add_argument("--level")
    ap.add_argument("--q")
    ap.add_argument("--id", nargs="+", help="lấy đúng các id này")
    ap.add_argument("--has-notes", action="store_true", help="chỉ mục có notes")
    ap.add_argument("--fields", help="danh sách trường, phân cách bằng dấu phẩy; 'all' = mọi trường")
    ap.add_argument("--sample", type=int, help="chọn ngẫu nhiên N mục từ kết quả")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--count", action="store_true", help="chỉ in số mục khớp")
    ap.add_argument("--format", choices=["json", "text", "md", "dict"], default="json", help="định dạng xuất: json (mặc định), text (dễ đọc), md (markdown) hoặc dict (từ điển dạng bảng để kiểm tra)")
    ap.add_argument("--audit", action="store_true", help="chế độ kiểm tra mẫu Giai đoạn 4: lấy 30 mục chuẩn (20 ngẫu nhiên + 10 công thức) xuất ra sample_audit.md")
    ap.add_argument("--out", help="đường dẫn file xuất (UTF-8)")
    ap.add_argument("--lessons", action="store_true", help="in yêu cầu cần đạt theo bài thay cho thuật ngữ")
    a = ap.parse_args()

    if a.lessons:
        query_lessons(a)
        return

    if a.format == "dict" and len(resolve_target(a.target)) != 1:
        sys.exit("LỖI: --format dict chỉ áp dụng cho một bộ cụ thể (vd: sinh_12)")

    if a.audit:
        units = resolve_target(a.target)
        if len(units) != 1:
            sys.exit("LỖI: --audit chỉ áp dụng cho một bộ cụ thể (vd: toan_10)")
        unit = units[0]
        terms = load_unit(unit)["terms"]
        rng = random.Random(a.seed or 2026)
        n_rand = 20 if a.sample is None else a.sample
        sample_rand = rng.sample(terms, min(n_rand, len(terms)))
        sample_ids = {t["id"] for t in sample_rand}

        candidates = [t for t in terms if t["id"] not in sample_ids and (
            t.get("type") in ("cong_thuc", "dinh_ly") or t.get("notation")
        )]
        sample_formula = rng.sample(candidates, min(10, len(candidates))) if candidates else []
        rows = sample_rand + sample_formula
        a.format = "md"
        if not a.out:
            a.out = str(unit_dir(unit) / "sample_audit.md")
    else:
        rows = filter_terms(resolve_target(a.target), a)

        if a.sample is not None and a.sample < len(rows):
            rows = random.Random(a.seed).sample(rows, a.sample)

    if a.count:
        print(len(rows))
        return

    output_content = ""
    if a.format == "text":
        lines = []
        for i, t in enumerate(rows, 1):
            src_str = "; ".join(
                f"{s['file']} tr.{s['pdf_page']}" + (f" (in: {s['printed_page']})" if s.get("printed_page") else "")
                for s in t.get("sources", [])
            )
            lines.append(f"[{i}] {t['term']} ({t['id']})")
            if t.get("notation"):
                lines.append(f"    • Kí hiệu:    {t['notation']}")
            lines.append(f"    • Định nghĩa: {t['definition']}")
            lines.append(f"    • Nguồn:      {src_str}")
            if t.get("lesson"):
                lines.append(f"    • Bài học:    {t.get('chapter', '')} — {t['lesson']}")
            if t.get("notes"):
                lines.append(f"    • Ghi chú:    {t['notes']}")
            lines.append("-" * 70)
        output_content = "\n".join(lines) + "\n"

    elif a.format == "dict":
        output_content = render_dict(resolve_target(a.target)[0], rows, a)

    elif a.format == "md":
        lines = []
        if a.audit:
            lines.append(f"# Mẫu kiểm định độc lập — Bộ `{a.target}`\n")
            lines.append(f"> Tổng cộng: **{len(rows)} mục** (gồm {len(sample_rand)} mục ngẫu nhiên và {len(sample_formula)} mục công thức / kí hiệu).\n")
            lines.append("> Hướng dẫn: Đọc ảnh trang PDF trong `sources` để đối chiếu `definition` và `notation`. Tỉ lệ lỗi cho phép: ≤ 5%.\n\n---\n")

        for i, t in enumerate(rows, 1):
            src_str = "; ".join(
                f"`{s['file']}` trang PDF {s['pdf_page']}" + (f" (trang in: {s['printed_page']})" if s.get("printed_page") else "")
                for s in t.get("sources", [])
            )
            lines.append(f"### {i}. {t['term']} (`{t['id']}`)\n")
            if t.get("notation"):
                lines.append(f"- **Kí hiệu:** {t['notation']}")
            lines.append(f"- **Định nghĩa:** {t['definition']}")
            lines.append(f"- **Nguồn:** {src_str}")
            if t.get("lesson"):
                lines.append(f"- **Bài học:** {t.get('chapter', '')} — {t['lesson']}")
            if t.get("notes"):
                lines.append(f"- **Ghi chú:** {t['notes']}")
            lines.append("\n---\n")
        output_content = "\n".join(lines)

    else:
        if a.fields == "all":
            out = rows
        else:
            fields = [f.strip() for f in a.fields.split(",")] if a.fields else DEFAULT_FIELDS
            out = [{f: t.get(f) for f in fields} for t in rows]
        output_content = json.dumps(out, ensure_ascii=False, indent=1) + "\n"

    if a.out:
        out_file = Path(a.out)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(output_content, encoding="utf-8")
        print(f"Đã xuất {len(rows)} mục vào: {out_file}")
        if a.format in ("md", "dict"):
            print("Mở file và nhấn Ctrl + Shift + V trong VS Code để xem trực quan.")
    else:
        print(output_content, end="")


def filter_terms(units, a):
    rows = []
    for unit in units:
        for t in load_unit(unit)["terms"]:
            if a.lesson and not contains(t["lesson"], a.lesson):
                continue
            if a.chapter and not contains(t["chapter"], a.chapter):
                continue
            if a.type and norm(t["type"]) != norm(a.type):
                continue
            if a.level and norm(t["level"]) != norm(a.level):
                continue
            if a.id and t["id"] not in a.id:
                continue
            if a.has_notes and not t.get("notes"):
                continue
            if a.q:
                hay = " ".join([t["term"], *t["aliases"], t["definition"], t.get("notation") or ""])
                if not contains(hay, a.q):
                    continue
            rows.append(t)
    return rows


def render_dict(unit, rows, a):
    data = load_unit(unit)
    lessons = []
    for e in data.get("lessons") or []:
        if a.chapter and not contains(e["chapter"], a.chapter):
            continue
        if a.lesson and not contains(e["lesson"] or e["chapter"], a.lesson):
            continue
        if a.level and norm(e["level"]) != norm(a.level):
            continue
        lessons.append(e)
    order = progress_order(unit)
    names = {}
    for u in units_of_subject(data["meta"]["subject"]):
        names.update({t["id"]: t["term"] for t in load_unit(u)["terms"]})
    scope = ", ".join(f"--{k} \"{v}\"" for k, v in (("chapter", a.chapter), ("lesson", a.lesson), ("level", a.level),
                                                    ("type", a.type), ("q", a.q)) if v)
    return dict_md.render(unit, data["meta"], rows, lessons, sorted(order, key=order.get), names, scope)


def query_lessons(a):
    rows = []
    for unit in resolve_target(a.target):
        for e in load_unit(unit).get("lessons") or []:
            if a.chapter and not contains(e["chapter"], a.chapter):
                continue
            if a.lesson and not contains(e["lesson"] or e["chapter"], a.lesson):
                continue
            if a.level and norm(e["level"]) != norm(a.level):
                continue
            if a.has_notes and not e.get("notes"):
                continue
            if a.q and not contains(" ".join([*e["objectives"], *e["key_terms"]]), a.q):
                continue
            rows.append({"unit": unit, **e})

    if a.count:
        print(len(rows))
        return

    def src_str(e, code="{}"):
        return "; ".join(
            f"{code.format(s['file'])} tr.{s['pdf_page']}" + (f" (in: {s['printed_page']})" if s.get("printed_page") else "")
            for s in e["sources"]
        )

    if a.format == "json":
        out = json.dumps(rows, ensure_ascii=False, indent=1) + "\n"
    else:
        lines = []
        for i, e in enumerate(rows, 1):
            title = f"{e['chapter']} — {e['lesson'] or '(cả chương)'} [{e['level']}]"
            if a.format == "md":
                lines.append(f"### {i}. {title}\n")
                lines.append(f"**{e['label']}**\n")
                lines += [f"- {o}" for o in e["objectives"]]
                if e["key_terms"]:
                    lines.append(f"\n**Thuật ngữ:** {', '.join(e['key_terms'])}")
                lines.append(f"\n**Nguồn:** {src_str(e, '`{}`')}")
                if e.get("notes"):
                    lines.append(f"\n**Ghi chú:** {e['notes']}")
                lines.append("\n---\n")
            else:
                lines.append(f"[{i}] {title}")
                lines.append(f"    {e['label']}:")
                lines += [f"      • {o}" for o in e["objectives"]]
                if e["key_terms"]:
                    lines.append(f"    Thuật ngữ: {', '.join(e['key_terms'])}")
                lines.append(f"    Nguồn: {src_str(e)}")
                if e.get("notes"):
                    lines.append(f"    Ghi chú: {e['notes']}")
                lines.append("-" * 70)
        out = "\n".join(lines) + "\n"

    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(out, encoding="utf-8")
        print(f"Đã xuất {len(rows)} mục vào: {a.out}")
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
