#!/usr/bin/python3
'''
this script fetches all the state data from specified db
'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


if __name__ = "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    for instance in session.query(State).order_by(states.id):
        print(instance.id, ": ", instance.name)
