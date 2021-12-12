from selenium import webdriver
import time
from constants import compNo

url ='https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay?method=nopayPagination' #監理網址

driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get(url)
driver.implicitly_wait(10) #隱式等待/彈性等待
driver.maximize_window()
driver.find_element_by_css_selector("#legal").click()         #click法人框
time.sleep(1)
driver.find_element_by_css_selector("#id2").send_keys(compNo) #find統編框 send統編
"""處理圖片驗證碼"""
img_label = driver.find_element_by_css_selector("#pickimg2")
img_label.screenshot(yzm.png)
time.sleep(2)
driver.close()
