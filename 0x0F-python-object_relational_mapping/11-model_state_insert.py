#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    query = "INSERT INTO  `hbtn_0e_6_usa`.`states` (`name`) VALUES(%s)"
    id = engine.execute(query, 'Louisiana')
