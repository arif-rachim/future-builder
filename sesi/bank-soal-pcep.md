# Bank Soal PCEP — Latihan Drill

> Kumpulan soal pilihan ganda bergaya **PCEP (Certified Entry-Level Python Programmer)**.
> Cocok untuk latihan menjelang ujian. Kerjakan tanpa melihat kunci dulu — kunci ada di bagian bawah.
> Total **45 soal**, dikelompokkan per topik. Jawablah dengan menebak **output** atau **jenis error**.

---

## Bagian A — Dasar, Variabel & Tipe Data (soal 1–10)

**1.** Apa output dari `print(type(10))` ?
a) `int` b) `<class 'int'>` c) `10` d) `number`

**2.** Hasil dari `print("5" + "3")` ?
a) `8` b) `53` c) `"53"` d) Error

**3.** `print(int("12") + 3)` menghasilkan...
a) `123` b) `15` c) `"15"` d) Error

**4.** Tipe data dari `input("Umur: ")` selalu...
a) `int` b) `float` c) `str` d) tergantung input

**5.** Manakah nama variabel yang **tidak valid**?
a) `_nama` b) `nama2` c) `2nama` d) `namaKu`

**6.** Output dari `print(3 * "ab")` ?
a) `ababab` b) `Error` c) `abab` d) `3ab`

**7.** `print(float("3.14"))` menghasilkan...
a) `3` b) `3.14` c) `"3.14"` d) Error

**8.** Berapa output `print(len("Python"))` ?
a) `5` b) `6` c) `7` d) Error

**9.** Apa hasil `print(10 == "10")` ?
a) `True` b) `False` c) `Error` d) `None`

**10.** Manakah komentar yang benar di Python?
a) `// komentar` b) `<!-- komentar -->` c) `# komentar` d) `/* komentar */`

---

## Bagian B — Operator (soal 11–18)

**11.** Output dari `print(2 ** 3 ** 2)` ?
a) `64` b) `512` c) `12` d) `256`

**12.** `print(17 // 5)` menghasilkan...
a) `3` b) `3.4` c) `4` d) `2`

**13.** `print(17 % 5)` menghasilkan...
a) `3` b) `2` c) `1` d) `0`

**14.** Output `print(2 + 3 * 4)` ?
a) `20` b) `14` c) `24` d) `9`

**15.** `print(10 / 2)` menghasilkan tipe...
a) `int` (`5`) b) `float` (`5.0`) c) `str` d) Error

**16.** Setelah `x = 5; x += 3`, nilai `x` adalah...
a) `5` b) `3` c) `8` d) `53`

**17.** Output `print(7 > 3 and 2 > 5)` ?
a) `True` b) `False` c) `Error` d) `None`

**18.** Output `print(not (5 == 5))` ?
a) `True` b) `False` c) `Error` d) `5`

---

## Bagian C — Percabangan (soal 19–25)

**19.** Apa output?
```python
x = 8
if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")
```
a) `A` b) `B` c) `C` d) tidak ada

**20.** Apa yang menyebabkan `IndentationError`?
a) lupa `:` b) salah indentasi blok c) typo nama d) bagi nol

**21.** Output?
```python
if 0:
    print("ya")
else:
    print("tidak")
```
a) `ya` b) `tidak` c) Error d) tidak ada output

**22.** `print("genap" if 4 % 2 == 0 else "ganjil")` menghasilkan...
a) `genap` b) `ganjil` c) Error d) `True`

**23.** Manakah yang bernilai `False` di kondisi `if`?
a) `1` b) `"halo"` c) `0` d) `[1,2]`

**24.** Output?
```python
a = 5
if a > 3 and a < 10:
    print("tengah")
```
a) `tengah` b) tidak ada c) Error d) `True`

**25.** Operator manakah untuk "tidak sama dengan"?
a) `=/=` b) `!=` c) `<>` d) `not=`

---

## Bagian D — Perulangan (soal 26–32)

**26.** Apa output?
```python
for i in range(3):
    print(i, end=" ")
```
a) `1 2 3` b) `0 1 2` c) `0 1 2 3` d) `1 2`

**27.** `range(2, 10, 3)` menghasilkan angka...
a) `2 5 8` b) `2 4 6 8` c) `2 5 8 11` d) `3 6 9`

**28.** Apa fungsi `break`?
a) lewati satu putaran b) keluar dari loop c) ulang dari awal d) hentikan program

**29.** Apa fungsi `continue`?
a) keluar loop b) lompat ke putaran berikutnya c) berhenti d) ulang fungsi

**30.** Berapa kali "hai" dicetak?
```python
i = 0
while i < 5:
    print("hai")
    i += 1
```
a) 4 b) 5 c) 6 d) tak terhingga

**31.** Apa output?
```python
total = 0
for n in [1, 2, 3, 4]:
    total += n
print(total)
```
a) `4` b) `10` c) `1234` d) `0`

