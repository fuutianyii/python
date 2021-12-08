from scapy.all import *
import Flag1
#Flag1
eth = F1
eth.Flag3 = F2
#Flag2=F1.F2
#Flag3
eth.F3 = F4
#Flag4=F3.F4
arp = F5
arp.F6 = F10
arp.F7 = 'ARP Spoof Target IP'
F8 = F9
#Flag5=F5.F6.F7.F8.F9.F10.F11

while True:
	F11(packet)
	print('Sending ARP Spoof......')
	Flag1.sleep(2)


