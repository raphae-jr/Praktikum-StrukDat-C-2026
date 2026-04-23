class StackList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.isEmpty():
            return"riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "riwayat kosong"
        return self.items[-1]
    
    def size(self):
        return len(self.items)

riwayat = StackList()

riwayat.push("idnonesia emas 2045")
riwayat.push("prabowo 2 periode")
riwayat.push("indonesia emas 2050")
riwayat.push("amerika runtuh")
print("Stack: ", riwayat.items)
print("Pop: ", riwayat.pop())
print("Stack after Pop: ", riwayat.items)
print("Peek: ", riwayat.peek())
print("isEmpty: ", riwayat.isEmpty())
print("Size: ", riwayat.size())