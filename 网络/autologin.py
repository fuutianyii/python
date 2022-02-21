from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from os import system

system("pip install selenium-4.1.0-py3-none-any.whl")
chrome_options = Options()
chrome_options.add_argument('--headless') #隐藏窗口
chrome_options.add_argument('--disable-gpu')  #隐藏窗口
wd = webdriver.Chrome(chrome_options=chrome_options)
# wd = webdriver.Chrome()
wd.get('http://172.21.201.162')
sleep(1)
username=wd.find_element_by_name("username")
username.click()
username.send_keys("test")
sleep(1)
password=wd.find_element_by_name("pwd_tip")
password.click()
password=wd.find_element_by_name("pwd")
password.click()
password.send_keys("123")
sleep(1)
login=wd.find_element_by_id("loginLink_div")
login.click()