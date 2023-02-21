from app.adapters.repositories.sqlalchemy import SqlAlchemyRepository
from app.models import Item

class ItemRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(Item)

    def get_by_description(self, description):
        result = self.get_by_attribute('description', description)
        if result:
            return result[0]
        return None