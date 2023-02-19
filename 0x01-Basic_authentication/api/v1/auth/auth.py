#!/usr/bin/env python3
"""
Module to handle user's authentification
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Class to handle authentification"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """intercept authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user"""
        return None
