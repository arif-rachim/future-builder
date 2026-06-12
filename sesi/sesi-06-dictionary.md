# Sesi 6 — `dictionary` & Mini-Proyek Data

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 4 (dictionary, pasangan key–value, iterasi dict)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Membuat dan mengakses `dictionary` (pasangan kunci → nilai).
2. Menambah, mengubah, dan menghapus item dictionary.
3. Mengulang isi dictionary dengan `for` (`keys`, `values`, `items`).
4. Menggabungkan list + dictionary dalam **mini-proyek buku alamat**.

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR nilai ujian |
| 20 mnt | Konsep + live coding | Dictionary |
| 25 mnt | Latihan terbimbing | Olah dictionary |
| 15 mnt | Tantangan | Buku alamat sederhana |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR nilai ujian. Pemantik:
> "List menyimpan data berurutan dengan nomor. Tapi bagaimana menyimpan 'nama → nomor HP'?
> Kita butuh **label**, bukan nomor urut. Itulah **dictionary** — seperti kamus:
> cari kata (kunci), dapat artinya (nilai)."

---

## 2) Konsep + Live Coding (20 menit)

### a. Membuat dictionary
```python
murid = {
    "nama": "Tazkia",
    "umur": 18,
    "jurusan": "Computer Science"
}
print(murid)
```
Setiap item punya **key** (kunci) dan **value** (nilai), dipisah `:`.

### b. Mengakses nilai lewat kunci
```python
print(murid["nama"])      # Tazkia
print(murid["umur"])      # 18
```

### c. Menambah / mengubah / menghapus
```python
murid["kampus"] = "UI"        # tambah item baru
murid["umur"] = 19            # ubah nilai
del murid["jurusan"]          # hapus item
print(murid)
```

### d. Mengecek keberadaan kunci
```python
if "nama" in murid:
    print("Ada nama:", murid["nama"])
```

### e. Mengulang dictionary
```python
for kunci in murid:
    print(kunci, "->", murid[kunci])

for kunci, nilai in murid.items():
    print(kunci, ":", nilai)
```
`.keys()` semua kunci, `.values()` semua nilai, `.items()` pasangan keduanya.

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Buat dictionary `harga` berisi 3 barang dan harganya. Cetak harga salah satu barang.

**Latihan 2.** Dari dictionary `nilai = {"Matematika": 90, "Fisika": 75, "Biologi": 85}`,
cetak setiap mata pelajaran dan nilainya dengan format `"Matematika: 90"`.

**Latihan 3.** Tambahkan satu pelajaran baru ke dictionary di Latihan 2, lalu cetak **rata-rata** semua nilai.
> Petunjuk: `sum(nilai.values()) / len(nilai)`.

---

## 4) Tantangan: Buku Alamat (15 menit)
Buat program buku alamat (gabungan dictionary):
1. Mulai dari dictionary kosong `{}`.
2. Ulang: tanyakan nama & nomor HP; simpan sebagai `kontak[nama] = nomor`.
3. Berhenti jika nama yang dimasukkan `"selesai"`.
4. Di akhir, cetak seluruh kontak dengan rapi.

Bonus: setelah selesai, minta sebuah nama dan cetak nomornya (atau `"tidak ditemukan"`).

---

## 5) Wrap-up (5 menit)

### Rangkuman
- Dictionary = pasangan **key → value**, diakses lewat kunci (bukan indeks angka).
- Tambah/ubah: `d[kunci] = nilai`. Hapus: `del`. Cek: `in`.
- Iterasi dengan `.items()`, `.keys()`, `.values()`.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **dictionary** | koleksi pasangan kunci–nilai |
| **key** | kunci/label pengakses |
| **value** | nilai yang disimpan |
| **pair** | pasangan key–value |
| **lookup** | pencarian nilai lewat kunci |

### 📌 PR
Buat "kamus mini" Inggris→Indonesia berisi minimal 5 kata. Lalu minta pengguna mengetik
sebuah kata Inggris, dan cetak artinya (atau `"kata tidak ada"`).

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
harga = {"roti": 12000, "susu": 18000, "telur": 25000}
print("Harga susu:", harga["susu"])
```
</details>

<details>
<summary>Latihan 2</summary>

```python
nilai = {"Matematika": 90, "Fisika": 75, "Biologi": 85}
for pelajaran, n in nilai.items():
    print(pelajaran + ":", n)
```
</details>

<details>
<summary>Latihan 3</summary>

```python
nilai["Kimia"] = 80
print("Rata-rata:", sum(nilai.values()) / len(nilai))
```
</details>

<details>
<summary>Tantangan: Buku Alamat</summary>

```python
kontak = {}
while True:
    nama = input("Nama (selesai untuk berhenti): ")
    if nama == "selesai":
        break
    nomor = input("Nomor HP: ")
    kontak[nama] = nomor

print("--- Buku Alamat ---")
for nama, nomor in kontak.items():
    print(nama, "->", nomor)

# Bonus
cari = input("Cari nama: ")
if cari in kontak:
    print(kontak[cari])
else:
    print("tidak ditemukan")
```
</details>

<details>
<summary>PR: Kamus mini</summary>

```python
kamus = {"apple": "apel", "book": "buku", "cat": "kucing",
         "house": "rumah", "water": "air"}
kata = input("Kata Inggris: ")
if kata in kamus:
    print(kamus[kata])
else:
    print("kata tidak ada")
```
</details>

---

## 🧭 Catatan pengajar
- Tekankan beda **list** (akses lewat nomor indeks) vs **dictionary** (akses lewat kunci bermakna).
- Mengakses kunci yang tidak ada → `KeyError`. Tunjukkan, lalu kenalkan pengecekan `in` sebagai pencegah (bahan Sesi 8 juga).
- **Beda level:** ajak Tazkia membuat list of dictionaries (mis. daftar beberapa murid) sebagai pratinjau struktur data nyata; Ardy fokus satu dictionary.
- **Sesi depan:** fungsi (`def`) — merapikan & menggunakan ulang kode.
