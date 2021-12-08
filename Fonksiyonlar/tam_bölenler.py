
def tam_bölen(sayı):
    tam_bölenler = []
    for i in range(2,sayı):
        if(sayı%i==0):
            tam_bölenler.append(i)
    return tam_bölenler

while True:
    sayı = input("Sayıyı giriniz")

    if(sayı=="q"):
        break
    else:
        sayı = int(sayı)
        if(tam_bölen(sayı)!=[]):
            print("Bu sayının tam bölenleri :",tam_bölen(sayı))
        elif(tam_bölen(sayı)==[]):
            print("Bu sayının tam böleni yoktur")