print("Harf Notu Hesaplama Uygulamasına Hoşgeldiniz")

vize1 = int(input("1.Vize Notu :"))
vize2 = int(input("2.Vize Notu :"))
finalnotu = int(input("Final Notu :"))

genel_ortalama = (vize1 * 30/100 + vize2 * 30/100 + finalnotu * 40/100)

if (genel_ortalama >= 90):
    print("AA")
elif (genel_ortalama >= 85):
    print("BA")
elif (genel_ortalama >= 80):
    print("BB")
elif (genel_ortalama >= 75):
    print("CB")
elif (genel_ortalama >= 70):
    print("CC")
elif (genel_ortalama >= 65):
    print("DC")
elif (genel_ortalama >= 60):
    print("DD")
elif (genel_ortalama >= 55):
    print("FD")
else:
    print("FF")
