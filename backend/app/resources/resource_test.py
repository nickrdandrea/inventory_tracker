#!/usr/bin/env python
from datetime import datetime, timedelta
import os
import unittest
import jwt
import requests
from app import create_app
from app import db
from app.models import User, Vendor
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ResourceCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.setup_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def setup_db(self):
        with self.app_context:
            user = User(name="Test User")
            user.set_password("testpassword123")
            vendor = Vendor(name="Test Vendor", url="testurl.com")
            db.session.add(user)
            db.session.add(vendor)
            db.session.commit()

    def test_register_post(self):
        registration_data = {
            "name": "Register Test User",
            "password": "testpassword456",
        }
        response = self.client.post("/register", json=registration_data)
        assert response.status_code == 201

    def test_login_post(self):
        response = self.client.post("/login", auth=("Test User", "testpassword123"))
        json = response.get_json()
        assert response.status_code == 200
        assert "token" in json.keys()

    def test_alert_get(self):
        response = self.client.get("/alerts")
        assert response.status_code == 200
        
    def test_alert_post(self):
        token = jwt.encode(
            {
                "id": str(1),
                "exp": datetime.utcnow() + timedelta(minutes=45),
            },
            os.getenv("SECRET_KEY"),
            "HS256",
        )
        alert_data = {"description": "Item test", "category": "Tests", "vendor_id": 1}
        header = {"x-access-tokens": token}
        response = self.client.post("/alerts", json=alert_data, headers=header)
        assert response.status_code == 201

    def test_vendor_get(self):
        response = self.client.get("/vendors")
        assert response.status_code == 200
        
    def test_vendor_post(self):
        token = jwt.encode(
            {
                "id": str(1),
                "exp": datetime.utcnow() + timedelta(minutes=45),
            },
            os.getenv("SECRET_KEY"),
            "HS256",
        )
        vendor_data = {"name": "Test POST Vendor", "url": "http://www.testvendor.com"}
        header = {"x-access-tokens": token}
        response = self.client.post("/vendors", json=vendor_data, headers=header)
        assert response.status_code == 201

    def test_items_get(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_item_post(self):
        token = jwt.encode(
            {
                "id": str(1),
                "exp": datetime.utcnow() + timedelta(minutes=45),
            },
            os.getenv("SECRET_KEY"),
            "HS256",
        )
        items_data = {
            "vendor": "Test Vendor",
            "items": [
                {"description": "Item test", "category": "Tests", "url": "testies.com"},
                {"description": "Item test2", "category": "Tests", "url": "testies.com"},
            ],
        }
        header = {"x-access-tokens": token}
        response = self.client.post("/", json=items_data, headers=header)
        assert response.status_code == 201