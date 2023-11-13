class Parkir:
    
    def __init__(self):
        self.data_login = {'cakboyo': 'pangerantampan', 'konoha': 'selaludihati', 'cakjukir': 'ahlinyaahli'}
        self.max_login_attempts = 3
        self.parkiran = {'lantai1': {'sepeda_motor': [], 'mobil': []},
                         'lantai2': {'sepeda_motor': [], 'mobil': []},
                         'lantai3': {'sepeda_motor': [], 'mobil': [], 'bus': []}}
        self.tarif = {'sepeda_motor': 2000, 'mobil': 5000, 'bus': 10000}
        self.total_pendapatan = 0

    def login(self):
        attempts = 0
        while attempts < self.max_login_attempts:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if self.check_login(username, password):
                username = "konoha"
                password = "selaludihati"
                print("Login berhasil!")
                return True
            else:
                attempts += 1
                print("Login gagal. Coba lagi.")

        print("Anda melebihi batas percobaan login. Program berhenti.")
        return False

    def check_login(self, username, password):
        return self.data_login.get(username) == password

    def parkir_kendaraan(self):
        jenis_kendaraan = input("Masukkan jenis kendaraan (sepeda_motor, mobil, bus): ")
        plat_nomor = input("Masukkan plat nomor kendaraan: ")

        if jenis_kendaraan == 'mobil':
            self.parkir_mobil(plat_nomor)
        elif jenis_kendaraan == 'sepeda_motor':
            self.parkir_sepeda_motor(plat_nomor)
        elif jenis_kendaraan == 'bus':
            self.parkir_bus(plat_nomor)
        else:
            print("Jenis kendaraan tidak valid.")

    def parkir_mobil(self, plat_nomor):
        if len(self.parkiran['lantai3']['mobil']) < 63:
            self.parkiran['lantai3']['mobil'].append(plat_nomor)
        elif len(self.parkiran['lantai2']['mobil']) < 63:
            self.parkiran['lantai2']['mobil'].append(plat_nomor)
        elif len(self.parkiran['lantai1']['mobil']) < 60:
            self.parkiran['lantai1']['mobil'].append(plat_nomor)
        else:
            print("Parkiran mobil penuh.")

    def parkir_sepeda_motor(self, plat_nomor):
        if len(self.parkiran['lantai1']['sepeda_motor']) < 30:
            self.parkiran['lantai1']['sepeda_motor'].append(plat_nomor)
        elif len(self.parkiran['lantai2']['sepeda_motor']) < 27:
            self.parkiran['lantai2']['sepeda_motor'].append(plat_nomor)
        elif len(self.parkiran['lantai3']['sepeda_motor']) < 30:
            self.parkiran['lantai3']['sepeda_motor'].append(plat_nomor)
        else:
            print("Parkiran sepeda motor penuh.")

    def parkir_bus(self, plat_nomor):
        if len(self.parkiran['lantai3']['bus']) < 18:
            self.parkiran['lantai3']['bus'].append(plat_nomor)
        else:
            print("Parkiran bus penuh.")

    def laporan(self):
        print("Laporan Hari Ini:")
        print("Total sepeda motor:", self.hitung_total_kendaraan('sepeda_motor'))
        print("Total mobil:", self.hitung_total_kendaraan('mobil'))
        print("Total bus:", self.hitung_total_kendaraan('bus'))
        print("Total pendapatan:", self.total_pendapatan)
        
        plat_nomor = input("Masukkan plat nomor kendaraan: ")
        self.cari_posisi_kendaraan(plat_nomor)

        jenis_kendaraan = input("Masukkan jenis kendaraan (sepeda_motor, mobil, bus): ")
        if self.parkiran_tersedia(jenis_kendaraan):
            print(f"Parkiran {jenis_kendaraan} masih tersedia.")
        else:
            print(f"Parkiran {jenis_kendaraan} penuh.")

    def hitung_total_kendaraan(self, jenis_kendaraan):
        total = 0
        for lantai in self.parkiran.values():
            total += len(lantai[jenis_kendaraan])
        return total

    def cari_posisi_kendaraan(self, plat_nomor):
        for lantai, area in self.parkiran.items():
            for jenis_kendaraan, kendaraan in area.items():
                if plat_nomor in kendaraan:
                    print(f"Kendaraan dengan plat nomor {plat_nomor} berada di lantai {lantai}, area {jenis_kendaraan}.")

    def parkiran_tersedia(self, jenis_kendaraan):
        for lantai in self.parkiran.values():
            if len(lantai[jenis_kendaraan]) < self.kapasitas_per_lantai:
                return True
        return False

    def run_program(self):
        if self.login():
            self.parkir_kendaraan()
            self.laporan()


if __name__ == "__main__":
    program_parkir = Parkir()
    program_parkir.run_program()
