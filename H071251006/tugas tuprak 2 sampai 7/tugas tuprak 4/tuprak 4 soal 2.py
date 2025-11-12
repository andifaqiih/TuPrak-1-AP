while True:
    pilihan = input("Pilih menu (kopi/teh/susu) atau 'stop' untuk keluar:").lower()
    
    if pilihan == "stop":
        print("Mesin berhenti. Terima kasih!")
        break
    
    elif pilihan == "kopi":
        harga = 5000
    elif pilihan == "teh":
        harga = 4000
    elif pilihan == "susu":
        harga = 6000
    else:
        print("Menu tidak tersedia. Silakan pilih lagi.")
        continue
        
    
    print("Masukkan uang Anda:")
    uang = int(input())   
    
    if uang == harga:
        print("Anda mendapat", pilihan + ".", "Tidak ada kembalian.")
    elif uang > harga:
        print("Anda mendapat", pilihan + ".", "Kembalian:", uang - harga)
    else:
        print("Uang tidak cukup!")