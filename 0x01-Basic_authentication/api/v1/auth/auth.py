#!/usr/bin/env python3
"""
Module to handle user's authentification
"""
import re
from typing import List, TypeVar


class Auth:
    """Class to handle authentification"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if the path is not in \
            the list of strings excluded_paths """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """intercept authorization header"""
        if request is None:
            return None
        authorization = request.headers.get('Authorization', None)
        print(authorization, 55555555555)
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user"""
        return None
