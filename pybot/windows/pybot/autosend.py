import requests
import sys
import time
import requests
import json



def autosend_vps():
    url="http://127.0.0.1:5700/send_private_msg"
    myobj = {'user_id':'1587873181', 'message':'来自自动提醒:到时候去续你的vps了!\n请访问:https://hax.co.id/','auto_escape':'true'}
    x = requests.post(url, data = myobj)


def autosend_web():
    url="http://127.0.0.1:5700/send_private_msg"
    myobj = {'user_id':'1587873181', 'message':'来自自动提醒:到时候去续你的web了!\n请访问:https://hax.co.id/','auto_escape':'true'}
    x = requests.post(url, data = myobj)


def everyday():
    url="http://127.0.0.1:5700/send_private_msg"
    myobj = {'user_id':'1587873181', 'message':'早上好，pybot运行状况良好！','auto_escape':'true'}
    x = requests.post(url, data = myobj)


def the_weather_today():
    data=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=苏州').text
    data = json.loads(data)
    day=data["data"]["forecast"][0]['date']
    weather=data["data"]["forecast"][0]['type']
    air_temperature_max=data["data"]["forecast"][0]['high']
    air_temperature_min=data["data"]["forecast"][0]['low']
    wind_power=data["data"]["forecast"][0]["fengli"]
    wind_direction=data["data"]["forecast"][0]['fengxiang']
    url="http://127.0.0.1:5700/send_private_msg"
    message=f"今天是{day}\n天气{weather}\n最高温度{air_temperature_max}\n最底温度{air_temperature_min}\n风向{wind_direction}\n风力{wind_power}"
    myobj = {'user_id':'1587873181','message':message,'auto_escape':'true'}
    x = requests.post(url, data = myobj)


if __name__ == "__main__":
    last_send=""
    sendtime="8"#运行时间（时）
    while True:
        if ((time.strftime("%H",time.localtime())==sendtime) & (last_send!=time.strftime("%d",time.localtime()))):#满足8点和上次发送时间不等于今天日期
            last_send=time.strftime("%d",time.localtime())
            everyday()
            the_weather_today()
        time.sleep(30)