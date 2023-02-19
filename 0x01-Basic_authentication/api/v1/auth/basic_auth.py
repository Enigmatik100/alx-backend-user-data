#!/usr/bin/env python3
"""
Module to handle user's authentification
"""
import base64
from typing import TypeVar
from models.user import User

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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """extract user's credentials"""
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) != str or \
                ':' not in decoded_base64_authorization_header:
            return None, None
        decoded = decoded_base64_authorization_header.split(':')
        return decoded[0], decoded[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """get current user's credentials """
        if user_email is None or user_pwd is None:
            return None

        obj = {'email': user_email}
        if not User.all():
            return None
        user = User.search(obj)
        if user:
            if user[0].is_valid_password(user_pwd):
                return user[0]
            return None
        return None
