#!/usr/bin/python3
"""Module to define the State class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class that inherits from Base."""
    __tablename__ = 'states'
    id = Column
    (Int, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    cities = relationship
    ('City', backref='state', cascade='all, delete-orphan')
