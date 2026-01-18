import sqlite3 as sq

db = "shop_store.db"

sql = """
SELECT name, description, price, date
FROM goods
WHERE
    strftime('%Y-%m', date, 'unixepoch') = strftime('%Y-%m', 'now') AND
    price BETWEEN 100 AND 400
"""

with sq.connect(db) as con:
    cur = con.cursor()

    cur.execute(sql)
    products = cur.fetchall()

con.close()    