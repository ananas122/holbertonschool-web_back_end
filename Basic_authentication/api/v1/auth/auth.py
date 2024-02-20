#!/usr/bin/env python3
"""Module for API authentication."""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class for managing API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        for excluded_path in excluded_paths:
            # Check if the given path is=excludedpath or it starts with
            if path == excluded_path or path.startswith(excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        return None
