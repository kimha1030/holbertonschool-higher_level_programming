#!/usr/bin/python3
"""Add a new state
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def add_state():
    """Add a new state"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
    session.close()

if __name__ == "__main__":
    add_state()
