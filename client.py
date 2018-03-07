import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

n1 = int(input("Masukkan angka pertama: "))
n2 = int(input("Masukkan angka kedua: "))
print("1.tambah\n2.kurang\n3.bagi\n4.kali")
op = int(input("operator: "))

print(c.calc(n1, n2, op))
