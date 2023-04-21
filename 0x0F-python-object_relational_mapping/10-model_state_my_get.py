#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Start engine to DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name
    state = session.query(State).filter_by(name=state_name).first()

    # Print state id or Not found
    if state:
        print(state.id)
    else:
        print('Not found')
