#!/usr/bin/python3
"""Lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def list_state():
    """List all states"""
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
    for row in query.all():
        print("{}: {}".format(row.id, row.name))
    session.close()

if __name__ == "__main__":
    list_state()
