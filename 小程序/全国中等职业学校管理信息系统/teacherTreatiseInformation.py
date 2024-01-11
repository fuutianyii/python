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

def insert_caseSchoolXsxxXsjzxx():
    pd.set_option('display.notebook_repr_html',False)
    # 读取xls（绝对路径）
    data=pd.read_excel(io=r'C:/Users/FTY/Downloads/教师论著信息-1.xlsx',header=0)
    data=data.values
    for i in data:
        url="http://zzxx.jse.edu.cn/msc-api/api/tour/teacherTreatiseInformation/save"
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
        brjs={
            "独立":"1",
            "第一":"2",
            "第二":"3",
            "第三":"4",
            "通讯作者":"5"
        }
        xkly={"法学,马克思主义理论":"3,35",
              "人文与社会科学":"2",
              "工学,电气工程":"8,88",
              "工学,机械工程":"8,82",
              "工学,计算机科学与技术":"8,812",
              "工学,信息与通信工程":"8,810",
              "教育学,教育学":"4,41",
              "教育学,体育学":"4,43",
              "经济学,应用经济学":"2,22",
              "理学,数学":"7,71",
              "其他":"999",
              "文学,外国语言文学":"5,52",
              "文学,中国语言文学":"5,51",
              "艺术学,美术学":"13,134"}
        datas={"xm":i[1],
               "jgh":i[0],
               "xxdm":"3632000472",
               "brjs":brjs[i[4]],
               "wszzlb":"6",
               "slqkArr":["9"],
               "kwdj":"3,32",
               "xkly":xkly[i[11]],
               "lzlbm":"2",
               "jcmc":i[2],
               "fbrq":i[3]}
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
        print(datas.decode())
        requests_data=requests.post(url,proxies=proxies,data=datas,headers=header)
        datas=requests_data.text
        print(i[1]+" "+datas)
        time.sleep(3)
if __name__ == "__main__":
    insert_caseSchoolXsxxXsjzxx()
    
    