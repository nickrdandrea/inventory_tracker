import pytest

from config import TestingConfig
from app.api import create_app

@pytest.fixture(scope="class")
def app():
    app = create_app(config=TestingConfig)
    return app

@pytest.fixture(scope="class")
def client(app):
    return app.test_client()

