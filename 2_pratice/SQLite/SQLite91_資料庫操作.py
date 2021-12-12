print()
import sqlite3

conn = sqlite3.connect('D:\python-training\SQLite\school.db')
rows = conn.execute("select * from score;")
for row in rows:
    for field in row:
        print('{}\t'.format(field), end='')
    print()
conn.close()

print()
# 教學網址: https://nkust.gitbook.io/python/sqlite-liao-cao-zuo-jie