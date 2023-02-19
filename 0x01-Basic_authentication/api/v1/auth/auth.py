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
        if path is None:
            return True
        elif not excluded_paths:
            return True
        path = path + '/' if path != '' and path[-1] != '/' else path
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """intercept authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user"""
        return None
