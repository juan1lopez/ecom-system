
import os
from dotenv import load_dotenv
from pathlib import Path


basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URI','postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto_ms')
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('REDIS_DB')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

class TestingConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING= True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB_URI','postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto_ms')
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('REDIS_DB')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DB_URI','postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto_ms')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
