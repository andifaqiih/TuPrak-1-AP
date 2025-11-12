angka=input("Masukkan Deret Angka (pisahkan dengan koma):")
angka_2=""
semua_angka=[]
for i in angka :
    if i == (","):
        semua_angka.append(int(angka_2))
        angka_2 = ""
    else :
        angka_2 += i
semua_angka.append(int(angka_2))

maksimum=semua_angka[0]
minimum=semua_angka[0]
jumlah=0
banyak=0
bilangan_prima=[]
for j in semua_angka:
    # untuk maksimum dan minimum
    if j > maksimum :
        maksimum=j
    if j < minimum:
        minimum=j
    # untuk rata
    jumlah +=j
    banyak +=1
    # untuk bilangan prima
    if j > 1:
        prima = True
        for k in range(2, j):
            if j % k == 0:
                prima = False
                break
        if prima:
            bilangan_prima.append(j)
rata= jumlah/banyak
print("Nilai Maksimum =",maksimum)
print("Nilai Minimum =", minimum)
print("Rata-rata nilai =",rata)
if rata >=70:
    print("Lulus")
else:
    print("Tidak Lulus")


print("Bilangan Prima dalam List :")
for p in bilangan_prima:
    print(p)