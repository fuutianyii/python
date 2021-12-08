import re
import requests
for i in range(18,37):
    print(i)
    urldata=requests.get("http://www.818221.com/bf/5859-1-"+str(i)+".html")
    urldata=urldata.text
    rule=re.compile("(http.*?m3u8)")
    m3u8=re.findall(rule, urldata)[0]
    f=open("m3u8.txt","a+")
    f.write(m3u8+"\n")
    print(m3u8)