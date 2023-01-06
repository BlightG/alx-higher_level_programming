#!/usr/bin/python3
""" Sql alchemy first trial """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# manage tables
Base = declarative_base()


class State(Base):
    """ states class to maniulate states table in hbtn_0e_6_usa """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
