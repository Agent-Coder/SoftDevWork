#Amanda Zheng
#SoftDev1 pd1
#Flasks HW
#2019-09-18
from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_english():
    print(__name__) #This is printed during reloading page
    return " HIIIIII!"#displayed text on the website

@app.route("/Spanish") #assign following fxn to run when run route requested
def hello_spanish():
    print(__name__)
    return " HOLAAAA!"

@app.route("/French") #assign following fxn to run when run route requested
def hello_french():
    print(__name__)
    return "bONJOURRR!"
if __name__ == "__main__":
    app.debug = True #allows for reloading
    app.run() #runs the webiste
