#!/usr/bin/env python3
""" Database for ORM """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database and returns it."""
        # Create a new User instance with the provided email and hashed password
        new_user = User(email=email, hashed_password=hashed_password)
        # Add the User instance to the current SQLAlchemy session
        self._session.add(new_user)
        # Commit the changes to the database to persist the new user
        self._session.commit()
        # Return the User instance, now with an ID assigned by the database
        return new_user
