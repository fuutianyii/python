import threading
from threading import Thread
from tkinter import *
from tkinter import scrolledtext
from typing import Sized
import requests
import re
import time

dict={}
def openurl():
    global dict
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    openurl=requests.get(url=r"https://mp.weixin.qq.com/s/l-LP-GerIdN0Ec8uaY9vQQ",headers=headers)
    urltext=openurl.text
    reurl=re.compile(r'<a target="_blank" href="(http://.*?)"')
    redurl=re.findall(reurl,str(urltext))
    for url in redurl:
        openurl=requests.get(url=url,headers=headers)
        openurl=openurl.text
        reurl=re.compile('<meta property="og:title" content="(.*?)" />\n  <meta property="og:url" ')
        redurl=re.findall(reurl,openurl)
        rename=re.compile("第(.*?)章")
        revideoname=re.compile('voice_encode_fileid="(.*?)"')
        redvideoname=re.findall(revideoname,openurl)
        try:
            newname=re.findall(rename,redurl[0])[0].replace(" ",'')
        except:
            newname="1"
        rangesign=newname.find("-")
        if (rangesign != -1):
            videoname=newname
            rangestart=int(newname[:rangesign])
            rangeend=int(newname[rangesign+1:])
            for newname in range(rangestart,rangeend+1):
                # print(redurl[0])
                dict[newname]=redvideoname
        else:    
            newname=int(newname)
            dict[newname]=redvideoname
    newdict={}
    for i in range(1,len(dict)+1):
        newdict[i]="https://res.wx.qq.com/voice/getvoice?mediaid="+dict[i][0]
    dict=newdict
    

def get(url,name,id):
    while True:
        try:
            content=requests.get(url)
            with open("F:/ts/mp3/"+name+".mp3","wb") as w:
                b.config(text="下载中！",command=None)
                w.write(content.content)
                break
        except:
            time.sleep(2)
    completebox.insert(END,name+" complete!")
    lb.itemconfig(id,background='green')
    b.config(text="下载选中内容",command=down)
    
      #https://blog.csdn.net/weixin_42272768/article/details/100796024

def down():
    global b
    tnum=threading.enumerate()
    downlist=lb.curselection()
    for i in downlist:
        url=dict[i+1]
        name="大魔王第"+str(i+1)+"章"
        b.config(text="下载中！",command=None)
        i=Thread(target=get,args=(url,name,i))
        i.start()
    
    

def tk():
    global completebox
    global lb
    global b
    root = Tk()
    root.title("Pack布局")
    fm=Frame(root)
    fmbuttom=Frame(root)
    complete=Frame(root)
    lb=Listbox(fm,selectmode=EXTENDED,width=80)
    for item in dict:
        name="大魔王第"+str(item)+"章"
        lb.insert(END,name)
    lb.pack()
    b = Button(fmbuttom,text='下载选中内容',command=down)
    b.pack()
    completebox=Listbox(complete,selectmode=EXTENDED,width=80)
    completebox.pack()
    fm.pack(padx=25,pady=30)
    fmbuttom.pack(padx=10,pady=10)
    complete.pack(side=RIGHT,padx=25,pady=30)
    root.mainloop()
    

    

if __name__ == "__main__":
    openurl()
    tk()