print()
from selenium import webdriver
import pyautogui
import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
from constants import compNo

#登入目標網站
url = 'https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay?method=pagination'
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

x = 0.5 #睡覺時間
pyautogui.FAILSAFE=True
browser = webdriver.Chrome('D:/chromedriver.exe')
browser.set_window_size(770,800)
browser.set_window_position(0,0)
browser.get(url) #driver.maximize_window()

browser.implicitly_wait(10) #彈性等待
browser.find_element_by_css_selector("#legal").click()         # 1選法人框
time.sleep(x)
browser.find_element_by_css_selector("#id2").send_keys(compNo) # 送入統編

time.sleep(x)
pyautogui.click(404,363)
time.sleep(x)
pyautogui.press('pgdn') 
time.sleep(x)
pyautogui.click(1452,994) #驗證碼輸入框

# 處理圖片驗證碼
captcha = input('請輸入驗證碼 ') #(暫時)人工input驗證碼(存驗證碼圖檔檔名用)
time.sleep(x)
img_label = browser.find_element_by_css_selector('#pickimg2')
time.sleep(x)  
img_label.screenshot('D:/P_一般驗證碼/'+ captcha +'.png') #暫存驗證碼圖檔
time.sleep(x)
pyautogui.click(390,653) 
time.sleep(x)
pyautogui.typewrite(captcha, 0.2) # 3送入驗證碼
time.sleep(x) 
browser.find_element_by_css_selector("#search2").click() # 4查詢罰單
time.sleep(x)

# 爬取罰單資料 & 轉成excel
browser.get(url)
soup = BeautifulSoup(browser.page_source, features='lxml')
fines = soup.find_all('input', id='paymentSel1')
result = []
for fine in fines:
	post = fine.find('input', id='paymentSel1')
	print(fines.getText())
	result.append(post.getText())

df = pd.DataFrame(result)
print(df)
df.to_excel("penalty.xlsx", index=False)

print()
# 110.09.10  https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/2/