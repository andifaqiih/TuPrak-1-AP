while True:    
    nilai=int(input("Masukkan Nilai Ganjil:"))
    if nilai %2==1:
        for i in range(nilai, 0,-2): # untuk segitiga bagian atas
            spasi=(nilai - i) // 2
            print(" " * spasi + "*" * i ) 
        for i in range(3, nilai +1, 2): # untuk segitiga bagian bawah
            spasi=(nilai - i)// 2
            print(" "* spasi + "*"*i)
        break
    else:
        print("Eror harus bilangan ganjil")