from typing import List
from sqlalchemy.dialects.sqlite import insert

from app import db
from app.daos import CoreDao
from app.models import Item, Vendor
from app.schemas.item_schema import ItemSchema

class ItemDao:
    @staticmethod
    def get_all() -> List[Item]:
        return Item.query.all()

    @staticmethod
    def add_item(item: Item, vendor: Vendor):
        item.vendor_id = vendor.id
        db.session.add(item)
        return CoreDao.safe_commit()
    
    @staticmethod
    def upsert_item(item: Item, vendor: Vendor):
        insert_values = ItemSchema().dump(item)
        insert_values["vendor_id"] = vendor.id
        insert_stmt = insert(Item).values(insert_values)
        do_update_stmt = insert_stmt.on_conflict_do_update(
                index_elements=["UniqueConstraint"], set_={"last_updated": db.func.now()}
            )
        db.session.execute(do_update_stmt)
        return CoreDao.safe_commit()



