from typing import Optional
from datetime import date

class Item:
    def __init__(self, id: int, name: str, cat: str, url: str, status:str, vendor_id: int, last_seen: Optional[date]):
        self.id = id
        self.name = name
        self.category = cat
        self.url = url
        self.status = status
        self.vendor_id = vendor_id
        self.last_seen = last_seen

