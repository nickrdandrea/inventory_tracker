from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import registry, relationship, sessionmaker


from app.models import Item, Vendor

class Database:
    _instance = None

    def __new__(cls, db_uri):
        if cls._instance is None:
            engine = create_engine(db_uri)
            session_factory = sessionmaker(bind=engine, expire_on_commit=False)
            mapper_registry = registry()
            mapper_registry.metadata.bind = engine
            cls._instance = super().__new__(cls)
            cls._instance.engine = engine
            cls._instance.session_factory = session_factory
            cls._instance.mapper_registry = mapper_registry
            cls._instance.metadata = mapper_registry.metadata
        return cls._instance
    
def create_tables(metadata):
    return {
        'vendors' : Table(
            "vendors",
            metadata,
            Column("id", Integer, autoincrement=True, primary_key=True),
            Column("name", String, unique=True, nullable=False),
            Column("url", String)
        ),
        'items' : Table(
            "items",
            metadata,
            Column("id", Integer, autoincrement=True, primary_key=True),
            Column("description", String, unique=True),
            Column("category", String),
            Column("url", String),
            Column("status", String),
            Column("vendor_id", Integer, ForeignKey("vendors.id")),
            Column("last_seen", DateTime)
        )
    }
        
def map_models(registry, tables):
    registry.map_imperatively(Item, tables['items'])
    registry.map_imperatively(Vendor, tables['vendors'], properties={
        "items": relationship(Item, backref="items")
    })

def init_db(db_uri):
    db = Database(db_uri)
    tables = create_tables(db.metadata)
    map_models(db.mapper_registry, tables)
    db.metadata.create_all()
    return db
