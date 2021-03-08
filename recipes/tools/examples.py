from recipes.main import app, db
from recipes.models.recipe import Recipe
from recipes.models.ingredient import Ingredient

with app.app_context():
    recipe = Recipe(name='salad')
    ing = Ingredient(name='leaf', recipe=recipe)
    db.session.add(ing)
    db.session.commit()
    print(recipe)

