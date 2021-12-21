#!/usr/bin/python3
"""Module: DBStorage, new engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session, relationship
from sqlalchemy.orm import Session,query
from models.base_model import Base, BaseModel


class DBStorage:
	"""New engine DBStorage"""
	__engine = None
	__session = None

	def __init__(self):
		
		self.__engine = create_engine()