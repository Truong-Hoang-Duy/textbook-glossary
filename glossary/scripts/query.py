#!/usr/bin/env python3
"""Lọc thuật ngữ mà không cần nạp cả file vào ngữ cảnh.

    python glossary/scripts/query.py <unit|mon> [--lesson TEXT] [--chapter TEXT] [--type TYPE]
        [--level LEVEL] [--q TEXT] [--id ID ...] [--has-notes] [--fields a,b,c|all]
        [--sample N [--seed S]] [--count]

<unit> (vd toan_10): chỉ tìm trong bộ đó. <mon> (vd toan): mọi bộ có meta.subject trùng.
Lọc là tìm chuỗi con, không phân biệt hoa thường. --q tìm trong term, aliases, definition, notation.
Mặc định in các trường: id, term, definition, notation, sources.
"""
import argparse
import json
import random
import sys
import unicodedata
from pathlib import Path

from _common import load_unit, resolve_target, setup_stdout, unit_dir

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
    ap.add_argument("--format", choices=["json", "text", "md"], default="json", help="định dạng xuất: json (mặc định), text (dễ đọc) hoặc md (markdown)")
    ap.add_argument("--audit", action="store_true", help="chế độ kiểm tra mẫu Giai đoạn 4: lấy 30 mục chuẩn (20 ngẫu nhiên + 10 công thức) xuất ra sample_audit.md")
    ap.add_argument("--out", help="đường dẫn file xuất (UTF-8)")
    a = ap.parse_args()

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
        rows = []
        for unit in resolve_target(a.target):
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
        if a.format == "md":
            print("Mở file và nhấn Ctrl + Shift + V trong VS Code để xem trực quan.")
    else:
        print(output_content, end="")


if __name__ == "__main__":
    main()
