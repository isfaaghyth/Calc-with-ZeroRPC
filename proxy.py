import zerorpc

c1 = zerorpc.Client()
c1.connect("tcp://127.0.0.1:4243")

c2 = zerorpc.Client()
c2.connect("tcp://127.0.0.1:4244")

class Hitung(object):
    def calc(self, n1, n2, op):
        if (op == 1): #tambah
            return c1.tambah(n1,n2)
        elif (op == 2): #kurang
            return c1.kurang(n1,n2)
        elif (op == 3): #bagi
            return c2.bagi(n1,n2)
        elif (op == 4): #kali
            return c2.kali(n1,n2)
        else:
            return 0


s = zerorpc.Server(Hitung())
s.bind("tcp://0.0.0.0:4242")
s.run()
