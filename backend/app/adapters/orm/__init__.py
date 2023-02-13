import os
from sqlalchemy.orm import registry, relationship
from sqlalchemy import create_engine

mapper_registry = registry()

def map_models():
    from app.models import Item, Vendor
    from app.adapters.orm.tables import items, vendors
    mapper_registry.map_imperatively(Item, items)
    mapper_registry.map_imperatively(Vendor, vendors, properties={
        "items": relationship(Item, backref="items")
    })

def get_db_uri():
    driver = os.environ.get('DB_DRIVER')
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    name = os.environ.get('DB_NAME')
    return f"{driver}://{user}:{password}@{host}/{name}"

SQLALCHEMYENGINE = create_engine(get_db_uri())
    
def init_db():
    map_models()
    mapper_registry.metadata.create_all(SQLALCHEMYENGINE)