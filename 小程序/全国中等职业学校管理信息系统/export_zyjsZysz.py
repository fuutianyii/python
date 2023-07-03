'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-28 12:19:14
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json

def export_caseSchoolTrainResource():
    url="http://zzxx.jse.edu.cn/msc-api/api/tour/zyjsZysz/list"
    data={"userId":"986e2223930e159dba69acc69851ba19","page":1,"limit":30}
    data=json.dumps(data)
    
    header={"Host": "zzxx.jse.edu.cn",
        "Content-Length": "65",
        "Menu": "/head/Page/tour1/zyjsZysz",
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
    proxies={'http':'http://127.0.0.1:8080'}
    requests_data=requests.post(url,proxies=proxies,data=data,headers=header)
    data=json.loads(requests_data.text)
    f=open("小程序/全国中等职业学校管理信息系统/data.txt","w")
    f.write("专业名称\t")
    f.write("本校专业编号\t")
    f.write("专业大类\t")
    f.write("专业大类代码\t")
    f.write("专业类\t")
    f.write("专业类代码\t")
    f.write("专业（技能）方向\t")
    f.write("学历/非学历教育\t")
    f.write("办学层次\t")
    f.write("学分制/学年制\t")
    f.write("学制\t")
    f.write("学习形式\t")
    f.write("培养模式\t")
    f.write("高校专业代码\t")
    f.write("高校专业名称\t")
    f.write("高校名称\t")
    f.write("批准设置日期\t")
    f.write("首次招生日期\t")
    f.write("职业资格证书\t")
    f.write("开设机构\t")
    f.write("专业办学状态\t")
    f.write("停招日期\t")
    f.write("撤销日期\t")
    f.write("所属机构\t")
    f.write("\n")
    
    for i in data["data"]["list"]:
        f.write(str(i["zydm"])+"-"+i["zymc"]+"\t")
        f.write(str(i["bxzybh"])+"\t")
        f.write(str(i["zydl"])+"\t")
        f.write(str(i["zydldm"])+"\t")
        f.write(str(i["zyl"])+"\t")
        f.write(str(i["zyldm"])+"\t")
        f.write(str(i["zyfx"])+"\t")
        f.write(str(i["xljy"])+"\t")
        f.write(str(i["bxcc"])+"\t")
        f.write(str(i["xfz"])+"\t")
        f.write(str(i["xz"])+"\t")
        f.write(str(i["xxxs"])+"\t")
        f.write(str(i["pyms"])+"\t")
        f.write(str(i["zydm"])+"\t")
        f.write(str(i["zymc"])+"\t")
        f.write(str(i["gxmc"])+"\t")
        f.write(str(i["pzszrq"])+"\t")
        f.write(str(i["sczsrq"])+"\t")
        f.write(str(i["zyzgzs"])+"\t")
        f.write(str(i["ksjg"])+"\t")
        f.write(str(i["zybxzt"])+"\t")
        f.write(str(i["tzny"])+"\t")
        f.write(str(i["cxny"])+"\t")
        f.write(str(i["ssjg"])+"\t")
        f.write("\n")
    f.close()


if __name__ == "__main__":
    export_caseSchoolTrainResource()
    
    
