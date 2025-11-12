books= [
    {"id": 1, "judul": "Belajar Python", "stok": 10, "harga": 85000},
    {"id": 2, "judul": "Algoritma Dasar", "stok":3, "harga": 120000},
    {"id": 3, "judul": "Struktur Data", "stok": 2, "harga": 95000}
]
print ("=== Menu Inventori Buku ===")
print ("1. Tampilkan semua buku")
print ("2. Tambahkan buku baru")
print ("3. Ubah stok buku")
print ("4. Buku dengan stok < 5")
print ("5. Hitung total nilai inventori")
menu=int (input("Pilih menu: "))

if menu == 1:
    print (f"Judul: {books[0]["judul"]}; id: {books[0]["id"]}, stok: {books[0]["stok"]}, harga: {books[0]["harga"]}")
    print (f"Judul: {books[1]["judul"]}; id: {books[1]["id"]}, stok: {books[1]["stok"]}, harga: {books[1]["harga"]}")
    print (f"Judul: {books[2]["judul"]}; id: {books[2]["id"]}, stok: {books[2]["stok"]}, harga: {books[2]["harga"]}")
elif menu == 2:
    id_baru = int(input("Masukkan ID buku yang ingin ditambahkan : "))
    judul_baru = str(input("Masukkan judul buku yang ingin ditambahkan : "))
    stok_baru = int(input("Masukkan stok buku yang ingin ditambahkan : "))
    harga_baru = int(input("Masukkan harga buku yang ingin ditambahkan : "))
    buku_baru = {"id": id_baru, "judul": judul_baru, "stok": stok_baru, "harga": harga_baru}
    books.append(buku_baru)
    print (f"Judul: {books[0]["judul"]}; id: {books[0]["id"]}, stok: {books[0]["stok"]}, harga: {books[0]["harga"]}")
    print (f"Judul: {books[1]["judul"]}; id: {books[1]["id"]}, stok: {books[1]["stok"]}, harga: {books[1]["harga"]}")
    print (f"Judul: {books[2]["judul"]}; id: {books[2]["id"]}, stok: {books[2]["stok"]}, harga: {books[2]["harga"]}")
    print (f"Judul: {books[3]["judul"]}; id: {books[3]["id"]}, stok: {books[3]["stok"]}, harga: {books[3]["harga"]}")
elif menu == 3:
    id = int(input("Masukkan ID buku yang stoknya ingin diubah : "))
    stok_baru = int(input("Masukkan perubahan stok buku : "))
    if (id == 1):
        books[0]["stok"] = stok_baru
        print (f"{books[0]["judul"]} : {books[0]["stok"]}")
    elif (id == 2):
        books[1]["stok"] = stok_baru
        print (f"{books[1]["judul"]} : {books[1]["stok"]}")
    elif (id == 3):
        books[2]["stok"] = stok_baru
        print (f"{books[2]["judul"]} : {books[2]["stok"]}")
    else :
        print ("ID buku tidak ditemukan")
elif menu == 4:
    if (books[0]["stok"] < 5):
        print (f"{books[0]["judul"]} : {books[0]["stok"]}")
    if (books[1]["stok"] < 5):
        print (f"{books[1]["judul"]} : {books[1]["stok"]}")
    if (books[2]["stok"] < 5):
        print (f"{books[2]["judul"]} : {books[2]["stok"]}")
elif menu == 5:
    total_inventori = (books[0]["stok"]*books[0]["harga"]) + (books[1]["stok"]*books[1]["harga"]) + (books[2]["stok"]*books[2]["harga"])
    print (f"Total inventori anda adalah {total_inventori}")
else :
    print ("Angka yang diinput tidak valid.")

