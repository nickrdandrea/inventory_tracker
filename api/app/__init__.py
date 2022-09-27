from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

from app.resources import ItemResource, LoginResource, RegisterResource, VendorResource, AlertResource

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    db.create_all(app=app)

    api = Api(app)
    api.add_resource(ItemResource, "/")
    api.add_resource(VendorResource, "/vendors")
    api.add_resource(LoginResource, "/login")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(AlertResource, "/alerts")

    CORS(app)
    return app