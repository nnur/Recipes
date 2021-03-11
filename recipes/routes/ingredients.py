from flask import request, jsonify
from flask_restful import Resource, fields, marshal_with, reqparse
from recipes.models import db
from recipes.models.ingredient import Ingredient

class Ingredients(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, location = 'json')
        self.reqparse.add_argument('recipe_id', type = int, location = 'json')

    @marshal_with(Ingredient.fields())
    def get(self, id=None):
        if id is None:
            ingredients = Ingredient.query.all()
            return ingredients
        
        ingredient = Ingredient.query.get(id)
        return ingredient, 200

    @marshal_with(Ingredient.fields())
    def post(self):
        args = self.reqparse.parse_args()
        ingredient = Ingredient(
            name=args["name"], 
            recipe_id=args["recipe_id"]
        )
        db.session.add(ingredient)
        db.session.commit()
        return ingredient, 201

    @marshal_with(Ingredient.fields())
    def put(self, id):
        ingredient = Ingredient.query.get(id)
        args = self.reqparse.parse_args()

        for key, value in args.items():
            if value is not None: 
                setattr(ingredient, key, value)

        db.session.commit()
        return ingredient, 200

    @marshal_with(Ingredient.fields())
    def delete(self, id):
        Ingredient.query.filter_by(id = id).delete()
        db.session.commit()
        return {}, 204
