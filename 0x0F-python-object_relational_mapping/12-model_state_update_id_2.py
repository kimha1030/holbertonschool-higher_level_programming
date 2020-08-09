#!/usr/bin/python3
"""Update a state
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def update_state():
    """Update a state"""
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
        State.id).filter(State.id == 2)
    for row in query:
        row.name = "New Mexico"
    session.commit()
    session.close()

if __name__ == "__main__":
    update_state()
