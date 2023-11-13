# Import library yang dibutuhkan
import random

# Deklarasi variabel
data_login = {"cakboyo": "pangerantampan", "konoha": "selaludihati", "cakjukir": "ahlinyaahli"}

# Deklarasi variabel parkiran
parkir_sepeda_motor = {
    1: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    2: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    3: ["A", "B", "C"],
}

parkir_mobil = {
    1: ["A", "B", "C"],
    2: ["D", "E", "F", "G", "H", "I", "J"],
    3: ["H", "I", "J"],
}

parkir_bus = {
    1: ["H", "I", "J"],
}

# Inisialisasi daftar parkiran
parkiran = {"sepeda motor": [], "mobil": [], "bus": []}

# Fungsi untuk melakukan login
def login():
    # Ulangi login hingga 3 kali
    for i in range(3):
        # Input username dan password
        username = input("Username: ")
        password = input("Password: ")

        # Cek apakah data login valid
        if username in data_login and data_login[username] == password:
            return username

        # Jika data login tidak valid, tampilkan pesan kesalahan
        else:
            print("Username atau password salah.")

    print("Anda telah melebihi batas login.")
    return None

# Fungsi untuk menentukan lantai parkir
def tentukan_lantai(jenis_kendaraan, plat_nomor):
    # Jika jenis kendaraan adalah sepeda motor
    if jenis_kendaraan == "sepeda motor":
        return 1 if len(parkir_sepeda_motor[1]) > 0 else 2 if len(parkir_sepeda_motor[2]) > 0 else 3
    # Jika jenis kendaraan adalah mobil
    elif jenis_kendaraan == "mobil":
        return 3 if len(parkir_mobil[3]) > 0 else 2 if len(parkir_mobil[2]) > 0 else 1
    # Jika jenis kendaraan adalah bus
    else:
        return 3

# Fungsi untuk mengisi parkiran
def isi_parkiran(jenis_kendaraan, plat_nomor, lantai):
    # Jika jenis kendaraan adalah sepeda motor
    if jenis_kendaraan == "sepeda motor":
        koordinat = random.choice(parkir_sepeda_motor[lantai])
        parkir_sepeda_motor[lantai].remove(koordinat)
        parkiran["sepeda motor"].append((plat_nomor, koordinat))
    # Jika jenis kendaraan adalah mobil
    elif jenis_kendaraan == "mobil":
        koordinat = random.choice(parkir_mobil[lantai])
        parkir_mobil[lantai].remove(koordinat)
        parkiran["mobil"].append((plat_nomor, koordinat))
        
    # elif jenis_kendaraan == "bus":
    #     koordinat = random.choice(parkir_bus[lantai])
    #     parkir_mobil[lantai].remove(koordinat)
    #     parkiran["bus"].append((plat_nomor, koordinat))

# Fungsi untuk menampilkan laporan parkiran
def laporan_parkiran():
    print("Laporan Parkiran:")
    for jenis_kendaraan, data_kendaraan in parkiran.items():
        print(f"Jenis Kendaraan: {jenis_kendaraan}")
        for plat_nomor, koordinat in data_kendaraan:
            print(f"Plat Nomor: {plat_nomor}, Koordinat: {koordinat}")

# Fungsi untuk menjalankan program
def run_program():
    username = login()
    if username:
        jenis_kendaraan = input("Masukkan jenis kendaraan (sepeda motor, mobil, bus): ")
        plat_nomor = input("Masukkan plat nomor kendaraan: ")

        # Tentukan lantai parkir
        lantai = tentukan_lantai(jenis_kendaraan, plat_nomor)

        # Isi parkiran
        isi_parkiran(jenis_kendaraan, plat_nomor, lantai)

        # Tampilkan laporan parkiran
        laporan_parkiran()

# Menjalankan program
run_program()
