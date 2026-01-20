import sqlite3 as sq

db = "shop_store.db"

sql = """
SELECT name, description, price, date
FROM products
WHERE price BETWEEN 100 AND 500 
ORDER BY date DESC
"""

with sq.connect(db) as con:
    cur = con.cursor()

    cur.execute(sql)
    products = cur.fetchall()


con.close()