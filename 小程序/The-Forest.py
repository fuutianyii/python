from pynput.keyboard import Key, Controller
import os
from pynput import keyboard
from time import sleep
godmod=False
def godmodoff():
    keyboard = Controller()

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('godmode off')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('speedyrun off')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def godmodon():
    keyboard = Controller()

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('godmode on')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('speedyrun on')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def help():
    keyboard = Controller()

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('revivelocalplayer')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def time():
    
    keyboard = Controller()
    
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('lightingtimeofdayoverride noon')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def getall():
    keyboard = Controller()
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 262')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #燃料

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 49')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #药

    
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 112')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #双酱果

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 89')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #零食/巧克力


    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 43')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #照明弹

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 57')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #木棒

    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.5)
    keyboard.type('additem 109')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)#苏打水
    
def smallhack():
    keyboard = Controller()
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.2)
    keyboard.type('additem 83')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #箭
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.2)
    keyboard.type('additem 37')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #酒
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.2)
    keyboard.type('additem 33')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #酒
    sleep(1)
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    sleep(0.2)
    keyboard.type('setstat BatteryCharge 100')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #手电筒电
    sleep(1)
    print('OK')

def everything():#小键盘0
    f=open("The-Forest.txt","r")
    str=f.readlines()
    keyboard = Controller()
    for i in str:
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)
        sleep(0.2)
        keyboard.type(i.replace("\n",""))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(1)

def openhack():
    keyboard = Controller()
    keyboard.type('developermodeon')

def pynexit():
    # keyboard.type('exit')
    os.kill()

def on_press(key):
    try:
#   print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:
#   print('special key {0} pressed'.format(key))
        pass
 
def on_release(key):
    global godmod
    a='{0}'.format(key)
    print(a.replace("\'",''))
    if a.replace("\'",'') == "+":
        print("smallhack")
        smallhack()

    if a.replace("\'",'') == "/":
        print("getall")
        getall()

    if a.replace("\'",'')=="Key.page_up":
        print("openhack")
        openhack()

    if a.replace("\'",'') == "-":
        help()

    if a.replace("\'",'') == "*":
        time()

    if a.replace("\'",'') == "Key.page_down":
        pynexit()

    if a.replace("\'",'') == "<110>":
        if godmod==True:
            godmodoff()
            godmod=False
        elif godmod==False:
            godmodon()
            godmod=True
    if a.replace("\'",'') == "<96>":
        everything()
    
while True:
    with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
        listener.join()

