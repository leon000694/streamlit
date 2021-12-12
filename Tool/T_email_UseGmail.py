import email.message
import smtplib
import sys
sys.path.append('D:/python-training/0_frequent/en_decode') # for import dectry
from en_decrypt import dectry

def send_gmail(receiver='s0972919686@outlook.com', title='', contents='Letter content'):
	## 訊息物件設定
	msg = email.message.EmailMessage()
	msg['From'] = 'hueisam57@gmail.com'
	msg['To'] = receiver
	msg['Subject'] = title 

	## 連線到 SMTP Server,驗證寄件人身分並發送郵件
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	dec_str = dectry 	('MjI5XzEzOV8yMzRfMjEwXzE3MV8yMTBfMjE3XzE3NV8xNjNfMTY3XzE1NF8yMjJfMTk1XzE0N18yMjBfMTQ5Xw==')
	server.login('hueisam57@gmail.com', dec_str)

	## 寄送多樣化的html內容 
	msg.add_alternative(contents, subtype='html') # 信件主要內容在此
	server.send_message(msg)
	server.close()

	print('已寄信給..', receiver)

#send_gmail()


print()
# 教學 https://yc-note.com/python/python-gmail/
# 影片 https://www.youtube.com/watch?v=YQboCnlOb6Y