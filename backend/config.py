import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def get_db_uri(driver=None, host=None, user=None, password=None, db_name=None):
    driver = driver or os.environ.get('DB_DRIVER')
    host = host or os.environ.get('DB_HOST')
    user = user or os.environ.get('DB_USER')
    password = password or os.environ.get('DB_PASS')
    db_name = db_name or os.environ.get('DB_NAME')
    return f"{driver}://{user}:{password}@{host}/{db_name}"

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fallback.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://'
    SECRET_KEY = 'you-will-never-guess'
    CORS_HEADERS = 'Content-Type'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_uri()

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_name=os.environ.get('TEST_DB_NAME'))

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_uri()
    REDIS_URL = os.environ.get('REDIS_URL')

config_options = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

CONFIG = config_options[os.environ.get('FLASK_ENV', 'default')]

