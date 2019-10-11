# Ayham Alnasser && Mandy Zheng(?)
# SoftDev
# skeleton :: SQLITE3 BASICS
# Oct 2019

import sqlite3   # enable control of an sqlite database
import csv       # facilitate CSV I/O


DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE) # open if file exists, otherwise create
c = db.cursor()               # facilitate db ops

# ==========================================================


##POPULATE THE DB IF EMPTY OTHERWISE IGNORE

with open('students.csv') as students:
    reader = csv.DictReader(students)
    command = 'CREATE TABLE students ' \
              '( name TEXT, ' \
              'age INTEGER, ' \
              'id  INTEGER' \
              ');'
    c.execute(command)
    for row in reader:
        curr_name = row['name']
        curr_age = str(row['age'])
        curr_id = str(row['id'])
        command = 'INSERT INTO students (name,age,id)' + '\n' + \
                  'VALUES ((' + '\'' + curr_name + '\'' '), ' \
                         '(' + curr_age + '), ' \
                         '(' + curr_id + '));'
        c.execute(command)

with open('courses.csv') as courses:
    reader = csv.DictReader(courses)
    command = 'CREATE TABLE courses ' \
              '(code TEXT, ' \
              'mark INTEGER, ' \
              'id  INTEGER' \
              ');'
    c.execute(command)
    for row in reader:
        curr_code = row['code']
        curr_mark = str(row['mark'])
        curr_id = str(row['id'])
        command = 'insert into courses (code,mark,id)' + '\n' + \
                  'values ((' + '\'' + curr_code + '\'' '), ' \
                          '(' + curr_mark + '), ' \
                          '(' + curr_id + '));'
        c.execute(command)

# ==========================================================
command = 'CREATE TABLE stu_avg' \
          '( id INTEGER, ' \
          'avg INTEGER ' \
          ');'
c.execute(command)


# ==========================================================
command = "SELECT name,mark,students.id FROM courses, students WHERE courses.id=students.id;"
c.execute(command)
rows = c.fetchall()
print(rows[0][1])
name = rows[0][0]
stud_id = rows[0][2]
avg, name_count = 0, 0
for row in rows:
    if row[0] == name:
        avg += row[1]
        name_count += 1
    else:
        avg /= name_count
        print(name, stud_id, avg)
        command = 'INSERT INTO stu_avg (id, avg) VALUES ((' + str(stud_id) + '),' + '(' + str(avg) + '));'
        c.execute(command)
        name = row[0]
        avg = row[1]
        stud_id = row[2]
        name_count = 1

avg /= name_count
print(name, stud_id, avg)
command = 'INSERT INTO stu_avg (id, avg) VALUES ((' + str(stud_id) + '),' + '(' + str(avg) + '));'
c.execute(command)



# ==========================================================

db.commit()  # save changes
db.close()  # close database
