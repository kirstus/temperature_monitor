import sys
import zmq, time
from datetime import datetime

class TemperatureLogger:
    def __init__(self,roomNumber, ts, host='localhost',port=5556):
        print('inicio de ', roomNumber)
        self.host = host
        self.port = port
        self.topicfilter = roomNumber
        self.ts = ts

        # Socket to talk to server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        #print("Collecting updates from weather server...")

        self.socket.connect ("tcp://%s:%d" % (self.host,self.port))

        # Subscribe to room
        self.socket.setsockopt(zmq.SUBSCRIBE, str(self.topicfilter).encode()) # subscribe to a room
        print('subscribed')

    def logTemperature(self,N=10):
        print('logging')
        # Process N updates
        total_value = 0
        string = ''
        for update_nbr in range (N):
            try:
                string = self.socket.recv(zmq.NOBLOCK)
                topic, temp, humidity = string.split()
                total_value += float(temp)
                print(topic, temp, humidity)
            except  zmq.Again as e:
                err = e.args[0]
                print(e)
                print('No data available')
                break

        print(total_value/N)

        print("Average temperature value for topic '%s' was %.1fC at" % (self.topicfilter, total_value / N), time.asctime())
        return total_value/N

    def logTemperatureForever(self,N=10):
        # Process N updates
        print('logging forever for room %d' % (self.topicfilter))
        with open('roomtemp.log','w') as f:
            while True:
                #time.sleep(1)
                totalValue = 0
                for update_nbr in range (N):
                    string = self.socket.recv()
                    topic, temp, humidity, timerecv = string.split()
                    totalValue += float(temp)
                    #print(topic, temp, humidity, timerecv)
                #print(totalValue/N)
                f.write('%s %.2f %f' % (self.topicfilter, totalValue, datetime.timestamp(datetime.now())))
                if self.topicfilter == 6:
                    print("Room: '%s' \tTemp: %.1fC \tTime: " % (self.topicfilter, totalValue / N),datetime.timestamp(datetime.now()))

