import random
import time
print("""
************
Sayı Tahmin
************

1 ile 40 arasındaki sayıyı tahmin edin""")


rastgele_sayı = random.randint(1, 40)
tahmin_hakkı = 7
while True:
      tahmin = int(input("Tahmininiz : "))
      if(tahmin_hakkı!=0):
            if(tahmin < rastgele_sayı):
                  print("Cevabınız sorgulanıyor...")
                  time.sleep(0.5)
                  print("Tahmininiz eksik kaldı")
                  tahmin_hakkı -= 1
            elif(tahmin > rastgele_sayı):
                  print("Cevabınız sorgulanıyor...")
                  time.sleep(0.5)
                  print("Tahmininiz fazla kaldı")
                  tahmin_hakkı -= 1
            elif(tahmin==rastgele_sayı):
                  print("Cevabınız sorgulanıyor...")
                  time.sleep(0.5)
                  print("Tebrikler dogru bildiniz\n\n")
                  istek = input("""Tekrar Oynamak ister misiniz?\n1. Evet\n2. Hayır\n""")
                  if (istek == "1"):
                        rastgele_sayı = random.randint(1, 40)
                        tahmin_hakkı = 7
                  elif (istek == "2"):
                        print("Yine bekleriz")
                        break
                  else:
                        print("İsteginizi anlayamadım... Çıkış yapılıyor")
                        break

      else:
            print("Tahmin hakkınız bitti\n\n")
            istek = input("""Tekrar Oynamak ister misiniz?\n1. Evet\n2. Hayır\n""")
            if (istek == "1"):
                  rastgele_sayı = random.randint(1, 40)
                  tahmin_hakkı = 7
            elif (istek == "2"):
                  print("Yine bekleriz")
                  break
            else:
                  print("İsteginizi anlayamadım... Çıkış yapılıyor")
                  break






