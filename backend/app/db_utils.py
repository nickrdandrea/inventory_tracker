from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import Alert, Item, User, Vendor
from app.schemas import ItemSchema


def safe_commit():
    try:
        db.session.commit()
        return True
    except SQLAlchemyError as error:
        db.session.rollback()
        return False

def search_item(expression):
    items = Item.query.filter(
                Item.__ts_vector__.match(expression, postgresql_reqconfig='english')
            ).all()
    return items

def add_vendor(name = "Test Vendor", url = "testurl.com"):
    vendor = Vendor(name = name, url = url)
    db.session.add(vendor)
    safe_commit()
    return vendor

def drop_records(table: db.Model):
    if not issubclass(table, db.Model):
        raise TypeError(f"{table} is not a Model.")
    table.query.delete()
    return safe_commit()

def upsert_item(items: list[Item], vendor: Vendor):
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
        return True
    except IntegrityError as e:
        return False