# Diberikan sebuah list yang merepresentasikan jumlah stok barang di gudang:
#stok = [15, 50, 30, 25, 40]
#1. Tambahkan stok baru sebesar 100 ke akhir list.
#2. Sisipkan angka 75 di posisi indeks ke-2.
#3. Urutkan list tersebut dari yang terbesar ke terkecil.
#4. Hitunglah nilai rata-rata dari seluruh stok tersebut.
5#. Tampilkan isi list setelah semua perubahan dilakukan.

stok = [15,50,30,25,40]
stok.insert(2,75)
stok.sort()
ratarata =sum(stok) / len(stok) 
print(stok)
print(ratarata)