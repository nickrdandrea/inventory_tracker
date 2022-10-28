from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

migrate = Migrate()
jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    migrate.init_app(app, db)
    db.init_app(app)
    # db.create_all(app=app)
    # populate_db(app)
    jwt.init_app(app)

    from app.resources import ItemResource, LoginResource, RegisterResource, VendorResource, AlertResource

    api = Api(app)
    api.add_resource(ItemResource, "/")
    api.add_resource(VendorResource, "/vendors")
    api.add_resource(LoginResource, "/login")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(AlertResource, "/alerts")

    return app