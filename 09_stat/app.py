from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_world():
    print(__name__) #where will this go?
    return "THIS IS ABOUT THE KID WHO SITS NEXT TO ME IN SYSTEM!"

coll=[0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def test_tmplt():
    return render_template('my_foist_template.html',
            foo="foooo",
            collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
