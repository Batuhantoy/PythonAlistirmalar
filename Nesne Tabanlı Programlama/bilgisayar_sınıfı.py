class Bilgisayar():
    def __init__(self,marka="Bilgi Yok",işlemci="Bilgi Yok",işlemcihızı="Bilgi Yok",ram="Bilgi Yok",işletim_sistemi="Bilgi Yok",durum="Kapalı",ses=0):
        self.marka=marka
        self.işlemci=işlemci
        self.işlemcihızı=işlemcihızı
        self.ram=ram
        self.işletim_sistemi=işletim_sistemi
        self.durum=durum
        self.ses=ses
        print("Bilgisayar __init__ çalıştı")
    def pc_kontrol(self,tercih):
        if(tercih=="Kapat"):
            self.durum="Kapalı"
        elif(tercih=="Aç"):
            self.durum="Açık"
        elif(tercih=="Uyku"):
            self.durum="Uykuda"
    def ses_kontrol(self,seçim):
        if(self.ses>=70 or seçim>=70):
            a=input("Kulagınıza zarar verebilir devam etmek istiyormusunuz")
            if(a=="evet"):
                self.ses=seçim
        elif(self.ses==100):
            print("Ses En yüksek seviyede")
    def __str__(self):
        return "Marka : {}\nİşlemci : {}\nİşlemci Hızı : {}\nRam : {} gb\nİşletim Sistemi : {}\nSes : {}\nDurum : {}\n"\
            .format(self.marka,self.işlemci,self.)

class bütün_bilgisayarlar(Bilgisayar):
    def __init__(self,marka="Bilgi Yok",işlemci="Bilgi Yok",işlemcihızı="Bilgi Yok",ram="Bilgi Yok",işletim_sistemi="Bilgi Yok",durum="Kapalı",ses=0):
        super().__init__(marka,işlemci,işlemcihızı,ram,işletim_sistemi,durum,ses)



