# Sesi 5 — Koleksi Data: `list` & `tuple`

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 4 (list, indexing, slicing, method list, tuple)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Membuat dan mengakses `list` (indexing & slicing).
2. Menggunakan method list: `append`, `remove`, `len`, `sort`.
3. Mengulang isi list dengan `for`.
4. Memahami `tuple` dan bedanya dengan list (immutable).

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR faktorial |
| 20 mnt | Konsep + live coding | List & tuple |
| 25 mnt | Latihan terbimbing | Olah data list |
| 15 mnt | Tantangan | Daftar belanja |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR faktorial. Pemantik:
> "Sampai sekarang satu variabel menyimpan satu nilai. Tapi kalau punya 30 nama murid?
> Bikin 30 variabel? Tidak. Kita pakai **list** — satu wadah untuk banyak data."

---

## 2) Konsep + Live Coding (20 menit)

### a. Membuat list
```python
buah = ["apel", "mangga", "jeruk"]
print(buah)
print(len(buah))      # 3 -> jumlah elemen
```

### b. Indexing (mengakses elemen)
```python
print(buah[0])    # "apel"  -> indeks mulai dari 0!
print(buah[2])    # "jeruk"
print(buah[-1])   # "jeruk" -> indeks negatif: dari belakang
```

### c. Mengubah & menambah
```python
buah[1] = "pisang"        # ganti elemen
buah.append("anggur")     # tambah di akhir
buah.remove("apel")       # hapus berdasarkan nilai
print(buah)
```

### d. Slicing (mengambil potongan)
```python
angka = [10, 20, 30, 40, 50]
print(angka[1:4])   # [20, 30, 40] -> indeks 1 s/d 3
print(angka[:2])    # [10, 20]
print(angka[3:])    # [40, 50]
```

### e. Mengulang list dengan `for`
```python
for b in buah:
    print("Saya suka", b)
```

### f. Method berguna
```python
nilai = [70, 90, 55, 88]
print(max(nilai), min(nilai), sum(nilai))
nilai.sort()
print(nilai)        # urut menaik
```

### g. `tuple` — list yang tidak bisa diubah
```python
koordinat = (3, 5)
print(koordinat[0])      # 3
# koordinat[0] = 9       # ❌ ERROR: tuple immutable (tak bisa diubah)
```
Gunakan tuple untuk data yang **tidak boleh berubah** (mis. koordinat, tanggal lahir).

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Buat list 5 angka, cetak jumlah dan rata-ratanya.

**Latihan 2.** Buat list nama teman, lalu cetak masing-masing dengan format `"1. Budi"`, `"2. Sari"`, dst.
> Petunjuk: pakai `for i in range(len(...))`.

**Latihan 3.** Dari list `[12, 7, 25, 3, 18]`, cetak hanya angka yang lebih besar dari 10.

---

## 4) Tantangan: Daftar Belanja (15 menit)
Buat program daftar belanja interaktif:
1. Mulai dari list kosong `[]`.
2. Ulang: minta pengguna mengetik barang; jika `"selesai"`, berhenti.
3. Setiap barang lain di-`append` ke list.
4. Di akhir, cetak seluruh daftar bernomor dan jumlah totalnya.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- List menyimpan banyak nilai; indeks mulai dari 0; `-1` elemen terakhir.
- `append`, `remove`, `len`, `sort`, `sum`, `max`, `min`.
- Slicing `[a:b]` ambil potongan. Tuple = list yang tidak bisa diubah.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **list** | koleksi terurut yang bisa diubah |
| **index** | posisi elemen (mulai 0) |
| **slice** | potongan dari list |
| **method** | fungsi yang melekat pada objek (`.append()`) |
| **immutable** | tidak bisa diubah (tuple) |

### 📌 PR
Buat program yang menyimpan 5 nilai ujian dalam list, lalu cetak nilai **tertinggi**,
**terendah**, dan **rata-rata** -nya.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
angka = [10, 20, 30, 40, 50]
print("Jumlah:", sum(angka))
print("Rata-rata:", sum(angka) / len(angka))
```
</details>

<details>
<summary>Latihan 2</summary>

```python
teman = ["Budi", "Sari", "Tazkia", "Ardy"]
for i in range(len(teman)):
    print(str(i + 1) + ".", teman[i])
```
</details>

<details>
<summary>Latihan 3</summary>

```python
angka = [12, 7, 25, 3, 18]
for n in angka:
    if n > 10:
        print(n)
```
</details>

<details>
<summary>Tantangan: Daftar Belanja</summary>

```python
belanja = []
while True:
    barang = input("Barang (selesai untuk berhenti): ")
    if barang == "selesai":
        break
    belanja.append(barang)

print("--- Daftar Belanja ---")
for i in range(len(belanja)):
    print(str(i + 1) + ".", belanja[i])
print("Total", len(belanja), "barang.")
```
</details>

<details>
<summary>PR: Nilai ujian</summary>

```python
nilai = [78, 92, 65, 88, 70]
print("Tertinggi:", max(nilai))
print("Terendah :", min(nilai))
print("Rata-rata:", sum(nilai) / len(nilai))
```
</details>

---

## 🧭 Catatan pengajar
- **Indeks mulai 0** adalah konsep yang paling sering bikin pemula tersandung — ulang berkali-kali.
- Tunjukkan langsung error saat mencoba mengubah tuple; kontras dengan list yang berhasil.
- **Beda level:** kenalkan **list comprehension** ke Tazkia (`[n for n in angka if n > 10]`) sebagai sneak-peek; Ardy cukup dengan loop biasa.
- **Sesi depan:** `dictionary` — menyimpan data berpasangan (kunci → nilai).
