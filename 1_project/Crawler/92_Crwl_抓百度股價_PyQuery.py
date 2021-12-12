print()
import requests
from pyquery import PyQuery

url = "https://cn.investing.com/equities/baidu.com"
heads = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
response = requests.get(url,headers = heads)
doc = PyQuery(response.text)
#print('1',doc)
price = doc("#last_last").text()
#print('2',price)
spans = doc("#quotes_summary_current_data .inlineblock div span").items()
#print('3',spans)
i = 0
for span in spans:
    i += 1
    if i == 2:
        priceDelta = span.text()
    elif i == 4:
        priceDeltaRatio = span.text()

print("今日股價:{0},漲跌:{1},涨福{2}".format(price, priceDelta, priceDeltaRatio))
print()

# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx 
# JSON型態: https://medium.com   https://cn.investing.com/equities/baidu.com  