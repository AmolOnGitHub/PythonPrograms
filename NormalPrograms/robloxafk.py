import pyautogui as p
import time
import random
import keyboard

def keyDownUp(key, t):
    p.keyDown(key)
    time.sleep(t)
    p.keyUp(key)
    # if random.randint(0, 1) == 1:
    # p.press('space')


i = 1
time.sleep(2)
toggle = False
t = time.time()
while i > 0:
    if keyboard.is_pressed('o'):
        toggle = not toggle
    if toggle:
        #keyDownUp("w", 1)
        keyDownUp("a", 0.5)
        #keyDownUp("s", 1)
        keyDownUp("d", 0.5)
        #p.click()
        #time.sleep(5)
    # if time.time() - t > 600:
    #    keyDownUp("z", 5)
    #    time.sleep(2)
    #    t = time.time()
    # p.keyDown("z")
    # p.press("4")
    # p.keyUp("z")