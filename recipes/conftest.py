import os
import pytest
import sqlalchemy_utils
from recipes.main import create_app
from recipes.models import db

def _create_test_db():
    db_url = os.environ['DATABASE_URL']
    if not sqlalchemy_utils.database_exists(db_url):
        sqlalchemy_utils.create_database(db_url)

def _drop_test_db():
    db_url = os.environ['DATABASE_URL']
    if sqlalchemy_utils.database_exists(db_url):
        sqlalchemy_utils.drop_database(db_url)

@pytest.fixture
def client():
    _drop_test_db()
    _create_test_db()
    app = create_app()
    context = app.app_context()
    context.push()
    db.create_all()
    yield app
    _drop_test_db()
    context.pop()