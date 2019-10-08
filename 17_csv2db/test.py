#Amanda Zheng and Michael Zhang
#SoftDev pd1
#k :: SQLITE3 BASICS
#Oct 7 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="test.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

command = "CREATE TABLE Students (name TEXT, age INTEGER, id INTEGER);" # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)
with open('students.csv') as student:
     reader = csv.DictReader(student)
     for row in reader:
         command = "insert into Students (name, age, id) values ('" + row['name'] + "', " + str(row['age']) + ", " + str(row['id']) + ");"
         c.execute(command)
         print(command)
 # test SQL stmt in sqlite3 shell, save as string
command =  "CREATE TABLE Courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)
with open('courses.csv') as course:
     reader = csv.DictReader(course)
     for row in reader:
         command = "insert into Courses (code, mark, id) values ('" + row['code'] + "', " + str(row['mark']) + ", " + str(row['id']) + ");"
         c.execute(command)
         print(command)


#==========================================================

db.commit() #save changes
db.close()
