from app.adapters.repositories.sqlalchemy_repository import SqlAlchemyRepository
from app.models import Vendor

class VendorRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(Vendor)

    def get_by_name(self, name):
        return self.get_by_attribute('name', name)