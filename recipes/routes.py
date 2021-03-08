from flask_restful import Resource, fields, marshal_with
from recipes.models.recipe import Recipe
from recipes.models.ingredient import Ingredient


class HelloWorld(Resource):
    def get(self):
        return 'hello world!'

recipes_fields = {
    'id': fields.String,
    'servings': fields.Integer,
    'name': fields.String,
    'description': fields.String
}

class Recipes(Resource):
    @marshal_with(recipes_fields)
    def get(self):
        recipes = Recipe.query.all()
        return recipes
