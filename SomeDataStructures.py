'''
Created on Apr 15, 2012

@author: maximilian
'''

#
# !!! Ignore the first two classes for now. We do not need them for functionallity
#

class CellManager(dict):
    '''This class might later be our database of all the cells that were ever scanned.
    It is basically a dictionary that maps mac adresses to Cell objects'''    
    def addCell(self, cell):
        if(cell in self):
            return
        self.update({cell.mac : cell})
        
    def getCell(self, mac):
        return self[mac]

class Cell:
    '''This class just holds information about a wlan network. It does not store
    the quality of the network because that changes everytime we move around.'''
    def __init__(self, mac, long = None, lat = None, essid = None):
        self.mac = mac
        self.long = long
        self.lat = lat
        self.essid = essid
            
    def __eq__(self, other):
        '''Implementation of equals operator '==' '''
        return self.mac == other.mac
        
        
    def __ne(self, other):
        '''Implementation of the not equals operator '!=' '''
        return self.mac != other.mac
            
    
    def __repr__(self):
        '''gives a string representation of the Cell'''
        return self.mac
    
        
#
#    !!! Here the interesting classes start. Ignore the boring stuff above
#
        
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
    '''This Class represents a room at our university.
    It mainly holds a name, and a list with WlanScans, that are associated with
    this room'''
      
    def __init__(self, name, location=None):
        '''location is optional'''
        self.name = name
        self.location = location
        self.wlanScans = []
        
    def addWlanScan(self, scan):
        '''Adds another WlanScan to be associated with this room'''
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
    
    
    