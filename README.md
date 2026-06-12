# Future Builder — Kelas Python untuk Tazkia & Ardy

Kelas Python pengantar yang **hands-on** dan **berbasis proyek**, dirancang untuk
Tazkia (calon mahasiswa CS UI) dan Ardy (calon SMA kelas atas). Tujuannya: dari hari
pertama langsung ngoding hal nyata, sambil membangun fondasi menuju sertifikasi
**PCEP – Certified Entry-Level Python Programmer** (OpenEDG Python Institute).

## Prinsip kelas
- **Why through how** — paham dunia kerja CS lewat membangun program nyata, bukan hafal teori.
- **Level pemula, untuk berdua** — jadi landasan bersama; pendalaman menyusul.
- **Bilingual** — penjelasan Bahasa Indonesia, istilah teknis diperkenalkan dalam Bahasa Inggris.
- **Target nyata** — silabus mengikuti PCEP, jadi tiap proyek diam-diam menutup satu bagian ujian.

## Format
- **Durasi:** 75 menit per sesi, mingguan.
- **Tools:** [Google Colab](https://colab.research.google.com) (di browser, tanpa install).
- **Komposisi sesi:** pemanasan → konsep + live coding → latihan terbimbing → tantangan → wrap-up.

## Peta silabus (berbasis PCEP)
| Sesi | Topik | Bagian PCEP |
|------|-------|-------------|
| 1 | Halo Python: program pertamamu (`print`, `input`, variabel, tipe data) | 1–2 |
| 2 | Operator & angka: bikin kalkulator | 2 |
| 3 | Pengambilan keputusan: `if` / `elif` / `else` | 3 |
| 4 | Perulangan: `for` & `while` | 3 |
| 5 | Koleksi data: `list` & `tuple` | 4 |
| 6 | `dictionary` & mini-proyek data | 4 |
| 7 | Fungsi (`def`) — merapikan kode | 4 |
| 8 | Error & exceptions + simulasi ujian PCEP | 5 |

> 8 sesi inti. Bisa ditambah sesi review/proyek akhir sebelum ujian asli.

## Materi
- [Sesi 1 — Halo Python: program pertamamu](sesi/sesi-01-halo-python.md)
- [Sesi 2 — Operator & angka: bikin kalkulator](sesi/sesi-02-operator-kalkulator.md)
- [Sesi 3 — Pengambilan keputusan: `if`/`elif`/`else`](sesi/sesi-03-if-else.md)
- [Sesi 4 — Perulangan: `for` & `while`](sesi/sesi-04-perulangan.md)
- [Sesi 5 — Koleksi data: `list` & `tuple`](sesi/sesi-05-list-tuple.md)
- [Sesi 6 — `dictionary` & mini-proyek data](sesi/sesi-06-dictionary.md)
- [Sesi 7 — Fungsi (`def`): merapikan kode](sesi/sesi-07-fungsi.md)
- [Sesi 8 — Error & exceptions + simulasi ujian PCEP](sesi/sesi-08-errors-ujian.md)

## Notebook Colab (siap-pakai)
Versi `.ipynb` tiap sesi ada di [`sesi/notebooks/`](sesi/notebooks/). Cara pakai:
1. Buka [Google Colab](https://colab.research.google.com) → **File → Upload notebook** → pilih file `.ipynb` sesi terkait.
2. Jalankan tiap sel kode dengan **Shift + Enter**.
3. Sel kosong bertanda `# ✍️ tulis kodemu di sini` adalah tempat berlatih. Kunci jawaban tersembunyi di bagian bawah notebook (klik untuk membuka).

> Notebook di-generate dari file materi markdown lewat `tools/generate_notebooks.py`
> (jalankan ulang script ini jika materi diperbarui).
