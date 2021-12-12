print()
from google.oauth2.service_account import Credentials
import gspread
import sqlite3
import pandas as pd
from datetime import datetime

#today = datetime.now().strftime('%m/%d') #月/日(mm/dd)
today = '11/05'

# google API應用範圍及驗證
scope = ['https://www.googleapis.com/auth/spreadsheets'] 
creds = Credentials.from_service_account_file("D:/Tool/m13-tmp.json", scopes=scope) #金鑰
gs = gspread.authorize(creds) #驗證

"""擷取當日體溫資料"""
gsheet1 = gs.open_by_url("https://docs.google.com/spreadsheets/d/1EPKMuFwaJ-P7alttY1fhzBF_6p7QzuznVlLBwlT_ol8/edit#gid=1420864834") #開啟-當期M13體溫表
worksheet1 = gsheet1.get_worksheet(0)
df_F = pd.DataFrame(worksheet1.get_all_records(head=1)) #讀取google sheet Feed資料
combined = [] #合併結果
for i in range(5):
	date1 = df_F.iat[i,0] 
	if date1 == today :
		result = df_F.iloc[i] #result為當日體溫資料數列
		combined.append(result) #combined為當日體溫資料
df_add = pd.DataFrame(combined) 
print(df_add)
input()

"""2_將當日體溫資料append累存至28天GoogleSheet體溫表"""
gsheet2 = gs.open_by_url('https://docs.google.com/spreadsheets/d/1eyRO8IKWcZfIv8cf1CR-g6MMhRRRDzJdCjHPXv4rGMI/edit#gid=0') #開啟累存GoogleSheet體溫表
worksheet2 = gsheet2.get_worksheet(0) #擷取第一個工作表 worksheet(0)
worksheet2.append_rows(df_add.values.tolist()) #將當日體溫資料附加

"""3_將當日體溫資料append累存至28天db體溫表"""
conn = sqlite3.connect('D:/P_Body_TMP/BodyTmp-M13.db') #連接資料庫/無則建立
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS BodyTmp("日期","瑞陽","煇昇","建甫","久慧","鴻茂","瓅文","英斌","聖育","昆諺","曉初","信德")''') 
conn.commit()
df_add.to_sql('BodyTmp', conn, if_exists='append', index=False) #將df_add資料累存db檔


# https://www.learncodewithmike.com/2021/06/pandas-and-google-sheets.html
# Google API Developer Console首頁 https://console.cloud.google.com/apis
print('<程式執行完成...> '+'\n', )