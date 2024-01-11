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

def insert_stuEmployment():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/学生毕业信息（升学） (3升4)200_1人.xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuEmployment/save"
        # datas={"xxdm":"3632000472",
        #        "xm":i[1],
        #        "jzxmmc":i[2],
        #        "jzxmzl":"2",
        #        "jzbz":str(i[4]),
        #        "zzdwhgr":"1",
        #        "jfly":"1",
        #        "bz":"无",
        #        "xjh":i[0]
        #        }
        datas={"zy":i[5],
               "sxgjdq":"156",
               "cc":"2",
               "xsxxmc":"江苏联合职业技术学校",
               "xxdm":"3632000472",
               "xm":i[1],
               "xjh":i[0],
               "bynf":i[2],
               "byqx":"25",
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
            "Userid": "4250d13e52966121abf7fe8113e9735a",
            "Token": "4250d13e52966121abf7fe8113e9735a",
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
        print(i[1]+" "+datas)
        time.sleep(3)
if __name__ == "__main__":
    insert_stuEmployment()
    
    