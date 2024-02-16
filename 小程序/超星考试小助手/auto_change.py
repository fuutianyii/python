from cgi import print_directory
import time
import keyboard
import pyautogui
import pyscreeze
import cv2

# Preload click images
next_button = cv2.imread("next.png", cv2.IMREAD_GRAYSCALE)
last_button = cv2.imread("last.png", cv2.IMREAD_GRAYSCALE)

# Set screen scale (1 for Windows, 2 for Mac)
screen_scale = 1

def auto_click(target, x, y):
    screenshot = pyscreeze.screenshot('my_screenshot.png')
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
    print("next")
    coordinate = auto_click(next_button, 0, 0)
    if coordinate:
        time.sleep(0.8)
        pyautogui.click(coordinate[0], coordinate[1] - 120, button='left')
def last():
    print("last")
    coordinate = auto_click(last_button, 0, 0)
    if coordinate:
        time.sleep(0.8)
        pyautogui.click(coordinate[0], coordinate[1] - 120, button='left')

keyboard.add_hotkey('ctrl+enter', next)
keyboard.add_hotkey('ctrl+right', next)
keyboard.add_hotkey('ctrl+left', last)
keyboard.wait()