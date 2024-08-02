#!/usr/bin/python3
""" a script that gets a state passed as argument
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    username = args[0]
    password = args[1]
    db_name = args[2]
    state_name = args[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username,
                password,
                db_name
                )
            )
    # create a session for querying
    Session = sessionmaker(bind=engine)
    session = Session()

    # list all states
    state = session.query(State).where(State.name == state_name).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Not found")
    session.close()
