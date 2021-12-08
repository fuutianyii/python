from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule  import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

test = on_command('print',rule = to_me())

@test.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    msg = str(event.get_message())
    msg = Message(msg)
    await test.finish(msg)
    



