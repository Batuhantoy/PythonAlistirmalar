liste = [(3,4),(10,3),(5,6),(1,9)]

def alan_hesaplama(x):
    return x[0]*x[1]

print(list(map(alan_hesaplama,liste)))
#print(list(map(lambda  x: alan_hesaplama(),liste)))
#print(list(map(lambda  x: x[0] * x[1],liste)))