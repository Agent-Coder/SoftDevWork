#Amanda Zheng, Yevgeniy Gorbachev
#SoftDev1 pd1
#K09 -- Yummy Mongo Py
#2020-02-26


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client.test
#db.restaurants.drop()
restaurants = db.restaurants
file = open("dataset.json", "r")
content = file.readlines()
for line in content:
    restaurants.insert_one(loads(line))
#for item in restaurants.find({}):
#    print(item)

#file = open("dataset.json", "r")
#doc=file.readlines()
#for line in doc:

#doc=doc[1:len(doc)-1]
#line=str(file.readline())
    #result=restaurants.insert_one(loads(line))


def findBorough(bor):
    return db.restaurants.inventory.find( { "borough": bor },{_id: 0, "name": 1,} )

def findzip(zip):
    return db.restaurants.inventory.find( { "address.zipcode": zip },{_id: 0, "name": 1,} )

def findzipgrade(zip,grade):
    return db.restaurants.inventory.find( { "address.zipcode": zip, "grades.grade": grade },{_id: 0, "name": 1,} )

def findzipthresh(zip,score):
    return db.restaurants.inventory.find( { "address.zipcode": zip, "grades.score": {"$lt":score}},{_id: 0, "name": 1,} )
