"""Hàm dùng chung cho các script glossary. Không chạy trực tiếp.

Bố cục (gốc dự án = thư mục chứa glossary/):
    <goc>/<unit>/*.pdf                     nguồn, chỉ đọc
    <goc>/glossary/<unit>/<unit>.json       dữ liệu
    <goc>/glossary/<unit>/progress.json     tiến độ + danh sách chương/bài chuẩn
    <goc>/glossary/<unit>/.ocr/             cache OCR (tự sinh)
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
GLOSSARY_DIR = SCRIPTS_DIR.parent
ROOT = GLOSSARY_DIR.parent
SCHEMA_PATH = GLOSSARY_DIR / "schema.json"
TESSDATA_DIR = GLOSSARY_DIR / "tessdata"
NON_UNIT_DIRS = {"scripts", "tessdata"}

UNIT_RE = re.compile(r"^([a-z]+(?:_[a-z]+)*)_([0-9]+)$")
SUBJECT_RE = re.compile(r"^[a-z]+(?:_[a-z]+)*$")

# Thứ tự ưu tiên khi xung đột định nghĩa: số nhỏ = ưu tiên cao.
BOOK_PRIORITY = {"sgk": 0, "scd": 1, "gv": 2, "sbt": 3}


def classify_book(filename):
    """(book_type, level) suy từ tên file; None nếu không nhận diện được.

    SGK -> sgk/co_ban; SBT -> sbt/co_ban; SCD -> scd/chuyen_de;
    SGV CD -> gv/chuyen_de; SGV -> gv/co_ban; Tài liệu bồi dưỡng GV, Slide tập huấn -> gv/co_ban.
    """
    name = unicodedata.normalize("NFC", filename).upper()
    words = name.split()
    if not words:
        return None
    head = words[0]
    if head == "SGV":
        return ("gv", "chuyen_de") if len(words) > 1 and words[1] == "CD" else ("gv", "co_ban")
    if name.startswith("TÀI LIỆU BỒI DƯỠNG GV") or name.startswith("SLIDE TẬP HUẤN"):
        return ("gv", "co_ban")
    return {"SGK": ("sgk", "co_ban"), "SBT": ("sbt", "co_ban"), "SCD": ("scd", "chuyen_de")}.get(head)


def setup_stdout():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def parse_unit(unit):
    """'vat_ly_10' -> ('vat_ly', 10). Trả về None nếu không đúng quy ước."""
    m = UNIT_RE.match(unit)
    if not m:
        return None
    return m.group(1), int(m.group(2))


def id_prefix(unit):
    """'toan_10' -> 'toan-10-'; 'vat_ly_10' -> 'vat-ly-10-'."""
    return unit.replace("_", "-") + "-"


def unit_dir(unit):
    return GLOSSARY_DIR / unit


def data_path(unit):
    return GLOSSARY_DIR / unit / f"{unit}.json"


def progress_path(unit):
    return GLOSSARY_DIR / unit / "progress.json"


def book_dir(unit):
    return ROOT / unit


def list_units():
    """Mọi thư mục con của glossary/ trông như một bộ (trừ scripts, tessdata)."""
    out = []
    for p in sorted(GLOSSARY_DIR.iterdir()):
        if p.is_dir() and p.name not in NON_UNIT_DIRS and not p.name.startswith("."):
            out.append(p.name)
    return out


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_schema():
    return load_json(SCHEMA_PATH)


def load_unit(unit):
    return load_json(data_path(unit))


def units_of_subject(subject):
    """Các bộ có meta.subject == subject (đọc meta, bỏ qua bộ hỏng)."""
    out = []
    for u in list_units():
        p = data_path(u)
        if not p.exists():
            continue
        try:
            if load_json(p).get("meta", {}).get("subject") == subject:
                out.append(u)
        except (OSError, ValueError):
            continue
    return out


def resolve_target(target):
    """Tên bộ -> [bộ]; tên môn -> mọi bộ của môn. Lỗi thì thoát."""
    if parse_unit(target):
        if not data_path(target).exists():
            sys.exit(f"LỖI: không thấy {data_path(target)}")
        return [target]
    if SUBJECT_RE.match(target):
        units = units_of_subject(target)
        if not units:
            sys.exit(f"LỖI: không có bộ nào thuộc môn '{target}'")
        return units
    sys.exit(f"LỖI: '{target}' không phải tên bộ ({{mon}}_{{lop}}) hay tên môn")


def subject_ids(subject, exclude_unit=None):
    """{id: unit} của mọi thuật ngữ trong môn (bỏ qua exclude_unit nếu có)."""
    ids = {}
    for u in units_of_subject(subject):
        if u == exclude_unit:
            continue
        for t in load_unit(u).get("terms", []):
            ids[t.get("id")] = u
    return ids


def progress_lessons(unit):
    """{chapter: set(lessons)} gộp từ mọi sách trong progress.json của bộ."""
    p = progress_path(unit)
    if not p.exists():
        return None
    prog = load_json(p)
    out = {}
    for book in prog.get("books", {}).values():
        for ch, chd in (book.get("chapters") or {}).items():
            out.setdefault(ch, set()).update((chd.get("lessons") or {}).keys())
    return out


def dumps_unit(data):
    """File dữ liệu bộ: meta thụt lề, mỗi thuật ngữ đúng một dòng (gọn, diff sạch)."""
    meta = json.dumps(data["meta"], ensure_ascii=False, indent=2).replace("\n", "\n  ")
    terms = ",\n".join("    " + json.dumps(t, ensure_ascii=False) for t in data["terms"])
    body = f"\n{terms}\n  " if terms else ""
    return f'{{\n  "meta": {meta},\n  "terms": [{body}]\n}}'


def write_json_atomic(path, data, backup=True):
    """Sao lưu .bak -> ghi file tạm cùng thư mục -> os.replace đè file chính.

    Dữ liệu bộ ({meta, terms}) ghi theo dumps_unit; file khác ghi thụt lề 2.
    """
    path = Path(path)
    if backup and path.exists():
        shutil.copy2(path, path.with_name(path.name + ".bak"))
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            if isinstance(data, dict) and set(data) == {"meta", "terms"}:
                f.write(dumps_unit(data))
            else:
                json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


# ---------- Chuẩn hóa văn bản để so khớp ----------

LATEX_INLINE_RE = re.compile(r"\$[^$]*\$")
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def strip_accents(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return unicodedata.normalize("NFC", s)


def tokens(text, keep_accents=True, drop_latex=True):
    """Chữ thường, NFC, bỏ LaTeX và dấu câu, tách từ; bỏ từ 1 ký tự (biến số, nhiễu OCR)."""
    if drop_latex:
        text = LATEX_INLINE_RE.sub(" ", text)
    text = unicodedata.normalize("NFC", text).lower()
    if not keep_accents:
        text = strip_accents(text)
    return [w for w in WORD_RE.findall(text) if len(w) > 1]


# ---------- Đọc text trang PDF (text layer hoặc OCR có cache) ----------

MIN_TEXT_CHARS = 30


def _pymupdf():
    try:
        import pymupdf  # noqa: F401
        return pymupdf
    except ImportError:
        try:
            import fitz as pymupdf  # bản cũ
            return pymupdf
        except ImportError:
            return None


def pdf_page_count(pdf_path):
    pm = _pymupdf()
    if pm is None:
        return None
    with pm.open(pdf_path) as doc:
        return doc.page_count


def find_tesseract():
    cand = [os.environ.get("TESSERACT_CMD"), shutil.which("tesseract"),
            r"C:\Program Files\Tesseract-OCR\tesseract.exe", "/usr/bin/tesseract"]
    for c in cand:
        if c and Path(c).exists():
            return c
    return None


class PageReader:
    """Lấy text một trang (1-based). Ưu tiên text layer; nếu trống thì OCR (vie) và cache."""

    def __init__(self, unit, allow_ocr=True):
        self.unit = unit
        self.pm = _pymupdf()
        self.tess = find_tesseract() if allow_ocr else None
        self.docs = {}
        self.cache_root = unit_dir(unit) / ".ocr"

    def _doc(self, file):
        if file not in self.docs:
            self.docs[file] = self.pm.open(book_dir(self.unit) / file)
        return self.docs[file]

    def page_count(self, file):
        return self._doc(file).page_count

    def text(self, file, page):
        """Trả về (text, cách_lấy) với cách_lấy ∈ text|ocr|ocr_cache; (None, lý_do) nếu không lấy được."""
        if self.pm is None:
            return None, "thiếu PyMuPDF"
        doc = self._doc(file)
        if page < 1 or page > doc.page_count:
            return None, "trang ngoài phạm vi"
        t = doc[page - 1].get_text()
        if len(t.strip()) >= MIN_TEXT_CHARS:
            return t, "text"
        cache = self.cache_root / Path(file).stem / f"p{page:04d}.txt"
        if cache.exists():
            t = cache.read_text(encoding="utf-8")
            if len(t.strip()) < MIN_TEXT_CHARS:
                return None, "OCR không ra chữ"
            return t, "ocr_cache"
        if not self.tess or not (TESSDATA_DIR / "vie.traineddata").exists():
            return None, "PDF dạng ảnh, không có OCR (tesseract + glossary/tessdata/vie.traineddata)"
        with tempfile.TemporaryDirectory() as td:
            img = Path(td) / "p.png"
            doc[page - 1].get_pixmap(dpi=300, colorspace=self.pm.csGRAY).save(img)
            r = subprocess.run([self.tess, str(img), "stdout", "-l", "vie", "--psm", "3",
                                "--tessdata-dir", str(TESSDATA_DIR)], capture_output=True)
        if r.returncode != 0:
            return None, "OCR lỗi: " + r.stderr.decode("utf-8", "replace").strip()[:200]
        t = r.stdout.decode("utf-8", "replace")
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(t, encoding="utf-8")
        if len(t.strip()) < MIN_TEXT_CHARS:
            return None, "OCR không ra chữ"
        return t, "ocr"


# ---------- Kiểm tra dữ liệu (dùng chung add_terms.py và validate.py) ----------

def schema_validator(schema, ref=None):
    try:
        import jsonschema
    except ImportError:
        sys.exit("LỖI: cần cài jsonschema (pip install jsonschema)")
    if ref:
        schema = dict(schema, **{"$ref": ref})
        for k in ("type", "required", "properties", "additionalProperties"):
            schema.pop(k, None)
    return jsonschema.Draft202012Validator(schema)


def schema_errors(validator, obj, label=""):
    out = []
    for e in sorted(validator.iter_errors(obj), key=lambda e: list(e.absolute_path)):
        loc = "/".join(str(p) for p in e.absolute_path)
        out.append(f"{label}{('/' + loc) if loc else ''}: {e.message}")
    return out


def term_errors(unit, terms, known_ids, lessons, page_counts):
    """Kiểm tra ngữ nghĩa (ngoài schema) cho danh sách thuật ngữ của một bộ.

    known_ids: tập id hợp lệ để related_terms trỏ tới (toàn môn).
    lessons: {chapter: set(lesson)} từ progress.json, hoặc None nếu không có.
    page_counts: {file: số trang hoặc None} — cache, hàm sẽ tự điền.
    """
    errs = []
    prefix = id_prefix(unit)
    for i, t in enumerate(terms):
        if not isinstance(t, dict):
            continue
        tid = t.get("id", f"#{i}")
        lab = f"[{tid}]"
        if isinstance(t.get("id"), str) and not t["id"].startswith(prefix):
            errs.append(f"{lab} id phải bắt đầu bằng '{prefix}'")
        if isinstance(t.get("definition"), str) and not t["definition"].strip():
            errs.append(f"{lab} definition rỗng")
        for r in t.get("related_terms") or []:
            if r not in known_ids:
                errs.append(f"{lab} related_terms trỏ tới id không tồn tại: {r}")
            if r == t.get("id"):
                errs.append(f"{lab} related_terms trỏ tới chính nó")
        ch, le = t.get("chapter"), t.get("lesson")
        if lessons is not None and isinstance(ch, str):
            if ch not in lessons:
                errs.append(f"{lab} chapter không có trong progress.json: {ch!r}")
            elif isinstance(le, str) and le not in lessons[ch]:
                errs.append(f"{lab} lesson không thuộc chương trong progress.json: {le!r}")
        for s in t.get("sources") or []:
            if not isinstance(s, dict) or not isinstance(s.get("file"), str):
                continue
            f = s["file"]
            if f not in page_counts:
                p = book_dir(unit) / f
                page_counts[f] = pdf_page_count(p) if p.exists() else -1
            n = page_counts[f]
            if n == -1:
                errs.append(f"{lab} sources.file không có trong {unit}/: {f}")
            elif n is not None and isinstance(s.get("pdf_page"), int) and s["pdf_page"] > n:
                errs.append(f"{lab} pdf_page {s['pdf_page']} vượt số trang ({n}) của {f}")
            cls = classify_book(f)
            if cls and s.get("book_type") != cls[0]:
                errs.append(f"{lab} book_type '{s.get('book_type')}' không khớp tên file {f} (phải là '{cls[0]}')")
        # level theo nguồn định nghĩa (nguồn đầu tiên trong sources).
        srcs = [s for s in t.get("sources") or [] if isinstance(s, dict) and isinstance(s.get("file"), str)]
        if srcs:
            cls = classify_book(srcs[0]["file"])
            if cls and t.get("level") != cls[1]:
                errs.append(f"{lab} level '{t.get('level')}' không khớp nguồn đầu {srcs[0]['file']} (phải là '{cls[1]}')")
    return errs
