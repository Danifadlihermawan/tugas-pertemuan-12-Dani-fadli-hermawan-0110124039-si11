from Animal import *

class ikan (Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design, ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design= design
        

    def cetak_ikan(self):
        super().cetak()
        print("Design \t: ", self.design,)
        

cupang = ikan("Cupang", "pelet", "Kolam Ikan", "Bertelur", "Corak Merah Putih")
cupang.cetak_ikan() 


from Animal import *

class ikan (Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design, ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design= design
        

    def cetak_ikan(self):
        super().cetak()
        print("Design \t: ", self.design,)
        

koi = ikan("Koi", "pelet", "Kolam Ikan", "Bertelur", "Corak belang oren")
koi.cetak_ikan()