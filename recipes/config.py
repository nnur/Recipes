import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
from recipes.constants import ENVIRONMENTS

basedir = abspath(dirname(__file__))


class Config(object):
    ENV = os.environ['ENV']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']


def load_config(app):
    app.config.from_object(f"recipes.config.Config")
    print(app.config['ENV'])
    