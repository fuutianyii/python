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

def insert_StuReward():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/25学生奖励（创新创业22年）.xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuInfo/list"
        datas={"userId":"986e2223930e159dba69acc69851ba19",
               "page":1,
               "limit":1,
               "xxdm":"3632000472",
               "xjh":i[0]
        }
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "7da69c1e9d9dead413cffe8c94c2184e",
            "Token": "7da69c1e9d9dead413cffe8c94c2184e",
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
        datas=json.loads(requests_data.text)
        hjdj={"特等":1,"一等":2,"二等":3,"三等":4}
        hjjb={"省部级":3,"地市级":4}
        if len(datas["data"]["list"])!=0:
            url="http://zzxx.jse.edu.cn/msc-api/api/tour/caseSchoolXxjl/save"
            datas={"xm":i[1],
                   "xjh":i[0],
                   "hjxs":"",
                   "zdls":i[8],
                   "xxmc":"3632000472",
                   "xxdm":"3632000472",
                   "hjxmlb":"8",
                   "hjxmmc":i[3],
                   "hjjb":hjjb[i[4]],
                   "hjdj":hjdj[i[5]],
                   "bfdw":i[6],
                   "hjrq":i[7]}
            datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
            header={"Host": "zzxx.jse.edu.cn",
                "Content-Length": "65",
                "Menu": "/head/Page/tour1/stuInfo",
                "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "Userid": "7da69c1e9d9dead413cffe8c94c2184e",
                "Token": "7da69c1e9d9dead413cffe8c94c2184e",
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
            print(i[0]+datas.decode())
        else:
            print(i[0]+":查无此人")
        time.sleep(3)
if __name__ == "__main__":
    insert_StuReward()
    
    