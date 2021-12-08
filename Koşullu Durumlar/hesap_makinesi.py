print("""**********
Hesap Makinesine Hoşgeldiniz

İşlemler:

1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme

**********""")
işlem = input("Hangi işlemi yapmak istiyorsunuz:")
a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

if(işlem == "1"):
      print("{} + {} = {}".format(a,b,a+b))

elif(işlem == "2"):
      print("{} - {} = {}".format(a, b, a - b))

elif(işlem == "3"):
      print("{} * {} = {}".format(a, b, a * b))

elif(işlem == "4"):
      print("{} : {} = {}".format(a, b, a / b))

else:
      print("Geçerli Bir İşlem Giriniz...")