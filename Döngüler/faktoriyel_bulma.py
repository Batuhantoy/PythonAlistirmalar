sayı=int(input("Faktoriyelini Bulmak istediginiz sayı:"))
fak=1

for i in range(1,sayı+1):
    fak *=i
    if (i == sayı):
        print(sayı,"=",fak)
    else:
        print(i,end=" x ")

