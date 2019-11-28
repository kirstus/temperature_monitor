import zmq
from tempsensor import TemperatureSensor
import threading

def createSensor(roomNumber,socket):
    print('inicio thread %d' % roomNumber)
    s = TemperatureSensor(roomNumber,socket)
    s.broadcastTemperatureForever()

port = 5556

print('aaa')

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%d" % port)

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
