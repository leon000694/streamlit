print()
import pyautogui
from pyautogui import FAILSAFE
import time

# time.sleep(1.5)
# print(pyautogui.position())

pyautogui.FAILSAFE = False
print(time.strftime("%Y-%m-%d %H:%M:%S %p", time.localtime()))
acc_time = 0
sleep_time = 300 # <===
for i in range(100):
    pyautogui.click(62,17)
    pyautogui.click(29,136)

    for j in (range(3)):
        time.sleep(sleep_time) 
        pyautogui.click(1063,1063)
        acc_time += (sleep_time/3600)
        print(time.strftime("%H:%M", time.localtime())," ", round(acc_time,1))

print()