import m3u8
import requests
from Crypto.Cipher import AES
import base64
import re
import threading
import time
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class GetVideoV2:
    def __init__(self):
        self.path="f://ts/"
        self.filenamelist=[]
        self.fileurllist=[]
        self.realm3u8=""
        self.realpath=""
        self.iv=""
        self.key=""
        print("start")

    def aesdecode(self):
        ##EXT-X-KEY:METHOD=AES-128,URI="https://ts8.hhmm0.com:9999/20210602/b4ZTBuKk/1000kb/hls/key.key",IV=0000000000000000
        pass
    def getrealm3u8(self,url):
        while True:
            try:
                tslist = m3u8.load(url)
                break
            except:
                print("29:load m3u8 error")
        if len(tslist.segments) == 0:
            data=requests.get(url).text
            # print(data)
            datalist=data.split("\n")
            m3u8path=None
            for m3u8data in datalist:
                if int(m3u8data.find(".m3u8"))!=-1:
                    m3u8path=m3u8data
                    rule=re.compile("(http.*.m3u8)")
                    realpath=re.findall(rule,m3u8path)
                    if  len(realpath) !=0:
                        self.realpath=realpath[0]
                        return realpath[0]
                    # else:

            rule=re.compile("(http.*?com/)")###############改规则
            domain=re.findall(rule,url)[0]
            realpath=domain+m3u8path
            print(realpath)
            self.realpath=realpath
            return realpath
        else:
            self.realpath=url
            
            return url
    def maketslist(self,url):
        tslist = m3u8.load(url)
        tslist=tslist.segments
        self.fileurllist=tslist.uri
        for ts in tslist:
            ts=ts.uri
            finalfind=ts.rfind("/")+1
            self.filenamelist.append(ts[finalfind::])
    def writefile(self):
        with open(self.path+"filenamelist.txt","w") as f:
            for name in self.filenamelist:
                if name[-3::]!=".ts":
                    name+=".ts"
                f.write("file "+name+"\n")
    def findkey(self):
        self.realm3u8=requests.get(self.realpath).text
        rule=re.compile("(http.*?\.key)")
        self.key=re.findall(rule, self.realm3u8)[0]
        self.key=requests.get(self.key).content
        return self.key
        
    def writem3u8(self):
        f=open(self.path+"get.m3u8","w")
        # print(self.realpath)
        self.realm3u8=requests.get(self.realpath).text
        f.write(self.realm3u8)
        f.close()

    def getfile(self,url):
        requests.get(url).content

    def getiv(self):
        f=open(self.path+"get.m3u8","r")
        ivlist=f.readlines()
        f.close()
        # print(ivlist)
        for iv in ivlist:
            ivplace=iv.find("iv=")
            import time
            # time.sleep(2)
            # print(iv)
            if (ivplace !=-1):
                self.iv=iv[ivplace::]
                break
            else:
                pass
        self.iv=self.iv[self.iv.find("=")+1::]
        # print("-"+self.iv+"-")
        if self.iv.replace(" ","")=="":
            self.iv="0000000000000000".encode()
        return self.iv

    def decodefile(self,data,key,iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        while len(data) % 16 !=0:
            data+=b" "
        content = cipher.decrypt(data)
        return content

    def downallts(self,tsurl,tsname):
        while True:    
            try:
                header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                data=requests.get(tsurl,headers=header,verify=False).content
                break
            except requests.exceptions.ReadTimeout:
                print("ReadTimeout")
                time.sleep(5)
            except requests.exceptions.ConnectionError:
                print("ConnectionError")
                time.sleep(5)
            except requests.exceptions.ChunkedEncodingError:
                print("ChunkedEncodingError")
                time.sleep(5)
                
        if tsname[-3::]!=".ts":
            tsname+=".ts"
        f=open(self.path+tsname,'wb')
        if self.key!="":
            f.write(self.decodefile(data, self.key, b'0000000000000000'))
        else:
            f.write(data)
        print(tsurl)


    def threaddown(self):
            thnum=len(threading.enumerate())
            downum=0
            lenum=len(self.filenamelist)
            while True:
                if len(threading.enumerate())<=20and downum<lenum:
                    tsurl=self.fileurllist[downum]
                    tsname=self.filenamelist[downum]
                    thname=tsname
                    thname=threading.Thread(target=self.downallts,args=(tsurl,tsname))
                    time.sleep(0.2)
                    thname.start()
                    downum=downum+1
                elif downum==lenum and len(threading.enumerate())<=thnum:
                    if len(threading.enumerate())<=thnum:
                        print("down end")
                        end=time.time()
                        localtime=str(time.strftime("%m-%d-%H-%M",time.localtime()))
                        a=time.time()
                        try:    
                            os.system('ffmpeg -f concat -safe 0 -i F:/ts/filenamelist.txt -c copy F:/ts/'+localtime+'.mp4')
                        except:
                            pass
                        b=time.time()
                        downum=0
                        break
                else:
                    pass
                    # print("theading not ending")

    def remove(self):
        listdir=os.listdir('F:\\ts\\')
        try:
            for i in listdir:
                if i[-3]+i[-2]+i[-1]=='.ts':
                    os.remove('F:\\ts\\'+i)
                elif i[-4]+i[-3]+i[-2]+i[-1]=='.txt':
                    os.remove('F:\\ts\\'+i)
                elif i[-5]+i[-4]+i[-3]+i[-2]+i[-1]=='.m3u8':
                    os.remove('F:\\ts\\'+i)
        except:
            pass
                

def video(url):
    getvideo=GetVideoV2()
    realpath=getvideo.getrealm3u8(url)#get m3u8 list
    getvideo.maketslist(realpath)#make list
    getvideo.writefile()#write local ffmpeg m3u8
    # key=getvideo.findkey()#get base64 key
    getvideo.writem3u8()
    # getvideo.getiv()
    getvideo.threaddown()
    getvideo.remove()

def encodevideo(url):
    getvideo=GetVideoV2()
    realpath=getvideo.getrealm3u8(url)#get m3u8 list
    getvideo.maketslist(realpath)#make list
    getvideo.writefile()#write local ffmpeg m3u8
    key=getvideo.findkey()#get base64 key
    getvideo.writem3u8()
    getvideo.getiv()
    getvideo.threaddown()
    getvideo.remove()