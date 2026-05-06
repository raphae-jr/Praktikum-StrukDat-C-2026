class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self.insert_recursive(self.root, new_node)

    def insert_recursive(self, current, new_node):
        if new_node.id_buku < current.id_buku:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self.insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self.insert_recursive(current.right, new_node)

    def search(self, id_buku):
        result = self.search_recursive(self.root, id_buku)

        if result:
            print(f"[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {result.judul}")
        else:
            print(f"[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan.")

    def search_recursive(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id_buku:
            return current
        elif id_buku < current.id_buku:
            return self.search_recursive(current.left, id_buku)
        else:
            return self.search_recursive(current.right, id_buku)

    def traversal_inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self.inorder_recursive(self.root)

    def inorder_recursive(self, current):
        if current:
            self.inorder_recursive(current.left)
            print(f"{current.id_buku} - {current.judul}")
            self.inorder_recursive(current.right)

    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    def height(self):
        return self.height_recursive(self.root)

    def height_recursive(self, node):
        if node is None:
            return -1
        left = self.height_recursive(node.left)
        right = self.height_recursive(node.right)
        return max(left, right) + 1

bst = BST()
print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'\
\n=========================================")

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")
bst.traversal_inorder()

bst.search(60)
bst.search(100)

min_buku = bst.get_min()
max_buku = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id_buku}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id_buku}")

print(f"[INFO] Tinggi (Height) Tree: {bst.height()}")
print("=========================================\
\nSimulasi Selesai!")