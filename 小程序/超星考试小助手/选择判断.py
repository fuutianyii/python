'''
Author: fuutianyii
Date: 2024-02-16 15:33:04
LastEditors: fuutianyii
LastEditTime: 2024-02-16 18:21:31
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
from cgi import print_directory
import time
import keyboard
import pyautogui
import pyscreeze
import cv2

# Preload click images
next_button = cv2.imread("nextL.png", cv2.IMREAD_GRAYSCALE)
last_button = cv2.imread("lastL.png", cv2.IMREAD_GRAYSCALE)

A = cv2.imread("AL.png", cv2.IMREAD_GRAYSCALE)
B = cv2.imread("BL.png", cv2.IMREAD_GRAYSCALE)
C = cv2.imread("CL.png", cv2.IMREAD_GRAYSCALE)
D = cv2.imread("DL.png", cv2.IMREAD_GRAYSCALE)

# Set screen scale (1 for Windows, 2 for Mac)
screen_scale = 1

def auto_click(target, x, y):
    pyscreeze.screenshot('my_screenshot.png')
    temp = cv2.imread(r'my_screenshot.png', cv2.IMREAD_GRAYSCALE)
    scale_temp = cv2.resize(temp, (temp.shape[1] // screen_scale, temp.shape[0] // screen_scale))

    res = cv2.matchTemplate(scale_temp, target, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    
    if max_val >= 0.9:
        top_left = max_loc
        tag_center_x = top_left[0] + target.shape[1] // 2
        tag_center_y = top_left[1] + target.shape[0] // 2
        pyautogui.click(tag_center_x + x, tag_center_y + y, button='left')
        return tag_center_x, tag_center_y
    else:
        return None

def next():
    auto_click(next_button, 0, 0)
def last():
    auto_click(last_button, 0, 0)
def choose(key):
    if (keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3') or keyboard.is_pressed('4')) and keyboard.is_pressed("down")==0:
        auto_click(key, 0, 0)


keyboard.add_hotkey('right', next)
keyboard.add_hotkey('enter', next)
keyboard.add_hotkey('left', last)

keyboard.add_hotkey('1', choose,args=(A,))
keyboard.add_hotkey('2', choose,args=(B,))
keyboard.add_hotkey('3', choose,args=(C,))
keyboard.add_hotkey('4', choose,args=(D,))
keyboard.wait()