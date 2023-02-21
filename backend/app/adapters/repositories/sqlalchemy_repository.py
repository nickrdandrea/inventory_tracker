from sqlalchemy import select, delete, update

from app.adapters.orm import SESSION_MAKER
from app.adapters.repositories import AbstractRepository

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, model):
        self.sessionmaker = SESSION_MAKER
        self.model = model
    
    def add(self, model_instance):
        with self.sessionmaker() as session:
            session.add(model_instance)
            session.commit()
    
    def get(self):
        with self.sessionmaker() as session:
            results = session.execute(
                select(self.model)
            ).all()
        return results

    def get_by_id(self, model_instance_id):
        with self.sessionmaker() as session:
            result = session.execute(
                select(self.model).where(self.model.id == model_instance_id)
            ).first()
        if result != None:
            return result[0]
        return None
        
    def get_by_attribute(self, attribute_name, attribute_value):
        with self.sessionmaker() as session:
            result = session.execute(
                select(self.model).where(getattr(self.model, attribute_name) == attribute_value)
            ).first()
        if result is not None:
            return result[0]
        return None

    def update(self, model_instance_id, updated_values):       
        with self.sessionmaker() as session:
            session.execute(
                update(self.model).
                where(self.model.id == model_instance_id).
                values(updated_values)
            )
            session.commit()

    def delete(self, model_instance_id):
        with self.sessionmaker() as session:
            session.execute(
                delete(self.model).
                where(self.model.id == model_instance_id)
            )
            session.commit()