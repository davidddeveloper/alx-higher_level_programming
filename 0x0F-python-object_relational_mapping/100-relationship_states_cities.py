#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the db
"""
from relationship_city import City
from relationship_state import State
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
    state = State()
    state.name = "California"
    session.add(state)
    session.commit()

    city = City()
    city.name = "San Francisco"
    city.state_id = state.id
    session.add(city)

    session.commit()

    session.close()
