print()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time 

url = 'https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html'
class Stock:
	def __init__(self, *stock_numbers):
		self.stock_numbers = stock_numbers #打包成元組
	def daily(self, year, month):
		browser = webdriver.Chrome(ChromeDriverManager().install())
		browser.get(url)
		time.sleep(5)

		select_year = Select(browser.find_element_by_name("yy"))
		select_year.select_by_value(year)
		select_month = Select(browser.find_element_by_name("mm"))
		select_month.select_by_value(month)
		
		stockno = browser.find_element_by_name("stockNo")

		result = []
		for stock_number in self.stock_numbers:
			stockno.clear() #清空股票代碼輸入框
			stockno.send_keys(stock_number)
			stockno.submit()
			time.sleep(2)

			soup = BeautifulSoup(browser.page_source, "lxml")
			table = soup.find("table", {"id": "report-table"})
			elements = table.find_all("td", {"class": "dt-head-center dt-body-center"})	
			data = (stock_number,)+tuple(element.getText() for element in elements)
			result.append(data)
			print('\n', result)

stock = Stock('2330', '2454', '2002')
stock.daily("2021", "8")


# https://wreadit.com/@wwwlearncodewithmikecom/post/151826