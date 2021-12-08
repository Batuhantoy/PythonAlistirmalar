bölenler = []
def ebob_bulma(x,y):
    i=1
    ebob=1

    while(i<=a and i<=b):

        if(a%i==0 and b%i==0):
            ebob=i
            #bölenler.append(i)
        i +=1
    return ebob

def ebob(a, b):
    ebob=1
    i=1
    for i in range(1,a) or range(1,b):
        if(a%i==0 and b%i==0):
            ebob=i
            bölenler.append(i)
    return ebob

a = int(input("1.Sayı :"))
b = int(input("2.Sayı :"))
print("EBOB({},{}) = {} dir".format(a,b,ebob(a,b)))
#print("EBOB({},{}) = {} dir".format(a,b,ebob_bulma(a,b)))
print(bölenler)







