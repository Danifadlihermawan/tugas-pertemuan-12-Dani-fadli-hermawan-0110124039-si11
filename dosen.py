from latihan import *

class dosen(latihan):
    gelar = ""
    jabatan = ""
    gaji = 0

    def _init_(self, nama, gender, umur, gelar, jabatan):
        super()._init_(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    def setgaji(self, uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print("gelar \t\t:", self.gelar,
              "\njabatan \t:", self.jabatan,
              "\ngaji \t\t:", self.gaji,
              "\n---------------") 