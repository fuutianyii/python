'''
Author: fuutianyii
Date: 2023-02-12 13:52:32
LastEditors: fuutianyii
LastEditTime: 2023-04-15 20:32:17
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from os import remove, system,path,mkdir
from threading import Thread,enumerate
import requests
import re
from base64 import b64encode

class selenium_driver():
    def __init__(self,url,path,timeout=1):
        self.path=path
        self.timeout=timeout
        self.url=url
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        option = webdriver.ChromeOptions()
        option.add_argument(r"--user-data-dir=F:\python\python爬虫_视频\Data_Backup")
        option.add_argument(r'--disk-cache-dir=F:\python\python爬虫_视频\Data_Backup')
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        option.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(desired_capabilities=caps,options=option)
        self.driver.get(self.url)

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
    
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def get_network_source(self):
        browser_log = self.driver.get_log('performance')
        self.events = [self.process_browser_log_entry(entry) for entry in browser_log]
        self.events = [event for event in self.events if 'Network.responseReceived' in event['method']]
        # self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': self.events[0]["params"]["requestId"]})
        
    
    def process_browser_log_entry(self,entry):
        response = json.loads(entry['message'])['message']
        return response
    
    def flei(self,key,path,lesson_id):
        for i in self.events:
            if i['method'] == "Network.responseReceived":
                if ".ts" in i['params']["response"]['url']:
                    ts_url=(i['params']["response"]['url'])
                    self.ts_url=ts_url
        for i in self.events:
            if i['method'] == "Network.responseReceived":
                if key in i['params']["response"]['url']:
                    m3u8_url=(i['params']["response"]['url'])
                    self.download(m3u8_url,path,lesson_id)
      
      
    def scroll_to_bottom(self):
        self.cl=[]
        while len(self.driver.find_elements(by=By.CLASS_NAME, value="hint")) == 0:
            js="window.scrollBy(0,10000);"  
            self.driver.execute_script(js)
            
    def get_course_list(self):
        js = 'return window.__user_id;'
        self._uid = self.driver.execute_script(js)
        self.course_list=[]
        self.driver.get(self.url)
        self.scroll_to_bottom()
        self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="topics-item_main")
        num=0
        for c in self.cl:
            num+=1          
            self.course_list.append("["+c.text.replace('\n',' ')+"]"+str(num))
    
    
    def choose_course(self):
        
        id=1
        for course in self.course_list:
            print(str(id)+course)
            id+=1
        self.course_id=int(input("输入序号:"))-1
        self.dir_name=self.course_list[self.course_id]
        # self.f=open("D:/PotPlayer/Playlist/"+self.dir_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","")+".dpl","w",encoding="UTF-8")
        # self.f.write("DAUMPLAYLIST\ntopindex=0\nsaveplaypos=0\n")
        self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="topics-item_main")
        self.driver.execute_script("arguments[0].click();",self.cl[self.course_id])
        

    def get_lesson_list(self):
        self.lesson_list=[]
        self.scroll_to_bottom()
        self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
        num=0
        for c in self.cl:
            num+=1          
            self.lesson_list.append("["+c.text.replace('\n',' ')+"]"+str(num))
    
    def choose_lesson(self):
        id=1
        for lesson in self.lesson_list:
            print(str(id)+lesson)
            id+=1
        lesson_id=input("输入序号或输入'*'获取全部:")
        if self.is_number(lesson_id):
            print("only one")
            lesson_id=int(lesson_id)
            lesson_id=lesson_id-1
            self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
            self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
            self.download_name=self.lesson_list[lesson_id]
            time.sleep(self.timeout)
            self.get_network_source()
            self.flei(".m3u8",self.path,"")
        elif lesson_id == "*":
            for lesson_id in range(0,len(self.lesson_list)):
                self.scroll_to_bottom()
                self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
                self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
                self.download_name=self.lesson_list[lesson_id]
                time.sleep(self.timeout)
                self.get_network_source()
                self.flei(".m3u8",self.path,lesson_id)#为""时不下载视频文件，仅下载m3u8
                self.driver.back()
        elif lesson_id.find(":") !=-1:
            print("select range")
            lesson_id_list=lesson_id.split(":")
            if len(lesson_id_list) == 2:
                for lesson_id in range(int(lesson_id_list[0])-1,int(lesson_id_list[1])):
                    print("------"+str(lesson_id)+"--------")
                    self.scroll_to_bottom()
                    self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
                    self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
                    self.download_name=self.lesson_list[lesson_id]
                    time.sleep(self.timeout)
                    self.get_network_source()
                    self.flei(".m3u8",self.path,lesson_id)
                    self.driver.back()     
        elif lesson_id.find(",")!=-1:
            print("select selection")
            lesson_id_list=lesson_id.split(",")
            print(lesson_id_list)
            if len(lesson_id_list) != 0:
                for lesson_id in lesson_id_list:
                    lesson_id=int(lesson_id)-1
                    print("------"+str(lesson_id)+"--------")
                    self.scroll_to_bottom()
                    self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
                    self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
                    self.download_name=self.lesson_list[lesson_id]
                    time.sleep(self.timeout)
                    self.get_network_source()
                    self.flei(".m3u8",self.path,lesson_id)
                    self.driver.back()     
            else:
                self.choose_lesson()
        else:
            self.choose_lesson()
        # self.f.close()

    def download(self,m3u8_url,lpath,lesson_id):
        if lesson_id != "":
            lesson_id=lesson_id+1
            # self.f.write(str(lesson_id)+"*file*"+m3u8_url+"\n")
            # self.f.write(str(lesson_id)+"*title*"+self.download_name+"\n")
            # self.f.flush()
            print(str(lesson_id)+"*file*"+m3u8_url+"\n")
            print(str(lesson_id)+"*title*"+self.download_name+"\n")
        else:
            pass
        
        if lpath!="":
            print(self.download_name)
            self.download_name=self.download_name[:self.download_name.find("直播")]
            print(self.download_name)
            ##
            if path.exists(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]):
                pass
            else:
                mkdir(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")])
            
            
            
            
            m3u8_request=requests.get(m3u8_url)
            m3u8_data=m3u8_request.content.decode()
            if m3u8_data.find("EXT-X-KEY")==-1:
                print("开始下载")
                print("D:\Shandou\转码程序\m3u8DL.exe --workDir \""+(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]).replace("/","\\")+"\" \""+m3u8_url+"\" --saveName \"" +self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","").replace("[","").replace(" ","")+"\"  --enableDelAfterDone")
                system("D:\Shandou\转码程序\m3u8DL.exe --workDir \""+(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]).replace("/","\\")+"\" \""+m3u8_url+"\" --saveName \"" +self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","").replace("[","").replace(" ","")+"\"  --enableDelAfterDone")
            else:
                print("解密视频")
                pattern=re.compile("(.*)/v.f\d")
                result_list=pattern.findall(self.ts_url)
                base_url=result_list[0]+"/"
                pattern=re.compile("(&sign=.*)")
                result_list=pattern.findall(self.ts_url)
                tail=result_list[0]
                
                m3u8_request=requests.get(m3u8_url)
                m3u8_data=m3u8_request.content.decode()
                f=open(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"/"+"encode.m3u8","w")
                pattern=re.compile(".*\.ts.*")
                result_list=pattern.findall(m3u8_data)

                for ts in result_list:
                    m3u8_data=m3u8_data.replace(ts,base_url+ts+tail)
                m3u8_data=m3u8_data.replace("\",IV=",f"&uid={self._uid}\",IV=")
                f.write(m3u8_data)
                f.close()
                
                # pattern=re.compile("(?<=AES-128,URI=\").*(?=\",IV=)")
                # result_list=pattern.findall(m3u8_data)
                # key_url=result_list[0]+tail
                # rsp = requests.get(url=key_url)
                # rsp_data = rsp.content
                # print(key_url)
                # if len(rsp_data) == 16:
                #     userid_bytes = bytes(self._uid.encode(encoding='utf-8'))
                #     result_list = []
                #     for index in range(0, len(rsp_data)):
                #         result_list.append(
                #             rsp_data[index] ^ userid_bytes[index])
                #     print(result_list)
                #     self.key=b64encode(bytes(result_list)).decode()
                # else:
                #     print(f"获取异常，请求返回值：{rsp.text}")
                # system("D:\Shandou\转码程序\m3u8DL.exe --workDir \""+lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"\" \""+(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"/"+"encode.m3u8\"").replace("/","\\")+" --saveName \"" +self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","").replace("[","")+"\" --useKeyBase64 \""+self.key+"\" --enableDelAfterDone")
                print("D:\Shandou\转码程序\m3u8DL.exe --workDir \""+lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"\" \""+(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"/"+"encode.m3u8\"").replace("/","\\")+" --saveName \"" +self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","").replace("[","")+" --enableDelAfterDone")
                system("D:\Shandou\转码程序\m3u8DL.exe --workDir \""+lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"\" \""+(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"/"+"encode.m3u8\"").replace("/","\\")+" --saveName \"" +self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","").replace("[","")+" --enableDelAfterDone")
                remove(lpath+"/"+self.dir_name[1:self.dir_name.find(" 已更新")]+"/"+"encode.m3u8")
        else:
            pass
        
if __name__ == '__main__':
    url='https://appyawovj9f9922.h5.xiaoeknow.com/p/course/big_column/p_62ca351ee4b0c94264785dd8'
    # selenium_driver=selenium_driver(url,"",2.5)
    selenium_driver=selenium_driver(url,"F:/",2.5)
    selenium_driver.get_course_list()
    selenium_driver.choose_course()
    selenium_driver.get_lesson_list()
    selenium_driver.choose_lesson()
    input("下载完成，任意输入退出")