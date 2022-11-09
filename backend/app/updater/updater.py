from app import create_app
from app.db_utils import upsert_item
from app.models import Item, Vendor
from app.schemas import ItemSchema

from app.updater.sources.thetoytrove_preorder import TheToyTrovePreorderScraper

app = create_app()
app.app_context().push()

def update_source(source):
    raw_items = source.get_items()
    schema = ItemSchema()
    items = map(schema.load, raw_items)
    vendor = Vendor.query.where(Vendor.name == source.NAME).first()
    upsert_item(items, vendor)

class Updater():
    def __init__(self):
        self.sources = []

    def run(self):
        for source in self.sources:
            job = app.task_queue.enqueue(update_source, source)
    
    def add_source(self, source):
        self.sources.append(source)
    
    def remove_source(self, source):
        self.sources.pop(source)

updater = Updater()
updater.add_source(TheToyTrovePreorderScraper)