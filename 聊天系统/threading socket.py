import threading,socket,time
import base64  
import os
def send():
    s=socket.socket()
    ip=input('输入本地IP:')
    dk=int(input('输入本地端口号:'))
    s.bind((ip,dk))
    s.listen()
    c,a=s.accept()
    print(a)
    qwe=input('`')
    while True:
        c.send(qwe.encode())
        qwe=input('`')
def recieve():
    ip=input('输入对方IP:')
    dk=int(input('输入对方端口号:'))
    s=socket.socket()
    s.connect((ip,dk))
    while True:
        qwe=s.recv(1024)
        print(qwe.decode())
threadone=threading.Thread(target=send)
threadtwo=threading.Thread(target=recieve)
threadone.start()
threadtwo.start()
threadone.join()
threadtwo.join()
