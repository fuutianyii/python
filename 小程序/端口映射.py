'''
Author: fuutianyii
Date: 2023-04-09 14:57:03
LastEditors: fuutianyii
LastEditTime: 2023-04-09 15:29:41
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

from os import system
from tkinter import Frame, Label, Button, Entry, Tk, RIGHT, LEFT

class Port_forward:
    def __init__(self):
        root = Tk()
        root.geometry("300x250")
        root.title("端口映射")
        server_ip=Frame(root)
        iptext=Label(server_ip,text="已有服务ip:",width=10,height=2)
        iptext.pack(side=LEFT)
        server_ipinput=Entry(server_ip)
        server_ipinput.pack(side=RIGHT)
        server_ipinput.insert(0,"127.0.0.1")
        server_ip.pack()
        
        server_port=Frame(root)
        iptext=Label(server_port,text="已有服务port:",width=10,height=2)
        iptext.pack(side=LEFT)
        server_portinput=Entry(server_port)
        server_portinput.pack(side=RIGHT)
        server_portinput.insert(0,"10810")
        server_port.pack()
        
        bind_ip=Frame(root)
        iptext=Label(bind_ip,text="绑定到ip:",width=10,height=2)
        iptext.pack(side=LEFT)
        bind_ipinput=Entry(bind_ip)
        bind_ipinput.pack(side=RIGHT)
        bind_ipinput.insert(0,"0.0.0.0")
        bind_ip.pack()
        
        bind_port=Frame(root)
        iptext=Label(bind_port,text="绑定到port:",width=10,height=2)
        iptext.pack(side=LEFT)
        bind_portinput=Entry(bind_port)
        bind_portinput.pack(side=RIGHT)
        bind_portinput.insert(0,"10810")
        bind_port.pack()
        
        buttonbox=Frame(root)
        kill=Button(buttonbox,text="开始",command=self.forward)
        kill.pack()
        kill=Button(buttonbox,text="停止",command=self.stop)
        kill.pack()
        buttonbox.pack()
        
        self.bind_ipinput=bind_ipinput
        self.bind_portinput=bind_portinput
        
        self.server_ipinput=server_ipinput
        self.server_portinput=server_portinput
        root.mainloop()
    def forward(self):
        system(f"netsh interface portproxy add v4tov4 listenport={self.bind_portinput.get()} listenaddress={self.bind_ipinput.get()} connectport={self.server_portinput.get()} connectaddress={self.server_ipinput.get()}")
        self.bindport=self.bind_portinput.get()
        self.bindip=self.bind_ipinput.get()
        
        self.bind_port=self.bind_ipinput.get()
        self.bind_ip=self.bind_ipinput.get()
    def stop (self):
        system(f"netsh interface portproxy delete v4tov4 listenport={self.bind_portinput.get()} listenaddress={self.bind_ipinput.get()}")
    
    def __del__ (self):
        system(f"netsh interface portproxy delete v4tov4 listenport={self.bindport} listenaddress={self.bindip}")
        
if __name__ == '__main__':
    port_forward=Port_forward()