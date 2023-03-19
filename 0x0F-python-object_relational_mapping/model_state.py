#!/usr/bin/python3
"""
Defines State model
Inherits from SQLAlchemy Base class and link to MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for MySQL DB.

    __tablename__ (str): The name of MySQl table in the store
    id (sqlalchemy.Integer): The state id
    name (sqlalchemy.String): The state name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
