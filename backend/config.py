import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Heroku environmental variable workaround
# database_url = os.environ.get('DATABASE_URI')
# if database_url is not None:
#     if database_url.startswith("postgres://"):
#         database_url.replace("postgres://", "postgresql://", 1)
#         os.environ['DATABASE_URI'] = database_url

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
