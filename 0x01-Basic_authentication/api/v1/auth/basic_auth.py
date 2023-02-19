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
        if type(user_email) == str and type(user_pwd) == str:
            obj = {'email': user_email}
            users = User.search(obj)
            if users:
                if users[0].is_valid_password(user_pwd):
                    return users[0]
                return None
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
