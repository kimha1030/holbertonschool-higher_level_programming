#!/usr/bin/python3
"""List all State obj that contain the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def state_contain():
    """Name state that contain the letter a"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(
        State.id).filter(State.name.contains("%a%"))
    for row in query:
        print("{}: {}".format(row.id, row.name))
    session.close()

if __name__ == "__main__":
    state_contain()
