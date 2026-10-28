"""Cổng 2b (spec mục 5.5, 7): kiểm tra độ phủ của từ điển Tầng 2.

    python textbook/scripts/check_coverage.py <unit> [--file Tu-dien-….md] [--template FILE] [--verbose]

Gom ứng viên thuật ngữ của nhóm (Chương/Chủ đề…) mà từ điển phủ:
  - cụm in đậm trong câu ở Tầng 1 (bỏ nhãn đoạn "**…:**" và tiêu đề cả dòng);
  - nhãn <!-- term: … --> ở Tầng 1;
  - cụm ngay sau "được gọi là" / "gọi là" / "còn được gọi là" ở Tầng 1;
  - tên thuật ngữ trong từ điển mẫu (mặc định _Huong-dan/Từ điển <Môn> <lớp>.md), ở các mục bài của nhóm.
Mỗi ứng viên phải trùng tên chính hoặc tên trong ngoặc của một dòng bảng, hoặc có một dòng
trong mục "## Đã xét, không tạo mục". Ứng viên chưa được xử lý là lỗi.

Bảng thuật ngữ cuối sách (nút back_matter có file Tầng 1, spec 5.7): mỗi mục in đậm phải có trong
một từ điển nào đó của bộ (bảng hoặc "Đã xét"). Khi bộ còn nhóm chưa có từ điển thì chỉ cảnh báo.
"""

import argparse
import re
import sys
from pathlib import Path

from _common import ROOT, display_title, iter_nodes, load_profile, load_progress, setup_stdout, unit_dir
from check_dict import BOLD_RE, TERM_RE, norm, parse_rows, split_term
from check_lesson import lesson_paths, split_frontmatter

REVIEWED = "Đã xét, không tạo mục"
REVIEW_RE = re.compile(r"^- (.+?) — (chỉ nhắc tên|không có trong SGK|tên khác của .+|gộp vào .+|chỉ có trong ví dụ, bài tập|tiêu đề, không phải thuật ngữ)(?:: .+)?$")
CALLED_RE = re.compile(r"(?:được gọi là|còn được gọi là|gọi là)\s+(?:các |những |một )?\(?\**([^,.;:()*\"]+?)\**\)?(?=[,.;:()\"]|\s+(?:nơi|có|ở|của|tách|cung|thường)\b|$)")


def sections_of(body):
    sections, cur = {}, None
    for line in body.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            sections[cur] = []
        elif cur:
            sections[cur].append(line)
    return sections


def candidates_from_lessons(lesson_files):
    found = {}

    def add(name, origin):
        name = re.sub(r"\s+", " ", name).strip(" -–")
        if 1 <= len(name.split()) <= 8:
            found.setdefault(norm(name), (name, origin))

    for lid, path in lesson_files:
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        skip = False
        for line in body.splitlines():
            s = line.strip()
            if s.startswith("## "):
                skip = s.startswith(("## 📷", "## ❓", "## ✏️"))  # danh sách hình, câu hỏi, bài tập
            if skip or s.startswith("#") or s.startswith("|"):
                continue
            for name in TERM_RE.findall(s):
                add(name, f"{lid} nhãn mô tả")
            if re.fullmatch(r"(?:\d+\.\s*)?\*\*[^*]+\*\*", s):
                continue  # tiêu đề cả dòng (kể cả mục đánh số in đậm)
            for b in BOLD_RE.findall(s):
                if not b.rstrip().endswith(":"):
                    add(b, f"{lid} in đậm")
            for m in CALLED_RE.finditer(re.sub(r"<!--.*?-->", "", s)):
                add(m.group(1), f"{lid} 'được gọi là'")
    return found


