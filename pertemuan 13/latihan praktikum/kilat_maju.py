class Graph:
    def __init__(self):
        self.nodes = {}

    def tambah_kota(self, nama):
        if nama not in self.nodes:
            self.nodes[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.nodes[u].append((v, jarak))
        self.nodes[v].append((u, jarak))

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota, tetangga in self.nodes.items():
            koneksi = ", ".join([f"{t[0]} ({t[1]})" for t in tetangga])
            print(f"{kota} terhubung ke: {koneksi}")

    def dijkstra(self, kota_asal):
        distances = {kota: float('inf') for kota in self.nodes}
        distances[kota_asal] = 0
        
        visited = set()
        unvisited = list(self.nodes.keys())

        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}")

        while unvisited:
            current_node = None
            for node in unvisited:
                if current_node is None or distances[node] < distances[current_node]:
                    current_node = node

            if distances[current_node] == float('inf'):
                break

            for tetangga, bobot in self.nodes[current_node]:
                jalur_baru = distances[current_node] + bobot
                if jalur_baru < distances[tetangga]:
                    distances[tetangga] = jalur_baru

            unvisited.remove(current_node)
            visited.add(current_node)

        return distances

navigasi = Graph()

print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')

jalan_data = [
    ("Jakarta", "Bandung", 150),
    ("Jakarta", "Cirebon", 200),
    ("Bandung", "Tasikmalaya", 100),
    ("Bandung", "Cirebon", 130),
    ("Cirebon", "Semarang", 250),
    ("Tasikmalaya", "Semarang", 200)
]

for u, v, d in jalan_data:
    print(f"[INPUT] Menambahkan jalan: {u} ke {v} ({d} km)")
    navigasi.tambah_jalan(u, v, d)

navigasi.tampilkan_graph()

hasil_jarak = navigasi.dijkstra("Jakarta")

print("\n[HASIL] Jarak Terpendek dari Jakarta:")
i = 1
for kota, jarak in hasil_jarak.items():
    if kota != "Jakarta":
        print(f"{i}. Ke {kota}: {jarak} km")
        i += 1

print("\nSimulasi Navigasi Selesai!")