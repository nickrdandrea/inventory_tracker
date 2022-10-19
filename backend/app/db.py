from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models import User, Vendor
import os
from sqlalchemy.exc import IntegrityError

NAME = os.environ.get('UPDATER_NAME')
PASSWORD = os.environ.get('UPDATER_PASSWORD')
REQUEST_URL = os.environ.get('REQUEST_URL')
VENDOR = "The Toy Trove"
VENDOR_URL = "https://thetoytrove.crystalcommerce.com"

def populate_db(app):
    try:
        with app.app_context():
            new_user = User(name=NAME)
            new_user.set_password(PASSWORD)
            db.session.add(new_user)
            vendor = Vendor(name=NAME, url=VENDOR_URL)
            db.session.add(vendor)
            db.session.commit()
    except IntegrityError:
        pass
    