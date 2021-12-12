print()
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd

## 範圍及驗證
scope = ['https://www.googleapis.com/auth/spreadsheets'] #定義存取的範圍
creds = Credentials.from_service_account_file("D:/python-training/3_Tool/gs_credentials.json", scopes=scope) #憑證檔、範圍傳入creds
gs = gspread.authorize(creds) #憑證傳入gspread

df = pd.read_csv('D:/python-training/3_Tool/temp.csv') #Feed資料
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1JxmidvNfBwjuTOqfd4Ih1xTPOFRTj0Gnm5ZoQIJrCgY/edit#gid=0') #體溫表
worksheet = sheet.get_worksheet(0) #get first worksheet
worksheet.update([df.columns.values.tolist()] + df.values.tolist()) #寫入 
new_df = pd.DataFrame(worksheet.get_all_records()) 
print(new_df)


print()
# https://www.learncodewithmike.com/2021/06/pandas-and-google-sheets.html