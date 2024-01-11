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

def export_monQljyJg():
    f=open("export_monQljyJg_data.txt","w")
    for i in range(1,3):
        print(i)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/monQljyJg/queryData"
        datas={"limit":500,
               "page":i,
               "jgid":"20223632000472JXGL_JXZLCJ80",
               "xnd":"2022",
               "xxdm":"3632000472",}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "912f012d50c2637b21dac53f453200b0",
            "Token": "912f012d50c2637b21dac53f453200b0",
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
        f.write("班级名称\t")
        f.write("课程号\t")
        f.write("学年\t")
        f.write("学期\t")
        f.write("年级\t")
        f.write("课程名称\t")
        f.write("专业名称\t")
        f.write("表中序号\n")
        for i in datas["data"]["list"]:
            f.write(i["BJMC"]+"\t")
            f.write(i["KCH"]+"\t")
            f.write(i["XN"]+"\t")
            f.write(i["XQ"]+"\t")
            f.write(i["NJ"]+"\t")
            f.write(i["KCMC"]+"\t")
            f.write(i["ZYMC"]+"\t")
            f.write(str(i["ROW_ID"])+"\n")
        time.sleep(3)
if __name__ == "__main__":
    export_monQljyJg()
    
    