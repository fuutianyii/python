import requests
req = requests.session()
url = "http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fi.mooc.chaoxing.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}
 
code = req.get("http://passport2.chaoxing.com/num/code?1620652495719", headers=headers)
with open('f:/Desktop/code.jpg', 'wb') as file:
    file.write(code.content)
    file.close
cap = int(input("验证码："))
data = {
'uname':'15050102729',
'password':'fty040529',
'numcode':cap
}
requests.packages.urllib3.disable_warnings()
login = req.post(url, headers=headers, params=data)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}
rs=req.get('https://mooc1-1.chaoxing.com/work/getAllWork?classId=37965715&courseId=216934629&isdisplaytable=2&mooc=1&ut=s&enc=d7c5f893a5a38faa1755d14d3c86aaf6&cpi=107113437&openc=b88af41e45929e48f01f5a09b3c0d372',headers=headers)
#目录页
rs=req.get('https://mooc1-1.chaoxing.com/work/selectWorkQuestionYiPiYue?courseId=216934629&classId=37965715&workId=13895603&workAnswerId=50373780&isdisplaytable=2&mooc=1&ut=s&evaluation=0&enc=278ff31d4f9fafd1ad842e76525898bf&workSystem=0&cpi=107113437',headers=headers)
#题目
print(rs.text)