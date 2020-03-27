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
    result= anime.find({})
    if stat!="NONE" and stat!=0 and stat!="0":
        result= anime.find({ "status": stat },{"title":1,"_id":0})
    answer=[]
    for x in result:
        answer.append(x["title"])
    return answer

def findTitle(name):
    result= anime.find({})
    if name!="" and name!="0":
        name=".*"+name+".*"
        result= anime.find({ "title": { "$regex": name, "$options" : "i" }})
    answer=[]
    for x in result:
        answer.append(x['title'])
    return answer

def findEp(num,mode):
    result= anime.find({})
    if(mode=="Less"):
        #num=int(num)
        result= anime.find({ "episodes": { "$lte": n }})
    elif(mode=="Greater"):
        #num=int(num)
        result= anime.find({ "episodes": { "$gte": n }})
    answer=[]
    for x in result:
        answer.append(x['title'])
    return answer


def findType(t):
    result=anime.find({})
    if (t!="0" and t!=0):
        result= anime.find({ "type": t },{"title":1,"_id":0}) 
    answer=[]
    for x in result:
        answer.append(x['title'])
    return answer

def findRand(num):
    return anime.aggregate([{ "$sample": { "size": num }}])

