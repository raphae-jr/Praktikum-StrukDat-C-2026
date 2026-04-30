# main.py

from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

# Tampilkan tabel kurs
table = [[kode, f"{nilai:,}".replace(",", ".")] for kode, nilai in kurs.items()]
print(tabulate(table, headers=["Kode", "Kurs"], tablefmt="grid"))

print()

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(dari, ke, jumlah)

if ke == "IDR":
    print(f"\n{jumlah:,.0f} {dari} = Rp {hasil:,.0f}".replace(",", "."))
else:
    print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {ke}".replace(",", "."))