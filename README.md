# Temperature Monitor

A distributed system to log the temperature data from any number of rooms in a building, and graph the data in real time.
Each node can be run from a different machine, as long as they are connected to the broker. Sensors publish the data in the topic of its room, and loggers are subscribed to the topic of one or more rooms.

    PUBS                              SUBS
    sensor[0]   -->           -->   logger[0]
    sensor[1]   -->   BROKER  -->   logger[1]
      ...                               ...
    sensor[N]   -->           -->   logger[N]

The data for a given room is graphed in realtime using the average temperature history and the timestamps in the log files.

`templogger.py`: A node which subscribes to a topic (room number) using ØMQ, and logs the average temperature and timestamp for every 10 measurements the sensor made.

`tempsensor.py`: A node which reads the (fictional) temperature for a given room at regular intervals and publishes it using ØMQ

`broker.py`: Simply a node running as ØMQ broker, it serves as a bridge between the sensors and the loggers.

`receptor.py`: An easier way to create multiple logger threads on the same machine.

`coletor.py`: An easier way to create multiple sensor threads on the same machine.

`visualClient.py`: A client to visualize the average temperature of a given room in real time.

With the notation of `command [optionalArgument=defaultvalue]`, the usage is:

    python broker.py [listenPortA=5566] [broadcastPortB=5577]
    python coletor.py [hostBroker='localhost'] [portA=5566]
    python receptor.py [roomToWatch=5] [hostBroker='localhost'] [portB=5577]

Example where the broker is running with the IP `192.168.0.1` and we want to watch the log and the graph in real time for room 3:

    python broker.py 5678 8765
    python coletor.py '192.168.0.2' 5678
    python receptor.py 3 '192.168.0.2' 8765 

To watch the log of every room in real time:

    python receptor.py all '192.168.0.2' 8765 

The log for every room is kept in the file `./roomtemp.log`

## Dependencies

- Matplotlib: [matplotlib](https://matplotlib.org/)
- ZeroMQ(ØMQ): [pyzmq](https://zeromq.org/languages/python/)
