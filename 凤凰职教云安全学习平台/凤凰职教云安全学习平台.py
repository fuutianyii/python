#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 尘耀
Date: 2022-12-08 18:47:07
LastEditors: fuutianyii
LastEditTime: 2022-12-27 13:26:04
mail: 1205509967@qq.com
QQ: 1205509967
'''

import requests
import json
import struct
import random
import time
import os

class SuzhouAnquan:
    def __init__(self, username, password, schoolId = "kjhaggstpvfawmyvqixvq"):
        self.user = username
        self.pasw = password
        self.schoolId = schoolId
        self.varInit()
        self.urlInit()
        self.header = {
            'Accept':'application/json, text/plain, */*',
            'Host': 'aq.fhmooc.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://aq.fhmooc.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://aq.fhmooc.com/home'
        }
    def varInit(self):
        self.userId = None
        self.quesType = None
        self.questionListDict = None
        self.allQuestionDict = {}
        self.session = requests.Session()

    def urlInit(self):
        self.loginUrl = "https://aq.fhmooc.com/api/common/Login/login"
        self.getMoudleUrl = "https://aq.fhmooc.com/api/portal/CellManager/getModuleList"
        self.getMoudleInfoUrl = "https://aq.fhmooc.com/api/portal/CourseIndex/getModuleInfo"
        self.quesTypeUrl = "https://aq.fhmooc.com/api/portal/PaperStuByQuesType/getQuesType"
        self.questiontypePractice = "https://aq.fhmooc.com/api/portal/PaperStuByQuesType/getModuleQuesList"
        self.questionInfoUrl = "https://aq.fhmooc.com/api/portal/PaperStuByQuesType/getQuestionInfo"
        self.addTimeUrl = "https://aq.fhmooc.com/api/design/LearnCourse/statStuProcessCellLogAndTimeLong"
        self.getPaperUrl = "https://aq.fhmooc.com/api/design/PaperIndex/getPaperList"
        self.getStuPaperListUrl = "https://aq.fhmooc.com/api/design/PaperStudent/getStuPaper"
        self.saveAnswerUrl = "https://aq.fhmooc.com/api/design/PaperStudent/saveStuQuesAnswer"
        self.submitUrl = "https://aq.fhmooc.com/api/design/PaperStudent/submitStuPaper"
        
    def login(self):
        data = {
            "schoolId": self.schoolId,
            "userName": self.user,
            "userPwd": self.pasw
        }
        resDict = self.session.post(self.loginUrl, data=data, headers=self.header).json()
        if resDict["code"] == 1:
            self.userId = resDict["userId"]
            self.echo(self.user+resDict["msg"], resDict["code"])
        else:
            self.echo(resDict["msg"], resDict["code"])

    def getQuesType(self):
        resDict = self.session.post(self.quesTypeUrl).json()
        if resDict['code'] == 1:
            self.quesType = resDict
            self.echo("单选题:%s, 多选题:%s, 判断题:%s" % (resDict['quesTypeList'][0]['count'], resDict['quesTypeList'][1]['count'], resDict['quesTypeList'][2]['count']))
        else:
            self.echo("获取题目数量出错")

    def getAllQuesDict(self, questionType):
        data = {
            'courseId':"",
            'quesType': questionType
        }
        resDict = self.session.post(self.questiontypePractice, data=data).json()
        if resDict["code"] == 1:
            self.echo("获取题目列表成功")
            return resDict["quesIds"]
        else:
            self.echo("获取总题目列表出错", resDict["code"])
            return None
    
    def getQuestionInfo(self, quesId):
        data = {
            'courseId':"",
            'quesId': quesId
        }
        resDict = self.session.post(self.questionInfoUrl, data=data).json()
        if resDict["code"] == 1:
            return resDict['quesInfo'][0]
        else:
            self.echo("获取总题目列表出错", resDict["code"])
            return None
            
    def run(self, addTime=0, ifAnswer=True):
        self.login()
        addTime=addTime*3600
        #self.getTiku()
        if addTime != 0:
            #self.openTask()
            res = self.addStudyTime(addTime)
            if res:
                self.echo("已增加学习时间 %s 秒" % addTime)
            else:
                self.echo("增加学习时间错误")
        
        if ifAnswer:
            fileName = os.path.join(os.path.dirname(__file__),"凤凰职教云安全学习平台题库.json")
            if os.path.isfile(fileName):
                self.readJson(fileName)
                self.echo("读取题库成功")
            # print(self.allQuestionDict)
            # 此处打印题库
            self.startAnswer()

    def startAnswer(self):
        paperId = self.getPaperId()
        paperDict = self.getPaperList(paperId)
        paperQuesList = paperDict["stuPaperQuesList"]
        paperId = paperDict["paperId"]
        paperStuId = paperDict["paperStuId"]
        
        for paperDict in paperQuesList:
            self.saveStudentAnwer(paperStuId, paperId, paperDict["quesId"])
        self.submitAnswer(paperStuId, paperId)
    
    def submitAnswer(self, paperStuId, paperId):
        data = {
            'paperStuId': paperStuId,
            'paperId': paperId
        }
        resDict = self.session.post(self.submitUrl, data=data).json()
        print(resDict)
        
    
    def saveStudentAnwer(self, paperStuId, paperId, questId):
        try:
            data = {
                "paperStuId": paperStuId,
                "paperId": paperId,
                "quesId": questId,
                "answerJson":"{\"quesId\":\"%s\",\"answer\":\"%s\"}" % (questId, self.getAnswerStr(self.allQuestionDict[questId]['answers']))
            }
        except:
            data = {
                "paperStuId": paperStuId,
                "paperId": paperId,
                "quesId": questId,
                "answerJson":"{\"quesId\":\"%s\",\"answer\":\"%s\"}" % (questId, "1")
            }
        # print(data)
        # 此处查看单次答题情况
        resDict = self.session.post(self.saveAnswerUrl, data=data).json()
        if resDict["code"] == 1:
            return True
        else:
            return False
    
    def getAnswerStr(self, answerList):
        tmp = ""
        for answer in answerList:
            tmp += "%s；" % answer
        return tmp[:-1]

    def getPaperList(self, paperId):
        data = {
            "courseId": paperId
        }
        resDict = self.session.post(self.getStuPaperListUrl, data=data).json()
        if resDict["code"] == 1:
            return resDict
        else:
            return []

    def getPaperId(self):
        resDict = self.session.post(self.getPaperUrl).json()
        if resDict["code"] == 1:
            return resDict["list"][0]['id']
        else:
            return None
    
    def openTask(self):
        resDict = self.session.post(self.getMoudleUrl).json()
        taskId = resDict["list"][0]["id"]
        data = {
            "moduleId": taskId
        }
        resDict = self.session.post(self.getMoudleInfoUrl, data=data).json()
    
    def addStudyTime(self, addTime):
        data = {
            'courseId':"qkcfawcsxyrom0zrwghhwq",
            'moduleIds':"gphvaoit9k5i4bmeyrrfaw",
            'cellId':"lkdaoit0qziwjjkhvwq",
            'auvideoLength': addTime,
            'videoTimeTotalLong': addTime
        }
        resDict = self.session.post(self.addTimeUrl, data=data).json()
        if resDict["code"] == 1:
            return True
        else:
            return False

    def getTiku(self):
        self.getQuesType()
        for i in range(1,4):
            questionListDict = self.getAllQuesDict(i) 
            i = 1
            maxLen = len(questionListDict)
            for questionIdDict in questionListDict:
                questionId = questionIdDict['id']
                info = self.getQuestionInfo(questionId)
                self.allQuestionDict[questionId] = info
                self.echo("%s/%s 题目ID: %s 题目类型: %s 题目: %s 答案: %s" % (i, maxLen, info["questionId"], info['questionType'], info['Content'], info['answers']))
                i+=1
                time.sleep(0.1)
        self.write(self.allQuestionDict)
        print("ok")

    def write(self, data):
        with open("%sTESTSSS.txt" % random.randint(1,1000), "w+") as f:
            json.dump(data, f)
    
    def readJson(self, fileName):
        with open(fileName) as f:
            self.allQuestionDict = json.load(f)
    
    def echo(self, message, code = 0):
        print("[Code:%s]> %s" % (code, message))

class Shell:
    def __init__(self):
        #welcome
        self.auto = input("是否自动模式?(Yes（默认）/No)")        
        if self.auto in {"","yes","y"}:
            print("自动模式启动")
        print("请输入您的账号和密码!")
        self.user = input("账号:")
        self.passwd = input("密码:")
        #self.isAddTime()
        #self.isAnswer()
    def isAddTime(self):
        if self.auto in {"","yes","y"}:
            return 10  
        isaddtime = input("是否添加学习时长?(Yes/No)")
        if isaddtime.lower() in {"yes","y"}:
            return self.getAddTime()
        elif isaddtime.lower() in {"no","n"}:
            return 0
        else:
            self.isAddTime()
    def getAddTime(self):
        time = input("请输入需要添加的时长!(单位:小时)")
        if time.isdigit():
        #if True:
            return int(time)
        else:
            print("输入的时长不正确!")
            self.getAddTime()
    def isAnswer(self):
        if self.auto in {"","yes","y"}:
            return True  
        isanswer = input("是否答题?(Yes/No)")
        if isanswer.lower() in {"yes","y"}:
            return True
        elif isanswer.lower() in {"no","n"}:
            return False
        else:
            self.isAnswer()

if __name__ == "__main__":
    # https://aq.fhmooc.com/assessDetail/qkcfawcsxyrom0zrwghhwq 查看是否通过
    shell = Shell()
    res = SuzhouAnquan(shell.user, shell.passwd)  # 用户名 密码
    res.run(shell.isAddTime(), shell.isAnswer())
    input("https://aq.fhmooc.com/assessDetail/qkcfawcsxyrom0zrwghhwq 查看是否通过")
    # os.system('pause')