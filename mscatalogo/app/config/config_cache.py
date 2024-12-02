from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

cache_config={
    'CACHE_TYPE': 'RedisCache', 
    'CACHE_DEFAULT_TIMEOUT': 300, 
    'CACHE_REDIS_HOST': os.environ.get('REDIS_HOST','localhost'), 
    'CACHE_REDIS_PORT': os.environ.get('REDIS_PORT', 6379), 
    'CACHE_REDIS_DB': os.environ.get('REDIS_DB', 0), 
    'CACHE_REDIS_PASSWORD': os.environ.get('REDIS_PASSWORD','qwerty'), 
    'CACHE_KEY_PREFIX': 'flask_' 
}