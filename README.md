#README

Usage:
python broker.py [listenPortA=5566] [broadcastPortB=5577]
python receptor.py [roomToWatch=5] [hostBroker='localhost'] [portB=5577]
python coletor.py [hostBroker='localhost'] [portA=5566]

Example:
python broker.py 5678 8765
python receptor.py 3 '192.168.0.2' 8765 
python coletor.py '192.168.0.2' 5678

To watch every room in real time:
python receptor.py all '192.168.0.2' 8765 

The log for every room is kept in the file ./roomtemp.log
