import os
from main import app
from app.models import User, Vendor
from app import db

NAME = os.environ.get('UPDATER_NAME')
PASSWORD = os.environ.get('UPDATER_PASSWORD')
REQUEST_URL = os.environ.get('REQUEST_URL')
VENDOR = "The Toy Trove"
VENDOR_URL = "https://thetoytrove.crystalcommerce.com"

def init():
    with app.app_context():
        new_user = User(name=NAME)
        new_user.set_password(PASSWORD)
        db.session.add(new_user)
        vendor = Vendor(name=NAME, url=VENDOR_URL)
        db.session.add(vendor)
        db.session.commit()