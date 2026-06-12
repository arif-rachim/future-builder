"""Build self-contained HTML pages from the course markdown files.

Output goes to html/ and can be opened directly in a browser (offline, no internet
needed) — designed to be easy to present/explain on screen.

Requires: pip install markdown pygments
"""
import re
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent.parent
SESI = ROOT / "sesi"
OUT = ROOT / "html"
OUT.mkdir(exist_ok=True)

# Ordered table of contents: (source markdown path, output html name, nav title)
PAGES = [
    (SESI / "sesi-01-halo-python.md",        "sesi-01.html", "Sesi 1 — Halo Python"),
    (SESI / "sesi-02-operator-kalkulator.md", "sesi-02.html", "Sesi 2 — Operator & Kalkulator"),
    (SESI / "sesi-03-if-else.md",            "sesi-03.html", "Sesi 3 — Percabangan"),
    (SESI / "sesi-04-perulangan.md",         "sesi-04.html", "Sesi 4 — Perulangan"),
    (SESI / "sesi-05-list-tuple.md",         "sesi-05.html", "Sesi 5 — List & Tuple"),
    (SESI / "sesi-06-dictionary.md",         "sesi-06.html", "Sesi 6 — Dictionary"),
    (SESI / "sesi-07-fungsi.md",             "sesi-07.html", "Sesi 7 — Fungsi"),
    (SESI / "sesi-08-errors-ujian.md",       "sesi-08.html", "Sesi 8 — Error & Ujian"),
    (SESI / "bank-soal-pcep.md",             "bank-soal.html", "Bank Soal PCEP"),
    (ROOT / "progress-checklist.md",         "checklist.html", "Checklist Progres"),
]

PYGMENTS_CSS = HtmlFormatter(style="friendly").get_style_defs(".codehilite")

PAGE_CSS = """
:root { --accent:#2563eb; --bg:#f7f8fb; --card:#fff; --text:#1f2430; --muted:#5b6472; }
* { box-sizing:border-box; }
body { margin:0; font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
  font-size:18px; line-height:1.7; color:var(--text); background:var(--bg); }
.topnav { position:sticky; top:0; z-index:10; background:#0f172a; color:#fff;
  display:flex; gap:.5rem; align-items:center; padding:.6rem 1rem; flex-wrap:wrap; }
.topnav a { color:#cbd5e1; text-decoration:none; font-size:.9rem; padding:.3rem .6rem;
  border-radius:6px; }
.topnav a:hover { background:#1e293b; color:#fff; }
.topnav .home { font-weight:700; color:#fff; }
.topnav .spacer { flex:1; }
.wrap { max-width:860px; margin:0 auto; padding:2rem 1.2rem 5rem; }
.card { background:var(--card); border:1px solid #e6e8ee; border-radius:14px;
  padding:1.6rem 1.8rem; box-shadow:0 1px 3px rgba(16,24,40,.04); }
h1 { font-size:2rem; line-height:1.25; margin-top:0; }
h2 { font-size:1.45rem; margin-top:2.2rem; padding-top:1rem; border-top:1px solid #eceef3; }
h3 { font-size:1.15rem; color:#111827; }
a { color:var(--accent); }
blockquote { margin:1rem 0; padding:.6rem 1rem; background:#eef2ff; border-left:4px solid var(--accent);
  border-radius:0 8px 8px 0; color:#374151; }
code { font-family:"SF Mono",Menlo,Consolas,monospace; font-size:.92em;
  background:#eef1f6; padding:.12em .4em; border-radius:5px; }
pre { background:#1e293b; border-radius:10px; padding:1rem 1.1rem; overflow:auto; }
pre code { background:none; color:#e2e8f0; padding:0; font-size:.9rem; line-height:1.55; }
.codehilite { background:#1e293b; border-radius:10px; margin:1rem 0; }
.codehilite pre { margin:0; }
table { border-collapse:collapse; width:100%; margin:1rem 0; font-size:.95rem; }
th,td { border:1px solid #e3e6ee; padding:.5rem .7rem; text-align:left; }
th { background:#f1f5f9; }
details { background:#f8fafc; border:1px solid #e3e6ee; border-radius:10px;
  padding:.4rem 1rem; margin:1rem 0; }
summary { cursor:pointer; font-weight:600; padding:.4rem 0; }
input[type=checkbox] { transform:scale(1.25); margin-right:.5rem; }
ul li { margin:.2rem 0; }
.prevnext { display:flex; justify-content:space-between; margin-top:2.5rem; gap:1rem; }
.prevnext a { background:var(--accent); color:#fff; text-decoration:none; padding:.6rem 1rem;
  border-radius:8px; font-size:.9rem; }
.prevnext a.disabled { background:#cbd5e1; pointer-events:none; }
@media print { .topnav,.prevnext { display:none; } .card { box-shadow:none; border:none; } }
"""

