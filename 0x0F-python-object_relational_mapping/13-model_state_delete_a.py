#!/usr/bin/python3
"""Delete a state
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def delete_state():
    """Delete a state"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.contains("%a%"))
    query.delete(synchronize_session='fetch')
    session.commit()
    session.close()

if __name__ == "__main__":
    delete_state()
