from sqlalchemy import select, delete, update
from typing import Any, Dict, List, Optional

from app.models import BaseModel
from app.adapters.orm import SESSION_MAKER
from app.adapters.repositories import AbstractRepository

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, model: BaseModel):
        self.sessionmaker = SESSION_MAKER
        self.model = model
    
    def add(self, model_instance: BaseModel) -> None:
        if not isinstance(model_instance, self.model):
            raise ValueError(f"Model instance is invalid")
        with self.sessionmaker() as session:
            session.add(model_instance)
            session.commit()
    
    def get(self) -> List[BaseModel]:
        with self.sessionmaker() as session:
            results = session.scalars(
                select(self.model)
            ).all()
        return results    
    
    def get_by_attribute(self, attribute_name: str, attribute_value: Any) -> List[BaseModel]:
        if not hasattr(self.model, attribute_name):
            raise ValueError(f"{self.model.__class__.__name__} does not have attribute {attribute_name}")
        with self.sessionmaker() as session:
            results = session.scalars(
                select(self.model).where(getattr(self.model, attribute_name) == attribute_value)
            ).all()
        return results

    def get_by_id(self, model_instance_id: int) -> Optional[BaseModel]:
        result = self.get_by_attribute('id', model_instance_id)
        if result:
            return result[0]
        return None
    
    def update(self, model_instance_id: int, updated_values: Dict[str, Any]) -> None:
        with self.sessionmaker() as session:
            result = session.execute(
                select(self.model).where(self.model.id == model_instance_id)
            ).first()
            if result is None:
                raise ValueError("Model instance not found")
            session.execute(
                update(self.model).
                where(self.model.id == model_instance_id).
                values(updated_values)
            )
            session.commit()

    def delete(self, model_instance_id: int) -> None:
        with self.sessionmaker() as session:
            result = session.execute(
                select(self.model).where(self.model.id == model_instance_id)
            ).first()
            if result is None:
                raise ValueError("Model instance not found")
            session.execute(
                delete(self.model).
                where(self.model.id == model_instance_id)
            )
            session.commit()