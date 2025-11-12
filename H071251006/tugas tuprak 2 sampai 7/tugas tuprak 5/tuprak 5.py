import re

# 1 fungsi untuk inputan datanya nanti
# validasi
def validasi_nama(nama):
    pattern = r"^[a-zA-Z0-9\s]+$" 
    result = re.match(pattern, nama)  # untuk mencocokkan inputannya nanti
    if result:
        return nama
    else:
        raise ValueError("Nama tidak diperbolehkan menggunakan karakter khusus selain spasi")
    
def validasi_kode(kode):
    pattern = r"^[A-Z]{3,5}[0-9]{3,5}$"
    result = re.match(pattern, kode)
    if result:
        return kode
    else:
        raise ValueError("Format kode salah!")
    
def validasi_email(email):
    pattern = r"^[a-z0-9]+@[a-z0-9]+\.com$" 
    result = re.match(pattern, email)
    if result:
        return email
    else:
        raise ValueError("Email hanya boleh diisi dengan format 'nama@domain.com' tanpa spasi dan simbol")
    
def validasi_harga(harga):
    if re.search(r"[a-zA-Z]", harga):
        raise ValueError("Input tidak valid, harus berupa angka")
    pattern = r"^[0-9]+$"
    result = re.match(pattern, harga)
    if result:
        return int(harga)
    else:
        raise ValueError("Harga hanya berupa angka positif")
    
def validasi_stok(stok):
    if re.search(r"[a-zA-Z]", stok):
        raise ValueError("Input tidak valid, harus berupa angka")
    pattern = r"^[0-9]+$"
    result = re.match(pattern, stok)
    if result:
        return int(stok)
    else:
        raise ValueError("Inputan harus angka Positif")
    
# Analisis
def analsis_penjualan(harga, stok):
    return harga * stok

def analisis_kategori(harga):
    if harga >= 5000000:
        return "Mahal"
    elif harga > 1000000:
        return "Sedang"
    else:
        return "Murah"

# 2 fungsi untuk hasil analisis produk 
def analisis_data(data):
    produk_mahal = 0
    produk_sedang = 0
    produk_murah = 0
    penjualan_keseluruhan = 0
    total_harga = 0
    banyak_harga = 0

    nama_max = data[0]["Nama"]
    harga_max = data[0]["Harga"]
    nama_min = data[0]["Nama"]
    harga_min = data[0]["Harga"]

    for i in data:
        penjualan_keseluruhan += i["Penjualan"]
        total_harga += i["Harga"]
        banyak_harga += 1
        mean = total_harga / banyak_harga

        if i["Kategori"] == "Mahal":
            produk_mahal += 1
        if i["Kategori"] == "Sedang":
            produk_sedang += 1
        if i["Kategori"] == "Murah":
            produk_murah += 1

        if i["Harga"] > harga_max:
            harga_max = i["Harga"]
            nama_max = i["Nama"]
        if i["Harga"] < harga_min:
            harga_min = i["Harga"]
            nama_min = i["Nama"]

    print(f"\nTotal Penjualan Keseluruhan: Rp{penjualan_keseluruhan}")
    print(f"Rata-rata Harga Produk: Rp{mean:,.0f}")
    print(f"Produk Termahal: {nama_max} (Rp{harga_max:,})")
    print(f"Produk Termurah: {nama_min} (Rp{harga_min:,})")
    print(f"\nJumlah Produk Kategori Mahal: {produk_mahal}")
    print(f"Jumlah Produk Kategori Sedang: {produk_sedang}")
    print(f"Jumlah Produk Kategori Murah: {produk_murah}")

def tampilkan_nama_produk(data, index=0):
    if index < len(data):
        print(f"{data[index]['Nama']}")
        tampilkan_nama_produk(data, index + 1)
    
data = []

print("=== SISTEM ANALISIS DATA PRODUK E-COMMERCE ===")
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Input Data Produk\n2. Lihat Hasil Analisis\n3. Keluar Program")
    menu = int(input("Pilih menu (1/2/3): "))
    match menu:
        case 1:
            while True:
                try:
                    nama = input("\nNama Produk (ketik selesai untuk kembali ke menu): ")
                    validasi_nama(nama)
                    if nama == "selesai":
                        break
                except ValueError:
                    print("Nama tidak diperbolehkan menggunakan karakter khusus selain spasi")
                    continue
                while True:
                    try:
                        kode = input("Kode Produk: ")
                        validasi_kode(kode)
                        break
                    except ValueError:
                        print("Format kode salah!")
                        continue
                while True:
                    try:
                        email = input("Email Supplier: ")
                        validasi_email(email)
                        break
                    except ValueError:
                        print("Email hanya boleh diisi dengan format 'nama@domain.com' tanpa spasi dan simbol")
                        continue
                while True:
                    try:
                        harga_input = input("Harga Produk: ")
                        harga = validasi_harga(harga_input)
                        break
                    except ValueError as e:
                        print(str(e))
                        continue
                while True:
                    try:
                        stok_input = input("Stok Barang: ")
                        stok = validasi_stok(stok_input)
                        break
                    except ValueError as e:
                        print(str(e))
                        continue
                penjualan = analsis_penjualan(harga, stok)
                kategori = analisis_kategori(harga)
                produk = {"Nama": nama,
                        "Kode": kode,
                        "Email": email,
                        "Harga": harga,
                        "Stok": stok,
                        "Penjualan": penjualan,
                        "Kategori": kategori}
                data.append(produk)
                print("✅ Data produk berhasil disimpan!")

        case 2:
            try:
                print("\n=== HASIL ANALISIS DATA ===")
                for i in data:
                    print(f"{i['Nama']}({i['Kode']}) - Harga: Rp{i['Harga']} - Stok: {i['Stok']} - Penjualan: Rp{i['Penjualan']} - Kategori: {i['Kategori']}")
                analisis_data(data)
                print(f"\n=== DAFTAR PRODUK REKURSIF ===")
                tampilkan_nama_produk(data)
                print("\nData Berhasil Dianalisis!")
            except Exception as e:
                print("Data masih kosong. Pilih menu 1 untuk memasukkan data")
        
        case 3:
            print("\nTerima kasih telah menggunakan program ini! 👋")
            break

        case _:
            print("Angka yang diinput tidak valid. Silahkan memilih (1/2/3) : ")