'''
Created on May 5, 2012

@author: maximilian
'''

import dbus
import dbus.service
import sys
from wicd import misc
from SomeDataStructures import WlanScan

if getattr(dbus, 'version', (0, 0, 0)) < (0, 80, 0):
    import dbus.glib
else:
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
            
class EasyWICDInterface():
    def __init__(self):
        bus = dbus.SystemBus()
        try:
            self.wireless = dbus.Interface(bus.get_object('org.wicd.daemon', '/org/wicd/daemon/wireless'),
                    'org.wicd.daemon.wireless')
            
        except dbus.DBusException:
            print 'Error: Could not connect to the daemon. Please make sure it is running.'
            sys.exit(3)
            
    def scan(self):
        self.wireless.Scan(True)
       
    def getWlanScan(self):
        scan = WlanScan()
        for network_id in range(0, self.wireless.GetNumberOfNetworks()):
            scan.update({str(self.wireless.GetWirelessProperty(network_id, 'bssid')) : int(self.wireless.GetWirelessProperty(network_id, 'quality'))})
        return scan
        
        
    def printList(self):
        print '#\tBSSID\t\t\tChannel\tQuality\tESSID'
        for network_id in range(0, self.wireless.GetNumberOfNetworks()):
            print '%s\t%s\t%s\t%s\t%s' % (network_id,
                self.wireless.GetWirelessProperty(network_id, 'bssid'),
                self.wireless.GetWirelessProperty(network_id, 'channel'),
                self.wireless.GetWirelessProperty(network_id, 'quality'),
                self.wireless.GetWirelessProperty(network_id, 'essid'))

interface = EasyWICDInterface()
interface.scan()
interface.printList()

print interface.getWlanScan()
