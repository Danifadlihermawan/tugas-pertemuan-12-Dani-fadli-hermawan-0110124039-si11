from Animal import *

class burung (Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design= design
        

    def cetak_burung(self):
        super().cetak()
        print("Design \t\t\t: ", self.design,)
    

merpati = burung("Merpati", "jagung", "Udara", "Bertelur", "Bulu Halus")
merpati.cetak_burung()  


from Animal import *

class burung (Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, design):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design= design
        

    def cetak_burung(self):
        super().cetak()
        print("Design \t\t\t: ", self.design,)
    

gagak = burung("Gagak", "jagung", "Udara", "Bertelur", "Bulu corak merah maroon")
gagak.cetak_burung() 