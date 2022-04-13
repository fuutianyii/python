from bs4 import BeautifulSoup
from tkinter import *
import re
import time
import sys
import urllib.request
import threading
import m3u8down
import os
###建议使用m3u8地址
global localtime
localtime=str(time.strftime("%d-%H-%M-%S",time.localtime()))
def gete1():
    global e1
    global http
    global gethttp
    http=e1.get()
    comurl=re.compile(r'(http.*)')
    m3u8list=re.findall(comurl,http)
    if http=='':
        guii=Tk()
        Label(guii,text="请输入网址!!!").grid(row=0,columnspan=3,rowspan=3)   
        guii.mainloop()
    elif m3u8list==[]:
        guii=Tk()
        Label(guii,text="请输入正确的网址!!!").grid(row=0,columnspan=3,rowspan=3)   
        guii.mainloop()
    else:
        pass
    comurl=re.compile(r'(http://www.baishixi.com.*)')
    m3u8list=re.findall(comurl,http)
    if m3u8list != []:
        gethttp=re.findall(comurl,http)[0]
        baishi()
    elif http[-5:]=='.m3u8':
        m3u8pachong()
    elif http[-4:]=='.mp4':
        mp4down()
    else:
        gethttp=http
        pypachong()

def mp4down():
    print("downing")
    urllib.request.urlretrieve(http,'F:\\ts\\'+localtime+'.mp4')
    downed()



def findm3u8():
    url=gethttp
    # ##伪装游览器
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    req = urllib.request.Request(url=url,headers=headers)
    reponse = urllib.request.urlopen(req)  

    html=reponse.read().decode()
    bhtml=BeautifulSoup(html,"html.parser")
    comurl=re.compile(r"(http.*?index.m3u8)")
    #['https:\\/\\/qq.mgzy-cdn7.com\\/20200810\\/LruwCKWi\\/index.m3u8', 'https:\\/\\/qq.mgzy-cdn7.com\\/20200810\\/QrumihPx\\/index.m3u8']
    m3u8=re.findall(comurl,str(bhtml))
    if len(m3u8)!=0:
        m3u81=m3u8[0]
        m3u8_url=m3u81.replace("\\","")
        m3u8down.downf(m3u8_url)
        m3u8down.remove()
        sys.exit(0)
    else:
        pass

def downing():
    guii=Tk()
    Label(guii,text="开始下载!").grid(row=0,columnspan=3)   
    guii.mainloop()

def downed():
    guii=Tk()
    Label(guii,text="下载完成!!!").grid(row=0,columnspan=3)   
    guii.mainloop()


def mp4changchong():
    url=gethttp
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    try:
        req = urllib.request.Request(url=url,headers=headers)
    except ValueError:
        sys.exit(0)
    reponse = urllib.request.urlopen(req)
    html=reponse.read().decode()
    bhtml=BeautifulSoup(html,"html.parser")
    comurl=re.compile(r'(https.*?.mp4)"')
    mp4=re.findall(comurl,str(bhtml))
    if mp4!=[]:
        threadone=threading.Thread(target=downing)
        threadone.start()
        urllib.request.urlretrieve(mp4[0],'F:\\ts\\'+localtime+'.mp4')
        downed()
    else:
        guii=Tk()
        text1="未找到可下载的视频链接,或非vip视频,请尝试其他视频网站地址,或可尝试在线播放!"
        text2="地址1:http://v.yhgou.cc/2019/?url="+http
        text3="地址2:https://5.nmgbq.com/jx.php?url="+http
        text4="或可在'http://www.jisudhw.com/'搜寻资源"
        Label(guii,text=text1).grid(row=0,columnspan=3,sticky=W)   
        Label(guii,text=text2).grid(row=1,columnspan=3,sticky=W)   
        Label(guii,text=text3).grid(row=2,columnspan=3,sticky=W)   
        Label(guii,text=text4).grid(row=3,columnspan=3,sticky=W)   
        guii.mainloop()



def pypachong():
    findm3u8()
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    global urljx
    urljx="http://jx.618g.com/?url="+gethttp
    requesturl=urllib.request.Request(url=urljx,headers=header)
    urltexturl=urllib.request.urlopen(requesturl)
    urlsoup=BeautifulSoup(urltexturl,'html.parser')
    title=str(urlsoup.find_all("title")[0])
    title=title.replace("<title>","")
    title=title.replace("</title>","")
    m3u8url=urlsoup.find_all("div",class_="player")
    comurl=re.compile(r'url=(http.*?m3u8)"')
    try:
        m3u8=re.findall(comurl,str(m3u8url))[0]
    except IndexError:
        mp4changchong()
        sys.exit(0)
    except UnboundLocalError:
        mp4changchong()
    print(m3u8)
    def down():
        m3u8down.downf(m3u8)
        m3u8down.remove()
    threadtwo=threading.Thread(target=down)
    threadtwo.start()
    threadtwo.join()
    


def m3u8pachong():
    print(http)
    m3u8down.downf(http)
    m3u8down.remove()
    downed()

def baishi():
    url=gethttp
    # ##伪装游览器
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    req = urllib.request.Request(url=url,headers=headers)
    reponse = urllib.request.urlopen(req)
    html=reponse.read().decode()
    bhtml=BeautifulSoup(html,"html.parser")
    comurl=re.compile(r"(http.*?m3u8)")
    m3u8=re.findall(comurl,str(bhtml))
    js=len(m3u8)
    for i in m3u8:
        print(i.replace("\\",""))
    jishu=int(http[-7]+http[-6])
    m3u8=m3u8[jishu-1].replace("\\","")
    m3u8down.downf(m3u8)
    m3u8down.remove()
    downed()



def do():
    mainer=threading.Thread(target=gete1)
    mainer.start()

if  __name__ == "__main__":
    def main():
        gui=Tk()
        gui.title("视频下载器")
        gui.geometry("280x120")
        Label(gui,text="视频下载").grid(row=0,columnspan=3)   
        Label(gui,text="网址:").grid(row=2,sticky=W)   
        Label(gui,text="   输入视频网址,\n   点击开始按钮\n   开始下载视频").grid(row=2,column=2,sticky=W,rowspan=2)   
        global e1
        e1=Entry(borderwidth=1)
        e1.grid(row=2,column=1,sticky=E)    
        Button(text="开始",bg="white",command=do,width=8,height=1).grid(row=4,column=1)
        gui.mainloop()
    main=threading.Thread(target=main)
    main.start()


# python3 使用 tkinter
#from tkinter import *

#https://v.qq.com/x/cover/mzc00200amqycok.html
#https://www.iqiyi.com/v_19rzihz2y0.html?vfrm=pcw_home&vfrmblk=O&vfrmrst=711219_home_dianshiju_float_video_area3
#https://hong.tianzhen-zuida.com/20200101/17572_c68f194f/index.m3u8
#https://iqiyi.cdn9-okzy.com/20200119/5141_998948cd/index.m3u8
#https://youku.cdn3-okzy.com/20200819/12165_8ce58d0f/1000k/hls/index.m3u8


