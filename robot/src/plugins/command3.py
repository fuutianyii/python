from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule  import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent, message
import time
test = on_command('时间',rule = to_me())
@test.handle()

async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    id =  str(event.get_user_id())
    # at_ = "[CQ:at,qq={}]".format(id) 
    msg = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    msg = Message(msg)
    test.finish(msg)
    await test.finish(msg)



