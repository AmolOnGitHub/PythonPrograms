import pyautogui
import time

time.sleep(2)
file = open("OtherPrograms/TypingShrek/shrekscript", 'r').read().split(" ")
for word in file:
    time.sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
