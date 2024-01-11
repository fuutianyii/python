'''
Author: fuutianyii
Date: 2023-07-06 15:49:55
LastEditors: fuutianyii
LastEditTime: 2024-01-11 20:04:49
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import json
import re
import os

def getFileWithFileType(path,suffix):
    input_template_All=[]
    input_template_All_Path=[]
    for root, dirs, files in os.walk(path, topdown=False):
         for name in files:
             #print(os.path.join(root, name))
             print(name)
             if os.path.splitext(name)[1] == suffix:
                 input_template_All.append(name)
                 input_template_All_Path.append(os.path.join(root, name))
    return input_template_All,input_template_All_Path

def html_to_txt(filename):
    print(filename+" START!")
    f=open(filename,"rb")
    data=f.read().decode()
    f.close()
    pattern = re.compile(r'<\/?[a-zA-Z -=\\\."\'_仿宋]+?>',re.S)
    data=data.replace('src=\\\"','src=\">')
    data=data.replace('\\" width=','<\\" width=')
    data=data.replace("<br>","\\n")
    data = pattern.sub('', data)
    data=json.loads(data)
    f=open(filename.replace(".html",".txt"),"w",encoding="utf-8")
    id=1
    last_type=""
    for i in data["data"]["questionList"]:
        i["stem"]=i["stem"].replace("http","\nhttp").replace("&nbsp;"," ").replace("&quot;","'").replace("&lt;","'").replace("&gt","'")
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
                regex = re.compile(r"_{2}_+")
                data = regex.sub('<FILL.TAG>'+str(b["v"]).replace("\\","\\\\")+'</FILL.TAG>', data,1)
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
    print(filename+" OK!")
        
        
if __name__ == '__main__':
    fileList=getFileWithFileType("F:/Desktop/C/",".html")[1]
    for i in fileList:
        html_to_txt(i)
    