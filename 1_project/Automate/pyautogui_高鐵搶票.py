print()
import pyautogui,time
import webbrowser
from PIL import Image

url = 'https://irs.thsrc.com.tw/IMINT'
webbrowser.open(url,new=0)
time.sleep(1)

ride_date = '2021/09/15' #<-----------
myID = 'S120330158'
myPhone = '0972919686'
x=0.25 #休眠時間(秒) <--------------------

# 切割驗證碼圖檔
time.sleep(x)
pyautogui.screenshot('temp1.png')
img = Image.open('temp1.png') #保留圖片
left,top,right,bottom = 506,813,650,866
img = img.crop((left,top,right,bottom))

# 第一頁
pyautogui.click(406,466) #起程站
time.sleep(x)
pyautogui.press('pgdn') #左營
time.sleep(x)
pyautogui.click(526,463) #到達站
time.sleep(x)
pyautogui.press(['pgdn','up','up','up','up','up','up','up','up','up','up','enter']) #台北
pyautogui.press(['tab','tab','tab','tab']) #去程(日期)
time.sleep(x)
pyautogui.typewrite(ride_date,0.1) #輸入搭乘日期
time.sleep(x)
pyautogui.click(536,635) #去程(時間)
time.sleep(x)
pyautogui.press(['pgup','pgup','pgdn']) #13:00 or 13:30
time.sleep(x)
pyautogui.click(1199,967) #轉換至 python terminal輸入定位
time.sleep(x)
captcha = input('請輸入驗證碼 ') # input
#time.sleep(x)
pyautogui.click(700,842) #驗證碼框
pyautogui.moveRel(200,0) #滑鼠右移
pyautogui.typewrite(captcha,0.1) 
time.sleep(x)
pyautogui.click(894,942) #開始查詢
time.sleep(x)

# 第二頁
pyautogui.screenshot('temp2.png') #保留圖片
time.sleep(x)
pyautogui.press('pgdn') 
pyautogui.screenshot('temp3.png') #保留圖片
time.sleep(x)
pyautogui.click(895,669) #確認車次
time.sleep(x)

# 第三頁
pyautogui.screenshot('temp4.png') #保留圖片
time.sleep(x)
pyautogui.click(188,742) #身分證框
time.sleep(x)
pyautogui.typewrite(myID,0.1) #
time.sleep(x)
pyautogui.click(177,832) #行動電話框
time.sleep(x)
pyautogui.typewrite(myPhone,0.1) #
time.sleep(x)
pyautogui.press(['pgdn','pgdn']) 
pyautogui.screenshot('temp5.png') #保留圖片
time.sleep(x)
pyautogui.click(31,403) #個資了解
time.sleep(x)
pyautogui.moveTo(888,577) #完成訂位
time.sleep(x)

img.save('D:/P_高鐵驗證碼/' + captcha + '.png')

print()