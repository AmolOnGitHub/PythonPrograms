from threading import Thread
import pyautogui as pt
import time


TIME = 2
THREADNO = 3

def fast():
    t = time.time()
    while time.time() - t <= TIME:
        pt.doubleClick()

time.sleep(2)
threads = []

pt.PAUSE = 0

for tx in range(THREADNO):
    threads.append(Thread(target = fast))

for tx in threads:
    tx.start()

for tx in threads:
    tx.join()
    
print("done")