import zerorpc
import calc2

def result(n1,n2,op):
    if op == 1:
        return "yey"

s = zerorpc.Server(result)
s.bind("tcp://0.0.0.0:4243")
s.run()
