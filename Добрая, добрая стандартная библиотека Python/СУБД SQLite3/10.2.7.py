import sqlite3 as sq

db = "students.sqlite"

sql = '''
DROP TABLE IF EXISTS students
'''

with sq.connect(db) as con:
    cur = con.cursor()
    cur.execute(sql)
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    st_group TEXT,
    scholarship INTEGER,
    year INTEGER                                       
    ) """)

con.close()    


#    cur.execute("DROP TABLE IF EXISTS users")

'''
name - имя студента (строка);
st_group - группа студента (строка);
scholarship - размер стипендии (целое число);
year - год поступления (целое число).
'''