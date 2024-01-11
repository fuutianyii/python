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

def export_zyjsZyjbtjXnsxjd():
    f=open("export_zyjsZyjbtjXnsxjd_data.txt","w")
    for i in range(1,2):
        print(i)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/zyjsZyjbtjXnsxjd/list"
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
            "Userid": "112de507daf188510dff402087256c8f",
            "Token": "112de507daf188510dff402087256c8f",
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
        f.write("本校专业编号\t")
        f.write("实训基地号\t")
        f.write("实训基地名称\t")
        f.write("实训基地批准级别\t")
        f.write("实训室数\t")
        f.write("建筑面积\t")
        f.write("教学、实习仪器设备总值\t")
        f.write("当年新增仪器设备值\t")
        f.write("仪器设备总数\t")
        f.write("大型仪器设备数\t")
        f.write("实践教学工位数\n")
        for i in datas["data"]["list"]:
            f.write(str(i["xn"])+"\t")
            f.write(str(i["zymc"])+"\t")
            f.write(str(i["bxzybh"])+"\t")
            f.write(str(i["sxjdh"])+"\t")
            f.write(str(i["sxjdmc"])+"\t")
            f.write(str(i["zcbm"])+"\t")
            f.write(str(i["sxss"])+"\t")
            f.write(str(i["jzmj"])+"\t")

            f.write(str(i["sbzz"])+"\t")

            f.write(str(i["dmxzyqsbz"])+"\t")
            f.write(str(i["yqsbzs"])+"\t")
            f.write(str(i["dxyqsbs"])+"\t")
            f.write(str(i["sjjxgws"])+"\n")
        time.sleep(3)
if __name__ == "__main__":
    export_zyjsZyjbtjXnsxjd()
    
    