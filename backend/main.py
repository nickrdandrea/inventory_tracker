from app import create_app, db
from app.models import Alert, Item, User, Vendor
from app.updater.updater import updater
from shelltools import test_data, test_upsert

app = create_app()

if __name__ == "__main__":
    app.run()
