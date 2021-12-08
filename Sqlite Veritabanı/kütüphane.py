import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı

    def __str__(self):
        return "Kitap ismi : {}\nYazar : {}\nYayınevi : {}\nTür : {}\nBaskı : {}\n"\
            .format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)

class Kütüphane():
    def __init__(self):
        self.baglantı_olustur()
    def baglantı_olustur(self):
        self.baglantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglantı.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def baglantıyı_kes(self):
        self.baglantı.close()

    def kitapları_göster(self):
        sorgu = "Select * from kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Kütüphanede hiçbir kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_sorgula(self,isim):
        sorgu = "Select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar)==0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))
        self.baglantı.commit()

    def kitap_sil(self,sütun,seçilen):
        sorgu = "Delete from kitaplar where {}=?".format(sütun)
        self.cursor.execute(sorgu,(seçilen,))
        self.baglantı.commit()

    def baskı_yükselt(self,isim):
        sorgu = "Select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar)==0):
            return print("Böyle bir kitap bulunmuyor...")
        else:
            print("Baskı yükseltiliyor")
            baskı = kitaplar[0][4]
            baskı +=1
            sorgu2="Update kitaplar set baskı=? where isim=?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.baglantı.commit()
            time.sleep(1)
            print("Baskı yükseltildi")

    def kontrol(self,aranan):
        self.cursor.execute("select * from kitaplar")
        data=self.cursor.fetchall()
        sonuç = False

        for i in data:
            for a in i:
                if(str(a).lower()==str(aranan).lower()):
                    kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                    sonuç=True
                    break
        else:
            print("Böyle bir kitap bulunamadı")

        while (sonuç==True):
            print(kitap)
            seçilen = input("Hangisini degiştirmek istersiniz ?\n") #Mavi
            if(seçilen==kitap.isim):
                sütun = "isim"
            elif (seçilen == kitap.yazar):
                sütun = "yazar"
            elif (seçilen == kitap.yayınevi):
                sütun = "yayınevi"                                 #sütun==yayınevi oldu
            elif (seçilen == kitap.tür):
                sütun = "tür"
            elif (int(seçilen) == kitap.baskı):
                sütun = "baskı"
            işlem = input("""
            Hangi işlemi yapmak istersiniz                            

            1. Güncelle
            2. Sil""")

            if (işlem == "1"):
                yenideger = input("Yeni deger : ")                 #yenideger =Kırmızı olsun
                if(sütun=="baskı"):
                    yenideger = int(yenideger)
                sorgu = "update kitaplar set {}=? where {}=?".format(sütun,sütun)
                self.cursor.execute(sorgu, (yenideger,seçilen))
                self.baglantı.commit()
            elif (işlem == "2"):
                self.kitap_sil(sütun,seçilen)

            sonuç=input("Başka degişim işlemi yapacakmısınız? (E/H)")
            if(sonuç=="H"):
                break