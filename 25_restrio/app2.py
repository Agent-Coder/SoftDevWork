#Amanda Zheng
#SoftDev1 pd1
#K25: Getting More Rest
#2019-11-13
from flask import Flask , render_template
import urllib, json
from json import loads
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen("https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple")
    response = u.read()
    data = json.loads(response)
    data=data['results']
    return render_template("superhero.html", list=data)


if __name__ == "__main__":
    app.debug = True
    app.run()
