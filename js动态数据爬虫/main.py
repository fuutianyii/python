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
        self.wd = webdriver.Chrome(chrome_options=chrome_options)
        # self.wd = webdriver.Chrome()
        
        
        # self.wd = webdriver.Chrome()
        self.waittime=2

    def __del__(self):#自动销毁
        try:
            self.wd.quit()
        except:
            pass

    def close(self):#关闭
        self.wd.quit()

    def toget(self,url):#获得页面并且等待响应
        self.wd.get(url)
        sleep(self.waittime)

    def togetone(self):#获得当前的详细信息
        self.elements = self.wd.find_element_by_class_name('aplayer-title')
        print("歌曲名："+self.elements.text)
        self.elements = self.wd.find_element_by_id('j-link-btn')
        print("源地址："+self.elements.get_attribute("href"))
        self.elements = self.wd.find_element_by_id('j-src-btn')
        print("下载地址："+self.elements.get_attribute("href"))
        self.elements = self.wd.find_element_by_id('j-lrc-btn')
        print("歌词："+self.elements.get_attribute("href"))

    def togetall(self):#获得所有的缩略信息
        self.elements = self.wd.find_elements_by_class_name('aplayer-list-title')
        self.id= self.wd.find_elements_by_class_name('aplayer-list-index')
        self.author = self.wd.find_elements_by_class_name('aplayer-list-author')
        while (len(self.elements)==0):
            print('sleep')
            self.waittime+=1
            sleep(self.waittime)
            # self.myindex = self.wd.find_elements_by_class_name('aplayer-list-index')
            self.elements = self.wd.find_elements_by_class_name('aplayer-list-title')
            self.id = self.wd.find_elements_by_class_name('aplayer-list-index')
            self.author = self.wd.find_elements_by_class_name('aplayer-list-author')
            print(len(self.author))
        for id in range(0,len(self.elements)):
            print(self.id[id].text+":"+self.elements[id].text+"-"+self.author[id].text)

    def clickli(self):#点击并且获得详细信息
        clicklist=self.wd.find_elements_by_class_name("aplayer-list-index")
        for clickone in clicklist:
            clickone.click()
            sleep(1)
            self.togetone()
    
    
songname=input("曲名：")
print("网易1 QQ2 酷狗3 酷我4")
choose=int(input())
type=["netease","qq","kugou","kuwo"]
url="http://music.9q4.cn/?name="+songname+"&type="+type[choose]
print(url)

weber=Weber()
weber.toget(url)
weber.togetall()
weber.clickli()
# weber.close()