from recipes.models.recipe import Recipe
from recipes.models import db
import json

def test_recipe_get_all(client):
    chicken_soup = Recipe(name='chicken soup', servings=10, description="delicious")
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(chicken_soup)
    db.session.add(brisket)
    db.session.commit()

    response = client.get("/recipes")
    parsed_response = json.loads(response.data)
    assert parsed_response[0]['name'] == chicken_soup.name
    assert parsed_response[1]['name'] == brisket.name

def test_recipe_get(client):
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(brisket)
    db.session.commit()

    response = client.get(f"/recipes/{brisket.id}")
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == brisket.name

def test_recipe_delete(client):
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(brisket)
    db.session.commit()

    response = client.delete(f"/recipes/{brisket.id}")
    assert response.status_code == 204

def test_recipe_put(client):
    brisket = Recipe(name='brisket', description="smoky flavours")
    db.session.add(brisket)
    db.session.commit()

    body = {
        "name": "dog beef", 
        "servings": 3
    }

    response = client.put(f"/recipes/{brisket.id}", data=json.dumps(body), content_type='application/json')
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == body['name']
    assert parsed_response['servings'] == body['servings']
    assert parsed_response['description'] == brisket.description


def test_recipe_post(client):
    body = {
        "name": "dog beef", 
        "servings": 3
    }
    response = client.post("/recipes", data=json.dumps(body), content_type='application/json')
    parsed_response = json.loads(response.data)
    assert parsed_response['name'] == body['name']
    assert parsed_response['servings'] == body['servings']