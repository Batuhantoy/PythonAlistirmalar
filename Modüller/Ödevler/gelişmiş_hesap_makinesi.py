import math
import keyboard
işlem = []

def silici(silinecek1,silinecek2,index,sonuç):
    işlem[index]=sonuç
    işlem.pop(silinecek2)
    işlem.pop(silinecek1)

def sonuçlama():
    sonuçlar = []
    sonuç = 0
    i =0
    j=0
    k=0
    l=0

    while i<len(işlem):
        if(işlem[i]=="/"):
            a = int(işlem[i-1]) / int(işlem[i+1])
            #sonuçlar.append(a)
            silici(i-1,i+1,i,a)
        i+=1
    while j<len(işlem):
        if(işlem[j]=="*"):
            b = int(işlem[j-1]) * int(işlem[j+1])
            #sonuçlar.append(b)
            silici(j-1,j+1,j,b)
        j+=1
    while k<len(işlem):
        if(işlem[k]=="+"):
            c = int(işlem[int(k-1)]) + int(işlem[int(k+1)])
            #sonuçlar.append(c)
            silici(k-1,k+1,k,c)
        k+=1
    while l < len(işlem):
        if(işlem[l]=="-"):
            d= int(işlem[l-1]) - int(işlem[l+1])
            #sonuçlar.append(d)
            silici(l-1,l+1,l,d)
        l+=1

    #for m in sonuçlar:
        #sonuç+=m
    print("Sonuç : ",işlem[0])


while True:
    t = input("Sayı:")

    if(t=="="):
        sonuçlama()
        işlem.clear()
        print("----------------------------------")
    elif(t=="q"):
        break
    else:
        işlem.append(t)






