print()
"""
*程式功能: 利用sqlite3運作資料庫資料、印出db內容
*教學網址: https://nkust.gitbook.io/python/sqlite-liao-cao-zuo-jie  
*使用方法: sqlite3.connect(*.db).execute("select *欄名from表名;")、 "{}\t".format(*), end=""、 "insert into t(x) v(y);".format(z)、 .commit()存改
"""
path1 = 'D:/0_私人檔案/0_1軟體_下載/Python/.Tools/'  #1.公司電腦工具路徑
path2 = 'D:/python-training/.Tool/'                 #2.私人電腦工具路徑
import sqlite3

dbfile = path2+'sql/contact.db' #<===檔名可以字串相加
conn = sqlite3.connect(dbfile) #<===

""" =====逐欄逐列印出--全部資料庫內容===== """
rows = conn.execute("select * from contact;") #<===
j = 1
for row in rows:
    while j < 4:
        if j > 2:
            for field in row:
                print("{}\t".format(field), end="")
            print()
        break
    j += 1
print()

""" 設定以欄位名稱操作資料庫的標準步驟 """
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("select * from contact;")
rows = cur.fetchall() #=====================================>關鍵變數
print()

i = 1
item = int(input("請輸入要輸出的資料列數: "))
print()
for row in rows:
    start = 4
    while i < start+item:
        if i > start-1:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(row['field2'], row['field3'], row['field6'], row['field5'], row['field8'], row['field9'], row['field11']))
        break
    i += 1

""" ========== 備份 Copy ==========="""
bcku = sqlite3.connect(path2+'sql/backup.db')
with bcku:
    conn.backup(bcku, pages=1) #progress=progress

bcku.close()
conn.close()
print()