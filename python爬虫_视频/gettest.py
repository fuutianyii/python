import requests
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
s=requests.get("https://baidu.com",headers=header)
# s=requests.get("https://baidu.com")
print(s.text)