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
    VALUES ("Montreal", "Paris", 444);
```

### Query example
```SQL
    SELECT * FROM flights
    WHERE origin LIKE '%a%';
    /*
    The %a% means 'any character before and after a 'a'
    */
```