'''
Author: fuutianyii
Date: 2024-07-13 23:58:28
LastEditors: fuutianyii
LastEditTime: 2024-08-01 16:51:23
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import os
import requests
import time

url='https://www.google.com/'
proxies={
'http':'192.168.1.10:10811',
'https':'192.168.1.10:10811'
}
proxies_local={
'http':'127.0.0.1:10810',
'https':'127.0.0.1:10810'
}
f=open("C:\\proxy_control.log","a+")
while True:
    try:
        if requests.get(url,proxies=proxies,timeout=5).status_code == 200 :
            f.write("正常\n")
            f.flush()
            time.sleep(300)
    except:
        f.write("代理出错，正在配置\n")
        f.flush()
        os.system("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 0 /f >nul 2>nul")
        os.system("reg add \"HKCU\\Software\\Microsoft\\/Windows\\CurrentVersion\\Internet Settings\" /v ProxyServer /d \"\" /f >nul 2>nul")
        os.system("taskkill -IM Whale.exe /f")
        time.sleep(5)
        os.popen("C:/Users/Administrator/Desktop/Whale.exe&")
        f.write("whale启动中...\n")
        f.flush()
        while True:
            data=str(os.popen("reg query \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable").read())
            if data.find("0x1") != -1:
                f.write("whale启动成功\n")
                f.flush()
                time.sleep(5)
                break
            else:
                f.write("等待whale启动\n")
                f.flush()
                time.sleep(1)
        try:
            if requests.get(url,proxies=proxies_local,timeout=5).status_code == 200 :
                f.write("代理启动成功\n")
                f.flush()
                os.system("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 0 /f >nul 2>nul")
                os.system("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyServer /d \"\" /f >nul 2>nul")
                f.write("关闭系统代理\n")
                f.flush()
                os.system("net stop frpc")
                os.system("net start frpc")
                f.write("重启frpc成功\n")
                f.flush()
        except requests.exceptions.ProxyError:
                f.write("本地代理错误\n")
                f.flush()
        except:
                f.write("本地代理错误\n")
                f.flush()
            
    