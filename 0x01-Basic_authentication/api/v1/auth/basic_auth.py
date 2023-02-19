#!/usr/bin/env python3
"""
Module to handle user's authentification
"""
from .auth import Auth


class BasicAuth(Auth):
    """Class to handle basic authentification"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract authorization header"""
        if authorization_header is None or \
                type(authorization_header) != str or \
                not authorization_header.startswith('Basic'):
            return None
        auth_details = authorization_header.split()
        if len(auth_details) > 1:
            return auth_details[1]
