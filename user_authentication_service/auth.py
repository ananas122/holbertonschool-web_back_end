#!/usr/bin/env python3
"""
encrypting passwords
"""
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Encrypting passwords using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a UUID for session IDs."""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth class."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the database.
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # If no user is found, proceed with adding the user
            hashed_password: str = _hash_password(password)
            # Add the new user to the database
            user = self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials."""
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)
            # Check if the provided password matches the hashed password in the database
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            # If no user is found with the provided email, return False
            return False

    def create_session(self, email: str) -> str:
        """Create a session ID and update it in the database."""
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new session ID
            session_id = _generate_uuid()
            # Update the user's session ID in the database
            self._db.update_user(user.id, session_id=session_id)

            return session_id

        except NoResultFound:
            # If no user is found with the provided email, return None
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Get user from session ID."""
        if session_id is None:
            # If the session ID is None, return None
            return None

        try:
            # Retrieve the user by session ID
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            # If no user is found with the provided session ID, return None
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy session for a given user."""
        # Update the user's session ID to None in the database
        self._db.update_user(user_id, session_id=None)
