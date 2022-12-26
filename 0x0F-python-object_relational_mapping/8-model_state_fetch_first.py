#!/usr/bin/python3
"""prints the first state object from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    con = engine.connect()
    s = select([State]).where(State.id == '1')
    for row in con.execute(s):
        print(f"{row[0]}: {row[1]}")
