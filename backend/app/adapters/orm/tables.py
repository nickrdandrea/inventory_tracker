from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime

from app.adapters.orm import MAPPER_REGISTRY
 
vendors = Table(
    "vendors",
    MAPPER_REGISTRY.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("url", String)
)

items = Table(
    "items",
    MAPPER_REGISTRY.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("description", String, unique=True),
    Column("category", String),
    Column("url", String),
    Column("status", String),
    Column("vendor_id", Integer, ForeignKey("vendors.id")),
    Column("last_seen", DateTime)
)