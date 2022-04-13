from scapy.all import *

ip=IP()
eth=Ether()
tcp=TCP()
ip.dst=''
tcp.flags=0
tcp.dport=80
m=0

def tcpnoflgs(packet):
    sendp(packet)

for i1 in range(0,256):
    for i2 in range(0,256):
        for i3 in range(0,256):
            for i4 in range(0,256):
                for port in range(0,65536):
                    ip.src=str(i1)+'.'+str(i2)+'.'+str(i3)+'.'+str(i4)
                    tcp.sport=port
                    packet=eth/ip/tcp
                    print(ip.src+""+tcp.sport)
                    m=m+1
                    print(m)