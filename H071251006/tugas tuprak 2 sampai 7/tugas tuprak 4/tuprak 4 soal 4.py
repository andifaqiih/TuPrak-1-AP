jumlah=int(input("Masukkan jumlah item belanja: "))
Daftar_Belanja=[]
for i in range(jumlah):
    barang=input(f"Masukkan barang ke-{i+1}")
    harga=int(input(f"Harga {barang}:"))
    jumlah_barang=int(input(f"Jumlah {barang}:"))
    daftar= {
        "Nama Barang":barang,
        "Harga":harga,
        "Jumlah": jumlah_barang
        }
    Daftar_Belanja.append(daftar)
    if i == jumlah :
        break
print("Daftar Belanja")
total=0
for j in Daftar_Belanja:
    barang = j["Nama Barang"]
    item = j["Jumlah"]
    nominal = j["Harga"]
    total += (item * nominal)
    print (f"{barang} x {item} = {(item * nominal):,}")
if total > 500000 :
    diskon = int(total * 0.1)
    total_akhir = total - diskon
else :
    diskon = 0
    total_akhir = total - diskon
print (f"\nTotal belanja : {(total):,}")
print (f"Diskon : {(diskon):,}")
print (f"Total akhir : {(total_akhir):,}")