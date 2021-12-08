from nonebot import on_command
from nonebot import rule
from nonebot.adapters import Bot, Event
from nonebot.rule  import command, to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent, event
from nonebot.adapters.cqhttp import GroupUploadNoticeEvent
import os
import re
from threading import Thread
import requests
# robot\cqhttp\data
# send=[CQ:messge,file=312hjkjkdfgh.jpg]
# send=[CQ:image,file=312hjkjkdfgh.jpg]
# send=[CQ:video,file=312hjkjkdfgh.mp4]
# send="[CQ:video,file=file:///F:/python/robot/cqhttp/data/videos/2.mp4]" 发送小视频和图片

def write(url,name):
    command="python f:\python\视频爬虫\optdown.py" +" -u "+url + " -n "+name
    print(command)
    os.system(command)
    path="F:/ts/"+name
    groupid="791054621"
    log=requests.get("http://127.0.0.1:5700/upload_group_file?group_id="+groupid+"&file="+path+"&name="+name)
    print(log.text)
    
down = on_command('down')
@down.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    msg = str(event.get_message())
    do=re.compile("(http.*?)\"")
    url=re.findall(do,msg)[0]
    do=msg.find("-n")
    name=msg[(do+2):].replace(" ","")[0]
    send="收到任务\nurl="+url+"\nname="+name
    # print(event.get_session_id)可查看群号，可能需要正则
    writer=Thread(target=write,args=(url,name))
    writer.start()
    send = Message(send)
    await down.finish(send)