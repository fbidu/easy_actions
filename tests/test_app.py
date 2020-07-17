"""
Unit test for the main app
"""
from pytest import fixture
from easy_actions import App
from easy_actions.authenticators import BasicAuth


@fixture
def basic_auth():
    """
    basic_auth for testing
    """
    return BasicAuth(username="admin", password="test")


@fixture
def test_app():
    """
    app for testig
    """
    return App("test-app")


# pylint: disable=redefined-outer-name
def test_app_instantiation(test_app):
    """
    Simple test if instantion works
    """
    assert test_app
