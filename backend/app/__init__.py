from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from config import Config
from app.db import db, populate_db
from app.resources import ItemResource, LoginResource, RegisterResource, VendorResource, AlertResource


login = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    db.create_all(app=app)
    populate_db(app)
    login.init_app(app)

    api = Api(app)
    api.add_resource(ItemResource, "/")
    api.add_resource(VendorResource, "/vendors")
    api.add_resource(LoginResource, "/login")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(AlertResource, "/alerts")

    return app