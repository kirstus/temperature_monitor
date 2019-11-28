import zmq
from tempsensor import TemperatureSensor
import threading
import sys

def createSensor(roomNumber,socket):
    print('inicio thread %d' % roomNumber)
    s = TemperatureSensor(roomNumber,socket)
    s.broadcastTemperatureForever()

host = 'localhost'
port = 5566
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

print('aaa')

context = zmq.Context()
socket = context.socket(zmq.PUB)
#socket.bind("tcp://*:%d" % port)
socket.connect("tcp://%s:%d" % (host,port))

threads = []
salas = []
for i in range(0,9):
    x = threading.Thread(target=createSensor, args=(i,socket), daemon=True)
    print('before append')
    threads.append(x)
    print('before start')
    x.start()
    #salas.append(TemperatureSensor(i,socket))
    #salas[i].broadcastTemperature()
#salas[1].broadcastTemperatureForever()

while True:
    v = input()
    if v == 'q':
        break
