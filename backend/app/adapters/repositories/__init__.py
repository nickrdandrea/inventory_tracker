import abc

from app.adapters.orm import SESSION_MAKER

class SqlAlchemyRepository(abc.ABC):
    def __init__(self):
        self.sessionmaker = SESSION_MAKER
    
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
    
from app.adapters.repositories.vendor_repository import VendorRepository
