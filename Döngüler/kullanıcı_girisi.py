print("""****************
Kullanıcı Girişi
****************""")

sys_kullanıcı_adı="batu"
sys_parola="980"
giris_hakkı=3

while True:
    if(giris_hakkı!=0):
        kullanıcı_adı = input("Kullanıcı Adı:")
        parola = input("Parola:")
        if (kullanıcı_adı != sys_kullanıcı_adı or parola != sys_parola):
            if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
                print("Kullanıcı Adı Hatalı")
            elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
                print("Parola Hatalı")
            elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
                print("İkiside Hatalı")
            print("------------------------------\n")
            giris_hakkı -= 1
        else:
            print("Giriş Başarılı...")
            break
    else:
        print("Giriş Hakkınız Bitti")
        break



