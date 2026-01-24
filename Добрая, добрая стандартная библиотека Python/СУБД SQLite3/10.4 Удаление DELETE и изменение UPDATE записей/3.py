import sqlite3 as sq

db = "students.db"

sql = """
UPDATE students
SET group_edu = 'ФПМИ-21'
WHERE lastname = 'Смирнов'
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)

    sql = """
    SELECT firstname, lastname, group_edu, address
    FROM students
    WHERE lastname = 'Смирнов' 
    """
    st_fmti = cur.execute(sql).fetchall()

con.close()


'''
firstname, lastname, group_edu, address
'''