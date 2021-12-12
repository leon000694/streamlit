print()
import email.message
import smtplib
import sys
sys.path.append('D:/python-training/0_frequent/en_decode') # path for import dectry
from decrypt import dectry
from datetime import datetime

def automail():
	## 1.訊息物件設定
	now_ = datetime.today().strftime("%Y/%m/%d %H:%M") #格式化日期
	msg = email.message.EmailMessage()
	msg['From'] = 'hueisam1@ms74.hinet.net'
	msg['To'] = 'hueisam57@gmail.com'
	msg['Subject'] = '{} 發生異常!請檢視'.format(now_)

	## 2.信件內容 
	msg.add_alternative('敬啟者:<br>請確認體溫是否已登錄...<br><br>&nbsp&nbsp leon' , subtype='html')

	## 3.連線到 SMTP Server,驗證寄件人身分並發送郵件
	#dec_str = dectry('MjI3XzEzN18yMjNfMjIyXzE1NF8yMjdfMjI2XzE2NF8xNzFfMTczXzE2NF8yMThfMTg3XzE1Ml8yMTFfMTQyXw==')
	try:
		server = smtplib.SMTP('msr.hinet.net', 587)
		server.ehlo() # optional
		server.login('hueisam1@ms74.hinet.net', '')
		server.send_message(msg)
		server.close()
		print('異常信件傳送完成'+'\n')
	except:
		print('Something went wrong'+'\n')


automail()

# 教學 https://yc-note.com/python/python-gmail/
# 影片 https://www.youtube.com/watch?v=YQboCnlOb6Y