import os
import requests
import re
import threading
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# url_m3u8= 'https://wuji.zhulong-zuida.com/20190706/762_c260ca6c/800k/hls/index.m3u8'
# url_m3u8=r'http://iqiyi.cdn9-okzy.com/20200812/13885_2e9c6b7a/1000k/hls/index.m3u8'
# url_m3u8=r'https://hong.tianzhen-zuida.com/20200101/17572_c68f194f/index.m3u8'
# url_m3u8=r'https://feifei.feifeizuida.com/20181210/2692_604e1b69/index.m3u8'
global thlock
global start
global downum
start=time.time()
thlock = threading.Lock()
passfile=[]
downum=0

def downf(url):
    global downum
    downum=0
    print("loaddown!")
    url_m3u8=url
    rr=''
    try:    
        rr = requests.get(url_m3u8)
    except requests.exceptions.ReadTimeout:
        time.sleep(2)
    except requests.exceptions.ConnectionError:
        time.sleep(2)
    except requests.exceptions.ChunkedEncodingError:
        time.sleep(2)
    # r.encoding='utf-8'
    comurl=re.compile(r".*\n.*\n(.*)")
    m3u8=re.findall(comurl,str(rr.text))
    print("downing")
    thnum=len(threading.enumerate())
    print(str(thnum)+" threadings start")
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
        print("writedown")
    else:
        lastm3u8=url_m3u8
        rr.encoding='utf-8'
        rr=rr.text
        comur=re.compile(r'\n(.*ts)')
        ts=re.findall(comur,rr)
        lenum=len(ts)
        with open('F:\\ts\\downfile.txt','w')as f:
            for i in range(0,lenum):
                rr=rr.replace(ts[i],'F:\\ts\\'+str(i)+'.ts')
                f.write('file '+str(i)+'.ts\n')
        # f.flush()
        print("writedown")



    def down(ddownum):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        url=lastm3u8.replace('index.m3u8',ts[ddownum])
        while True:
            try:
                res = requests.get(url,headers=header,timeout=(30,30))
                # res = requests.get(url,headers=header)
                with open('F:\\ts\\'+str(ddownum)+'.ts','wb') as f:
                    f.write(res.content)
                    f.flush()
                    print(url)
                break
            except requests.exceptions.ReadTimeout:
                time.sleep(2)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
            except requests.exceptions.ChunkedEncodingError:
                time.sleep(2)

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
                end=time.time()
                localtime=str(time.strftime("%m-%d-%H-%M",time.localtime()))
                a=time.time()
                os.system('ffmpeg -f concat -safe 0 -i F:/ts/downfile.txt -c copy F:/ts/'+localtime+'.mp4')
                b=time.time()
                print('下载完成!下载耗时:'+str((end-start)/60)+'分钟!')
                print('合并完成!合并耗时:'+str(b-a)+'秒!')
                downum=0
                break
        else:
            pass
def remove():
    listdir=os.listdir('F:\\ts\\')
    for i in listdir:
        if i[-2]+i[-1]=='ts':
            os.remove('F:\\ts\\'+i)
        elif i[-3]+i[-2]+i[-1]=='txt':
            os.remove('F:\\ts\\'+i)
