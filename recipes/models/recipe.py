from recipes.models import db
from sqlalchemy.dialects.postgresql import JSON
from flask_restful import fields

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servings = db.Column(db.Integer(), default=1)
    name = db.Column(db.String(200))
    description = db.Column(db.String())
    ingredients = db.relationship("Ingredient", cascade="all,delete", backref="recipe")

    def __repr__(self):
        return '<Recipe %r>' % self.name

    @staticmethod
    def fields():
        recipes_fields = {
            'id': fields.String,
            'servings': fields.Integer,
            'name': fields.String,
            'description': fields.String
        }

        return recipes_fields