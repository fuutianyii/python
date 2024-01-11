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

def update_sxcc():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）

    for i in range(1,27):
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuInfo/list"
        datas={"userId":"986e2223930e159dba69acc69851ba19",
        "page":i,
        "limit":1,
        "xxdm":"3632000472",
        "sznj":"2020",
        "sxcc":"1"}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "def5f4b44787360ca6372b5d030af4ec",
            "Token": "def5f4b44787360ca6372b5d030af4ec",
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
        if len(datas["data"]["list"])==0:
            print("无数据")
            continue
        try:
            print(datas["data"]["list"][0]["xm"])
        except TypeError:
            print(datas)
            exit()
        xjh=datas["data"]["list"][0]["xjh"]

        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuEmployment/list"
        datas={"userId":"986e2223930e159dba69acc69851ba19",
               "page":1,
               "limit":10,
               "xnd":"2022",
               "xxdm":"3632000472",
               "xjh":xjh}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "def5f4b44787360ca6372b5d030af4ec",
            "Token": "def5f4b44787360ca6372b5d030af4ec",
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
        xm=datas["data"]["list"][0]["xm"]
        id=datas["data"]["list"][0]["id"]
        xjh=datas["data"]["list"][0]["xjh"]
        zy=datas["data"]["list"][0]["zy"]
        id=datas["data"]["list"][0]["id"]
        id=datas["data"]["list"][0]["id"]
        id=datas["data"]["list"][0]["id"]
        time.sleep(1)
        if (datas["data"]["list"][0]["byqx"] == "升学-五年一贯制升学"):
            url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuEmployment/update"
            datas={"id":id,
                "xxdm":"3632000472",
                "xjh": xjh,
                "byqx":"25",
                "xsxxmc":"江苏联合职业技术学校",
                "zy":zy,
                "cc":"2",
                "sxgjdq":"156",
                "sxsf":"32"}
            datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
            header={"Host": "zzxx.jse.edu.cn",
                "Content-Length": "65",
                "Menu": "/head/Page/tour1/stuInfo",
                "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "Userid": "def5f4b44787360ca6372b5d030af4ec",
                "Token": "def5f4b44787360ca6372b5d030af4ec",
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
            print(xm+":"+datas)
            time.sleep(3)
        else:
            print("不是五年一贯制升学")
if __name__ == "__main__":
    update_sxcc()
    
    