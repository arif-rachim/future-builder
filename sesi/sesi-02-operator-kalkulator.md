# Sesi 2 — Operator & Angka: Bikin Kalkulator

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 2 (operator, ekspresi, tipe data numerik, konversi tipe)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Menggunakan operator aritmetika: `+ - * / // % **`.
2. Memahami beda `int` dan `float`, serta konversi `int()` / `float()` / `str()`.
3. Memahami **urutan operasi** (operator precedence).
4. Membuat **kalkulator sederhana** yang menerima dua angka dari pengguna.

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR sesi 1, ingat `input` + `int()` |
| 20 mnt | Konsep + live coding | Operator & tipe angka |
| 25 mnt | Latihan terbimbing | Hitung-hitungan |
| 15 mnt | Tantangan | Kalkulator dua angka |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Minta masing-masing menjalankan ulang "bot perkenalan" dari PR. Tanyakan: "Kenapa kemarin
`umur + 1` sempat error?" → ingatkan `input()` menghasilkan **string**, perlu `int()`.

> 💡 Pemantik: "Komputer pertama diciptakan untuk satu hal: **menghitung**. Hari ini kita
> bikin program penghitung kita sendiri."

---

## 2) Konsep + Live Coding (20 menit)

### a. Operator aritmetika
```python
print(7 + 3)    # 10  penjumlahan
print(7 - 3)    # 4   pengurangan
print(7 * 3)    # 21  perkalian
print(7 / 3)    # 2.333...  pembagian (hasil selalu float)
print(7 // 3)   # 2   pembagian bulat (floor division)
print(7 % 3)    # 1   sisa bagi (modulo)
print(7 ** 3)   # 343 pangkat (7 pangkat 3)
```

> 🔑 Bedakan `/` (hasil pecahan/`float`) vs `//` (dibulatkan ke bawah). `%` (modulo)
> sering keluar di PCEP — gunanya cari sisa bagi (mis. cek ganjil/genap).

### b. `int` vs `float`
```python
a = 10        # integer (angka bulat)
b = 3.5       # float (angka desimal)
print(a + b)  # 13.5  -> campur int & float jadi float
```

### c. Konversi tipe (type casting)
```python
print(int(3.9))      # 3   (memotong, bukan membulatkan)
print(float(5))      # 5.0
print(str(100))      # "100"  -> jadi teks
```

### d. Urutan operasi (precedence)
```python
print(2 + 3 * 4)     # 14, bukan 20 (kali dulu)
print((2 + 3) * 4)   # 20, kurung dieksekusi dulu
```
Urutan: `**` → `* / // %` → `+ -`. Pakai kurung kalau ragu.

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Hitung dan tampilkan: luas persegi panjang dengan panjang 12 dan lebar 5.

**Latihan 2.** Tanyakan sebuah angka, lalu tampilkan **kuadrat** dan **akar pangkat** -nya.
> Petunjuk: akar = pangkat `** 0.5`.

**Latihan 3.** Tanyakan jumlah menit, lalu ubah jadi format **jam & menit**.
> Petunjuk: gunakan `//` dan `%` dengan 60.

---

## 4) Tantangan: Kalkulator Dua Angka (15 menit)
Buat program yang:
1. Menanyakan **angka pertama** dan **angka kedua**.
2. Menampilkan hasil `+`, `-`, `*`, `/`, dan sisa bagi `%`.

Tantangan bonus: tampilkan juga **rata-rata** kedua angka.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- Operator: `+ - * / // % **`.
- `/` selalu float; `//` membulatkan ke bawah; `%` sisa bagi.
- Konversi: `int()`, `float()`, `str()`. Kurung mengatur urutan.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **operator** | simbol operasi (mis. `+`) |
| **float** | angka desimal/pecahan |
| **modulo** | sisa hasil bagi (`%`) |
| **expression** | gabungan nilai & operator yang menghasilkan nilai |
| **type casting** | mengubah tipe data |

### 📌 PR
Buat program "konversi suhu": tanyakan suhu Celsius, tampilkan dalam Fahrenheit.
> Rumus: `F = C * 9/5 + 32`.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
panjang = 12
lebar = 5
print("Luas:", panjang * lebar)
```
</details>

<details>
<summary>Latihan 2</summary>

```python
angka = float(input("Masukkan sebuah angka: "))
print("Kuadrat:", angka ** 2)
print("Akar:", angka ** 0.5)
```
</details>

<details>
<summary>Latihan 3</summary>

```python
total = int(input("Berapa menit? "))
jam = total // 60
menit = total % 60
print(jam, "jam", menit, "menit")
```
</details>

<details>
<summary>Tantangan: Kalkulator</summary>

```python
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))
print("Jumlah :", a + b)
print("Selisih:", a - b)
print("Kali   :", a * b)
print("Bagi   :", a / b)
print("Sisa   :", a % b)
print("Rata2  :", (a + b) / 2)   # bonus
```
</details>

<details>
<summary>PR: Konversi suhu</summary>

```python
c = float(input("Suhu dalam Celsius: "))
f = c * 9/5 + 32
print(c, "C =", f, "F")
```
</details>

---

## 🧭 Catatan pengajar
- Tunjukkan langsung di Colab beda `7/3` vs `7//3` — visual lebih nempel daripada dijelaskan.
- Kalau pembagian dengan 0, akan muncul `ZeroDivisionError` — ini bahan bagus untuk Sesi 8 (exceptions). Catat saja dulu.
- **Beda level:** untuk Tazkia, singgung bahwa `float` punya keterbatasan presisi (`0.1 + 0.2`); untuk Ardy cukup sampai konsep dasar.
- **Sesi depan:** pengambilan keputusan dengan `if` — program mulai bisa "berpikir".
