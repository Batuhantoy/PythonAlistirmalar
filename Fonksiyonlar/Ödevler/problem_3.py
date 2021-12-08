
def ekok_bulma(a,b):
    i=2
    ekok=1
    while True:
        if(a%i==0 and b%i==0):
            ekok *=i
            a//=i
            b//=i
        elif(a%i==0 and b%i!=0):
            ekok*=i
            a//=i
        elif (a % i != 0 and b % i == 0):
            ekok *= i
            b //= i
        else:
            i+=1
        if(a==1 and b==1):
            break
    return ekok

a = int(input("1.Sayı :"))
b = int(input("2.Sayı :"))
print("EKOK({},{}) = {} dir".format(a,b,ekok_bulma(a,b)))