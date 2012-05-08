#!/bin/python
import subprocess

# Invoking iwlist for scanning networks
# You would possibly want to change the device name
# TODO
scanData=subprocess.check_output(["iwlist","wlan0","scan"],shell=False)
# just for testing purposes
#print scanData

# splitting String
# wlan0     Scan completed :
#          Cell 01 - Address: 00:26:F2:CD:C5:56
#                    Channel:1
#                    Frequency:2.412 GHz (Channel 1)
#                    Quality=69/70  Signal level=-41 dBm  
#                    Encryption key:on
#                    ESSID:"FG-Info"
#                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 18 Mb/s
#                              24 Mb/s; 36 Mb/s; 54 Mb/s
#                    Bit Rates:6 Mb/s; 9 Mb/s; 12 Mb/s; 48 Mb/s
#                    Mode:Master
#                    Extra:tsf=0000048af6a0c386
#                    Extra: Last beacon: 1187806ms ago
#                    IE: Unknown: 000746472D496E666Fw
#                    IE: Unknown: 010882848B962430486C
#                    IE: Unknown: 030101
#                    IE: Unknown: 2A0100
#                    IE: Unknown: 2F0100
#                    IE: IEEE 802.11i/WPA2 Version 1
#                        Group Cipher : CCMP
#                        Pairwise Ciphers (1) : CCMP
#                        Authentication Suites (1) : PSK
#                    IE: Unknown: 32040C121860
#                    IE: Unknown: 2D1A7C181BFFFF000000000000000000000000000000000000000000
#                    IE: Unknown: 3D1601081500000000000000000000000000000000000000
#                    IE: Unknown: DD090010180201F0040000
#                    IE: Unknown: DD180050F2020101800003A4000027A4000042435E0062322F00
#
# probably wrong token?!
scanCells = scanData.split("Cell")
# accessing each cell
for cell in scanCells :
    print cell
    lines = cell.split("\n")
    for line in lines :
        # line matches "01 - Address: <MAC>"
        if(line

        # line matches ESSID:"<essid>"
