from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import config
from app.config.config_cache import cache_config
from flask_caching import Cache
import os

db = SQLAlchemy()
cache = Cache()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config['development']
    app.config.from_object(configuration)
    
    db.init_app(app)
    cache.init_app(app, config=cache_config)

    with app.app_context():
        from app.resource import producto_blueprint
        app.register_blueprint(producto_blueprint)

    return app