class Metin():
    def __init__(self):
        with open("uzunmetin.txt","r",encoding="utf-8") as file:
            metin = file.read()
            kelimeler = metin.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i.strip("\n")
                i.strip(" ")
                i.strip(".")
                i.strip(",")
                self.sade_kelimeler.append(i)
    def sayıcı(self):
        sözlük =dict()

        for i in self.sade_kelimeler:
            if(i in sözlük):
                sözlük[i] +=1
            else:
                sözlük[i] = 1
        for kelime,sayı in sözlük.items():
            print("'{}' = {}".format(kelime,sayı))

    def harf_sayıcı(self,cümle):
        sayım = dict()

        for i in cümle:
            if(i in sayım):
                sayım[i] +=1
            else:
                sayım[i] = 1
        for i,j in sayım.items():
            print(i," : ",j)

metin = Metin()
#metin.sayıcı()

metin.harf_sayıcı("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb")
