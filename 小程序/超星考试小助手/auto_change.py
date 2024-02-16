'''
Author: fuutianyii
Date: 2024-02-13 17:58:54
LastEditors: fuutianyii
LastEditTime: 2024-02-13 22:10:43
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import time
import keyboard
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import pyscreeze
import cv2


# # 设置点击位置
# position1 = (1010,617)
# position2 = (444, 500)
# position3 = (864,617)
def auto_click(click_img,x,y):
    # 屏幕缩放系数 mac缩放是2 windows一般是1
    screenScale=1

    #事先读取按钮截图
    target= cv2.imread(click_img,cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot=pyscreeze.screenshot('my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    # print("目标图宽高："+str(twidth)+"-"+str(theight))
    # print("模板图宽高："+str(tempwidth)+"-"+str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    # print("缩放后模板图宽高："+str(stempwidth)+"-"+str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val>=0.9):
        # 计算出中心点
        top_left = max_loc
        tagHalfW=int(twidth/2)
        tagHalfH=int(theight/2)
        tagCenterX=top_left[0]+tagHalfW
        tagCenterY=top_left[1]+tagHalfH
        #左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX+x,tagCenterY+y,button='left')
        return tagCenterX,tagCenterY
    else:
        return None

# 监听键盘事件
def listen_keyboard():
    print("开始监听")
    while True:
        # 检测按键事件
        if (keyboard.is_pressed('ctrl') and keyboard.is_pressed('enter')) or (keyboard.is_pressed('ctrl') and keyboard.is_pressed('right')):
            coordinate=auto_click("next.png",0,0)
            if coordinate!=None:
                time.sleep(0.8)
                pyautogui.click(coordinate[0],coordinate[1]-120,button='left')
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('left'):
            coordinate=auto_click("last.png",0,0)
            if coordinate!=None:
                time.sleep(0.8)
                pyautogui.click(coordinate[0],coordinate[1]-120,button='left')

# 启动监听
listen_keyboard()