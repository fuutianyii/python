import ftplib
host='172.16.1.131'
username='ftpuser'
password='qwe'
f = ftplib.FTP(host)  # 实例化FTP对象
f.login(username, password)  # 登录

def ftp_download():
    '''以二进制形式下载文件'''
    ftpdirfile = '1.txt'
    localfile = '1.txt'
    fw = open(localfile, 'wb')
    f.retrbinary('RETR '+ftpdirfile,fw.write)
    fw.close()
    print("down 1.txt")
 
 
def ftp_upload():
    '''以二进制形式上传文件'''
    ftpdirfile = 'python-exe.txt'
    localfile = 'python-exe.txt'
    fr = open(localfile, 'rb')
    f.storbinary('STOR '+ftpdirfile,fr)
    fr.close()
    print("upload 2.txt")
 
ftp_download()
ftp_upload()
f.quit()
