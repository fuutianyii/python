import socket
import optparse

def calstrsec(str, pos, findstr):
    begin = pos
    while (str[pos] != findstr):
        pos = pos + 1    
    return pos - begin

def banneracq(host, port):
    try:
        conn = socket.socket()
        conn.connect((host, port))
        conn.send('GET / HTTP/1.1\r\n' + 'Host: '+host+'\r\n'+'Connection: Keep-Alive\r\n'+'\r\n')
        temp = []
        while True:
            res = conn.recv(1024)
            if not res:
                break
            temp.append(res)
            data = ''.join(temp)
            # print data[:]
            print (data[data.find('Server:',0,len(data)):data.find('Server:',0,len(data))+calstrsec(data, data.find('Server:',0,len(data)),'\r\n')])
            conn.close()
        conn.close()
    except:
        pass
    
def main():
    parser = optparse.OptionParser('usage %prog' + '-H <target host>  <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')
    (option, args) = parser.parse_args()
    host = option.tgtHost
    port = option.tgtPort
    if (host == None) | (port == None):
        print (parser.usage) 
        exit(0)
    banneracq(host, port)
    
if __name__ == "__main__":
    main()
    