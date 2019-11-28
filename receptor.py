from templogger import TemperatureLogger
import threading, time, sys
import lindatp

class Receptor:
    def __init__(self,host='localhost',port=5577):
        self.ts = lindatp.lindatp()
        self.threads = []
        self.host = host
        self.port = port

    def createReceptor(self,roomNumber,ts,host,port):
        print('inicio thread %d' % roomNumber)
        r = TemperatureLogger(roomNumber,ts,host,port)
        r.logTemperatureForever()

    def createThreads(self,N=9):
        for i in range(0,N):
            print(i)
            x = threading.Thread(target=self.createReceptor, args=(i,self.ts,self.host,self.port), daemon=True)
            self.threads.append(x)
            x.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.ts.exit()

    def exit(self):
        self.ts.exit()

if __name__=='__main__':
    host = 'localhost'
    port = 5577

    if len(sys.argv) > 1:
        host =  sys.argv[1]

    if len(sys.argv) > 2:
        port =  sys.argv[2]
        int(port1)

    rcp = Receptor(host,port)
    rcp.createThreads()
    while True:
        v = input()
        if v == 'q':
            rcp.exit()

