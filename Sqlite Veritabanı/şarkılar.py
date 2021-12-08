import sqlite3
import time

class Şarkı():
    def __init__(self,şarkı_ismi,şarkı_sanatçısı,albüm,prodüksiyon_şirketi,şarkı_süresi,şarkı_listesi=""):
        self.şarkı_ismi=şarkı_ismi
        self.şarkı_sanatçısı=şarkı_sanatçısı
        self.albüm=albüm
        self.prodüksiyon_şirketi=prodüksiyon_şirketi
        self.şarkı_süresi=şarkı_süresi
        self.şarkı_listesi = şarkı_listesi

    def __str__(self): #print(şarkı) deyince bu çalışıcak
        return "-------------------------------------Şarkı İsmi : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı Süresi : {}\n"\
            .format(self.şarkı_ismi,self.şarkı_sanatçısı,self.albüm,self.prodüksiyon_şirketi,self.şarkı_süresi)

class şarkı_program_kontrol():
    def __init__(self):
        self.baglantı_aç()

    def baglantı_aç(self):
        self.con = sqlite3.connect("şarkı_veritabanı.db")
        self.cursor = self.con.cursor()

        sorgu = "Create Table If not exists şarkılar (şarkı_ismi TEXT,şarkı_sanatçısı TEXT,albüm TEXT,prodüksiyon_şirketi TEXT,şarkı_süresi INT,şarkı_listesi TEXT)"
        self.cursor.execute(sorgu)
        self.con.commit()
    def baglantı_kapat(self):
        self.con.close()
    def şarkıları_göster(self):
        sorgu = "select * from şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()
        if(len(şarkılar)==0):
            print("Şarkı Bulunmuyor...")
        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
                print(şarkı)
    def şarkıları_eleyipgöster(self,seçilen_liste):
        sorgu = "select * from şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()
        temiz=[]
        for i in şarkılar:
            if(i[5]!=seçilen_liste):
               temiz.append(i)
        for i in temiz:
            şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
            print(şarkı)

    def şarkı_arama(self,aranan):
        self.cursor.execute("select * from şarkılar")
        şarkılar = self.cursor.fetchall()
        sonuç = False

        for i in şarkılar:
            for a in i:
                if(str(a).lower()==str(aranan).lower()):
                    if(str(aranan).lower() == i[5]):
                        sorgu = "select * from şarkılar where şarkı_listesi=?"
                        self.cursor.execute(sorgu,(i[5],))
                        liste = self.cursor.fetchall()
                        for i in liste:
                            şarkı = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5])
                        sonuç=True
                    else:
                        şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
                        sonuç = True
        if(sonuç==False):
            print("Aradıgınız kelimeye uygun sonuç bulunamadı")
        else:
            return şarkı

    def komut_çalıştır(self,sorgu):
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()
        for i in liste:
            print(i)
    def şarkı_ekle(self,şarkı):
        sorgu = "Insert into şarkılar Values(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(şarkı.şarkı_ismi,şarkı.şarkı_sanatçısı,şarkı.albüm,şarkı.prodüksiyon_şirketi,şarkı.şarkı_süresi,şarkı.şarkı_listesi))
        self.con.commit()
        print("Şarkı başarıyla eklendi")

    def şarkı_sil(self,silinecek):
        sorgu = "delete from şarkılar where şarkı_ismi=?"
        self.cursor.execute(sorgu,(silinecek,))
        self.con.commit()
        print("Şarkı Başarıyla Silindi")

    def toplam_şarkısüresi(self):
        toplam = 0
        seçenek = input("""
        1. Belirli bir şarkının süresini ögren
        2. Toplam Süre
        3. Şarkı Listesinin
        """)

        if(seçenek=="1"):
            self.şarkıları_göster()
            seçilen = input("Şarkı ismi : ")
            sorgu = "select şarkı_süresi from şarkılar where şarkı_ismi=?"
            self.cursor.execute(sorgu,(seçilen,))
            şarkı = self.cursor.fetchall()
            print(şarkı[0][0])
        elif(seçenek=="2"):
            sorgu = "select şarkı_süresi from şarkılar"
            self.cursor.execute(sorgu)
            süreler = self.cursor.fetchall()
            for i in süreler:
                toplam += i[0]
            print("Toplam Şarkı Süresi : ",toplam)
        elif(seçenek=="3"):
            sorgu = "select şarkı_listesi from şarkılar"
            self.cursor.execute(sorgu)
            şarkılisteleri = self.cursor.fetchall()
            a = 1
            temiz = []
            for i in şarkılisteleri:
                if(i[0] not in temiz and i[0]!=""):
                    temiz.append(i[0])
            for i in temiz:
                print("{}. {}".format(a, i[0]))
                a += 1
            seçilen = input("Hangi şarkı listesinin toplam süresini istersiniz : ")
            sorgu = "select şarkı_süresi from şarkılar where şarkı_listesi=?"
            self.cursor.execute(sorgu,(seçilen,))
            süreler = self.cursor.fetchall()
            for i in süreler:
                toplam += i[0]
            print("{} listesinin toplam süresi : {}".format(seçilen,toplam))



    def şarkı_listeleri(self,işlem,iişlem,liste_ismi,eklenecekler):
        if(işlem=="1"):
            if(iişlem=="1"):
                for i in eklenecekler:
                    sorgu = "update şarkılar set şarkı_listesi=? where şarkı_ismi=?"
                    self.cursor.execute(sorgu,(liste_ismi,i))
                    self.con.commit()
            if(iişlem=="2"):
                sorgu = "update şarkılar set şarkı_listesi=? where şarkı_ismi=?"
                self.cursor.execute(sorgu,(liste_ismi,eklenecekler))
                self.con.commit()
        elif(işlem=="2"):
            if(iişlem=="1"):
                for i in eklenecekler:
                    sorgu = "update şarkılar set şarkı_listesi=? where şarkı_ismi=?"
                    self.cursor.execute(sorgu, (liste_ismi, i))
                    self.con.commit()

    def şarkı_listelerini_göster(self):
        sorgu= "select şarkı_listesi from şarkılar"
        self.cursor.execute(sorgu)
        şarkılisteleri = self.cursor.fetchall()
        temiz = []
        for i in şarkılisteleri:
            if(i[0] not in temiz and i[0]!=""):
                temiz.append(i[0])
        return temiz
