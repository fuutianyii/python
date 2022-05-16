import requests
import re
from tkinter import *
from tkinter import scrolledtext
import threading
from threading import Thread
import time

html=requests.get(r"https://mp.weixin.qq.com/s/ngvZPotwAKNSly_B0S-X6A")
html=html.text
comurl=re.compile(r'(http://mp.weixin.qq.com/.*?21.wechat_redirect)"')
downht=re.findall(comurl,html)
downht=downht[::-1]
infodic={}
def write_info(url):
    html=requests.get(url)
    html=html.text
    comurl=re.compile('voice_encode_fileid=\"(.*?)\"')
    downurl=re.findall(comurl,html)
    # print(downurl)
    comurl=re.compile('\" name=\"(.*?)\" play_length')
    name=re.findall(comurl,html)
    for i in range(0,len(downurl)):
        infodic[name[i].replace("&nbsp;","").replace("(","").replace(")","").replace("（","").replace("）","").replace(" ","").replace("修仙","").replace("章","").replace("第","")]=downurl[i]
    
for i in downht:
    write_info(i)

def get(url,name,id):
    while True:
        try:
            content=requests.get("https://res.wx.qq.com/voice/getvoice?mediaid="+url)
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
    # tnum=threading.enumerate()
    downlist=lb.curselection()
    for i in downlist:
        name=lb.get(i)
        url=infodic[name]
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
    # title=sorted(infodic.keys(), reverse=False)#排序
    for item in infodic.keys():
        name=item
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
tk()