**32.** Loop berikut menghasilkan...
```python
for i in range(5, 0, -1):
    print(i, end="")
```
a) `12345` b) `54321` c) `5432` d) `01234`

---

## Bagian E — List, Tuple & Dictionary (soal 33–40)

**33.** Apa output `print([1, 2, 3][1])` ?
a) `1` b) `2` c) `3` d) Error

**34.** Apa output?
```python
x = [10, 20, 30, 40]
print(x[-1])
```
a) `10` b) `40` c) `30` d) Error

**35.** Setelah `a = [1, 2]; a.append(3)`, isi `a` adalah...
a) `[1, 2]` b) `[1, 2, 3]` c) `[3, 1, 2]` d) Error

**36.** Apa output `print([1, 2, 3, 4][1:3])` ?
a) `[1, 2]` b) `[2, 3]` c) `[2, 3, 4]` d) `[1, 2, 3]`

**37.** Manakah yang **immutable** (tak bisa diubah)?
a) list b) dictionary c) tuple d) set

**38.** Apa output?
```python
d = {"a": 1, "b": 2}
print(d["b"])
```
a) `1` b) `2` c) `"b"` d) Error

**39.** Mengakses kunci yang tidak ada di dictionary menimbulkan...
a) `IndexError` b) `KeyError` c) `ValueError` d) `None`

**40.** `print(len({"x": 1, "y": 2, "z": 3}))` menghasilkan...
a) `1` b) `2` c) `3` d) `6`

---

## Bagian F — Fungsi & Error (soal 41–45)

**41.** Apa output?
```python
def f(a, b=10):
    return a + b
print(f(5))
```
a) `5` b) `15` c) `10` d) Error

**42.** Fungsi tanpa `return` mengembalikan...
a) `0` b) `""` c) `None` d) Error

**43.** Apa output?
```python
def kali(a, b):
    print(a * b)
hasil = kali(3, 4)
print(hasil)
```
a) `12` lalu `12` b) `12` lalu `None` c) `None` d) Error

**44.** Error apa: `print(int("abc"))` ?
a) `TypeError` b) `NameError` c) `ValueError` d) `SyntaxError`

**45.** Blok manakah yang **selalu** dijalankan pada `try/except`?
a) `try` b) `except` c) `else` d) `finally`

---

## ✅ Kunci Jawaban

<details>
<summary>Klik untuk melihat kunci & pembahasan singkat</summary>

| No | Jwb | No | Jwb | No | Jwb |
|----|-----|----|-----|----|-----|
| 1 | **b** `<class 'int'>` | 16 | **c** `8` | 31 | **b** `10` |
| 2 | **b** `53` (gabung string) | 17 | **b** `False` | 32 | **b** `54321` |
| 3 | **b** `15` | 18 | **b** `False` | 33 | **b** `2` (indeks 1) |
| 4 | **c** `str` | 19 | **b** `B` | 34 | **b** `40` |
| 5 | **c** `2nama` (tak boleh diawali angka) | 20 | **b** salah indentasi | 35 | **b** `[1,2,3]` |
| 6 | **a** `ababab` | 21 | **b** `tidak` (`0` = False) | 36 | **b** `[2,3]` |
| 7 | **b** `3.14` | 22 | **a** `genap` | 37 | **c** tuple |
| 8 | **b** `6` | 23 | **c** `0` | 38 | **b** `2` |
| 9 | **b** `False` (int ≠ str) | 24 | **a** `tengah` | 39 | **b** `KeyError` |
| 10 | **c** `# komentar` | 25 | **b** `!=` | 40 | **c** `3` |
| 11 | **b** `512` (`**` dari kanan) | 26 | **b** `0 1 2` | 41 | **b** `15` |
| 12 | **a** `3` (floor division) | 27 | **a** `2 5 8` | 42 | **c** `None` |
| 13 | **b** `2` (sisa bagi) | 28 | **b** keluar loop | 43 | **b** `12` lalu `None` |
| 14 | **b** `14` (kali dulu) | 29 | **b** lompat putaran berikut | 44 | **c** `ValueError` |
| 15 | **b** `float` `5.0` | 30 | **b** 5 | 45 | **d** `finally` |

**Catatan jebakan favorit PCEP:**
- No 11 — `**` bersifat *right-associative*: `2 ** (3 ** 2) = 2 ** 9 = 512`.
- No 2 vs No 3 — string `+` string = penggabungan; `int()` dulu kalau mau dijumlah.
- No 43 — `print` ≠ `return`. Fungsi yang hanya `print` mengembalikan `None`.
- No 26/27 — `range` mulai dari angka pertama, berhenti **sebelum** angka kedua.

</details>

---

## 🧭 Cara pakai untuk pengajar
- Bagi jadi sesi drill: kerjakan **per bagian (A–F)** sesuai sesi yang sudah dipelajari.
- Minta murid **menebak dulu** sebelum menjalankan di Colab, baru verifikasi.
- Fokuskan pembahasan pada soal yang salah — di situ letak miskonsepsinya.
