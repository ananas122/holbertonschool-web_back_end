#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Add a new user to the database.
        """
        # Create a new User instance
        user = User(email=email, hashed_password=hashed_password)
        # Add the User instance to the current SQLAlchemy session
        self._session.add(user)
        # Commit the changes to the database to persist the new user
        self._session.commit()
        # Return the User instance, now with an ID assigned by the db
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database by specified criteria."""
        try:
            # Effectue 1requ ds db pr récup 1er user = critères kwargs
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound(
                    "Not found")
            return user
        except NoResultFound as e:
            # e pr stock l instance de l except capturé ici
            raise NoResultFound(f"Invalid: {e}")
