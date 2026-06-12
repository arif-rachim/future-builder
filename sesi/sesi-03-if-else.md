# Sesi 3 — Pengambilan Keputusan: `if` / `elif` / `else`

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 3 (kondisi, operator perbandingan & logika, percabangan)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Menggunakan operator perbandingan (`== != > < >= <=`) dan logika (`and or not`).
2. Membuat percabangan dengan `if`, `elif`, `else`.
3. Memahami pentingnya **indentasi** (indentation) di Python.
4. Membuat program yang **mengambil keputusan** berdasarkan masukan.

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR konversi suhu |
| 20 mnt | Konsep + live coding | Kondisi & percabangan |
| 25 mnt | Latihan terbimbing | Program pengambil keputusan |
| 15 mnt | Tantangan | Penilai nilai ujian |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR konversi suhu. Pemantik:
> "Sejauh ini program kita patuh lurus. Hari ini dia mulai bisa **memilih** — melakukan
> hal berbeda tergantung situasi. Persis seperti otak kita memutuskan."

---

## 2) Konsep + Live Coding (20 menit)

### a. Nilai benar/salah (boolean)
```python
print(5 > 3)     # True
print(5 == 3)    # False  -> perhatikan: == (banding), bukan = (isi)
```
`True` dan `False` adalah tipe **boolean**.

### b. Operator perbandingan
```python
#  ==  sama dengan       !=  tidak sama
#  >   lebih besar       <   lebih kecil
#  >=  besar/sama        <=  kecil/sama
```

### c. `if` — lakukan jika benar
```python
umur = int(input("Berapa umurmu? "))
if umur >= 17:
    print("Kamu sudah boleh punya KTP.")
```
> 🔑 Perhatikan **titik dua** `:` dan **indentasi** (spasi menjorok). Python pakai
> indentasi untuk menandai blok kode — ini wajib, bukan sekadar rapi.

### d. `if` / `else`
```python
if umur >= 17:
    print("Sudah dewasa.")
else:
    print("Masih di bawah umur.")
```

### e. `if` / `elif` / `else` — banyak pilihan
```python
nilai = int(input("Nilai ujian: "))
if nilai >= 85:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("Perlu remедial")
```

### f. Operator logika
```python
umur = 20
punya_sim = True
if umur >= 18 and punya_sim:
    print("Boleh menyetir.")
# and = kedua syarat benar | or = salah satu benar | not = kebalikan
```

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Tanyakan sebuah angka, cetak `"Genap"` atau `"Ganjil"`.
> Petunjuk: pakai `% 2`.

**Latihan 2.** Tanyakan umur, cetak kategori: `< 13` Anak, `13–17` Remaja, `>= 18` Dewasa.

**Latihan 3.** Tanyakan dua angka, cetak mana yang lebih besar (atau "sama").

---

## 4) Tantangan: Penilai Nilai Ujian (15 menit)
Buat program yang:
1. Menanyakan nilai (0–100).
2. Menolak jika di luar 0–100 (cetak `"Nilai tidak valid"`).
3. Jika valid, cetak grade A/B/C/D/E sesuai aturanmu.

Bonus: tambahkan pesan `"Selamat!"` jika grade A atau B.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- `==` membandingkan, `=` mengisi.
- `if`/`elif`/`else` untuk percabangan; indentasi menandai blok.
- `and`, `or`, `not` menggabungkan kondisi.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **condition** | syarat yang dievaluasi benar/salah |
| **boolean** | tipe nilai `True`/`False` |
| **branch** | cabang alur program |
| **indentation** | spasi menjorok penanda blok |
| **comparison operator** | operator perbandingan |

### 📌 PR
Buat "cek tahun kabisat": tanyakan tahun, cetak apakah kabisat (leap year).
> Aturan: habis dibagi 4, **kecuali** habis dibagi 100 tetapi tidak habis dibagi 400.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
n = int(input("Masukkan angka: "))
if n % 2 == 0:
    print("Genap")
else:
    print("Ganjil")
```
</details>

<details>
<summary>Latihan 2</summary>

```python
umur = int(input("Umur: "))
if umur < 13:
    print("Anak")
elif umur <= 17:
    print("Remaja")
else:
    print("Dewasa")
```
</details>

<details>
<summary>Latihan 3</summary>

```python
a = int(input("Angka 1: "))
b = int(input("Angka 2: "))
if a > b:
    print(a, "lebih besar")
elif b > a:
    print(b, "lebih besar")
else:
    print("Sama besar")
```
</details>

<details>
<summary>Tantangan: Penilai</summary>

```python
nilai = int(input("Nilai (0-100): "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("A - Selamat!")
elif nilai >= 70:
    print("B - Selamat!")
elif nilai >= 60:
    print("C")
elif nilai >= 50:
    print("D")
else:
    print("E")
```
</details>

<details>
<summary>PR: Tahun kabisat</summary>

```python
th = int(input("Tahun: "))
if th % 4 == 0 and (th % 100 != 0 or th % 400 == 0):
    print("Kabisat")
else:
    print("Bukan kabisat")
```
</details>

---

## 🧭 Catatan pengajar
- **Error paling umum:** lupa `:` atau indentasi salah → `IndentationError`. Tunjukkan dengan sengaja sekali.
- Tekankan beda `=` vs `==`; ini sumber bug klasik dan sering diuji di PCEP.
- **Beda level:** ajak Tazkia menyederhanakan kondisi kabisat & diskusikan keterbacaan; untuk Ardy cukup sampai jalan.
- **Sesi depan:** perulangan — biar program bisa mengulang tanpa copy-paste.
