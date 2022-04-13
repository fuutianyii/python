import socket
import time
print(socket.gethostbyname(socket.gethostname()))
s=socket.socket()
time.sleep(5)
s.connect(("192.168.103.1",12345))
with open("GUI.py","wb")as f:
    filen=s.recv(1024)
    while filen:
        f.write(filen)
        filen=s.recv(1024)

