# WEEK 4 - SQL
This class uses **Postgresql**
### Data Type
* INTEGER
* DECIMAL
* SERIAL (auto-incread
* VARCHAR
* TIMESTAMP
* etc..

### Create Table
```SQL
    CREATE TABLE flight (
        id SERIAL PRIMARY KEY,
        origin VARCHAR NOT NULL,
        destination VARCHAR NOT NULL,
        duration INTEGER NOT NULL
    );
```
To run postgres server, it can be done on the local machine or you can host it (heroku is a free host)

### Constraints
* NOT NULL
* UNIQUE
* PRIMARY KEY
* DEFAULT
* CHECK
* etc..

### Insert data
```SQL
    INSERT INTO flights
    (origin, destination, duration)
    VALUES ('Montreal', 'Paris', 444);
```
### Foreign key
```SQL
CREATE TABLE passenger(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL,
    flightId INTEGER REFERENCES flights
);
```
### Query example
```SQL
    SELECT * FROM flights
    WHERE origin LIKE '%a%';
    /*
    The %a% means 'any character before and after a 'a'
    */

    SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) >1 ;
```

Relational databases can are able to link different table with foreign key

**INDEXES** are used to get data faster. Cons: slower to insert/edit data

## **SQL Transaction**
* Used the solve the race condition problem (multiple modification allow)
* A transaction is done with begin and commit

**Sql alchemy** is a library that manage the connection to db
```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# ://<user>:<pwd>@<host>:<port>/<db_name>
dbPath = 'postgresql://postgresql:postgresql@localhost:5432/testflask'
#engine deal with everything related to the db
engine = create_engine(dbPath))

#allow differents session
db = scoped_session(sessionmaker(bind=engine))
```
How to execute Query
```python
flights = db.execute("SELECT origin, destination FROM flights").fetchall()
#fetchall() returns result as a list
for flight in flights:
    print(f"{flight.origin} to {flight.destination}")
```

Read and use CSV
```python
f = open("text.csv")
#csv.reader is a built-in python function
reader = csv.reader(f)
for origin, destination, duration in reader:
    db.execute("INTERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration", 
       {"origin":origin, "destination":destination, "duration":duration})
    print(f"from {origin} to {destination} duration {duration}.")
    db.commit()
```