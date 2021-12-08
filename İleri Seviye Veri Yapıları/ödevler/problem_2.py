class Şiir():
    def __init__(self):
        baş_harf = ""
        with open("şir.txt","r",encoding="utf-8") as file:
            for i in file:
                baş_harf += i[0]

            şiir = file.readlines()
            baş_harfler =[]
            for i in şiir:
                baş_harfler.append(i[0])
                print(i[0],end="")


        print(baş_harf)
şiir = Şiir()
