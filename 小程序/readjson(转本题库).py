'''
Author: fuutianyii
Date: 2023-07-06 15:49:55
LastEditors: fuutianyii
LastEditTime: 2023-07-12 20:23:35
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import json
import re

f=open("f:/desktop/1.html","rb")
data=f.read().decode()
f.close()
pattern = re.compile(r'<[^>]+>',re.S)
data = pattern.sub('', data)
data=json.loads(data)
f=open("f:/desktop/1.txt","w",encoding="utf-8")

for i in data["data"]["questionList"]:
    if i["type"]==0:
        f.write(i["stem"]+"\n")
        choice=["A","B","C","D"]
        c=0
        a=0
        for b in i["content"]["ol"]:
            f.write(choice[c]+"."+b["v"]+"\n")
            if b["r"] == True:
                a=choice[c]
            c+=1
        f.write("答案："+a+"\n")
    elif i["type"]==1:
        f.write(i["stem"]+"\n")
        choice=["A","B","C","D"]
        c=0
        a=""
        for b in i["content"]["ol"]:
            f.write(choice[c]+"."+b["v"]+"\n")
            if b["r"] == True:
                a+=choice[c]
            c+=1
        f.write("答案："+a+"\n")
    elif i["type"]==2:
        for b in i["content"]["ol"]:
            f.write("答案："+b["v"]+"\n")
    elif i["type"]==3:
        f.write("答案："+str(i["content"]["v"])+"\n")
    else:
        print(i["stem"])
        print(i["content"])
    f.write("解析："+i["answerAnalysis"]+"\n")
    
    f.write("\n")
    