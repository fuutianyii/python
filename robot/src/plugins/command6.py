from nonebot import on_command
from nonebot import rule
from nonebot.adapters import Bot, Event
from nonebot.rule  import command, to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent, message
from nonebot.adapters.cqhttp import GroupUploadNoticeEvent
import os
import re


respond = on_command("",rule = to_me())
@respond.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    url = str(event.get_message())
    print()
    card='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><picture cover="'+url+'"/>'
    gomsg="[CQ:xml,data="+card+"]"
    gomsg = Message(gomsg)
    await respond.finish(gomsg)
