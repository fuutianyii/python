import sys
if len(sys.argv) !=2:
    print "Usage:arpPing <IP>\n eg:arpPing 192.168.0.1"
    sys.exit(1)
    #ʹ��nmapģ��ɨ�裬�����ĺ�����ΪPortScanner��-PR��ʾʹ����ARP��-sn��ʾ��������״̬��
import nmap
nm = nmap.PortScanner()
nm.scan(sys.argv[1], arguments='-sn -PR')
for host in nm.all_hosts():
    print('---------------------------')
    print('Host:%s(%s)'%(host,nm[host].hostname()))
    print('State:%s'% nm[host].state())
