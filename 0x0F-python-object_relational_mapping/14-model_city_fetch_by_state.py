#!/usr/bin/python3
"""
This script joins City and State tables
and prints a list of all Cities with their
state names, city names, and city ids.
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import update
from urllib.parse import quote_plus;

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine(
        f'mysql+mysqldb://{username}:{quote_plus(password)}@{host}:{port}/{db_name}')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    usa = session.query(City, State) \
        .join(State, State.id == City.state_id) \
        .order_by(City.id.asc()) \
        .all()

    for city in usa:
        print("{}: ({}) {}".format(city.State.name,
                                   city.City.id,
                                   city.City.name))
