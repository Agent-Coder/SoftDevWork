# Ayham Alnasser && Mandy Zheng (DELETING DB FILES)
# SoftDev1 pd1
# K#18 - Average
# 2019-10-13

import sqlite3   # enable control of an sqlite database
import csv       # facilitate CSV I/O


DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE) # open if file exists, otherwise create
c = db.cursor()               # facilitate db ops

# ==========================================================

while True:  # add as many students as the user wants
    user_input = input("Add a grade? Y/N ")
    if 'y' in user_input.lower():
        user_input = input("Enter the students' course, mark, and id - separated by commas:\n")
        if len(user_input.split(',')) == 3:
            with open("courses.csv", 'a') as o_file:
                o_file.write(user_input + '\n') # new line to move cursor to the next line in file
        else:
            print("Incorrect input; expected 3 arguments")
    else:
        break

# ==========================================================

with open('students.csv') as students:
    reader = csv.DictReader(students) # make a dictionary out of every header in csv
    command = 'CREATE TABLE students ' \
              '( name TEXT, ' \
              'age INTEGER, ' \
              'id  INTEGER' \
              ');'
    c.execute(command)
    for row in reader:
        curr_name, curr_age, curr_id = row['name'], str(row['age']), str(row['id'])
        command = 'INSERT INTO students (name,age,id)' + '\n' + \
                  'VALUES ((' + '\'' + curr_name + '\'' '), ' \
                         '(' + curr_age + '), ' \
                         '(' + curr_id + '));'  # add to sql table
        c.execute(command)

with open('courses.csv') as courses:
    reader = csv.DictReader(courses) # same as both
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
c.execute(command)  # create stu_avg table

command = "SELECT name,mark,students.id FROM courses, students WHERE courses.id=students.id;"
c.execute(command)
rows = c.fetchall()  # create a 2-d array of the outputs
stud_dict = dict()
for row in rows:
    if row[2] in stud_dict.keys():  # catch any repeats if csv is not ordered bc of new inputs
        stud_dict[row[2]].append(row[1])  # append new course grade into preexisting list
    else:
        stud_dict[row[2]] = [row[1]]  # make a list of the first element

for key in stud_dict.keys():
    avg = sum(stud_dict[key]) / len(stud_dict[key])  # finds the average
    command = 'INSERT INTO stu_avg (id, avg) VALUES ((' + str(key) + '),' + '(' + str(avg) + '));'
    c.execute(command)

# ==========================================================

db.commit()  # save changes
db.close()  # close database
