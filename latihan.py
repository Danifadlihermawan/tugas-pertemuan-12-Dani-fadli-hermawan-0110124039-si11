class latihan: 
    
    def __init__(self, nama, gender, umur):
      self.nama = nama 
      self.gender = gender 
      self.umur = umur 

    def cetak(self):
       super().cetak ()
       print("Nama \t\t :",self.nama,
             "\nJenis kelamin \t :",self.gender,
             "\numur \t\t :",self.umur) 