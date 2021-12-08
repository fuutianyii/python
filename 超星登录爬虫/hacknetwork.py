import requests
import json
 
host = "http://172.16.1.3"
data={"username":"student02","password":"123456"}
# r = requests.post(url)
r = requests.post(host,data=data)
#response = r.json()
print (r.text)
 