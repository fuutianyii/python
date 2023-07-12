'''
Author: fuutianyii
Date: 2023-07-06 15:49:55
LastEditors: fuutianyii
LastEditTime: 2023-07-12 22:38:16
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import json
import re

f=open("F:/专转本/计算机基础/第一章/数字技术基础.html","rb")
data=f.read().decode()
f.close()
pattern = re.compile(r'<[^>]+>',re.S)
data = pattern.sub('', data)
data=json.loads(data)
f=open("F:/专转本/计算机基础/第一章/数字技术基础.txt","w",encoding="utf-8")

id=1
last_type=""
for i in data["data"]["questionList"]:
    if i["type"]==0:
        if last_type!=0:
            f.write("\n\n单选题\n\n")
            id=1
        f.write(str(id)+"."+i["stem"]+"\n")
        choice=["A","B","C","D"]
        c=0
        a=0
        for b in i["content"]["ol"]:
            f.write(choice[c]+"."+b["v"]+"\n")
            if b["r"] == True:
                a=choice[c]
            c+=1
        f.write("参考答案:"+a+"\n")
        last_type=0
    elif i["type"]==1:
        if last_type!=1:
            f.write("\n\n多选题\n\n")
            id=1
        f.write(str(id)+"."+i["stem"]+"\n")
        choice=["A","B","C","D"]
        c=0
        a=""
        for b in i["content"]["ol"]:
            f.write(choice[c]+"."+b["v"]+"\n")
            if b["r"] == True:
                a+=choice[c]
            c+=1
        f.write("参考答案:"+a+"\n")
        last_type=1
        
    elif i["type"]==2:
        if last_type!=2:
            f.write("\n\n填空题\n\n")
            id=1
        answer=""
        data = str(i["stem"])
        for b in i["content"]["ol"]:
            regex = re.compile(r"_+")
            data = regex.sub('<FILL.TAG>'+str(b["v"])+'</FILL.TAG>', data,1)
            answer+=b["v"]+";"
        f.write(str(id)+"."+data+"\n")
        f.write("参考答案:"+answer+"\n")
        last_type=2
    elif i["type"]==3:
        if last_type!=3:
            f.write("\n\n判断题\n\n")
            id=1
        f.write(str(id)+"."+i["stem"]+"\n")
        f.write("参考答案:"+str(i["content"]["v"]).replace("True","对").replace("False","错")+"\n")
        last_type=3
    else:
        print(str(id)+"."+i["stem"])
        print(i["content"])
        
    while ((i["answerAnalysis"].find("\r\n\r\n") !=-1) or (i["answerAnalysis"].find("\n\n") !=-1)):
        i["answerAnalysis"]=i["answerAnalysis"].replace("\r\n\r\n","\r\n").replace("\n\n","\n")
    f.write("解析："+i["answerAnalysis"]+"\n")    
    f.write("\n")
    id+=1
    