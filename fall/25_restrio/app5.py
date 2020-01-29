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
    u = urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/208218")
    response = u.read()
    data = json.loads(response)
    return render_template("art.html", title=data['title'], pic=data['primaryImage'],
                                        department=data['department'], date=data['objectDate'],
                                        medium=data['medium'], credit=data['creditLine'],
                                        tags=data['tags'], place=data['excavation'],
                                        classify=data['classification'])

if __name__ == "__main__":
    app.debug = True
    app.run()
