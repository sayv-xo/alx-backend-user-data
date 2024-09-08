#!/usr/bin/env python3
"""Authentication module for API
"""
from flask import request
from typing import TypeVar, List
import os


class Auth:
    """API authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Define authorized and excluded paths

        Args:
            path: a path to access
            excluded_path: list of excluded paths

        Returns:
            False if path is in excluded_path else True
        """
        if path is None or not excluded_paths:
            return True

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            if excluded.startswith(path):
                return False
            if path.startswith(excluded):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Defines authorization header

        Args:
            request: Flask request object

        Returns:
            None
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Defines the current user

        Args:
            request: Flask request object

        Returns:
            None
        """
        return None

    def session_cookie(self, request=None):
        """Return a cookie value from request
        Args:
            request: Flask request object
        Returns a cookie value
        """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
