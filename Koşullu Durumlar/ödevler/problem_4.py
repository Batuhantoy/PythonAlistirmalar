print("""Hangi Şeklin Tipini Bulmak İstiyorsunuz

1. Üçgen
2. Dikdörtgen""")

seçim = input("Seçiminiz :")
if(seçim == "1"):
    a = int(input("Birinci Kenar :"))
    b = int(input("İkinci Kenar :"))
    c = int(input("Üçüncü Kenar :"))

    if(abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b):
        if(a==b or a==c or b==c):
            print("İkizkenar Üçgen")
        elif(a==b==c):
            print("Eşkenar Üçgen")
else:
    print("Üçgen Belirtmiyor")


if(seçim==2):
    a = int(input("Birinci Kenar :"))
    b = int(input("İkinci Kenar :"))
    c = int(input("Üçüncü Kenar :"))
    d = int(input("Dördüncü Kenar :"))

    if(a==b==c==d):
        print("Kare")
    elif((a==b and c==d) or (a==c and b==d) or (a==d and b==c)):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
else:
    print("Geçersiz Seçim...")