from Animal import *

class ular(Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design= design
        self.racun= racun 

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t: ", self.design,
        "\nRacun \t\t\t : ", self.racun) 

anaconda = ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Jawa", "Tidak Berbisa")
anaconda.cetak_ular() 


from Animal import *

class ular(Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.nama = nama
        self.makanan = makanan 
        self.hidup = hidup 
        self.berkembang_biak = berkembang_biak 
        self.design= design
        self.racun= racun 

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t: ", self.design,
        "\nRacun \t\t\t : ", self.racun) 

cobra = ular("Cobra", "Kerbau", "Amazon", "Bertelur", "Batik madura", "Berbisa")
cobra.cetak_ular()
