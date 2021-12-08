from şarkılar import *

print("""*********************
YT Music

1.Şarkıları Göster
2. Şarkı Ara
3. Şarkı Ekle
4. Şarkı Sil
5. Şarkı Listesine Ekle
6. Şarkı Süresi
*********************""")

şarkıyeri = şarkı_program_kontrol()
while True:
    işlem = input("Yapacagınız işlem : ")
    if(işlem=="q"):
        print("Yine bekleriz...")
        şarkıyeri.baglantı_kapat()
        break
    elif(işlem=="1"):
        şarkıyeri.şarkıları_göster()
    elif(işlem=="2"):
        aranan = input("Aradıgınız kelime : ")
        şarkıyeri.şarkı_arama(aranan)
    elif(işlem=="3"):
        isim = input("İsim : ")
        sanatçı = input("Sanatçı : ")
        albüm = input("Albüm : ")
        prodüksiyon_şirketi = input("Prodüksiyon Şirketi : ")
        süresi = input("Süresi : ")

        yeni_şarkı = Şarkı(isim,sanatçı,albüm,prodüksiyon_şirketi,süresi)
        şarkıyeri.şarkı_ekle(yeni_şarkı)
        print("Kitap Eklendi")
    elif(işlem=="4"):
        şarkıyeri.şarkıları_göster()
        silinecek_şarkı = input("Silmek istediginiz şarkı ismi : ")
        şarkıyeri.şarkı_sil(silinecek_şarkı)
    elif(işlem=="5"):
        işlem = input("1. Yeni Şarkı listesi oluştur\n2. Şarkı Listesine Şarkı Ekle")
        if(işlem=="1"):
            liste_ismi = input("Yeni Şarkı Listesi İsmi : ")
            işlem =input("""
            1. Eklemek İstediginiz Şarkıları virgülle ayırarak yazınız
            2. Şarkı Ara
            """)
            if(işlem=="1"):
                liste = şarkıyeri.komut_çalıştır("select şarkı_ismi from şarkılar")
                eklenecekler = input("Eklemek istediklerinizi virgülle ayırarak yazınız : ")
                eklenecekler = eklenecekler.split(",")
                şarkıyeri.şarkı_listeleri("1","1",liste_ismi,eklenecekler)
            elif(işlem=="2"):
                aranan = input("Aradıgınız Şarkı : ")
                şarkı = şarkıyeri.şarkı_arama(aranan)
                istek=input("Bu şarkıyı listeye eklemek istiyormusunuz (E/H)")
                if(istek=="E"):
                    #liste_ismi1=input("Liste İsmi : ")
                    şarkıyeri.şarkı_listeleri("1","2",liste_ismi,şarkı.şarkı_ismi)
                elif(istek=="H"):
                    pass
        elif(işlem=="2"):
            a=1
            for i in şarkıyeri.şarkı_listelerini_göster():
                print("{}. {}".format(a,i))
                a+=1
            seçilen_liste = input("Hangi listeye eklemek istersiniz?")
            şarkıyeri.şarkıları_eleyipgöster(seçilen_liste)
            eklenecekler = input("Eklemek istediklerinizi virgülle ayırarak yazınız")
            eklenecekler = eklenecekler.split(",")
            şarkıyeri.şarkı_listeleri("2","1",seçilen_liste,eklenecekler)
    elif(işlem=="6"):
        şarkıyeri.toplam_şarkısüresi()



