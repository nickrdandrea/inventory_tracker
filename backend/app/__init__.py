from flask import Flask
from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from redis import Redis
import rq


from config import Config
from app.adapters.orm import init_db

# migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    init_db()
    # migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('tracker-tasks', connection=app.redis)
    api = Api(app)
    
    return app