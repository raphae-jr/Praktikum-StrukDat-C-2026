class Tubuh:
    def __init__(self, tangan, kaki, kepala):
        self.tangan = tangan
        self.kaki = kaki
        self.kepala = kepala

    def bagian_1(self):
        print("ukuran tangan", self.tangan)

    def bagian_2(self):
        print("ukuran kaki", self.kaki)


p1 = Tubuh(1, 2, 3)

p1.bagian_1()
p1.bagian_2()

p1.kaki = 5
p1.bagian_2()
