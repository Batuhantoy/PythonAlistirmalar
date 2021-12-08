print("""******************
Kullanıcı Girişi
******************""")

sys_kullanıcı_adı = "batu"
sys_parola = "980"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if(kullanıcı_adı != sys_kullanıcı_adı or parola != sys_parola):
    if(kullanıcı_adı == sys_kullanıcı_adı and parola!=sys_parola):
        print("Parola Hatalı...")

    elif(kullanıcı_adı != sys_kullanıcı_adı and parola==sys_parola):
        print("Kullanıcı Adı Hatalı...")

    elif(kullanıcı_adı!=sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Giriş Başarılı")

