#!/usr/bin/python3
""" Prints the first State object from the database 'hbtn_0e_6_usa'. """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    """ Prints the first State object from the database 'hbtn_0e_6_usa'. """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(username,
                                                      password,
                                                      database_name)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
