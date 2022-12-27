#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 5:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id)\
                                .filter(State.name == sys.argv[4]).first()

    print("Not found" if not state else state.id)
