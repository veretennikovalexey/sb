# blood

import sqlite3 as sq

sql = """CREATE TABLE IF NOT EXISTS persons (
person_id INTEGER PRIMARY KEY AUTOINCREMENT, 
fname TEXT NOT NULL,
lastname TEXT NOT NULL,
gender INTEGER NOT NULL DEFAULT 1,
age    INTEGER NOT NULL,
salary REAL NOT NULL
)"""

with sq.connect("persons.db") as con:
    cur = con.cursor() # Cursor
    cur.execute(sql)

con.close()