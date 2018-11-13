from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello World"
    return render_template("index.html", headline=headline)

@app.route("/date")
def checkDate():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("date.html", new_year=new_year)

@app.route("/more")
def more():
    return render_template("more.html")