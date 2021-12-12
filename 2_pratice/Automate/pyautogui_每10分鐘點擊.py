print()
import pyautogui,time

print(time.strftime("%Y-%m-%d %H:%M:%S %p", time.localtime()))
print('開始計時','\n')
for i in range(100):
    for j in range(10):
        time.sleep(60)
        k = i*10 + j
        print(k,'minutes',end='')
        print('\b'*10,end='',flush=True)
    pyautogui.click(1408,1053) #螢幕下方空白處

print()