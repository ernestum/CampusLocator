'''
Created on May 8, 2012

@author: maximilian
'''
from WicdConnecting import EasyWICDInterface
from SomeDataStructures import *

interface = EasyWICDInterface()

roomList = dict()

name = None
actualRoom = None
s = "n"
while True:
    if(s == "n"):
        name = raw_input("Name des Raums:")
        if(roomList.has_key(name)):
            actualRoom = roomList[name]
        else:
            actualRoom = Room(name)
            roomList[name] = actualRoom
    elif(s == "l"):
        interface.scan()
        wlanScan = interface.getWlanScan()
        minDistance = actualRoom.distanceTo(wlanScan)
        closestRoom = actualRoom
        for room in roomList:
            d = room.distanceTo(wlanScan)
            if(d < minDistance):
                minDistance = d
                closestRoom = room
        print "Naechter Raum: " + str(closestRoom.name)
    else:
        print "Scannen..."
        interface.scan()
        actualRoom.addWlanScan(interface.getWlanScan())
        print "Neue informationen ueber " + str(actualRoom.name) + " hinzugefuegt"
    s = raw_input()
    