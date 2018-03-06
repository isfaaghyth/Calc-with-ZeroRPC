import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

n1 = input("Masukkan angka pertama: ")
n2 = input("Masukkan angka kedua: ")
print("1.tambah\n2.kurang\n3.bagi\n4.kali")
op = input("operator: ")

print(c.calc(n1, n2, op))
