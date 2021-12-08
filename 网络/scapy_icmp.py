from scapy.all import *

def sendp(packet):
    respacket=sr(packet,timeout=1)
    print(respacket[0][0][1][0].fields["dst"])#原理相同
    print(respacket[0].res[0][1][0].fields["src"])#原理相同


icmp=ICMP()
ip=IP()
ip.dst="172.17.169.129"
mypacket=ip/icmp
sendp(mypacket)