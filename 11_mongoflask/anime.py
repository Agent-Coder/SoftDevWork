#Amanda Zheng, Tiffany Cao, Team Blank
#K11 --
#2020-03-05

from flask import Flask, render_template, request,session
from pymongo import MongoClient
import json
from bson.json_util import loads

app = Flask(__name__)
client = MongoClient("localhost", 27017)
anime = client.weeb.anime

def create():
    anime.drop()
    file = open("anime.json", "r")
    doc = file.readlines()
    for x in doc:
        anime.insert_one(loads(x))

#create()

def findStatus(stat):
    if stat==0:
        result= anime.find({})
    else:
        result= anime.find({ "status": stat })
    answer=[]
    for x in result:
        answer.append(x["title"].encode('utf8'))
    return answer

def findTitle(name):
    if name=="":
        result= anime.find({})
    else:
        name=".*"+name+".*"
        result= anime.find({ "title": { "$regex": name, "$options" : "i" }})
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer

def findEp(num,mode):
    if mode==0 or num == "":
        result= anime.find({})
    if(mode=="Less"):
        result= anime.find({ "episodes": { "$lte": num }})
    else:
        result= anime.find({ "episodes": { "$gte": num }})
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer


def findType(type):
    if type==0:
        result=anime.find({})
    else:
        result= anime.find({ "type": type })
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer

def findRand(num):
    return anime.aggregate([{ "$sample": { "size": num }}])


t=findType("OVA")
s=findStatus("CURRENTLY")
e=findEp(0,0)
h=findTitle("")
loop=[]
if(len(t)<len(s) and len(t)<len(e) and len(t)<len(h)):
    loop=t
elif(len(s)<len(t) and len(s)<len(e) and len(s)<len(h)):
    loop=s
elif(len(e)<len(s) and len(e)<len(t) and len(e)<len(h)):
    loop=e
else:
    loop=h
results = []
count = 0
for x in loop:
    if (x in s) and (x in t) and (x in e) and (x in h):
        results.append(x)
        count+=1
    if count>50:
        break
#for result in findStatus("CURRENTLY"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findTitle("girl"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findEp(20):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findType("OVA"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findRand(10):
   #if (result["title"]==""):
     #print("No Name Found")
   #else:
     #print (result["title"])

if __name__ == "__main__":
    app.debug = True
    #app.run()
