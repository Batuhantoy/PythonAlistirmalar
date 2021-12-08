import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses ="0",kanal_listesi=["Trt"],şuankikanal = "Trt"):
        self.tv_durum= tv_durum
        self.tv_ses=int(tv_ses)
        self.kanal_listesi=kanal_listesi
        self.şuankikanal=şuankikanal

    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum="Açık"
    def tv_kapa(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum="Kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış: 'q'\n")

            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses: ",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses güncellendi: ",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("{} kanalı eklendi".format(kanal_ismi))
    def rasgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.şuankikanal= self.kanal_listesi[rastgele]
        print("Şuanki kanal: ",self.şuankikanal)
    def kanal_seç(self):
        print(kanal_listesi)
        seçilen_kanal = input("İzlemek istediginiz kanalın ismini yazınız: ")
        if(seçilen_kanal in kanal_listesi):
            self.şuankikanal = seçilen_kanal
        else:
            print("Kanal listenizde bu kanal yok")
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞuanki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.şuankikanal)

print("""
Televizyon Uygulaması

1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Ögrenme
6. Rastgele Kanala Geçme
7. Kanal Degiştir
8. Tv Bilgileri

Çıkmak için 'q' ya basın.
""")
kumanda = Kumanda()
while True:
    işlem = input("İşlemi seçiniz: ")
    if(işlem=="q"):
        print("Program Sonlandırılıyor")
        break
    elif(işlem=="1"):
        kumanda.tv_ac()
    elif(işlem=="2"):
        kumanda.tv_kapa()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(işlem=="5"):
        print("Kanal Sayısı: ",len(kumanda))
    elif(işlem=="6"):
        kumanda.rasgele_kanal()
    elif(işlem=="7"):
        kumanda.kanal_seç()
    elif (işlem == "8"):
        print(kumanda)
    else:
        print("Geçersiz İşlem...")



