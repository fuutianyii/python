
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
作者：尘耀
简介：本脚本专门用于对习讯云APP每日签到，每周周报提交，每月月报提交
环境：python3环境，第三方requests、rsa库
最后编辑者：fuutianyii
最后编辑时间：2023/4/23
版本：version 3.0
注意：读README.md，需要首先手动签到过一次。
tips:貌似sign_resources_info有第一次签到的信息，不需要用户获取地址写配置文件，但是写都写了就懒得改了捏。
"""
import uuid
import copy
import random
import json
import rsa
import requests
import base64
from http import client
from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib import parse
from python_mail import python_mail
from time import sleep
import argparse
client.HTTPConnection._http_vsn=10
client.HTTPConnection._http_vsn_str='HTTP/1.1'

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CONFIG = {}
proxy = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
proxy = {'http': '', 'https': ''}
class XIXUNYUN:
    def __init__(self, username, password, schoolId="1622"):
        # 学校ID 默认 苏高职1622
        self.schoolId = schoolId
        # 用户名和密码
        self.username = username
        self.password = password
        # Token
        self.token = None
        
        # 设备ID
        self.deviceId = uuid.uuid4().hex
        # 设备MAC
        self.mac = "%3A".join(["%02x" % x for x in map(lambda x: random.randint(0,255), range(6))])
        # Session
        self.session = requests.Session()
        self.session.verify=False
        self.session.proxies=proxy

        # 登录URL
        self.loginUrl = "https://api.xixunyun.com/login/api?from=app&version=5.0.3&platform=android&entrance_year=0&graduate_year=0&school_id=%s" % self.schoolId
        # 签到URL
        self.signUrl = "https://api.xixunyun.com/signin_rsa?token=%s&from=app&version=5.0.3&platform=android&entrance_year=0&graduate_year=0&school_id=%s"
        # 周报月报URL
        self.weeklyReportUrl = "https://api.xixunyun.com/Reports/StudentOperator"
        self.MonthlyReportUrl = "https://api.xixunyun.com/Reports/StudentOperator"
        
        # 获取签到信息URL
        self.getSignUrl = "https://api.xixunyun.com/signin40/homepage?month_date=%s&token=%s&from=app&version=5.0.3&platform=android&entrance_year=0&graduate_year=0&school_id=%s"
        # 获取周报月报信息URL
        self.getWeelkyReport = "https://api.xixunyun.com/Reports/StudentSearch"
        self.getMontlhyReport = "https://api.xixunyun.com/Reports/StudentSearch"
        
        # 默认header头
        self.defaultHeader = {
            'Host': 'api.xixunyun.com',
            'User-Agent': 'okhttp/3.8.0',
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip",
            "Connection": None,
            "Accept": None
        }
        
        #加密公钥 别问我为啥需要我也不知道 网上找的
        self.rsa_public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlYsiV3DsG" \
                 "+t8OFMLyhdmG2P2J4GJwmwb1rKKcDZmTxEphPiYTeFIg4IFEiqDCA" \
                 "TAPHs8UHypphZTK6LlzANyTzl9LjQS6BYVQk81LhQ29dxyrXgwkRw9RdWa" \
                 "MPtcXRD4h6ovx6FQjwQlBM5vaHaJOHhEorHOSyd/deTvcS+hRSQIDAQAB\n-----END PUBLIC KEY-----\n"
        
    
    def public_encrypt(self, raw_data):
        pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(self.rsa_public_key)
        base46_enc = base64.b64encode(rsa.encrypt(raw_data.encode(), pub_key))
        return base46_enc.decode('utf-8')
    
    def getSignTimeInfo(self):
        """获取签到url需要的日期参数

        Returns:
            str: 日期字符串
        """
        return "%s-%s" % (datetime.today().year, datetime.today().month)
    
    def ifisToday(self, timeStamp):
        """返回是否是今天

        Args:
            timeStamp (int): 时间戳

        Returns:
            bool: 是否是今天
        """
        inputDate = date.fromtimestamp(int(timeStamp))
        todayDate = date.today()
        return inputDate == todayDate
    
    def login(self):
        data = {
            'platform':2,
            'password':self.password,
            'app_version':'5.0.3',
            'key':'',
            'mac':self.mac,
            'uuid':'2ce5e26e048f01e9',
            'app_id':'cn.vanber.xixunyun.saas',
            'system':'6.0.1',
            'account':self.username,
            'school_id':self.schoolId,
            'request_source':'3',
            'registration_id':'140fe1da9e4a5848359',
            'model':''
        }
        header = copy.copy(self.defaultHeader)
        header["content-type"] = "application/x-www-form-urlencoded"
        res = self.session.post(url=self.loginUrl, headers=header, data=data, verify=False)
        if res.status_code == 200:
            print
            self.token = res.json()["data"]["token"]
            return {"code":1}
        else:
            return {"code":0, "message":"用户：%s未获取到Token" % self.username}
    
    def sign(self, address, addressName, remark, comment, latitude, longitude, city, province):
        res = self.getSignInfo()
        if res["code"] == 1:
            return {"code":0, "message":"用户：%s已签到过" % self.username}
        elif res["code"] == -1:
            return {"code":0, "message": res["message"]}
        elif res["code"] == -2:
            return {"code":0, "message": "用户：%s 请求获取签到网页失败\n请联系管理员脚本出现问题" % self.username}
        
        data = {
            "address": address,
            "province": province,
            "city": city,
            "latitude": self.public_encrypt(latitude),
            "remark": remark,
            "comment": comment,
            "address_name": addressName,
            "change_sign_resource": 0,
            "longitude": self.public_encrypt(longitude),
            
            
        }
        res = self.session.post(
            url=self.signUrl % (self.token, self.schoolId),
            headers=self.defaultHeader,
            data=data,
        )
        res = res.json()
        if res["code"] == 20000:
            return {"code":1, "message":res}
        else:
            print(res)
            return {"code":0, "message":"用户：%s签到失败" % self.username}
        

    def getSignInfo(self):
        """获取签到信息

        Returns:
            dict: 是否签到过
        """
        res = self.session.get(
            url=self.getSignUrl % (self.getSignTimeInfo(), self.token, self.schoolId),
            headers=self.defaultHeader
        )
        res = res.json()
        if res["code"] == 20000:
            if res["data"]["sign_resources_info"] == None:
                return {"code":-1, "message":"用户：%s没有手动签到过一次，请手动签到第一次" % self.username}
            if res["data"]["sign_in_month"]:
                for signDict in res["data"]["sign_in_month"]:
                    if self.ifisToday(signDict["sign_time"]):
                        return {"code":1}
                    pass
                return {"code":0}
            else:
                return {"code":0}
        else:
            return {"code":-2}
    
    def getWeeklyReport(self):
        """获取最新周报信息

        Returns:
            Dict/None: 返回周报信息，若没有周报返回None
        """
        data = {
            "business_type": "week",
            "page_size": "20",
            "order": "create_time.desc",
            "page_no": "1",
            "token": self.token,
            "from": "app",
            "version": "5.0.3",
            "platform": "android",
            "entrance_year": "0",
            "graduate_year": "0",
            "school_id": self.schoolId
        }
        res = self.session.get(
            url=self.getWeelkyReport,
            params=data,
            headers=self.defaultHeader
        )
        res = res.json()
        if res["code"] == 20000:
            if res["data"]["list"] == None:
                return {"code":1, "message":None}
            else:
                return {"code":1, "message":res["data"]["list"][0]}
        else:
            return {"code":0}
        pass
        
    def submitWeeklyReport(self, submitMessageList):
        """提交周报

        Args:
            submitMessageList (list): 提交内容列表

        Returns:
            dict: 返回值
        """
        # 获取本周的周一和周日
        today = date.today()
        startDate = datetime.strftime(today - timedelta(today.weekday()), "%Y/%m/%d")
        endDate = datetime.strftime(today + timedelta(7 - today.weekday() - 1), "%Y/%m/%d")
        
        newReport = self.getWeeklyReport()
        if newReport["code"] == 0:
            return {"code":0, "message":"用户：%s请求获取周报信息失败" % self.username}
        data = newReport["message"]
        if data:
            # 判断是否今天已经提交过了
            SubmitTime = date.fromtimestamp(int(data["create_time"]))
            if SubmitTime >= (today - timedelta(today.weekday())):
                return {"code":0, "message":"用户：%s周报已经提交过" % self.username}
            # SubmitTime = date.fromtimestamp(int(data["create_time"]))
            # NowTime = date.today()
            # tmp = (NowTime-SubmitTime).days
            # if tmp == 0:
            #     return {"code":0, "message":"用户：%s周报已经提交过" % self.username}
        # 提交周报
        content = [
            {
                "content": submitMessageList[0],
                "require": "1",
                "sort": "1",
                "title": "实习工作具体情况及实习任务完成情况"
            },
            {
                "content": submitMessageList[1],
                "require": "0",
                "sort": "2",
                "title": "主要收获及工作成绩"
            },
            {
                "content": submitMessageList[2],
                "require": "0",
                "sort": "3",
                "title": "工作中的问题及需要老师的指导帮助"
            }
        ]
        urlArgs = {
            "token": self.token,
            "from": "app",
            "version": "5.0.3",
            "platform": "android",
            "entrance_year": "0",
            "graduate_year": "0",
            "school_id": self.schoolId
        }
        data = {
            "business_type":"week",
            "end_date":endDate,
            "content":content,
            "attachment":"",
            "start_date":startDate
        }
        data = parse.urlencode(data).replace("+","").replace("%27", "%22")
        header = copy.copy(self.defaultHeader)
        header["content-type"] = "application/x-www-form-urlencoded"
        res = self.session.post(
            url=self.weeklyReportUrl,
            params=urlArgs,
            data=data,
            headers=header
        )
        res = res.json()
        if res["code"] == 20000:
            return {"code":1, "message":"用户：%s \n本周(%s-%s)周报已成功提交" % (self.username, startDate, endDate)}
        else:
            return {"code":0, "message":"用户：%s 本周周报提交失败" % self.username}
        pass

    def getMonthlyReport(self):
        """获取最新周报信息

        Returns:
            Dict/None: 返回周报信息，若没有周报返回None
        """
        data = {
            "business_type": "month",
            "page_size": "20",
            "order": "create_time.desc",
            "page_no": "1",
            "token": self.token,
            "from": "app",
            "version": "5.0.3",
            "platform": "android",
            "entrance_year": "0",
            "graduate_year": "0",
            "school_id": self.schoolId
        }
        res = self.session.get(
            url=self.getMontlhyReport,
            params=data,
            headers=self.defaultHeader
        )
        print("-",res.text,"-")
        res = res.json()
        if res["code"] == 20000:
            if res["data"]["list"] == None:
                return {"code":1, "message":None}
            else:
                print(res)
                return {"code":1, "message":res["data"]["list"][0]}
        else:
            return {"code":0}
        pass

    def is_current_month(self,timestamp):
        # 将时间戳转换为 datetime 对象
        print(timestamp)
        ldate = datetime.fromtimestamp(timestamp)
        
        # 获取当前日期
        today = date.today()
        
        # 获取本月月初日期
        first_day_of_month = today.replace(day=1)
        
        # 获取下个月的月初日期，然后减去一天
        last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1) - timedelta(days=1))
        
        # 判断日期是否在本月范围内
        return first_day_of_month <= ldate.date() <= last_day_of_month


    def submitMonthlyReport(self, submitMessageList):
        """提交月报

        Args:
            submitMessageList (list): 提交内容列表

        Returns:
            dict: 返回值
        """
        # 获取本月月初和月底日期
        today = date.today()
        startDate = today.replace(day=1)
        endDate = (startDate.replace(month=startDate.month % 12 + 1, day=1) - timedelta(days=1))

        
        newReport = self.getMonthlyReport()
        print("getMonthReport")
        if newReport["code"] == 0:
            return {"code":0, "message":"用户：%s请求获取月报信息失败" % self.username}
        data = newReport["message"]
        if data:
            # 判断是否今天已经提交过了
            if (self.is_current_month(int(data["create_time"]))):
                return {"code":0, "message":"用户：%s月报已经提交过" % self.username}
            # SubmitTime = date.fromtimestamp(int(data["create_time"]))
            # NowTime = date.today()
            # tmp = (NowTime-SubmitTime).days
            # if tmp == 0:
            #     return {"code":0, "message":"用户：%s月报已经提交过" % self.username}
        # 提交月报
        content = [
            {
                "content": submitMessageList[0],
                "require": "1",
                "sort": "1",
                "title": "实习工作具体情况及实习任务完成情况"
            },
            {
                "content": submitMessageList[1],
                "require": "0",
                "sort": "2",
                "title": "主要收获及工作成绩"
            },
            {
                "content": submitMessageList[2],
                "require": "0",
                "sort": "3",
                "title": "工作中的问题及需要老师的指导帮助"
            }
        ]
        urlArgs = {
            "token": self.token,
            "from": "app",
            "version": "5.0.3",
            "platform": "android",
            "entrance_year": "0",
            "graduate_year": "0",
            "school_id": self.schoolId
        }
        data = {
            "business_type":"month",
            "end_date":endDate,
            "content":content,
            "attachment":"",
            "start_date":startDate
        }
        data = parse.urlencode(data).replace("+","").replace("%27", "%22")
        header = copy.copy(self.defaultHeader)
        header["content-type"] = "application/x-www-form-urlencoded"
        res = self.session.post(
            url=self.MonthlyReportUrl,
            params=urlArgs,
            data=data,
            headers=header
        )
        res = res.json()
        if res["code"] == 20000:
            return {"code":1, "message":"用户：%s \n本周(%s-%s)月报已成功提交" % (self.username, startDate, endDate)}
        else:
            return {"code":0, "message":"用户：%s 本周月报提交失败" % self.username}
        pass

def pushtoWechat(token, content, title="习讯云签到"):
    """ 推送消息至微信 官网：http://www.pushplus.plus

    Args:
        token (str): pushpush申请的token
        content (str): 发送内容
        title (str, optional): 标题. Defaults to "习讯云签到".

    Returns:
        bool: 是否发送成功
    """
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    res = requests.post(
        'http://www.pushplus.plus/send',
        data=body,
        headers=headers
    )
    if res.json()["code"] == "200":
        return True
    else:
        return False
    
def pushtoMail(mail, content, title="习讯云签到"):
    """ 推送消息至微信 官网：http://www.pushplus.plus

    Args:
        mail (str): mail接收者地邮箱地址
        content (str): 发送内容
        title (str, optional): 标题. Defaults to "习讯云签到".
    """
    global CONFIG
    pymail=python_mail("qq",CONFIG["mail_provider"],CONFIG["mail_provider_password"])
    pymail.send_email(mail,title,content)
    

def readConfig(path):
    """获取配置文件
    """
    global CONFIG
    with open(path,'r',encoding='utf-8') as f:
        CONFIG = json.load(f)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-c', '--config', type=str ,default="config.json" ,help='config path')
    args = parser.parse_args()
    readConfig(args.config)
    for userDict in CONFIG["userList"]:
        userObj = XIXUNYUN(
            userDict["username"],
            userDict["password"],
            schoolId=CONFIG["schoolId"],
            # mail_type=CONFIG["mail_type"],
            # mail_provider=CONFIG["mail_provider"],
            # mail_provider_password=CONFIG["mail_provider_password"],
        )        
        res = userObj.login()
        today = datetime.today().weekday()
        day = datetime.today().day
        if res["code"]:
            print("%s 登录成功" %userDict["username"])
            sleep(4) #sleep 防检测

            # 签到功能
            lifeMode = userDict["lifeMode"][today]
            signInfo = userDict[lifeMode]
            res = userObj.sign(
                signInfo["address"],
                signInfo["address_name"], 
                signInfo["remark"], 
                signInfo["comment"], 
                signInfo["latitude"], 
                signInfo["longitude"], 
                signInfo["city"], 
                signInfo["province"]
            )
            if res["code"]:
                resObj = res["message"]
                message = "用户：%s\n时间: %s\n持续天数：%s\n信息：%s" % (userDict["username"],str(datetime.today()), resObj["data"]["continuous"], resObj["data"]["message_string"])
                print(message)
                # pushtoWechat(userDict["pushToken"], message, title="习讯云签到成功提示")
                pushtoMail(userDict["mail"], message, title="习讯云签到成功提示")
            else:
                print(res["message"])
                # pushtoWechat(userDict["pushToken"], res["message"])
                pushtoMail(userDict["mail"], res["message"], title="习讯云签到异常")
            
            # 周报功能
            if userDict.get("weeklyReport"):
                weeklyReport = userDict["weeklyReport"]
                if weeklyReport == today:
                    res = userObj.submitWeeklyReport(userDict["weeklyReportMessage"])
                    print(res["message"])
                    if res["code"]:
                        # pushtoWechat(userDict["pushToken"], res["message"],title="习讯云周报提交成功提示")
                        pushtoMail(userDict["mail"], res["message"], title="习讯云周报提交成功提示")
                    else:
                        # pushtoWechat(userDict["pushToken"], res["message"])     
                        pushtoMail(userDict["mail"], res["message"], title="习讯云周报异常")
            # 月报功能
            if userDict.get("monthlyReport"):
                monthlyReport = userDict["monthlyReport"]
                if monthlyReport == day:
                    print("post monthly")
                    res = userObj.submitMonthlyReport(userDict["monthlyReportMessage"])
                    print(res["message"])
                    if res["code"]:
                        # pushtoWechat(userDict["pushToken"], res["message"],title="习讯云周报提交成功提示")
                        pushtoMail(userDict["mail"], res["message"], title="习讯云月报提交成功提示")
                    else:
                        # pushtoWechat(userDict["pushToken"], res["message"])     
                        pushtoMail(userDict["mail"], res["message"], title="习讯云月报异常")
        else:
            print(res["message"])
            # pushtoWechat(userDict["pushToken"], res["message"])
            pushtoMail(userDict["mail"], res["message"], title="习讯云ERROR")
