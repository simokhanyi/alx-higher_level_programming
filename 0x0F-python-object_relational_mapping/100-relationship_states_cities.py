#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco"."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create a State object "California" with the City "San Francisco"
    new_state = State(name="California", cities=[City(name="San Francisco")])

    # Add the State to the session and commit
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
