url = 'https://facebook.com' # 設定要前往的網址
spec_url = 'https://www.facebook.com/moea.gov.tw' # 切換畫面
username = 'hueisam1@ms74.hinet.net'
password = 'leOn0278'
# 教學網站  https://aitmr1234567890.medium.com/fb-%E7%88%AC%E8%9F%B2%E5%8F%AF%E4%BB%A5%E6%9B%B4%
# E7%B0%A1%E5%96%AE-%E7%94%A8selenium%E8%87%AA%E5%8B%95%E7%99%BB%E5%85%A5fb-%E7%B3%BB%E5%88%971-
# %E9%99%84python%E7%A8%8B%E5%BC%8F%E7%A2%BC-82570c79a824

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
from pandas.core.frame import DataFrame
import time 
import pandas as pd

# 關閉通知
# options = webdriver.ChromeOptions()
# prefs = {
#     'profile.default_content_setting_values':
#         {
#             'notifications':2
#         }
# }
# options.add_experimental_option('prefs', prefs)
# options.add_argument("disable-infobars")

# -----透過Browser Driver 開啟 Chrome -----
driver = webdriver.Chrome('D:/python-training/.Tool/chromedriver')  
driver.maximize_window() # 最大化窗口
driver.get(url)  #----- 前往該網址 -----

# ----- 輸入帳號密碼 -----
# time.Sleep(1)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element_by_id("email")
elem.send_keys(username)

elem = driver.find_element_by_id("pass")
elem.send_keys(password)

elem.send_keys(Keys.RETURN)
time.sleep(3)

# 檢查有沒有被擋下來 
if len(driver.find_elements_by_xpath("//*[contains(text(), '你的帳號暫時被鎖住')]")) > 0:
    driver.find_elements_by_xpath("//*[contains(text(), '是')]")[1].click()

#driver.get(spec_url) # 切換畫面

print()
