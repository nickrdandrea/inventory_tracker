import os
import rq
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful import Api
from redis import Redis

from app.adapters.orm import init_db

jwt = JWTManager()
cors = CORS()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.db = init_db(app.config['SQLALCHEMY_DATABASE_URI'])
    jwt.init_app(app)
    cors.init_app(app)
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('tracker-tasks', connection=app.redis)
    api = Api(app)
    
    return app