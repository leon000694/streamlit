print()
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# create stores table
command1 = """CREATE TABLE IF NOT EXISTS 
contacts (date text, name text, number INTEGER PRIMARY KEY)"""
c.execute(command1)

#c.execute("INSERT INTO contacts VALUES ('2018-03-11','王小寶','222')")
c.execute("INSERT INTO contacts VALUES ('2018-03-12','吳有明','321')")

c.execute("DELETE FROM contacts WHERE number = 222")

for row in c.execute('SELECT * FROM contacts ORDER BY number'):
	print(row)

conn.commit()
conn.close()

print()
# https://www.youtube.com/watch?v=r5hukuRVKGA