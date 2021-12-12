print()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
import pyautogui, time
import pandas as pd
from pandas.core.frame import DataFrame
from constants import account1, pword1 

date_start = '20210801' # <=============
date_end   = '20211008' # <=============

start_time = time.time()
url1 = 'https://www.t-cat.com.tw/'
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome('D:/chromedriver', options=option)
driver.get(url1)
driver.set_window_size(760,760)
driver.set_window_position(0,0)

## 1.契約客戶登入頁面
driver.find_element_by_css_selector('#contentContainer > div.idxL > div.green-container > div > img').click() # 彈出視窗--公告點除
driver.find_element_by_xpath('//*[@id="header"]/div[3]/ul/li[2]/a').click() #契客登入
# 登入帳、密、驗證碼
driver.switch_to.window(driver.window_handles[1]) # 定位關鍵1--多窗口--由窗0切至窗1
elem = driver.find_element_by_id('txtUserID') # 定位帳號
elem.send_keys(account1)
elem = driver.find_element_by_id('txtUserPW') # 定位密碼
elem.send_keys(pword1)
time.sleep(6)
pyautogui.click(1400,995)
captcha = input('1_VSC程式區 輸入驗證碼:')
elem = driver.find_element_by_id('txtValidate') # 定位驗證碼
elem.send_keys(captcha)
driver.find_element_by_id('btnSubmit').click() # 點選登入按鈕

## 2.查詢帳務、交易明細
driver.find_element_by_xpath('//*[@id="NavigationMenu"]/ul/li[4]/a').click() #定位帳務
driver.find_element_by_xpath('//*[@id="NavigationMenu:submenu:54"]/li[2]/a').click() #定位明細
iframe = driver.find_element_by_id('ifrmMain') ## 定位關鍵2
driver.switch_to_frame(iframe) ## 元素存在iframe中--要switch_to *****
elem = driver.find_element_by_id('txtDateS') # 定位起始日期
elem.clear()
elem.send_keys(date_start) 
elem = driver.find_element_by_id('txtDateE') # 定位結束日期
elem.clear()
elem.send_keys(date_end)
driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #定位搜尋

## 3.資料抓取、整理
result = []
df_P = pd.DataFrame(columns=['項次','託運單號','運費金額','訂單日期','收件人姓名','收件人地址','附加服務金','付現'])
number = driver.find_element_by_xpath('//*[@id="lblTotleCount"]').text # 取得期間託運件數
print('\n'+'總筆數:', number)
page_num = int((int(number)-1)/10)+2 # 總頁數
for i in range (1, page_num):
	item = 12 # iter次數，從 2開始 末數12不計，共迴圈10次
	if i == page_num-1: 
		item = (int(number) % 10)+2 # 配合網站頁次特性加工計算正確迴圈次數(item值)避免噴錯
	for j in range(2, item):
		order_xpath = '//*[@id="grdList"]/tbody/tr[{}]/td[7]/a'.format(j)
		price_xpath = '//*[@id="grdList"]/tbody/tr[{}]/td[8]'.format(j)
		appach_xpath = '//*[@id="grdList"]/tbody/tr[{}]/td[9]'.format(j)
		cash_xpath = '//*[@id="grdList"]/tbody/tr[{}]/td[10]'.format(j)	

		date_xpath = '//*[@id="TranBillDetail"]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]'
		name_xpath = '//*[@id="TranBillDetail"]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]'
		address_xpath = '//*[@id="TranBillDetail"]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[7]/td[2]'
		try:
			order_num = driver.find_element_by_xpath(order_xpath).text
			price = driver.find_element_by_xpath(price_xpath).text
			appach = driver.find_element_by_xpath(appach_xpath).text
			cash = driver.find_element_by_xpath(cash_xpath).text

			page1_xpath = driver.find_element_by_xpath('//*[@id="grdList"]/tbody/tr[{}]/td[7]/a'.format(j)) #關鍵--定位項次
			page1_xpath.click()  #關鍵--點擊項次(次頁)

			date =  driver.find_element_by_xpath(date_xpath).text
			name = driver.find_element_by_xpath(name_xpath).text 
			address = driver.find_element_by_xpath(address_xpath).text 

			driver.find_element_by_xpath('//*[@id="prePage"]').click()  #關鍵--點擊回主頁
		except:
			print('第',i,'頁 第',j-1,"筆 遇到例外情況，請檢視! 第",(i-1)*10+j-1,'筆','\n')
			break

		k = (i-1)*10+j
		row = [k-1,order_num,price,date,name,address,appach,cash]
		print(row)
		df_P = df_P.append({'項次':k-1,'託運單號':order_num,'運費金額':price,'訂單日期':date,'收件人姓名':name	,'收件人地址':address,'附加服務金':appach,'付現':cash}, ignore_index=True) # 資料字典化並附加到 df_P內

	# (換頁)點擊下一頁運行--取得新頁資料
	if i == page_num-1:
		continue # 如為最後一頁則不運行跳過，否則會噴錯
	elif i >= 11:
		l = (i+1)-(page_num-1-10) #此公式為12頁次以後定址用
		pagex_xpath = driver.find_element_by_xpath("//*[@id='grdList']/tbody/tr[12]/td/a[{}]".format(l)) #關鍵--定位次頁
		pagex_xpath.click()  #關鍵--點擊次頁
		#input('測試2'+'\n')
	else:
		l = i # l代表xpath之定位序號 (i=1~10)
		pagex_xpath = driver.find_element_by_xpath('//*[@id="grdList"]/tbody/tr[12]/td/a[{}]'.format(l)) #關鍵--定位序號
		pagex_xpath.click() #關鍵--點擊次頁
		#input('測試1'+'\n')
	
## 4.產出資料存excel檔
print(df_P, '\n')
df_P.to_excel("D:/Temp/黑貓_O.xlsx", sheet_name=date_start, index = False)

end_time = time.time()
print('運行時間:', int(end_time -  start_time), '秒')
print('ending...'+'\n')
#input('測試'+'\n')