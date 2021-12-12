print()
""" 這是測試排程的Python程式 """
import csv

#開放控制次數的CSV檔案
with open('次數.csv', newline='', encoding='utf-8') as f:
    rows=csv.reader(f, delimiter=',')
    for row in rows:
        n = row[0]
        print("上次已執行第",n,"次/頁")   

#執行5次後停止執行
if int(n) < 10:
#執行所需的程式片段(例如爬蟲)
    number_list = []
    for i in range(1,int(n)+1):
        number_list.append(i)
    print(number_list)
    
#執行完將計數寫回CSV檔
    with open('次數.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([str(int(n)+101)[1:]])

print()
# https://www.ptt.cc/bbs/movie/index.html  