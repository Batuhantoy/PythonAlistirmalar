pisagor_listesi = []
def pisagor_üçgeni():
    c = 0
    for a in range(1,101):
        for b in range(1,101):
            c = (a**2+b**2) ** 0.5

            if(c==int(c)):
                pisagor_listesi.append((a,b,int(c)))

    return pisagor_listesi

pisagor_üçgeni()
print(pisagor_listesi)

