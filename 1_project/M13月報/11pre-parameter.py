import sys
sys.path.append('D:/python-training/Tool') # for import dectry
from T_email_UseGmail import send_gmail

## 每月10日自動發(含gs試算表網址)信 通知各承辦人填報相關數據
url = 'https://docs.google.com/spreadsheets/d/1VLgx3MrjBtj8KSlO4j4LWN3aignk_ILgKpmnH2vEsD8/edit#gid=0' # 填報表Google Sheet網址

send_gmail(title='請您協助於本月15日前登錄10月份M13相關業務數據。', contents=f'Google雲碟網址: {url}, from M13 Hsu Hui-Sheng.')