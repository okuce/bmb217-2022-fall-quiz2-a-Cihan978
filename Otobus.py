"""Esat Cihan Özgültekin"""
"""20217170028"""

class Otobus:
    nereden:str=""
    nereye:str=""
    plaka:str=""
    dolu_koltuk:int=0
    
    def__init__(self,plaka,nereden,nereye,dolu_koltuk) :
       self.plaka=plaka
       self.nereden=nereden
       self.nereye=nereye
       self._dolu_koltuk=dolu_koltuk

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        self.dolu_koltuk=self.dolu_koltuk+1
        return self.dolu_koltuk


    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        self.dolu_koltuk=self.dolu_koltuk-1
        return self.dolu_koltuk



    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("Otobüs güzergahi:{}{},Plaka:{} ,Dolu Koltuk:{} ",format(self.nereden,self.nereye,self.plaka,self.dolu_koltuk))
