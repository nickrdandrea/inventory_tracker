from app.adapters.repositories.sqlalchemy_repository import SqlAlchemyRepository
from app.models import Item

class ItemRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(Item)

    def get_by_description(self, description):
        return self.get_by_attribute('description', description)