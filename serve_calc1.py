import zerorpc

class Cal1(object):
    def tambah(self, n1,n2):
        print("ciee manggil tambah")
        return n1 + n2

    def kurang(self, n1,n2):
        print("ciee manggil kurang")
        return n1 - n2


s = zerorpc.Server(Cal1())
s.bind("tcp://0.0.0.0:4243")
s.run()
