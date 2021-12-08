liste = ["345","sadas","324a","14","kemal"]
sıra=1
for i in liste:
    try:
        print("{}.Eleman : ".format(sıra),int(i))
    except ValueError:
        print("{}.eleman olan {} elemanı integer olamaz".format(sıra,i))
    finally:
        sıra+=1