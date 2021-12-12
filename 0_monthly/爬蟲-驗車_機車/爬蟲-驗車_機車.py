from selenium import webdriver
import pandas as pd
import time
import datetime

path = 'D:/機車驗車月稽/'
url = 'https://www.motorim.org.tw/query/query_check.aspx' #機車排氣定檢 網址
driver = webdriver.Chrome('D:/chromedriver.exe') # 先下載chromedriver.exe放入D槽
df = pd.read_excel(path+'汽機車保管資料.xlsx',sheet_name="機車",header=0)
df['定檢結果'] = '' #新增[Column]
df['領照日期'] = ''
for index,row in df.iterrows():
    carname = df.iat[index,3] #=====>指定3欄(車牌)為key欄
    result1 = [] #檢驗狀態
    result2 = [] #領 牌 日
    driver.get(url)
    driver.maximize_window()
    elem = driver.find_element_by_css_selector("#ctl00_MainContent_txtCarNo") #定位車牌框
    elem.send_keys(carname)
    commit = driver.find_element_by_css_selector('#ctl00_MainContent_btnQuery') #定位查詢鈕
    commit.click()
    elem = driver.find_element_by_css_selector("#ctl00_MainContent_lblTestStatus") #定位檢驗狀態
    result1.append(elem.text) #=====>將結果附加至各車牌檢驗狀態欄
    print(carname, '檢驗狀態 ',result1)
    elem = driver.find_element_by_css_selector("#ctl00_MainContent_lblIssueDt") #定位領牌日
    result2.append(elem.text) #=====>將結果附加至各車牌領牌日欄
    row['定檢結果'] = "".join(result1)
    row['領照日期'] = "".join(result2)
    df.iloc[index] = row #必須重新賦值回去，重要!
driver.close()

Today = datetime.date.today()
filename = '月稽結果 '+str(Today)+'.xlsx'
df.to_excel(path+filename, sheet_name='機車', index = False)

# datetime日期參考: http://www.jsphp.net/python/show-24-213-1.html
# pyinstaller打包: https://blog.typeart.cc/pyinstaller%E5%B8%B8%E7%94%A8%E5%8F%83%E6%95%B8/