print()
import requests
import requests.cookies
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import pyautogui,time

options = Options()
options.add_argument("--disable-notifications") #取消所有的alert彈出視窗

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://rent.591.com.tw/")

area = driver.find_element_by_id("area-box-close")
area.click() #取消<選擇縣市>的div視窗

for page in range(1,3):
	soup = BeautifulSoup(driver.page_source, "html.parser")
	elements = soup.find_all("li", {"class":"pull-left infoContent"})
	print(f"==========第{str(page)}頁==========")
	for element in elements:
		title = element.find("h3").find("a").getText().strip() #取li下h3，再取h3下的a並去空白
		print(title)
	page_next = driver.find_element_by_class_name("pageNext") #分頁
	page_next.click() #點擊一下按鈕
	input()

driver.close()

# print('<局部運行結果>\n',  end='') #=====
# print()
# https://www.learncodewithmike.com/2020/06/how-to-scrape-different-pages-using-python-scraper.html