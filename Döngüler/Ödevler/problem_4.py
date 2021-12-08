toplam=0
while True:
    a=input("Sayı giriniz:")
    if(a=="q"):
        print("Program Sonlandırılıyor...")
        print("Girdiginiz sayıların toplamı =",toplam)
        break
    toplam+=int(a)
