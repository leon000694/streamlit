print()
import pyautogui
from pyautogui import FAILSAFE
import webbrowser 
import time
from PIL import Image

ride_date = '2021/9/16'
myID = 'S120330158'
myPhone = '0972919686'

pyautogui.FAILSAFE = False
chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'    
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  
url = 'https://irs.thsrc.com.tw/IMINT'
webbrowser.get('chrome').open(url,new=0)

#pyautogui.displayMousePosition()
t=2 # time.sleep時間
for i in range(3):
	time.sleep(t)
	pyautogui.click(870,465)

""" 第一頁 """
time.sleep(2)
pyautogui.click(870,465)
time.sleep(2)
pyautogui.click(870,738) #點-起程(左營)
time.sleep(2)
pyautogui.click(1000,465) 
time.sleep(2)
pyautogui.click(1000,520) #點-到達(台北)

pyautogui.click(826,636) 
pyautogui.dragRel(84,0,0.5, button='left') #選取日期框
pyautogui.typewrite(ride_date)

pyautogui.click(1003,635) 
pyautogui.click(997,613) #點-乘車時間13:30
pyautogui.click(1150,836)#點-驗證碼框
pyautogui.moveRel(200,0)  #相對位置移動
time.sleep(10)    #此時間用於輸入驗證碼
# 待設計驗證碼辨識程式=>再直接 pyautogui.typerwrite('驗證碼')
pyautogui.click(1350,933) #點-開始查詢

""" 第二頁 """
time.sleep(0.25)
pyautogui.click(1910,883) #點-右下捲軸
pyautogui.click(1354,620) #點-確認車次

""" 第三頁 """
time.sleep(0.25) 
pyautogui.click(641,725) # myID
pyautogui.typewrite(myID)
pyautogui.click(638,821) # myPhone
pyautogui.typewrite(myPhone)
pyautogui.click(1910,883) # 點右下捲
pyautogui.click(493,539) # 同意個資
pyautogui.moveTo(1345,715) # 完成訂票

time.sleep(0.5)
pyautogui.screenshot('temp.png')
left,top,right,bottom = 967,811,1112,866
img = Image.open('temp.png')
img = img.crop((left,top,right,bottom))
img.save('captua.png')

print()
# https://www.youtube.com/watch?v=hF-dJj559ug
# print("座標 ",pyautogui.position())
# 