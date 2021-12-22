#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """City instances with state_id == to current state.id"""
            c_list = []
            dict_obj = models.storage.all(City)
            for i in list(dict_obj).values():
                if i.state_id == self.id:
                    c_list.append(i)
            return c_list
