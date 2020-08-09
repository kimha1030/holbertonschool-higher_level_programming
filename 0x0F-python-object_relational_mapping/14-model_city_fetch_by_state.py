#!/usr/bin/python3
"""Prints all City objects from DB
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def list_state_city():
    """Prints all City objects from DB"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(
        State,
        City).filter(
        State.id == City.state_id).order_by(
        City.id)
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()

if __name__ == "__main__":
    list_state_city()
