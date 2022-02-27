import requests
import sys

def autosend_vps():
	url="http://127.0.0.1:8666/send_private_msg"
	myobj = {'user_id':'1587873181', 'message':'来自自动提醒:到时候去续你的vps了!\n请访问:https://hax.co.id/','auto_escape':'true'}
	x = requests.post(url, data = myobj)
	f=open("autosend","a+")
	f.write(x.text+"vps")
	f.close()


def autosend_web():
	url="http://127.0.0.1:8666/send_private_msg"
	myobj = {'user_id':'1587873181', 'message':'来自自动提醒:到时候去续你的web了!\n请访问:https://hax.co.id/','auto_escape':'true'}
	x = requests.post(url, data = myobj)
	f=open("autosend","a+")
	f.write(x.text+"web")
	f.close()


def everyday():
	url="http://127.0.0.1:8666/send_private_msg"
	myobj = {'user_id':'1587873181', 'message':'早上好，pybot运行状况良好！','auto_escape':'true'}
	x = requests.post(url, data = myobj)
	f=open("autosend","a+")
	f.write(x.text+"everyday")
	f.close()

if __name__ == "__main__":
    arg=sys.argv[1]
    if arg == "autosend_vps":
        autosend_vps()
    elif arg == "autosend_web":
        autosend_web()
    elif arg == "everyday":
        everyday()
	