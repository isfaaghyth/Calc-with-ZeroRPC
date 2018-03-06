import zerorpc
import calc1
import calc2

class Hitung(object):
    def calc(self, n1, n2, op):
        if (op == 1): #tambah
            return(calc1.tambah(n1,n2))
        elif (op == 2): #kurang
            return(calc1.kurang(n1,n2))
        elif (op == 3): #bagi
            return(calc2.bagi(n1,n2))
        elif (op == 4): #kali
            return(calc2.kali(n1,n2))
        else:
            return(0)

s = zerorpc.Server(Hitung())
s.bind("tcp://0.0.0.0:4242")
s.run()
