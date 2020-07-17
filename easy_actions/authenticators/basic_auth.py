"""
Module for a HTTP Basic Auth
"""


# pylint: disable=too-few-public-methods
class BasicAuth:
    """
    Implements an HTTP-Basic auth
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
