from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime

from app.adapters.orm import mapper_registry
 
vendors = Table(
    "vendors",
    mapper_registry.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("url", String)
)

items = Table(
    "items",
    mapper_registry.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("description", String, unique=True),
    Column("category", String),
    Column("url", String),
    Column("status", String),
    Column("vendor_id", Integer, ForeignKey("vendors.id")),
    Column("last_seen", DateTime)
)