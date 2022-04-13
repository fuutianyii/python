import socket

print("输入需要通信的ip")
ip=input()
print("连接成功!!")
while True:
    s=socket.socket()
    s.connect((ip,1234))
    x=s.recv(1024)
    s.close()
    print(ip,":",x.decode())

