from app.models import BaseModel

class Vendor(BaseModel):
    def __init__(self, name: str, url: str, id = None):
        self.id = id
        self.name = name
        self.url = url
        self._items = set() #type: Set[Item]
    
    def __repr__(self):
        return f"Vendor Name: {self.name} ID: {self.id}"

