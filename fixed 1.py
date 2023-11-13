#perulangan
from typing import Self

harga_sepeda_motor = 2000
harga_mobil = 5000
harga_bus = 10000
total_pendapatan = 0
masuk = 1
keluar = 2

Parkir = [['LantaiSatuS','A,B,C,D,E,F,G,H,I,J', 30,0, 2000],
              ['LantaiSatuM','A,B,C,D,E,F,G,H,I,J', 60,0,5000],
              ['LantaiDuaS','A,B,C', 27,0,2000],
              ['LantaiDuaM','D,E,F,G,H,I,J', 63,0,5000],
              ['LantaiTigaS','A,B,C,D,E,F,G,H,I,J', 30,0,2000],
              ['LantaiTigaM','A,B,C,D,E,F,G', 42,5000],
              ['LantaiTigaB','H,I,J', 18, 10000]]

user = "konoha"
password = "selaludihati"
login = False
#password benar
print(">>>>>SELAMAT DATANG DIPARKIRAN CAK BOYO<<<<<")
while login == False :
        inuser = input("Silahkan masukkan user :")
        inpass = input("Silahkan masukkan password :")
        if inuser == user and inpass == password:
            login = True
            print ("password benar, silahkan masuk")
        else : 
            print ("password salah, coba lagi")
            print("======================================")

print("Tekan 1 untuk masuk dan tekan 2 untuk keluar")
pilihan = int(input("Masukkan pilihan : "))
if pilihan == 1 :
    print('''Pilihan jenis_kendaraan: 
      1. Mobil
      2. Sepedah Motor
      3. bus
      note : ketik 0 untuk exit
      ''')
    jenis_kendaraan = input("Jenis kendaraan : ")


    jumlah = 0
    if jenis_kendaraan == "1":
        jumlah = int(input("jumlah kendaraan masuk: "))
        if jumlah <= Parkir[1][2]:
            total = jumlah*Parkir[1][4]
            Parkir[1][3] += jumlah
            Parkir[1][2] += Parkir[1][2] - Parkir[1][3]
            print('total yang harus dibayarkan adalah Rp.', total)
        elif jumlah > Parkir[1][2]:
            print ('maaf, parkiran penuh', Parkir[1][11])
        else :
            Parkir[1][11] == 0
            print('maaf, sudah habis')
    else:
        print("Jenis kendaraan tidak valid.")        
else:
    print("terima kasih telah menggunakan jasa kami. silakan keluar.")

