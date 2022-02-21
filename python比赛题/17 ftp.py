import ftplib
f = ftplib.FTP()  # 实例化FTP对象
f.connect('192.168.103.55') # 连接
f.login("ftpuser", "qwe")  # 登录
filelist=f.nlst()
for i in filelist:   #多下
  path=open(i,'wb')
  f.retrbinary('RETR '+i,path.write,1024) 
path.close()
path=open('2.txt','rb')
a='4.txt'
f.storbinary('STOR '+a,path,1024)   #上传
f.close()