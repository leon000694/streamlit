print()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pyautogui
from pyautogui import FAILSAFE
import time
from datetime import datetime

ride_date = '2021/09/16' 
pyautogui.FAILSAFE = False
url = 'https://irs.thsrc.com.tw/IMINT' #高鐵網路訂票網址 https://irs.thsrc.com.tw/IMINT/?locale=tw

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
#options = Options()
#options.add_argument("--disable-notifications")
driver = webdriver.Chrome('D:/chromedriver',options=option) # 
driver.get(url)
driver.maximize_window()
time.sleep(0.5)
pyautogui.click(635,675) #點同意個資

time.sleep(2)
elem2 = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
left = elem2.location['x']
right = elem2.location['x'] + elem2.size['width']
top = elem2.location['y']
bottom = elem2.location['y'] + elem2.size['height']
print('se lenium ',left,right,top,bottom)
driver.save_screenshot('temp2.png')
img2 = Image.open('temp2.png')
img2a = img2.crop((left, top, right, bottom))
img2a.save('captua2.png')

time.sleep(1)
pyautogui.click(875,412) 
time.sleep(0.3)
pyautogui.click(862,686) #點起程(左營)
time.sleep(0.3)
pyautogui.click(1012,416) 
pyautogui.click(1001,480) #點到達(台北)

time.sleep(0.3)
pyautogui.click(825,578) 
pyautogui.dragRel(90,30,0.5, button='left')
elem1 = driver.find_element_by_css_selector('#toTimeInputField')
elem1.send_keys(ride_date) #送出搭乘日期

time.sleep(0.3)
pyautogui.click(993,585) 
time.sleep(0.3)
pyautogui.click(998,1011) #點乘車時間13:00
time.sleep(0.3)
pyautogui.click(1174,793) #點驗證碼框

left,right,top,bottom = 959,1123,763,823
print('pyautogui ',left,right,top,bottom)
pyautogui.screenshot('temp1.png')
img1 = Image.open('temp1.png')
img1a = img1.crop((left,top,right,bottom))
img1a.save('captua1.png')

#time.sleep(100)
#driver.close()

print()
# https://www.youtube.com/watch?v=hF-dJj559ug
# pyautogui.displayMousePosition()