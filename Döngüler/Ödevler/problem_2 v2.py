sayı = input("Sayı giriniz:")
basamak_sayısı=len(sayı)
sayı=int(sayı)

güncelbasamak=0
toplam=0

geçicisayı=sayı

while(geçicisayı>0):
    güncelbasamak = geçicisayı % 10
    toplam += güncelbasamak ** basamak_sayısı
    geçicisayı //= 10

if(toplam==int(sayı)):
    print("{} sayısı bir Armstrong sayısıdır".format(sayı))
else:
    print("{} sayısı bir Armstrong sayısı degildir".format(sayı))