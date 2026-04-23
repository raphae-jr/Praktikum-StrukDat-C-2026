stack = []
stack.append("idnonesia emas 2045")
stack.append("prabowo 2 periode")
stack.append("indonesia emas 2050")
stack.append("amerika runtuh")

print("Stack: ",stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

popelement = stack.pop()
print("pop: ",popelement)

topelement = stack[-1]
print("peek: ",topelement)

print("riwayat terbaru: ",stack)

print("Jumlah riwayat: ", len(stack))