print("""***************
Beden Kitle İndeksi Hesaplama Uygulaması
***************""")

kilo = int(input("Kilonuzu giriniz:"))
boy = float(input("Boyunuzu giriniz:"))
bki = kilo / boy**2

if (bki < 18.5):
    print("Zayıf")

elif(18.5 <= bki <25):
    print("Normal")

elif(25<=bki<30):
    print("Fazla Kilolu")

elif(bki>30):
    print("Obez")

"""
if (bki < 18.5):
    print("Zayıf")

elif(bki>=18.5 and bki<25):
    print("Normal")

elif(bki>=25 and bki<30):
    print("Fazla Kilolu")

elif(bki>30):
    print("Obez")

"""