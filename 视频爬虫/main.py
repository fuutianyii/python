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
    listboxprint("loaddown!")
    url_m3u8=url
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
    comurl=re.compile(r".*\n.*\n(.*)")
    
    m3u8=re.findall(comurl,str(gettext))
    listboxprint("downing")
    thnum=len(threading.enumerate())
    listboxprint(str(thnum)+" threadings start")
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
        listboxprint("writedown")
    else:
        lastm3u8=url_m3u8
        rr.encoding='utf-8'
        rr=rr.text
        comur=re.compile(r'\n(http.*)\n#EXTINF:')
        ts=re.findall(comur,rr)
        lenum=len(ts)
        listboxprint(ts)
        with open('F:\\ts\\downfile.txt','w')as f:
            for i in range(0,lenum):
                rr=rr.replace(ts[i],'F:\\ts\\'+str(i)+'.ts')
                f.write('file '+str(i)+'.ts\n')
                f.flush()
        listboxprint("writedown")
    def down(ddownum):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        url=ts[ddownum]
        while True:
            try:
                res = requests.get(url,headers=header,timeout=(30,30))
                # res = requests.get(url,headers=header)
                with open('F:\\ts\\'+str(ddownum)+'.ts','wb') as f:
                    f.write(res.content)
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
        progressbar["value"]=(downok/lenum)*800
        listboxprint("下载陈功:"+str(downok)+"/"+str(lenum)+"----"+url)
        

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
                COMMAND='ffmpeg -f concat -safe 0 -i F:/ts/downfile.txt -c copy F:/ts/'+title+'.mp4'
                os.system(COMMAND)
                downum=0
                break
            downbutton.config(text='下载',command=starttencentvideodown)
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
    listboxprint("正在访问视频信息")
    reponse = urllib.request.urlopen(tencenturl)  
    html=reponse.read().decode()
    stringhtml=str(BeautifulSoup(html,"html.parser"))
    findtitle=re.compile(r"<title>(.*?)</title>")
    title=re.findall(findtitle,stringhtml)[0]
    title=title.replace("_1080P在线观看平台_腾讯视频","")
    listboxprint(str(title))
    endurl="http://jx.618g.com/?url="+tencenturl
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    req = urllib.request.Request(url=endurl,headers=headers)
    while True:
        try:
            listboxprint("正在解析地址")
            reponse = urllib.request.urlopen(req)  
            break
        except:
            listboxprint("解析失败")
            downbutton.config(text='下载',command=starttencentvideodown)
            global downingvideo
            downingvideo=False
            break
    listboxprint("解析成功")
    html=reponse.read().decode()
    bhtml=str(BeautifulSoup(html,"html.parser"))
    listboxprint("正在获取视频地址")
    listboxprint(endurl)
    
    try:
        findmp4=re.compile(r"(https://.*?mp4)")
        
        mp4url=re.findall(findmp4,bhtml)[0]
        listboxprint("获取mp4资源")
        listboxprint('开始下载视频')
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
                            progressbar["value"]=800*loaded
                            n+=1
                        f.close()
            listboxprint("生成视频---F://ts/"+title+".mp4")
            downbutton.config(text='下载',command=starttencentvideodown)    
            downingvideo=False
            # mp4data=requests.get(mp4url).content
            # with open(r"f://ts/"+title+".mp4","wb") as videowriter:
                
            #     videowriter.write(mp4data)
            #     videowriter.flush()
        except:
            listboxprint("获取失败")
            downbutton.config(text='下载',command=starttencentvideodown)
            
            downingvideo=False
    except:
        # try:
        print(bhtml)
        findm3u8=re.compile(r"(https://.*?m3u8)\"")
        m3u8url=re.findall(findm3u8,bhtml)[0]
        listboxprint("获取m3u8资源")
        listboxprint('开始下载视频')
        print(m3u8url)
        downf(m3u8url)
        remove()
        # except:
        #     listboxprint("无法获取资源")
   
def listboxprint(str):
    global completebox
    completebox.insert(0,str)
    completebox.pack()

def starttencentvideodown():
    url=inputentry.get()
    listboxprint("获得网址:"+url)
    respect=re.compile(r"(https://.*?html)")
    if (len(re.findall(respect,url))) !=1:
        listboxprint("请输入正确的网址！")
        downbutton.config(text='下载',command=starttencentvideodown)
        global downingvideo
        downingvideo=False
    else:
            ThreadStartDown=Thread(target=tencentvideodown,args=(url,))
            ThreadStartDown.start()

def start():
    global downingvideo
    if downingvideo == False:
        global downbutton
        downingvideo=True
        downbutton.config(text="下载中",command=None)
        ThreadStart=Thread(target=starttencentvideodown)
        ThreadStart.start()
    else:
        pass

    
tencenturl="https://v.qq.com/x/cover/m441e3rjq9kwpsc/g00365t07os.html"
# tencentvideodown(tencenturl)
def tk():
    global completebox
    global inputentry
    global downbutton
    global progressbar
    global root
    root = Tk()
    root.title("crawler 三代")
    fm=Frame(root)
    fm.pack(padx=25,pady=30)
    
    fmbuttom=Frame(root)
    inputentry=Entry(fmbuttom,borderwidth=1,width=80)
    inputentry.pack()
    downbutton = Button(fmbuttom,text='下载',command=start)
    downbutton.pack()
    fmbuttom.pack(padx=10,pady=10)


    ProgressbarFrame=Frame(root)   
    ProgressbarFrame.pack()
    progressbar = ttk.Progressbar(ProgressbarFrame, orient = "horizontal", length=570, mode="determinate", value=0.0,maximum=800)
    progressbar.pack()

    complete=Frame(root)
    completebox=Listbox(complete,selectmode=EXTENDED,width=80)
    completebox.pack()
    complete.pack(padx=25,pady=30)
    # lb.insert(END,"1")
    # lb.pack()
    # for item in dict:
    #     name="大魔王第"+str(item)+"章"
    #     lb.insert(END,name)
    # lb.pack()
    root.mainloop()
        


if __name__ == "__main__":
    tk()