#!/usr/bin/python3
"""Prints the first State object from the DB
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def first_state():
    """Print first state"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    try:
        query = session.query(State).order_by(State.id).first()
        print("{}: {}".format(query.id, query.name))
    except:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    first_state()
