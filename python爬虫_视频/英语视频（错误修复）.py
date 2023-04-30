# # !/usr/bin/env python3
# # -*- coding: utf-8 -*-
# '''
# Author: fuutianyii
# Date: 2023-04-11 10:17:30
# LastEditors: fuutianyii
# LastEditTime: 2023-04-11 10:36:07
# github: https://github.com/fuutianyii
# mail: fuutianyii@gmail.com
# QQ: 1587873181
# '''
import requests
import base64



header={'authority':'pri-cdn-tx.xiaoeknow.com',
'accept':'*/*',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'no-cache',
'origin':'https://appyawovj9f9922.h5.xiaoeknow.com',
'pragma':'no-cache',
'referer':'https://appyawovj9f9922.h5.xiaoeknow.com/',
'sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
keydata=requests.get("https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=appyawovj9f9922&mid=m_s64Wrnm2m9Vhq_Sdp91xzi&urld=bc1397f2d3f8ee652f18d160d3f1cc8f&uid=u_lp_1672706463_63b3799f2e99b_GLBLtf",headers=header)
key=base64.b64encode(keydata.content)


import requests
import re
from Crypto.Cipher import AES



def get_key_from_url(url: str, userid: str) -> str:
    """
    通过请求m3u8文件中的key的url,获取解密视频key的base64字符串密钥
    :param url: m3u8文件中获取key的url
    :param userid: 用户id，放视频时飘动的那一串
    :return: key的base64字符串
    """
    # url拼接uid参数
    url += f'&uid={userid}'
    # 发送get请求
    rsp = requests.get(url=url)
    rsp_data = rsp.content
    if len(rsp_data) == 16:
        userid_bytes = bytes(userid.encode(encoding='utf-8'))
        result_list = []
        for index in range(0, len(rsp_data)):
            result_list.append(
                rsp_data[index] ^ userid_bytes[index])
        print(result_list)
        return base64.b64encode(bytes(result_list)).decode()
    else:
        print(f"获取异常，请求返回值：{rsp.text}")
        return ''
 
 
if __name__ == '__main__':
    _url = 'https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=appyawovj9f9922&mid=m_whFybc17HdJ0z_fYtm08YK&urld=894e80e0672c5c1bf15010d484868b1f'
    _uid = 'u_lp_1672706463_63b3799f2e99b_GLBLtf'
    base64_key = get_key_from_url(url=_url, userid=_uid)
    print(base64_key)
    f=open(r"F:\进阶提升365必刷\进阶提升365必刷 09 完形02 视频 2022.08.06   78次学习4\raw.m3u8","r")
    url_list=f.read()
    pattern=re.compile("(?<=https://).*(?=)")
    url_list=pattern.findall(url_list)
    for i in range(0,len(url_list)):
        data=requests.get("https://"+url_list[i],headers=header)
        encode=data=data.content
        cryptor = AES.new(base64.b64decode(base64_key.encode()), AES.MODE_CBC, b'0000000000000000')
        while (len(encode)%16!=0):
            encode=encode+b" "
        cont=cryptor.decrypt(encode)
        #以追加的形式保存为mp4文件，mp4可以随意命名，这里命名为小鹅通视频下载测试
        f=open(f"f:/ts/{i}.ts","wb")
        f.write(cont)
        f.close()