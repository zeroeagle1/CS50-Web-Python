from flask import Flask, render_template, request, session
from flask_session import Session
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

@app.route("/form")
def form():
    return render_template("form.html")

# Note: that route can only be accesed via post request
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
@app.route("/note", methods=["GET", "POST"])
def note():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("note.html", notes=notes)