a=int(input("1. Sayı:"))
b=int(input("2. Sayı:"))
fibonacci= [a,b]
for i in range(20):
    a,b= b,a+b
    fibonacci.append(b)
print(fibonacci)
