print()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from datetime import datetime
import sys
sys.path.append('D:/python-training/0_frequent/en_decode') # path for import dectry
from decrypt import dectry

def automail():
	
	## 1.物件設定
	now_ = datetime.today().strftime("%Y/%m/%d %H:%M") #格式化日期
	content =  MIMEMultipart() # 建立MIMEMultipart物件
	content['subject'] = '{} 發現異常，請檢視!'.format(now_) 
	content['from'] = 'hueisam57@gmail.com'
	content['to'] = 'hueisam57@gmail.com'
	content.attach(MIMEText('Demo python send email')) # 郵件純文字內容


	## ２.連線到 SMTP Server,驗證寄件人身分並發送郵件
	dec_str = dectry('MjI5XzEzOV8yMzRfMjEwXzE3MV8yMTBfMjE3XzE3NV8xNjNfMTY3XzE1NF8yMjJfMTk1XzE0N18yMjBfMTQ5Xw==') # 解密
	with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp: #設定SMTP伺服器 ##
		try:
			smtp.ehlo() # 驗證SMTP伺服器
			smtp.starttls() # 建立加密傳輸安全協定 TLS(Transport Layer Security)
			smtp.login('hueisam57@gmail.com', dec_str) #登入寄件者gmail ##
			smtp.send_message(content) #寄出信件
			print('寄信Complete!'+'\n')
		except Exception as e:
			print('Something went wrong'+'\n', e)

automail()


# 教學 https://yc-note.com/python/python-gmail/
# 影片 https://www.youtube.com/watch?v=YQboCnlOb6Y