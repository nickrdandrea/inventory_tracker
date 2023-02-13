from typing import Optional
from datetime import date

class Vendor:
    def __init__(self, name: str, url: str, id = None):
        self.id = id
        self.name = name
        self.url = url
        self._items = set() #type: Set[Item]

