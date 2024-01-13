#!/usr/bin/python3
"""Lists all State objects with the letter 'a' from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects with the letter 'a' and print the results
    states_with_a = session.query(State).filter(State.name.like('%a%')).
    order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
