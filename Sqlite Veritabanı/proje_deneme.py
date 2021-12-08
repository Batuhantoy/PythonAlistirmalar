from  kütüphane import *

print("""************************************
Kütüphane Programına Hoşgeldiniz

İşlemler:

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
6. Degişiklik

Çıkmak için 'q' ya basın
************************************""")

kütüphane = Kütüphane()
while True:
    işlem = input("Yapacagınız İşlem : \n")
    if(işlem=="q"):
        print("Yine bekleriz...")
        kütüphane.baglantıyı_kes()
        break
    elif(işlem=="1"):
        kütüphane.kitapları_göster()
    elif (işlem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz? ")
        print("Kitap Sorgulanıyor...")
        time.sleep(1)

        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim = input("İsim : ")
        yazar = input("Yazar : ")
        yayınevi = input("Yayınevi : ")
        tür = input("Tür : ")
        baskı = int(input("Baskı : "))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi")
    elif (işlem == "4"):
        isim = input("Silmek istediginiz kitap ismi : ")
        cevap = input("Emin misiniz ? (E/H)")
        if(cevap=="E"):
            print("Kitap siliniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi")
    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ? ")
        kütüphane.baskı_yükselt(isim)
    elif(işlem=="6"):
        aranan=input("Aradıgınız kitapla ilgili bir anahtar kelime girin : ")
        kütüphane.kontrol(aranan)
    else:
        print("Geçersiz işlem...")
