from recipes.models.recipe import Recipe
from recipes.models import db

def test_recipe(client):
    chicken_soup = Recipe(name='chicken soup', servings=10, description="delicious")
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(chicken_soup)
    db.session.add(brisket)
    db.session.commit()

    recipes = Recipe.query.all()

    assert recipes[0].name == chicken_soup.name
    assert recipes[1].name == brisket.name