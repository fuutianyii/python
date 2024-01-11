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

def insert_shcoolInnerOrg():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/我的校内机构.xlsx',header=0)
    data=data.values
    for i in data:
        print(i)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/shcoolInnerOrg/save"
        机构类别={"教学系部":"1","教科研机构":"2","公共服务":"3","党务部门":"4","行政机构":"5","附属单位":"6","后勤部门":"7","其他":"8"}
        datas={"addTime":"",
               "addUser":"",
               "children":[],
               "fzrgh":"",
               "fzrlxfs":"",
               "fzrrzrq":"",
               "fzrxm":"",
               "id":"",
               "jgdz":"",
               "jgh":str(i[0]),
               "jgjc":"",
               "jgjp":"",
               "jgjzgs":"",
               "jglbdm":str(机构类别[i[2]]),
               "jgmcdwmc":i[1],
               "jgszdxzqhm":"",
               "jgszdxzqhmqc":"",
               "jgywmc":"",
               "jgyxbs":"",
               "jgyzbm":"",
               "jgzt":"1",
               "jlny":"",
               "label":"",
               "lssjjgh":"",
               "lsxqh":"",
               "schooName":"",
               "sfst":"1",
               "sfxsjg":"",
               "status":"",
               "tree":["0"],
               "upTime":"",
               "upUser":"",
               "value":"",
               "xxdm":"3632000472"}
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
        print(str(i[0])+" "+datas)
        time.sleep(3)
if __name__ == "__main__":
    insert_shcoolInnerOrg()
    
    