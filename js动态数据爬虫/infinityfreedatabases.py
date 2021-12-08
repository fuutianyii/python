from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
chrome_options = Options()
chrome_options.add_argument('--headless') #隐藏窗口
chrome_options.add_argument('--disable-gpu')  #隐藏窗口
wd = webdriver.Chrome(chrome_options=chrome_options)
wd.get("http://fuutianyii.great-site.net/api/login.php?username=guest")
time.sleep(2)
password=wd.find_element_by_class_name('password')
print(password.text)