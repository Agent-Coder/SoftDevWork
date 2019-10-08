import csv

with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile,'name','age','id')
    for row in reader:
        print(row['name'],row['age'],row['id'])
