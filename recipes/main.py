from recipes.app import create_app


app = create_app()

# Models
from recipes.models.recipe import Recipe
from recipes.models.ingredient import Ingredient


@app.route('/')
def hello_world():
    return 'Hello, World!'