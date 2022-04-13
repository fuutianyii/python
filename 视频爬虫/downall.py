import os
f=open("m3u8.txt","r")
m3u8line=f.readlines()
num=18
for i in m3u8line:
    m3u8=i.replace("\n","")
    os.system("python f:/python/视频爬虫/optdown.py -u "+m3u8+" -n "+str(num)+".mp4")
    num+=1