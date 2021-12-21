#!/usr/bin/python3
""" State Module for HBNB project """
from AirBnB_clone_v2.models import city
from models.city import City
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """City instances with state_id == to current state.id"""
            c_list = []
            dict_obj = all(City)
            for i in list(dict_obj).values():
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
