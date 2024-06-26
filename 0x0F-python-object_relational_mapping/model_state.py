#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base as new_declarative_base
from sqlalchemy import create_engine

Base = new_declarative_base()
if __name__ == "__main__":
    from urllib.parse import quote_plus
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            quote_plus(
                sys.argv[2]),
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
