class Parkir:

    def __init__(self):
        self.data_login = {'cakboyo': 'pangerantampan', 'konoha': 'selaludihati', 'cakjukir': 'ahlinyaahli'}
        self.max_login_attempts = 3
        self.parkiran = {
            'lantai1S': {'sepeda_motor': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 'mobil': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']},
            'lantai1M': {'sepeda_motor': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 'mobil': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']},
            'lantai2S': {'sepeda_motor': ['A', 'B', 'C'], 'mobil': ['A', 'B', 'C']},
            'lantai2M': {'sepeda_motor': ['D', 'E', 'F', 'G', 'H', 'I', 'J'], 'mobil': ['D', 'E', 'F', 'G', 'H', 'I', 'J']},
            'lantai3S': {'sepeda_motor': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 'mobil': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 'bus': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']},
            'lantai3M': {'sepeda_motor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'mobil': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'bus': ['A', 'B', 'C', 'D', 'E', 'F', 'G']},
            'lantai3B': {'sepeda_motor': ['H', 'I', 'J'], 'mobil': ['H', 'I', 'J'], 'bus': ['H', 'I', 'J']}
        }
        self.tarif = {'sepeda_motor': 2000, 'mobil': 5000, 'bus': 10000}
        self.kapasitas_per_lantai = {'sepeda_motor': [30, 27, 30], 'mobil': [60, 63, 42], 'bus': [0, 0, 18]}
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
        jenis_kendaraan = input("Masukkan jenis kendaraan (sepeda motor, mobil, bus): ")
        plat_nomor = input("Masukkan plat nomor kendaraan: ")

        if jenis_kendaraan in self.kapasitas_per_lantai:
            self.parkir(jenis_kendaraan, plat_nomor)
        else:
            print("Jenis kendaraan tidak valid.")
            
        
    # def parkir(self, jenis_kendaraan, plat_nomor, lantai_nomor):
    #     for lantai in ['lantai3', 'lantai2', 'lantai1']:
    #     lantai_nomor = int(lantai[-1])  # Convert the last character to an integer
    #     if len(self.parkiran[lantai][jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][lantai_nomor - 1]:
    #         self.parkiran[lantai][jenis_kendaraan].append(plat_nomor)
    #         print(f"{jenis_kendaraan.capitalize()} dengan plat nomor {plat_nomor} parkir di {lantai}.")
    #     return

    # print(f"Parkiran {jenis_kendaraan} penuh.")


    def parkir(self, jenis_kendaraan, plat_nomor):
        for lantai in ['lantai3', 'lantai2', 'lantai1']:
            lantai_nomor = int(lantai[-1])  # Convert the last character to an integer
            if len(self.parkiran[lantai][jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][lantai_nomor - 1]:
                self.parkiran[lantai][jenis_kendaraan].append(plat_nomor)
            print(f"{jenis_kendaraan.capitalize()} dengan plat nomor {plat_nomor} parkir di {lantai}.")
            return
    
        
        print(f"Parkiran {jenis_kendaraan} penuh.")
            # lantai = int(lantai[-1])
            # if len(self.parkiran[lantai][jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][lantai[-1] - '1']:
            #     self.parkiran[lantai][jenis_kendaraan].append(plat_nomor)
            #     print(f"{jenis_kendaraan.capitalize()} dengan plat nomor {plat_nomor} parkir di {lantai}.")
            #     return


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
                if jenis_kendaraan in lantai:
                    total += len(lantai[jenis_kendaraan])
            return total

    # def hitung_total_kendaraan(self, jenis_kendaraan):
    #     total = 0
    #     for lantai in self.parkiran.values():
    #         total += len(lantai[jenis_kendaraan])
    #     return total

    def cari_posisi_kendaraan(self, plat_nomor):
        for lantai, area in self.parkiran.items():
            for jenis_kendaraan, kendaraan in area.items():
                if plat_nomor in kendaraan:
                    print(f"Kendaraan dengan plat nomor {plat_nomor} berada di lantai {lantai}, area {jenis_kendaraan}.")

    def parkiran_tersedia(self, jenis_kendaraan):
        for lantai, area in self.parkiran.items():
            if jenis_kendaraan in area:
                lantai_nomor = lantai[-1]
                if lantai_nomor.isdigit() and len(area[jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][int(lantai_nomor) - 1]:
                    return True
        # for lantai, area in self.parkiran.items():
        #     if jenis_kendaraan in area and len(area[jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][int(lantai[-1]) - 1]:
        #         return True
        return False

    
    # def parkiran_tersedia(self, jenis_kendaraan):
    #     for lantai in self.parkiran.values():
    #         if len(lantai[jenis_kendaraan]) < self.kapasitas_per_lantai[jenis_kendaraan][lantai[-1] - '1']:
    #             return True
    #     return False

    def run_program(self):
        if self.login():
            self.parkir_kendaraan()
            self.laporan()


if __name__ == "__main__":
    program_parkir = Parkir()
    program_parkir.run_program()
