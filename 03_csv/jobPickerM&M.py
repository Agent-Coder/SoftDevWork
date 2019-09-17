import random
file=open("occupations.csv","r")
job=file.read().split("\n")
#opening, reading, and splitting the occupations thing on new lines
def splitCategory(l):
    #splits occupations and percentages
    for x in range(0,len(l)):
        #loop through list 
        l[x]=l[x].rsplit(",",1)
        #split at the last comma of each item (becomes 2d array with occupation and percentage)
    return l
job=splitCategory(job)

def takeOutQuotes(l):
    #function for taking out quotes
    for x in range(0,len(l)):
        #loop through the list
        for i in range(0,len(l[x])-1):
            #loop through the occupation and then the percentage
            l[x][i]=l[x][i].strip("\"")
            #strip the quotes
    return l
job=takeOutQuotes(job)
job=job[1:len(job)-2]
#take out the first item(category titles) and last thing (total percentage) 
def rangePercent(l):
    #make 
    l[0][1]=float(l[0][1])
    #make the first string percentage a float
    for x in range(1,len(l)):
        l[x][1]=round(float(l[x][1])+l[x-1][1],1)
    return l
job=rangePercent(job)

def randomPick(l):
    rand=random.randint(0,1000)
    rand=rand/10.0
    counta=0
    countb=len(l)-1
    if rand>99.8:
        return "unemployed"
    while l[counta][1]<rand and l[countb][1]>rand:
        counta=counta+1
        countb=countb-1
    if  l[countb][1]==rand:
         return l[countb][0]
    if l[counta][1]>=rand:
        return l[counta][0]
    else:
        return l[countb+1][0]
print (randomPick(job))


