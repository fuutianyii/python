import sys
if len(sys.argv) !=2:
    print "Usage:arpPing <IP>\n eg:arpPing 192.168.0.1"
    sys.exit(1)
    #使用nmap模块扫描，这个库的核心类为PortScanner，-PR表示使用了ARP，-sn表示测试主机状态。
import nmap
nm = nmap.PortScanner()
nm.scan(sys.argv[1], arguments='-sn -PR')
for host in nm.all_hosts():
    print('---------------------------')
    print('Host:%s(%s)'%(host,nm[host].hostname()))
    print('State:%s'% nm[host].state())
