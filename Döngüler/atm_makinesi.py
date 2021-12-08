print("""**** ATM Makinesine Hoşgeldiniz ****
    İşlemler:

    1. Bakiye Sorgulama
    2. Para Yatırma
    3.Para Çekme

    Programdan çıkmak için 'q' ya basın...""")
bakiye = 1000

while True:
    işlem=input("Yapmak istediginiz işleminizi seçiniz:")
    if(işlem == "q"):
        print("Çıkış yapılıyor... yine bekleriz")
        break
    elif(işlem=="1"):
        print("Güncel Bakiyeniz :",bakiye)
        continue
    elif(işlem=="2"):
        yatırılanpara = int(input("Yatırmak İstenilen Miktar:"))
        bakiye += yatırılanpara
        continue
    elif(işlem=="3"):
        çekilenpara = int(input("Çekilmek İstenilen Miktar:"))
        if(çekilenpara>bakiye):
            print("Bakiyenizi aştınız lütfen tekrar deneyiniz...")
            continue

        bakiye-=çekilenpara
        continue
    else:
        print("Geçersiz İşlem...")
        continue




