from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')

    app = Flask(__name__)
    config_class = config.factory(app_context if app_context else 'development')
    app.config.from_object(config_class)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.resource import compra_blueprint
    app.register_blueprint(compra_blueprint, url_prefix='/compras')
    
    @app.shell_context_processor
    def make_shell_context():
        return {"app": app, "db": db}

    return app
