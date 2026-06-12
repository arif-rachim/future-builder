# Sesi 7 — Fungsi (`def`): Merapikan Kode

> **Durasi:** 75 menit · **Tools:** Google Colab · **Peserta:** Tazkia & Ardy (pemula)
> **Target PCEP:** Bagian 4 (fungsi, parameter & argumen, `return`, scope)

## 🎯 Tujuan sesi
Di akhir sesi ini, Tazkia & Ardy akan:
1. Membuat fungsi sendiri dengan `def`.
2. Memahami **parameter** & **argument**, serta nilai balik `return`.
3. Memahami beda variabel **lokal** dan **global** (scope) secara dasar.
4. Memecah program menjadi fungsi-fungsi yang rapi dan dapat dipakai ulang.

---

## ⏱️ Rundown 75 menit
| Waktu | Bagian | Aktivitas |
|-------|--------|-----------|
| 10 mnt | Pemanasan & review | Cek PR kamus mini |
| 20 mnt | Konsep + live coding | `def`, parameter, `return` |
| 25 mnt | Latihan terbimbing | Membuat fungsi |
| 15 mnt | Tantangan | Refactor kalkulator jadi fungsi |
| 5 mnt | Wrap-up & PR | Rangkuman, kosakata, tugas |

---

## 1) Pemanasan & Review (10 menit)
Bahas PR kamus mini. Pemantik:
> "Kalau ada kode yang kamu pakai berulang-ulang, copy-paste itu melelahkan dan rawan
> salah. Programmer profesional membungkusnya jadi **fungsi** — tulis sekali, pakai
> berkali-kali. Ini fondasi kode yang rapi di dunia kerja."

---

## 2) Konsep + Live Coding (20 menit)

### a. Membuat & memanggil fungsi
```python
def sapa():
    print("Halo, selamat datang!")

sapa()      # memanggil fungsi
sapa()      # bisa dipanggil berkali-kali
```

### b. Parameter & argument
```python
def sapa(nama):           # nama = parameter
    print("Halo,", nama)

sapa("Tazkia")            # "Tazkia" = argument
sapa("Ardy")
```

### c. `return` — mengembalikan nilai
```python
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)              # 8
print(tambah(10, 20))     # 30
```
> 🔑 Beda **`print`** vs **`return`**: `print` hanya menampilkan ke layar; `return`
> mengembalikan nilai supaya bisa **dipakai lagi** (disimpan, dihitung lagi). Ini sangat
> sering diuji di PCEP.

### d. Parameter dengan nilai default
```python
def sapa(nama, salam="Halo"):
    print(salam + ",", nama)

sapa("Ardy")                 # Halo, Ardy
sapa("Tazkia", "Selamat pagi")  # Selamat pagi, Tazkia
```

### e. Scope (lokal vs global) — dasar
```python
def coba():
    x = 10        # x ini LOKAL, hanya hidup di dalam fungsi
    print(x)

coba()
# print(x)        # ❌ ERROR: x tidak dikenal di luar fungsi
```

---

## 3) Latihan Terbimbing (25 menit)

**Latihan 1.** Buat fungsi `luas_persegi(sisi)` yang me-`return` luas. Panggil dengan beberapa nilai.

**Latihan 2.** Buat fungsi `ganjil_genap(n)` yang me-`return` string `"genap"` atau `"ganjil"`.

**Latihan 3.** Buat fungsi `rata_rata(daftar)` yang menerima sebuah list angka dan me-`return` rata-ratanya.

---

## 4) Tantangan: Refactor Kalkulator (15 menit)
Ingat kalkulator Sesi 2? Sekarang rapikan jadi fungsi:
1. Buat fungsi `tambah(a,b)`, `kurang(a,b)`, `kali(a,b)`, `bagi(a,b)`.
2. Tanyakan dua angka dari pengguna.
3. Panggil keempat fungsi dan tampilkan hasilnya.

Bonus: buat fungsi `kalkulator(a, b, operasi)` di mana `operasi` berupa string (`"+","-","*","/"`),
dan fungsi memilih operasi yang sesuai.

---

## 5) Wrap-up (5 menit)

### Rangkuman
- `def nama(parameter):` membuat fungsi; panggil dengan `nama(argument)`.
- `return` mengembalikan nilai agar bisa dipakai lagi (beda dari `print`).
- Parameter bisa punya nilai default. Variabel di dalam fungsi bersifat **lokal**.

### 🔤 English corner
| Istilah | Arti |
|---------|------|
| **function** | blok kode yang bisa dipakai ulang |
| **parameter** | variabel penerima di definisi fungsi |
| **argument** | nilai yang dikirim saat memanggil |
| **return** | mengembalikan nilai dari fungsi |
| **scope** | jangkauan hidup sebuah variabel |

### 📌 PR
Buat fungsi `cek_password(kata)` yang me-`return` `"kuat"` jika panjang kata ≥ 8 karakter,
selain itu `"lemah"`. Uji dengan beberapa input.

---

## ✅ Kunci jawaban (untuk pengajar)

<details>
<summary>Latihan 1</summary>

```python
def luas_persegi(sisi):
    return sisi * sisi

print(luas_persegi(4))   # 16
print(luas_persegi(7))   # 49
```
</details>

<details>
<summary>Latihan 2</summary>

```python
def ganjil_genap(n):
    if n % 2 == 0:
        return "genap"
    else:
        return "ganjil"

print(ganjil_genap(10))
print(ganjil_genap(7))
```
</details>

<details>
<summary>Latihan 3</summary>

```python
def rata_rata(daftar):
    return sum(daftar) / len(daftar)

print(rata_rata([80, 90, 100]))
```
</details>

<details>
<summary>Tantangan: Kalkulator (fungsi)</summary>

```python
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b):   return a * b
def bagi(a, b):   return a / b

a = float(input("Angka 1: "))
b = float(input("Angka 2: "))
print("Tambah:", tambah(a, b))
print("Kurang:", kurang(a, b))
print("Kali  :", kali(a, b))
print("Bagi  :", bagi(a, b))

# Bonus
def kalkulator(a, b, operasi):
    if operasi == "+": return a + b
    if operasi == "-": return a - b
    if operasi == "*": return a * b
    if operasi == "/": return a / b
    return "operasi tidak dikenal"

print(kalkulator(6, 2, "*"))   # 12
```
</details>

<details>
<summary>PR: Cek password</summary>

```python
def cek_password(kata):
    if len(kata) >= 8:
        return "kuat"
    else:
        return "lemah"

print(cek_password("rahasia"))      # lemah
print(cek_password("rahasiaku123")) # kuat
```
</details>

---

## 🧭 Catatan pengajar
- **`print` vs `return`** adalah konsep tersulit di sesi ini. Tunjukkan fungsi ber-`print` yang tidak bisa dijumlahkan vs fungsi ber-`return` yang bisa.
- Tekankan bahwa fungsi tanpa `return` mengembalikan `None`.
- **Beda level:** kenalkan ke Tazkia konsep `*args` / fungsi memanggil fungsi (komposisi); Ardy cukup fungsi sederhana ber-return.
- **Sesi depan:** error & exceptions + simulasi ujian PCEP — sesi penutup.
