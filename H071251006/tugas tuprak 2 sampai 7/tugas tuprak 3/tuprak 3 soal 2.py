data= [
    {"nama": "Alya", "Nilai": 88},
    {"nama": "Budi", "Nilai": 67},
    {"nama": "Citra","Nilai": 74}
]

if data[0]["Nilai"]>= 85 :
    print (f"{data[0]["nama"]}: {data[0]["Nilai"]} -> Lulus (A)")
elif 85 > data[0]["Nilai"] >= 70  :
    print (f"{data[0]["nama"]}: {data[0]["Nilai"]} -> Lulus (B)")
elif 70 > data[0]["Nilai"] >= 50  :
    print (f"{data[0]["nama"]}: {data[0]["Nilai"]} -> Gagal (C)")
else :
    print (f"{data[0]["nama"]}: {data[0]["Nilai"]} -> Gagal (D)")

if data[1]["Nilai"]>= 85 :
    print (f"{data[1]["nama"]}: {data[1]["Nilai"]} -> Lulus (A)")
elif 85 > data[1]["Nilai"] >= 70  :
    print (f"{data[1]["nama"]}: {data[1]["Nilai"]} -> Lulus (B)")
elif 70 > data[1]["Nilai"] >= 50  :
    print (f"{data[1]["nama"]}: {data[1]["Nilai"]} -> Gagal (C)")
else :
    print (f"{data[1]["nama"]}: {data[1]["Nilai"]} -> Gagal (D)")

if data[2]["Nilai"]>= 85 :
    print (f"{data[2]["nama"]}: {data[2]["Nilai"]} -> Lulus (A)")
elif 85 > data[2]["Nilai"] >= 70  :
    print (f"{data[2]["nama"]}: {data[2]["Nilai"]} -> Lulus (B)")
elif 70 > data[2]["Nilai"] >= 50  :
    print (f"{data[2]["nama"]}: {data[2]["Nilai"]} -> Gagal (C)")
else :
    print (f"{data[2]["nama"]}: {data[2]["Nilai"]} -> Gagal (D)")

rata= (data[0]["Nilai"] + data[1]["Nilai"] + data[2]["Nilai"])/3
print (f"Rata - rata kelas : {rata:.2f}")

if data[0]["Nilai"] > data[1]["Nilai"] and data[0]["Nilai"]> data[2]["Nilai"]:
    print(f"Nilai tertinggi: {data[0]["Nilai"]} ({data[0]["nama"]})")
elif data[0]["Nilai"] < data[1]["Nilai"] and data[1]["Nilai"] > data[2]["Nilai"]:
    print(f"Nilai tertinggi: {data[1]["Nilai"]} ({data[1]["nama"]})")
else:
    print(f"Nilai tertinggi: {data[2]["Nilai"]} ({data[2]["Nilai"]})")

if data[0]["Nilai"] < data[1]["Nilai"] and data[0]["Nilai"]< data[2]["Nilai"]:
    print(f"Nilai terendah: {data[0]["Nilai"]} ({data[0]["nama"]})")
elif data[0]["Nilai"] > data[1]["Nilai"] and data[1]["Nilai"] < data[2]["Nilai"]:
    print(f"Nilai terendah: {data[1]["Nilai"]} ({data[1]["nama"]})")
else:
    print(f"Nilai terendah: {data[2]["Nilai"]} ({data[2]["Nilai"]})")