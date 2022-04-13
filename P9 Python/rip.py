from scapy.all import *

def rip_send(update):
    sendp(update)

eth = Ether()
ip = IP()
udp = UDP()
rip = RIP()
ripentry = RIPEntry()
update = eth/ip/udp/rip/ripentry
update[ip].src = '192.168.1.107'
update[ip].dst = '224.0.0.9'
update[UDP].sport = 520
update[UDP].dport = 520
update[RIP].cmd = 2
update[RIP].version = 2
update[RIPEntry].addr = '88.88.88.0'
update[RIPEntry].mask = '255.255.255.0'
update[RIPEntry].meteric = 5

rip_send(update)
print("sending packetto %s" %ip.dst + 'port Is %s'%update[IP].dst)
