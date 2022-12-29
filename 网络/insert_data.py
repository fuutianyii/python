'''
Author: fuutianyii
Date: 2022-12-29 15:26:18
LastEditors: fuutianyii
LastEditTime: 2022-12-29 17:19:33
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''




# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
from imp import reload
import json
import time
import MySQLdb
    
reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '004f7cff636359e8'
APP_SECRET = 'r14PmJh5FpkxxUNqip3evQadY1j0BGDP'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def api_connect(q):
    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    return response.content


if __name__ == '__main__':
    print(json.dumps(["暂无"]).replace("\\","\\\\"))
    connect=MySQLdb.connect('192.168.1.10','FTY','toor','omelette')
    c=connect.cursor()
    c.execute('''select * from words where US="暂无" or UK="暂无" group by english''')
    no_type_word=c.fetchall()
    for word in no_type_word:
        print(word[1])

        # exam_type=json.loads(api_connect(word[1]))["basic"]['exam_type']
        data=json.loads(api_connect(word[1]))["basic"]
        # us=json.loads(api_connect(word[1]))["basic"]["us-phonetic"]
        # uk=json.loads(api_connect(word[1]))["basic"]["uk-phonetic"]

        if "us-phonetic"  in data.keys():
            us=data["us-phonetic"].replace("'","\\'")
        else:
            if "uk-phonetic"  in data.keys():
                us=data["uk-phonetic"].replace("'","\\'")
            else:
                us="暂无"
        if "uk-phonetic"  in data.keys():
            uk=data["uk-phonetic"].replace("'","\\'")
        else:
            if "us-phonetic"  in data.keys():
                uk=data["us-phonetic"].replace("'","\\'")
            else:
                uk="暂无"
        print(f'''update words set uk='{uk}',us='{us}' where english="'''+word[1]+'''";''')
        c.execute(f'''update words set uk='{uk}',us='{us}' where english="'''+word[1]+'''";''')
        c.execute('''flush privileges;''')
        connect.commit()
    connect.close()
    