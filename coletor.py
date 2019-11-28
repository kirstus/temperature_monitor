import zmq
from tempsensor import TemperatureSensor
import threading
import sys

def createSensor(roomNumber,host,port):
    print('inicio thread %d' % roomNumber)
    s = TemperatureSensor(roomNumber,host,port)
    s.broadcastTemperatureForever()

host = 'localhost'
port = 5566
if len(sys.argv) > 1:
    host =  sys.argv[1]

if len(sys.argv) > 2:
    port =  sys.argv[2]
    port = int(port)

threads = []
salas = []
for i in range(0,9):
    x = threading.Thread(target=createSensor, args=(i,host,port), daemon=True)
    threads.append(x)
    x.start()
    #salas.append(TemperatureSensor(i,socket))
    #salas[i].broadcastTemperature()
#salas[1].broadcastTemperatureForever()

while True:
    v = input()
    if v == 'q':
        break
