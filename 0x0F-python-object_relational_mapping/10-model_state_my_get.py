#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__" and len(sys.argv) == 5:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    con = engine.connect()
    s = select([State]).where(State.name == (sys.argv[4])).order_by(State.id)
    result = con.execute(s)
    # try if result is found or not
    try:
        if result.id:
            for row in result:
                print(row.id)
    except AttributeError:
        print("Not found")
