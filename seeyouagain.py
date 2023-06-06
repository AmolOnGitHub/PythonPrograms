import pyautogui as p
import time
import keyboard

def keyDownUp(key, t):
    p.keyDown(key)
    time.sleep(t)
    p.keyUp(key)


i = 1
time.sleep(2)
print("start")
toggle = True
t = time.time()

while i > 0:
    time.sleep(5)
    if toggle:
        with open('seeyouagain.txt', 'r') as f:
            for l in f:
                for word in l.split():
                    p.typewrite(word, 0.001)
                    keyDownUp("enter", 0.1)
