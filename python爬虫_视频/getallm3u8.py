import requests
import re
start=29
end=40

for i in range(start,end+1):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url="https://www.sppmc.com/vplay/17280-1-"+str(i)+".html"
    # print(url)
    data=requests.get(url,headers=header).text
    # print(data)
    rule=re.compile(r"(https://.*?m3u8)")
    m3u8list=re.findall(rule, data)
    print(m3u8list[0])