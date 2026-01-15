import sqlite3 as sq

data_customers = [
    ('Александр', 'Репин', 'adfgd@mail.ru', 1766315439, False),
    ('Дмитрий', 'Павлов', 'dpavdfd@list.ru', 1766271986, True),
]

db = "customers.db"

sql = """CREATE TABLE IF NOT EXISTS customers (
fname TEXT,
lastname TEXT,
email TEXT NOT NULL,
created_at INTEGER NOT NULL,
is_active INTEGER DEFAULT 0
)"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    cur.executemany(
        "INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
        data_customers        
    )

con.close()


