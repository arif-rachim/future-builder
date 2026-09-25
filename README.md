# Future Builder: a project-based Python class

Future Builder is a hands-on, project-based introductory Python course written in Bahasa Indonesia for two beginner learners: one preparing to study computer science at university and one about to start upper secondary school. The goal is for learners to write real programs from the first session while building towards the **PCEP – Certified Entry-Level Python Programmer** certification from the OpenEDG Python Institute, so each of the eight weekly 75-minute sessions quietly covers one part of the PCEP syllabus, from `print` and variables to functions and exceptions, ending with a mock exam. The material is written as Markdown lesson files and turned by two Python scripts into Google Colab notebooks (with practice cells and hidden answer keys) and into self-contained HTML pages for presenting on screen. The repository also contains a 45-question PCEP question bank and a progress checklist. The eight core sessions are complete; extra review or final-project sessions can be added before the real exam.

> Course material is in Bahasa Indonesia, with technical terms introduced in English.

## Principles

- **Why through how**: learners understand what computer science work is like by building real programs, not by memorising theory.
- **Beginner level, for two learners**: a shared foundation; deeper material comes later.
- **Bilingual**: explanations in Bahasa Indonesia, technical terms introduced in English.
- **A real target**: the syllabus follows PCEP, so every project covers a section of the exam.

## Format

- **Length:** 75 minutes per session, weekly.
- **Tools:** [Google Colab](https://colab.research.google.com) (in the browser, nothing to install).
- **Session structure:** warm-up → concept + live coding → guided practice → challenge → wrap-up.

## Syllabus map (based on PCEP)

| Session | Topic | PCEP section |
|------|-------|-------------|
| 1 | Hello Python: your first program (`print`, `input`, variables, data types) | 1–2 |
| 2 | Operators and numbers: build a calculator | 2 |
| 3 | Making decisions: `if` / `elif` / `else` | 3 |
| 4 | Loops: `for` and `while` | 3 |
| 5 | Data collections: `list` and `tuple` | 4 |
| 6 | `dictionary` and a mini data project | 4 |
| 7 | Functions (`def`): tidying up code | 4 |
| 8 | Errors and exceptions + a PCEP mock exam | 5 |

> Eight core sessions. Review or final-project sessions can be added before the real exam.

## Materials (Bahasa Indonesia)

- [Session 1 — Halo Python: program pertamamu](sesi/sesi-01-halo-python.md)
- [Session 2 — Operator & angka: bikin kalkulator](sesi/sesi-02-operator-kalkulator.md)
- [Session 3 — Pengambilan keputusan: `if`/`elif`/`else`](sesi/sesi-03-if-else.md)
- [Session 4 — Perulangan: `for` & `while`](sesi/sesi-04-perulangan.md)
- [Session 5 — Koleksi data: `list` & `tuple`](sesi/sesi-05-list-tuple.md)
- [Session 6 — `dictionary` & mini-proyek data](sesi/sesi-06-dictionary.md)
- [Session 7 — Fungsi (`def`): merapikan kode](sesi/sesi-07-fungsi.md)
- [Session 8 — Error & exceptions + simulasi ujian PCEP](sesi/sesi-08-errors-ujian.md)

## Colab notebooks (ready to use)

An `.ipynb` version of each session is in [`sesi/notebooks/`](sesi/notebooks/). To use one:

1. Open [Google Colab](https://colab.research.google.com) → **File → Upload notebook** → choose the session's `.ipynb` file.
2. Run each code cell with **Shift + Enter**.
3. Empty cells marked `# ✍️ tulis kodemu di sini` ("write your code here") are for practice. The answer key is hidden at the bottom of the notebook (click to open).

The notebooks are generated from the Markdown lessons by `tools/generate_notebooks.py`: text becomes Markdown cells, `python` code blocks become runnable cells, an empty cell is inserted after each exercise or challenge, and the answer key and teacher notes stay in one collapsed cell. Run the script again whenever the lessons change:

```bash
python3 tools/generate_notebooks.py
```

## HTML version (for presenting on screen)

A tidy HTML version that opens in any browser is in [`html/`](html/); start from [`html/index.html`](html/index.html). It has navigation between sessions, syntax highlighting and answer keys that open on click. Every page is self-contained and works without an internet connection.

Regenerate the HTML after changing the lessons:

```bash
pip install markdown pygments
python3 tools/build_html.py
```

## Practice and tracking

- [PCEP question bank](sesi/bank-soal-pcep.md): 45 drill questions in six parts (basics and data types, operators, conditionals, loops, collections, functions and errors) with answers and explanations.
- [Progress checklist](progress-checklist.md): tick off each skill once it has been mastered, to see when a learner is ready for the next session.

## Project structure

```text
sesi/                  Markdown lessons (source of truth) and the PCEP question bank
sesi/notebooks/        generated Colab notebooks, one per session
html/                  generated self-contained HTML pages
progress-checklist.md  per-session skills checklist
tools/                 generate_notebooks.py and build_html.py
```

## Tech stack

Python 3 · Markdown · Jupyter / Google Colab · Python-Markdown · Pygments
