"""Pd讀寫excel """
print()
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

file = 'Tool\krtc-contact.xlsx'
df = pd.read_excel(file, sheet_name='contact', usecols="B,C,E,F,H,I,K:M")

engine = create_engine('sqlite://', echo=False) 
df.to_sql('contact', engine, if_exists='replace', index=False)

#results = engine.execute("Select * from contact where dept in ('M100','M110','M120','M130')")
results = engine.execute("Select * from contact where dept = 'M130'")

final = pd.DataFrame(results, columns=df.columns)
final.to_excel('output.xlsx', index=False)
print(final)

print()
# https://www.youtube.com/watch?v=71zkSuzkJrw