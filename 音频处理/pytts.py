'''
Author: fuutianyii
Date: 2023-01-08 16:52:59
LastEditors: fuutianyii
LastEditTime: 2023-01-08 20:59:38
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

import pyttsx3
engine = pyttsx3.init() #创建对象

#这是一个基于本地语音系统的tts，效果仅仅能听
#如果在linux环境中运行，请确保已安装espeak与ffmpeg模块

engine.setProperty('rate',125)
engine.save_to_file('a','test.mp3')
engine.runAndWait()