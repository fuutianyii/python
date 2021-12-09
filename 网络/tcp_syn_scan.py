
from scapy.all import *
from threading import Thread

def sendpacket(packeter):
    (ans,unans)=sr(packeter,timeout=1,iface="Realtek PCIe GbE Family Controller",verbose=0)
    for (send,recv) in ans:
        if recv["TCP"].fields["flags"]=="SA":
            print(str(recv["TCP"].fields["sport"])+" is open")
        elif recv["TCP"].fields["flags"]=="RA":
            print(str(recv["TCP"].fields["sport"])+" is close")
    for (send) in unans:
            print(str(send["TCP"].fields["dport"])+" is filter")
            
ip=IP()
ip.src="172.17.169.146"
ip.dst="172.17.169.157"

for port in range(445,449):
# for port in range(446,447):
# for port in range(0,65535):
    tcp=TCP()
    tcp.dport=port
    tcp.sport=556
    tcp.flags="S"
    packeter=ip/tcp
    scan=Thread(target=sendpacket,args=(packeter,))
    scan.start()