#!/usr/bin/env python3
"""
Module to handle user's authentification
"""
import base64

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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception as e:
            return None
