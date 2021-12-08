class Metin():
    def __init__(self):
        with open("mailler.txt","r",encoding="utf-8") as file:
            for satır in file:
                satır = satır[:-1]
                if(satır.endswith(".com") and satır.find("@") != -1):
                    print(satır)

            self.mail = list()
            metin = file.read()
            mailler = metin.split("\n")
            for i in mailler:
                self.mail.append(i)



    def uygun_olanlar(self):
        for i in self.mail:
            if (i.endswith("@gmail.com") or i.endswith("@yahoo.com")):
                print(i)
        print("------------------------------------------------")

        for i in self.mail:
            if(i.rfind("@gmail.com")!=-1 or i.rfind("@yahoo.com")!= -1):
                print(i)

mailler = Metin()
#mailler.uygun_olanlar()
