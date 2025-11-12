username1= str (input("Masukkan username Anda :"))
password1= str (input("Masukkan password Anda :"))

if username1== "admin" and password1== "12345":
    print ("Login berhasil!")
else:
    print ("Login gagal, coba lagi")

    username2= str(input("Masukkan username Anda :"))
    password2= str(input("Masukkan password Anda :"))
    if username2== "admin" and password2== "12345":
        print ("Login berhasil!")
    else:
        print ("Login gagal, coba lagi")

        username3= str(input("Masukkan username Anda :"))
        password3= str(input("Masukkan password Anda :"))

        if username3== "admin" and password3=="12345":
            print ("Login berhasil!")
        else:
            print("Akun anda diblokir!")