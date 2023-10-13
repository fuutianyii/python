'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-28 15:07:43
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json
import pandas as pd
import time

def update_rdsj():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/390人团员.xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuInfo/list"
                        # /msc-api/api/tour/teacherTreatiseInformation/save
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
        
        datas={"userId":"986e2223930e159dba69acc69851ba19",
        "page":1,
        "limit":10,
        "xxdm":"3632000472",
        "xjh":i[0]}
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "a2e3e15881dc91ae692c01c9fae9fd9b",
            "Token": "a2e3e15881dc91ae692c01c9fae9fd9b",
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
        
        requests_data=requests.post(url,data=datas,headers=header)
        datas=json.loads(requests_data.text)
        id=datas["data"]["list"][0]["id"]
        # print(i[1]+" "+datas)
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuInfo/update"
                        # /msc-api/api/tour/teacherTreatiseInformation/save
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
        
        datas={"id":id,"xjh":i[0],"jxdh":i[11]}
        print(datas)
        datas=json.dumps(datas,ensure_ascii=False).encode("utf-8")
        
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/stuInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "a2e3e15881dc91ae692c01c9fae9fd9b",
            "Token": "a2e3e15881dc91ae692c01c9fae9fd9b",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Origin": "https://zzxx.jse.edu.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"}
        # proxies={'http':'http://127.0.0.1:8080'}
        # proxies=proxies
        requests_data=requests.post(url,data=datas,headers=header)
        print(i[1]+requests_data.text)
        time.sleep(3)



if __name__ == "__main__":
    
    update_rdsj()
    
    