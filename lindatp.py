import hashlib, binascii, os, time

# tuple = (autor, topico, msg, [ ... ,]* time_sent, msg_number)
class lindatp():
    def __init__(self):
        self.tuplespace = {}
        #self.log = open('roomtemp.log','r+')
        #self.import_tuples()
        #self.log.close()
        self.log = open('roomtemp.log','w')
        #self.tuples.write('oi\n')
        #self.tuples.write('nice\n')

    def __del__(self):
        #if self.tuplespace != {}:
            #self.export_tuples()
        #self.tuples.write('tchau\n')
        self.log.close()

    def __exit__(self, exc_type, exc_value, traceback):
        #if self.tuplespace != {}:
            #self.export_tuples()
        #self.tuples.write('tchau\n')
        self.log.close()

    def exit(self):
        self.__del__()

    def export(self):
        for topic in self.tuplespace:
            for t in self.tuplespace[topic]:
                self.log.write(pack(t)+'\n')

    def import_tuples(self):
        for l in self.tuples.readlines():
            t = unpack(l)
            #print(tuple(t))
            self.insert(tuple(t))
        for l in self.passwd.readlines():
            t = unpack(l)
            #print(tuple(t))
            self.insertpasswd(tuple(t))
        for l in self.msgnum.readlines():
            t = unpack(l)
            #print(tuple(t))
            self.insertnumbers(tuple(t))

    def insert(self, t):
        indice = self.tuplespace
        topic = t[0]

        if topic not in self.tuplespace:
            r = t+(0,)
            log = {t[0]: [r]}
            self.tuplespace = {**self.tuplespace,**log}
        else:
            r = t + (len(self.tuplespace[topic]),)
            self.tuplespace[topic].append(r)
        #print('pack',self.pack(r)+'\n')
        self.log.write(self.pack(r)+'\n')
        return(r[-1])

    def pack(self,t):
        data = ''
        for elem in t:
            data += str(elem) + ' '
        return data[:-2]

    def getFirst(self,topic):
        if topic not in self.tuplespace:
            return None
        return self.tuplespace[topic][0]

    def getNext(self,topic,offset=0):
        if topic not in self.tuplespace:
            return None
        if offset >= len(self.tuplespace[topic])-1:
            return None
        return self.tuplespace[topic][offset+1]

if __name__ == '__main__':
    lnd = lindatp()
    b = ('borg','um',29, 0, )
    bb = ('borg','dois',26, 0)
    d = ('blop','ayo',30, 0, )
    e = ('prope','ayo',99, 0, 0)
    a = (2,2,5, 0, 0)
    print('b: ',b)
    print('bb: ',bb)
    i = lnd.insert(b)
    print(i)
    k = lnd.insert(d)
    print(k)
    j = lnd.insert(bb)
    print(j)
    a = lnd.getFirst('borg')
    aa = lnd.getNext('borg',a[-1])
    print(a)
    print(aa)
