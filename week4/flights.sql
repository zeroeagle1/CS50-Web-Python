CREATE TABLE flights(
	id SERIAL PRIMARY KEY,
        origin VARCHAR NOT NULL,
        destination VARCHAR NOT NULL,
        duration INTEGER NOT NULL
);

CREATE TABLE passenger(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL,
    flightId INTEGER REFERENCES flights
);

INSERT INTO flights (origin, destination, duration) VALUES ('mtl', 'par', 544);
INSERT INTO flights (origin, destination, duration) VALUES ('mtl', 'nyc', 544);
INSERT INTO flights (origin, destination, duration) VALUES ('mtl', 'lax', 4124);
INSERT INTO flights (origin, destination, duration) VALUES ('nyc', 'par', 4114);
INSERT INTO flights (origin, destination, duration) VALUES ('wash', 'cal', 124);
INSERT INTO flights (origin, destination, duration) VALUES ('bogata', 'yellow  knife', 551);
INSERT INTO flights (origin, destination, duration) VALUES ('constantinople', 'istanbul', 1);
