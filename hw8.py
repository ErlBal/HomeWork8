import sqlite3

con = sqlite3.connect('student.db')
cur = con.cursor()
#cur.execute('''DROP TABLE students''')
cur.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    hobby TEXT,
    yearofbirth INTEGER,
    points INTEGER
    ) ''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Alex', 'Washington', 'sport', 2001, 7)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Daryl', 'Dixon', 'gardening', 2000, 11)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Davis', 'Johnson', 'music', 1999, 11)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Dexter', 'McPherson', 'science', 2003, 13)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Felix', 'Cunningham', 'football', 2001, 10)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Gordon', 'Richardson', 'no', 2001, 12)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Homer', 'Simpson', 'no', 2000, 6)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Peter', 'Griffin', 'no', 2002, 8)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Richard', 'Brown', 'karate', 2000, 8)''')
cur.execute('''INSERT INTO students(name, surname, hobby, yearofbirth, points)
 VALUES ('Sean', 'Oslon', 'gaming', 2000, 9)''')
cur.execute('''SELECT * FROM students''')

cur.execute('''UPDATE students SET name = 'genius' WHERE points>=10''')
cur.execute("SELECT rowid, * FROM students")

item = cur.fetchall()

for i in item:
    surname = str(i[3])
    if len(surname) == 10:
        print(surname)
    else:
         ...

cur.execute('''DELETE FROM students WHERE id % 2 = 0''')
cur.execute('''SELECT name FROM students WHERE name = 'genius' ''')

print(cur.fetchall())
con.commit()
con.close()