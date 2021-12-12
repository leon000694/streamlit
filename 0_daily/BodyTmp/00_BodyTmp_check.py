from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
from T_send_sms_BodyTmp import send_sms
from datetime import datetime
import sys
sys.path.append('D:/python-training/Tool')
from T_email_UseGmail import send_gmail

today = datetime.now().strftime('%m/%d')  #月/日(mm/dd)
#today = '12/08' #手動測試日期非當日時才使用

## 讀取雲碟-當週體溫gs表資料
scope = ['https://www.googleapis.com/auth/spreadsheets'] #google API應用範圍
creds = Credentials.from_service_account_file("D:/python-training/Tool/T_gsheet_Credentials.json", scopes=scope) ##金鑰
gs = gspread.authorize(creds) #驗證

gsheet = gs.open_by_url("https://docs.google.com/spreadsheets/d/1EPKMuFwaJ-P7alttY1fhzBF_6p7QzuznVlLBwlT_ol8/edit#gid=1420864834") #開啟-當週-M13體溫表
worksheet = gsheet.get_worksheet(0)
df_F = pd.DataFrame(worksheet.get_all_records(head=1)) #讀取google sheet Feed資料


## 擷取當日體溫資料 df_add
for i in range(5):
	date = df_F.iat[i,0] #[row,column](列,欄)(高,寬)概念
	if date == today : 
		result = df_F.iloc[i] 
		for j in range(1,12):
			if df_F.iat[i,j] == '' : # [列,*欄]
				# 發送手機簡訊
				name = df_F.columns[j] 
				phone = df_F.iat[7, j] 
				#send_sms(name, phone)  # 發送簡訊給異常者
				print(f'已發送簡訊給{name}\n')

				# 寄送 gmail副知本人
				send_gmail(title='副知 M13資訊',contents=f'{name}今日10:00尚未登錄體溫! \nhttps://docs.google.com/spreadsheets/d/1EPKMuFwaJ-P7alttY1fhzBF_6p7QzuznVlLBwlT_ol8/edit#gid=1420864834')

print('<程式執行完成...> '+'\n' )


# 教學 https://www.learncodewithmike.com/2021/06/pandas-and-google-sheets.html
# Google API Developer Console首頁 https://console.cloud.google.com/apis