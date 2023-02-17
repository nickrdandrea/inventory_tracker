import os
from sqlalchemy.orm import registry, relationship, sessionmaker
from sqlalchemy import create_engine

def get_db_uri():
    driver = os.environ.get('DB_DRIVER')
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    name = os.environ.get('DB_NAME')
    return f"{driver}://{user}:{password}@{host}/{name}"

SQLALCHEMY_ENGINE = create_engine(get_db_uri())
SESSION_MAKER = sessionmaker(bind=SQLALCHEMY_ENGINE, expire_on_commit=False)
MAPPER_REGISTRY = registry()
MAPPER_REGISTRY.metadata.bind = SQLALCHEMY_ENGINE

def map_models():
    from app.models import Item, Vendor
    from app.adapters.orm.tables import items, vendors
    MAPPER_REGISTRY.map_imperatively(Item, items)
    MAPPER_REGISTRY.map_imperatively(Vendor, vendors, properties={
        "items": relationship(Item, backref="items")
    })

def init_db():
    MAPPER_REGISTRY.metadata.clear()
    map_models()
    MAPPER_REGISTRY.metadata.create_all()