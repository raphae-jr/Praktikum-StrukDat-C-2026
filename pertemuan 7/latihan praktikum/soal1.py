data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
def pisah(Arr):
    ganjil = []
    genap = []

    for plat in Arr:

        isi = plat.split()
        nomor = int(isi[1][-1])

        if nomor % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)
            
    return ganjil, genap

ganjil, genap = pisah(data)

print("Plat Ganjil:", ganjil)
print("Plat Genap :", genap)