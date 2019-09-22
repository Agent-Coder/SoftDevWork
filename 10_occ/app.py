# Amanda Zheng and Yaru Luo (AI-YA)
# SoftDev1 pd1
# K#10: Jinja Tuning
# 2019-09-24

from flask import Flask, render_template
app = Flask(__name__) # create instance of class Flask
import csv, random

rows = []
with open('occupations.csv', 'r') as csvFile:
    csvreader = csv.reader(csvFile)
    for row in csvreader:
        rows.append(row)
dictionary = {}
for item in rows[1: len( rows) - 1]:
    key = item[0]
    value = float( item[1])
    dictionary[ key] = value
r = []
with open('link.csv', 'r') as cFile:
    csvread = csv.reader(cFile)
    for row in csvread:
        r.append(row)
encyclopedia={}
for item in r[0: len( r)]:
    key = item[0]
    value = item[1]
    encyclopedia[ key] = value

#make into a dictionary
def rangePercent(l):
    di=list(l.keys())
    l[di[1]]=float(l.get(di[1]))
    for k in range(1,len(l.keys())):
        l[di[k]]=round(float(l.get(di[k])+l.get(di[k-1])),1)
        #make the current percentage the sum of the previous and current such that if the first item has 6.1 percent and second one has 10.2 %
        #we will modify the second number to be 16.3 so that when we generate a random number we can use binary search to find which two items it is between
        #if our random number is 5.3, since its less than the 6.1, the first item is returned
        #if 11.4 is generated, second item is returned because it is greater than 6.1 but less than 16.3
    return l
dictionary=rangePercent(dictionary)
def randomPick(l):
    #generates a random percentage between 0 and 100%
    rand=random.randint(1,1000)
    rand=rand/10.0
    di=list(l.keys())
    #counters for looping through the list
    counta=0
    countb=len(di)-1
    #the case where none of the occupations are selected
    if rand>99.8:
        return "unemployed"
    #loop through the list both from the front and the back until the randomly generated percentage is within one of the sections
    while l.get(di[counta])<rand and l.get(di[countb])>rand:
        #loop through both front and back; front loop till find something greater, back loop till find something smaller
        counta=counta+1
        #advance front loop
        countb=countb-1
        #push back back loop
    #this is the case that the randomly generated percentage was exactly one of the percentages
    if  l.get(di[countb])==rand:
         return di[countb]
        #deals with edge case for back loop
    if l.get(di[counta])>=rand:
        return di[counta]
    #front loop returns whatever item it counted up to
    else:
        return di[countb+1]
    #back loop returns the next item
coll=dictionary
col=encyclopedia
@app.route("/") # assign following fxn to run when route requested
def hello_world():
    print(__name__+ "Norm")
    return "Werk werk werk werk werk" #default localhost page

@app.route("/occupyflaskst")
def init():
    print("csving")
    return render_template(
        'work.html',
        coll = dictionary,   #for the tablified occupations list
        output = randomPick(coll), #for the lucky occupation
        col=encyclopedia
        )

if __name__ == "__main__":
    #autopilot
    app.debug = True
    app.run()
