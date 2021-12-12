print()
import sqlite3
import datetime

"""
**程式功能: 利用sqlite3運作資料庫
**使用方法: sqlite3.connect(x.db).execute("select *欄名 from score表名;")、 "{}\t".format(x),end=""、 "insert into t(x) v(y);".format(z)、 .commit()存改、 .close()關閉連結
"""

path = '.Tool\sql'
dbfile = '.Tool\sql\school.db'
conn = sqlite3.connect(dbfile)

""" 以下為要顯示資料庫內容時才使用 """
rows = conn.execute("select * from score;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
print()

""" 輸入成績資料並存入資料庫的標準做法 insert a row of data"""
# stuno = input("學    號: ")
# chi = input("國文成績: ")
# eng = input("英文成績: ")
# mat = input("數學成績: ")
# his = input("歷史成績: ")
# geo = input("地理成績: ")
# print()
# sql_str = "insert into score(stuno, chi, eng, mat, his, geo) values('{}',{},{},{},{},{});".format(stuno, chi, eng, mat, his, geo)
# conn.execute(sql_str)
# conn.commit() #save the changes

""" 設定以欄位名稱操作資料庫的標準步驟 """
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("select * from score;")
rows = cur.fetchall()
print("rows[0]= ",rows[0].keys())
print(type(rows))
print(type(rows[0]))
print()

print("學號\t國文\t英文")
for row in rows:
    print("{}\t{}\t{}".format(row['stuno'], row['chi'], row['eng']))
print()

""" =========備份 Copy =========="""
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')
bck = sqlite3.connect(path+'backup.db')
with bck:
    conn.backup(bck, pages=1, progress=progress)
bck.close()
conn.close()

print()
# 教學網址: https://nkust.gitbook.io/python/sqlite-liao-cao-zuo-jie  
# SQL常用指令 https://www.1keydata.com/tw/sql/sqlandor.html