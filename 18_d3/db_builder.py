#Amanda Zheng, Tiffany Cao, Yifan Wang (Team Icky Toothpaste)
#SoftDev1 pd1
#K18 -- Come Up For Air
#2020-04-18
import sqlite3, urllib, json

DB_FILE = "covid19.db"

def exec(cmd):
    """Executes a sqlite command"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd)
    db.commit()
    return output

def execmany(cmd, inputs):
    """Executes a sqlite command using ? placeholder"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd, inputs)
    db.commit()
    return output

#==========================================================
def build_db():
    print("Database is being created. It may take a while. Please stand by...")
    command = "CREATE TABLE IF NOT EXISTS covid19_tbl (day INT, month INT, cases INT, country TEXT)"
    exec(command)
    f = open("../static/countries.csv", "r")
    lines=f.read()
    for line in lines:
        if "France" in line:
            entry=line.strip("\n").split(",")
            command = "INSERT INTO covid19_tbl VALUES("+entry[1]+","+entry[2]+","+entry[4]+",'"+entry[6]+"')"
            exec(command)
        '''elif "Italy" in line:
            entry=line.strip("\n").split(",")
            command = "INSERT INTO covid19_tbl VALUES("+entry[1]+","+entry[2]+","+entry[4]+",'"+entry[6]+"')"
            exec(command)'''
        #elif "United_States_of_America" in line or "Egypt" in line or "United_Kingdom" in line or "China" in line or "Canada" in line or "Brazil" in line or "South_Korea" in line or "Turkey" in line
