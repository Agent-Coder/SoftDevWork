#Amanda Zheng, Tiffany Cao, Yifan Wang (Team Icky Toothpaste)
#SoftDev1 pd1
#K18 -- Come Up For Air
#2020-04-18

from flask import Flask, request, render_template
from utl import db_builder
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    db_builder.build_db()
    app.debug = True
    app.run()
