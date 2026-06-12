# Sesi 4 — Perulangan: `for` & `while`

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 3 (loop `for`/`while`, `range`, `break`, `continue`)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Menggunakan `for` dengan `range()` untuk mengulang sejumlah kali.
2. Menggunakan `while` untuk mengulang selama syarat benar.
3. Mengendalikan loop dengan `break` dan `continue`.
4. Membuat program berulang (mis. tabel perkalian, tebak angka).

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR tahun kabisat |
| 20 mnt | Konsep + live coding | `for`, `while`, `break`, `continue` |
| 25 mnt | Latihan terbimbing | Pengulangan |
| 15 mnt | Tantangan | Game tebak angka |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR kabisat. Pemantik:
> "Bayangkan harus mencetak angka 1 sampai 100. Mau ngetik `print` 100 kali? Tentu tidak.
> Hari ini kita ajari komputer **mengulang** — keahlian utamanya."

---

## 2) Konsep + Live Coding (20 menit)

### a. `for` dengan `range()`
```python
for i in range(5):
    print("Halo", i)      # i = 0,1,2,3,4
```
`range(5)` menghasilkan angka 0 sampai 4 (5 angka, mulai dari 0).
```python
for i in range(1, 6):     # 1 sampai 5
    print(i)
for i in range(0, 10, 2): # 0,2,4,6,8 (langkah 2)
    print(i)
```

### b. `while` — ulang selama syarat benar
```python
hitung = 1
while hitung <= 5:
    print(hitung)
    hitung = hitung + 1   # WAJIB ada, kalau tidak loop tak berhenti!
```
> 🔑 Hati-hati **infinite loop** (loop tak berujung). Pastikan ada yang mengubah kondisi
> agar suatu saat menjadi `False`. Di Colab, hentikan dengan tombol ⏹ (stop).

### c. `break` dan `continue`
```python
for i in range(1, 10):
    if i == 5:
        break        # hentikan loop sepenuhnya
    print(i)         # 1,2,3,4

for i in range(1, 6):
    if i == 3:
        continue     # lewati sisa, lanjut ke putaran berikut
    print(i)         # 1,2,4,5
```

### d. Menjumlah dalam loop (pola akumulasi)
```python
total = 0
for i in range(1, 11):
    total = total + i
print("Jumlah 1-10:", total)   # 55
```

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Cetak bilangan genap dari 2 sampai 20.

**Latihan 2.** Tanyakan sebuah angka `n`, cetak **tabel perkalian** -nya (1 sampai 10).

**Latihan 3.** Pakai `while`: minta pengguna terus memasukkan kata, berhenti jika mengetik `"stop"`.

---

## 4) Tantangan: Game Tebak Angka (15 menit)
Komputer "memikirkan" angka rahasia (mis. `rahasia = 7`). Pengguna menebak berulang
sampai benar. Setiap tebakan, beri petunjuk `"terlalu besar"` / `"terlalu kecil"`.

```python
rahasia = 7
# lengkapi dengan while ...
```
Bonus: hitung berapa kali tebakan sampai benar.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- `for ... in range()` untuk jumlah pengulangan yang diketahui.
- `while` untuk mengulang selama kondisi benar — waspadai infinite loop.
- `break` keluar dari loop; `continue` lompat ke putaran berikutnya.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **loop** | perulangan |
| **iteration** | satu kali putaran loop |
| **range** | rentang angka |
| **break** | keluar dari loop |
| **continue** | lanjut ke putaran berikutnya |

### 📌 PR
Buat program yang menghitung **faktorial** sebuah angka (mis. `5! = 5*4*3*2*1 = 120`)
menggunakan loop.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
for i in range(2, 21, 2):
    print(i)
```
</details>

<details>
<summary>Latihan 2</summary>

```python
n = int(input("Angka: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```
</details>

<details>
<summary>Latihan 3</summary>

```python
while True:
    kata = input("Ketik kata (stop untuk berhenti): ")
    if kata == "stop":
        break
    print("Kamu mengetik:", kata)
```
</details>

<details>
<summary>Tantangan: Tebak Angka</summary>

```python
rahasia = 7
percobaan = 0
while True:
    tebak = int(input("Tebak angka (1-10): "))
    percobaan = percobaan + 1
    if tebak == rahasia:
        print("Benar! Dalam", percobaan, "tebakan.")
        break
    elif tebak > rahasia:
        print("Terlalu besar")
    else:
        print("Terlalu kecil")
```
</details>

<details>
<summary>PR: Faktorial</summary>

```python
n = int(input("Angka: "))
hasil = 1
for i in range(1, n + 1):
    hasil = hasil * i
print(n, "! =", hasil)
```
</details>

---

## 🧭 Catatan pengajar
- **Demonstrasikan infinite loop** sengaja (lupa menaikkan counter), lalu tunjukkan cara stop di Colab. Pelajaran yang menempel.
- Tekankan `range(n)` mulai dari **0** dan berhenti **sebelum** n — sumber off-by-one error klasik & sering diuji PCEP.
- **Beda level:** ajak Tazkia membuat versi tebak-angka dengan angka acak (`import random`); Ardy cukup angka tetap dulu.
- **Sesi depan:** menyimpan banyak data dalam satu wadah — `list`.
