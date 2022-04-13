import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.16.1.131', port=22, username='root', password='qweqwe')
channel = ssh.invoke_shell()  #变成交互性终端

while 1:
    command = input(">>")
    channel.send(command + "\n")  #加\n代表回车执行
    time.sleep(0.2)
    buf = channel.recv(10024).decode("utf-8")
    print(buf)
	
