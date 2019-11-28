import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import lindatp

class VisualClient:

    def __init__(self,ts):
        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        
        self.ts = ts
    
    # This function is called periodically from FuncAnimation
    def animate(self,i, xs, ys):
    
        # Read temperature (Celsius) from TMP102
        current = self.ts.getNext(self.roomNumber,self.index)
        if current is None:
            return
        temp = float(current[1])
        timestamp = dt.datetime.fromtimestamp(float(current[2]))
        #print('x: %s \t y: %.2f' % (timestamp,temp))
        self.index = current[-1]

    
        # Add x and y to lists
        #xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        #ys.append(temp_c)
        xs.append(timestamp.strftime('%H:%M:%S'))
        ys.append(temp)
    
        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]
    
        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys)
    
        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Temperature da sala %d' %  self.roomNumber)
        plt.ylabel('Temperatura (ºC)')
    
    def start(self,roomNumber):
        self.roomNumber = roomNumber
        first = self.ts.getFirst(self.roomNumber)
        #print(first)
        self.index= 0 if first is None else first[-1]
        baseTemp = float(first[1])
        timestamp = float(first[2])
        self.ax.autoscale(False)
        #plt.ylim(baseTemp-5,baseTemp+5)
        self.ax.set_ylim(15,35)
        xs = [timestamp]
        ys = [baseTemp]
        # Set up plot to call animate() function periodically
        self.ani = animation.FuncAnimation(self.fig, self.animate, fargs=(self.xs, self.ys), interval=1000)
        plt.show()
                                    
