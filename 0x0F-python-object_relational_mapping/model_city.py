#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py that
contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import State, Base


class City(Base):
    """
    class city that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)i
