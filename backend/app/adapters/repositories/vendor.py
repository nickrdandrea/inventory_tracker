from typing import Optional

from app.adapters.repositories.sqlalchemy import SqlAlchemyRepository
from app.models import Vendor

class VendorRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(Vendor)

    def get_by_name(self, name: str) -> Optional[Vendor]:
        result = self.get_by_attribute('name', name)
        if result:
            return result[0]
        return None