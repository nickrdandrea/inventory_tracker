from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import Alert, Item, User, Vendor
from app.schemas import ItemSchema

def upsert_item(items: Item, vendor: Vendor):
    upsert_values = []
    for item in items:
        item_values = ItemSchema(exclude=["id", "date_created"]).dump(item)
        item_values["vendor_id"] = vendor.id
        upsert_values.append(item_values)
    
    insert_stmt = insert(Item)
    upsert_stmt = insert_stmt.on_conflict_do_update(
        constraint = '_description_vendor_id_uc',
        set_ =  { "last_updated": db.func.now() }
    )

    try:
        db.session.execute(upsert_stmt, upsert_values)
        db.session.commit()
    except IntegrityError as e:
        abort(500, message="Unexpected Error!")