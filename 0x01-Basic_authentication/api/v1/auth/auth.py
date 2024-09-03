#!/usr/bin/env python3
"""Authentication module for API
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """API authentication class
    """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """Define authorized and excluded paths

        Args:
            path: a path to access
            excluded_path: list of excluded paths

        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Defines authorization header

        Args:
            request: Flask request object

        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Defines the current user

        Args:
            request: Flask request object

        Returns:
            None
        """
        return None
