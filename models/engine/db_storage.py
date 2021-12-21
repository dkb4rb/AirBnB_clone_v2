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
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all method"""
        rdict = {}
        if cls == None:
            query_1 = self.__session.query(User, State, City, Amenity,
                                        Place, Review)
            for i in query_1:
                key_word = ("{}.{}".format(type(i).__name__, i.id))
                rdict[key_word] = i
            return rdict
        else:
            if type(cls) == str:
                cls = eval(cls)
            query_2 = self.__session.query(cls)
            for x in query_2:
                key_word = ("{}.{}".format(type(x).__name__, x.id))
                rdict[key_word] = x
                return rdict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit al changesof the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current db session"""
        if obj:
            self.__session.delete(obj)
