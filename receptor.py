from templogger import TemperatureLogger
import threading, time
import lindatp


def createReceptor(roomNumber,ts,host,port):
    print('inicio thread %d' % roomNumber)
    r = TemperatureLogger(roomNumber,ts,host,port)
    r.logTemperatureForever()

ts = lindatp.lindatp()
recipientes = []
threads = []
host = 'localhost'
port = 5577
for i in range(0,9):
    print(i)
    print('before x')
    x = threading.Thread(target=createReceptor, args=(i,ts,host,port), daemon=True)
    print('before append')
    threads.append(x)
    print('before start')
    x.start()

while True:
    v = input()
    if v == 'q':
        break
