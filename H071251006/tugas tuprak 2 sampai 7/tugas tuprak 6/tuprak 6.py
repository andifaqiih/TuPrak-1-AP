class mahasiswa:
    def __init__(self, nama, nim, prodi, nilai_tugas, nilai_uts, nilai_uas):
        self.nama= nama
        self.nim= nim
        self.prodi= prodi
        self.nilai_tugas= nilai_tugas
        self.nilai_uts= nilai_uts
        self.nilai_uas= nilai_uas
     
    def nilaiakhir(self):
        return (0.3*self.nilai_tugas)+(0.3*self.nilai_uts)+(0.3*self.nilai_uas)
    def status_kelulusan(self):
        nilai_akhir = self.nilaiakhir()
        if nilai_akhir >= 60 :
            return  "Lulus ✅"
        else :
            return "Tidak Lulus ❌"
    def data_mahasiswa(self):
        print ("")
        print(f"Nama: {self.nama}")
        print(f"Nim : {self.nim}")
        print(f"Prodi: {self.prodi}")
        print(f"Nilai Tugas: {self.nilai_tugas}")
        print(f"Nilai UTS: {self.nilai_uts}")
        print(f"Nilai UAS : {self.nilai_uts}")
print("=== SISTEM DATA MAHASISWA ===")
jumlah_mahasiswa=int(input("Masukkan Jumlah Mahasiswa:")) 
daftar_mahasiswa=[]

for i in range (jumlah_mahasiswa):
    print(f"-- Mahasiswa ke-{i+1} --")
    nama=input("Nama: ")
    nim=input("NIM: ")
    prodi=input("Prodi: ")
    nilai_tugas=float(input("Nilai Tugas: "))
    nilai_uts=float(input("Nilai UTS: "))
    nilai_uas=float(input("Nilai UAS: "))
    mahasiswa_data=mahasiswa(nama,nim,prodi,nilai_tugas,nilai_uts,nilai_uas)
    daftar_mahasiswa.append(mahasiswa_data)
    print()

print("=== DAFTAR NILAI MAHASISWA ===")
print("="*100)
print(f"{'NO':<7} | {'NAMA':<20} | {'NIM':<15} | {'PRODI':<20} | {'NILAI AKHIR':<12} | {'STATUS':<15}") 
print("="*100)
nomor = 1
for mahasiswa_data in daftar_mahasiswa:
    print(f'| {nomor:<5} | {mahasiswa_data.nama:<20} | {mahasiswa_data.nim:<15} | {mahasiswa_data.prodi:<20} | {mahasiswa_data.nilaiakhir():<12.2f} | {mahasiswa_data.status_kelulusan():<15}')
    nomor += 1


