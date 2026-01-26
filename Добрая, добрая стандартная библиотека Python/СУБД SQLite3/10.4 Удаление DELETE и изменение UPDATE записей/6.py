import sqlite3 as sq

db = "students.db"

sql = """
DELETE 
FROM students
WHERE gender = 1
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    sql = """
    SELECT firstname, lastname, birthday
    FROM students
    ORDER BY birthday DESC
    """
    stu = cur.execute(sql).fetchone()

con.close()