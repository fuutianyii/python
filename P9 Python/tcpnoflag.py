from scapy.all import *



def tcpnoflag(packet):
    sendp(packet)



eth = Ether()
ip = IP()
ip.dst="192.168.1.100"
tcp= TCP()
tcp.dport = 80

m = 0
for i in range(0,256):
    for j in range(0,256):
        for k in range(0,256):
            for l in range(0,256):
                for sp in range(0,65536):
                    ip.src=str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l)
                    tcp.sport = sp
                    packet=eth/ip/tcp
                    tcpnoflag(packet)
                    print("sending packetto %s" %ip.dst + 'port Is %s'%tcp.dport)
                    m=m+1
                    print(m)
    