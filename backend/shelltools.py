from app import db
from app.models import Item, Vendor
from app.daos import ItemDao, VendorDao
from app.db_utils import upsert_item

def test_data():
    item1 = Item(description='Test Item', category='Test', url='testurl.com')
    item2 = Item(description='Test Item2', category='Test2', url='testurl.com')
    item3 = Item(description='Test Item3', category='Test', url='testurl.com')
    item4 = Item(description='Test Item4', category='Test2', url='testurl.com')

    vendor1 = Vendor(name='Test Vendor', url='testurl.com')
    vendor2 = Vendor(name='Test Vendor2', url='testurl.com')

    VendorDao.add_vendor(vendor1)
    VendorDao.add_vendor(Vendor2)

    ItemDao.add_item(item1, vendor1)
    ItemDao.add_item(item2, vendor1)
    ItemDao.add_item(item3, vendor2)
    ItemDao.add_item(item4, vendor2)

    upsert_item(vendor1, item1)

    return

def test_upsert():
    vendors = Vendor.query.all()
    item1 = Item(description='Upsert Item3', category='Test', url='testurl.com')
    item2 = Item(description='Upsert Item4', category='Test2', url='testurl.com')

    items = [item1, item2]

    #ItemDao.add_item(item1, vendors[0])
    upsert_item(items, vendors[0])