def candidates_from_template(template, lesson_labels):
    found = {}
    if not template or not template.exists():
        return found
    text = template.read_text(encoding="utf-8")
    cur = None
    for line in text.splitlines():
        if line.startswith("## "):
            m = re.match(r"## (Bài \d+)", line)
            cur = m.group(1) if m else line[3:].strip()
            continue
        if cur in lesson_labels and line.startswith("|"):
            for cells in parse_rows([line]):
                if len(cells) == 4 and cells[0] != "Thuật ngữ":
                    found.setdefault(norm(split_term(cells[0])[0]), (cells[0], f"từ điển mẫu, {cur}"))
    return found


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("--file")
    ap.add_argument("--template")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    progress = load_progress(a.unit)
    base = unit_dir(a.unit)
    tpl = load_profile(a.unit)["template"]
    template = Path(a.template) if a.template else (ROOT / tpl.format(grade=progress["grade"]) if tpl else ROOT / "-")
    paths = lesson_paths(a.unit, progress["toc"])
    bad = 0
    all_covered, dict_groups = {}, set()
    for dpath in ([base / a.file] if a.file else sorted(base.glob("Tu-dien-*.md"))):
        fm, body = split_frontmatter(dpath.read_text(encoding="utf-8"))
        group = next(n for n, _ in iter_nodes(progress["toc"]) if n["role"] == "group" and display_title(n) == fm["chuong"])
        lessons = [n for n in group["children"] if n["role"] == "lesson"]
        lesson_files = [(n["id"], paths[n["id"]][1]) for n in lessons if n["id"] in paths and paths[n["id"]][1].exists()]
        labels = {n["label"] for n in lessons if n.get("label")} | {"Thuật ngữ dùng chung"}

        sections = sections_of(body)
        covered, errors = {}, []
        for name, lines in sections.items():
            if name == REVIEWED:
                for l in lines:
                    s = l.strip()
                    if not s:
                        continue
                    m = REVIEW_RE.match(s)
                    if not m:
                        errors.append(f"dòng '{REVIEWED}' sai dạng '- <thuật ngữ> — <lý do>': {s[:80]}")
                        continue
                    for n in [m.group(1)] + split_term(m.group(1))[1] + [split_term(m.group(1))[0]]:
                        covered[norm(n)] = "đã xét"
                continue
            for cells in parse_rows([l for l in lines if l.startswith("|")][1:]):
                if len(cells) == 4:
                    term, aliases = split_term(cells[0])
                    for n in [term] + aliases:
                        covered[norm(n)] = "bảng"

        all_covered.update(covered)
        dict_groups.add(group["id"])
        cands = candidates_from_lessons(lesson_files)
        for k, v in candidates_from_template(template, labels).items():
            cands.setdefault(k, v)
        missing = sorted((v for k, v in cands.items() if k not in covered), key=lambda x: x[1])
        ok = not missing and not errors
        print(f"{dpath.name} {'ĐẠT' if ok else 'KHÔNG ĐẠT'} — {len(cands)} ứng viên, {len(missing)} chưa xử lý"
              + (f" (từ điển mẫu: {template.name})" if template.exists() else " (không có từ điển mẫu)"))
        for e in errors:
            print(f"  lỗi: {e}")
        for name, origin in missing:
            print(f"  chưa xử lý: {name}  [{origin}]")
        if a.verbose:
            for k, (name, origin) in sorted(cands.items()):
                print(f"    {covered.get(k, '—'):7} {name}  [{origin}]")
        bad += not ok

    glossaries = [(n["id"], paths[n["id"]][1]) for n, _ in iter_nodes(progress["toc"])
                  if n["role"] == "back_matter" and n["id"] in paths and paths[n["id"]][1].exists()]
    if glossaries and not a.file:
        groups = {n["id"] for n, _ in iter_nodes(progress["toc"])
                  if n["role"] == "group" and any(c["role"] == "lesson" for c in n["children"])}
        complete = groups <= dict_groups
        gl = candidates_from_lessons(glossaries)
        missing = sorted(v for k, v in gl.items() if k not in all_covered)
        tag = "lỗi" if complete else "cảnh báo"
        print(f"Bảng thuật ngữ cuối sách: {len(gl)} mục, {len(missing)} chưa có trong từ điển nào"
              + ("" if complete else f" (mới có từ điển cho {len(dict_groups)}/{len(groups)} nhóm, chỉ cảnh báo)"))
        for name, origin in missing:
            print(f"  {tag}: {name}  [{origin}]")
        bad += bool(missing and complete)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
