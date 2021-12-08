
#print("Çıkmak için q ya basınız")
sayı = input("Sayıyı giriniz:")
basamak_sayısı=len(sayı)
toplam=0

for a in sayı:
    toplam += int(a) ** basamak_sayısı

if(toplam==int(sayı)):
    print("{} sayısı bir Armstrong sayısıdır".format(sayı))
else:
    print("{} sayısı bir Armstrong sayısı degildir".format(sayı))
