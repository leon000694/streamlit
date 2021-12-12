print()
import pandas as pd
import sqlite3

df = pd.read_csv('Tool/Billionaire.csv') #讀取csv資料檔案
conn = sqlite3.connect('billionaire.db') #建立資料庫
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Billionaire(Name, NetWorth, Country, Source, Rank, Age, Industry)''') #建立資料表
conn.commit()
df.to_sql('Billionaire', conn, if_exists='append', index=False)

us_df = pd.read_sql("SELECT * FROM BILLIONAIRE WHERE Country='Taiwan'", conn)
print(us_df)

print()
# https://www.learncodewithmike.com/2021/05/pandas-and-sqlite.html