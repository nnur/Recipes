from flask import Flask
from recipes.config import load_config
from flask_migrate import Migrate
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    load_config(app)
    api = Api(app)

    from recipes.models import db
    from recipes.routes import HelloWorld, Recipes
    
    api.add_resource(HelloWorld, '/') 
    api.add_resource(Recipes, '/recipes') 

    db.init_app(app)
    migrate = Migrate(app, db)

    return app