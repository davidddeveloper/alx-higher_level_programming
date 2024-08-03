#!/usr/bin/python3
"""
    a python file that contains the class definition of a State

"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from relationship_city import City

Base = declarative_base()


class State(Base):
    """ Represents a state """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state", cascade="all, delete-orphan")


if __name__ == '__main__':
    args = sys.argv[1:]
    username = args[0]
    password = args[1]
    db_name = args[2]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    username, password, db_name
                )
            )
    Base.metadata.create_all(engine)
