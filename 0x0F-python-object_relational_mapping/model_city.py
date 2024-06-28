#!/usr/bin/python3
"""Defines a City model."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): The city's id.
        name (str): The city's name.
        state_id (int): The state's id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
