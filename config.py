import os
from os.path import join, dirname

from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config(object):
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI  = os.environ.get('DATABASE')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:metallica1@localhost/test_db'
    DEBUG = True
    JWT_SECRET_KEY = 'Test'

class ProductionConfig(Config):
    
    DEBUG = False
    


config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "test":Testing
}