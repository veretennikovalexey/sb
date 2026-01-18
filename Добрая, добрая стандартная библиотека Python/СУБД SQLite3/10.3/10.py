import sqlite3 as sq

sql = """
SELECT rowid, name, price, stock_quantity
FROM products
WHERE price >= 400 OR stock_quantity <= 50
"""

db = "shop_store.db"

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)
    products = cur.fetchall()

con.close