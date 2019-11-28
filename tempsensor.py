import zmq
import random
import sys
import time

class TemperatureSensor:

    def toJSON(self,d):
        j = {   'sala':         d[0],
                'temperatura':  d[1],
                'humidity':     d[2],
                'timestamp':    d[3]
            }
        return j

    def __init__(self,roomNumber,host,port):
        print('oi')
        #self.port = port
        self.topic = roomNumber
        #self.context = zmq.Context()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        #socket.bind("tcp://*:%d" % port)
        self.socket.connect("tcp://%s:%d" % (host,port))
        #self.socket = self.context.socket(zmq.PUB)
        #self.socket = socket
        #random.seed(str(self))
        self.roomtemp = random.randrange(200,280)/10     # temperatura inicial da sala

    def broadcastTemperature(self):
        self.roomtemp += (random.randrange(0,200)-100)/10000 * self.roomtemp
        self.humidity = random.randrange(600,920)/10

        self.a = self.toJSON([self.topic,self.roomtemp,self.humidity,1])
        print(self.a)
        print("%d %f" % (self.topic,self.roomtemp))
        self.socket.send("%d %f %d".encode('ascii') % (self.topic,self.roomtemp,self.humidity))
        #socket.send("%d %d" % (topic, messagedata))

    def broadcastTemperatureForever(self):
        t = 1
        while True:
            self.roomtemp += (random.randrange(0,200)-100)/10000 * self.roomtemp
            self.humidity = random.randrange(600,920)/10
            t += 1
            self.a = self.toJSON([self.topic,self.roomtemp,self.humidity,t])
            print(self.a)
            print("%d %f" % (self.topic,self.roomtemp))
            self.socket.send("%d %f %d %d".encode('ascii') % (self.topic,self.roomtemp,self.humidity,t))
            #socket.send("%d %d" % (topic, messagedata))
            time.sleep(1)
