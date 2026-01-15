import sqlite3 as sq

sql = """
SELECT rowid, name, price, stock_quantity
FROM products"""

db = "shop_store.data"

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)
    products = cur.fetchall()

con.close()

# rowid, name, price, stock_quantity