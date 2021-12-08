import socket
s=socket.socket()
hostname=socket.gethostname()
IP=socket.gethostbyname(hostname)
print(IP)
part=1234
s.bind((hostname,part))
s.listen(5)
print("等待连接~")
while True:
    c,addr=s.accept()
    print("连接成功!")
    print("连接IP:",addr[0])
    print("输入:",end="")
    i=input()
    send_info = i.encode()
    c.send(send_info)
    c.close()