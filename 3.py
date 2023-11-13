# Import library yang dibutuhkan
import random

# Deklarasi variabel
data_login = [["cakboyo", "pangerantampan"], ["konoha", "selaludihati"], ["cakjukir", "ahlinyaahli"]]

# Fungsi untuk melakukan login
def login():
    # Ulangi login hingga 3 kali
    for i in range(3):
        # Input username dan password
        username = input("Username: ")
        password = input("Password: ")

        # Cek apakah data login valid
        if username in data_login and data_login[username][1] == password:
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
        # Jika lantai 1 masih ada tempat parkir, maka parkir di lantai 1
        if len(parkir_sepeda_motor[0]) > 0:
            return 1
        # Jika lantai 2 masih ada tempat parkir, maka parkir di lantai 2
        elif len(parkir_sepeda_motor[1]) > 0:
            return 2
        # Jika lantai 3 masih ada tempat parkir, maka parkir di lantai 3
        else:
            return 3

    # Jika jenis kendaraan adalah mobil
    elif jenis_kendaraan == "mobil":
        # Jika lantai 3 masih ada tempat parkir, maka parkir di lantai 3
        if len(parkir_mobil[0]) > 0:
            return 3
        # Jika lantai 2 masih ada tempat parkir, maka parkir di lantai 2
        elif len(parkir_mobil[1]) > 0:
            return 2
        # Jika lantai 1 masih ada tempat parkir, maka parkir di lantai 1
        else:
            return 1

    # Jika jenis kendaraan adalah bus
    else:
        return 3

# Fungsi untuk mengisi parkiran
def isi_parkiran(jenis_kendaraan, plat_nomor, lantai):
    # Jika jenis kendaraan adalah sepeda motor
    if jenis_kendaraan == "sepeda motor":
        # Jika lantai yang dipilih adalah lantai 1
        if lantai == 1:
            # Cari koordinat kosong di lantai 1
            koordinat = random.choice(parkir_sepeda_motor[0])
            parkir_sepeda_motor[0].remove(koordinat)
            # Masukkan data kendaraan ke daftar parkiran
            parkiran["sepeda motor"].append((plat_nomor, koordinat))
        # Jika lantai yang dipilih adalah lantai 2
        elif lantai == 2:
            # Cari koordinat kosong di lantai 2
            koordinat = random.choice(parkir_sepeda_motor[1])
            parkir_sepeda_motor[1].remove(koordinat)
            # Masukkan data kendaraan ke daftar parkiran
            parkiran["sepeda motor"].append((plat_nomor, koordinat))
        # Jika lantai yang dipilih adalah lantai 3
        else:
            # Cari koordinat kosong di lantai 3
            koordinat = random.choice(parkir_sepeda_motor[2])
            parkir_sepeda_motor[2].remove(koordinat)
            # Masukkan data kendaraan ke daftar parkiran
            parkiran["sepeda motor"].append((plat_nomor, koordinat))

    # Jika jenis kendaraan adalah mobil
    elif jenis_kendaraan == "mobil":
        # Jika lantai yang dipilih adalah lantai 3
        if lantai == 3:
            # Cari koordinat kosong di lantai 3
            koordinat = random.choice(parkir_mobil[0])
            parkir_mobil[0].remove(koordinat)
            # Masukkan data kendaraan ke daftar parkiran
            parkiran["mobil"].append((plat_nomor, koordinat))
        # Jika lantai yang dipilih adalah lantai 2
        elif lantai == 2:
            # Cari koordinat kosong di lantai 2
            koordinat = random.choice(parkir_mobil[1])
            parkir_mobil[1].remove(koordinat)
            parkiran["mobil"].append((plat_nomor, koordinat))
            
            
            run_program()

