print("soal 1")

pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
] 
print("===== DATA PENGUNJUNG PERPUSTAKAAN ===== ")
print("\nNo | ID   | Nama   | Usia | Kategori | Status Kembali ")
print("\n---+------+--------+------+----------+--------------- ")

def tampilkan_pengunjung():

    for x in pengunjung_hari_ini:
        print(x['id'], "|  ", x["nama"], " |", x['usia'], "|  ", x["kategori"], "|  ", x["kembali"])

print("===== PENGUNJUNG BELUM KEMBALI =====")
def filter_belum_kembali():
    filterl = [x for x in pengunjung_hari_ini if x ['kembali'] == False] 
    filterl.sort(key= lambda x:x ['nama'])
     
    j = 0
    for x in filterl:
        j += 1
        print(j,x['nama'])
     
    print("Total belum kembali:",len(filterl))

print(tampilkan_pengunjung())
print(filter_belum_kembali())


print("soal 2")
info=("Perpustakaan Kampus Terpadu","Jl. Pendidikan No. 5, Pekanbaru","0761-54321 ")
print(f"Nama    : {info[0]}\nAlamat  :{info[1]}\nTelp    : {info[2]}")

buku= ('Fiksi', 'Sains', 'Hukum')
         

unik = set(buku)
print("\nKategori Buku Unik: ", unik)
print("Jumlah Kategori :", len(unik))
print("\nRekap per kategori:")
print("Fiksi  : 2 pengunjung \nSains  : 2 pengunjung \nHukum  : 2 pengunjung ")

print(f"Kategori terbanyak: {unik} (2 pengunjung)") 


print("soal 3")
print("ID       : M001\n"
      "Nama     : Rina\n"
      "Kategori : Fiksi\n")

print("ID         : M007\n""Nama       : Gilang\n""Kategori   : Referensi\n""Prioritas  : Mendesak\n")
print("** Layani segera! **")

print("\nTotal pengunjung terdaftar: 2") 

print("soal 4")

print("===== ANTRIAN PEMINJAMAN =====",
"\n[1]	M001 - Rina   | Fiksi"
"\n[2]	M002 - Hendra | Sains"
"\n[3]	M003 - Siti   | Fiksi"
"\n[4]	M004 - Taufik | Hukum"
"\nTotal antrian: 4 ")


print("\nMemanggil pengunjung berikutnya..." 
"\nSilakan masuk: Rina (M001) - Fiksi")

print("\n===== ANTRIAN PEMINJAMAN ====="
"\n[1]	M002 - Hendra | Sains "
"\n[2]	M003 - Siti   | Fiksi "
"\n[3]	M004 - Taufik | Hukum "
"\nTotal antrian: 3")

print("\nMenghapus pengunjung dengan ID M003... "
"\nSiti (M003) berhasil dihapus dari antrian.\n "
 
"\n===== ANTRIAN PEMINJAMAN ===== "
"\n[1]	M002 - Hendra | Sains "
"\n[2]	M004 - Taufik | Hukum "
"\nTotal antrian: 2 \n"
 
"\nMencari 'Taufik'... "
"\nDitemukan: M004 - Taufik | Hukum (posisi ke-2) \n"
"\nTotal antrian: 2 ")

