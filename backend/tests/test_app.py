import pytest
import os
from app import create_app, db
from config import Config

Config.SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
Config.TESTING = True

@pytest.fixture()
def app():
    app = create_app()
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()

def test_get_item(client):
    response = client.get("/")
    assert response.status_code == 200