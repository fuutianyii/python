'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-29 10:37:05
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json
import pandas as pd
import time

def export_caseSchoolTrainResource():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/25学生奖励.xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/caseSchoolXxjl/list"
        datas={"userId":"986e2223930e159dba69acc69851ba19","page":1,"limit":10,"xxmc":"3632000472","xxdm":"null","xjh":i[0],"size":1,"sing":"92ba7d5cbbba06068d3c911dbceff88e","time":"1688005071000"}
        datas=json.dumps(datas)
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "ff3eb7224a5864774400ccc3c2e1176f",
            "Token": "ff3eb7224a5864774400ccc3c2e1176f",
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
        print(i[1])
        datas=json.loads(requests_data.text)
        f=open("小程序/全国中等职业学校管理信息系统/data.txt","w")
        f.write("姓名\t")
        f.write("获奖名称\t")
        f.write("获奖级别\t")
        f.write("获奖类别\t")
        f.write("\n")
        
        for i in datas["data"]["list"]:
            f.write(str(i["xm"])+"\t")
            f.write(str(i["hjxmmc"])+"\t")
            f.write(str(i["hjjb"])+"\t")
            f.write(str(i["hjxmlb"])+"\t")
            f.write("\n")
            
            
            # url="http://zzxx.jse.edu.cn/msc-api/api/tour/caseSchoolXxjl/delete"
            # datas=[]
            # print(i['id'])
            # datas.append(i['id'])
            
            # datas=json.dumps(datas)
            # header={"Host": "zzxx.jse.edu.cn",
            #     "Content-Length": "65",
            #     "Menu": "/head/Page/tour1/stuInfo",
            #     "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            #     "Sec-Ch-Ua-Mobile": "?0",
            #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            #     "Content-Type": "application/json;charset=UTF-8",
            #     "Accept": "application/json, text/plain, */*",
            #     "Userid": "ff3eb7224a5864774400ccc3c2e1176f",
            #     "Token": "ff3eb7224a5864774400ccc3c2e1176f",
            #     "Sec-Ch-Ua-Platform": '"Windows"',
            #     "Origin": "https://zzxx.jse.edu.cn",
            #     "Sec-Fetch-Site": "same-origin",
            #     "Sec-Fetch-Mode": "cors",
            #     "Sec-Fetch-Dest": "empty",
            #     "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
            #     "Accept-Encoding": "gzip, deflate",
            #     "Accept-Language": "zh-CN,zh;q=0.9",
            #     "Connection": "close"}
            # proxies={'http':'http://127.0.0.1:8080'}
            # requests_data=requests.post(url,proxies=proxies,data=datas,headers=header)
            # print(requests_data.text)
        f.close()

        

        time.sleep(3)
if __name__ == "__main__":
    export_caseSchoolTrainResource()
    
    
