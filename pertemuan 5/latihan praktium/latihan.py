stok_barang = [15, 40, 30, 10, 25]
stok_barang[3]= 50
stok_barang.append(5)
stok_barang.sort(reverse=True)
stok_barang1 = sum(stok_barang)
print(stok_barang1)
print ("stok aman") if stok_barang1>20 else ("waspada")

data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for Nama in data_aktivitas:
    if Nama[1] > 80:
        print(f'{Nama[0]},mendapatkan Gold.')
    elif Nama[1]>50:
        print(f'{Nama[0]}, mendapatkan  Silver')
    else:
        print(f'{Nama[0]}, mendapatkan Bronze')


ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print(ukm_coding.difference(ukm_coding))
print(ukm_coding|ukm_robotik)

def cek(a):
    if a in ukm_robotik:
        return True
    
cek('andi')


gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

print(gudang_pc[0]["item"])
gudang_pc[1]["kategori"]= "aksesoris"
print(gudang_pc)
gudang_pc.append({"item":"headset","harga":3500,"stok": 8})
print(gudang_pc)
for x in range(len(gudang_pc)):
    print(f'item: {gudang_pc[x]["item"]} total ={gudang_pc[x]["harga"]*gudang_pc[x]["stok"]}')