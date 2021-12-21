#!/usr/bin/python3
"""Module: DBStorage, new engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.orm import Session, query
from sqlalchemy.sql.functions import user
from models.base_model import Base, BaseModel
from os import getenv


class DBStorage:
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("""'mysql+mysqldb://{}:{}@{}/{}'
                                    .format(user, password, host, db),
                                    pool_pre_ping=True""")
        
