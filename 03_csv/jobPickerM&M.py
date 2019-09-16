import random
file=open("occupations.csv","r")
job=file.read().split("\n")

def splitCategory(l):
    for x in range(0,len(l)):
        l[x]=l[x].rsplit(",",1)
    return l
job=splitCategory(job)

def takeOutQuotes(l):
    for x in range(0,len(l)):
        for i in range(0,len(l[x])-1):
            l[x][i]=l[x][i].strip("\"")
    return l
job=takeOutQuotes(job)
job=job[1:len(job)-2]
def rangePercent(l):
    l[0][1]=float(l[0][1])
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


