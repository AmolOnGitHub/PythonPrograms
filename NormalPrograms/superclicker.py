from threading import Thread
import pyautogui as pt
import time

def fast():
    t = time.time()
    while time.time() - t <= 10:
        pt.doubleClick()

time.sleep(2)
threads = []

pt.PAUSE = 0

for tx in range(3):
    threads.append(Thread(target = fast))

for tx in threads:
    tx.start()

for tx in threads:
    tx.join()
    
print("done")