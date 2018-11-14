from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
dbPath = 'postgresql://postgres:postgres@localhost:5432/testflask'
engine = create_engine(dbPath)

db  = scoped_session(sessionmaker(bind=engine))
    
@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    print("log")
    return render_template("register.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")

    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number...")
    
   # if db.execute("SELECT * FROM flights WHERE id = :id", {"id", flight_id}).rowcount == 0:
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="Invalid fligh_id")
    db.execute("INSERT INTO passenger (name, flightid) VALUES (:name, :flightid)",
        {"name":name, "flightid":flight_id})
    db.commit()
    return render_template("succes.html")

@app.route("/flights")
def flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flight/<int:flight_id>")
def flight(flight_id):
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight")
    
    passengers = db.execute("SELECT * FROM passenger WHERE flightid = :flightid", 
        {"flightid":flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)