class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queuell:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0 

    def enqueu(self, nama, keluhan): 
        data_lengkap = f"{nama},{keluhan}"
        new_node = node(data_lengkap)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Antrian kosong,kosong" 

        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Kosong,Kosong"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        if not temp:
            print("Antrian Kosong")
            return
        while temp:
            print(f"[{temp.data}]", end=" , ")
            temp = temp.next
        print("None")
        
    def clear(self):
        print("\nSesi poliklinik selesai. Antrian dikosongkan...")
        while not self.isEmpty():
            self.dequeue()

Antrian = queuell()
Antrian.enqueu("ANI", "batuk pilek")
Antrian.enqueu("CITRA", "sakit kepala")
Antrian.enqueu("DODI", "nyeri perut")

print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================")

print(f"\nApakah antrian kosong?")
      
if Antrian.isEmpty():
    print(" | Ya, masih kosong")
else: 
    print(" | tidak, Ada antrian")
    
print(f'Jumlah pasien menunggu: {Antrian.length} orang')

nama, keluhan = Antrian.peek().split(",")
print(f'Pasien berikutnya: {nama} _ {keluhan}')

nama1, keluhan1 = Antrian.dequeue().split(",")
print(f'Dokter memanggil: {nama1} _ {keluhan1}')

Antrian.enqueu('EKO', 'sakit gigi') 
Antrian.printQueue()

nama1, keluhan1 = Antrian.dequeue().split(",")
print(f'Dokter memanggil: {nama1} _ {keluhan1}')
print(f'Jumlah pasien menunggu: {Antrian.length} orang')

Antrian.clear()
if Antrian.isEmpty():
    print('Status: Antrean sekarang kosong')