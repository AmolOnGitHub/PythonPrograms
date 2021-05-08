import pyautogui as p
import time
import random

def keyDownUp(key, t):
    p.keyDown(key)
    time.sleep(t)
    p.keyUp(key)
    if random.randint(0, 1) == 1:
        p.press('space')

time.sleep(2)

i = 1
while i > 0:
    keyDownUp("w", 1)
    keyDownUp("a", 1)
    keyDownUp("s", 1)
    keyDownUp("d", 1)
    p.doubleClick()
    
    