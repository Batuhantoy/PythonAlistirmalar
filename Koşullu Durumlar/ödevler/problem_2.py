print("3 Sayı giriniz")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if(a==b or a==c or b==c):
    if(a==b):
        print("En büyük iki sayı vardır:",a)
    elif(a==c):
        print("En büyük iki sayı vardır:",a)
    elif(b==c):
        print("En büyük iki sayı vardır",b)

else:#yukarıya gerek yok ama örnek olsun
    if a>=b and a>=c:
        print("En büyük sayı :", a)
    elif b>=a and b>=c:
        print("En büyük sayı :", b)
    elif c>=a and c>=b:
        print("En büyük sayı :", c)