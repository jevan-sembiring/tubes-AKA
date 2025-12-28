# 📊 Perbandingan Jump Search dan Exponential Search

Website ini merupakan aplikasi sederhana berbasis **Python (Flask)** yang digunakan untuk membandingkan performa algoritma **Jump Search** dan **Exponential Search** pada data terurut, berdasarkan:

* Jumlah langkah (step)
* Waktu eksekusi (milidetik)
* Skenario **Best Case, Average Case, dan Worst Case**
* Perbandingan versi **iteratif dan rekursif** pada Exponential Search

Aplikasi ini dibuat untuk memenuhi kebutuhan **Tugas Besar Analisis Kompleksitas Algoritma (AKA)**.

---

## 🧩 Fitur Utama

* Input jumlah data terurut (`n`)
* Data otomatis dibentuk dari `1` sampai `n`
* Pengujian:

  * Jump Search
  * Exponential Search Iteratif
  * Exponential Search Rekursif
* Tabel hasil perbandingan waktu dan langkah
* Grafik:

  1. Perbandingan Exponential Search Iteratif vs Rekursif
  2. Perbandingan Jump Search vs Exponential Search

---

## 🛠️ Teknologi yang Digunakan

* Python 3
* Flask
* Matplotlib
* HTML (Jinja2 Template)

---

## ⚙️ Cara Menjalankan Website (VS Code)

### 1️⃣ Pastikan Python Terinstall

Cek versi Python:

```bash
python3 --version
```

Disarankan Python **3.9 ke atas**.

---

### 2️⃣ Buka Folder Project di VS Code

```bash
cd jump_vs_exponential
code .
```

---

### 3️⃣ Buat Virtual Environment (Disarankan)

**MacOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4️⃣ Install Dependensi

```bash
pip install flask matplotlib
```

Atau jika tersedia `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Jalankan Aplikasi Flask

```bash
python app.py
```

Jika berhasil, akan muncul output seperti:

```
Running on http://127.0.0.1:5000
```

---

### 6️⃣ Buka Website di Browser

Buka browser dan akses:

```
http://127.0.0.1:5000
```

---

## 🧪 Cara Menggunakan Website

1. Masukkan nilai `n` (jumlah data terurut, harus > 0)
2. Klik tombol **Proses**
3. Website akan menampilkan:

   * Tabel hasil Best, Average, dan Worst Case
   * Grafik perbandingan algoritma

---

## 📌 Catatan Penting

* Waktu eksekusi diukur dalam **milidetik (ms)**
* Perbedaan waktu antara Colab dan website adalah **normal**, karena:

  * Perbedaan environment
  * Overhead web server (Flask)
* Fokus analisis ada pada **pola perbandingan**, bukan nilai absolut waktu

---

## 🎓 Tujuan Akademik

Aplikasi ini dirancang untuk:

* Menganalisis kompleksitas algoritma pencarian
* Membandingkan efisiensi Jump Search dan Exponential Search
* Memenuhi ketentuan tugas:

  > *Satu algoritma diturunkan ke dalam dua pendekatan (iteratif dan rekursif)*
