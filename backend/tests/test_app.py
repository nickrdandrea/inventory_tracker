import pytest
import os
from app import create_app
from app.models import Vendor
from app.adapters.orm import SQLALCHEMYENGINE, mapper_registry
from app.adapters.repositories.repository import VendorRepository
from config import Config

# Config.SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
# Config.TESTING = True

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

@pytest.fixture()
def reset_db(app):
    mapper_registry.metadata.bind = SQLALCHEMYENGINE 
    mapper_registry.metadata.drop_all()
    mapper_registry.metadata.create_all()

def test_vendor_repo(client, reset_db):
    vendor_repo = VendorRepository()
    vendor = Vendor(name="testvendor", url="testurll.com")
    vendor_repo.add(vendor)
    getVendor = vendor_repo.get(vendor_name="testvendor")
    assert getVendor.name == "testvendor", "Add/Get error."
    
    vendor_repo.add(vendor)
    allVendors = vendor_repo.get_all()
    assert len(allVendors) == 1, "Unique vendor name error."
    
    vendor1 = Vendor(name="testvendor1", url="testurll.com")
    vendor2 = Vendor(name="testvendor2", url="testurll.com")
    vendor3 = Vendor(name="testvendor3", url="testurll.com")
    vendor_repo.add(vendor1)
    vendor_repo.add(vendor2)
    vendor_repo.add(vendor3)
    allVendors = vendor_repo.get_all()
    assert len(allVendors) == 4, "Get all error."

    vendor = vendor_repo.get(vendor_name="testvendor2")
    vendor_repo.delete(vendor.id)
    print(vendor_repo.get_all()[0].name)
    for v in vendor_repo.get_all():
        assert v.name != "testvendor2", "Delete error."

# def test_get_item(client):
#     response = client.get("/")
#     assert response.status_code == 200