import sqlite3 as sq

# менеджер контекста

sql = "SELECT * FROM users LIMIT 4"

with sq.connect("saper.db") as con:  
    cur = con.cursor() # Cursor

    cur.execute(sql)
    # result = cur.fetchall()
    # print(result)
    for result in cur:
        print(result)

con.close()
