from nonebot.adapters.onebot.v11 import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from random import randint
emoji = on_keyword({'随机表情'})
@emoji.handle()
async def send_emoji(bot: Bot, event: Event, state: T_State):
    emoji_msg = "[CQ:face,id="+str(randint(0,247))+"]"
    await emoji.send(Message(emoji_msg))