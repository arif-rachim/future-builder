# Sesi 1 — Halo Python: Program Pertamamu

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 1 (konsep dasar Python) & Bagian 2 (variabel, tipe data, I/O)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Bisa membuka dan menjalankan kode di Google Colab.
2. Memahami `print()` untuk menampilkan teks dan `input()` untuk menerima masukan.
3. Mengerti **variabel** (variable) serta tipe data **string** dan **integer**.
4. Pulang membawa **1 program buatan sendiri yang jalan**: sebuah "bot perkenalan".

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pembuka & setup | Cerita pemantik + buka Google Colab |
| 20 mnt | Konsep + live coding | Pengajar ngetik, murid ikut |
| 25 mnt | Latihan terbimbing | Murid ngetik sendiri, pengajar dampingi |
| 15 mnt | Tantangan | Bikin "bot perkenalan" (boleh berdua) |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas rumah |

---

## 1) Pembuka & Setup (10 menit)

### Pemantik (cerita pembuka)
> "Komputer itu super cepat, tapi *bodoh* — dia cuma melakukan persis apa yang kita
> perintahkan. Hari ini kita belajar bahasa untuk memberi perintah itu: **Python**.
> Dalam 75 menit, kalian akan bikin program yang ngobrol sama kalian."

Kenapa Python? Bahasa paling ramah pemula, dipakai di dunia kerja nyata: web (Instagram),
data science, AI (ChatGPT dilatih dengan banyak Python), otomasi, dll.

### Setup Google Colab (lakukan bareng)
1. Buka **https://colab.research.google.com** (login dengan akun Google).
2. Klik **File → New notebook**.
3. Ketik di sel pertama: `print("Halo!")`
4. Tekan **Shift + Enter** untuk menjalankan. Kalau muncul tulisan `Halo!` di bawah → **berhasil!** 🎉

> 💡 *Catatan pengajar:* pastikan keduanya berhasil menjalankan sel pertama sebelum lanjut.
> Inilah momen "kode pertamaku jalan" — rayakan kecil-kecilan, ini yang bikin nagih.

---

## 2) Konsep + Live Coding (20 menit)
Pengajar mengetik, murid menyalin & menjalankan tiap baris.

### a. `print()` — menampilkan sesuatu
```python
print("Halo, dunia!")
print("Belajar Python itu seru")
```
`print` artinya "cetak / tampilkan". Teks di dalam tanda kutip disebut **string** (untaian karakter).

### b. Variabel (variable) — kotak penyimpan
```python
nama = "Tazkia"
print(nama)
print("Halo,", nama)
```
`nama` adalah **variabel**: nama kotak untuk menyimpan nilai. Tanda `=` artinya
"isi kotak ini dengan...", bukan "sama dengan" seperti di matematika.

### c. `input()` — menerima masukan dari pengguna
```python
nama = input("Siapa namamu? ")
print("Senang berkenalan,", nama)
```
`input()` membuat program **bertanya** dan menunggu pengguna mengetik jawaban.

### d. Angka & tipe data
```python
umur = input("Berapa umurmu? ")
print("Tahun depan umurmu", umur + 1)   # ❌ ini akan ERROR — kenapa ya?
```
Ternyata error! Karena `input()` selalu menghasilkan **string**, bukan **integer** (angka bulat).
Komputer bingung "menjumlah" teks. Perbaikannya — ubah dulu jadi angka pakai `int()`:
```python
umur = int(input("Berapa umurmu? "))
print("Tahun depan umurmu", umur + 1)   # ✅ sekarang jalan
```

> 🔑 **Poin penting:** `string` = teks, `integer` = angka bulat. `int()` mengubah teks
> jadi angka. Ini konsep yang sering keluar di PCEP.

---

## 3) Latihan Terbimbing (25 menit)
Murid mengerjakan sendiri di Colab; pengajar berkeliling/mendampingi.

**Latihan 1.** Tampilkan 3 baris: nama lengkapmu, sekolah/kampusmu, dan hobimu.

**Latihan 2.** Buat program yang menanyakan **makanan favorit**, lalu membalas:
`"Wah, <makanan> memang enak!"`

**Latihan 3.** Buat program yang menanyakan **tahun lahir**, lalu menghitung & menampilkan umur.
> Petunjuk: tahun sekarang `2026`. Ingat `int()`.

---

## 4) Tantangan: "Bot Perkenalan" (15 menit)
Boleh dikerjakan berdua. Buat program yang:
1. Menanyakan **nama**.
2. Menanyakan **umur**.
3. Menanyakan **cita-cita**.
4. Membalas dengan satu paragraf ramah, contoh:
   `"Halo Ardy! Umurmu 16 tahun ya. Semoga cita-citamu jadi game developer tercapai 🚀"`

Tantangan bonus (opsional): tambahkan hitungan **"di tahun berapa kamu akan berumur 25"**.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- `print()` menampilkan, `input()` bertanya.
- **Variabel** menyimpan nilai.
- `input()` menghasilkan **string**; pakai `int()` untuk mengubahnya jadi angka.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **print** | menampilkan / mencetak ke layar |
| **input** | masukan dari pengguna |
| **variable** | wadah penyimpan nilai |
| **string** | data berupa teks |
| **integer** | data berupa angka bulat |

### 📌 PR (tugas rumah)
Sempurnakan "bot perkenalan"-mu, lalu tambahkan satu pertanyaan baru sesukamu
(misal: warna favorit) dan balasan yang sesuai. Simpan notebook-nya — minggu depan kita kembangkan.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
print("Tazkia Rachim")
print("Computer Science, Universitas Indonesia")
print("Hobi: membaca")
```
</details>

<details>
<summary>Latihan 2</summary>

```python
makanan = input("Apa makanan favoritmu? ")
print("Wah,", makanan, "memang enak!")
```
</details>

<details>
<summary>Latihan 3</summary>

```python
tahun_lahir = int(input("Tahun berapa kamu lahir? "))
umur = 2026 - tahun_lahir
print("Berarti umurmu sekitar", umur, "tahun.")
```
</details>

<details>
<summary>Tantangan: Bot Perkenalan</summary>

```python
nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))
cita = input("Apa cita-citamu? ")

print("Halo", nama + "!", "Umurmu", umur, "tahun ya.")
print("Semoga cita-citamu jadi", cita, "tercapai 🚀")

# Bonus
selisih = 25 - umur
print("Kamu akan berumur 25 tahun di", 2026 + selisih)
```
</details>

---

## 🧭 Catatan pengajar
- **Jangan kejar tuntas.** Kalau setup Colab makan waktu, pangkas latihan — yang penting tiap anak pulang dengan 1 program jalan.
- **Rayakan error.** Error itu normal & bagian dari belajar. Tunjukkan cara membaca pesan error dengan tenang.
- **Beda level Tazkia & Ardy:** kalau Tazkia cepat selesai, beri tantangan bonus; ajak dia bantu jelaskan ke Ardy (mengajar = cara belajar terbaik).
- **Sesi depan:** Operator & angka — kita bikin kalkulator sungguhan (PCEP Bagian 2).
