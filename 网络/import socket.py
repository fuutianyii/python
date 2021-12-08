import socket
import optparse

def calstrsec(str,pos,findstr):
    begin=pos
    while(str[pos]!=findstr):
        pos=pos+1
    return pos-begin

def banneracq(host,post):
    try:
        conn=s.s()
        conn.c((host,post))
        conn.send("GET / HTTP/1.1\r\nHost: "+host+"\r\nConnection: Keep-Alive")
        temp=[]
        
        while True:
            res=conn.recv(1024)
            temp.append(res)
            data="".join(temp)
            print(data[data.find("Server: ",0,len(data)):data.find("Server: ",0,len(data))+calstrsec(data,data.find("Server: ",0,len(data)),"\r\n")])
            conn.close()
        conn.close()
    except:
        pass
    

def main():
    parser=optparse.OptionParser("自己想,自己查")
    parser.add_option("-H",dest="host")
    parser.add_option("-S",dest="post")
    option,args=parser.parse_args()
    host=option.host
    post=option.post
    if (host==None)|(post==None):
        print(parser.usage)
        exit(0)
    banneracq(host,post)

if __name__=="__main__":
    main()
