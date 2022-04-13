from scapy.all import *
import optparse
from sys import argv,exit
def sendpacket(packet,interface):
    result=[]
    ans,unans=srp(packet,timeout=1,iface=interface)#ans中有请求有响应,unans只有请求没有响应 返回一个元组
    for destination,source in ans: ##ans 同样是个元组
        result.append([source[ARP].psrc,source[ARP].hwsrc])
    for ip,mac in result:
        print(ip+"\t\t"+mac)
    



if((len(argv)==1)):
    print('''
1:Intel(R) Wireless-AC 9462
2:Realtek PCIe GbE Family Controller
3:VMware Virtual Ethernet Adapter for VMnet2
Usage: usage arp-scan -i 1 -r 172.16.1.0/24 -s yourip

Options:
  -h, --help    show this help message and exit
  -i INTERFACE
  -r RANGE
  -s SOURCE''')
    exit(0)
elif(((len(argv)>=2) & (argv[1] == "-h"))):
    print('''
1:Intel(R) Wireless-AC 9462
2:Realtek PCIe GbE Family Controller
3:VMware Virtual Ethernet Adapter for VMnet2
Usage: usage arp-scan -i 1 -r 172.16.1.0/24 -s yourip

Options:
  -h, --help    show this help message and exit
  -i INTERFACE
  -r RANGE
  -s SOURCE''')
    exit(0)
elif ((len(argv)>=2) & (argv[1] == "-l")):
    if argv[1] == "-l":
        interface="Realtek PCIe GbE Family Controller"
        mac=get_if_hwaddr(interface)
        try:
            ip=argv[2]+"/24"
        except IndexError:
            ip=get_if_addr(interface)+"/24"
else:
    opt=optparse.OptionParser("usage %prog -i 1 -r 172.16.1.0/24 -s yourip")
    opt.add_option("-i",dest="interface")
    opt.add_option("-r",dest="range")
    opt.add_option("-s",dest="source")
    (args,other)=opt.parse_args()
    if int(args.interface)==1:
        interface="Intel(R) Wireless-AC 9462"
    elif int(args.interface)==2:
        interface="Realtek PCIe GbE Family Controller"
    elif int(args.interface)==3:
        interface="VMware Virtual Ethernet Adapter for VMnet2"
    source=args.source
    print(interface)
    mac=get_if_hwaddr(interface)
    ip=args.range
    if ((interface == None) & (ip == None) & (source == None)):
        exit(0)

eth=Ether()
arp=ARP()
interface="Realtek PCIe GbE Family Controller"
packet=Ether(dst="FF:FF:FF:FF:FF:FF",src=mac)/ARP(pdst=ip)
sendpacket(packet,interface)
