'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-28 19:06:01
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json

def export_kcjsKcxx():
    url="http://zzxx.jse.edu.cn/msc-api/api/tour/kcjsKcxx/list"
    
    
    
    header={"Host": "zzxx.jse.edu.cn",
        "Content-Length": "65",
        "Menu": "/head/Page/tour6/kcjsKcxx",
        "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Userid": "3da07989cd9468e869d3f599346ad4f4",
        "Token": "3da07989cd9468e869d3f599346ad4f4",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://zzxx.jse.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://zzxx.jse.edu.cn/msc/index.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"}
    f=open("小程序/全国中等职业学校管理信息系统/data.txt","w")
    f.write("课程号\t")
    f.write("课程名称\t")
    f.write("\n")
    for i in range(1,6):
        data={"userId":"986e2223930e159dba69acc69851ba19","page":i,"limit":500}
        data=json.dumps(data)
        proxies={'http':'http://127.0.0.1:8080'}
        requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
        print(requests_data.text)
        data=json.loads(requests_data.text)
        
        
        for i in data["data"]["list"]:
            f.write(str(i["bxzybh"])+"\t")
            f.write(str(i["sfmlwzy"])+"\t")
            f.write("\n")
    f.close()


if __name__ == "__main__":
    export_kcjsKcxx()
    
    
