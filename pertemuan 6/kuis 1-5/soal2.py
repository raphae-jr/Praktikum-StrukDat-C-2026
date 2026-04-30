stok_gadget = [ 
 {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},  
 {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},  
 {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},  
 {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, ] 

def filter_harga(data, min_harga, max_harga):
    filter_harga(min_harga= int)
    filter_harga(max_harga= str)
min_harga = stok_gadget[1],[2]
max_harga = stok_gadget[3],[2]

masukan1 = int(input("Masukan Batas Bawah"))
masukan = int(input("Masukan Batas Atas"))
if  min_harga == masukan:
    print("Tidak ada gadget dalam rentang harga  tersebut." )
elif max_harga == masukan1:
    print("Tidak ada gadget dalam rentang harga  tersebut." )
else: print(stok_gadget)


