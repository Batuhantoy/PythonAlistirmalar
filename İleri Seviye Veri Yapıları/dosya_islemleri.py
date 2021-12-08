class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_içerigi = file.read()
            kelimeler = dosya_içerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)

    def tüm_kelimeler(self):
        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        print("Tüm kelimeler :")
        for i in kelimeler_kümesi:
            print(i)
            print("******************")

    def kelime_frekansı(self):

        kelime_sözlük = dict()

        for i in self.sade_kelimeler:
            if(i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1

        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor...".format(kelime,sayı))
            print("-----------------------------------------")

    def kelime_arama(self,kelime):

        arama = {kelime:0}
        for i in self.sade_kelimeler:
            if(i == kelime and arama[kelime]==0 ):
                arama[kelime] =1
            elif(i == kelime):
                arama[kelime] += 1
        if(arama[kelime]==0):
            print(" kelimeden metinde bulunmamaktadır")
        else:
            print("Aradıgınız '{}' kelimesinden {} tane var".format(kelime, arama[kelime]))

dosya = Dosya()
keli = input("aramak istediginiz kelime :")
dosya.kelime_arama(keli)