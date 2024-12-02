from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[1])
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod 
    def init_app(app):
        pass
        

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URI','postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto_ms')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}