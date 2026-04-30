# ================= DOUBLE LINKED LIST =================
#parkir dan hapus

class NodeDLL:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = NodeDLL(plat)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def tampilkan_maju(self):
        current = self.head
        print("[Maju]")
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        current = self.tail
        print("[Mundur]")
        while current:
            print(current.plat)
            current = current.prev

    def hapus_kendaraan(self, plat):
        current = self.head
        while current:
            if current.plat == plat:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next


# ================= CIRCULAR LINKED LIST =================

class NodeCLL:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = NodeCLL(nama)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def giliran_berikutnya(self, n):
        current = self.head
        for i in range(1, n + 1):
            print(f"Giliran {i}: {current.nama}")
            current = current.next


# ================= MAIN PROGRAM =================

# --- Double Linked List ---
dll = DoubleLinkedList()

dll.tambah_kendaraan("B 1111 AA")
dll.tambah_kendaraan("D 2222 BB")
dll.tambah_kendaraan("A 3333 CC")
dll.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
dll.tampilkan_maju()

dll.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
dll.tampilkan_maju()

print()
dll.tampilkan_mundur()


# --- Circular Linked List ---
print("\n=== Circular Linked List ===")

cll = CircularLinkedList()
cll.tambah_petugas("Andi")
cll.tambah_petugas("Budi")
cll.tambah_petugas("Citra")
cll.tambah_petugas("Dewi")

cll.giliran_berikutnya(6)