import sqlite3 as sq
import datetime

db = "students.db"

# Вычисляем количество секунд для 01.01.2006
date_2006 = int(datetime.datetime(2006, 1, 1).timestamp())

sql = """
UPDATE students
SET group_edu = 'Выпускник', address = NULL
WHERE birthday < ?
"""

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql, (date_2006,))
    
    sql = """
    SELECT firstname, lastname, group_edu, email, birthday
    FROM students
    WHERE birthday < ?
    """
    result = cur.execute(sql, (date_2006,)).fetchall()
    
    # Преобразуем секунды в datetime.date
    graduates = []
    for row in result:
        firstname, lastname, group_edu, email, birthday_seconds = row
        birthday_date = datetime.date.fromtimestamp(birthday_seconds)
        graduates.append((firstname, lastname, group_edu, email, birthday_date))

con.close()