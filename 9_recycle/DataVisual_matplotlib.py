print()
from google.oauth2.service_account import Credentials
import gspread
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## 讀取GS表資料
scope = ['https://www.googleapis.com/auth/spreadsheets'] # google API應用範圍
creds = Credentials.from_service_account_file("D:/python-training/Tool/T_gsheet_Credentials.json", scopes=scope) #金鑰
gs = gspread.authorize(creds) #驗證
gsheet = gs.open_by_url("https://docs.google.com/spreadsheets/d/1LJEUYcjOayfaKn1hiRbKRR3lPpj9unS1NvvPI2lcQZw/edit#gid=339883143") # M13重要業務參數表(gs)
worksheet = gsheet.get_worksheet(0)
df_F = pd.DataFrame(worksheet.get_all_records(head=1)) # 讀取google sheet Feed資料
df = df_F.iloc[:, lambda df_F:[0,1,2,3,4,5,6,7,8,9,10]] # .iloc[列, lambda df:[欄]]
#print(df)

df['date'] = df['date'].astype('datetime64[ns]')

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(
	nrows=7, ncols=1, sharex=True, figsize=(7.5,5)) #(寬,高)
fig.tight_layout(pad=1)

ax1.plot(df['date'], df['telecom'],color='r')
ax2.plot(df['date'], df['network'],color='r')
ax3.plot(df['date'], df['fuel'],color='orange')
ax4.plot(df['date'], df['electricity'],color='c')
ax5.plot(df['date'], df['waterpower'],color='c')
ax6.plot(df['date'], df['KRTC-send'],color='limegreen')
ax6.plot(df['date'], df['KRTC-receive'],color='b')
ax7.plot(df['date'], df['TITC-send'],color='limegreen')
ax7.plot(df['date'], df['TITC-receive'],color='b')

ax1.set_ylabel('telecom', fontsize=8)
ax2.set_ylabel('network', fontsize=8)
ax3.set_ylabel('fuel', fontsize=8)
ax4.set_ylabel('electricity', fontsize=8)
ax5.set_ylabel('waterpower', fontsize=8)
ax6.set_ylabel('KRTC', fontsize=8)
ax7.set_ylabel('TITC', fontsize=8)

plt.show()
fig.savefig('plot.png',dpi=300,format='png')
print()