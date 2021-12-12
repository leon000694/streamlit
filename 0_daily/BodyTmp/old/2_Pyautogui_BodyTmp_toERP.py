print()
"""手動autopygui方式登錄同仁體溫"""
#from tkinter.constants import FLAT
import pyautogui, time
import sqlite3
import pandas as pd
from datetime import datetime

"""0_Pandas讀取同仁資料庫內 id及當日體溫資料"""
conn = sqlite3.connect('D:/Python/Project/BodyTmp_28/BodyTmp28_M13.db') #連接資料庫/無則建立
df_id = pd.read_sql("SELECT * FROM BodyTmp WHERE 日期='id_'", conn)
df_tp = pd.read_sql("SELECT * FROM BodyTmp WHERE 日期 = '09/30'", conn) # <======

x=0.5 # timesleep()時間
#today = datetime.now().strftime('%m/%d') #月/日(mm/dd)
# url1 = 'http://erp.krtc.com.tw/erp/login'
# url2 = 'http://erp.krtc.com.tw/erp/hh/a010/index'

for i in range(1,12):
    id_ = df_id.iat[0,i]
    tmp = df_tp.iat[0,i]
    print(i, id_, tmp)
    if tmp == '休' :
        continue
    pyautogui.click(308, 465) #受測人員框
    pyautogui.typewrite(id_, 0.5)
    pyautogui.click(248, 525) #選定人員
    time.sleep(x)

    # pyautogui.click(185, 556) #量測方式
    # pyautogui.click(185, 516) 
    # time.sleep(x)

    pyautogui.click(214, 650) #測得體溫
    time.sleep(x)
    pyautogui.press('backspace')
    #time.sleep(x)
    pyautogui.press('backspace')
    #time.sleep(x)
    pyautogui.press('backspace')
    #time.sleep(x)   
    pyautogui.press('backspace')
    time.sleep(2)
    pyautogui.typewrite(str(tmp), 0.5)
    time.sleep(x)

    pyautogui.click(212, 743) #身體狀況
    pyautogui.click(198, 473)
    time.sleep(x)

    pyautogui.click(288,837) #量測時間
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(x)

    pyautogui.click(174,914) #新增紀錄
    time.sleep(2)
    pyautogui.click(645,626) #
    time.sleep(x)

    #7pyautogui.press('pgup') #回到起始點


print('<運行結果-----1')
print('<運行結果-----2')
print('<運行結果-----3')
