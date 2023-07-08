'''
Author: fuutianyii
Date: 2023-07-06 15:49:55
LastEditors: fuutianyii
LastEditTime: 2023-07-06 16:33:45
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import json
import re

f=open("f:/desktop/1.html","rb")
data=f.read().decode()
pattern = re.compile(r'<[^>]+>',re.S)
data = pattern.sub('', data)
data=json.loads(data)
for i in data["data"]["questionList"]:
    print(i["stem"])
    if i["type"]==0:
        choice=["A","B","C","D"]
        c=0
        a=0
        for b in i["content"]["ol"]:
            print(choice[c]+"."+b["v"])
            if b["r"] == True:
                a=choice[c]
            c+=1
        print("答案："+a)
    elif i["type"]==2:
        for b in i["content"]["ol"]:
            print("答案："+b["v"])
    elif i["type"]==3:
        print("答案："+str(i["content"]["v"]))

    else:
        print(i["content"])
    print("解析："+i["answerAnalysis"])
    
    print()        
    