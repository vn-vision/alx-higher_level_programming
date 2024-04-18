#!/usr/bin/python3
'''
this script fetches all the state data from specified db
'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

Session = sessionmaker()

for instance in session.query(State).order_by(states.id):
    print(instance.id, ": ", instance.name)
