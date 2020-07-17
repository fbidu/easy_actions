"""
Unit test for the basic auth
"""
from easy_actions.authenticators import BasicAuth


def test_initialize():
    """
    Can we initialize an basic auth instance?
    """
    basic_auth = BasicAuth(username="test", password="test")

    assert basic_auth
