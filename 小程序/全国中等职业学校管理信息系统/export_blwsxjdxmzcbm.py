'''
Author: fuutianyii
Date: 2023-06-26 10:02:16
LastEditors: fuutianyii
LastEditTime: 2023-06-26 11:13:38
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json

def export_caseSchoolTrainResource():
    url="http://zzxx.jse.edu.cn/msc-api/api/tour/caseSchoolTrainResource/list"
    data={"userId":"986e2223930e159dba69acc69851ba19","page":1,"limit":30}
    data=json.dumps(data)
    
    header={"Host": "zzxx.jse.edu.cn",
        "Content-Length": "65",
        "Menu": "/head/Page/tour1/caseSchoolTrainResource",
        "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Userid": "495c328c43e386c60e8258cd7a9f7552",
        "Token": "495c328c43e386c60e8258cd7a9f7552",
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
    print(requests_data.text)
    data=json.loads(requests_data.text)
    print(data)
    f=open("f:/desktop/hello.txt","w")
    f.write("实训基地名称\t")
    f.write("实训基地号\t")
    f.write("学年\t")
    f.write("批准日期/成立年度\t")
    f.write("面向专业\t")
    f.write("基地类别\t")
    f.write("是否服务中小学劳动教育实践基地\t")
    f.write("建筑面积\t")
    f.write("教学、实习仪器设备总值\t")
    f.write("当年新增仪器设备值\t")
    f.write("仪器设备总数\t")
    f.write("大型仪器设备数\t")
    f.write("实践教学工位数\t")
    f.write("管理人员\t")
    f.write("实训基地级别（1，2，3，4分别是国家，省级，地市及、其他）\t")
    f.write("\n")
    
    for i in data["data"]["list"]:
        f.write(str(i["sxjdmc"])+"\t")
        f.write(str(i["sxjdh"])+"\t")
        f.write(str(i["xnd"])+"\t")
        f.write(str(i["pzrq"])+"\t")
        f.write(str(i["zyzy"])+"\t")
        f.write(str(i["jdlb"])+"\t")
        f.write(str(i["sffwzxxldjysjjd"])+"\t")
        f.write(str(i["jzmj"])+"\t")
        f.write(str(i["jxsxyqsbz"])+"\t")
        f.write(str(i["dnxzyqsbz"])+"\t")
        f.write(str(i["yqsbzs"])+"\t")
        f.write(str(i["dxyqsbs"])+"\t")
        f.write(str(i["gws"])+"\t")
        f.write(str(i["glryzz"])+"\t")
        f.write(str(i["blwsxjdxmzcbm"])+"\t")
        f.write("\n")
    f.close()


if __name__ == "__main__":
    export_caseSchoolTrainResource()
    
    
