hari=int(input("Masukkan Jumlah Hari: "))
suhu_harian=[]
for i in range (hari):
    suhu_c=float(input(f"Masukkan suhu hari ke {i+1} (°C)"))
    suhu_harian.append(suhu_c)
    if i == hari:
        break
print ("|----------------------------------------|")
print ("|           Data Suhu Harian             |")
print ("|----------------------------------------|")
print ("| Hari | Celcius | Fahrenheit | Kategori |")
print ("|----------------------------------------|")
hari_sekian=0
for j in (suhu_harian):
    if j < 20 :
        kategori="Dingin"
    elif 20<=j<=29:
        kategori="Sejuk "
    elif 30<=j<=35:
        kategori="Hangat "
    else:
        kategori="Panas "
    suhu_f=j*9/5+32
    hari_sekian+= 1
    print (f"|  {hari_sekian}   |   {j}  |    {suhu_f}    |  {kategori}  |")
print ("|----------------------------------------|")  