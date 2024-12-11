from latihan import *

class mahasiswa(latihan):
    prodi = ""
    semester = 0
    def _init_(self, nama, gender, umur, prodi, semester):
        super()._init_(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
    
    def cetak(self):
        super().cetak()
        print("prodi \t\t:", self.prodi,
              "\nsemester \t:", self.semester,
              "\n---------------")