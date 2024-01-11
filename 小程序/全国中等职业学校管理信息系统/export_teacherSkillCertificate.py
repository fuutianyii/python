'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-29 11:40:20
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
from codecs import ascii_encode
import requests
import json
import pandas as pd
import time

def export_teacherSkillCertificate():
    f=open("export_teacherSkillCertificate_data.txt","w")
    f.write("姓名\t")
    f.write("工号\t")
    f.write("证书名称\t")
    f.write("证书编号\t")
    f.write("证书类型\t")
    f.write("证书等级\t")
    f.write("证书颁发单位\t")
    f.write("证书颁发级别\t")
    f.write("证书颁发日期\n")
    for i in range(1,2):
        print(i)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/teacherInfo/list"
        datas={"userId":"986e2223930e159dba69acc69851ba19","page":i,"limit":500}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "21ffad701e2cb37413de314fce392e09",
            "Token": "21ffad701e2cb37413de314fce392e09",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Origin": "https://zzxx.jse.edu.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"}
        proxies={'http':'http://127.0.0.1:8080'}
        requests_data=requests.post(url,proxies=proxies,data=datas,headers=header)
        datas=requests_data.text
        datas=json.loads(datas)
        for i in datas["data"]["list"]:
            # f.write(str(i["jgh"])+"\t")
            # f.write(str(i["xm"])+"\t")
            jgh=i["jgh"]
            url="http://zzxx.jse.edu.cn/msc-api/api/tour/teacherSkillCertificate/list"



            datas={"userId":"986e2223930e159dba69acc69851ba19","page":1,"limit":10,"xxdm":"3632000472","jgh":jgh}
            datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
            
            header={"Host": "zzxx.jse.edu.cn",
                "Content-Length": "65",
                "Menu": "/head/Page/tour1/stuInfo",
                "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "Userid": "21ffad701e2cb37413de314fce392e09",
                "Token": "21ffad701e2cb37413de314fce392e09",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Origin": "https://zzxx.jse.edu.cn",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "close"}
            proxies={'http':'http://127.0.0.1:8080'}
            requests_data=requests.post(url,proxies=proxies,data=datas,headers=header)
            datas=requests_data.text
            datas=json.loads(datas)
            for i in datas["data"]["list"]:
                print(i['xm'])
                f.write(str(i["xm"])+"\t")
                f.write(str(i["jgh"])+"\t")
                f.write(str(i["zsmc"])+"\t")
                f.write(str(i["zsbh"])+"\t")
                f.write(str(i["zslxm"])+"\t")
                f.write(str(i["zsdj"])+"\t")
                f.write(str(i["zsbfdw"])+"\t")
                f.write(str(i["bfdwjb"])+"\t")
                f.write(str(i["zsbfrq"])+"\n")
                f.flush()
                time.sleep(3)
if __name__ == "__main__":
    export_teacherSkillCertificate()
    
    