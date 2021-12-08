from nonebot import on_command
from nonebot import rule
from nonebot.adapters import Bot, Event
from nonebot.rule  import command, to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent, message
from nonebot.adapters.cqhttp import GroupUploadNoticeEvent
import os
import re
respond = on_command("说句话",rule = to_me())
@respond.handle()

async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    # card="1.jpg"
    # gomsg = "[CQ:cardimage,file="+card+"]"#大图
    id=str(event.get_user_id())
    if id=="1642108406":
        gomsg="[CQ:tts,text=凯彦哥哥好厉害！！！]"
    else:
        gomsg="[CQ:tts,text=老铁六六六]"
    gomsg = Message(gomsg)
    await respond.finish(gomsg)