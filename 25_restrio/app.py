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
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2/alpha/col")
    response = u.read()
    data = json.loads(response)
    print(data['name'])
    return render_template("spotify.html", name=data['name'],
                            capital=data['capital'],
                            population=data['population'],
                            languages=data['languages'][0]['name'],
                            flag=data['flag'],
                            timezones=data['timezones'],
                            borders=data['borders'],
                            currencies=data['currencies'][0]['name'],
                            symbol=data['currencies'][0]['symbol'],
                            region=data['region'],
                            subregion=data['subregion'],
                            area=data['area'],
                            nativeName=data['nativeName'],
                            numericCode=data['numericCode'])


if __name__ == "__main__":
    app.debug = True
    app.run()
