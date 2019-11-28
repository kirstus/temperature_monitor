from templogger import TemperatureLogger
import threading, time, sys
import lindatp, visualClient

class Receptor:
    def __init__(self,host='localhost',port=5577,roomToWatch=1):
        self.ts = lindatp.lindatp()
        self.threads = []
        self.host = host
        self.port = port
        self.roomToWatch = roomToWatch

    def createReceptor(self,roomNumber,ts,host,port):
        print('iniciando receptor %d' % roomNumber)
        r = TemperatureLogger(roomNumber,ts,host,port,watch=(roomNumber==self.roomToWatch))
        r.logTemperatureForever()

    def createThreads(self,N=9):
        for i in range(0,N):
            print(i)
            x = threading.Thread(target=self.createReceptor, args=(i,self.ts,self.host,self.port), daemon=True)
            self.threads.append(x)
            x.start()

    def startClient(self):
        self.c = visualClient.VisualClient(self.ts)
        print('iniciando cliente visual...')
        self.c.start(self.roomToWatch)

    def __exit__(self, exc_type, exc_value, traceback):
        self.ts.exit()

    def exit(self):
        self.ts.exit()

if __name__=='__main__':
    host = 'localhost'
    port = 5577
    roomToWatch = 5

    if len(sys.argv) > 1:
        roomToWatch =  sys.argv[1]
        roomToWatch = int(roomToWatch)

    if len(sys.argv) > 2:
        host =  sys.argv[2]

    if len(sys.argv) > 3:
        port =  sys.argv[3]
        port = int(port)

    rcp = Receptor(host,port,roomToWatch)
    rcp.createThreads()
    time.sleep(3)
    rcp.startClient()
    while True:
        v = input()
        if v == 'q':
            rcp.exit()

