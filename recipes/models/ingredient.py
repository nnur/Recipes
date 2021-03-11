from recipes.models import db
from sqlalchemy.dialects.postgresql import JSON
from flask_restful import fields

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id', ondelete='CASCADE'), nullable=False)

    @staticmethod
    def fields():
        ingredients_fields = {
            'id': fields.String,
            'name': fields.String,
            'recipe_id': fields.Integer
        }

        return ingredients_fields

    def __repr__(self):
        return '<Ingredient %r>' % self.name