import pytest
from recipes.models.ingredient import Ingredient
from recipes.models.recipe import Recipe
from recipes.models import db
import json

@pytest.fixture
def recipe():
    chicken_soup = Recipe(name='chicken soup', servings=10, description="delicious")
    db.session.add(chicken_soup)
    db.session.commit()
    return chicken_soup

def test_ingredient_get_all(client, recipe):
    carrot = Ingredient(name='carrot', recipe_id=recipe.id)
    garlic = Ingredient(name='garlic', recipe_id=recipe.id)
    db.session.add(carrot)
    db.session.add(garlic)
    db.session.commit()

    response = client.get("/ingredients")
    parsed_response = json.loads(response.data)
    assert parsed_response[0]['name'] == carrot.name
    assert parsed_response[1]['name'] == garlic.name

def test_ingredient_get(client, recipe):
    garlic = Ingredient(name='garlic', recipe_id=recipe.id)
    db.session.add(garlic)
    db.session.commit()

    response = client.get(f"/ingredients/{garlic.id}")
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == garlic.name

def test_ingredient_delete(client, recipe):
    garlic = Ingredient(name='garlic', recipe_id=recipe.id)
    db.session.add(garlic)
    db.session.commit()

    response = client.delete(f"/ingredients/{garlic.id}")
    assert response.status_code == 204

def test_ingredient_put(client, recipe):
    garlic = Ingredient(name='garlic', recipe_id=recipe.id)
    db.session.add(garlic)
    db.session.commit()

    body = {
        "name": "celery", 
    }

    response = client.put(f"/ingredients/{garlic.id}", data=json.dumps(body), content_type='application/json')
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == body['name']


def test_ingredient_post(client, recipe):
    body = {
        "name": "dog beef", 
        "recipe_id": recipe.id
    }
    response = client.post("/ingredients", data=json.dumps(body), content_type='application/json')
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == body['name']
    assert parsed_response['recipe_id'] == body['recipe_id']