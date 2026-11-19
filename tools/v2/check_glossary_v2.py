"""Kiểm định định dạng, chất lượng giải nghĩa và 4 quy tắc chống trùng cho Từ điển Ver 2 (SPEC-GLOSSARY-V2).

    python textbook/glossary_v2/scripts/check_glossary_v2.py [--dir textbook/glossary_v2/markdown] [--strict-warnings]
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

FILE_TO_DISCIPLINE = {
    "Tu-dien-Toan-hoc.md": ("Toán học", "toan_hoc"),
    "Tu-dien-Vat-li.md": ("Vật lí", "vat_li"),
    "Tu-dien-Hoa-hoc.md": ("Hóa học", "hoa_hoc"),
    "Tu-dien-Sinh-hoc.md": ("Sinh học", "sinh_hoc"),
    "Tu-dien-Tin-hoc.md": ("Tin học", "tin_hoc"),
    "Tu-dien-Dia-li.md": ("Địa lí", "dia_li"),
    "Tu-dien-Lich-su.md": ("Lịch sử", "lich_su"),
    "Tu-dien-GD-KT-va-PL.md": ("Giáo dục Kinh tế và Pháp luật", "gd_kt_va_pl"),
    "Tu-dien-Ngu-van.md": ("Ngữ văn", "ngu_van"),
    "Tu-dien-Tieng-Anh.md": ("Tiếng Anh", "tieng_anh"),
}

VALID_DISCIPLINES = {v[0] for v in FILE_TO_DISCIPLINE.values()}

DISCIPLINE_KEYWORDS = {
    "Toán học": ("toán học", "toán ", "thống kê", "giải tích", "xác suất", "đại số", "hình học"),
    "Vật lí": ("vật lí", "vật lý", "cơ học", "điện từ", "quang học", "nhiệt học", "hạt nhân"),
    "Hóa học": ("hóa học", "hoá học", "SGK Hóa học", "SGK Hoá học", "phản ứng hóa học", "hoá lí", "hóa lí"),
    "Sinh học": ("sinh học", "di truyền", "tế bào", "thực vật", "động vật", "sinh thái", "tiến hoá", "tiến hóa", "vi sinh"),
    "Tin học": ("tin học", "máy tính", "lập trình", "cơ sở dữ liệu", "mạng máy tính", "thuật toán", "trí tuệ nhân tạo"),
    "Địa lí": ("địa lí", "địa lý", "khí hậu", "địa hình", "dân cư", "lãnh thổ", "kinh tế – xã hội"),
    "Lịch sử": ("lịch sử", "cách mạng", "chiến tranh", "văn minh", "triều đại"),
    "Giáo dục Kinh tế và Pháp luật": ("kinh tế và pháp luật", "kt&pl", "pháp luật", "hiến pháp", "thị trường", "ngân sách"),
    "Ngữ văn": ("ngữ văn", "văn học", "thơ", "truyện", "tiểu thuyết", "nghị luận", "tu từ"),
    "Tiếng Anh": ("tiếng anh", "global success"),
}

FORBIDDEN_VI_STARTERS = (
    "nhờ đó",
    "vì vậy",
    "do vậy",
    "do đó",
    "từ đó",
    "như vậy",
    "qua đó",
)

FORBIDDEN_EN_STARTERS = (
    "therefore,",
    "thus,",
    "hence,",
    "as a result,",
    "consequently,",
)

ALT_FIELD_RE = re.compile(r"^Giải thích khác \((.+)\)$")
ALT_VAL_RE = re.compile(r"^EN:\s*(.+?)\s*/\s*VI:\s*(.+)$")
PAGE_RE = re.compile(r"\btr\.\s*([0-9]+(?:\s*(?:,|–|-)\s*[0-9]+)*)\s*$")
REDUNDANT_BAI_RE = re.compile(r"Bài\s+(\d+)\s*:\s*Bài\s+\1\b", re.IGNORECASE)
HOMONYM_SUFFIX_RE = re.compile(
    r"\((?:mathematics|physics|chemistry|biology|molecular biology|ecology|statistics|botany|zoology|genetics|anatomy|"
    r"computer science|informatics|geography|history|economics|law|literature|linguistics|English)\)$",
    re.IGNORECASE,
)


def setup_utf8() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def norm(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip().lower()


def slugify_ascii(text: str) -> str:
    nfd = unicodedata.normalize("NFD", text.replace("đ", "d").replace("Đ", "D"))
    ascii_str = "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")
    ascii_str = ascii_str.lower()
    # Map common Greek letters
    greek_map = {
        "α": "alpha",
        "β": "beta",
        "γ": "gamma",
        "δ": "delta",
        "μ": "mu",
        "σ": "sigma",
        "ω": "omega",
    }
    for g, rep in greek_map.items():
        ascii_str = ascii_str.replace(g, rep)
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_str).strip("-")
    return slug or "term"


def split_vi_display(text: str) -> tuple[str, list[str]]:
    """'Điểm khởi đầu sao chép (Ori; điểm Ori)' -> ('Điểm khởi đầu sao chép', ['Ori', 'điểm Ori'])."""
    s = unicodedata.normalize("NFC", text).strip()
    m = re.fullmatch(r"(.+?)\s+\(([^()]+)\)", s)
    if not m:
        return s, []
    main = m.group(1).strip()
    aliases = [a.strip() for a in re.split(r"[;,]", m.group(2)) if a.strip()]
    return main, aliases


def balanced_math_dollars(text: str) -> bool:
    # Count unescaped $ signs outside codeticks
    cleaned = re.sub(r"`[^`]*`", "", text)
    cleaned = cleaned.replace(r"\$", "")
    # Ignore $$ display blocks first
    cleaned = cleaned.replace("$$", "")
    return cleaned.count("$") % 2 == 0


def infer_context_metadata(raw_ctx: str, origin_discipline: str) -> dict:
    low = norm(raw_ctx)
    disciplines = []
    for disc, kws in DISCIPLINE_KEYWORDS.items():
        if any(kw.lower() in low for kw in kws):
            disciplines.append(disc)
    if not disciplines:
        disciplines = [origin_discipline]
    grade = None
    m_grade = re.search(r"\blớp\s*(10|11|12)\b|\b(10|11|12)\s*,\s*Bài\b", raw_ctx, re.IGNORECASE)
    if m_grade:
        grade = int(m_grade.group(1) or m_grade.group(2))
    m_lesson = re.search(r"(Bài\s+\d+(?:\s*[–-]\s*\d+)?|Thuật ngữ dùng chung|Bảng giải thích thuật ngữ)", raw_ctx)
    lesson_ref = m_lesson.group(1) if m_lesson else None
    return {
        "raw": raw_ctx.strip(),
        "disciplines": disciplines,
        "grade": grade,
        "lesson_ref": lesson_ref,
    }


def parse_source_segment(seg: str) -> tuple[dict | None, str | None]:
    s = seg.strip()
    if not s:
        return None, "đoạn Nguồn rỗng"
    if "tr. chưa rõ" in norm(s):
        return None, f"không được để 'tr. chưa rõ': {s}"
    m_page = PAGE_RE.search(s)
    if not m_page:
        return None, f"Nguồn thiếu số trang hợp lệ ('..., tr. <số>'): {s}"
    page_spec = m_page.group(1)
    pages: list[int] = []
    for part in page_spec.split(","):
        part = part.strip()
        if "–" in part or "-" in part:
            bounds = re.split(r"[–-]", part)
            start_p, end_p = int(bounds[0].strip()), int(bounds[1].strip())
            if end_p < start_p:
                return None, f"dải trang không hợp lệ '{part}' trong: {s}"
            pages.extend(range(start_p, end_p + 1))
        else:
            pages.append(int(part))

    without_pages = s[: m_page.start()].rstrip(" ,")
    parts = [p.strip() for p in without_pages.split(",") if p.strip()]
    if not parts:
        return None, f"Nguồn thiếu tên sách: {s}"
    book = parts[0]

    unit = None
    m_sgk = re.match(
        r"^SGK\s+(Sinh học|Hóa học|Hoá học|Vật lí|Toán|Tin học(?:\s+CS|\s+ICT)?|Địa lí|Lịch sử|GD KT&PL|Ngữ văn|Tiếng Anh)\s+(10|11|12)\b",
        book,
        re.IGNORECASE,
    )
    if m_sgk:
        subj_map = {
            "sinh học": "sinh",
            "hóa học": "hoa",
            "hoá học": "hoa",
            "vật lí": "vat_ly",
            "toán": "toan",
            "tin học": "tin_hoc",
            "tin học cs": "tin_hoc_khmt",
            "tin học ict": "tin_hoc_thud",
            "địa lí": "dia",
            "lịch sử": "lich_su",
            "gd kt&pl": "gd_kt_va_pl",
            "ngữ văn": "ngu_van",
            "tiếng anh": "tieng_anh",
        }
        unit = f"{subj_map[norm(m_sgk.group(1))]}_{m_sgk.group(2)}"

    group = None
    lesson = None
    section = None
    for p in parts[1:]:
        if re.match(r"^(Phần|Chương|Chủ đề|Unit|Tập)\b", p, re.IGNORECASE):
            group = p if group is None else f"{group}, {p}"
        elif re.match(r"^(B\d+|Bài\s+\d+|Bảng\s+|Giải thích\s+|Sơ đồ\s+)", p, re.IGNORECASE):
            m_sec_in_lesson = re.match(r"^(.+?)\s*\(Mục\s+([^)]+)\)$", p, re.IGNORECASE)
            if m_sec_in_lesson:
                lesson = m_sec_in_lesson.group(1).strip()
                section = m_sec_in_lesson.group(2).strip()
            else:
                lesson = p
        elif re.match(r"^Mục\s+", p, re.IGNORECASE):
            section = re.sub(r"^Mục\s+", "", p, flags=re.IGNORECASE).strip()

    return {
        "raw": s,
        "book": book,
        "unit": unit,
        "group": group,
        "lesson": lesson,
        "section": section,
        "printed_pages": sorted(set(pages)),
    }, None


def parse_markdown_file(path: Path) -> tuple[list[dict], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    entries: list[dict] = []

    expected_disc_pair = FILE_TO_DISCIPLINE.get(path.name)
    expected_disc = expected_disc_pair[0] if expected_disc_pair else None

    raw_text = path.read_text(encoding="utf-8")
    if "\n---\n" not in raw_text:
        errors.append(f"[{path.name}] thiếu đường phân cách '---' sau phần mở đầu")
        body = raw_text
    else:
        _, body = raw_text.split("\n---\n", 1)

    # Strip trailing footer after final ---
    body_main = re.split(r"\n---\s*\n<!--", body, maxsplit=1)[0].strip()
    if not body_main:
        return [], [f"[{path.name}] không có mục từ nào"], []

    raw_blocks = re.split(r"(?m)^### ", body_main)
    if raw_blocks[0].strip():
        errors.append(f"[{path.name}] có nội dung lạ trước mục '### ' đầu tiên: {raw_blocks[0].strip()[:60]}")

    blocks = [b.strip() for b in raw_blocks[1:] if b.strip()]
    prev_key = None
    prev_term = None

    for block in blocks:
        lines = block.splitlines()
        term_en = unicodedata.normalize("NFC", lines[0].strip())
        if not term_en:
            errors.append(f"[{path.name}] tiêu đề '### ' trống")
            continue

        # Sort check
        cur_key = term_en.lower()
        if prev_key is not None and cur_key < prev_key:
            errors.append(f"[{path.name}] sai thứ tự A–Z: '{term_en}' đứng sau '{prev_term}'")
        prev_key = cur_key
        prev_term = term_en

        if " / " in term_en:
            warnings.append(f"[{path.name}] '{term_en}': tiêu đề chứa ' / ', nên chọn 1 khóa tiếng Anh chuẩn duy nhất")

        # Parse fields
        field_order: list[str] = []
        fields: dict[str, list[str]] = {}
        alt_explanations: list[dict] = []
        cur_field: str | None = None

        for line in lines[1:]:
            if not line.strip():
                continue
            m_top = re.match(r"^- \*\*(.+?):\*\*\s*(.*)$", line)
            if m_top:
                fname = unicodedata.normalize("NFC", m_top.group(1).strip())
                fval = unicodedata.normalize("NFC", m_top.group(2).strip())
                m_alt = ALT_FIELD_RE.match(fname)
                if m_alt:
                    field_order.append("Giải thích khác")
                    m_av = ALT_VAL_RE.match(fval)
                    if not m_av:
                        errors.append(
                            f"[{path.name}] '{term_en}': trường '{fname}' phải có dạng 'EN: ... / VI: ...'"
                        )
                    else:
                        alt_explanations.append(
                            {
                                "source_label": m_alt.group(1).strip(),
                                "explanation_en": m_av.group(1).strip(),
                                "explanation_vi": m_av.group(2).strip(),
                            }
                        )
                    cur_field = fname
                else:
                    field_order.append(fname)
                    fields.setdefault(fname, [])
                    if fval:
                        fields[fname].append(fval)
                    cur_field = fname
            elif line.startswith("  - ") and cur_field:
                sub_val = unicodedata.normalize("NFC", line[4:].strip())
                fields.setdefault(cur_field, []).append(f"SUB:{sub_val}")
            else:
                errors.append(f"[{path.name}] '{term_en}': dòng sai cú pháp trường: {line[:80]}")

        required_seq = ["Tiếng Việt", "Chuyên ngành gốc", "Giải thích (EN)", "Giải thích (VI)", "Bối cảnh", "Nguồn"]
        filtered_order = [f for f in field_order if f != "Giải thích khác"]
        if filtered_order != required_seq:
            errors.append(
                f"[{path.name}] '{term_en}': thứ tự/tập trường không chuẩn (nhận được {filtered_order}, cần {required_seq})"
            )
            continue

        term_vi_display = fields["Tiếng Việt"][0] if fields["Tiếng Việt"] else ""
        origin_disc = fields["Chuyên ngành gốc"][0] if fields["Chuyên ngành gốc"] else ""
        exp_en = fields["Giải thích (EN)"][0] if fields["Giải thích (EN)"] else ""
        exp_vi = fields["Giải thích (VI)"][0] if fields["Giải thích (VI)"] else ""
        ctx_items = fields["Bối cảnh"]
        src_items = fields["Nguồn"]

        if not term_vi_display:
            errors.append(f"[{path.name}] '{term_en}': thiếu giá trị 'Tiếng Việt'")
        if origin_disc not in VALID_DISCIPLINES:
            errors.append(f"[{path.name}] '{term_en}': 'Chuyên ngành gốc' không hợp lệ: {origin_disc!r}")
        elif expected_disc and origin_disc != expected_disc:
            errors.append(
                f"[{path.name}] '{term_en}': 'Chuyên ngành gốc' = {origin_disc!r} không khớp file {path.name} ({expected_disc!r})"
            )

        # Validate explanations
        if not exp_en or not exp_vi:
            errors.append(f"[{path.name}] '{term_en}': thiếu Giải thích (EN) hoặc Giải thích (VI)")
        else:
            low_vi = norm(exp_vi)
            low_en = norm(exp_en)
            if any(low_vi.startswith(st) for st in FORBIDDEN_VI_STARTERS):
                errors.append(f"[{path.name}] '{term_en}': Giải thích (VI) mở đầu bằng từ nối dẫn chuyện SGK: {exp_vi[:60]}")
            if any(low_en.startswith(st) for st in FORBIDDEN_EN_STARTERS):
                errors.append(f"[{path.name}] '{term_en}': Giải thích (EN) mở đầu bằng từ nối dẫn chuyện: {exp_en[:60]}")
            if "được gọi là" in low_vi:
                warnings.append(f"[{path.name}] '{term_en}': Giải thích (VI) còn cụm 'được gọi là' (nên viết trực diện kiểu từ điển)")
            if not balanced_math_dollars(exp_en):
                errors.append(f"[{path.name}] '{term_en}': Giải thích (EN) lẻ dấu '$'")
            if not balanced_math_dollars(exp_vi):
                errors.append(f"[{path.name}] '{term_en}': Giải thích (VI) lẻ dấu '$'")

        # Validate contexts
        contexts: list[dict] = []
        disambig_notes: list[str] = []
        for raw_c in ctx_items:
            c_clean = raw_c[4:].strip() if raw_c.startswith("SUB:") else raw_c.strip()
            if not c_clean:
                continue
            if REDUNDANT_BAI_RE.search(c_clean):
                errors.append(f"[{path.name}] '{term_en}': Bối cảnh lặp thừa số bài: {c_clean}")
            if c_clean.startswith("*Lưu ý:*") or c_clean.startswith("Lưu ý:"):
                disambig_notes.append(re.sub(r"^\*?Lưu ý:\*?\s*", "", c_clean).strip())
            else:
                contexts.append(infer_context_metadata(c_clean, origin_disc))
        if not contexts:
            errors.append(f"[{path.name}] '{term_en}': thiếu nội dung Bối cảnh sử dụng")

        # Validate sources
        if not src_items:
            errors.append(f"[{path.name}] '{term_en}': thiếu trường Nguồn")
            continue
        raw_src_joined = "; ".join(s[4:].strip() if s.startswith("SUB:") else s.strip() for s in src_items if s.strip())
        sources: list[dict] = []
        for seg in raw_src_joined.split(";"):
            parsed_src, err = parse_source_segment(seg)
            if err:
                errors.append(f"[{path.name}] '{term_en}': {err}")
            elif parsed_src:
                sources.append(parsed_src)
        if not sources:
            errors.append(f"[{path.name}] '{term_en}': không đọc được Nguồn hợp lệ")

        term_vi_main, aliases_vi = split_vi_display(term_vi_display)
        disc_slug = FILE_TO_DISCIPLINE.get(path.name, ("misc", "misc"))[1]
        entry_id = f"{disc_slug.replace('_', '-')}-{slugify_ascii(term_en)}"

        entries.append(
            {
                "id": entry_id,
                "term_en": term_en,
                "term_vi": term_vi_main,
                "term_vi_display": term_vi_display,
                "aliases_vi": aliases_vi,
                "origin_discipline": origin_disc,
                "explanation_en": exp_en,
                "explanation_vi": exp_vi,
                "alt_explanations": alt_explanations,
                "contexts": contexts,
                "disambiguation_notes": disambig_notes,
                "sources": sources,
                "markdown_file": path.name,
            }
        )

    return entries, errors, warnings


def parse_conflicts_md(path: Path) -> list[dict]:
    if not path.exists():
        return []
    conflicts: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|") or re.match(r"^\|\s*(Thuật ngữ|---)", s):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 5:
            conflicts.append(
                {
                    "term_en": cells[0],
                    "term_vi": cells[1],
                    "kind": cells[2],
                    "detail": cells[3],
                    "status": "resolved" if "đóng" in norm(cells[4]) or "resolved" in norm(cells[4]) else "open",
                }
            )
    return conflicts


def parse_review_md(path: Path) -> list[dict]:
    if not path.exists():
        return []
    items: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|") or re.match(r"^\|\s*(Thuật ngữ|---)", s):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 5:
            items.append(
                {
                    "term_vi": cells[0],
                    "term_en": cells[1] or None,
                    "unit": cells[2],
                    "context": cells[3],
                    "reason": cells[4],
                }
            )
    return items


def validate_directory(md_dir: Path) -> tuple[list[dict], list[dict], list[dict], list[str], list[str]]:
    all_entries: list[dict] = []
    all_errors: list[str] = []
    all_warnings: list[str] = []

    md_files = sorted(md_dir.glob("Tu-dien-*.md"))
    if not md_files:
        return [], [], [], [f"Không tìm thấy file Tu-dien-*.md nào trong {md_dir}"], []

    for path in md_files:
        entries, errs, warns = parse_markdown_file(path)
        all_entries.extend(entries)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    conflicts = parse_conflicts_md(md_dir / "Danh-sach-xung-dot.md")
    conflict_vi_set = {norm(c["term_vi"]) for c in conflicts}
    conflict_en_set = {norm(c["term_en"]) for c in conflicts}
    review_items = parse_review_md(md_dir / "Danh-sach-xem-xet.md")

    # Cross-file 4-rule deduplication checks
    seen_en: dict[str, dict] = {}
    seen_vi: dict[str, list[dict]] = {}
    seen_ids: set[str] = set()

    for e in all_entries:
        # Ensure unique id
        base_id = e["id"]
        idx = 2
        while e["id"] in seen_ids:
            e["id"] = f"{base_id}-{idx}"
            idx += 1
        seen_ids.add(e["id"])

        k_en = norm(e["term_en"])
        if k_en in seen_en:
            prev = seen_en[k_en]
            all_errors.append(
                f"[Trùng khóa EN - Quy tắc 1] '{e['term_en']}' ({e['markdown_file']}) trùng với '{prev['term_en']}' ({prev['markdown_file']})"
            )
        else:
            seen_en[k_en] = e

        if e["origin_discipline"] != "Tiếng Anh":
            k_vi = norm(e["term_vi"])
            seen_vi.setdefault(k_vi, []).append(e)

    for k_vi, group in seen_vi.items():
        if len(group) > 1:
            # Allow if any entry carries an explicit domain disambiguation suffix or is logged in Danh-sach-xung-dot.md
            has_disambig_suffix = any(HOMONYM_SUFFIX_RE.search(x["term_en"]) for x in group)
            logged = k_vi in conflict_vi_set or any(norm(x["term_en"]) in conflict_en_set for x in group)
            desc = ", ".join(f"'{x['term_en']}' ({x['markdown_file']})" for x in group)
            if not (has_disambig_suffix or logged):
                all_errors.append(
                    f"[Trùng Tiếng Việt khác khóa EN - Quy tắc 2/4] '{group[0]['term_vi']}' xuất hiện ở nhiều mục chưa gộp/khai báo xung đột: {desc}"
                )

    return all_entries, conflicts, review_items, all_errors, all_warnings


def main() -> None:
    setup_utf8()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dir", default="glossary/v2/markdown", help="Thư mục chứa Tu-dien-*.md")
    ap.add_argument("--strict-warnings", action="store_true", help="Coi cảnh báo là lỗi")
    args = ap.parse_args()

    md_dir = Path(args.dir)
    entries, conflicts, review_items, errors, warnings = validate_directory(md_dir)

    ok = not errors and (not warnings if args.strict_warnings else True)
    status = "ĐẠT" if ok else "KHÔNG ĐẠT"
    print(
        f"Kiểm định Glossary V2 [{md_dir}]: {status} — "
        f"{len(entries)} mục từ, {len(conflicts)} xung đột ghi nhận, {len(review_items)} mục xem xét, "
        f"{len(errors)} lỗi, {len(warnings)} cảnh báo"
    )
    for err in errors[:50]:
        print(f"  [LỖI] {err}")
    if len(errors) > 50:
        print(f"  ... và {len(errors) - 50} lỗi khác")
    for warn in warnings[:30]:
        print(f"  [CẢNH BÁO] {warn}")
    if len(warnings) > 30:
        print(f"  ... và {len(warnings) - 30} cảnh báo khác")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
