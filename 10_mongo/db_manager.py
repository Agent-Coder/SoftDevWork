#Amanda Zheng, Yevgeniy Gorbachev (downgraded-octo-waffle)
#SoftDev1 pd1
#K09 -- Yummy Mongo Py
#2020-02-26


from bson.json_util import loads
from pymongo import MongoClient
import json
client = MongoClient("localhost",27017)
quiz = client.jeopardy.quiz
quiz.drop()
file = open("teamname.json", "r")
doc = json.load(file)
print(doc[0])
for line in doc:
    quiz.insert_one(line)

def findTopic(q):
    return quiz.find( { "question": q },{ "category": 1,"_id":0} )

def questionWorth(q):
    return quiz.find( { "question": q },{ "value": 1,"_id":0} )

def price(p):
    p="$"+str(p)
    return quiz.find( { "value": p },{ "question": 1,"_id":0} )

def category(c):
    return quiz.find( { "category": c },{ "question": 1,"_id":0} )

def answer(q):
    return quiz.find( { "question": "'"+q+"'" },{ "answer": 1,"_id":0} )

def doubleJeopardy():
    return quiz.find( { "round": "Double Jeopardy!" },{ "question": 1,"_id":0} )




print("\nPrinting category of the question: William Pereira ercted his Transmaerica \"Pyramid\" in this city\n")

for result in findTopic("'William Pereira erected his Transamerica \"Pyramid\" in this city'"):
    if(result["category"]==""):
       print("No Questions Found")
    else:
       print(result["category"].strip("'"))

print("\nPrinting all questions of a category\n")
for result in category("HISTORY"):
    if (result["question"]==""):
        print("No Questions Found")
    else:
       print(result["question"].strip("'"))


print("\nPrinting how much a question is worth: It can be a place to leave your puppy when you take a trip, or a carrier for him that fits under an airplane seat\n")

for result in questionWorth("'It can be a place to leave your puppy when you take a trip, or a carrier for him that fits under an airplane seat'"):
    if (result["value"]==""):
        print("No Questions Found")
    else:
      print (result["value"].strip("'"))

print("\nPrinting questions worth $600\n")

for result in price(600):
    if(result["question"]==""):
        print("No Questions Found")
    else:
      print(result["question"].strip("'"))

print("\nPrinting answer to a Jeopardy Question: Africa's lowest temperature was 11 degrees below zero in 1935 at Ifrane, just south of Fez in this country\n")
for result in answer("Africa's lowest temperature was 11 degrees below zero in 1935 at Ifrane, just south of Fez in this country"):
    if(result["answer"]==""):
        print("No Questions Found")
    else:
        print(result["answer"].strip("'"))

print("\nPrinting Double Jeopardy Questions\n")
for result in doubleJeopardy():
    print(result["question"].strip("'"))
    
