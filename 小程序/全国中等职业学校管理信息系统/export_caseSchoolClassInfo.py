'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-26 14:25:39
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json
import time

def export_caseSchoolTrainResource():
    url="http://zzxx.jse.edu.cn/msc-api/api/tour/caseSchoolClassInfo/list"
    data={"userId":"986e2223930e159dba69acc69851ba19",
          "page":1,
          "limit":110}
    data=json.dumps(data)
    
    header={"Host": "zzxx.jse.edu.cn",
        "Content-Length": "65",
        "Menu": "/head/Page/tour1/caseSchoolClassInfo",
        "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Userid": "9cf2949156c01bac5dfd18854a4ed196",
        "Token": "9cf2949156c01bac5dfd18854a4ed196",
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
    requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
    data=json.loads(requests_data.text)
    f=open("小程序/全国中等职业学校管理信息系统/data.txt","w")
    f.write("班号\t")
    f.write("班级名称\t")
    f.write("所属专业\t")
    f.write("本校专业编号\t")
    f.write("所在年级\t")
    f.write("入学学期\t")
    f.write("建班年月\t")
    f.write("校区名称\t")
    f.write("学生人数\t")
    f.write("学习形式\t")
    f.write("培养模式\t")
    f.write("联招合作类型\t")
    f.write("班级性质\t")
    f.write("班级状态\t")
    f.write("\n")
    
    for i in data["data"]["list"]:
        f.write(str(i["bh"])+"\t")
        f.write(str(i["bjmc"])+"\t")
        f.write(str(i["sszy"])+"\t")
        f.write(str(i["bxzybh"])+"\t")
        f.write(str(i["sznj"])+"\t")
        f.write(str(i["rxxq"])+"\t")
        f.write(str(i["jbny"])+"\t")
        f.write(str(i["xqmc"])+"\t")
        url="http://zzxx.jse.edu.cn//msc-api/api/tour/caseSchoolClassInfo/info/"+str(i["id"])
        data={"sing":"e2f4c4ca7cecf1f277632bb2cbd06ab5"}
        data=json.dumps(data)
        header={"Host": "zzxx.jse.edu.cn",
            "Content-Length": "65",
            "Menu": "/head/Page/tour1/caseSchoolClassInfo",
            "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Userid": "9cf2949156c01bac5dfd18854a4ed196",
            "Token": "9cf2949156c01bac5dfd18854a4ed196",
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
        requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
        detail_data=json.loads(requests_data.text)
        f.write(str(detail_data["data"]["xsrs"])+"\t")#班级人数无
        print(detail_data["data"]["xsrs"])
        f.write(str(i["xxxs"])+"\t")
        f.write(str(i["pyms"])+"\t")
        f.write(str(i["lzhzlx"])+"\t")
        f.write(str(i["bjxz"])+"\t")
        f.write(str(i["sffszzb"])+"\t")
        f.write("\n")
        time.sleep(3)
    f.close()


if __name__ == "__main__":
    export_caseSchoolTrainResource()
    
    
