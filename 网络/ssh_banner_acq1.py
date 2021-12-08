import socket
import optparse

def banneracq(host,port):
	try:
		conn = socket.socket()
		conn.connect((host,port))
		res = conn.recv(4096)
		print(res.decode("gb2312"))
		conn.close()
	except:
		pass

def main():
	parser = optparse.OptionParser('usage%prog ' + '-H <target host>'+'-P <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')
	(options, args) = parser.parse_args()
	host = options.tgtHost
	port = options.tgtPort
	if(host==None)|(port==None):
		print(parser.usage)
		exit()
	banneracq(host,port)


if __name__ == '__main__':
	main()











# #encoding: utf-8
# import socket
# import optparse

# def banneracq(host,port):
#     try:
#         conn=socket.socket()
#         conn.connect((host,port))
#         res=conn.recv(1024)
#         print(res.encode("gb2312"))
#         conn.close()
#     except:
#         pass

# def main():
#     parser=optparse.optionparser("usage%prog"+"-H <target host>"+"-P <target port>")
#     parser.add_option("-H",dest="tgtHost",type="string",help="specify target host")
#     parser.add_option("-P",dest="tgtPort",type="int",help="specify target port")
#     (option,args)=parser.parse_args()
#     host=option.tgtHost()
#     port=option.tgtPort()
#     if(host==None)|(port==None):
#         print(host,port)
#         exit()
#     banneracq(host,port)

# if __name__=="__main__":
#     main()


# PS F:\Desktop> python f:\Desktop\ssh_banner_acq1.py -H 172.16.1.234 -P 22
# SSH-2.0-OpenSSH_8.2p1 Debian-4