import zerorpc

c = zerorpc.Client()
c.connect("tcp://10.107.247.255:4243")

n1 = input("masukkan angka pertama: ")
n2 = input("masukkan angka kedua: ")
print "1.tambah\n2.kurang\n3.bagi\n4.kali"
op = input("operator (1..4): ")

print c.result(n1,n2,op)
