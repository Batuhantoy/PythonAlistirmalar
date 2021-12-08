def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    durum = "1"
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
    if(son_not>=90):
        harf="AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DD"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf="FF"
        durum="0"

    #harften sonra \n
    return isim + " ----------> " + harf+"\n"+","+ isim+","+durum+","+harf

with open("kişiler.txt","r",encoding="utf-8") as file:
    eklenecekler=[]
    kalanlar = []
    geçenler = []

    for i in file:
        liste2= not_hesapla(i).split(",")
        eklenecekler.append(liste2[0])
        if(liste2[2]=="0"):
            kalanlar.append(liste2[1]+"  "+liste2[3]+"\n")
        else:
            geçenler.append(liste2[1]+"  "+liste2[3]+"\n")

    with open("notlar.txt","w",encoding="utf-8") as file2:
        file2.writelines(eklenecekler)

    with open("kalanlar.txt","w",encoding="utf-8") as file3:
        file3.writelines(kalanlar)
    with open("geçenler.txt","w",encoding="utf-8") as file4:
        file4.writelines(geçenler)