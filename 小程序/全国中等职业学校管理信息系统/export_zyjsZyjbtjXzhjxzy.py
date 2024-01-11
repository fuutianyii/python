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

def export_zyjsZyjbtjXzhjxzy():
    f=open("export_zyjsZyjbtjXzhjxzy_data.txt","w")
    for i in range(1,2):
        print(i)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/zyjsZyjbtjXzhjxzy/list"
        datas={"limit":50,"page":1,"xxdm":"3632000472","userId":"986e2223930e159dba69acc69851ba19",}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "b3a417c5d053c6431e7b4616f27e9899",
            "Token": "b3a417c5d053c6431e7b4616f27e9899",
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
        f.write("学年\t")
        f.write("专业名称\t")
        f.write("专业教学资源库数\t")
        f.write("专业教学资源库总容量\t")
        f.write("专业教学库购买金额\t")
        f.write("仿真实习实训软件数\t")
        f.write("上网课程数\t")
        f.write("电子图书资源数\t")
        f.write("专业纸质图书数\t")
        f.write("音视频教学资源时长\t")
        f.write("数字化教学资源总数投入\t")
        f.write("当年新增数字教学资源投入\n")
        for i in datas["data"]["list"]:
            f.write(str(i["xn"])+"\t")
            f.write(str(i["zymc"])+"\t")
            f.write(str(i["zyjxzyksl"])+"\t")
            f.write(str(i["zyjxzykzrl"])+"\t")
            f.write(str(i["zyjxzykgmje"])+"\t")
            f.write(str(i["fzsxsxrjsl"])+"\t")
            f.write(str(i["swkcs"])+"\t")
            f.write(str(i["dztszyz"])+"\t")

            f.write(str(i["zyzztss"])+"\t")

            f.write(str(i["yspjxzysc"])+"\t")
            f.write(str(i["szhjxzyztr"])+"\t")
            f.write(str(i["dnxzszjxzytr"])+"\n")
        time.sleep(3)
if __name__ == "__main__":
    export_zyjsZyjbtjXzhjxzy()
    
    