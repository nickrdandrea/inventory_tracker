import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model_instance):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, model_instance):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, model_instance, model_instance_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, model_instance):
        raise NotImplementedError

from app.adapters.repositories.vendor_repository import VendorRepository
from app.adapters.repositories.item_repository import ItemRepository
