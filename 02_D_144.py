print ("============================")
print("=  NAMA : AIZA FRAVY QANZA =")
print("=  NIM  : L200170144       =")
print("=  MODUL: 2                =")
print("=  KELAS: D                =")
print("=============================")



from datetime import date
print ("==============================NOMER 1 ==============================")
#No. 1
class Pesan(object):
    def __init__(self, kata):
        self.kata = kata

    def apakahTerkandung(self, yo):
        if yo in self.kata:
            return True
        else:
            return False
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        kon = len(self.kata) - v
        return kon
    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        return v
#A    
p9 = Pesan("Indonesia adalah negeri yang indah")
p10 = Pesan("Surakarta")
print(p9.apakahTerkandung("ege"))
print(p9.apakahTerkandung("eka"))
#B
p10 = Pesan("Surakarta")
print(p10.hitungKonsonan())
#C
print(p10.hitungVokal())

print ("==============================NOMER 2 ==============================")
#No 2
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Manusia"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    
    def ambilUangSaku(self):
        return self.us

    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
        
    def ambilKotaTinggal(self):
        return self.kota
    
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
        
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
m2 = Mahasiswa('Andi', 365, 'Magelang', 275000)
m3 = Mahasiswa('Sri', 676, 'Yogyakarta', 240000)

#A
print (m1.ambilKotaTinggal())
#B
print (m1.perbaruiKotaTinggal("Sleman"))
print (m1.ambilKotaTinggal())
#C
print (m2.ambilUangSaku())
print (m2.tambahUangSaku(50000))
print (m2.ambilUangSaku())

print ("==============================NOMER 3 ==============================")
#No 3
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Manusia"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

#start
a = input("Masukkan nama: ")
b = input("Masukkan nim: ")
c = input("Masukkan kota tinggal: ")
d = input("Masukkan uang saku: ")

x = Mahasiswa(a,b,c,d)
#end

print (x)

print ("==============================NOMER 4 & 5 ==============================")

#No 4, 5
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Manusia"""

    def __init__(self, nama, NIM, kota, us, lk = []):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listKuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

    #No.4
    def ambilKuliah(self, ambil):
        self.listKuliah.append(ambil)

    #No.5
    def hapusListKuliah(self, hapus):
        for x in self.listKuliah:
            if hapus in self.listKuliah:
                self.listKuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")

m1 = Mahasiswa('Bella', 157, 'Jakarta', 250000)
m2 = Mahasiswa('Aiza', 158, 'Samarinda', 275000)
m3 = Mahasiswa('Shafira', 159, 'Bandung', 240000)
print (m1.listKuliah)
m1.ambilKuliah("Matematika Diskrit")
print (m1.listKuliah)
m1.ambilKuliah("Algoritma dan struktur data")
print (m1.listKuliah)
print (m2.hapusListKuliah)

print ("==============================NOMER 6 ==============================")
#No. 6
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = NIS
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl

print ("==============================NOMER 7 ==============================")
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')

##Dari class Manusia:
##    1. nama
##    2. keadaan
##    3. ucapkanSalam
##    4. makan
##    5. olahraga
##    6. mengalikanDenganDua
##
##Dari class Mahasiswa:
##    1. NIM
##    2. kotaTinggal
##    3. uangsaku
##    4. ambilNama
##    5. ambilNIM
##    6. ambilUangSaku
##    7. makan
##    8. ambilKotaTinggal
##    9. perbaruiKotaTinggal
##    10. tambahUangSaku
##    11. listKuliah
##    12. ambilKuliah
##    13. hapusKuliah
##
##Dari class MhsTIF:
##    1. katakanpy
