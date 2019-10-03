#Amanda Zheng, Junhee Lee, Team Jam
#SoftDev1 pd1
#K12 -- Echo Echo Echo
#2019-09-26

from flask import Flask, render_template, request,session

app = Flask(__name__)

@app.route("/", methods=['GET'])
def origin():
    print(__name__ + "root")
    return render_template("form.html")

@app.route("/auth")
def auth():
    print("\n\n\n")
    print("***DIAG: This flask obj***")
    print(app)
    print("***DIAG: request obj***")
    print(request)
    print("***DIAG:request.args***")
    print(request.args)
    #print("***DIAG: request.args['user']***")
    #print(request.args['user'])
    #print("***DIAG: request.headers***")
    #print(request.headers)
    session['user']=request.args['user']
    print(session.pop('user'))
    print(request.cookies.get('user'))
    return render_template("submit.html",output=request.args.get('user'))

if __name__ == "__main__":
    app.debug = True
    app.run()
