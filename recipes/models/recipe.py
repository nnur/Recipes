from recipes.models import db
from sqlalchemy.dialects.postgresql import JSON


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servings = db.Column(db.Integer(), default=1)
    name = db.Column(db.String(200))
    description = db.Column(db.String())

    def __repr__(self):
        return '<Recipe %r>' % self.name