from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
#pip install selenium
# https://chromedriver.storage.googleapis.com/index.html 驱动下载地址
#down chromedriver.exe对应版本


class Weber:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless') #隐藏窗口
        chrome_options.add_argument('--disable-gpu')  #隐藏窗口
        chrome_options.add_argument("--mute-audio")#静音
        self.wd = webdriver.Chrome(chrome_options=chrome_options)
        # self.wd = webdriver.Chrome()
        self.waittime=2
    def __del__():
        self.wd.quit()

    def close(self):#关闭
        self.wd.quit()

    def toget(self,url):#获得页面并且等待响应
        self.wd.get(url)
        sleep(self.waittime)

    def getmain(self):#获得当前的详细信息
        mainsonglist=[]
        try:
            self.elements = self.wd.find_element_by_class_name("aplayer-pic").get_attribute("style")
            num=self.elements.find("http")
            self.elements=self.elements[num::]
            self.elements=self.elements[:-3]#歌曲图片
            mainsonglist.append(self.elements)
        except:
            mainsonglist.append("nopic.jpg")
        self.elements = self.wd.find_element_by_class_name("aplayer-title")
        mainsonglist.append(self.elements.text)
        self.elements = self.wd.find_element_by_id('j-src-btn')
        mainsonglist.append(self.elements.get_attribute("href"))
        return mainsonglist

    def togetall(self):#获得所有的缩略信息
        
        try:
            sleep(1.5)
            clicklist=self.wd.find_elements_by_class_name("aplayer-more")
            clicklist[0].click()
            sleep(1.5)
        except:
            pass
        self.elements = self.wd.find_elements_by_class_name('aplayer-list-title')
        self.author = self.wd.find_elements_by_class_name('aplayer-list-author')
        while (len(self.elements)==0):
            # print('sleep')
            clicklist=self.wd.find_elements_by_class_name("aplayer-more")
            clicklist[0].click()
            sleep(1.5)
            self.waittime+=1
            sleep(self.waittime)
            # self.myindex = self.wd.find_elements_by_class_name('aplayer-list-index')
            self.elements = self.wd.find_elements_by_class_name('aplayer-list-title')
            self.author = self.wd.find_elements_by_class_name('aplayer-list-author')
            # print(len(self.author))
        infoline=[]
        for id in range(0,len(self.elements)):
            infoline.append(self.elements[id].text)
            infoline.append(self.author[id].text)
        return infoline

    def clickli(self,indexnum):#点击并且获得详细信息
        clicklist=self.wd.find_elements_by_class_name("aplayer-list-index")
        clicklist[indexnum].click()
        return self.getmain()
