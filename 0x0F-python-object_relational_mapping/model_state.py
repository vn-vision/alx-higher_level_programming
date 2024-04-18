#!/usr/bin/python3
'''
contains a definition of class State
an instance Base = declarative_base()
'''
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine


Base = declarative_base()


class State(Base):
    '''
    This is  class state that inherits from Base
    creates a table states and its attributes
    id: pk, name: of the state
    '''
    __tablename__ = 'states'

    # create a class attribute for the table states
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
