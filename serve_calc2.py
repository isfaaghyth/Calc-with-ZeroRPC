import zerorpc

class Cal2(object):
    def bagi(self, n1, n2):
        print("ciee manggil bagi")
        return n1 / n2

    def kali(self, n1, n2):
        print("cocuit, manggil kali")
        return n1 * n2


s = zerorpc.Server(Cal2())
s.bind("tcp://0.0.0.0:4244")
s.run()
