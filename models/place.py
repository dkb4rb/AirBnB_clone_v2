#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from AirBnB_clone_v2.models.review import Review
from models.base_model import Base, BaseModel
from sqlalchemy import String, Integer, Float, ForeignKey
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            review_list = []
            for review in all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
    else:
        reviews = relationship("Review", backref="place",
                               cascade="all, delete", passive_deletes=True)
