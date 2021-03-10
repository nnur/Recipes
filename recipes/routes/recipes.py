from flask import request, jsonify
from flask_restful import Resource, fields, marshal_with, reqparse
from recipes.models import db
from recipes.models.recipe import Recipe


class HelloWorld(Resource):
    def get(self):
        return 'Hello world!'

class Recipes(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('servings', type = int, location = 'json')

    @marshal_with(Recipe.fields())
    def get(self, id=None):
        if id is None:
            recipes = Recipe.query.all()
            return recipes
        
        recipe = Recipe.query.get(id)
        return recipe, 200

    @marshal_with(Recipe.fields())
    def post(self):
        args = self.reqparse.parse_args()
        recipe = Recipe(
            name=args["name"], 
            servings=args["servings"], 
            description=args["description"]
        )
        db.session.add(recipe)
        db.session.commit()
        return recipe, 201

    @marshal_with(Recipe.fields())
    def put(self, id):
        recipe = Recipe.query.get(id)
        args = self.reqparse.parse_args()

        for key, value in args.items():
            setattr(recipe, key, value)

        db.session.commit()
        return recipe, 200

    @marshal_with(Recipe.fields())
    def delete(self, id):
        Recipe.query.filter_by(id = id).delete()
        db.session.commit()
        return {}, 204
