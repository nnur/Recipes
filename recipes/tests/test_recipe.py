from recipes.models.recipe import Recipe
from recipes.models import db
import json

def test_recipe(client):
    chicken_soup = Recipe(name='chicken soup', servings=10, description="delicious")
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(chicken_soup)
    db.session.add(brisket)
    db.session.commit()

    response = client.get("/recipes")
    parsed_response = json.loads(response.data)
    assert parsed_response[0]['name'] == chicken_soup.name
    assert parsed_response[1]['name'] == brisket.name