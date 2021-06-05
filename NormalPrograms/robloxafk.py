import pyautogui as p
import time
import random

def keyDownUp(key, t):
    p.keyDown(key)
    time.sleep(t)
    p.keyUp(key)
    #if random.randint(0, 1) == 1:
        #p.press('space')

time.sleep(2)
t = time.time()
i = 1
keyDownUp("z", 5)
time.sleep(2)
t = time.time()
while i > 0:
    #keyDownUp("w", 1)
    #keyDownUp("a", 1)
    #keyDownUp("s", 1)
    #keyDownUp("d", 1)
    #.doubleClick()
    if time.time() - t > 600:
        keyDownUp("z", 5)
        time.sleep(2)
        t = time.time()
    p.keyDown("z")
    p.press("4")
    p.keyUp("z")
    
    
    