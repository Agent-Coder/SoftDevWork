import random

def randStudent(lis):
    firstRand=random.randint(0,2)
    if firstRand==0:
        firstRand='orpheus'
    elif firstRand==1:
        firstRand='rex'
    else:
        firstRand='endymion'
    print (lis.get(firstRand)[random.randint(0,len(lis.get(firstRand))-1)])
Krewes={'orpheus':['aksjfoad','sadjofija','oisdfhahio'], 'rex':['ejsdfho','cidfh','biudhf'], 'endymion':['iodfu','laks','maios']}
randStudent(Krewes)

        
