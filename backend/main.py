from app import create_app, db
from app.models import Alert, Item, User, Vendor
from app.updater.updater import updater
from shelltools import test_data, test_upsert

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
            "db": db, 
            "Alert": Alert, 
            "Item": Item, 
            "User": User, 
            "Vendor": Vendor,
            "test_data": test_data,
            "test_upsert": test_upsert,
            "updater": updater
            }

if __name__ == "__main__":
    app.run()
