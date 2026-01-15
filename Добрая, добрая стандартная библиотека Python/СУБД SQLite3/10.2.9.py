import sqlite3 as sq

db = "cars.db"

sql = """CREATE TABLE IF NOT EXISTS cars (
uid INTEGER PRIMARY KEY AUTOINCREMENT, 
model TEXT NOT NULL,
vin TEXT NOT NULL,
year INTEGER NOT NULL DEFAULT 1,
distance INTEGER DEFAULT 0
)"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

con.close()   