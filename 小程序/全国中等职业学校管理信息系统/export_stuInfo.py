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

def export_caseSchoolTrainResource():
    url="http://zzxx.jse.edu.cn/msc-api/api/tour/stuInfo/list"
    
    
    
    header={"Host": "zzxx.jse.edu.cn",
        "Content-Length": "65",
        "Menu": "/head/Page/tour1/stuInfo",
        "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Userid": "066646e9213842e6fb6780a9ac65b35f",
        "Token": "066646e9213842e6fb6780a9ac65b35f",
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
    for i in range(1,8):
        data={"userId":"986e2223930e159dba69acc69851ba19","page":i,"limit":500}
        data=json.dumps(data)
        proxies={'http':'http://127.0.0.1:8080'}
        requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
        print(requests_data.text)
        data=json.loads(requests_data.text)
        f.write("学籍号\t")
        f.write("姓名\t")
        f.write("学号\t")
        f.write("出生日期\t")
        f.write("国籍地区\t")
        f.write("性别\t")
        f.write("民族\t")
        f.write("政治面貌\t")
        f.write("班级\t")
        f.write("年级\t")
        f.write("xxdm\t")
        f.write("\n")
        
        for i in data["data"]["list"]:
            f.write(str(i["xjh"])+"\t")
            f.write(str(i["xm"])+"\t")
            f.write(str(i["xh"])+"\t")
            f.write(str(i["csrq"])+"\t")
            f.write(str(i["gjdq"])+"\t")
            f.write(str(i["xbm"])+"\t")
            f.write(str(i["mzm"])+"\t")
            f.write(str(i["zzmmm"])+"\t")
            f.write(str(i["szbj"])+"\t")
            f.write(str(i["sznj"])+"\t")
            f.write(str(i["xxdm"])+"\t")
            f.write("\n")
    f.close()


if __name__ == "__main__":
    export_caseSchoolTrainResource()
    
    
