#!/usr/bin/python3
import sys
from scapy.all import sr1,RandShort,IP,TCP

usage = "Example: ./PortScan.py 127.0.0.1 20 80"

if len(sys.argv) != 4:
    print(usage)
    sys.exit(1)

rhost = sys.argv[1]
src_port = RandShort()

for rport in range(int(sys.argv[2]),int(sys.argv[3])+1):
    packet = IP(dst=rhost)/TCP(sport=src_port,dport=rport,flags='S')
    resp = sr1(packet,timeout=10)
    if str(type(resp)) == "<class 'NoneType'>":
        print('{} did not reply.'.format(rport))
    elif resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x14:
            print('{} is no open.'.format(rport))
        elif resp.getlayer(TCP).flags == 0x12:
            send_rst = sr1(IP(dst=rhost)/TCP(sport=src_port,dport=rport,flags="AR"),timeout=10)
            print('{} is open.'.format(rport))

print('End of operation')
sys.exit(0)

