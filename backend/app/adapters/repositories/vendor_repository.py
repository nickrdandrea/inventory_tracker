from sqlalchemy import select, delete, update

from app.adapters.repositories import SqlAlchemyRepository
from app.models import Vendor

class VendorRepository(SqlAlchemyRepository):
    def add(self, vendor: Vendor):
        with self.sessionmaker() as session:
            session.add(vendor)
            session.commit()
    
    def get(self):
        with self.sessionmaker() as session:
            vendors = session.execute(
                select(Vendor)
            ).all()
        return vendors
    
    def get_by_name(self, vendor_name):
        with self.sessionmaker() as session:
            vendor = session.execute(
                select(Vendor).where(Vendor.name == vendor_name)
            ).first()
        if vendor != None:
            return vendor[0]
        else:
            return None

    def get_by_id(self, vendor_id: int):
        with self.sessionmaker() as session:
            vendor = session.execute(
                select(Vendor).where(Vendor.id == vendor_id)
            ).first()
        if vendor != None:
            return vendor[0]
        else:
            return None

    def update(self, vendor_id, updated_values):       
        with self.sessionmaker() as session:
            session.execute(
                update(Vendor).
                where(Vendor.id == vendor_id).
                values(updated_values)
            )
            session.commit()

    def delete(self, vendor_id):
        with self.sessionmaker() as session:
            session.execute(
                delete(Vendor).
                where(Vendor.id == vendor_id)
            )
            session.commit()