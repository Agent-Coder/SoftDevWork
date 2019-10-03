#Amanda Zheng and Emily Zhang (Team CookieMonster)
#SoftDev1 pd10
#K15 -- Do I Know You?
#2019-10-02
import os
from flask import Flask, render_template, request, redirect, url_for,session
app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("home.html")
@app.route("/error1")
def error1():
    return render_template("error1.html")

@app.route("/error2")
def error2():
    return render_template("error2.html")

@app.route("/error3")
def error3():
    return render_template("error3.html")

@app.route("/redirecting-from-login")
def redirecting():
        user="CookieMonster"
        pa="SeasameStreet"
        if(request.args["username"]==user):
            if (request.args["password"]==pa):
                return redirect(url_for('welcome'))
            else:
                return redirect(url_for('error2'))
        else:
            if (request.args["password"]==pa):
                return redirect(url_for('error1'))
            else:
                return redirect(url_for('error3'))

@app.route("/welcome")
def welcome():
    #random_bytes = os.urandom(64)
    #app.secret_key = b64encode(random_bytes).decode('utf-8')
    #session[app.secret_key]=
    return render_template("welcome.html")

@app.route("/loggedout")
def logged_out():
    return render_template("home.html")

@app.route("/redirecting-from-welcome")
def redirector():
        return redirect(url_for('logged_out'))

if __name__ == "__main__":
    app.debug = True
    app.run()
