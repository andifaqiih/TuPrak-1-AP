jumlah=int(input("Masukkan jumlah Mahasiswa: "))
Daftar_Mahasiswa=[]
for i in range (jumlah) :
    nama=input(f"Masukkan nama Mahasiswa ke-{i+1}:")
    nilai=int(input(f"Masukkan nilai {nama}:"))
    if nilai >= 85 :
        grade="A"
    elif 70<= nilai <= 84 :
        grade="B"
    elif 55<= nilai <= 69 :
       grade="C"
    elif 40<= nilai or nilai <= 54 :
        grade="D"
        if nilai < 50:
            grade="D -> Butuh remedial"
    else:
        grade="E -> Butuh remedial"

    Daftar_Mahasiswa.append({
        "Nama":nama,
        "Nilai":nilai,
        "Grade": grade
    })
print ("Daftar Mahasiswa :")
for k in Daftar_Mahasiswa:
    print (f"Nama: {k["Nama"]},Nilai: {k["Nilai"]},Grade: {k["Grade"]}")