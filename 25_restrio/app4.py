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
    u = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/JPY")
    response = u.read()
    data = json.loads(response)
    return render_template("currency.html", base=data['base'], exchange=data['rates'])

if __name__ == "__main__":
    app.debug = True
    app.run()
