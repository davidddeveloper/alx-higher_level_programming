#!/usr/bin/python3
""" a script that list all cities by states in db
"""
from model_state import Base, State
from model_city import City
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
    cities = session.query(City).join(State).where(
            City.state_id == State.id
        ).all()
    for city in cities:
        state = session.query(State).where(
            State.id == city.state_id
        ).first()
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
