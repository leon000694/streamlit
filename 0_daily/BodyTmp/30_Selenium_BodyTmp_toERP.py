print()
import sqlite3, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from constants import account1, pword1 
start_time = time.time()

x = 0.5 

"""0_Pandas讀取同仁sql3資料庫內id及當日體溫資料"""
today = datetime.now().strftime('%m/%d') #月/日(mm/dd) #
conn = sqlite3.connect('D:/Python/Per-Daily/BodyTmp_28/BodyTmp28_M13.db') #連接資料庫/無則建立
df_id = pd.read_sql("SELECT * FROM BodyTmp WHERE 日期='id_'", conn) #取出id_ List
df_tp = pd.read_sql(f"SELECT * FROM BodyTmp WHERE 日期 = '{today}'", conn) #取出溫度LList

url1 = 'http://erp.krtc.com.tw/erp/login'
url2 = 'http://erp.krtc.com.tw/erp/hh/a010/index'
browser = webdriver.Chrome('D:/chromedriver')

browser.get(url1)
login1 = browser.find_element_by_id("username") #定位
login1.send_keys(account1)
login2 = browser.find_element_by_id("password") #定位
login2.send_keys(pword1)
login2.send_keys(Keys.ENTER)
time.sleep(3)

for i in range(1,12): # i=欄序
	browser.get(url2)
	time.sleep(2)
	id_ = df_id.iat[0,i] # i for 1 to 11
	tmp = df_tp.iat[0,i]
	print(i, id_, tmp)
	if tmp == '休':
		continue
	if tmp == '':
		continue
	elem1 = browser.find_element_by_xpath("//*[@id='myform']/div[1]/div[2]//input[@type='text']")
	elem1.click() # 受測人員
	elem1.send_keys(str(id_))
	elem12 = browser.find_element_by_css_selector('div.el-scrollbar') 
	elem12.click() # 選受測人員
	time.sleep(x)

	elem2 = browser.find_element_by_xpath("//*[@id='myform']/div[2]/div[1]//input[@type='number']")
	elem2.click() # 測得體溫
	elem2.send_keys(str(tmp))
	time.sleep(x)

	elem3 = browser.find_element_by_xpath("//*[@id='myform']/div[2]/div[2]//option[@value='0']")
	elem3.click() # 身體症狀
	time.sleep(x)

	elem4 = browser.find_element_by_xpath("//*[@id='myform']/div[2]/div[3]//input[@type='text']")
	elem4.click() # 量測時間
	elem4.send_keys(Keys.ENTER)
	time.sleep(x)

	elem5 = browser.find_element_by_xpath("//*[@id='myform']/div[3]//button[@type='button']")
	elem5.click() # 新增紀錄
	time.sleep(x) 

	elem6 = browser.find_element_by_xpath("/html/body/div[10]/div/div[3]/button[2]/span")
	elem6.click() # 確定新增
	time.sleep(1) 
	
end_time = time.time()
print('運行時間:', int(end_time -  start_time), '秒')

	
print('ending...'+'\n')
