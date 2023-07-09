CREATE TABLE IF NOT EXISTS people (
    given_name varchar(50),
    family_name varchar(50),
    date_of_birth varchar(15),
    place_of_birth varchar(50),
    unique key place (given_name, family_name, date_of_birth, place_of_birth)
);

CREATE TABLE IF NOT EXISTS places (
    city varchar(50),
    county varchar(50),
    country varchar(50),
    unique key place (city, county, country)
);