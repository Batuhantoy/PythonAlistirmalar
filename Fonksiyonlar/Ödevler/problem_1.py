def mükemmel_sayı(sayı):
    bölenlertoplam=0
    for i in range(1,sayı):
        if(sayı%i==0):
            bölenlertoplam+=i

    return bölenlertoplam==sayı
    #if(bölenlertoplam==sayı):
    #    return True
    #else:
    #    return False
while True:
    istek = input("""
    Ne yapmak istersiniz
    1. 1'den 1000'e kadar olan mükemmel sayıları bul
    2. Kendi girdigim bir sayıyı kontrol et
    3. Çıkış
    """)
    if(istek=="1"):
        for a in range(1,1000):
            if(mükemmel_sayı(a)):
                print("Mükemmel Sayı : ",a)
    elif(istek=="2"):

        while True:
            sayı = input("Sayı : ")
            if(sayı=="q"):
                print("Program sonlandırılıyor...")
                break
            else:
                sayı = int(sayı)
                if(mükemmel_sayı(sayı)):
                    print("{} mükemmel bir sayıdır".format(sayı))
                else:
                    print("{} mükemmel bir sayı değildir".format(sayı))
    elif(istek=="3"):
        break