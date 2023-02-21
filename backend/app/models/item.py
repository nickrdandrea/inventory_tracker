from app.models import BaseModel

class Item(BaseModel):
    def __init__(self, 
                 description: str, 
                 category: str, 
                 url: str, 
                 status:str, 
                 last_seen = None,
                 id = None,
                 vendor_id = None):
        self.id = id
        self.description = description
        self.category = category
        self.url = url
        self.status = status
        self.vendor_id = vendor_id
        self.last_seen = last_seen
    
    def set_vendor(self, vendor):
        self.vendor_id = vendor.id

    def __repr__(self):
        return f"Item Description: {self.description} ID: {self.id}"


