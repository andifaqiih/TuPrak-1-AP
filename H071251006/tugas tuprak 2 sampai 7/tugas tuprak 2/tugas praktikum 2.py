# Data toko
barang = ["Buku", "Pensil", "Pulpen"]
harga = [20000, 3000, 5000]
jumlah = [2, 5, 3]
# nomor 1
Total_Buku = (harga[0]*jumlah[0])
print (Total_Buku)
Total_Pensil = (harga[1]*jumlah[1])
print (Total_Pensil)
Total_Pulpen = (harga[2]*jumlah[2])
print (Total_Pulpen)
# nomor 2
Total_Harga = [Total_Buku, Total_Pensil, Total_Pulpen]
# nomor 3
Total_Belanja = (Total_Harga[0]+Total_Harga[1]+Total_Harga[2])
print (Total_Belanja)
# # nomor 4
Belanjaan = {
    "Buku": Total_Buku, 
    "Pulpen": Total_Pulpen, 
    "Pensil": Total_Pensil, 
    "Total Belanja": Total_Belanja
    }
# # nomor 5
print (Total_Buku > Total_Pulpen)
print (Belanjaan["Buku"]> Belanjaan["Pulpen"])
print (Total_Belanja > 50000)
print (Belanjaan["Total Belanja"]> 50000)
print (jumlah[0] + jumlah[1] + jumlah[2] > 5 )


