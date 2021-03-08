from recipes.models import db
from sqlalchemy.dialects.postgresql import JSON


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', backref=db.backref('ingredient', lazy=True))

    def __repr__(self):
        return '<Ingredient %r>' % self.name