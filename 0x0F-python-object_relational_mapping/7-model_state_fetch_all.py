#!/usr/bin/python3
"""
The `State` class inherits from `Base`, an SQLAlchemy declarative base.
Instances of `State` will be a MySQL database.
"""

from sys import argv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from model_state import Base, State
from urllib.parse import quote_plus

if __name__ == '__main__':

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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
