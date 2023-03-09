'''
Author: fuutianyii
Date: 2023-02-12 13:52:32
LastEditors: fuutianyii
LastEditTime: 2023-03-05 14:39:01
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from os import system,path,mkdir

class selenium_driver():
    def __init__(self,url,timeout=1):
        self.timeout=timeout
        self.url=url
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(desired_capabilities=caps)
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.add_cookie({'name' : 'ko_token', 'value' : 'd78e21f15bf9c445b0793c6a222fee7c'})
        # xenbyfpfUnhLsdkZbX=0; sensorsdata2015jssdkcross={"$device_id":"185945939be225-09f8827020595b-26021151-2073600-185945939bf81e"}; sa_jssdk_2015_appyawovj9f9922_h5_xiaoeknow_com={"distinct_id":"u_lp_1672706463_63b3799f2e99b_GLBLtf","first_id":"185945939be225-09f8827020595b-26021151-2073600-185945939bf81e","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""}}; anony_token=35b6b7fcb586a8dd49fc6ea25a764385; ko_token=d78e21f15bf9c445b0793c6a222fee7c; shop_version_type=4; dataUpJssdkCookie={"wxver":"","net":"","sid":""}; logintime=1676185165

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
                if key in i['params']["response"]['url']:
                    m3u8_url=(i['params']["response"]['url'])
                    self.download(m3u8_url,path,lesson_id)
      
      
    def scroll_to_bottom(self):
        self.cl=[]
        while len(self.driver.find_elements(by=By.CLASS_NAME, value="hint")) == 0:
            js="window.scrollBy(0,10000);"  
            self.driver.execute_script(js)
            
    def get_course_list(self):
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
        self.f=open("D:/PotPlayer/Playlist/"+self.dir_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","")+".dpl","w",encoding="UTF-8")
        self.f.write("DAUMPLAYLIST\ntopindex=0\nsaveplaypos=0\n")
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
            lesson_id=int(lesson_id)
            lesson_id=-1
            self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
            self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
            self.download_name=self.lesson_list[lesson_id]
            time.sleep(self.timeout)
            self.get_network_source()
            self.flei(".m3u8","F:/Desktop/","")
        elif lesson_id == "*":
            for lesson_id in range(0,len(self.lesson_list)):
                self.scroll_to_bottom()
                self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
                self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
                self.download_name=self.lesson_list[lesson_id]
                time.sleep(self.timeout)
                self.get_network_source()
                self.flei(".m3u8","",lesson_id)
                self.driver.back()
        elif lesson_id.find(":"):
            lesson_id=lesson_id.split(":")
            if len(lesson_id) == 2:
                for lesson_id in range(lesson_id[0]-1,lesson_id[1]):
                    self.scroll_to_bottom()
                    self.cl=self.driver.find_elements(by=By.CLASS_NAME, value="content-info")
                    self.driver.execute_script("arguments[0].click();",self.cl[lesson_id])
                    self.download_name=self.lesson_list[lesson_id]
                    time.sleep(self.timeout)
                    self.get_network_source()
                    self.flei(".m3u8","",lesson_id)
                    self.driver.back()            
            else:
                self.choose_lesson()
        else:
            self.choose_lesson()
        self.f.close()

    def download(self,m3u8_url,lpath,lesson_id):
        if lesson_id != "":
            lesson_id=lesson_id+1
            self.f.write(str(lesson_id)+"*file*"+m3u8_url+"\n")
            self.f.write(str(lesson_id)+"*title*"+self.download_name+"\n")
            self.f.flush()
            print(str(lesson_id)+"*file*"+m3u8_url+"\n")
            print(str(lesson_id)+"*title*"+self.download_name+"\n")
        else:
            pass
        
        if lpath!="":
            if path.exists(lpath+"/"+self.dir_name):
                pass
            else:
                mkdir(lpath+"/"+self.dir_name)
            system("ffmpeg -i "+m3u8_url.replace("&","^&")+" -c copy \""+lpath+"/"+self.dir_name+"/"+self.download_name.replace(">"," ").replace("<"," ").replace("|"," ").replace("&","^&").replace(":"," ").replace("?"," ").replace("\"","").replace("*","")+".mp4\"")
        else:
            pass
        
if __name__ == '__main__':
    url='https://appyawovj9f9922.h5.xiaoeknow.com/p/course/big_column/p_62ca351ee4b0c94264785dd8'
    # url='https://appyawovj9f9922.h5.xiaoeknow.com/v2/course/alive/l_63da1b7de4b0fc5d122b3032?type=2&resource_type=4&resource_id=l_63da1b7de4b0fc5d122b3032&app_id=appyawovj9f9922&pro_id=p_63da1b35e4b06159f734886d'
    selenium_driver=selenium_driver(url,2.5)
    selenium_driver.get_course_list()
    selenium_driver.choose_course()
    selenium_driver.get_lesson_list()
    selenium_driver.choose_lesson()
    # selenium_driver.get_network_source()
    # selenium_driver.flei(".m3u8","F:/Desktop/")
    input("下载完成，任意输入退出")