HTML_TMPL = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Future Builder</title>
<style>{css}
{pygments}</style>
</head>
<body>
<nav class="topnav">
  <a class="home" href="index.html">🏠 Future Builder</a>
  <span class="spacer"></span>
  {navlinks}
</nav>
<div class="wrap">
  <article class="card">
{body}
  </article>
  <div class="prevnext">{prevnext}</div>
</div>
</body>
</html>
"""


def render_md(md_path):
    text = md_path.read_text(encoding="utf-8")
    # Let markdown process content inside <details> (md_in_html needs the attribute).
    text = text.replace("<details>", '<details markdown="1">')
    md = markdown.Markdown(extensions=["extra", "codehilite", "sane_lists", "nl2br"],
                           extension_configs={"codehilite": {"guess_lang": False}})
    # Render task-list checkboxes [ ] / [x] as real checkboxes.
    html = md.convert(text)
    html = re.sub(r"\[ \]", '<input type="checkbox" disabled>', html)
    html = re.sub(r"\[x\]", '<input type="checkbox" checked disabled>', html)
    return html


def navlinks(current_out):
    links = []
    for _, out, title in PAGES:
        short = title.split(" — ")[0]
        cls = ' style="color:#fff;background:#1e293b"' if out == current_out else ""
        links.append(f'<a href="{out}"{cls}>{short}</a>')
    return "\n  ".join(links)


def prevnext(i):
    parts = []
    if i > 0:
        parts.append(f'<a href="{PAGES[i-1][1]}">← {PAGES[i-1][2]}</a>')
    else:
        parts.append('<a class="disabled" href="#">←</a>')
    if i < len(PAGES) - 1:
        parts.append(f'<a href="{PAGES[i+1][1]}">{PAGES[i+1][2]} →</a>')
    else:
        parts.append('<a class="disabled" href="#">→</a>')
    return "".join(parts)


def build_index():
    items = "\n".join(
        f'<li><a href="{out}">{title}</a></li>' for _, out, title in PAGES
    )
    body = f"""<h1>🚀 Future Builder — Kelas Python (PCEP)</h1>
<p>Materi kelas Python untuk <strong>Tazkia</strong> &amp; <strong>Ardy</strong>.
Klik sesi untuk membukanya. Halaman ini bisa dibuka langsung di browser, cocok untuk
ditampilkan saat menjelaskan.</p>
<h2>Daftar Materi</h2>
<ol>
{items}
</ol>
<blockquote>💡 Versi notebook Colab (<code>.ipynb</code>) ada di folder
<code>sesi/notebooks/</code> untuk praktik langsung.</blockquote>
"""
    html = HTML_TMPL.format(title="Daftar Materi", css=PAGE_CSS, pygments=PYGMENTS_CSS,
                            navlinks=navlinks("index.html"), body=body,
                            prevnext=f'<span></span><a href="{PAGES[0][1]}">Mulai Sesi 1 →</a>')
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print("wrote html/index.html")


def main():
    for i, (src, out, title) in enumerate(PAGES):
        body = render_md(src)
        html = HTML_TMPL.format(title=title, css=PAGE_CSS, pygments=PYGMENTS_CSS,
                                navlinks=navlinks(out), body=body, prevnext=prevnext(i))
        (OUT / out).write_text(html, encoding="utf-8")
        print("wrote html/" + out)
    build_index()


if __name__ == "__main__":
    main()
