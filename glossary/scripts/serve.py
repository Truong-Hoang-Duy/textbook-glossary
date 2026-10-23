#!/usr/bin/env python3
"""Trang web cục bộ để xuất từ điển thuật ngữ (query.py --format dict) cho mọi bộ.

    python glossary/scripts/serve.py [--port 8765] [--no-browser]

Chỉ nghe trên 127.0.0.1 (dữ liệu trích sách có bản quyền, dùng nội bộ). Mỗi bộ có nút Xem / Tải .md,
lọc được theo chương và cấp độ; nút "Tải tất cả" trả về file zip gồm từ điển của mọi bộ.
Dữ liệu đọc lại mỗi lần bấm nên luôn khớp với file JSON hiện tại.
"""
import argparse
import datetime
import html
import io
import webbrowser
import zipfile
from argparse import Namespace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse

import dict_md
from _common import data_path, list_units, load_unit, progress_order, setup_stdout
from query import filter_terms, render_dict

LEVELS = {"": "Tất cả cấp độ", "co_ban": "Cơ bản", "chuyen_de": "Chuyên đề"}


def units():
    """Các bộ đã có file dữ liệu (bỏ thư mục bộ mới tạo, còn rỗng)."""
    return [u for u in list_units() if data_path(u).exists()]


def opts(chapter=None, level=None):
    return Namespace(chapter=chapter or None, lesson=None, level=level or None, type=None, q=None,
                     id=None, has_notes=False)


def export(unit, chapter=None, level=None):
    a = opts(chapter, level)
    return render_dict(unit, filter_terms([unit], a), a)


def filename(unit, chapter=None, level=None):
    return dict_md.filename(unit, chapter, None, level)


def unit_info(unit):
    data = load_unit(unit)
    present = {t["chapter"] for t in data["terms"]} | {e["chapter"] for e in data.get("lessons") or []}
    order = progress_order(unit)
    chapters = sorted(present, key=lambda c: order.get((c, None), len(order)))
    return data["meta"], chapters


def page():
    rows_by_grade = {}
    for unit in units():
        try:
            meta, chapters = unit_info(unit)
        except (OSError, ValueError, KeyError):
            continue
        rows_by_grade.setdefault(meta["grade"], []).append((unit, meta, chapters))

    e = html.escape
    sections = []
    for grade in sorted(rows_by_grade):
        trs = []
        for unit, meta, chapters in rows_by_grade[grade]:
            ch_opts = '<option value="">Tất cả chương</option>' + "".join(
                f'<option value="{e(c)}">{e(c)}</option>' for c in chapters)
            lv_opts = "".join(f'<option value="{k}">{v}</option>' for k, v in LEVELS.items())
            trs.append(
                f'<tr data-unit="{unit}" data-name="{e(meta["subject_name"].lower())} {unit}">'
                f'<td><b>{e(meta["subject_name"])}</b><br><code>{unit}</code></td>'
                f'<td class="num">{meta["term_count"]}</td><td class="num">{meta.get("lesson_count", 0)}</td>'
                f'<td>{meta["last_updated"]}</td>'
                f'<td><select class="ch">{ch_opts}</select> <select class="lv">{lv_opts}</select></td>'
                f'<td class="act"><button data-dl="0">Xem</button> <button data-dl="1" class="pri">Tải .md</button></td></tr>')
        sections.append(f'<h2>Khối {grade}</h2><table><thead><tr><th>Bộ</th><th>Thuật ngữ</th><th>Bài YCCĐ</th>'
                        f'<th>Cập nhật</th><th>Phạm vi</th><th></th></tr></thead><tbody>{"".join(trs)}</tbody></table>')

    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Xuất từ điển thuật ngữ</title>
