# Pertemuan 12 - File I/O dan Error Handling

Nama: Alya Mutiara Marine
NIM: 2225250224
Kelas: 3A

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM,nilai

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case
Catat kondisi, hasil yang diharapkan, hasil aktual, dan status.

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| **Normal** (Semua baris valid) | Semua record diproses dan rekap benar. | Record valid sukses dihitung (Rata-rata: 83.40, Lulus: 5). | Sukses |
| **File hilang** (nilai.txt tidak tersedia) | Pesan file tidak ditemukan; program tidak crash. | Menampilkan `"Pesan file tidak ditemukan; program tidak crash."` | Sukses |
| **Nilai invalid** (A004,abc) | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Menampilkan `"Baris invalid dilewati/dilaporkan: A004,abc"` | Sukses |
| **Baris kosong** (Ada baris kosong) | Baris kosong dilewati. | Menampilkan `"Baris kosong dilewati."` | Sukses |
| **Batas lulus** (Nilai 60) | Dihitung sebagai lulus. | Semua data nilai $\geq 60$ sukses disaring masuk ke jumlah lulus. | Sukses |

## Refleksi
Jelaskan satu error yang ditemukan dan cara program menanganinya.
- **Error yang ditemukan:** `ValueError` saat mencoba mengonversi data string huruf (`'abc'`) menjadi tipe data desimal angka menggunakan perintah `float()` pada Latihan 4. Hal ini menyebabkan program mengalami *crash* terhenti di tengah jalan.
- **Cara program menanganinya:** Menggunakan struktur blok penanganan `try-except` (`except ValueError:`). Dengan blok ini, program tidak akan *crash* melainkan langsung melompati baris yang rusak tersebut, memunculkan laporan pemberitahuan di terminal, lalu melanjutkan pemrosesan baris-baris data berikutnya sampai selesai dengan aman.