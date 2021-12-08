sayı = int(input("Sayıyı giriniz :"))
bölenler =[]
toplam =0
for i in range(1,sayı):
    if(sayı%i==0):
        if(i!=sayı):
            bölenler.append(i)
        else:
            continue

for a in bölenler:
    toplam+=a

print("Bölen Sayılar :",bölenler)
if(toplam==sayı):
    print("{} sayısı mükemmel sayıdır".format(sayı))
else:
    print("{} sayısı mükemmel sayı degildir".format(sayı))