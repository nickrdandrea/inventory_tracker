import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import select, insert, delete

from app.adapters.orm import SQLALCHEMYENGINE
from app.models import Vendor

class SqlAlchemyUnitOfWork():
    def __init__(self):
        pass

class SqlAlchemyRepository(abc.ABC):
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=SQLALCHEMYENGINE)
    
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, model):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, model, id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, model):
        raise NotImplementedError

class VendorRepository(SqlAlchemyRepository):
    def add(self, vendor: Vendor):
        with self.sessionmaker() as session:
            session.add(vendor)
            session.commit()
    
    def get(self, vendor_name: str):
        with self.sessionmaker() as session:
            vendor = session.execute(
                select(Vendor).where(Vendor.name == vendor_name)
            ).first()[0]
        return vendor
    
    def get_all(self):
        with self.sessionmaker() as session:
            vendors = session.execute(
                select(Vendor)
            ).all()
        return vendors

    def update(self, vendor, id):
        pass

    def delete(self, vendor_id):
        with self.sessionmaker() as session:
            session.execute(
                delete(Vendor).
                where(Vendor.id == vendor_id)
            )