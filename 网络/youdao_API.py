# -*- coding: UTF-8 -*-
import sys
import os
import requests
from requests.exceptions import RequestException
import json
import uuid
import hashlib
import time

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_PATH = os.path.split(CURRENT_PATH)[0]

YOUDAO_API_URL = 'https://openapi.youdao.com/api'
YOUDAO_API_DOC = r'http://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html'


def get_result(word):
    time_curtime = int(time.time())
    app_id = '004f7cff636359e8' # 这里填应用ID
    app_key = 'ivQSM1YCE6SQo1vqhLcaZWO3MDdHinCF' # 这里填应用密钥
    uu_id = uuid.uuid4()
    sign = hashlib.sha256((app_id + word  + str(uu_id) + str(time_curtime) + app_key).encode('utf-8')).hexdigest()   # sign生成
    data = {
        'q':word,
        'from':"en",
        'to':"zh-CHS",
        'appKey':app_id,
        'salt': uu_id,
        'sign':sign,
        'signType':"v3",
        'curtime':time_curtime,
    }

    try:
        r = requests.post(YOUDAO_API_URL, params=data)
        return r.json()
    except RequestException as e:
        print('net error: %s' % e.message)
        sys.exit()


if __name__ == '__main__':
        n = input("input:")
        result = get_result(n)

        if 'basic' in result:
            basic = result['basic']
            explains = basic['explains']
            if len(explains) > 0:
                print('词意：')
                for e in explains:
                    print(e)
                print('')
        
            if 'uk-phonetic' in basic:
                print('英式发音:' + basic['uk-phonetic']) 
            if 'us-phonetic' in basic:
                print('美式发音:' + basic['us-phonetic']) 
            print('')

        if 'web' in result:
            print('网络翻译：')
            for e in result['web']:
                print('{}: {}'.format(e['key'], e['value']))
            print('')