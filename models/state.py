#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
