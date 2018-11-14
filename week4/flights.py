import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def selectSql(db):
    #FETCH EXAMPLE
    flights = db.execute('SELECT * FROM flights').fetchall()
    for flight in flights:
        print(f"{flight.origin} TO {flight.destination} with distance of {flight.duration}")

def insertSql(db):
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        # (:origin, :dest...) are placeholders and we need to pass a dict with these key value
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
            {"origin":origin, "destination":destination, "duration":duration})
        print(f"Added origin:{origin} destination:{destination} duration:{duration}.")
        db.commit()
def main():
    # ://<user>:<pwd>@<host>:<port>/<db_name>
    dbPath = 'postgresql://postgres:postgres@localhost:5432/testflask'
    engine = create_engine(dbPath)

    db = scoped_session(sessionmaker(bind=engine))

    selectSql(db)
    #insertSql(db)
    selectSql(db)

if __name__=='__main__':
    main()