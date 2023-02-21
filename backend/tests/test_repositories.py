import pytest

from app.models import Vendor, Item
from app.adapters.orm import MAPPER_REGISTRY, SESSION_MAKER
from app.adapters.repositories import VendorRepository
from tests import app, client

@pytest.fixture()
def reset_db():
    MAPPER_REGISTRY.metadata.create_all()

    yield

    MAPPER_REGISTRY.metadata.drop_all()

@pytest.mark.usefixtures("client", "reset_db")
class TestVendorRepository:
    vendor_repo = VendorRepository()

    def test_vendor_repo_get(self):
        test_vendor1 = Vendor(name="gettest1", url="testurl.com")
        test_vendor2 = Vendor(name="gettest2", url="testurl.com")
        with SESSION_MAKER() as session:
            session.add(test_vendor1)
            session.add(test_vendor2)
            session.commit()
    
        allVendors = self.vendor_repo.get()
        assert len(allVendors) == 2, "Get error."
        vendor = self.vendor_repo.get_by_name(test_vendor1.name)
        assert vendor.name == test_vendor1.name, "Get by name error."
        vendor = self.vendor_repo.get_by_id(2)
        assert vendor.name == test_vendor2.name, "Get by id error."
    
    def test_vendor_repo_add(self):
        vendor = Vendor(name="addtest", url="testurl.com")
        self.vendor_repo.add(vendor)
        assert self.vendor_repo.get_by_name(vendor.name) is not None
    
    def test_vendor_repo_update(self):
        vendor = Vendor(name="updatetest", url="testurl.com")
        self.vendor_repo.add(vendor)
        self.vendor_repo.update(vendor.id, {'name':'updatedtest'})
        assert self.vendor_repo.get_by_name('updatedtest') is not None
    
    def test_vendor_repo_delete(self):
        vendor = Vendor(name="deletetest", url="testurl.com")
        self.vendor_repo.add(vendor)
        self.vendor_repo.delete(vendor.id)
        assert self.vendor_repo.get_by_name('deletetest') is None

    def test_vendor_relationship(self):
        vendor = Vendor(name="testV", url="lol")
        item = Item("testItem", "Tests", "oogoo.com", "out of stock", vendor_id=1)
        with SESSION_MAKER() as session:
            session.add(vendor)
            vendor.items.append(item)
            session.commit()
        assert vendor.items[0].description == item.description
