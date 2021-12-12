print()
"""
**教學網址: NA
**功能方法: 用webdriver.Chrome控制瀏覽器；引用檔案使用路徑+檔案拼接方式便利公司/家裡電腦路徑能簡易切換；用for複循環；用.iat取得車牌
           selenium(webdriver.chrome/.maximize_window()/.get/.find_element_by_css_selector('')/.send_keys(x)/.click)_
           pandas.DataFrame(x).to_excel('').close_time.sleep_[].append(x)
"""
url = 'https://www.motorim.org.tw/query/query_check.aspx' #設定要調閱機車資料的網址
path1 = 'D:/0_私人檔案/0_1軟體_下載/Python/.Tools/'        #公司電腦
path2 = 'D:/python-training/.Tool/'                       #私人電腦
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(path1+'chromedriver.exe') #====================> 切換電腦路徑(1公司 or 2私人)
time.sleep(1)

df = pd.read_excel(path1+'公務機車.xlsx',sheet_name="機車") #=============> 切換電腦路徑
df['定檢結果'] = ''
df['領照日期'] = ''

for index,row in df.iterrows():
    result1 = []
    result2 = []
    carname = df.iat[index, 2]
    print(index,carname)

    driver.get(url)
    elem1 = driver.find_element_by_css_selector("#ctl00_MainContent_txtCarNo") #輸入車牌號
    elem1.send_keys(carname)
    time.sleep(0.1)
    commit = driver.find_element_by_css_selector('#ctl00_MainContent_btnQuery')  #按鈕查詢
    commit.click() #=========================================================切換至下一網頁
    time.sleep(0.1)
    
    elem1 = driver.find_element_by_css_selector("#ctl00_MainContent_lblTestStatus") #附加檢驗狀態
    result1.append(elem1.text)
    elem2 = driver.find_element_by_css_selector("#ctl00_MainContent_lblIssueDt") #附加領牌日
    result2.append(elem2.text)

    row['定檢結果'] = "".join(result1)
    row['領照日期'] = "".join(result2)
    df.iloc[index] = row #必須重新賦值回去，重要!
    # i = i + 1
    # if i <= 40:
    #     continue
    # else:
    #     break

df.to_excel('temp.xlsx')
driver.close()

print()