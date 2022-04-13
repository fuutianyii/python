import ftplib
f=ftplib.FTP()
f.connect('192.168.99.')
f.login('ftpuser','qwe')
#filelist=f.nlst()
#filesize=f.size(filelist[0])
#print(filesize)
filename=''
#for i in filelist:
    #if int(filesize) <= int(f.size(i)):
        #filename=i
with open(filename,'rb')as ff:
    f.storbinary('STOR '+filename,ff,1024)
f.close()
