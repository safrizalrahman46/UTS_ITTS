harga_sepeda_motor = 2000
harga_mobil = 5000
harga_bus = 10000
total_pendapatan = 0
max_attempts = 3

login_data = [
    ['cakboyo', 'pangerantampan'],
    ['konoba', 'selaludihati'],
    ['cakjukir', 'ahlinyaahli']
]

Parkir = [
    ['LantaiSatuS', 'A,B,C,D,E,F,G,H,I,J', 30, 0, harga_sepeda_motor, {}],
    ['LantaiSatuM', 'A,B,C,D,E,F,G,H,I,J', 60, 0, harga_mobil, {}],
    ['LantaiDuaS', 'A,B,C', 27, 0, harga_sepeda_motor, {}],
    ['LantaiDuaM', 'D,E,F,G,H,I,J', 63, 0, harga_mobil, {}],
    ['LantaiTigaS', 'A,B,C,D,E,F,G,H,I,J', 30, 0, harga_sepeda_motor, {}],
    ['LantaiTigaM', 'A,B,C,D,E,F,G', 42, 0, harga_mobil, {}],
    ['LantaiTigaB', 'H,I,J', 18, 0, harga_bus, {}]
]

def login():
    attempts = 0
    while attempts < max_attempts:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        for user_data in login_data:
            if username == user_data[0] and password == user_data[1]:
                return True
        print("Login gagal. Silakan coba lagi.")
        attempts += 1
    print("Anda sudah melebihi batas percobaan login. Program berhenti.")
    return False

def park_vehicle():
    jenis_kendaraan = input("Jenis kendaraan (sepeda motor, mobil, bus): ")
    plat_nomor = input("Masukkan plat nomor kendaraan: ")

    if jenis_kendaraan.lower() == "mobil":
        park_mobil(plat_nomor)
    elif jenis_kendaraan.lower() == "sepeda motor":
        park_sepeda_motor(plat_nomor)
    elif jenis_kendaraan.lower() == "bus":
        park_bus(plat_nomor)
    else:
        print("Jenis kendaraan tidak valid.")

def park_mobil(plat_nomor):
    for floor in reversed(Parkir[-3:]):
        if floor[3] < floor[2]:
            park(plat_nomor, floor)
            return
    print("Maaf, parkiran mobil penuh.")

def park_sepeda_motor(plat_nomor):
    for floor in Parkir[:3]:
        if floor[3] < floor[2]:
            park(plat_nomor, floor)
            return
    print("Maaf, parkiran sepeda motor penuh.")

def park_bus(plat_nomor):
    floor = Parkir[-1]
    if floor[3] < floor[2]:
        park(plat_nomor, floor)
    else:
        print("Maaf, parkiran bus penuh.")

def park(plat_nomor, floor):
    koordinat = find_empty_coordinate(floor[1], floor[5], floor[0][-1])
    floor[5][koordinat] = plat_nomor
    floor[3] += 1
    print(f"Kendaraan dengan plat nomor {plat_nomor} parkir di {floor[0]} koordinat {koordinat}.")

def find_empty_coordinate(available_coordinates, occupied_coordinates, lantai):
    available_coords = available_coordinates.split(',')
    for coord in available_coords:
        full_coord = f"{coord}{lantai}"  # Menambahkan lantai ke koordinat
        if full_coord not in occupied_coordinates:
            return full_coord
    return None

def report():
    total_sepeda_motor = sum(floor[3] for floor in Parkir[:3])
    total_mobil = sum(floor[3] for floor in Parkir[1:4])
    total_bus = Parkir[-1][3]

    print(f"Total sepeda motor: {total_sepeda_motor}")
    print(f"Total mobil: {total_mobil}")
    print(f"Total bus: {total_bus}")

    total_pendapatan = calculate_total_pendapatan()
    print(f"Total pendapatan: Rp. {total_pendapatan}")

def calculate_total_pendapatan():
    total = 0
    for floor in Parkir:
        total += floor[3] * floor[4]
    return total

def find_vehicle_position(plat_nomor):
    for floor in Parkir:
        if plat_nomor in floor[5].values():
            for koordinat, nomor_plat in floor[5].items():
                if nomor_plat == plat_nomor:
                    print(f"Kendaraan dengan plat nomor {plat_nomor} parkir di {floor[0]} koordinat {koordinat}.")
                    return
    print(f"Kendaraan dengan plat nomor {plat_nomor} tidak ditemukan di parkiran.")

def check_parkiran_full():
    for floor in Parkir:
        if floor[3] < floor[2]:
            print(f"Parkiran {floor[0]} belum penuh untuk jenis kendaraan ini.")
        else:
            print(f"Parkiran {floor[0]} penuh untuk jenis kendaraan ini.")

def cek_koordinat_plat():
    plat_nomor = input("Masukkan plat nomor kendaraan: ")
    find_vehicle_position(plat_nomor)

def main():
    if login():
        while True:
            print("\nMenu:")
            print("1. Parkir kendaraan")
            print("2. Laporan")
            print("3. Cari posisi kendaraan")
            print("4. Cek parkiran penuh")
            print("5. Cek koordinat plat")
            print("6. Keluar")
            
            choice = input("Pilih menu (1/2/3/4/5/6): ")

            if choice == "1":
                park_vehicle()
            elif choice == "2":
                report()
            elif choice == "3":
                plat_nomor = input("Masukkan plat nomor kendaraan: ")
                find_vehicle_position(plat_nomor)
            elif choice == "4":
                check_parkiran_full()
            elif choice == "5":
                cek_koordinat_plat()
            elif choice == "6":
                print("Terima kasih telah menggunakan layanan parkir.")
                break
            else:
                print("Pilihan tidak valid.")

if _ _main_ _ == "_ _main_ _":
        main()