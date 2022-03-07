from nonebot.adapters.onebot.v11 import Message
from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import random
import hashlib
import json


emoji = on_startswith({"翻译","tr"})
@emoji.handle()
async def send_emoji(bot: Bot, event: Event, state: T_State):
    words=event.get_message()
    q=str(words)[3:]
    print(words)
    print(q)
    appKey = '004f7cff636359e8'
    secretKey = 'ivQSM1YCE6SQo1vqhLcaZWO3MDdHinCF'
    httpClient = None
    myurl = '/api'
    fromLang = 'auto'
    toLang = 'auto'
    salt = random.randint(1, 65536)
    sign = appKey+q+str(salt)+secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    data={'appKey': appKey, 'q': q, 'from': fromLang, 'to': toLang, 'salt': str(salt), 'sign': sign}
    d=requests.post("https://openapi.youdao.com/api",data=data)
    returntext=q
    json_data=json.loads(d.text)
    # print(json_data)
    tanslation_results=""
    for means in json_data["translation"]:
        tanslation_results+=means+","
    returntext+="\n翻译："+tanslation_results
    try:
        json_data["web"]
        returntext+="\n\n网络释义\n"
        for word_formations in range(0,len(json_data["web"])):
            word_formation=json_data["web"][word_formations]["key"]
            returntext+=word_formation+":\n"
            word_formation_means=""
            for means in json_data["web"][word_formations]["value"]:
                word_formation_means+=means+"\n"
            returntext+=word_formation_means
    except:
        pass
    returntext+="\n词典：\n"
    dictreturns=""
    for dictreturn in json_data["basic"]["explains"]:
        dictreturns+=dictreturn+"\n"
    returntext+=dictreturns
    print(returntext)
    await emoji.finish(returntext)
