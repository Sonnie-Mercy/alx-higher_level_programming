#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create mySQL engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured Session class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states containing the letter "a"
    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print the results
    for state in query:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
