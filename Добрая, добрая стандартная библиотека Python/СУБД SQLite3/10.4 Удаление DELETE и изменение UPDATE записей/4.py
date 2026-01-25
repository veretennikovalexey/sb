import sqlite3 as sq

db = "students.db"

sql = """
UPDATE students
SET 
    group_edu = 'ВШПИ-11',
    email = 'msk_' || email
WHERE address LIKE '%Москва%'
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    sql = """
    SELECT firstname, lastname, group_edu, email, address
    FROM students
    WHERE address LIKE '%Москва%'
    """
    students_moscow = cur.execute(sql).fetchmany(2)

con.close()