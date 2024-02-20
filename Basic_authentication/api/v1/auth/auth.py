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

        # Iterate through the excluded paths
        for excluded_path in excluded_paths:
            # Check if the path is equal to an excluded path or if it starts with an excluded path
            if path == excluded_path or path.startswith(excluded_path):
                return False

        # Authentication is required for the given path
        return True


    def authorization_header(self, request=None) -> str:
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        return None
