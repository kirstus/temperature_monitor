import sys
import zmq, time
from datetime import datetime
from ast import literal_eval

class TemperatureLogger:
    def __init__(self,roomNumber, ts, host='localhost',port=5577):
        #print('inicio de ', roomNumber)
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
        #print('subscribed')

    def logTemperature(self,N=10):
        #print('logging')
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
        while True:
            #time.sleep(1)
            total = 0
            for i in range (N):
                string = self.socket.recv()
                #print('recv: ',string)
                d = literal_eval(string[2:].decode())
                topic = d['sala']
                temp = d['temperatura']
                humidity = d['humidity']
                timerecv = d['timestamp']
                #print('sala',topic, 'this thread',self.topicfilter)
                #print('temperature',temp)
                #print('time',timerecv)
                #print('humidity',humidity)
                #topic, temp, humidity, timerecv = string.split()
                total += float(temp)
                #print(topic, temp, humidity, timerecv)
            averageTemp = total/N
            tempTuple = (self.topicfilter,"%.2f" % averageTemp,datetime.timestamp(datetime.now()))
            #print(total/N)
            #print(tempTuple)
            self.ts.insert(tempTuple)
            #f.write('%s %.2f %f' % (self.topicfilter, totalValue, datetime.timestamp(datetime.now())))
            if self.topicfilter == 1:
                print("Room: '%s' \tAvg temp: %.1fC \tTime: %.6f" % (self.topicfilter, total / N,datetime.timestamp(datetime.now())))

