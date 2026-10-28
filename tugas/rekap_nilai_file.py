def baca_data(nama_file):
    # lengkapi proses baca + validasi
    data_valid = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                # Bersihkan baris dan lewati baris kosong
                baris = baris.strip()
                if not baris:
                    print("Baris kosong dilewati.")
                    continue
                
                # Pisahkan NIM dan nilai
                try:
                    nim, teks_nilai = baris.split(",")
                    # Coba konversi nilai ke float
                    nilai = float(teks_nilai)
                    # Simpan record valid dalam struktur data
                    data_valid[nim] = nilai
                except (ValueError, IndexError):
                    # Tangani nilai yang tidak dapat dikonversi / format salah
                    print(f"Baris invalid dilewati/dilaporkan: {baris}")
                    continue
        return data_valid
    except FileNotFoundError:
        # Jika file tidak ditemukan, tampilkan pesan yang jelas dan program tidak crash
        print("Pesan file tidak ditemukan; program tidak crash.")
        return None

def tulis_rekap(nama_file, data):
    # lengkapi proses penulisan
    if data is None:
        return
    
    # Hitung statistik dari record valid
    if not data:
        jumlah_data = 0
        rata_rata = 0
        nilai_min = 0
        nilai_maks = 0
        lulus = 0
    else:
        list_nilai = list(data.values())
        jumlah_data = len(list_nilai)
        rata_rata = sum(list_nilai) / jumlah_data
        nilai_min = min(list_nilai)
        nilai_maks = max(list_nilai)
        # Hitung jumlah nilai minimal 60 sebagai lulus
        lulus = sum(1 for nilai in list_nilai if nilai >= 60)
    
    # Tulis ringkasan ke data/hasil_rekap.txt
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_min}\n")
        file.write(f"Nilai maksimum: {nilai_maks}\n")
        file.write(f"Jumlah lulus: {lulus}\n")
    
    # Tampilkan ringkasan proses pada terminal
    print("\n--- RINGKASAN PROSES PADA TERMINAL ---")
    print(f"Jumlah data valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Nilai minimum: {nilai_min}")
    print(f"Nilai maksimum: {nilai_maks}")
    print(f"Jumlah lulus: {lulus}")
    print(f"Rekap berhasil ditulis ke {nama_file}\n")

input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

# jalankan alur utama
print("=== Memulai Proses Baca Data ===")
mahasiswa_valid = baca_data(input_file)

print("\n=== Memulai Proses Tulis Rekap ===")
tulis_rekap(output_file, mahasiswa_valid)