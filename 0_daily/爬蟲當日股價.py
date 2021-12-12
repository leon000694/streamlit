print()
import pandas as pd
import requests
import sqlite3
from datetime import datetime

today = datetime.now().strftime('%Y%m%d') #西元年(yyyymmdd)
chinese_today = f"{(datetime.now().year - 1911)}/{datetime.now().strftime('%m/%d')}" #民國年(yyy/mm/dd)
#today = '20210915' #假日未開市測試用
#chinese_today = '110/09/15'

#資料庫作業1(讀取股票代碼/爬取當日股價)
conn1 = sqlite3.connect('D:/P_Stocks/stocks-no_F.db') #連接資料庫/無則建立
cursor = conn1.cursor()
cursor.execute('SELECT StockNo FROM StockNumbers')
combined = [] #合併結果
for stock_no in cursor.fetchall():
	response = requests.get(f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={today}&stockNo={stock_no[0]}")
	response_data = response.json()['data']
	result = [data for index, data in enumerate(response_data) if chinese_today in response_data[index]]
	#print('response_data', response_data)
	#print('result', result)
	if result: #如果有資料
		result[0].insert(1, stock_no[0]) #插入第2順位
		combined.append(result[0]) #combine多支股票當日股價
		print('combined', combined)
		print()

#資料庫作業2(建立股價新資料庫)
conn2 = sqlite3.connect('D:/P_Stocks/stock-price_O.db') #連接資料庫/無則建立
cursor = conn2.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DayPrice("日期","股票代碼","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數")''') #建立資料表DayPrice
conn2.commit()
df = pd.DataFrame(combined, columns=["日期","股票代碼","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]) #資料來源requests.get()>response>response_data >result>combined
df.to_sql('DayPrice', conn2, if_exists='append', index=False)

print()
# https://www.learncodewithmike.com/2021/08/python-scraper-read-sqlite-database.html
# https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html