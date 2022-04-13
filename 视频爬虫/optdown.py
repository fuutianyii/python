import requests
import re
from tkinter import *
import urllib
from bs4 import BeautifulSoup
from threading import Thread
import os
import threading
import time
from soupsieve.css_parser import VALUE
import urllib3
from tkinter import ttk
from  contextlib import  closing
import optparse
optparse.OptionParser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
global downingvideo
downingvideo=False
# url_m3u8= 'https://wuji.zhulong-zuida.com/20190706/762_c260ca6c/800k/hls/index.m3u8'
# url_m3u8=r'http://iqiyi.cdn9-okzy.com/20200812/13885_2e9c6b7a/1000k/hls/index.m3u8'
# url_m3u8=r'https://hong.tianzhen-zuida.com/20200101/17572_c68f194f/index.m3u8'
# url_m3u8=r'https://feifei.feifeizuida.com/20181210/2692_604e1b69/index.m3u8'
global thlock
global start
global downum
downok=0
start=time.time()
thlock = threading.Lock()
passfile=[]
downum=0

def downf(url):
    gettext=""
    downum=0
    url_m3u8=url
    print(url_m3u8)
    rr=''
    try:    
        rr = requests.get(url_m3u8)
        gettext=rr.text
    except requests.exceptions.ReadTimeout:
        time.sleep(2)
    except requests.exceptions.ConnectionError:
        time.sleep(2)
    except requests.exceptions.ChunkedEncodingError:
        time.sleep(2)
    # r.encoding='utf-8'
    print(gettext)
    comurl=re.compile(r".*\n.*\n(.*)")
    
    m3u8=re.findall(comurl,str(gettext))
    thnum=len(threading.enumerate())
    if len(m3u8)<50:
        lastm3u8=url_m3u8.replace('index.m3u8',m3u8[0])
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        while True:    
            try:
                rr = requests.get(lastm3u8,headers=header,verify=False)
                break
            except requests.exceptions.ReadTimeout:
                time.sleep(2)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
            except requests.exceptions.ChunkedEncodingError:
                time.sleep(2)
        rr.encoding='utf-8'
        rr=rr.text
        comur=re.compile(r'\n(.*ts)')
        ts=re.findall(comur,rr)
        lenum=len(ts)
        with open('F:\\ts\\downfile.txt','w')as f:
            for i in range(0,lenum):
                rr=rr.replace(ts[i],'F:\\ts\\'+str(i)+'.ts')
                f.write('file '+str(i)+'.ts\n')
        f.close()
    else:
        lastm3u8=url_m3u8
        rr.encoding='utf-8'
        rr=rr.text
        comur=re.compile(r'\n(http.*)\n#EXTINF:')
        ts=re.findall(comur,rr)
        lenum=len(ts)
        with open('F:\\ts\\downfile.txt','w')as f:
            for i in range(0,lenum):
                rr=rr.replace(ts[i],'F:\\ts\\'+str(i)+'.ts')
                f.write('file '+str(i)+'.ts\n')
                f.flush()
    def down(ddownum):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        url=ts[ddownum]
        while True:
            try:
                res = requests.get(url,headers=header,timeout=(30,30))
                # res = requests.get(url,headers=header)
                with open('F:\\ts\\'+str(ddownum)+'.ts','wb') as f:
                    f.write(res.content)
                    print(res.text)
                    f.flush()
                break
            except requests.exceptions.ReadTimeout:
                time.sleep(2)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
            except requests.exceptions.ChunkedEncodingError:
                time.sleep(2)
        global progressbar
        global downok
        downok+=1

        

    while True:
        global passfile
        time.sleep(0.1)
        if len(threading.enumerate())<=50 and downum<lenum:
            thname=ts[downum]
            thname=threading.Thread(target=down,args=(downum,))
            thname.start()
            downum=downum+1
        elif downum==lenum and len(threading.enumerate())<=thnum:
            if len(threading.enumerate())<=thnum:
                os.system('ffmpeg -f concat -safe 0 -i F:/ts/downfile.txt -c copy F:/ts/'+title+'.mp4')
                b=time.time()
                downum=0
                break
            global downingvideo
            downingvideo=False
        else:
            pass
def remove():
    listdir=os.listdir('F:\\ts\\')
    for i in listdir:
        if i[-2]+i[-1]=='ts':
            os.remove('F:\\ts\\'+i)
        elif i[-3]+i[-2]+i[-1]=='txt':
            os.remove('F:\\ts\\'+i)



def tencentvideodown(tencenturl):
    global title
    reponse = urllib.request.urlopen(tencenturl)  
    html=reponse.read().decode()
    endurl="https://vip.lytwx.top/?url="+tencenturl
    print(endurl)
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    req = urllib.request.Request(url=endurl,headers=headers)
    print("finging")
    while True:
        try:
            reponse = urllib.request.urlopen(req)  
            break
        except:
            global downingvideo
            downingvideo=False
            pass
    html=reponse.read().decode()
    bhtml=str(BeautifulSoup(html,"html.parser"))
    print(bhtml)
    
    try:
        findmp4=re.compile(r"(https://.*?mp4)")
        mp4url=re.findall(findmp4,bhtml)[0]
        print(findmp4)
        try: 
            with closing(requests.get(mp4url,stream=True)) as  r:
                    #定义一个1024的字节
                    chunk_size=1024
                    content_size=int(r.headers['content-length'])
                    #开始把内容写入到path中，格式为wb,赋值给 f
                    with open(r"f://ts/"+title+".mp4","wb") as f:
                        n=1;
                        #边下载边存硬盘  chunk_size=chunk_size可修改 单位为B
                        for  chunl in r.iter_content(chunk_size=chunk_size):
                            # 每次下载+1
                            loaded=n*1024.0/content_size
                            #写入文件
                            f.write(chunl)
                            n+=1
                        f.close()
            downingvideo=False
            # mp4data=requests.get(mp4url).content
            # with open(r"f://ts/"+title+".mp4","wb") as videowriter:
                
            #     videowriter.write(mp4data)
            #     videowriter.flush()
        except:
            
            downingvideo=False
    except:
        # try:
        findm3u8=re.compile(r"(https://.*?m3u8)\"")
        print(bhtml)
        m3u8url=re.findall(findm3u8,bhtml)[0]
        print(m3u8url)
        print(m3u8url)
        downf(m3u8url)
        remove()
        # except:
        #     listboxprint("无法获取资源")
   

def starttencentvideodown():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url")
    parser.add_option("-n", "--name", dest="name")
    (options, args) = parser.parse_args()
    url=options.url
    global title
    title=options.name
    print(title)
    print(url)
    respect=re.compile(r"(https://.*?html)")
    if (len(re.findall(respect,url))) !=1:
        global downingvideo
        downingvideo=False
    else:
        ThreadStartDown=Thread(target=tencentvideodown,args=(url,))
        ThreadStartDown.start()


starttencentvideodown()