# Sesi 8 — Error & Exceptions + Simulasi Ujian PCEP

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 5 (jenis error, `try`/`except`) + review semua bagian

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Mengenali jenis error umum (`SyntaxError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`).
2. Menangani error dengan `try` / `except`.
3. Mereview seluruh materi sesi 1–7.
4. Mengerjakan **simulasi soal PCEP** dan tahu langkah menuju ujian asli.

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR cek_password |
| 15 mnt | Konsep + live coding | Error & `try`/`except` |
| 20 mnt | Latihan terbimbing | Tangani error |
| 25 mnt | Simulasi ujian PCEP | Kerjakan soal pilihan ganda |
| 5 mnt | Penutup & peta lanjutan | Apa setelah PCEP |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR cek_password. Pemantik:
> "Program yang baik tidak langsung 'mati' ketika pengguna salah memasukkan data. Hari ini
> kita belajar membuat program **tahan banting** — dan menutup persiapan PCEP kalian."

---

## 2) Konsep + Live Coding (15 menit)

### a. Jenis error umum
```python
print(10 / 0)         # ZeroDivisionError -> bagi nol
int("halo")           # ValueError -> teks bukan angka
print(x)              # NameError -> variabel belum dibuat
"5" + 5               # TypeError -> campur string & int
print("halo)          # SyntaxError -> tanda kutip belum ditutup
```
> 🔑 PCEP banyak menanyakan **"error apa yang muncul"** dari potongan kode. Hafal ciri
> tiap error: `ValueError` (nilai salah), `TypeError` (tipe salah), `NameError` (nama tak
> dikenal), `ZeroDivisionError` (bagi nol), `SyntaxError` (penulisan salah).

### b. `try` / `except` — menangkap error
```python
try:
    angka = int(input("Masukkan angka: "))
    print("Kuadratnya:", angka ** 2)
except ValueError:
    print("Itu bukan angka yang valid!")
```
Kode di `try` dicoba; jika error, lompat ke `except` alih-alih program mati.

### c. `try` / `except` / `else` / `finally`
```python
try:
    hasil = 10 / int(input("Pembagi: "))
except ZeroDivisionError:
    print("Tidak bisa bagi nol")
except ValueError:
    print("Harus angka")
else:
    print("Hasil:", hasil)      # jalan jika TIDAK ada error
finally:
    print("Selesai.")           # SELALU jalan
```

---

## 3) Latihan Terbimbing (20 menit)

**Latihan 1.** Bungkus program pembagian dua angka dengan `try/except` agar pembagian nol & input non-angka tertangani rapi.

**Latihan 2.** Untuk tiap baris berikut, tebak **error apa** yang muncul (lalu cek di Colab):
```python
a) print(5 + "5")
b) print(int("3.5"))
c) print(nilai_tidak_ada)
d) print(10 % 0)
```

**Latihan 3.** Buat program yang terus meminta angka sampai pengguna memasukkan angka yang valid (pakai loop + try/except).

---

## 4) Simulasi Ujian PCEP (25 menit)
Kerjakan mandiri, lalu bahas bersama. (Kunci di bawah.)

**1.** Apa output dari `print(2 ** 3 ** 2)` ?
&nbsp;&nbsp;a) 64 &nbsp; b) 512 &nbsp; c) 12 &nbsp; d) Error

**2.** Apa hasil `print(7 // 2)` ?
&nbsp;&nbsp;a) 3.5 &nbsp; b) 3 &nbsp; c) 4 &nbsp; d) 1

**3.** Tipe data hasil `input()` selalu...
&nbsp;&nbsp;a) int &nbsp; b) float &nbsp; c) str &nbsp; d) bool

**4.** Apa output?
```python
x = [1, 2, 3, 4]
print(x[-2])
```
&nbsp;&nbsp;a) 2 &nbsp; b) 3 &nbsp; c) 4 &nbsp; d) Error

