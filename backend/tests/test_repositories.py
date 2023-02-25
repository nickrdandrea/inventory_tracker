import pytest

from app.models import Vendor, Item
from app.adapters.repositories import VendorRepository
from tests import app, client

@pytest.fixture()
def reset_db(app):
    app.db.mapper_registry.metadata.create_all()

    yield

    app.db.mapper_registry.metadata.drop_all()

@pytest.fixture(scope="class")
def vendor_repo(app):
    return VendorRepository(app.db)

@pytest.mark.usefixtures("app", "client", "reset_db", "vendor_repo")
class TestVendorRepository:
    def test_vendor_repo_get(self, app, reset_db, vendor_repo):
        test_vendor1 = Vendor(name="gettest1", url="testurl.com")
        test_vendor2 = Vendor(name="gettest2", url="testurl.com")
        with app.db.session_factory() as session:
            session.add(test_vendor1)
            session.add(test_vendor2)
            session.commit()
    
        allVendors = vendor_repo.get()
        assert len(allVendors) == 2, "Get error."
        vendor = vendor_repo.get_by_name(test_vendor1.name)
        assert vendor.name == test_vendor1.name, "Get by name error."
        vendor = vendor_repo.get_by_id(2)
        assert vendor.name == test_vendor2.name, "Get by id error."
    
    def test_vendor_repo_add(self, reset_db, vendor_repo):
        vendor = Vendor(name="addtest", url="testurl.com")
        vendor_repo.add(vendor)
        assert vendor_repo.get_by_name(vendor.name) is not None
    
    def test_vendor_repo_update(self, reset_db, vendor_repo):
        vendor = Vendor(name="updatetest", url="testurl.com")
        vendor_repo.add(vendor)
        vendor_repo.update(vendor.id, {'name':'updatedtest'})
        assert vendor_repo.get_by_name('updatedtest') is not None
    
    def test_vendor_repo_delete(self, reset_db, vendor_repo):
        vendor = Vendor(name="deletetest", url="testurl.com")
        vendor_repo.add(vendor)
        vendor_repo.delete(vendor.id)
        assert vendor_repo.get_by_name('deletetest') is None

    def test_vendor_relationship(self, app, reset_db):
        vendor = Vendor(name="testV", url="lol")
        item = Item("testItem", "Tests", "oogoo.com", "out of stock", vendor_id=1)
        with app.db.session_factory() as session:
            session.add(vendor)
            vendor.items.append(item)
            session.commit()
        assert vendor.items[0].description == item.description
