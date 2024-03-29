from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
import rq
from sqlalchemy.exc import OperationalError


from config import Config

migrate = Migrate()
jwt = JWTManager()
db = SQLAlchemy()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    migrate.init_app(app, db)
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('tracker-tasks', connection=app.redis)

    from old_app.resources import ItemResource, ItemsResource, SearchResource
    from old_app.resources import LoginResource, RegisterResource, AlertResource
    from old_app.resources import ProfileResource, LogoutResource
    from old_app.resources import VendorResource, VendorItemResource, VendorsResource

    api = Api(app)
    api.add_resource(ItemResource, "/<int:item_id>")
    api.add_resource(ItemsResource, "/")
    api.add_resource(VendorResource, "/<string:vendor_name>")
    api.add_resource(VendorsResource, "/vendors")
    api.add_resource(VendorItemResource, "/<string:vendor_name>/<int:item_id>")
    api.add_resource(LoginResource, "/login")
    api.add_resource(LogoutResource, "/logout")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(ProfileResource, "/profile")
    api.add_resource(AlertResource, "/alerts")
    api.add_resource(SearchResource, "/search")
    
    return app