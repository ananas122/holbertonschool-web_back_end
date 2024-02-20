#!/usr/bin/env python3
"""Module for API authentication."""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path."""
        # Check if the path is None or excluded_paths is None or empty
        if path is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            # Make the comparison "slash tolerant" by ensuring both paths end with a/
            if path.rstrip("/") == excluded_path.rstrip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the Flask request.

        Args:
        request: The Flask request.

        Returns:
            str: The Authorization header from the request if present, 
            None otherwise.
        """
        if not request:
            return None
        return request.headers.get('Authorization')

