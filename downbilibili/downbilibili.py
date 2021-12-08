import requests
import re
import os
def star(aid,cid,name):
    url2 = "https://api.bilibili.com/x/player/playurl?avid={avid}&cid={cid}&qn={qxd}&type=&otype=json"
    headers2 = {
        "host": "",
        "Referer": "https://www.bilibili.com",
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36"
    }
    avid=[]
    avid.append(id)
    # get_cid(avid[0])#已知aid获取cid
    # print("cid"+str(cid) + "name"+name)
    flv_url , size = get_flvurl(url2.format(avid=aid,cid=cid,qxd=32))
    global shuju
    shuju = size / 1024 / 1024
    print("本视频大小为：%.2fM" % shuju)
    h = re.findall("https://(.+)com",flv_url)
    host = h[0]+"com"
    headers2["host"] = host
    print("allok")
    res = requests.get(flv_url,headers=headers2,stream=True, verify=False)
    print("getok")
    save_movie(res,name)
def validateTitle(name):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_name = re.sub(rstr, "_",name)  # 替换为下划线
    return new_name
def get_cid(aid):#获得cid
    header = {
        'host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
             }
    url = "https://api.bilibili.com/x/player/pagelist?aid={aid}&jsonp=jsonp".format(aid=aid)
    response = requests.get(url,headers=header).json()
    # print(response)
    return response["data"][0]["cid"] ,response["data"][0]["part"]
def get_flvurl(url):#获得视频真实flv地址
    header = {'host': 'api.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    response = requests.get(url,headers=header).json()    
    # print(response)
    rule=re.compile(r"'new_description': '(.*?)'")#能下载的清晰度
    # print(str(response))
    datalist=re.findall(rule, str(response))#对应的数字清晰度id
    rule=re.compile(r"'quality': (.*?),")
    # print(str(response))
    best=re.findall(rule, str(response))
    # print(best)
    for i in range(0,len(best)):
        best[i]=int(best[i])
    bestint=0
    for i in best:
        bestint=max(bestint,i)
    # print(bestint)

    url=url.replace("qn=32", "qn="+str(bestint))
    
    header = {'host': 'api.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    response = requests.get(url,headers=header).json()    

    return response["data"]["durl"][0]["url"],response["data"]["durl"][0]["size"]


def save_movie(res,name):#保存视频
    global shuju
    shuju=shuju*1024*1024
    print('name:'+name)
    name=validateTitle(name)
    getdate=0
    videoname="{name}.flv".format(name = name)
    path="f://ts/"
    with open(path+ videoname,"wb") as f:
        for data in res.iter_content(1024):
            f.write(data)
            getdate=getdate+1024
            # print("\x1b[2K",end="")
            print("已下载："+str(getdate/shuju*100)[:4]+"%",end="\r")
        convervideo=input("下载视频为flv格式,输入y转换为mp4格式:")
        
        if convervideo == "y" or convervideo == "Y":     
            command="ffmpeg -i " +path+ videoname + "  " +path+ videoname.replace("flv","mp4")
            print(command)
            os.system(command)
            os.remove(path+videoname.replace("mp4","flv"))
        else:
            pass
        print("complete！")
def start(url):

    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    openurl=requests.get(url=url,headers=headers)
    openurl=openurl.text
    rematch=re.compile('part\":\"(.*?)\"')
    videoname=re.findall(rematch,openurl)
    rematch=re.compile('{\"cid\":(.*?),\"page')
    id=re.findall(rematch,openurl)
    videocid={}
    for  i in  range(0,len(id)):
        videocid[videoname[i]]=id[i]
    # print("识别到:",end="\n")
    num=1
    # print(videocid)
    for one in videocid:
        print(str(num)+one)
        num+=1
    # print(videocid[0])
    if len(videoname)!=1:
        downcid=int(input("输入下载的序号："))
        cid=videocid[videoname[downcid-1]]
        name=videoname[downcid-1]
    else:
        cid=videocid[videoname[0]]
        name=videoname[0]
    rematch=re.compile('"aid":(\d*?),')
    id=re.findall(rematch,openurl)
    # print(id)
    try:
        id.remove("0")
    except:
        pass
    for one in id:
        repeat=0
        for two in id:
            if one == two:
                repeat +=1
                if repeat == 2:
                    aid = one
    # print(type(aid))

    if type(id) == "<class 'list'>":
        print("not list")
        aid = id[0]
    print("aid"+aid)
    print("cid"+str(cid))

    name=name.replace(" ","")
    star(aid ,cid,name)
if __name__=="__main__":
    url=input("url:")
    start(url)