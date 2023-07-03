'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-28 17:28:13
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json
import pandas as pd
import time

def insert_stuCertificate():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'F:/Desktop/stuInfo.xlsx',header=0)
    stuInfo=data.values
    stuDict={}
    for i in stuInfo:
        stuDict[i[2]]=i
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/学生职业资格证书张琦(1).xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuCertificate/save"
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "aa19cc2fc11e136de5498da90a5478b2",
            "Token": "aa19cc2fc11e136de5498da90a5478b2",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Origin": "https://zzxx.jse.edu.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"}
        data={"xxdm":"3632000472",
            "xm":i[1],
            "xjh":stuDict[i[0]][0],
            "zsmc":i[2],
            "zsbh":str(i[3]),
            "pxzslx":"2",
            "zsbfdw":i[6],
            "zsbfrq":i[7].replace("-",""),
            "hddfhzymxzyzgzsdj":"4",
            "yzmcm":"",
            "sing":"ee41ac682d4711d8181033064380d858",
            "time":"1687935943000"}
        data=json.dumps(data,ensure_ascii=False).encode("utf-8")
        proxies={'http':'http://127.0.0.1:8080'}
        requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
        print(i[1]+" "+requests_data.text)
        data=json.loads(requests_data.text)
        time.sleep(3)


if __name__ == "__main__":
    insert_stuCertificate()
    
    
