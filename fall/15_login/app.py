#Amanda Zheng and Emily Zhang (Team CookieMonster)
#SoftDev1 pd10
#K15 -- Do I Know You?
#2019-10-02
import os,base64
from flask import Flask, render_template, request, redirect, url_for,session
app = Flask(__name__)

app.secret_key = os.urandom(64)
#random secret key(has to be outside here)
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
    """
    Makes user and password, checks username and password.
    Redirects to different errors if either or user  and password is wrong.
    If both are right, make session key and make the value the user
    """
        user="CookieMonster"
        pa="SeasameStreet"
        if(request.args["username"]==user):
            if (request.args["password"]==pa):
                session['user']=user
                #make session, name the key anything and value should be user
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
    return render_template("welcome.html")

@app.route("/loggedout")
def logged_out():
    session.pop('user',None)
    #pop out the user
    return render_template("home.html")

@app.route("/redirecting-from-error")
def relogin():
    return render_template("home.html")

@app.route("/redirecting-from-welcome")
def redirector():
        return redirect(url_for('logged_out'))

if __name__ == "__main__":
    app.debug = True
    app.run()
