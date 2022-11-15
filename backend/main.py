from app import create_app, db
from app.models import Alert, Item, User, Vendor
from app.updater.updater import updater
from shelltools import test_data, test_upsert
from app.db_utils import add_vendor, drop_records, search_item

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
            "db": db,
            "Item": Item, 
            "User": User, 
            "Vendor": Vendor,
            "test_data": test_data,
            "test_upsert": test_upsert,
            "add_vendor": add_vendor,
            "drop_records": drop_records,
            "search_item": search_item
            }

if __name__ == "__main__":
    app.run()
