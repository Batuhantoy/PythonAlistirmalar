def temizleyici(satır):
    satır=satır.replace("\n","")
    satır=satır.replace("	"," ")
    return satır


def ayıklayıcı(futbolcu):
    futbolcu=temizleyici(futbolcu)
    liste = futbolcu.split(" ")
    takımı=""
    for i in liste:
        if(i=="GS"):
            takımı="GS"
        elif (i == "FB"):
            takımı = "FB"
        elif (i == "BJK"):
            takımı = "BJK"
    return futbolcu+","+takımı



with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = []
    fb = []
    bjk = []
    ayıklanacak_liste=file.readlines()
    for i in ayıklanacak_liste:
        liste2=ayıklayıcı(i).split(",")
        #print(ayıklayıcı(i))
        if (liste2[1] == "GS"):
            gs.append(liste2[0]+"\n")
        elif (liste2[1] == "FB"):
            fb.append(liste2[0]+"\n")
        elif (liste2[1] == "BJK"):
            bjk.append(liste2[0]+"\n")

    with open("gs.txt","w",encoding="utf-8")as file2:
        file2.writelines(gs)
    with open("fb.txt","w",encoding="utf-8")as file2:
        file2.writelines(fb)
    with open("bjk.txt","w",encoding="utf-8")as file2:
        file2.writelines(bjk)



