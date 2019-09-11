import random

def randStudent(lis):
    secRand=lis.keys()[random.randint(0,2)]
    print secRand
    print (lis.get(secRand)[random.randint(0,len(lis.get(secRand))-1)])
Krewes={'orpheus':['aksjfoad','sadjofija','oisdfhahio'], 'rex':['ejsdfho','cidfh','biudhf'], 'endymion':['iodfu','laks','maios']}
randStudent(Krewes)

        
