from templogger import TemperatureLogger
import threading, time


def createReceptor(roomNumber,host,port):
    print('inicio thread %d' % roomNumber)
    r = TemperatureLogger(roomNumber,host,port)
    r.logTemperatureForever()

recipientes = []
threads = []
host = 'localhost'
port = 5556
for i in range(0,9):
    print(i)
    print('before x')
    x = threading.Thread(target=createReceptor, args=(i,host,port), daemon=True)
    print('before append')
    threads.append(x)
    print('before start')
    x.start()

while True:
    v = input()
    if v == 'q':
        break
