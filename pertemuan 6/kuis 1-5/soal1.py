def registrasi_gadget(merk, tipe, harga, sn):
    registrasi_gadget(harga= float)
    registrasi_gadget(sn= str)

sn = str(input('masukan kode seri='))
harga = float(input("Masukan Harg="))

if harga < 10000000:
    print("Masukan Harga minimal 1 juta")
elif sn < str(4):
    print("minimal 5 huruf")
else:
    print('tersedia')
                 
