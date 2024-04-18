#!/usr/bin/python3
'''
contains a definition of class State
an instance Base = declarative_base()
'''
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
conn = engine.connect()

class State(Base):
    # class state that inherits from Base
    __tablename__ = 'states'

    # create a class attribute for the table states
    id = Column(Integer, primary_key=True, nullable=False, autogincrement=True)
    name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
