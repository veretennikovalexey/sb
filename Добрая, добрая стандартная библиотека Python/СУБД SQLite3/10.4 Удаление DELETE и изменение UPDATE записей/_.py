import sqlite3 as sq

db = "s"

sql = """
s
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    sql = """
    s
    """
    result = cur.execute(sql).fetchall()

con.close()