print()
"""
**教學網址: https://www.youtube.com/watch?v=-c5rrzjsN34
**程式功能: pandas直接讀取台銀html .iloc[]讀取欄 .str.extract('\((\w+)\)')萃取英文字
**使用方法: pandas{.read_html(url)/len()/.iloc[]/.columns
"""
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'       #設定要調閱機車資料的網址
path1 = 'D:/0_私人檔案/0_1軟體_下載/Python/.Tools/'   #公司電腦
path2 = 'D:/python-training/.Tool/'                  #私人電腦工具路徑
import pandas

dfs = pandas.read_html(url)
#print(dfs)
print("len= ", len(dfs))
currency = dfs[0].iloc[:, 0:5]
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出']
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
print(currency)

print()