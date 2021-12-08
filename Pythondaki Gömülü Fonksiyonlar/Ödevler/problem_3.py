from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

çift_sayılar = list(filter(lambda x: x % 2 ==0,liste))
print(çift_sayılar)
print(reduce(lambda x,y: x + y,çift_sayılar))