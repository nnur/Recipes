from flask import Flask
from recipes.config import load_config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    load_config(app)

    from recipes.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    return app