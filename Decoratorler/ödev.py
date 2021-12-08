def mükemmel_sayı(fonk):
    def özellik():
        mükemmeller=[]
        for i in range(1,1001):
            toplam = 0
            for a in range(1,i):
                if(i%a==0):
                    toplam += a
            if(i==toplam):
                mükemmeller.append(i)
        print(mükemmeller)
        fonk()
    return özellik

@mükemmel_sayı
def asal_sayılar():
    sayı=int(input("Kaça kadar : "))
    asallar=[]
    for i in range(2,sayı):
        for a in range(2,i):
            if(i%a==0):
                break
        else:
            #if(i not in asallar or i==2):
            asallar.append(i)

    print(asallar)

asal_sayılar()

