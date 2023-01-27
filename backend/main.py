from app import create_app, db
from app.models import Alert, Item, User, Vendor
from app.updater.updater import updater
from app.db_utils import add_vendor, drop_records, search_item

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
            "db": db,
            "Item": Item, 
            "User": User, 
            "Vendor": Vendor,
            "add_vendor": add_vendor,
            "drop_records": drop_records,
            "search_item": search_item,
            "updater": updater
            }

if __name__ == "__main__":
    app.run()
