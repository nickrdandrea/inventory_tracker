from typing import List

from app import db
from app.daos import CoreDao
from app.models import Item, Vendor

class VendorDao:
    @staticmethod
    def get_all() -> List[Item]:
        return Vendor.query.all()

    @staticmethod
    def add_vendor(vendor: Vendor):
        db.session.add(vendor)
        return CoreDao.safe_commit()
    