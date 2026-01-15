import sqlite3 as sq

sql = """
SELECT name, price, manufacturer
FROM products
WHERE price < 150"""

db = "shop_store.db"
with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)
    products = cur.fetchall()

con.close()    

