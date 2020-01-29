#Amanda Zheng
#SoftDev1 pd1
#K24: A RESTful Journey Skyward
#2019-11-13
from flask import Flask , render_template
import urllib, json
from json import loads
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date=2019-10-06&hd=true&api_key=B0LkrGwFcjxCAT1dmcbuS4dPAq7b3yCT50W1dWT8")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic=data['url'], desc=data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
