import sqlite3 as sq

db = "students.db"

sql = """
DELETE 
FROM students
WHERE gender = 2 AND rowid <= 10
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    sql = """
    SELECT firstname, lastname, birthday
    FROM students
    ORDER BY gender
    """
    res_students = cur.execute(sql).fetchall()

con.close()