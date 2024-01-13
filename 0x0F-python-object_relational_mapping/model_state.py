#!/usr/bin/python3
"""Defines State class and creates Base instance."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create engine
engine = create_engine
('mysql+mysqldb://username:password@localhost:3306/hbtn_0e_6_usa')

# Create Base instance
Base = declarative_base()


# Define State class
class State(Base):
    """Class representing the states table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(engine)
