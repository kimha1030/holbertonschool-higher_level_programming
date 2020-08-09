#!/usr/bin/python3
"""Prints the id of the argument (state)
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def get_state():
    """Prints the id of the argument (state)"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    count = 0
    for row in query:
        if row.name == sys.argv[4]:
            count = row.id
    if count != 0:
        print(count)
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    get_state()