<style>
:root {{ --bg:#fafaf9; --fg:#1c1917; --mute:#78716c; --line:#e7e5e4; --card:#fff; --acc:#2563eb; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#1c1917; --fg:#f5f5f4; --mute:#a8a29e; --line:#44403c; --card:#292524; --acc:#60a5fa; }} }}
body {{ margin:0; padding:24px 16px; background:var(--bg); color:var(--fg); font:15px/1.5 system-ui, sans-serif; }}
main {{ max-width:1100px; margin:auto; }}
header {{ display:flex; flex-wrap:wrap; gap:12px; align-items:center; justify-content:space-between; }}
h1 {{ font-size:22px; margin:0; }} h2 {{ font-size:17px; margin:28px 0 8px; }}
p.note {{ color:var(--mute); margin:6px 0 0; }}
input, select, button {{ font:inherit; padding:5px 8px; border:1px solid var(--line); border-radius:6px; background:var(--card); color:var(--fg); }}
select.ch {{ max-width:260px; }}
button {{ cursor:pointer; }} button.pri {{ background:var(--acc); border-color:var(--acc); color:#fff; }}
.wrap {{ overflow-x:auto; }}
table {{ width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); border-radius:8px; }}
th, td {{ padding:8px 10px; border-bottom:1px solid var(--line); text-align:left; vertical-align:middle; }}
th {{ font-size:13px; color:var(--mute); font-weight:600; }}
td.num {{ text-align:right; font-variant-numeric:tabular-nums; }} td.act {{ white-space:nowrap; }}
code {{ color:var(--mute); font-size:12px; }}
</style></head><body><main>
<header><div><h1>Xuất từ điển thuật ngữ</h1>
<p class="note">Định dạng giống <code>query.py --format dict</code>. Dữ liệu sách KNTT, chỉ dùng nội bộ.</p></div>
<div><input id="q" placeholder="Lọc môn…"> <a href="/export_all"><button class="pri">Tải tất cả (.zip)</button></a></div></header>
<div class="wrap">{"".join(sections)}</div>
</main><script>
document.getElementById("q").addEventListener("input", ev => {{
  const q = ev.target.value.trim().toLowerCase();
  document.querySelectorAll("tr[data-unit]").forEach(tr => tr.hidden = q && !tr.dataset.name.includes(q));
}});
document.addEventListener("click", ev => {{
  const b = ev.target.closest("button[data-dl]"); if (!b) return;
  const tr = b.closest("tr");
  const p = new URLSearchParams({{unit: tr.dataset.unit, chapter: tr.querySelector(".ch").value,
                                  level: tr.querySelector(".lv").value, download: b.dataset.dl}});
  if (b.dataset.dl === "1") location.href = "/export?" + p; else window.open("/export?" + p, "_blank");
}});
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def send(self, body, ctype, name=None, status=200):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        if name:
            self.send_header("Content-Disposition", f"attachment; filename=\"{name}\"; filename*=UTF-8''{quote(name)}")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        try:
            if url.path == "/":
                self.send(page(), "text/html; charset=utf-8")
            elif url.path == "/export":
                unit = q.get("unit", "")
                if unit not in units():
                    return self.send(f"Không có bộ '{unit}'", "text/plain; charset=utf-8", status=404)
                chapter, level = q.get("chapter") or None, q.get("level") or None
                name = filename(unit, chapter, level) if q.get("download") == "1" else None
                self.send(export(unit, chapter, level), "text/plain; charset=utf-8" if not name else "text/markdown; charset=utf-8", name)
            elif url.path == "/export_all":
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                    for unit in units():
                        z.writestr(filename(unit), export(unit))
                self.send(buf.getvalue(), "application/zip", f"tu_dien_tat_ca_{datetime.date.today().isoformat()}.zip")
            else:
                self.send("Không tìm thấy", "text/plain; charset=utf-8", status=404)
        except Exception as ex:  # báo lỗi ra trình duyệt thay vì đóng kết nối
            self.send(f"LỖI: {ex!r}", "text/plain; charset=utf-8", status=500)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}")


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true", help="không tự mở trình duyệt")
    a = ap.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    url = f"http://127.0.0.1:{a.port}/"
    print(f"Đang chạy tại {url} (Ctrl+C để dừng)")
    if not a.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
