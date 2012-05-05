'''
Created on Apr 15, 2012

@author: maximilian
'''


class CellManager(dict):
    
    def addCell(self, cell):
        if(cell in self):
            return
        self.update({cell.mac : cell})
        
    def getCell(self, mac):
        return self[mac]

class Cell:
    
    def __init__(self, mac, long = None, lat = None, essid = None):
        self.mac = mac
        self.long = long
        self.lat = lat
        self.essid = essid
            
    def __eq__(self, other):
        return self.mac == other.mac
        
        
    def __ne(self, other):
        return self.mac != other.mac
            
    
    def __repr__(self):
        return self.mac
    
        
class WlanScan(dict):

    def distanceTo(self, otherWlanScan):
        distance = 0
        for cell in set(self).union(otherWlanScan):
            distance = distance + abs(self.getSignalStrength(cell) - otherWlanScan.getSignalStrength(cell))**2
        return distance
            
    def getSignalStrength(self, mac):
        if (mac in self): 
            return self[mac]
        else:
            return 0

class Room():
    """This Class represents a room at our university"""  
    def __init__(self, name, location=None):
        self.name = name
        self.location = location
        self.wlanScans = []
        
    def addWlanScan(self, scan):
        self.wlanScans.append(scan)
        
    def distanceTo(self, wlanScan):
        distances = []
        for scan in self.wlanScans:
            distances.append(wlanScan.distanceTo(scan))
        return min(distances)
    
if __name__ == '__main__':
    mgr = CellManager()
    mgr.addCell(Cell("c1"))
    mgr.addCell(Cell("c2"))
    
    scan = WlanScan({"c1":1, "c2":2})
    scan2 = WlanScan({"c4": 9, "c2":2})
    scan3 = WlanScan({"c4": 7, "c2":2})
    
    r = Room
    print r
    
    print scan.distanceTo(scan2)
    print scan2.distanceTo(scan3)
    
    print "c2" in scan
    
    
    