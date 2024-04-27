#Nama : Mikha Naftali
#NIM  : 41823010047
#Matkul : Pemprograman Lanjut

print("Selamat Datang Di Aplikasi Perhitungan Nilai Mahasiswa")

tugas=int(input("Masukan Nilai Tugas Anda\n:"))
uts=int(input("Masukan Nilai UTS Anda\n:"))
uas=int(input("Masukan Nilai UAS Anda\n:"))
nilai=(0.25*tugas) + (0.35*uts) + (0.4*uas)
print("Nilai akhir anda adalah :",nilai)

if nilai >= 85:
    print("Dalam Huruf A")
elif nilai >= 80 and nilai < 85:
    print("Dalam Huruf A-")
elif nilai >= 75 and nilai < 80:
    print("Dalam Huruf B+")
elif nilai >= 70 and nilai < 75:
    print("Dalam Huruf B")
elif nilai >= 65 and nilai < 70:
    print("Dalam Huruf B-")
elif nilai >= 60 and nilai < 65:
    print("Dalam Huruf C+")
elif nilai >= 55 and nilai < 60:
    print("Dalam Huruf C")
elif nilai >= 50 and nilai < 55:
    print("Dalam Huruf C-")
elif nilai >= 30 and nilai < 50:
    print("Dalam Huruf D")
elif nilai <=30:
    print("Anda mendapat niai E Dan tidak lulus Mata kuliah ini")
else:
    print("Masukan Nilai dengan benar")


    