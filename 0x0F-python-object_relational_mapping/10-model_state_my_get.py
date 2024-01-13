#!/usr/bin/python3
"""Prints the State object with the specified name from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <user> <password> <db> <state>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db, state =
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db))

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the specified name and print the result
    state = session.query(State).filter_by(name=state).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
