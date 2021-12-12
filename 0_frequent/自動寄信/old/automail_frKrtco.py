import smtplib
from datetime import datetime
import sys
sys.path.append('D:/python-training/0_frequent/en_decode') # append path for import dectry
from en_decrypt import dectry

def automail():
    now_ = datetime.today().strftime("%Y/%m/%d %H:%M") # 現今日期/時間
    smtp = smtplib.SMTP('mail.krtco.com.tw', 587) ##
    smtp.ehlo()

    # 登入帳號、密碼
    dec_str = dectry('MjMwXzEzOV8yMjZfMjEzXzEwMl8xNjBfMTcyXzExMV8=') ## 
    smtp.login('hueisam@krtco.com.tw', dec_str) ##
    from_addr = 'hueisam@krtco.com.tw'
    to_addr = 'hueisam57@gmail.com'

    # 寄送郵件內容
    msg = 'Subject: Leon sent by Python scripts\n{} discover abnormal. Please check!'.format(now_)

    # 顯示郵件傳送狀態
    status = smtp.sendmail(from_addr, to_addr, msg)  # 加密文件，避免私密信息被截取
    if status == {}:
        print("郵件傳送成功!"+'\n')
    else:
        print("郵件傳送失敗!"+'\n')
    smtp.quit()

automail()