**5.** Error apa yang muncul: `int("abc")` ?
&nbsp;&nbsp;a) TypeError &nbsp; b) NameError &nbsp; c) ValueError &nbsp; d) SyntaxError

**6.** Apa output?
```python
for i in range(1, 4):
    print(i, end=" ")
```
&nbsp;&nbsp;a) 1 2 3 &nbsp; b) 1 2 3 4 &nbsp; c) 0 1 2 3 &nbsp; d) 1 2 3 4 5

**7.** Manakah yang membuat dictionary?
&nbsp;&nbsp;a) `[1,2,3]` &nbsp; b) `(1,2,3)` &nbsp; c) `{1,2,3}` &nbsp; d) `{"a":1}`

**8.** Apa output?
```python
def f(a, b=2):
    return a + b
print(f(3))
```
&nbsp;&nbsp;a) 3 &nbsp; b) 5 &nbsp; c) Error &nbsp; d) 2

---

## 5) Penutup & Peta Lanjutan (5 menit)

### Rangkuman seluruh kelas
Sesi 1–8 sudah menutup kelima bagian silabus **PCEP**:
fundamental → tipe data & operator → kondisi → loop → koleksi (list/tuple/dict) →
fungsi → error handling.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **exception** | error saat program berjalan |
| **try / except** | mencoba & menangkap error |
| **traceback** | jejak pesan error |
| **handle** | menangani error |
| **runtime** | saat program berjalan |

### 🎓 Langkah menuju ujian PCEP
1. Latihan soal resmi di **edube.org** (gratis) — kursus "Python Essentials 1".
2. Banyak latihan soal pilihan ganda (mengenali output & error).
3. Ujian PCEP daring di **OpenEDG** — tidak ada batas waktu kedaluwarsa.
4. Setelah PCEP → lanjut **PCAP** (intermediate) atau masuk ke materi teknis CS yang lebih dalam.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
try:
    a = float(input("Angka 1: "))
    b = float(input("Angka 2: "))
    print("Hasil:", a / b)
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")
except ValueError:
    print("Masukan harus berupa angka")
```
</details>

<details>
<summary>Latihan 2 (jenis error)</summary>

- a) `TypeError` — campur int dan str
- b) `ValueError` — `"3.5"` bukan integer (gunakan `float()` dulu)
- c) `NameError` — variabel belum didefinisikan
- d) `ZeroDivisionError` — modulo dengan nol
</details>

<details>
<summary>Latihan 3</summary>

```python
while True:
    try:
        angka = int(input("Masukkan angka: "))
        break
    except ValueError:
        print("Bukan angka, coba lagi.")
print("Terima kasih, kamu memasukkan:", angka)
```
</details>

<details>
<summary>Kunci Simulasi Ujian PCEP</summary>

1. **b) 512** — `**` dihitung dari kanan: `3 ** 2 = 9`, lalu `2 ** 9 = 512`
2. **b) 3** — floor division
3. **c) str** — `input()` selalu menghasilkan string
4. **b) 3** — indeks `-2` = elemen kedua dari belakang
5. **c) ValueError**
6. **a) 1 2 3** — `range(1,4)` → 1,2,3; `end=" "` agar sebaris
7. **d) `{"a":1}`** — yang lain: list, tuple, set
8. **b) 5** — `b` memakai default 2, `3 + 2`
</details>

---

## 🧭 Catatan pengajar
- Soal nomor 1 (`2 ** 3 ** 2`) hampir selalu menjebak — tekankan `**` bersifat **right-associative**.
- Biasakan murid **membaca traceback dari baris paling bawah** (di situ jenis & pesan error).
- **Beda level:** dorong Tazkia langsung mendaftar latihan resmi edube & menargetkan ujian PCEP; Ardy boleh mengulang sesi 1–4 dulu sampai mantap sebelum lanjut.
- **Setelah kelas ini:** inilah jembatan ke "pelajaran teknis CS mendetail" yang jadi tujuan awal — struktur data, algoritma, dan proyek nyata.
