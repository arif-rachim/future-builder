"""Generate Google Colab notebooks (.ipynb) from the session markdown files.

For each sesi/*.md:
- Text becomes markdown cells.
- ```python blocks (in the lesson body) become runnable code cells.
- After each "Latihan"/"Tantangan" section an empty code cell is inserted to type in.
- The "Kunci jawaban" + "Catatan pengajar" tail is kept as ONE markdown cell so the
  answer keys stay hidden inside their <details> blocks (Colab renders these).
"""
import json
import re
from pathlib import Path

SESI_DIR = Path(__file__).resolve().parent.parent / "sesi"
OUT_DIR = SESI_DIR / "notebooks"
OUT_DIR.mkdir(exist_ok=True)

ANSWER_HEADING = "## ✅ Kunci jawaban"

BANNER = (
    "> 📓 **Notebook latihan** — buka di [Google Colab](https://colab.research.google.com)\n"
    "> (File → Upload notebook), lalu jalankan tiap sel kode dengan **Shift + Enter**.\n"
    ">\n"
    "> Sel kode kosong bertanda `# ✍️ tulis kodemu di sini` adalah tempatmu berlatih.\n"
    "> Kunci jawaban ada di bagian paling bawah (klik untuk membuka)."
)


def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code_cell(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": text}


def empty_practice_cell():
    return code_cell("# ✍️ tulis kodemu di sini\n")


def split_body_into_cells(body):
    """Split markdown body into alternating markdown / python-code cells."""
    cells = []
    # Split keeping the fenced python blocks.
    parts = re.split(r"(```python\n.*?\n```)", body, flags=re.DOTALL)
    for part in parts:
        if not part.strip():
            continue
        m = re.match(r"```python\n(.*?)\n```$", part, flags=re.DOTALL)
        if m:
            cells.append(code_cell(m.group(1) + "\n"))
        else:
            cells.append(md_cell(part.strip("\n")))
            # Add an empty code cell after exercise / challenge sections.
            if re.search(r"##\s*\d\)\s*(Latihan|Tantangan)", part) or \
               re.search(r"\*\*Latihan \d", part):
                cells.append(empty_practice_cell())
    return cells


def build_notebook(md_path):
    raw = md_path.read_text(encoding="utf-8")

    if ANSWER_HEADING in raw:
        body, tail = raw.split(ANSWER_HEADING, 1)
        tail = ANSWER_HEADING + tail
    else:
        body, tail = raw, ""

    cells = [md_cell(BANNER)]
    cells += split_body_into_cells(body)
    if tail.strip():
        cells.append(md_cell(tail.strip("\n")))

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
            "colab": {"provenance": []},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main():
    md_files = sorted(SESI_DIR.glob("sesi-*.md"))
    for md in md_files:
        nb = build_notebook(md)
        out = OUT_DIR / (md.stem + ".ipynb")
        out.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
        print("wrote", out.relative_to(SESI_DIR.parent), "-", len(nb["cells"]), "cells")


if __name__ == "__main__":
    main()
