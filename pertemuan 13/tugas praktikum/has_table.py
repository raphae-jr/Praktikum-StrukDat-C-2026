class LibraryHashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, kode):
        unicode_sum = sum(ord(char) for char in kode)
        return unicode_sum % self.size

    def insert(self, kode, judul):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for item in bucket:
            if item[0] == kode:
                item[1] = judul 
                return
        
        bucket.append([kode, judul]) 

    def search(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for item in bucket:
            if item[0] == kode:
                return item[1]
        return "Buku tidak ditemukan"

    def delete(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for i, item in enumerate(bucket):
            if item[0] == kode:
                del bucket[i]
                return True
        return False

    def display(self):
        print("\n--- Isi Hash Table Perpustakaan ---")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
        print("-----------------------------------\n")

perpustakaan = LibraryHashTable()

perpustakaan.insert("BK111", "Mahir C++ Dalam Satu Jam")
perpustakaan.insert("BK222", "Python Dasar")
perpustakaan.insert("BK333", "Matematika Diskrit")
perpustakaan.insert("BK444", "Atomic Habits")

perpustakaan.display()

perpustakaan.insert("BK045", "Mein Kampf")
perpustakaan.insert("BK111", "Bumi Manusia") 

perpustakaan.display()

print(f"Cari BK222: {perpustakaan.search('BK222')}")
print(f"Cari BK999 (tidak ada): {perpustakaan.search('BK999')}")

perpustakaan.delete("BK333")
print("\n[BK333 Berhasil Dihapus]")

perpustakaan.display()