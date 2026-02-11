#2. Diberikan sebuah tuple barang:
#barang = ("B001", "Laptop Gaming", 15000000)
#1. Akses dan tampilkan harga barang dari tuple tersebut.
#2. Cobalah untuk mengubah harga barang menjadi 14000000. Jelaskan dalam
#komentar kode mengapa hal ini menyebabkan error (Gunakan comment).
#3. Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga
#variabel: kode, nama, dan harga.

barang = ("b001", "laptop gaming", 15000000)
(kode,nama,harga) = barang
# barang[2]='14000000'
#karena tuple bersifat unchangeable. tidak bisa diganti
print(harga)

