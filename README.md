## 🕵️‍♀️ Instagram Follow Checker (GUI)

Aplikasi Python sederhana berbasis GUI (Tkinter) untuk membantu kamu mengecek siapa saja yang kamu follow, tapi tidak follow kamu balik di Instagram.

---

## 📥 1. Cara Mendapatkan File JSON dari Instagram

1. Buka Instagram lewat browser/app 🌐
2. Masuk ke **Pengaturan dan Privasi**
3. Pilih **Pusat Akun > Data dan Privasi**
4. Pilih **Unduh Informasi**
5. Pilih format **JSON**📄, lalu pilih hanya **Orang yang Anda Ikuti dan Pengikut**
6. Pilih kisaran tanggal **semua waktu** ⏳
7. Setelah selesai, kamu akan mendapatkan file ZIP
8. Ekstrak ZIP tersebut, cari dua file berikut:
   - `followers_1.json`
   - `following.json`

---

## 🛠 2. Cara Menjalankan Program

### Opsi A: Lewat VS Code💻

1. Pastikan kamu sudah install [Python](https://www.python.org/downloads/)
2. Buka folder project ini di VS Code
3. Jalankan terminal di VS Code (Ctrl + `)
4. Jalankan perintah berikut:

```bash
python cek_instagram_gui.py
```

### Opsi B: Lewat Terminal Biasa (CMD)

1. Buka folder tempat kamu menyimpan file `cek_instagram_gui.py`
2. Tekan **Shift + Klik Kanan** lalu pilih **"Open PowerShell window here"**
3. Jalankan:

```bash
python cek_instagram_gui.py
```

---

## 📷 3. Cara Menggunakan Aplikasinya

1. Klik tombol **"Mulai Cek Followers"**▶️
2. Pilih file `followers_1.json`
3. Pilih file `following.json`
4. Hasil akan muncul langsung di layar dalam bentuk daftar username dengan link profilnya

---

## 💻 Tampilan Aplikasi

> Antarmuka ringan dan mudah dibaca, menggunakan `Tkinter`. Tidak perlu install library tambahan.

---

## 🔧 Buat Versi .EXE (opsional)

Kalau ingin menjadikan aplikasi ini `.exe`, kamu bisa gunakan PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed cek_instagram_gui.py
```

Hasilnya ada di folder `dist/`.

---

## 📄 Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pribadi atau pembelajaran.
