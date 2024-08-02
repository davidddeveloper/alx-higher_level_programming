#!/usr/bin/python3
""" a script that updates a state
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
    state = session.query(State).where(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
